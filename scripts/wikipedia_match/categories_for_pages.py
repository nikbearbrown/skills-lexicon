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
