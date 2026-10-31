#!/usr/bin/env python3
"""Stage 1: match skills-lexicon entries to English Wikipedia articles, read-only. Python 3.9.
Usage: python3 -I match_entries.py --lexicon LEXICON_DIR --db DB_PATH --out OUT_DIR [--names "A,B,C"] [--limit N]
Writes OUT_DIR/matches.jsonl (one line per entry), candidates.jsonl (one per Wikipedia page), summary.json.
It never decides: it records every candidate page, how it matched, and flags that need a person."""
import argparse
import json
import os
import re
import sqlite3
import sys
import time
QUALIFIER = re.compile(r"\s*\([^)]*\)\s*$")
DISAMBIG = re.compile(r"\b(may|can) (also )?(refer|mean)\b|\bdisambiguation\b", re.I)
NEED = {
    "articles": ["page_id", "title", "rev_id", "rev_timestamp"],
    "redirects": ["from_title", "to_title", "to_page_id"],
    "passages": ["page_id", "section", "char_start", "text"],
}
HOW_RANK = {"title": 0, "redirect": 1, "title-minus-qualifier": 2, "redirect-minus-qualifier": 3}
def fail(code, msg):
    print("STOP: " + msg, file=sys.stderr)
    sys.exit(code)
def check_schema(con):
    for t, cols in NEED.items():
        have = [r[1] for r in con.execute('pragma table_info("%s")' % t)]
        if not have:
            fail(2, "table %s is missing; tables are %s" % (t, [r[0] for r in con.execute("select name from sqlite_master where type='table'")]))
        missing = [c for c in cols if c not in have]
        if missing:
            fail(2, "table %s lacks columns %s; it has %s" % (t, missing, have))
    idx = [r[1] for r in con.execute('pragma index_list("passages")')]
    first = [con.execute('pragma index_info("%s")' % i).fetchone() for i in idx]
    if not any(f and f[2] == "page_id" for f in first):
        fail(3, "passages has no index starting with page_id (indexes: %s); a lead lookup would scan 43 million rows" % idx)
def build_forms(lexicon, names):
    sys.path.insert(0, os.path.join(lexicon, "tools"))
    import lexicon as L
    entries, errs = L.load(os.path.join(lexicon, "entries"))
    if errs:
        fail(4, "lexicon errors: %s" % errs[:3])
    entries = [e for e in entries if e.get("status") != "deprecated"]
    if names:
        want = {L.norm(n) for n in names}
        entries = [e for e in entries if L.norm(e["preferred_name"]) in want]
    forms = {}
    for e in entries:
        for i, f in enumerate(L.forms(e)):
            forms.setdefault(L.norm(f["label"]), []).append((e["id"], f["label"], "preferred" if i == 0 else "variant"))
    return L, entries, forms
def lead_of(con, page_id):
    rows = con.execute("select text from passages where page_id = ? and section = '' order by char_start limit 3", (page_id,)).fetchall()
    return "\n".join(r[0] for r in rows if r[0])[:2500]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", required=True)
    ap.add_argument("--db", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--names", default="")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    t0 = time.time()
    if os.path.exists(os.path.join(a.out, "matches.jsonl")):
        fail(5, "%s already holds results; use a new --out folder" % a.out)
    con = sqlite3.connect("file:%s?mode=ro" % a.db, uri=True)
    check_schema(con)
    L, entries, forms = build_forms(a.lexicon, [n for n in a.names.split(",") if n])
    if a.limit:
        keep = {e["id"] for e in sorted(entries, key=lambda e: e["key"])[:a.limit]}
        forms = {k: [x for x in v if x[0] in keep] for k, v in forms.items()}
        forms = {k: v for k, v in forms.items() if v}
        entries = [e for e in entries if e["id"] in keep]
    print("entries %d, distinct normalised forms %d" % (len(entries), len(forms)), flush=True)
    def nrm(t):
        return L.norm(t.replace("_", " "))
    hits = {}      # entry id -> list of candidate dicts
    pages = {}     # page_id -> info
    n = 0
    for page_id, title, rev_id, rev_ts in con.execute("select page_id, title, rev_id, rev_timestamp from articles"):
        n += 1
        k1, k2 = nrm(title), nrm(QUALIFIER.sub("", title))
        for key, how in ((k1, "title"), (k2, "title-minus-qualifier")):
            if key in forms and (how == "title" or k2 != k1):
                pages[page_id] = {"page_id": page_id, "title": title, "rev_id": rev_id, "rev_timestamp": rev_ts}
                for eid, label, kind in forms[key]:
                    hits.setdefault(eid, []).append({"page_id": page_id, "title": title, "how": how, "form": label, "form_kind": kind})
    print("articles scanned %d (%.0fs)" % (n, time.time() - t0), flush=True)
    r = 0
    for from_title, to_title, to_page_id in con.execute("select from_title, to_title, to_page_id from redirects"):
        r += 1
        k1, k2 = nrm(from_title), nrm(QUALIFIER.sub("", from_title))
        for key, how in ((k1, "redirect"), (k2, "redirect-minus-qualifier")):
            if key in forms and (how == "redirect" or k2 != k1) and to_page_id:
                pages.setdefault(to_page_id, {"page_id": to_page_id, "title": to_title})
                for eid, label, kind in forms[key]:
                    hits.setdefault(eid, []).append({"page_id": to_page_id, "title": to_title, "how": how, "form": label, "form_kind": kind, "via": from_title})
    print("redirects scanned %d (%.0fs)" % (r, time.time() - t0), flush=True)
    for pid, p in pages.items():
        if "rev_id" not in p:
            row = con.execute("select title, rev_id, rev_timestamp from articles where page_id = ?", (pid,)).fetchone()
            if row:
                p["title"], p["rev_id"], p["rev_timestamp"] = row
        p["lead"] = lead_of(con, pid)
        p["disambiguation"] = bool(p["title"].endswith("(disambiguation)") or DISAMBIG.search(p["lead"][:300]))
    print("leads read for %d pages (%.0fs)" % (len(pages), time.time() - t0), flush=True)
    os.makedirs(a.out, exist_ok=True)
    tmp = os.path.join(a.out, ".tmp-")
    tiers = {"confident": 0, "needs-a-person": 0, "no-match": 0}
    with open(tmp + "matches.jsonl", "w", encoding="utf-8") as fm:
        for e in sorted(entries, key=lambda e: e["key"]):
            c = hits.get(e["id"], [])
            seen, uniq = set(), []
            for h in c:
                kk = (h["page_id"], h["how"], h["form"])
                if kk not in seen:
                    seen.add(kk)
                    uniq.append(h)
            uniq.sort(key=lambda h: (HOW_RANK[h["how"]], 0 if h["form_kind"] == "preferred" else 1))
            pids = {h["page_id"] for h in uniq}
            reasons = []
            if not uniq:
                tier = "no-match"
            else:
                if len(pids) > 1:
                    reasons.append("%d different pages" % len(pids))
                if any(pages[p]["disambiguation"] for p in pids):
                    reasons.append("a candidate is a disambiguation page")
                if not any(h["how"] in ("title", "redirect") for h in uniq):
                    reasons.append("matched only after dropping a qualifier in parentheses")
                tier = "needs-a-person" if reasons else "confident"
            tiers[tier] += 1
            fm.write(json.dumps({"entry_id": e["id"], "entry_key": e["key"], "preferred_name": e["preferred_name"], "tier": tier,
                                 "reasons": reasons, "candidates": uniq}, ensure_ascii=False) + "\n")
    with open(tmp + "candidates.jsonl", "w", encoding="utf-8") as fc:
        for pid in sorted(pages):
            fc.write(json.dumps(pages[pid], ensure_ascii=False) + "\n")
    summary = {"entries": len(entries), "tiers": tiers, "candidate_pages": len(pages), "articles_scanned": n, "redirects_scanned": r,
               "seconds": round(time.time() - t0), "db": a.db, "lexicon": a.lexicon}
    with open(tmp + "summary.json", "w") as fs:
        json.dump(summary, fs, indent=1)
    for name in ("matches.jsonl", "candidates.jsonl", "summary.json"):
        os.rename(tmp + name, os.path.join(a.out, name))
    print(json.dumps(summary))
if __name__ == "__main__":
    main()
