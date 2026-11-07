# Job titles to O*NET occupations: a pilot

**Status: NOT RUN (run after 07, on datasets 07 shows have clean title columns)**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer).

GOAL
Pilot: take a few of the downloaded job-posting datasets that have a clear job-title column, count the titles, map them to O*NET occupations (SOC codes) by exact match against O*NET's own title lists, and measure how much maps cleanly. We do not need all the data, which is still downloading: pick a few good datasets and work from those. Nothing is decided here: a title matching one occupation is "same", matching several is "ambiguous", matching none is "none". The aim is a measured coverage figure and two hand-check samples, then a decision on whether a model step is worth building.

PATHS (use exactly these; find the ones marked FIND, invent none)
- FIND: the folder of downloaded datasets under /projects/aiskunks (it holds about 2,110 folders each with a dataset.zip, about 300 MB in all) and the download ledger beside it (3,310 rows for 2,110 unique destinations, because ssh retries repeated rows). Show me both paths and ask if there is more than one candidate. The downloads are still running: read only, never touch, move or delete anything there.
- Read only: /projects/aiskunks/onet/31.0/ : the tables Occupation Data.txt, Alternate Titles.txt and Sample of Reported Titles.txt (the real names may differ slightly; list the folder and say which files you used).
- Read only: /projects/aiskunks/skills-lexicon (do not edit it).
- Write only: /projects/aiskunks/skills-lexicon-work/job-titles-pilot/ (create it).
- On the Mac: my local clone of the skills-lexicon repository, for the licence list in step 2 and for step 6.

RULES
No sudo. Stay inside /projects/aiskunks. No passwords, keys or tokens anywhere. Delete and overwrite nothing on the cluster, and change no permissions. Many small files are slow on /projects (about 2 files per second): this job writes a handful. Python on the login node is 3.9. Run the scanning as Slurm batch jobs, not on the login node. Use tar over ssh to copy to the Mac (not rsync). Do not touch main, merge, or open a pull request. Use only datasets whose licence is clear (see step 2). If anything differs from what is described, stop and report instead of improvising.

STEP 1. Write the script.
  mkdir -p /projects/aiskunks/skills-lexicon-work/job-titles-pilot
Write this file exactly to /projects/aiskunks/skills-lexicon-work/job-titles-pilot/title_pilot.py :

    #!/usr/bin/env python3
    """Job-title pilot: inventory the downloaded datasets, count titles in chosen ones, match them to O*NET occupation titles. Python 3.9.

      python3 -I title_pilot.py inventory --root DIR --out inventory.jsonl
      python3 -I title_pilot.py extract --zip Z --member M --column C --out counts.jsonl
      python3 -I title_pilot.py match --counts counts.jsonl --titles FILE [FILE ...] --out DIR --dataset NAME

    Reads only. A match is a candidate, not a decision: one occupation code is `same`, several are `ambiguous`, none is `none`."""
    import argparse
    import collections
    import csv
    import glob
    import io
    import itertools
    import json
    import os
    import re
    import sys
    import unicodedata
    import zipfile

    TITLE_COL = re.compile(r"(^|[_\s-])(job[_\s-]?title|job[_\s-]?role|title|position|designation|role|occupation)($|[_\s-])", re.I)
    BAD_COL = re.compile(r"sub[_\s-]?title|company|employer|school|department|category|type|description|url|link", re.I)
    LEVELS = {"senior", "sr", "junior", "jr", "lead", "principal", "staff", "intern", "trainee", "entry", "level", "i", "ii", "iii", "iv", "v", "associate", "assistant"}
    csv.field_size_limit(10 ** 7)


    def sniff(sample):
        best = max(",\t;|", key=lambda d: sample.split("\n")[0].count(d))
        return best


    def inventory(root, out):
        n = 0
        with open(out, "w", encoding="utf-8") as fo:
            for z in sorted(glob.glob(os.path.join(root, "**", "*.zip"), recursive=True)):
                try:
                    zf = zipfile.ZipFile(z)
                except zipfile.BadZipFile:
                    fo.write(json.dumps({"zip": z, "error": "bad zip"}) + "\n")
                    continue
                for info in zf.infolist():
                    if not info.filename.lower().endswith((".csv", ".tsv")) or info.file_size == 0:
                        continue
                    with zf.open(info) as f:
                        head = f.read(65536).decode("utf-8", "replace")
                    d = sniff(head)
                    try:
                        header = next(csv.reader(io.StringIO(head), delimiter=d))
                    except Exception:
                        continue
                    cols = [h for h in header if TITLE_COL.search(h) and not BAD_COL.search(h)]
                    rows = 0
                    if cols and info.file_size < 800 * 1024 * 1024:
                        with zf.open(info) as f:
                            rows = sum(1 for _ in io.TextIOWrapper(f, encoding="utf-8", errors="replace")) - 1
                    fo.write(json.dumps({"zip": z, "member": info.filename, "bytes": info.file_size, "delimiter": d, "header": header[:40],
                                         "title_columns": cols, "rows": rows}, ensure_ascii=False) + "\n")
                    n += 1
        print("inventory: %d tabular members -> %s" % (n, out))


    def extract(zpath, member, column, out):
        c = collections.Counter()
        zf = zipfile.ZipFile(zpath)
        with zf.open(member) as f:
            text = io.TextIOWrapper(f, encoding="utf-8", errors="replace", newline="")
            head = text.readline()
            d = sniff(head)
            rd = csv.DictReader(itertools.chain([head], text), delimiter=d)
            if column not in (rd.fieldnames or []):
                print("STOP: column %r not in %s" % (column, rd.fieldnames), file=sys.stderr)
                sys.exit(2)
            rows = 0
            for r in rd:
                rows += 1
                t = (r.get(column) or "").strip()
                if t:
                    c[t] += 1
        with open(out, "w", encoding="utf-8") as fo:
            for t, n in c.most_common():
                fo.write(json.dumps({"title": t, "count": n}, ensure_ascii=False) + "\n")
        print("extract: %d rows, %d distinct titles -> %s" % (rows, len(c), out))


    def normalise(t):
        s = unicodedata.normalize("NFKC", t).lower().replace("&", " and ")
        s = re.sub(r"[\(\[\{][^\)\]\}]*[\)\]\}]", " ", s)
        s = re.split(r"\s[-–—|@]\s|\sat\s|,", s)[0]
        toks = re.findall(r"[a-z0-9+#./]+", s)
        levels = [x for x in toks if x in LEVELS or x.isdigit()]
        core = [x for x in toks if x not in LEVELS and not x.isdigit()]
        return " ".join(core), levels


    def load_titles(files):
        idx = collections.defaultdict(set)
        names = {}
        for p in files:
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                rd = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
                next(rd, None)
                for r in rd:
                    if len(r) < 2:
                        continue
                    k = normalise(r[1])[0]
                    if k:
                        idx[k].add(r[0][:7])
                        names.setdefault(r[0][:7], r[1])
        return idx, names


    def match(counts, files, out, dataset):
        idx, names = load_titles(files)
        os.makedirs(out, exist_ok=True)
        tot = collections.Counter(); dist = collections.Counter(); rows_total = 0
        with open(os.path.join(out, "titles_matched.jsonl"), "w", encoding="utf-8") as fo:
            for line in open(counts, encoding="utf-8"):
                d = json.loads(line)
                key, levels = normalise(d["title"])
                codes = sorted(idx.get(key, []))
                rel = "none" if not codes else "same" if len(codes) == 1 else "ambiguous"
                tot[rel] += d["count"]; dist[rel] += 1; rows_total += d["count"]
                fo.write(json.dumps({"dataset": dataset, "title": d["title"], "count": d["count"], "normalised": key, "levels": levels, "relation": rel,
                                     "soc": codes[:6], "soc_titles": [names[c] for c in codes[:6]]}, ensure_ascii=False) + "\n")
        summary = {"dataset": dataset, "rows_with_title": rows_total, "distinct_titles": sum(dist.values()),
                   "rows_by_relation": dict(tot), "distinct_by_relation": dict(dist),
                   "share_of_rows": {k: round(v / rows_total, 3) for k, v in tot.items()} if rows_total else {}}
        with open(os.path.join(out, "summary.json"), "w") as fs:
            json.dump(summary, fs, indent=1)
        print(json.dumps(summary))


    def main():
        ap = argparse.ArgumentParser()
        sub = ap.add_subparsers(dest="cmd", required=True)
        a = sub.add_parser("inventory"); a.add_argument("--root", required=True); a.add_argument("--out", required=True)
        b = sub.add_parser("extract"); b.add_argument("--zip", required=True); b.add_argument("--member", required=True); b.add_argument("--column", required=True); b.add_argument("--out", required=True)
        c = sub.add_parser("match"); c.add_argument("--counts", required=True); c.add_argument("--titles", nargs="+", required=True); c.add_argument("--out", required=True); c.add_argument("--dataset", required=True)
        x = ap.parse_args()
        if x.cmd == "inventory":
            inventory(x.root, x.out)
        elif x.cmd == "extract":
            extract(x.zip, x.member, x.column, x.out)
        else:
            match(x.counts, x.titles, x.out, x.dataset)


    if __name__ == "__main__":
        main()

Check it parses: python3 -I -c "import ast; ast.parse(open('/projects/aiskunks/skills-lexicon-work/job-titles-pilot/title_pilot.py').read()); print('syntax ok')"

STEP 2. Inventory and choose datasets.
a. Write /projects/aiskunks/skills-lexicon-work/job-titles-pilot/inventory.sbatch (partition short, 1 hour, 4 GB, 1 cpu, output /projects/aiskunks/skills-lexicon-work/job-titles-pilot/inventory-%j.log) that runs: python3 -I title_pilot.py inventory --root <the dataset folder you found> --out /projects/aiskunks/skills-lexicon-work/job-titles-pilot/inventory.jsonl . Submit it and read the log. Report how many tabular files were found, how many have a title-like column, and the ten most common title column names.
b. Licences. On the Mac, the public GitHub branch data/kaggle-occurrence-evidence-20261030 holds a file data/source-occurrences/kaggle-publication-2026-10-30/sources.json that records each dataset's publisher-declared licence (field license_as_recorded, keyed by dataset_ref). Read it with git show origin/data/kaggle-occurrence-evidence-20261030:data/source-occurrences/kaggle-publication-2026-10-30/sources.json . Also check the cluster ledger for a licence column and tell me if there is one. A dataset is eligible only if its licence is recorded and is one of: CC0, CC BY 4.0, MIT, Apache 2.0, ODC-By. Datasets with non-commercial, share-alike, GPL, copyright-only or missing licences are NOT eligible for the pilot.
c. Choose 3 to 5 eligible datasets: each with a title column whose values are single job titles (look at 20 values from each before choosing; reject a column that holds sentences, skills or company names), at least 5,000 rows, and as different from each other as possible (different countries or sites, judged from the location or company columns or the dataset name). If fewer than 3 are eligible, STOP and tell me how many are, and which others had a good title column but an ineligible licence. Show me the table of chosen datasets (dataset, zip path, member, column, rows, licence) and continue.

STEP 3. Extract and match (one batch file).
For each chosen dataset write the command pair into /projects/aiskunks/skills-lexicon-work/job-titles-pilot/run.sbatch (partition short, 2 hours, 8 GB, 1 cpu, output /projects/aiskunks/skills-lexicon-work/job-titles-pilot/run-%j.log): first extract with title_pilot.py extract (zip, member, column) into /projects/aiskunks/skills-lexicon-work/job-titles-pilot/<short dataset name>/counts.jsonl, then match with title_pilot.py match --counts that file --titles "<Occupation Data.txt>" "<Alternate Titles.txt>" "<Sample of Reported Titles.txt>" (the real file names) --out /projects/aiskunks/skills-lexicon-work/job-titles-pilot/<short dataset name> --dataset <dataset_ref>. Submit, watch squeue -u $USER, read the log. All steps must exit 0; a STOP line means report it exactly.

STEP 4. Report the measurements.
For each dataset and for all together: rows with a title, distinct titles, and the share of rows that are same, ambiguous and none (from summary.json). Also the ten most frequent titles in each relation class with their counts.

STEP 5. Hand-check samples (do not judge them yourself).
For each dataset print two tables from titles_matched.jsonl: 40 random matched titles (relation same: raw title, normalised title, the O*NET occupation title and SOC code), and 40 random distinct unmatched titles weighted by frequency (relation none: raw title, count). Use a fixed random seed of 7. I will mark which matches are wrong and which unmatched titles an O*NET title should have caught.

STEP 6. Publish.
- Copy /projects/aiskunks/skills-lexicon-work/job-titles-pilot/title_pilot.py and, for each chosen dataset, summary.json and titles_matched.jsonl to a temporary folder on the Mac with tar over ssh. Verify sha256 on both sides. If the matched files together exceed 30 MB, STOP and tell me.
- In my local clone: git fetch origin, then create the branch data/job-titles-pilot-20261101 from origin/main. Put the files at data/job-titles-pilot/<short dataset name>/ and scripts/job_titles/title_pilot.py.
- Write data/job-titles-pilot/README.md: what the files are (one line per distinct title in a dataset, with its count, a normalised form, the seniority words removed, the relation and the O*NET-SOC codes it matched); the datasets used with their licences exactly as recorded; that the O*NET titles are used under CC BY 4.0 with this notice: "This product includes information from the O*NET 31.0 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), used under the CC BY 4.0 license. O*NET(R) is a trademark of USDOL/ETA. The matches and counts here were produced from that information by the Skills Lexicon project; USDOL/ETA has not approved, endorsed or tested these modifications."; and that counts are rows in each dataset, not jobs or market share (datasets overlap and repeat postings).
- Run python3 -I tools/lexicon.py validate in the clone (it must end with 0 errors) and git status (only those files staged). Commit "Job-title pilot: titles from N datasets matched to O*NET occupations" and push git push -u origin data/job-titles-pilot-20261101. If the push is refused, STOP and report the exact message.

STOP AND ASK IF: the dataset folder or ledger is ambiguous; fewer than 3 datasets are eligible; a title column holds something that is not a job title; any exit status is not 0; the O*NET title files cannot be found; a checksum differs; validate does not end with 0 errors; extra files are staged; the branch exists; the push is refused.

REPORT BACK (short, plain text)
The dataset folder and ledger paths; the inventory numbers; the chosen-datasets table; job ids and run times; the step 4 measurements; the step 5 tables; the branch name and commit hash; anything that failed or was skipped. Do not say a check passed unless you ran it and saw it pass.
```
