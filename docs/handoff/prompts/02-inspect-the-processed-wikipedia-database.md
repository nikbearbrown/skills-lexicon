# Inspect the processed Wikipedia sqlite

**Status: DONE (kept as a record; do not run again)**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer). Nothing here needs sudo, and nothing may be deleted, edited or moved.

GOAL
We want to match entries of the skills lexicon to English Wikipedia articles, and pull each article's cleaned lead paragraph, categories, infobox facts, redirects and inbound-link count. A processed, searchable Wikipedia build already exists on the cluster. Before anything is designed, I need to know exactly what it contains. This job only inspects it. It changes nothing.

PATHS (use exactly these; invent none)
- Processed build (read only): /projects/medhavy/fact-checker/data/wikipedia/20261001/ , with the sub-folders raw/, jsonl/, db/, build/, logs/, venv/ . The database file is db/enwiki-20261001.sqlite . The symlink /projects/medhavy/fact-checker/data/wikipedia points to the same folder.
- Raw dump (read only, stays compressed): /projects/aiskunks/enwiki/20261001/
- Lexicon checkout (read only): /projects/aiskunks/skills-lexicon (commit e8ce1744e920e02889827c32d7b51247501c6e3f)
- Write ONLY here: /projects/aiskunks/skills-lexicon-work/wikipedia-inspect/

RULES (restated)
No sudo. Stay inside the two project folders above. No passwords, keys or tokens anywhere. Do not decompress the dump. Delete nothing. Many small files are slow on /projects (about 2 files per second): write results as ONE text file, never many. Python on the login node is 3.9: no match statements, no X | Y type syntax. Open the database read-only. Do not run heavy work on the login node: run the script as a Slurm batch job.

STEP 1. Look before running.
On the cluster run these and keep the output for the report:
  ls -la /projects/medhavy/fact-checker/data/wikipedia/20261001/
  ls -la /projects/medhavy/fact-checker/data/wikipedia/20261001/db/ /projects/medhavy/fact-checker/data/wikipedia/20261001/build/ /projects/medhavy/fact-checker/data/wikipedia/20261001/logs/
  du -sh /projects/medhavy/fact-checker/data/wikipedia/20261001/* 2>/dev/null
  df -h /projects/aiskunks
  id
If the database file is not readable by me (permission denied), STOP and tell me which group owns it and what I would need; do not try to get around it.
For jsonl/ do not list recursively: report only the number of entries (ls | wc -l, or find with -maxdepth 1 | wc -l) and the first 5 names with their sizes, because the folder may hold thousands of files.
Also look for a README, a build script or a log in build/ or logs/ that says how the database and the jsonl were made (what was kept, what was dropped, which columns exist). Read what you find (head, not cat, for anything large) and quote the relevant lines in the report.

STEP 2. Create the work folder and the script.
  mkdir -p /projects/aiskunks/skills-lexicon-work/wikipedia-inspect/
Write this file, exactly, to /projects/aiskunks/skills-lexicon-work/wikipedia-inspect/inspect_wiki_db.py :

    #!/usr/bin/env python3
    """Read-only look at the processed Wikipedia sqlite: tables, columns, row counts, indexes, and a few sample rows.
    Usage: python3 inspect_wiki_db.py DB_PATH > report.txt   (Python 3.9 compatible)"""
    import json
    import sqlite3
    import sys
    import time

    DB = sys.argv[1]
    TITLES = ["Kubernetes", "Git", "Git (software)", "MySQL", "Jira (software)", "Python (programming language)",
              "Apple", "Microsoft Excel", "K8s", "Container orchestration"]
    QUERY_SECONDS = 90


    def connect():
        con = sqlite3.connect("file:%s?mode=ro" % DB, uri=True)
        con.row_factory = sqlite3.Row
        return con


    def timed(con, sql, args=()):
        """Run a query, but abort it after QUERY_SECONDS so a missing index cannot hang the job."""
        start = time.time()
        con.set_progress_handler(lambda: 1 if time.time() - start > QUERY_SECONDS else 0, 100000)
        try:
            rows = con.execute(sql, args).fetchall()
            return rows, round(time.time() - start, 2), None
        except sqlite3.OperationalError as e:
            return [], round(time.time() - start, 2), str(e)
        finally:
            con.set_progress_handler(None, 0)


    def clip(v):
        if isinstance(v, (bytes, bytearray)):
            return "<%d bytes>" % len(v)
        if isinstance(v, str) and len(v) > 300:
            return v[:300] + "...[%d chars]" % len(v)
        return v


    def main():
        con = connect()
        print("sqlite version", sqlite3.sqlite_version, "python", sys.version.split()[0])
        objs = con.execute("select type, name, tbl_name, sql from sqlite_master order by type, name").fetchall()
        tables = [o["name"] for o in objs if o["type"] == "table"]
        print("\n== objects ==")
        for o in objs:
            print(o["type"], o["name"], "on", o["tbl_name"])
            print("   ", (o["sql"] or "").replace("\n", " ")[:500])
        print("\n== row counts (max rowid; exact count if quick) ==")
        for t in tables:
            if t.endswith(("_data", "_idx", "_docsize", "_config", "_content")):
                continue
            rows, secs, err = timed(con, 'select max(rowid) as m from "%s"' % t)
            print(t, "max rowid:", rows[0]["m"] if rows else None, "(%ss)" % secs, err or "")
        print("\n== sample rows for chosen titles ==")
        for t in tables:
            cols = [c["name"] for c in con.execute('pragma table_info("%s")' % t)]
            tcol = next((c for c in cols if c.lower() in ("title", "page_title", "name", "article", "article_title")), None)
            if not tcol:
                continue
            print("\n-- table", t, "columns:", cols, "title column:", tcol)
            for title in TITLES:
                rows, secs, err = timed(con, 'select * from "%s" where "%s" = ? limit 2' % (t, tcol), (title,))
                print("  title=%r -> %d row(s) in %ss %s" % (title, len(rows), secs, err or ""))
                for r in rows:
                    print("     ", json.dumps({k: clip(r[k]) for k in r.keys()}, ensure_ascii=False, default=str)[:1500])
        con.close()


    if __name__ == "__main__":
        main()

Also write this batch file, exactly, to /projects/aiskunks/skills-lexicon-work/wikipedia-inspect/inspect.sbatch :

    #!/bin/bash
    #SBATCH --job-name=wiki-inspect
    #SBATCH --partition=short
    #SBATCH --time=00:30:00
    #SBATCH --mem=8G
    #SBATCH --cpus-per-task=1
    #SBATCH --output=/projects/aiskunks/skills-lexicon-work/wikipedia-inspect/job-%j.log
    cd /projects/aiskunks/skills-lexicon-work/wikipedia-inspect
    python3 -I inspect_wiki_db.py /projects/medhavy/fact-checker/data/wikipedia/20261001/db/enwiki-20261001.sqlite > report.txt 2>&1
    echo "exit status $?" >> report.txt

STEP 3. Dry run, then the job.
  cd /projects/aiskunks/skills-lexicon-work/wikipedia-inspect && python3 -I -c "import ast,sys; ast.parse(open('inspect_wiki_db.py').read()); print('syntax ok')"
Then submit:  sbatch inspect.sbatch   and check it with  squeue -u $USER . When it ends, read report.txt in full. If the job fails or the report ends without "exit status 0", report that instead of guessing.

STEP 4. Check.
- report.txt contains a "== objects ==" section, a "== row counts" section and at least one "-- table" section with sample rows.
- Say whether the title Kubernetes was found, in which table(s), and what columns came with it.
- Using the sqlite, answer these questions with evidence from the report, and say "not present" where that is the case: does the database hold (a) the article text or only a part of it, and which part; (b) the raw wikitext or cleaned text; (c) redirects; (d) categories per article; (e) infobox data; (f) revision ids; (g) links between articles or inbound-link counts; (h) a full-text search index? Is the index on title usable (did the title lookups return in well under a second)?
- Check which Python packages the venv at /projects/medhavy/fact-checker/data/wikipedia/20261001/venv/ holds (look at its lib/python*/site-packages folder names only; do not activate it or install anything) and say whether mwparserfromhell is among them.

STOP AND ASK if: any path above is missing or differs from this description; the database is unreadable; the work folder already exists with files in it; the job fails; or the database is much larger or smaller than a full English Wikipedia (about 7 million articles) would suggest.

REPORT BACK (short, plain text, paste-ready)
1. Sizes and listing of the build folder, and what the logs or build scripts say about how it was made.
2. The full contents of report.txt (it should be a few hundred lines; if it is much longer, give the "== objects ==" part, the row counts and the Kubernetes rows, and say where the full file is).
3. Your answers to (a) to (h) and the mwparserfromhell result.
4. Job id, run time, and anything that failed or was skipped.
Do not summarise away numbers: I need the exact table names, column names and counts.
```
