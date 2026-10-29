"""One-off: record the runs and votes made before the run registry and the vote ledger existed.

    python3 -I scripts/backfill_provenance.py --blind-root /home/user/agent2/skills-lexicon

Registers each run's model and effort in data/runs.json (read from the session settings for the main session, and
from each subagent's transcript for the subagents), then writes one vote per tag per run into
data/assessments.jsonl, from the entries and decisions those runs saved. Refuses to run twice.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import assess as AS  # noqa: E402
import compare_runs as C  # noqa: E402
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402

MODEL, DATE = "claude-sonnet-5-5", "2026-10-29"
MAIN = "main session; model and effort read from the session settings"
SUB = "subagent; model and effort read from the subagent's own transcript"
RUNS = {
    "2026-10-29-pilot-100-tags": ("main-session", MAIN),
    "2026-10-29-scope-annotation": ("main-session", MAIN),
    "2026-10-29-scope-annotation-batch-002": ("main-session", MAIN),
    "2026-10-29-batch-002": ("subagent", SUB),
    "2026-10-29-pilot-100-tags-blind-redraft": ("subagent", SUB),
}


def votes(root, run, orig, in_main):
    who = AS.model_assessor(MODEL, "xhigh")
    out = []
    for key, o in sorted(C.outcomes(root, run).items()):
        tag = orig.get(key, o["term"])
        d = o["decision"]
        if d == "new":
            kw = {"entry": o["entry"]["id"]} if in_main else {"proposed_name": o["entry"]["preferred_name"]}
            out.append(AS.vote(tag, "yes", who, run, DATE, **kw))
        elif d == "variant_of":
            out.append(AS.vote(tag, "yes", who, run, DATE, variant_of=o["target_id"]))
        else:
            out.append(AS.vote(tag, {"not_a_skill": "no", "unsure": "unsure"}[d], who, run, DATE, reason=o["reason"]))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--blind-root", required=True)
    a = ap.parse_args(argv)
    if AS.load(a.root):
        raise SystemExit("data/assessments.jsonl already has votes; not running twice")
    for label, (agent, note) in RUNS.items():
        L.register_run(a.root, label, MODEL, "xhigh", agent, date=DATE, note=note)
    orig = {L.norm(g["term"]): g["term"] for g in T.read_tags(a.root, [T.TAGS] + list(T.LISTS.values()))}
    recs = (votes(a.root, "2026-10-29-pilot-100-tags", orig, True) + votes(a.root, "2026-10-29-batch-002", orig, True)
            + votes(a.blind_root, "2026-10-29-pilot-100-tags-blind-redraft", orig, False))
    AS.append(a.root, recs)
    print(f"registered {len(RUNS)} runs; recorded {len(recs)} votes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
