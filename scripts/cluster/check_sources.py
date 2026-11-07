#!/usr/bin/env python3
"""Counts for the three sources, and a few lookups. Python 3.9. Reads only."""
import glob
import gzip
import os
import re
import sys

PWN = "/projects/aiskunks/wordnet/pwn-3.1"
OEWN = sorted(glob.glob("/projects/aiskunks/wordnet/oewn-*"))
ONET = sorted(glob.glob("/projects/aiskunks/onet/*"))
ESCO = sorted(glob.glob("/projects/aiskunks/esco/*"))


def pwn_counts():
    dict_dir = next((os.path.join(r, "dict") for r, d, f in os.walk(PWN) if "dict" in d), None)
    if not dict_dir:
        print("PWN: no dict folder found under", PWN)
        return None
    out = {}
    for pos in ("noun", "verb", "adj", "adv"):
        n = 0
        with open(os.path.join(dict_dir, "data." + pos), encoding="utf-8", errors="replace") as f:
            for line in f:
                if not line.startswith("  "):
                    n += 1
        out[pos] = n
    print("PWN 3.1 synsets by part of speech:", out, "total", sum(out.values()))
    return dict_dir


def pwn_lookup(dict_dir, words):
    for w in words:
        hits = []
        for pos in ("noun", "verb", "adj", "adv"):
            with open(os.path.join(dict_dir, "index." + pos), encoding="utf-8", errors="replace") as f:
                for line in f:
                    if line.startswith(w + " "):
                        hits.append((pos, int(line.split()[2])))
                        break
        print("  lemma %-12s senses by pos: %s" % (w, hits or "none"))


def oewn_counts():
    for d in OEWN:
        for p in glob.glob(os.path.join(d, "*.xml*")):
            op = gzip.open if p.endswith(".gz") else open
            n = 0
            with op(p, "rt", encoding="utf-8", errors="replace") as f:
                for line in f:
                    n += len(re.findall(r"<Synset ", line))
            print("OEWN", os.path.basename(p), "synsets:", n)


def onet_counts():
    for d in ONET:
        for p in sorted(glob.glob(os.path.join(d, "**", "*.txt"), recursive=True)):
            with open(p, encoding="utf-8", errors="replace") as f:
                n = sum(1 for _ in f)
            print("O*NET", os.path.relpath(p, d), "lines:", n)


def esco_counts():
    for d in ESCO:
        for p in sorted(glob.glob(os.path.join(d, "**", "*.csv"), recursive=True)):
            with open(p, encoding="utf-8", errors="replace") as f:
                n = sum(1 for _ in f)
            print("ESCO", os.path.relpath(p, d), "lines:", n)


if __name__ == "__main__":
    dd = pwn_counts()
    if dd:
        pwn_lookup(dd, ["python", "java", "negotiation", "reasoning", "auditing", "kubernetes", "git", "jira", "swahili"])
    oewn_counts()
    onet_counts()
    esco_counts()