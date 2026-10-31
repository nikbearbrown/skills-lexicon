#!/usr/bin/env python3
"""Resolve Wikipedia match candidates into a relation per lexicon entry, using the page's categories. Python 3.9.

Usage: python3 -I resolve_matches.py --lexicon DIR --in DATA_DIR --out FILE
Reads matches.jsonl, candidates.jsonl, categories.jsonl (from match_entries.py and categories_for_pages.py) and the lexicon's
entries. Writes one JSON line per entry with a `relation`:
  same         the entry's own name is the page's title (or the title minus a parenthetical), and the categories fit the entry's kind
  related      the page is a redirect target or a broader page; use it as a link, not as the entry's description
  ambiguous    several pages remain; the top ones are listed for a person
  none         no usable page
A candidate is a suggestion with a reason, never a decision. Scores are shown so a person can see why."""
import argparse
import json
import os
import re
import sys

TECH = {"tool", "platform", "framework", "library", "programming-language", "markup-language", "style-language", "modeling-language", "standard"}
SOFT = re.compile(r"software|programming languages?|markup languages?|scripting languages?|query languages?|computing platforms?|cloud computing|"
                  r"application programming interface|web frameworks?|librar(y|ies)|databases?|operating systems?|file formats?|web (servers?|browsers?)|"
                  r"network protocols?|internet protocols?|\bapis?\b|open[- ]source|free software|source-available|mobile apps|web services|"
                  r"computer security|computer network|cryptograph|data (formats?|serialization)|machine learning|artificial intelligence|"
                  r"cloud services|microsoft|google|apple inc|adobe|oracle|\bibm\b|\bsap\b|enterprise (resource planning|software)|clients \(computing\)|computing terminology|"
                  r"software engineering|computing standards?|computer(-| )?(science|programming|hardware|file)|information technology|\bsql\b|\.net", re.I)
STRICT = {"framework", "library", "programming-language", "markup-language", "style-language", "modeling-language"}
LANG = re.compile(r"\blanguages?\b|\bdialects?\b", re.I)
PLANG = re.compile(r"programming|markup|scripting|query|modeling|modelling|stylesheet|computer", re.I)
CRED = re.compile(r"certif|credential|degrees?|diplomas?|licen[cs]|qualification|accredit|academic|professional (associations?|titles?)|"
                  r"nursing|medical (education|specialt)|examination|exams?|\bboards?\b|higher education|vocational|occupations?", re.I)
NOISE = re.compile(r"albums?|songs?|singles?|films?|television|surnames?|given names|\bships\b|\bbands\b|disambiguation|novels?|fictional|characters?|"
                   r"comics|video games?|football|villages?|populated places|municipalit|airports?|\bspecies\b|\bgenus\b|mythology|discograph|episodes|"
                   r"seasons|musical groups|people|births|deaths|\bports\b|railway|roller coasters|amusement|missiles?|vehicles|automobiles|"
                   r"companies (of|based)|football clubs|universities and colleges|educational institutions|buildings|streets|rivers|mountains|islands|"
                   r"given-name|place names", re.I)
QUAL_OK = {
    "tech": re.compile(r"software|program|language|framework|librar|database|computing|computer|operating system|service|platform|protocol|file format|web|"
                       r"standard|api|tool|engine|markup|scripting|query|hardware|algorithm|data|network|app|editor|ide\b|library|server|cloud|security", re.I),
    "human-language": re.compile(r"language|dialect", re.I),
    "credential": re.compile(r"certif|credential|degree|exam|licen|designation|qualification|diploma", re.I),
}
QUALIFIER = re.compile(r"\s*\(([^)]*)\)\s*$")
BASE = {"redirect-contains": 4.0, "exact-title": 5.0, "title-minus-qualifier": 4.0, "redirect": 2.0, "variant-title": 1.0, "variant-redirect": 0.5, "variant-qualifier": 0.5}


def kind_fits(kind, cats):
    text = " | ".join(cats)
    if kind in TECH:
        return bool(SOFT.search(text))
    if kind == "human-language":
        return any(LANG.search(c) and not PLANG.search(c) for c in cats)
    if kind == "credential":
        return bool(CRED.search(text))
    return None          # kinds without a category test (knowledge, skill, method, ability, work-activity)


def key(t):
    k = re.sub(r"[^a-z0-9]", "", t.lower())
    return k[:-1] if k.endswith("s") and len(k) > 4 else k


def qualifier_ok(kind, title):
    q = QUALIFIER.search(title)
    if not q:
        return True
    if kind in TECH:
        return bool(QUAL_OK["tech"].search(q.group(1)))
    if kind in ("human-language", "credential"):
        return bool(QUAL_OK[kind].search(q.group(1)))
    return False         # skills, knowledge, methods, abilities: a parenthetical page is not evidence the plain name means it


def basis_of(c, norm):
    pref = c["form_kind"] == "preferred"
    if c["how"] == "title":
        return "exact-title" if pref else "variant-title"
    if c["how"] == "title-minus-qualifier":
        return "title-minus-qualifier" if pref else "variant-qualifier"
    return "redirect" if pref else "variant-redirect"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", required=True)
    ap.add_argument("--in", dest="indir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    sys.path.insert(0, os.path.join(a.lexicon, "tools"))
    import lexicon as L
    entries, _ = L.load(os.path.join(a.lexicon, "entries"))
    E = {e["id"]: e for e in entries}
    cands, cats = {}, {}
    for l in open(os.path.join(a.indir, "candidates.jsonl"), encoding="utf-8"):
        d = json.loads(l); cands[d["page_id"]] = d
    for l in open(os.path.join(a.indir, "categories.jsonl"), encoding="utf-8"):
        d = json.loads(l); cats[d["page_id"]] = d.get("categories", [])
    out, tally = [], {}
    for line in open(os.path.join(a.indir, "matches.jsonl"), encoding="utf-8"):
        m = json.loads(line)
        e = E[m["entry_id"]]
        kind = e["kind"]
        if e.get("provenance", {}).get("source", "").startswith("imported from O*NET"):
            out.append({"entry_id": m["entry_id"], "entry_key": m["entry_key"], "preferred_name": m["preferred_name"], "kind": kind,
                        "relation": "none", "page": None, "top": [], "was_tier": m["tier"], "note": "O*NET ability: already matched to its source"})
            tally["none"] = tally.get("none", 0) + 1
            continue
        pages = {}
        for c in m["candidates"]:
            b = basis_of(c, L.norm)
            ek = key(e["preferred_name"])
            plain = QUALIFIER.sub("", c["title"])
            if (c["form_kind"] == "preferred" or key(c["form"]) == ek) and b in ("redirect", "variant-redirect", "variant-title") and (key(c["title"]) == ek or key(plain) == ek):
                b = "exact-title" if key(c["title"]) == ek else "title-minus-qualifier"
            elif c["form_kind"] == "preferred" and b == "redirect" and len(ek) >= 4 and len(key(plain)) >= 4 and ek in key(plain):
                b = "redirect-contains"
            elif c["form_kind"] == "preferred" and b == "exact-title" and key(c["title"]) != ek:
                b = "title-minus-qualifier" if False else b
            p = pages.setdefault(c["page_id"], {"page_id": c["page_id"], "title": c["title"], "basis": b, "via": c.get("via"), "form": c["form"]})
            if BASE[b] > BASE[p["basis"]]:
                p.update(basis=b, via=c.get("via"), form=c["form"])
        scored = []
        for pid, p in pages.items():
            info = cands.get(pid, {})
            cs = cats.get(pid, [])
            s = BASE[p["basis"]]
            notes = []
            if p["basis"] in ("title-minus-qualifier", "variant-qualifier") and not qualifier_ok(kind, p["title"]):
                s = min(s, 1.5); notes.append("the parenthetical does not suggest this kind")
            if info.get("disambiguation"):
                s -= 10; notes.append("disambiguation page")
            fit = kind_fits(kind, cs)
            if fit is True:
                s += 3; notes.append("categories fit the kind")
            elif fit is False:
                s -= 1; notes.append("categories do not fit the kind")
                if kind in STRICT:
                    s -= 4
            if NOISE.search(" | ".join(cs)):
                s -= 4; notes.append("categories look unrelated (%s)" % NOISE.search(" | ".join(cs)).group(0))
            scored.append({"page_id": pid, "title": p["title"], "basis": p["basis"], "via": p["via"], "score": round(s, 1), "notes": notes,
                           "rev_id": info.get("rev_id")})
        scored.sort(key=lambda x: -x["score"])
        top = scored[0] if scored else None
        second = scored[1]["score"] if len(scored) > 1 else -99
        if not top or top["score"] < 2:
            rel = "none"
        elif top["score"] >= 4 and top["score"] - second >= (1 if top["basis"] == "exact-title" else 2):
            rel = "same" if BASE[top["basis"]] >= 4 else "related"
        elif top["score"] >= 2 and top["score"] - second >= 2:
            rel = "related"
        else:
            rel = "ambiguous"
        tally[rel] = tally.get(rel, 0) + 1
        out.append({"entry_id": m["entry_id"], "entry_key": m["entry_key"], "preferred_name": m["preferred_name"], "kind": kind,
                    "relation": rel, "page": top if rel in ("same", "related") else None, "top": scored[:3] if rel == "ambiguous" else [], "was_tier": m["tier"]})
    tmp = a.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    os.rename(tmp, a.out)
    print(json.dumps(tally))


if __name__ == "__main__":
    main()
