# Which job-posting fields can be read unambiguously

**Status: NOT RUN (run this first of 05 to 07)**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer).

GOAL
A large collection of job-posting datasets has been downloaded to the cluster and is still growing. Find out which fields can be read UNAMBIGUOUSLY from it: fields that sit in their own column with a header that names them and values that behave like that field (job title, company name, location, salary, date posted, employment type, experience level, industry, a structured skills list, and so on). We are NOT parsing free text: a description column is only marked as free text. This is a survey: it reports what is there and decides nothing. I decide afterwards which fields to extract.

PATHS (use exactly these; find the one marked FIND, invent none)
- FIND: the folder of downloaded datasets under /projects/aiskunks (many folders each with a dataset.zip) and the download ledger beside it (it has repeated rows from ssh retries, so it has more rows than unique destinations). Show me both paths and ask if there is more than one candidate. The downloads may still be running: read only; never touch, move, rename or delete anything there.
- Write only: /projects/aiskunks/skills-lexicon-work/job-fields-survey/ (create it)
- On the Mac: my local clone of the skills-lexicon repository, for the licence list and step 6.

RULES
No sudo. Stay inside /projects/aiskunks. No passwords, keys or tokens anywhere. Delete and overwrite nothing on the cluster, and change no permissions. Many small files are slow on /projects (about 2 files per second): this job writes a few files. Python on the login node is 3.9. Run the survey as a Slurm batch job, not on the login node. Use tar over ssh to copy to the Mac (not rsync). Do not touch main, merge, or open a pull request. If anything differs from what is described, or fails, stop and report instead of improvising.

STEP 1. Write the script.
  mkdir -p /projects/aiskunks/skills-lexicon-work/job-fields-survey
Write this file exactly to /projects/aiskunks/skills-lexicon-work/job-fields-survey/field_survey.py :

    #!/usr/bin/env python3
    """Survey which job-posting fields can be read unambiguously from their own column in downloaded datasets. Python 3.9. Reads only.

      python3 -I field_survey.py survey --root DIR --out OUTDIR [--workers 8] [--sample 2000] [--limit N]
      python3 -I field_survey.py summarise --columns OUTDIR/columns.jsonl --out OUTDIR/summary.json

    A field counts as unambiguous only when a column's HEADER names it and its VALUES behave like that field (short, consistent, parseable).
    Free text (descriptions) is never parsed: it is only marked `free_text`. Nothing is decided here; the output is evidence for a person."""
    import argparse
    import collections
    import csv
    import glob
    import io
    import itertools
    import json
    import multiprocessing
    import os
    import re
    import statistics
    import sys
    import zipfile

    csv.field_size_limit(10 ** 7)
    HEAD = {
        "job_title": r"(^|[_\s-])(job[_\s-]?title|job[_\s-]?role|title|position|designation|role|occupation|post[_\s-]?name)($|[_\s-])",
        "company": r"(^|[_\s-])(company|employer|organi[sz]ation|org[_\s-]?name|firm|hiring[_\s-]?org|business[_\s-]?name)($|[_\s-])",
        "location": r"(^|[_\s-])(location|city|state|country|region|place|locality|job[_\s-]?location|work[_\s-]?location)($|[_\s-])",
        "salary": r"(salary|wage|pay[_\s-]?(rate|range)?|compensation|min[_\s-]?pay|max[_\s-]?pay|ctc|remuneration)",
        "date": r"(date|posted|published|created|listed|time[_\s-]?stamp)",
        "employment_type": r"(employment|job[_\s-]?type|contract|work[_\s-]?type|schedule|working[_\s-]?hours|position[_\s-]?type|full[_\s-]?time)",
        "experience_level": r"(experience|seniority|career[_\s-]?level|job[_\s-]?level|level)",
        "industry": r"(industry|sector|field|domain)",
        "skills_list": r"(^|[_\s-])(skills?|key[_\s-]?skills|tags?|technologies|tech[_\s-]?stack|keywords)($|[_\s-])",
        "education": r"(education|degree|qualification)",
        "remote": r"(remote|work[_\s-]?from[_\s-]?home|wfh|telecommut)",
        "url": r"(url|link|href)",
        "job_id": r"(^|[_\s-])(job[_\s-]?id|posting[_\s-]?id|id|uuid|ref(erence)?)($|[_\s-])",
        "description": r"(description|details|responsibilit|summary|requirements?|about|overview|content|text)",
    }
    HEAD = {k: re.compile(v, re.I) for k, v in HEAD.items()}
    DATE = [re.compile(p) for p in (r"^\d{4}-\d{2}-\d{2}", r"^\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}", r"^\d{4}/\d{2}/\d{2}",
                                     r"^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? \d{1,2},? \d{4}", r"^\d{1,2} (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]* \d{4}", r"^\d{9,13}$")]
    RELATIVE = re.compile(r"\b(ago|yesterday|today|hours?|days?|weeks?|months?)\b", re.I)
    CURRENCY = re.compile(r"(\$|€|£|₹|usd|eur|gbp|inr|cad|aud|\d[\d,\.]*\s?(k|lpa|per|/))", re.I)
    SEP = re.compile(r"[,;|/]")


    def sniff(line):
        return max(",\t;|", key=lambda d: line.count(d))


    def profile(values):
        vals = [v.strip() for v in values if v is not None]
        ne = [v for v in vals if v]
        n = len(vals) or 1
        words = [len(v.split()) for v in ne] or [0]
        p = {"filled": round(len(ne) / n, 3), "distinct": round(len(set(ne)) / (len(ne) or 1), 3), "n_distinct": len(set(ne)),
             "median_words": statistics.median(words), "long_share": round(sum(1 for w in words if w >= 12) / (len(ne) or 1), 3),
             "digit_share": round(sum(1 for v in ne if re.search(r"\d", v)) / (len(ne) or 1), 3),
             "date_share": round(sum(1 for v in ne if any(d.match(v.lower()) for d in DATE)) / (len(ne) or 1), 3),
             "relative_date_share": round(sum(1 for v in ne if RELATIVE.search(v)) / (len(ne) or 1), 3),
             "currency_share": round(sum(1 for v in ne if CURRENCY.search(v)) / (len(ne) or 1), 3),
             "list_share": round(sum(1 for v in ne if SEP.search(v)) / (len(ne) or 1), 3),
             "url_share": round(sum(1 for v in ne if v.lower().startswith(("http://", "https://", "www."))) / (len(ne) or 1), 3)}
        return p


    def judge(ftype, p):
        """(unambiguous?, reason). Header and values must agree."""
        if p["filled"] < 0.5:
            return False, "fewer than half the sampled rows have a value"
        if ftype == "description":
            return False, "free text: never parsed"
        if ftype == "job_title":
            ok = p["median_words"] <= 7 and p["long_share"] < 0.05 and p["distinct"] < 0.95
            return ok, "short values, few long ones, repeats" if ok else "values too long or all different: not a title column"
        if ftype == "company":
            ok = p["median_words"] <= 6 and p["long_share"] < 0.03 and p["url_share"] < 0.2
            return ok, "short values" if ok else "values too long to be a name"
        if ftype == "location":
            ok = p["median_words"] <= 6 and p["long_share"] < 0.03 and p["url_share"] < 0.2
            return ok, "short values" if ok else "values too long to be a place"
        if ftype == "salary":
            ok = p["digit_share"] >= 0.5 and p["long_share"] < 0.1
            return ok, "mostly numeric, currency or range values" if ok else "not mostly numeric"
        if ftype == "date":
            if p["date_share"] >= 0.8:
                return True, "80% or more parse as dates"
            if p["relative_date_share"] >= 0.5:
                return False, "relative dates (3 days ago) need the scrape date: ambiguous"
            return False, "values do not parse as dates"
        if ftype in ("employment_type", "experience_level", "industry", "education", "remote"):
            ok = p["n_distinct"] <= 60 and p["median_words"] <= 6
            return ok, "a short list of repeated values" if ok else "too many different values for a category"
        if ftype == "skills_list":
            ok = p["list_share"] >= 0.5 and p["median_words"] <= 40 and p["long_share"] < 0.5
            return ok, "delimited short labels (already structured)" if ok else "not delimited short labels"
        if ftype == "url":
            ok = p["url_share"] >= 0.8
            return ok, "values are links" if ok else "not links"
        if ftype == "job_id":
            ok = p["distinct"] >= 0.9 and p["median_words"] <= 2
            return ok, "mostly unique short values" if ok else "not an identifier"
        return False, "unknown type"


    def survey_member(args):
        zpath, member, sample = args
        out = []
        try:
            zf = zipfile.ZipFile(zpath)
            with zf.open(member) as f:
                text = io.TextIOWrapper(f, encoding="utf-8", errors="replace", newline="")
                first = text.readline()
                rd = csv.reader(itertools.chain([first], text), delimiter=sniff(first))
                header = next(rd)
                rows = list(itertools.islice(rd, sample))
            for i, h in enumerate(header):
                col = [r[i] if i < len(r) else None for r in rows]
                p = profile(col)
                types = [t for t, rx in HEAD.items() if rx.search(h)]
                res = []
                for t in types:
                    ok, why = judge(t, p)
                    res.append({"type": t, "unambiguous": ok, "why": why})
                out.append({"zip": zpath, "member": member, "column": h, "rows_sampled": len(rows), "profile": p, "candidates": res})
        except Exception as e:
            out.append({"zip": zpath, "member": member, "error": "%s: %s" % (type(e).__name__, str(e)[:120])})
        return out


    def survey(root, outdir, workers, sample, limit):
        os.makedirs(outdir, exist_ok=True)
        if os.path.exists(os.path.join(outdir, "columns.jsonl")):
            print("STOP: %s already has results" % outdir, file=sys.stderr)
            sys.exit(5)
        jobs, other = [], collections.Counter()
        for z in sorted(glob.glob(os.path.join(root, "**", "*.zip"), recursive=True)):
            try:
                for info in zipfile.ZipFile(z).infolist():
                    ext = os.path.splitext(info.filename)[1].lower()
                    if ext in (".csv", ".tsv") and info.file_size > 0:
                        jobs.append((z, info.filename, sample))
                    elif not info.is_dir():
                        other[ext or "(none)"] += 1
            except zipfile.BadZipFile:
                other["(bad zip)"] += 1
        if limit:
            jobs = jobs[:limit]
        print("tabular members: %d; other members by extension: %s" % (len(jobs), dict(other.most_common(12))), flush=True)
        tmp = os.path.join(outdir, ".tmp-columns.jsonl")
        n = 0
        with multiprocessing.Pool(workers) as pool, open(tmp, "w", encoding="utf-8") as fo:
            for res in pool.imap_unordered(survey_member, jobs, chunksize=4):
                for r in res:
                    fo.write(json.dumps(r, ensure_ascii=False) + "\n")
                n += 1
                if n % 200 == 0:
                    print("  %d members done" % n, flush=True)
        os.rename(tmp, os.path.join(outdir, "columns.jsonl"))
        with open(os.path.join(outdir, "other_members.json"), "w") as f:
            json.dump(dict(other), f, indent=1)
        print("done: %d members" % n)


    def summarise(columns, out):
        by = collections.defaultdict(lambda: {"columns": 0, "unambiguous_columns": 0, "datasets": set(), "members": set(), "headers": collections.Counter(), "why_not": collections.Counter()})
        errors, members = 0, set()
        for line in open(columns, encoding="utf-8"):
            d = json.loads(line)
            if "error" in d:
                errors += 1
                continue
            members.add((d["zip"], d["member"]))
            for c in d["candidates"]:
                b = by[c["type"]]
                b["columns"] += 1
                if c["unambiguous"]:
                    b["unambiguous_columns"] += 1
                    b["datasets"].add(d["zip"])
                    b["members"].add((d["zip"], d["member"]))
                    b["headers"][d["column"].strip().lower()] += 1
                else:
                    b["why_not"][c["why"]] += 1
        summary = {"members_read": len(members), "members_with_errors": errors, "fields": {}}
        for t, b in sorted(by.items(), key=lambda kv: -len(kv[1]["datasets"])):
            summary["fields"][t] = {"columns_matching_header": b["columns"], "unambiguous_columns": b["unambiguous_columns"], "datasets": len(b["datasets"]),
                                    "members": len(b["members"]), "top_headers": b["headers"].most_common(12), "top_reasons_rejected": b["why_not"].most_common(4)}
        with open(out, "w") as f:
            json.dump(summary, f, indent=1)
        print(json.dumps({k: (v["datasets"], v["unambiguous_columns"]) for k, v in summary["fields"].items()}))


    def main():
        ap = argparse.ArgumentParser()
        sub = ap.add_subparsers(dest="cmd", required=True)
        a = sub.add_parser("survey"); a.add_argument("--root", required=True); a.add_argument("--out", required=True)
        a.add_argument("--workers", type=int, default=8); a.add_argument("--sample", type=int, default=2000); a.add_argument("--limit", type=int, default=0)
        b = sub.add_parser("summarise"); b.add_argument("--columns", required=True); b.add_argument("--out", required=True)
        x = ap.parse_args()
        if x.cmd == "survey":
            survey(x.root, x.out, x.workers, x.sample, x.limit)
        else:
            summarise(x.columns, x.out)


    if __name__ == "__main__":
        main()

Check it parses: python3 -I -c "import ast; ast.parse(open('/projects/aiskunks/skills-lexicon-work/job-fields-survey/field_survey.py').read()); print('syntax ok')"

STEP 2. Dry run on a small slice.
Write /projects/aiskunks/skills-lexicon-work/job-fields-survey/dry.sbatch (partition short, 30 minutes, 8 GB, 4 cpus, output /projects/aiskunks/skills-lexicon-work/job-fields-survey/dry-%j.log) that runs: python3 -I field_survey.py survey --root <the dataset folder> --out /projects/aiskunks/skills-lexicon-work/job-fields-survey/dry --workers 4 --limit 60 ; then python3 -I field_survey.py summarise --columns /projects/aiskunks/skills-lexicon-work/job-fields-survey/dry/columns.jsonl --out /projects/aiskunks/skills-lexicon-work/job-fields-survey/dry/summary.json . Submit it and read the log. Report the first lines it prints (how many tabular files, which other file types are in the archives), and show summary.json. If it prints a STOP line or errors, report it exactly (code 5 means the output folder exists).

STEP 3. Full survey.
Write /projects/aiskunks/skills-lexicon-work/job-fields-survey/full.sbatch (partition short, 6 hours, 16 GB, 8 cpus, output /projects/aiskunks/skills-lexicon-work/job-fields-survey/full-%j.log) that runs the survey with --workers 8 --out /projects/aiskunks/skills-lexicon-work/job-fields-survey/full and then the summarise step into /projects/aiskunks/skills-lexicon-work/job-fields-survey/full/summary.json. Submit it, watch squeue -u $USER, read the log. If it will not finish in 6 hours, report how far it got and what limit you would use; do not resubmit with a larger limit without asking.

STEP 4. Report what the survey found.
a. summary.json for the full run: for each field type, the number of datasets and members where an unambiguous column was found, and the twelve most common header names.
b. What the survey could NOT read: the other_members.json counts of file types that are not csv or tsv (json, xlsx, parquet and so on), the number of files with errors, and what fraction of the datasets that is.
c. For each of job_title, company, location, salary, date and skills_list: three randomly chosen datasets (fixed random seed 7) and, for each, the column header and ten values from that column, so I can see whether the survey was right. This is for me to read here; it must not be published.
d. Headers the survey marked as NOT unambiguous although the header names the field (job_title or company or location), with the reason, and five examples of values: so I can see where the checks are too strict or too loose.
e. Duplicate datasets: how many of the datasets share an identical file name and size with another (a cheap sign of repeated or derived datasets).
f. Licences. Join the datasets to the publisher-declared licences in data/source-occurrences/kaggle-publication-2026-10-30/sources.json on the GitHub branch data/kaggle-occurrence-evidence-20261030 (git show origin/data/kaggle-occurrence-evidence-20261030:data/source-occurrences/kaggle-publication-2026-10-30/sources.json ; keyed by dataset_ref), and check whether the cluster ledger has a licence column. Report how many datasets have a recorded licence, how many of those are CC0, CC BY 4.0, MIT, Apache 2.0 or ODC-By, and for job_title, company and location how many unambiguous datasets have one of those licences. The rest have unknown licences and may only be used for private analysis.

STEP 5. Checks.
- The dataset folder is unchanged and the downloads were not disturbed: report whether the number of dataset.zip files only grew while you worked.
- ls -l /projects/aiskunks/skills-lexicon-work/job-fields-survey/full : columns.jsonl, other_members.json and summary.json exist. If columns.jsonl is larger than 40 MB, say so.

STEP 6. Publish the counts, never the values.
- Copy /projects/aiskunks/skills-lexicon-work/job-fields-survey/field_survey.py, /projects/aiskunks/skills-lexicon-work/job-fields-survey/full/summary.json and /projects/aiskunks/skills-lexicon-work/job-fields-survey/full/other_members.json to the Mac with tar over ssh, and columns.jsonl too only if it is under 40 MB (it holds headers and statistical profiles, no values). Verify sha256 on both sides.
- In my local clone: git fetch origin, then create the branch data/job-fields-survey-20261102 from origin/main. Put the files at data/job-fields-survey/ and scripts/job_fields/field_survey.py.
- Write data/job-fields-survey/README.md: what the survey is (which column headers and value behaviour count as unambiguous, in plain words), what it did not read, the date and the number of datasets and members surveyed, that no posting text or values are included, and that the datasets have different publisher-declared licences, so this survey is evidence about structure only.
- Run python3 -I tools/lexicon.py validate in the clone (it must end with 0 errors) and git status (only those files staged). Commit "Job-posting field survey: which fields sit in their own column" and push git push -u origin data/job-fields-survey-20261102. If the push is refused, STOP and report the exact message.

STOP AND ASK IF: the dataset folder or ledger is ambiguous; the dry run fails; the full run fails or will not finish; the folder shrinks or files change while you read; a checksum differs; validate does not end with 0 errors; extra files are staged; the branch exists; the push is refused.

REPORT BACK (short, plain text)
The dataset folder and ledger paths; the dry-run output; job ids and run times; the step 4 results a to f; the step 5 checks; the branch name and commit hash; anything that failed or was skipped. Do not say a check passed unless you ran it and saw it pass.
```
