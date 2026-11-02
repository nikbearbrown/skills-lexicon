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
