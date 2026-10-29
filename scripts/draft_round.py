"""Set up and collect a round of parallel drafting, so several agents can draft different tags at once.

    python3 -I scripts/draft_round.py prepare round-01 --agents 3 --size 100
    python3 -I scripts/draft_round.py collect round-01 --agent 1 --model-id claude-sonnet-5-5 --effort xhigh

prepare: takes the next unresolved tags, gives each agent its own slice, and builds for each a private copy of this
repository (no .git) under /home/user/rounds/<round>/a<N>/skills-lexicon with work/candidates.json and work/requests/
ready. The agent only writes work/responses/. collect: runs ingest on this repository, once per agent, on that agent's
requests and responses. Ingest validates the whole dictionary answer by answer, so an answer that clashes with another
agent's entry is rejected and its tag stays unresolved, to be drafted again in a later round with the new entry visible.
"""
import argparse
import datetime
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402
import make_requests as M  # noqa: E402
import tags_to_candidates as T  # noqa: E402

BASE = Path("/home/user/rounds")


def prepare(round_id, agents, size, root=L.ROOT, unsure=False):
    every = T.read_tags(root, [T.TAGS] + list(T.LISTS.values()))
    done = T.resolved(root)
    groups = T.unsure_pool(root, every) if unsure else [g for g in every if L.norm(g["term"]) not in done]
    out = []
    for i in range(1, agents + 1):
        chosen = groups[(i - 1) * size:i * size]
        if not chosen:
            break
        d = BASE / round_id / f"a{i}" / "skills-lexicon"
        if d.exists():
            raise SystemExit(f"{d} exists; use a new round id")
        shutil.copytree(root, d, ignore=shutil.ignore_patterns(".git", "work", "__pycache__"))
        T.main([str(d / "work"), "--root", str(d), "--first", str(size), "--offset", str((i - 1) * size)] + (["--unsure"] if unsure else []))
        M.main([str(d / "work"), "--root", str(d), "--min-postings", "0"])
        out.append((i, len(chosen), d))
    print(f"{len(groups)} unresolved tags; prepared {len(out)} agents")
    for i, n, d in out:
        print(f"  agent {i}: {n} tags in {d}")
    return out


def collect(round_id, agent, model_id, effort, root=L.ROOT, dry=False):
    d = BASE / round_id / f"a{agent}" / "skills-lexicon"
    run = f"{datetime.date.today().isoformat()}-{round_id}-a{agent}"
    r = I.ingest(d / "work", root, "model:" + model_id, run, datetime.date.today().isoformat(), dry, effort=effort, agent="subagent")
    print(f"{run}: new {len(r['new'])}, variants {len(r['variant'])}, not a skill {len(r['not_a_skill'])}, unsure {len(r['unsure'])}, "
          f"rejected {len(r['rejected'])}, claims dropped {r['dropped_claims']}")
    for term, why in r["rejected"]:
        print(f"  rejected {term!r}: {why[:160]}")
    return run, r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("round")
    p.add_argument("--agents", type=int, default=3)
    p.add_argument("--size", type=int, default=100)
    p.add_argument("--unsure", action="store_true", help="tags a model only answered unsure to, for a second model")
    c = sub.add_parser("collect")
    c.add_argument("round")
    c.add_argument("--agent", type=int, required=True)
    c.add_argument("--model-id", required=True)
    c.add_argument("--effort", required=True, choices=sorted(L.EFFORTS))
    c.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "prepare":
        prepare(a.round, a.agents, a.size, unsure=a.unsure)
    else:
        collect(a.round, a.agent, a.model_id, a.effort, dry=a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
