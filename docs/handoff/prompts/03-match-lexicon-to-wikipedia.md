# Match lexicon entries to Wikipedia articles

**Status: DONE (kept as a record; do not run again)**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer).

GOAL
Match every entry of the skills lexicon (3,688) to English Wikipedia articles, using the processed Wikipedia build that already exists, and for each candidate article record its page id, title, revision id and timestamp, its cleaned lead paragraph, and its categories. The job records candidates and flags; it decides nothing. Results are a few files. Nothing in the lexicon checkout changes.

PATHS (use exactly these; invent none)
- Read only: the database /projects/medhavy/fact-checker/data/wikipedia/20261001/db/enwiki-20261001.sqlite
- Read only: the jsonl folder /projects/medhavy/fact-checker/data/wikipedia/20261001/jsonl (the *.articles.jsonl part files, about 32 GB)
- Read only: the lexicon checkout /projects/aiskunks/skills-lexicon (commit e8ce1744e920e02889827c32d7b51247501c6e3f, working tree clean)
- Write only: /projects/aiskunks/skills-lexicon-work/wikipedia-match/ (create it)

RULES (restated)
No sudo. Stay inside the two project folders. No passwords, keys or tokens anywhere. Do not decompress the raw dump. Delete nothing, and do not edit the lexicon checkout: it must still be clean when you finish. Creating many small files is slow on /projects (about 2 files per second): this job writes a handful of files. Python on the login node is 3.9; the scripts are written for it. Heavy work runs as Slurm jobs, never on the login node. Compute nodes may not have internet; this job needs none. If anything below fails or surprises you, stop and report; do not improvise.

STEP 1. Create the folder and the scripts.
  mkdir -p /projects/aiskunks/skills-lexicon-work/wikipedia-match
Write these two files exactly.

File /projects/aiskunks/skills-lexicon-work/wikipedia-match/match_entries.py :

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

File /projects/aiskunks/skills-lexicon-work/wikipedia-match/categories_for_pages.py :

    #!/usr/bin/env python3
    """Stage 2: read each candidate page's categories from the .articles.jsonl part files. Python 3.9.

    Usage: python3 -I categories_for_pages.py --jsonl JSONL_DIR --candidates OUT_DIR/candidates.jsonl --out OUT_DIR/categories.jsonl [--workers 8]
    Needs the key that holds the page id; it finds it from the first record and stops if it cannot."""
    import argparse
    import glob
    import json
    import multiprocessing
    import os
    import re
    import sys

    ID_KEYS = ("page_id", "pageid", "id")
    WANTED = set()
    KEY = None


    def init(wanted, key):
        global WANTED, KEY
        WANTED, KEY = wanted, key


    def scan(path):
        out, fallbacks, lines = [], 0, 0
        rx = re.compile(r'"%s"\s*:\s*(\d+)' % KEY)
        with open(path, encoding="utf-8") as f:
            for line in f:
                lines += 1
                m = rx.search(line[:600])
                if m:
                    if int(m.group(1)) not in WANTED:
                        continue
                else:
                    fallbacks += 1
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                pid = rec.get(KEY)
                if pid in WANTED:
                    out.append({"page_id": pid, "title": rec.get("title"), "categories": rec.get("categories", [])})
        return path, lines, fallbacks, out


    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("--jsonl", required=True)
        ap.add_argument("--candidates", required=True)
        ap.add_argument("--out", required=True)
        ap.add_argument("--workers", type=int, default=8)
        ap.add_argument("--max-files", type=int, default=0, help="dry run: read only the first N files")
        a = ap.parse_args()
        if os.path.exists(a.out):
            print("STOP: %s exists" % a.out, file=sys.stderr)
            sys.exit(5)
        wanted = {json.loads(l)["page_id"] for l in open(a.candidates, encoding="utf-8")}
        files = sorted(glob.glob(os.path.join(a.jsonl, "**", "*.articles.jsonl"), recursive=True))
        if not files:
            print("STOP: no *.articles.jsonl under %s" % a.jsonl, file=sys.stderr)
            sys.exit(2)
        with open(files[0], encoding="utf-8") as f:
            first = json.loads(f.readline())
        key = next((k for k in ID_KEYS if k in first and isinstance(first[k], int)), None)
        print("files %d, first record keys %s, page id key %s" % (len(files), sorted(first), key), flush=True)
        if not key or "categories" not in first:
            print("STOP: cannot find a page id key (%s) and a categories list in the first record" % (ID_KEYS,), file=sys.stderr)
            sys.exit(2)
        if a.max_files:
            files = files[:a.max_files]
        found, tot_lines, tot_fb = {}, 0, 0
        with multiprocessing.Pool(a.workers, initializer=init, initargs=(wanted, key)) as pool:
            for path, lines, fb, out in pool.imap_unordered(scan, files):
                tot_lines += lines
                tot_fb += fb
                for r in out:
                    found[r["page_id"]] = r
                print("%s lines %d fallbacks %d found %d" % (os.path.basename(path), lines, fb, len(out)), flush=True)
        tmp = a.out + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            for pid in sorted(found):
                f.write(json.dumps(found[pid], ensure_ascii=False) + "\n")
        os.rename(tmp, a.out)
        print(json.dumps({"wanted": len(wanted), "found": len(found), "lines": tot_lines, "lines_without_id_in_first_600_chars": tot_fb}))


    if __name__ == "__main__":
        main()

Check they parse:  cd /projects/aiskunks/skills-lexicon-work/wikipedia-match && python3 -I -c "import ast; [ast.parse(open(f).read()) for f in ('match_entries.py','categories_for_pages.py')]; print('syntax ok')"

STEP 2. Dry run on 10 well-known names (expected to finish in a few minutes, mostly scanning the articles and redirects tables).
Write /projects/aiskunks/skills-lexicon-work/wikipedia-match/dry.sbatch exactly:

    #!/bin/bash
    #SBATCH --job-name=wiki-match-dry
    #SBATCH --partition=short
    #SBATCH --time=01:00:00
    #SBATCH --mem=12G
    #SBATCH --cpus-per-task=2
    #SBATCH --output=/projects/aiskunks/skills-lexicon-work/wikipedia-match/dry-%j.log
    cd /projects/aiskunks/skills-lexicon-work/wikipedia-match
    python3 -I match_entries.py --lexicon /projects/aiskunks/skills-lexicon --db /projects/medhavy/fact-checker/data/wikipedia/20261001/db/enwiki-20261001.sqlite --out /projects/aiskunks/skills-lexicon-work/wikipedia-match/dry --names "Python,SQL,Docker,Java,React,TensorFlow,MATLAB,PostgreSQL,Tableau,Amazon Web Services"
    echo "exit status $?"
    python3 -I categories_for_pages.py --jsonl /projects/medhavy/fact-checker/data/wikipedia/20261001/jsonl --candidates /projects/aiskunks/skills-lexicon-work/wikipedia-match/dry/candidates.jsonl --out /projects/aiskunks/skills-lexicon-work/wikipedia-match/dry/categories.jsonl --workers 2 --max-files 2
    echo "exit status $?"

Submit it (sbatch dry.sbatch), wait, read the log. Expected: no STOP line; "entries 10" (or fewer if a name is not an entry: say which); the summary line; and a categories line that prints the first record's keys and the page id key. It is fine if the 2-file categories step finds few or no pages (it only read two files); what matters is that it reports the keys and does not STOP. Show me the first 3 lines of /projects/aiskunks/skills-lexicon-work/wikipedia-match/dry/matches.jsonl, and the first candidate with its lead (first 300 characters of the lead only).
If the job prints a STOP line, report it exactly and wait for me; the three codes mean: 2 a table or column or the jsonl keys differ from what was expected, 3 passages has no page_id index, 5 the output folder already exists.

STEP 3. Full run. Only after the dry run looked right.
Write /projects/aiskunks/skills-lexicon-work/wikipedia-match/full.sbatch exactly:

    #!/bin/bash
    #SBATCH --job-name=wiki-match
    #SBATCH --partition=short
    #SBATCH --time=08:00:00
    #SBATCH --mem=16G
    #SBATCH --cpus-per-task=8
    #SBATCH --output=/projects/aiskunks/skills-lexicon-work/wikipedia-match/full-%j.log
    cd /projects/aiskunks/skills-lexicon-work/wikipedia-match
    python3 -I match_entries.py --lexicon /projects/aiskunks/skills-lexicon --db /projects/medhavy/fact-checker/data/wikipedia/20261001/db/enwiki-20261001.sqlite --out /projects/aiskunks/skills-lexicon-work/wikipedia-match/full
    echo "exit status $?"
    python3 -I categories_for_pages.py --jsonl /projects/medhavy/fact-checker/data/wikipedia/20261001/jsonl --candidates /projects/aiskunks/skills-lexicon-work/wikipedia-match/full/candidates.jsonl --out /projects/aiskunks/skills-lexicon-work/wikipedia-match/full/categories.jsonl --workers 8
    echo "exit status $?"

Submit it, watch squeue -u $USER, and read the log when it ends. Both "exit status" lines must say 0.

STEP 4. Checks (run on the login node; they are small).
a. Counts: cat /projects/aiskunks/skills-lexicon-work/wikipedia-match/full/summary.json . Expected: entries 3688 (or 3688 minus any deprecated entries; say the number), tiers that add up to the same number, candidate_pages in the low thousands. Report the three tier counts.
b. Files: ls -la /projects/aiskunks/skills-lexicon-work/wikipedia-match/full/ . Expected exactly: matches.jsonl, candidates.jsonl, categories.jsonl, summary.json.
c. The lexicon is untouched: cd /projects/aiskunks/skills-lexicon && git status --porcelain (must print nothing) && python3 -I tools/lexicon.py validate (must end with 0 errors).
d. Known cases. Show the tier, reasons and candidate titles for the entries named Python, SQL, Docker, Java, React, TensorFlow, MATLAB, PostgreSQL, Tableau, Amazon Web Services (grep the preferred_name in matches.jsonl). Expected: each has a candidate; Python, Java, Docker, React should point at their software or language article, not at a disambiguation page. Report any that do not.
e. Categories: for the page whose title is Kubernetes (if an entry matched it, otherwise any matched page), show its categories. Expected: a list of plain-text category names like those in the inspection report.
f. Coverage: how many candidate pages have no entry in categories.jsonl (should be 0 or very few). Say the number.
g. Ambiguity: how many entries are tier needs-a-person, and the 15 most common reasons.

STOP AND ASK IF: the output folder exists; any exit status is not 0; the summary counts do not match (a); the lexicon checkout is no longer clean or no longer validates; the full run is still going after 6 hours; categories coverage (f) is below 99 percent.

REPORT BACK (short, plain text)
Job ids and run times for the dry run and the full run; the summary.json contents; results of checks a to g (exact numbers); paths and sizes of the four output files; anything that failed or was skipped. Big files stay on the cluster. Do not paste whole files. When I ask for it later, you will copy matches.jsonl, candidates.jsonl, categories.jsonl and summary.json to the Mac with tar over ssh (not rsync).
```
