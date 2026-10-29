"""Add `certification`, `certification_scope` or `language_type` to entries that already exist.

    python3 -I tools/annotate.py answers.json --model-id claude-sonnet-5-5 --effort xhigh --run 2026-10-29-scope [--dry-run]

answers.json maps an entry's key (its file name without .json) or its id to the model's answer, in the shape
SKILL.md gives for those fields:
    {"passenger-endorsement": {"certification_scope": {"value": "many-issuers", "basis": "general-knowledge"},
                               "annotation_note": ""}}
The same rules as ingest apply, because it is the same code: the operator names the model and the run, a guessed
basis is dropped, and every saved annotation gets its own `drafted` evidence record. An entry that already has the
field is left alone (nothing is overwritten), and a `reviewed` entry is refused, since adding a claim would
unreview it. Nothing is saved unless the whole dictionary still validates.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402

FIELDS = ("certification", "certification_scope", "language_type")


def apply(entries, answers, by, run, today):
    """Return (changed entries, report lines). `entries` is modified in place."""
    changed, report = [], []
    for ref, ans in answers.items():
        e = next((x for x in entries if x.get("key") == ref or x["_file"] == f"{ref}.json"), None) or L.find(entries, ref)
        if e is None:
            report.append(f"{ref}: no such entry")
            continue
        if e["status"] == "reviewed":
            report.append(f"{ref}: reviewed; adding a claim would unreview it, so propose it as a pull request")
            continue
        todo = {k: ans[k] for k in FIELDS if k in ans}
        have = [k for k in todo if k in e]
        for k in have:
            todo.pop(k)
            report.append(f"{ref}: already has {k}; left alone")
        if not todo:
            continue
        # certification_scope needs certification: true, either already on the entry or answered in the same call
        origin = e["provenance"].get("legacy_tag")
        req = {"origin": origin} if origin else {}
        ev, dropped = [], []
        I.annotate({**todo, "annotation_note": ans.get("annotation_note", "")}, req, e, ev, dropped, by, run, today)
        e.setdefault("evidence", []).extend(ev)
        report += [f"{ref}: dropped {d}" for d in dropped]
        if ev:
            changed.append(e)
            report.append(f"{ref}: added {', '.join(x['field'] for x in ev)}")
    return changed, report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("answers")
    ap.add_argument("--model-id", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--effort", required=True, choices=sorted(L.EFFORTS), help="the effort level the model ran at")
    ap.add_argument("--agent", default="main-session", help="main-session, or subagent")
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    entries, errs = L.load(Path(a.root) / "entries")
    if errs + L.validate(entries):
        raise SystemExit("dictionary does not validate before annotating; fix it first")
    answers = json.loads(Path(a.answers).read_text("utf-8"))
    changed, report = apply(entries, answers, "model:" + a.model_id, a.run, a.date)
    problems = L.validate(entries)
    if problems:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(problems[:4]))
    if not a.dry_run:
        L.register_run(a.root, a.run, a.model_id, a.effort, a.agent, date=a.date)
        for e in changed:
            (Path(a.root) / "entries" / e["_file"]).write_text(
                json.dumps(I.clean(e), indent=1, ensure_ascii=False) + "\n", "utf-8")
    print("\n".join(report))
    print(("DRY RUN: nothing written. " if a.dry_run else "") + f"{len(changed)} entries annotated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
