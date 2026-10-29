"""One step of the overnight loop, run whenever a drafting agent reports.

    python3 -I scripts/overnight_step.py collect round-03 2 <task id>

Reads the agent's own transcript for the model and effort it really ran at (never assumed), ingests its answers into this
repository, and records the result. When every agent of the round has been collected it builds the round's batch view, adds a
row to docs/OVERNIGHT.md, validates, commits and pushes the branch, and prepares the next round (the tags rejected for
clashing with a sibling's entry are simply unresolved again, so they come round once more, now as variants).
"""
import collections
import datetime
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import draft_round as D  # noqa: E402
import lexicon as L  # noqa: E402

TASKS = Path("/tmp/claude-0/-home-user/51e956f7-ba36-520a-915f-8cd07d641b86/tasks")
ROOT = L.ROOT
DATE = datetime.date.today().isoformat()


def transcript(task_id):
    """The model and effort a subagent actually ran at, from its transcript."""
    text = (TASKS / f"{task_id}.output").read_text("utf-8", "replace")
    pick = lambda key: collections.Counter(re.findall(rf'"{key}":"([^"]+)"', text)).most_common(1)  # noqa: E731
    m, e = pick("model"), pick("effort")
    if not m or not e:
        raise SystemExit(f"no model or effort found in the transcript of {task_id}")
    return m[0][0], e[0][0]


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def finish(round_id, state):
    plan = json.loads((D.BASE / round_id / "plan.json").read_text("utf-8"))
    runs = [state[str(i)]["run"] for i in plan["agents"]]
    out = subprocess.run([sys.executable, "-I", "tools/batch.py", *runs], cwd=ROOT, capture_output=True, text=True)
    counts = json.loads(Path(ROOT / "data" / sorted(p.name for p in (ROOT / "data").glob("skills_batch_*.json"))[-1]).read_text("utf-8"))["batch"]["counts"]
    rej = sum(state[str(i)]["rejected"] for i in plan["agents"])
    entries = len(list((ROOT / "entries").glob("*.json")))
    rn = round_id.replace("round-", "")
    with open(ROOT / "docs" / "OVERNIGHT.md", "a", encoding="utf-8") as f:
        f.write(f"\n| round {rn} | {', '.join(r.split('-round-')[1] for r in runs)} | {counts['new_entries']} new | {counts['variants_added']} variants | "
                f"{counts['not_a_skill']} not a skill | {counts['unsure']} unsure | {rej} rejected | {entries} entries in all |\n")
    v = subprocess.run([sys.executable, "-I", "tools/lexicon.py", "validate"], cwd=ROOT, capture_output=True, text=True).stdout.strip().splitlines()
    if " 0 errors" not in v[-2]:
        raise SystemExit("validation failed after the round; not committing:\n" + "\n".join(v[-4:]))
    git("add", "-A")
    git("commit", "-q", "-m", f"{round_id}: {counts['new_entries']} new entries, {counts['variants_added']} variants, {counts['not_a_skill']} not a skill, {counts['unsure']} unsure, "
        f"{rej} rejected; {entries} entries\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_019HJ8tnR2iarmEKD9F3uUo2")
    push = git("push", "origin", "overnight-1")
    print(f"ROUND DONE: {counts}; {rej} rejected; {entries} entries; push: {(push.stderr or push.stdout).strip().splitlines()[-1] if (push.stderr or push.stdout).strip() else 'ok'}")
    nxt = f"round-{int(rn) + 1:02d}"
    try:
        D.prepare(nxt, len(plan["agents"]), plan["size"])
        print(f"NEXT ROUND READY: {nxt}")
    except SystemExit as e:
        print("could not prepare the next round:", e)


def main(argv=None):
    cmd, round_id, agent, task = (argv or sys.argv[1:])[:4]
    assert cmd == "collect"
    model, effort = transcript(task)
    print(f"transcript says {model} at {effort}")
    run, r = D.collect(round_id, int(agent), model, effort)
    sp = D.BASE / round_id / "state.json"
    state = json.loads(sp.read_text("utf-8")) if sp.exists() else {}
    state[str(agent)] = {"run": run, "task": task, "model": model, "effort": effort, "rejected": len(r["rejected"]),
                         "new": len(r["new"]), "unsure": len(r["unsure"])}
    sp.write_text(json.dumps(state, indent=1) + "\n", "utf-8")
    plan = json.loads((D.BASE / round_id / "plan.json").read_text("utf-8"))
    missing = [i for i in plan["agents"] if str(i) not in state]
    if missing:
        v = subprocess.run([sys.executable, "-I", "tools/lexicon.py", "validate"], cwd=ROOT, capture_output=True, text=True).stdout.strip().splitlines()
        if " 0 errors" not in v[-2]:
            raise SystemExit("validation failed; not committing:\n" + "\n".join(v[-4:]))
        git("add", "-A")      # commit each agent as it is collected, so nothing is ever left uncommitted
        git("commit", "-q", "-m", f"{round_id} agent {agent} ingested: {len(r['new'])} new, {len(r['variant'])} variants, {len(r['not_a_skill'])} not a skill, "
            f"{len(r['unsure'])} unsure, {len(r['rejected'])} rejected\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_019HJ8tnR2iarmEKD9F3uUo2")
        git("push", "origin", "overnight-1")
        print(f"committed and pushed; waiting for agents {missing}")
    else:
        finish(round_id, state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
