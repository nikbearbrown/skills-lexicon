# Match O*NET technologies to the lexicon (hot technology, in demand)

**Status: NOT RUN**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer).

GOAL
Find out which software and technologies that O*NET lists for occupations are already in the skills lexicon and which are missing, with O*NET's own "Hot Technology" and "In Demand" flags as the demand signal. Run it on the current O*NET release (31.0) and on the older one (30.2) for comparison, then publish the results on a new branch of the skills-lexicon GitHub repository so Claude Cloud can read them. Nothing is decided here: the job records matches, hints and counts.

PATHS (use exactly these; invent none)
- Read only: /projects/aiskunks/onet/31.0/ and /projects/aiskunks/onet/30.2/ (each with its extracted text tables; file names contain spaces, do not rename anything)
- Read only: /projects/aiskunks/skills-lexicon (git checkout of the lexicon; do not edit it)
- Write only: /projects/aiskunks/skills-lexicon-work/onet-match/ (create it), with sub-folders 31.0 and 30.2 for results
- On the Mac: my local clone of the skills-lexicon repository (under Documents/CoWork/bear-textbooks/books/skills-lexicon); use a temporary folder outside it for copies

RULES
No sudo. Stay inside /projects/aiskunks. No passwords, keys or tokens anywhere. Delete nothing. Many small files are slow on /projects: this job writes a handful. Python on the login node is 3.9; the script below is written for it. Run the matching as a Slurm batch job. Use tar over ssh to copy to the Mac (not rsync). Do not touch main, do not merge, do not open a pull request. If anything differs from what is described here, or fails, stop and report instead of improvising.

STEP 0. Look at the tables first (read only; run on the login node, it is quick).
For each of these files in /projects/aiskunks/onet/31.0/ report the exact path, the line count, and the first three lines (the header and two rows): Software Skills.txt, Essential Skills.txt, Transferable Skills.txt, Knowledge.txt, Abilities.txt, Work Activities.txt, Occupation Data.txt. If a file name differs, find the real one with ls and say so. Do the same for Technology Skills.txt and Skills.txt in /projects/aiskunks/onet/30.2/. For Software Skills.txt (31.0) and Technology Skills.txt (30.2) also report how many rows have Hot Technology = Y and how many have In Demand = Y (use the column names the file actually has). If the header of either table has no column holding the technology's name or no occupation code column, STOP and show me the header.

STEP 1. Write the script.
  mkdir -p /projects/aiskunks/skills-lexicon-work/onet-match
Write this file exactly to /projects/aiskunks/skills-lexicon-work/onet-match/match_onet_tech.py :

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

    COLS = {"soc": ("o*net-soc code", "o*net-soc", "onet-soc code"), "example": ("example", "technology skill", "name"),
            "code": ("commodity code",), "title": ("commodity title",), "hot": ("hot technology",), "demand": ("in demand",)}
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

Check it parses: python3 -I -c "import ast; ast.parse(open('/projects/aiskunks/skills-lexicon-work/onet-match/match_onet_tech.py').read()); print('syntax ok')"

STEP 2. Run it (two runs, one batch file).
Write /projects/aiskunks/skills-lexicon-work/onet-match/run.sbatch exactly:

    #!/bin/bash
    #SBATCH --job-name=onet-match
    #SBATCH --partition=short
    #SBATCH --time=00:30:00
    #SBATCH --mem=4G
    #SBATCH --cpus-per-task=1
    #SBATCH --output=/projects/aiskunks/skills-lexicon-work/onet-match/run-%j.log
    cd /projects/aiskunks/skills-lexicon-work/onet-match
    python3 -I match_onet_tech.py --lexicon /projects/aiskunks/skills-lexicon --table "/projects/aiskunks/onet/31.0/Software Skills.txt" --release 31.0 --out /projects/aiskunks/skills-lexicon-work/onet-match/31.0 --show 40
    echo "exit status $?"
    python3 -I match_onet_tech.py --lexicon /projects/aiskunks/skills-lexicon --table "/projects/aiskunks/onet/30.2/Technology Skills.txt" --release 30.2 --out /projects/aiskunks/skills-lexicon-work/onet-match/30.2 --show 40
    echo "exit status $?"

Submit with sbatch, watch squeue -u $USER, read the log. Both "exit status" lines must be 0. If the script prints a STOP line, report it exactly (code 2: header differs; 5: output folder exists).

STEP 3. Checks (run on the login node).
a. Show both summary.json files. Report: rows, distinct examples, how many matched exactly, how many only "contains" an entry's name, how many none, and the same split for the hot examples.
b. Look up these names in each matches.jsonl (case-insensitive substring of the example) and print a short table for each hit: example, occupations, hot, in demand, match, entry keys: git, jira, kubernetes, mysql, mongodb, jenkins, docker, python, sql, tableau, excel, aws, azure, kafka, snowflake, splunk, terraform, ansible, react, django, github. Do not filter them out; I want to see what O*NET calls each (for example Atlassian JIRA).
c. Compare the releases: how many 31.0 examples flagged hot are not in the 30.2 table at all, and how many 30.2 hot examples are absent from 31.0. Give five examples of each.
d. The lexicon checkout is untouched: git -C /projects/aiskunks/skills-lexicon status --porcelain prints nothing.
e. File sizes: ls -l /projects/aiskunks/skills-lexicon-work/onet-match/31.0 /projects/aiskunks/skills-lexicon-work/onet-match/30.2 . If the four result files together are over 30 MB, STOP and tell me.

STEP 4. Publish.
- Copy /projects/aiskunks/skills-lexicon-work/onet-match/31.0/matches.jsonl, summary.json, /projects/aiskunks/skills-lexicon-work/onet-match/30.2/matches.jsonl, summary.json and /projects/aiskunks/skills-lexicon-work/onet-match/match_onet_tech.py to a temporary folder on the Mac with tar over ssh. Verify sha256 on both sides (sha256sum on the cluster, shasum -a 256 on the Mac); they must match.
- In my local clone: git fetch origin, then create the branch data/onet-tech-match-20261101 from origin/main. Put the files at data/onet-match/31.0/ (matches.jsonl, summary.json), data/onet-match/30.2/ (the same two) and scripts/onet_match/match_onet_tech.py.
- Write data/onet-match/README.md: what the files are (one line per distinct technology example in O*NET's table, with the number of occupations that list it, the Hot Technology and In Demand flags, and the lexicon entries it matches exactly or hints at); that a "contains" hint is not a match; the two releases and their table names (31.0 Software Skills, 30.2 Technology Skills); that the O*NET data is used under CC BY 4.0 with this notice: "This product includes information from the O*NET 31.0 and 30.2 Databases by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), used under the CC BY 4.0 license. O*NET(R) is a trademark of USDOL/ETA. The counts and matches here were produced from that information by the Skills Lexicon project; USDOL/ETA has not approved, endorsed or tested these modifications."; and the sha256 of each file.
- Run python3 -I tools/lexicon.py validate in the clone: it must end with 0 errors. Run git status: only the files named above may be staged. Commit with the message "O*NET technology match, releases 31.0 and 30.2 (hot technology and in-demand signal)" and push with git push -u origin data/onet-tech-match-20261101. If the push is refused, STOP and report the exact message.

STOP AND ASK IF: a path above is missing; a table header differs from what the script needs; any exit status is not 0; result files exceed the limit; a checksum differs; validate does not end with 0 errors; extra files are staged; the branch already exists; the push is refused.

REPORT BACK (short, plain text)
Step 0 headers and counts; job id and run time; the two summary.json contents; the table from check b; the answers to c, d and e; the branch name and commit hash; anything that failed or was skipped. Do not say a check passed unless you ran it and saw it pass.
```
