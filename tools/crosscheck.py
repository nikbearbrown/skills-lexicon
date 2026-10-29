"""Record a second, independent draft of the same tags as checks on the first draft's entries.

    python3 -I tools/crosscheck.py --a-root . --a-run <first run> --b-root <other folder> --b-run <second run>

Both runs drafted the same tags. For each tag that became a new entry in both, this compares the claims `kind`,
`certification` and `language_type`, and writes a `checked` evidence record on the first draft's entry for each: `supports`
when the second draft gave the same value, `contradicts` (with the value it gave) when it did not. The second run must
already be in data/runs.json, which says which model and effort made it. A model checking a model is recorded and shown,
but it never backs a claim, and an unresolved `contradicts` blocks `reviewed` until a person settles it. Tags one
draft made an entry for and the other did not are votes, not claims: see tools/assess.py.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import compare_runs as C  # noqa: E402
import lexicon as L  # noqa: E402

FIELDS = ("kind", "certification", "language_type")


def say(v):
    return "not a language" if v is None else str(v)


def crosscheck(a_root, a_run, b_root, b_run, model, effort, today):
    """Return (entries changed in memory, [(entry file, field, outcome)])."""
    A, B = C.outcomes(a_root, a_run), C.outcomes(b_root, b_run)
    entries, _ = L.load(Path(a_root) / "entries")
    by_id = {e["id"]: e for e in entries}
    log = []
    for key, x in sorted(A.items()):
        y = B.get(key)
        if x["decision"] != "new" or not y or y["decision"] != "new":
            continue
        e, other = by_id[x["entry"]["id"]], y["entry"]
        for f in FIELDS:
            if f not in e or any(v.get("field") == f and v.get("run") == b_run for v in e.get("evidence", [])):
                continue                       # nothing to check, or already recorded
            theirs = L.KIND_ALIASES.get(other.get(f), other.get(f)) if f == "kind" else other.get(f)
            same = e[f] == theirs
            rec = {"field": f, "by": f"model:{model}", "action": "checked", "outcome": "supports" if same else "contradicts",
                   "date": today, "run": b_run,
                   "note": f"second draft ({effort}) gave the same value" if same else f"second draft ({effort}) said {say(theirs)}"[:200]}
            e.setdefault("evidence", []).append(rec)
            log.append((e["_file"], f, rec["outcome"]))
    return entries, log


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a-root", default=str(L.ROOT))
    ap.add_argument("--a-run", required=True)
    ap.add_argument("--b-root", required=True)
    ap.add_argument("--b-run", required=True)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    reg = L.load_runs(a.a_root).get(a.b_run)
    if not reg:
        raise SystemExit(f"{a.b_run!r} is not in data/runs.json; register the model and effort that made it first")
    entries, log = crosscheck(a.a_root, a.a_run, a.b_root, a.b_run, reg["model"], reg["effort"], a.date)
    problems = L.validate(entries) + L.check_runs(entries, L.load_runs(a.a_root))
    if problems:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(problems[:4]))
    touched = {f for f, _, _ in log}
    if not a.dry_run:
        for e in entries:
            if e["_file"] in touched:
                (Path(a.a_root) / "entries" / e["_file"]).write_text(
                    json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n", "utf-8")
    n_ok = sum(1 for _, _, o in log if o == "supports")
    print(("DRY RUN: nothing written. " if a.dry_run else "") + f"{len(log)} checks on {len(touched)} entries: {n_ok} agree, {len(log) - n_ok} disagree")
    for f, field, o in log:
        if o == "contradicts":
            print(f"  disagrees: {f[:-5]} · {field}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
