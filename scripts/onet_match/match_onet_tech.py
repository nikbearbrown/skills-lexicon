#!/usr/bin/env python3
"""Match the software and technology names in an O*NET table to the skills lexicon. Python 3.9. Reads only.

Usage: python3 -I match_onet_tech.py --lexicon DIR --table FILE --release 31.0 --out OUTDIR [--show 30]
The table is tab separated with a header: an occupation code column, an example (the technology's name), commodity code and title,
and the Hot Technology and In Demand flags (Y or N). One output line per distinct example name: how many occupations list it, whether
it is flagged hot or in demand, and which lexicon entries it matches (exactly, or because the example contains an entry's name).
It decides nothing: a contained name is only a hint for a person."""
import argparse
import collections
import csv
import json
import os
import re
import sys

COLS = {"soc": ("o*net-soc code", "o*net-soc", "onet-soc code"), "example": ("example", "workplace example", "technology skill", "name"),
        "code": ("commodity code", "element id"), "title": ("commodity title", "element name"), "hot": ("hot technology",), "demand": ("in demand",)}
TRAIL = re.compile(r"\s+(software|platform|tools?|framework|library|application|system|service)$", re.I)
PAREN = re.compile(r"\s*\([^)]*\)\s*")


def find_cols(header):
    low = {h.strip().lower(): h for h in header}
    out = {}
    for k, names in COLS.items():
        out[k] = next((low[n] for n in names if n in low), None)
    return out


def keys_of(name, norm):
    base = norm(name.replace("®", "").replace("™", ""))
    ks = [base]
    for k in (PAREN.sub(" ", base).strip(), TRAIL.sub("", base).strip(), TRAIL.sub("", PAREN.sub(" ", base).strip()).strip()):
        if k and k not in ks:
            ks.append(k)
    return ks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", required=True)
    ap.add_argument("--table", required=True)
    ap.add_argument("--release", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--show", type=int, default=30)
    a = ap.parse_args()
    if os.path.exists(os.path.join(a.out, "matches.jsonl")):
        print("STOP: %s already holds results" % a.out, file=sys.stderr)
        sys.exit(5)
    sys.path.insert(0, os.path.join(a.lexicon, "tools"))
    import lexicon as L
    entries, errs = L.load(os.path.join(a.lexicon, "entries"))
    entries = [e for e in entries if e.get("status") != "deprecated"]
    forms = {}
    for e in entries:
        for i, f in enumerate(L.forms(e)):
            forms.setdefault(L.norm(f["label"]), []).append((e["id"], e["key"], "preferred" if i == 0 else "variant"))
    with open(a.table, encoding="utf-8", errors="replace", newline="") as f:
        rd = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        header = next(rd)
        cols = find_cols(header)
        if not cols["example"] or not cols["soc"]:
            print("STOP: cannot find an occupation code and an example column; the header is %s" % header, file=sys.stderr)
            sys.exit(2)
        idx = {k: header.index(v) for k, v in cols.items() if v}
        rows = 0
        agg = {}
        for r in rd:
            if len(r) < len(header):
                continue
            rows += 1
            ex = r[idx["example"]].strip()
            if not ex:
                continue
            d = agg.setdefault(ex, {"soc": set(), "hot_soc": set(), "demand_soc": set(), "codes": set(), "titles": set()})
            soc = r[idx["soc"]]
            d["soc"].add(soc)
            if "hot" in idx and r[idx["hot"]].strip().upper() == "Y":
                d["hot_soc"].add(soc)
            if "demand" in idx and r[idx["demand"]].strip().upper() == "Y":
                d["demand_soc"].add(soc)
            if "code" in idx:
                d["codes"].add(r[idx["code"]])
            if "title" in idx:
                d["titles"].add(r[idx["title"]])
    out = []
    for ex, d in agg.items():
        exact = []
        for k in keys_of(ex, L.norm):
            for eid, ekey, kind in forms.get(k, []):
                if (eid, ekey) not in [(x["entry_id"], x["entry_key"]) for x in exact]:
                    exact.append({"entry_id": eid, "entry_key": ekey, "via": k, "form_kind": kind})
        contains = []
        if not exact:
            toks = L.norm(ex).split()
            seen = set()
            for n in range(min(4, len(toks)), 0, -1):
                for i in range(0, len(toks) - n + 1):
                    g = " ".join(toks[i:i + n])
                    if len(g) >= 4 and g in forms and g != L.norm(ex):
                        for eid, ekey, kind in forms[g]:
                            if eid not in seen:
                                seen.add(eid)
                                contains.append({"entry_id": eid, "entry_key": ekey, "contained_form": g})
        out.append({"example": ex, "release": a.release, "n_occupations": len(d["soc"]), "n_hot_occupations": len(d["hot_soc"]),
                    "n_in_demand_occupations": len(d["demand_soc"]), "hot": bool(d["hot_soc"]), "in_demand": bool(d["demand_soc"]),
                    "commodity_codes": sorted(d["codes"]), "commodity_titles": sorted(d["titles"]),
                    "match": "exact" if exact else "contains" if contains else "none", "entries": exact, "contained_entries": contains[:5]})
    out.sort(key=lambda x: (-x["n_occupations"], x["example"].casefold()))
    os.makedirs(a.out, exist_ok=True)
    tmp = os.path.join(a.out, ".tmp-")
    with open(tmp + "matches.jsonl", "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    cnt = collections.Counter(o["match"] for o in out)
    hot = collections.Counter(o["match"] for o in out if o["hot"])
    summary = {"release": a.release, "table": os.path.basename(a.table), "rows": rows, "distinct_examples": len(out), "match": dict(cnt),
               "hot_examples": sum(1 for o in out if o["hot"]), "hot_match": dict(hot), "in_demand_examples": sum(1 for o in out if o["in_demand"]),
               "entries_in_lexicon": len(entries), "columns_used": {k: v for k, v in cols.items()}}
    with open(tmp + "summary.json", "w") as f:
        json.dump(summary, f, indent=1)
    for n in ("matches.jsonl", "summary.json"):
        os.rename(tmp + n, os.path.join(a.out, n))
    print(json.dumps(summary))
    print("\nTop %d unmatched by occupations (hot or in-demand first):" % a.show)
    un = [o for o in out if o["match"] == "none"]
    un.sort(key=lambda o: (-(o["hot"] or o["in_demand"]), -o["n_occupations"]))
    for o in un[:a.show]:
        print("  %-44s occ=%-4d hot=%-5s demand=%s" % (o["example"][:44], o["n_occupations"], o["hot"], o["in_demand"]))


if __name__ == "__main__":
    main()

