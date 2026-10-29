"""Turn the legacy tag lists into candidates, so the same pipeline can draft entries from them.

    python3 -I tools/tags_to_candidates.py work --sample 100 --seed 1 --quota Skill=75,Certification=15,Language=10 --pool tags
    python3 -I tools/tags_to_candidates.py work --first 100        # the next 100 unresolved tags, all three lists

Reads data/skills_tags.csv, data/skills-certification.csv and data/skills-language.csv (all Tag, Class).
Tags that differ only in case are one candidate; its origin lists every file, row and class so a conflict
stays visible. A tag that appears in the certification or language list gets that list's name in `in_lists`:
a hint for the model to check, not an answer. Tags already resolved (a name or variant of an entry, or a
recorded decision) are skipped, so a run can be repeated. Writes work/candidates.json. A candidate has no
postings and no quotes: the model has only the name, and the request says so.
"""
import argparse
import csv
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402

TAGS = "data/skills_tags.csv"
LISTS = {"certification": "data/skills-certification.csv", "language": "data/skills-language.csv"}


def read_tags(root, files):
    """Group rows from several files by normalised tag. CSV line 1 is the header, so the first tag is row 2."""
    groups = {}
    for name in files:
        with open(Path(root) / name, encoding="utf-8", newline="") as f:
            for i, r in enumerate(csv.DictReader(f), start=2):
                tag = (r.get("Tag") or "").strip()
                if not tag:
                    continue
                g = groups.setdefault(L.norm(tag), {"term": tag, "sources": {}})
                s = g["sources"].setdefault(name, {"file": name, "rows": [], "classes": []})
                s["rows"].append(i)
                s["classes"].append((r.get("Class") or "").strip())
    return list(groups.values())


def classes(g):
    return sorted({c for s in g["sources"].values() for c in s["classes"]})


def in_lists(g):
    return [k for k, f in LISTS.items() if f in g["sources"]]


def resolved(root):
    """Normalised forms already covered: entry names and variants, and terms with a recorded decision."""
    entries, _ = L.load(Path(root) / "entries")
    seen = {L.norm(fm["label"]) for e in entries for fm in L.forms(e)}
    dec = Path(root) / "data" / "term-decisions.json"
    if dec.exists():
        seen |= {L.norm(d["term"]) for d in json.loads(dec.read_text("utf-8"))}
    return seen


def origin(g):
    cl = classes(g)
    o = {"sources": [{"file": s["file"], "rows": s["rows"], "class": "/".join(sorted(set(s["classes"])))}
                     for s in g["sources"].values()],
         "class": "/".join(cl), "in_lists": in_lists(g)}
    if len(cl) > 1:
        o["class_conflict"] = True
    return o


def candidate(g):
    return {"term": g["term"], "n_postings": 0, "quotes": [], "origin": origin(g)}


def sample(groups, n, seed, quota):
    """Reproducible stratified sample by first class. Tags whose class conflicts are always included."""
    rnd = random.Random(seed)
    first = lambda g: classes(g)[0]  # noqa: E731
    chosen = [g for g in groups if len(classes(g)) > 1]
    left = dict(quota)
    for g in chosen:
        if left.get(first(g), 0) > 0:
            left[first(g)] -= 1
    for c, k in left.items():
        pool = [g for g in groups if first(g) == c and g not in chosen]
        chosen += rnd.sample(pool, min(k, len(pool)))
    pool = [g for g in groups if g not in chosen]
    chosen += rnd.sample(pool, max(0, min(n - len(chosen), len(pool))))
    return chosen[:n]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work")
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--sample", type=int, help="a reproducible stratified sample of this many tags")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--quota", default="", help="Class=N,... for --sample, e.g. Skill=75,Certification=15,Language=10")
    ap.add_argument("--first", type=int, help="the first N unresolved tags in file order")
    ap.add_argument("--offset", type=int, default=0, help="with --first: skip this many unresolved tags first, so parallel runs get different tags")
    ap.add_argument("--pool", choices=["tags", "all"], default="all",
                    help="draw from skills_tags.csv only, or from all three lists (default)")
    a = ap.parse_args(argv)
    if bool(a.sample) == bool(a.first):
        ap.error("give exactly one of --sample or --first")
    every = read_tags(a.root, [TAGS] + list(LISTS.values()))
    done = resolved(a.root)
    groups = [g for g in every if L.norm(g["term"]) not in done and (a.pool == "all" or TAGS in g["sources"])]
    if a.first:
        chosen = groups[a.offset:a.offset + a.first]
    else:
        quota = {k: int(v) for k, v in (p.split("=") for p in a.quota.split(",") if p)}
        chosen = sample(groups, a.sample, a.seed, quota)
    out = Path(a.work)
    out.mkdir(parents=True, exist_ok=True)
    (out / "candidates.json").write_text(json.dumps([candidate(g) for g in chosen], indent=1, ensure_ascii=False) + "\n", "utf-8")
    by = {}
    for g in chosen:
        by[classes(g)[0]] = by.get(classes(g)[0], 0) + 1
    print(f"{len(chosen)} candidates from {len(groups)} unresolved tags {dict(sorted(by.items()))} -> {out / 'candidates.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
