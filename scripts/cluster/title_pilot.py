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
