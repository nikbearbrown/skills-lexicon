"""The vote ledger: who thinks each tag is a skill, is not a skill, or is unsure.

    python3 -I tools/assess.py add "Zerto" yes --human Bear
    python3 -I tools/assess.py add "Pedals" no --model claude-opus-5-5 --effort high --run 2026-11-02-second-opinion --reason "a physical part"
    python3 -I tools/assess.py tally [--splits] [--tag Zerto]

data/assessments.jsonl holds one line per vote: the tag, the answer (yes, no or unsure), who gave it (a person, or
a model with the effort it ran at), the run, the date, and a reason when the answer is no or unsure. Any number of
people and models can vote on one tag. A tag listed in one of the legacy tag lists also counts as one vote for
"skill": it is worked out from the lists, not stored. Votes never change an entry on their own. A vote does not back
a claim; it shows who thinks what, and where they disagree.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402

FILE = "data/assessments.jsonl"
ANSWERS = ("yes", "no", "unsure")
LEGACY = {"type": "legacy-list", "name": "legacy tag lists"}


def load(root=L.ROOT):
    p = Path(root) / FILE
    return [json.loads(x) for x in p.read_text("utf-8").splitlines() if x.strip()] if p.exists() else []


def who(a):
    """A short, comparable name for an assessor."""
    if a["type"] == "model":
        return f"{a['model']} ({a['effort']})"
    return a.get("name", a["type"])


def identity(rec):
    a = rec["assessor"]
    return (rec["key"], rec.get("question", "skill"), a["type"], a.get("model") or a.get("name"), a.get("effort"), rec.get("run"))


def model_assessor(model, effort):
    if effort not in L.EFFORTS:
        raise ValueError(f"effort must be one of {sorted(L.EFFORTS)}")
    return {"type": "model", "model": model, "effort": effort}


def human_assessor(name):
    return {"type": "human", "name": name}


def vote(tag, answer, assessor, run, date, reason=None, entry=None, variant_of=None, proposed_name=None):
    if answer not in ANSWERS:
        raise ValueError(f"answer must be one of {list(ANSWERS)}")
    rec = {"tag": tag, "key": L.norm(tag), "question": "skill", "answer": answer, "assessor": assessor, "run": run, "date": date}
    for k, v in (("reason", (reason or "")[:200] or None), ("entry", entry), ("variant_of", variant_of), ("proposed_name", proposed_name)):
        if v:
            rec[k] = v
    return rec


def append(root, records):
    """Add votes. A second vote by the same assessor in the same run on the same tag is refused."""
    have = {identity(r) for r in load(root)}
    for r in records:
        if identity(r) in have:
            raise ValueError(f"{r['tag']!r}: {who(r['assessor'])} has already voted in run {r.get('run')!r}")
        have.add(identity(r))
    p = Path(root) / FILE
    p.parent.mkdir(exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def legacy_votes(root=L.ROOT):
    """One 'yes' per tag that appears in a legacy list: key -> vote. Worked out from the lists each time."""
    out = {}
    for g in T.read_tags(root, [T.TAGS] + list(T.LISTS.values())):
        out[L.norm(g["term"])] = {"tag": g["term"], "key": L.norm(g["term"]), "question": "skill", "answer": "yes", "assessor": LEGACY,
                                  "classes": T.classes(g), "in_lists": T.in_lists(g)}
    return out


def tally(root=L.ROOT):
    """key -> {tag, votes: [...]} with the legacy listing first."""
    out = {}
    for k, v in legacy_votes(root).items():
        out[k] = {"tag": v["tag"], "votes": [v]}
    for r in load(root):
        out.setdefault(r["key"], {"tag": r["tag"], "votes": []})["votes"].append(r)
    return out


def summary(votes):
    c = {a: [] for a in ANSWERS}
    for v in votes:
        c[v["answer"]].append(who(v["assessor"]))
    return c


def split(votes):
    """True when real assessors (not the list) gave different answers, or the list and an assessor differ."""
    return len({v["answer"] for v in votes}) > 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="record a vote")
    a.add_argument("tag")
    a.add_argument("answer", choices=ANSWERS)
    a.add_argument("--human")
    a.add_argument("--model")
    a.add_argument("--effort")
    a.add_argument("--run")
    a.add_argument("--reason")
    a.add_argument("--date", default=datetime.date.today().isoformat())
    a.add_argument("--root", default=str(L.ROOT))
    t = sub.add_parser("tally", help="show the votes")
    t.add_argument("--splits", action="store_true", help="only tags where the votes differ")
    t.add_argument("--tag")
    t.add_argument("--root", default=str(L.ROOT))
    args = ap.parse_args(argv)
    if args.cmd == "add":
        if bool(args.human) == bool(args.model):
            ap.error("give exactly one of --human or --model")
        if args.model:
            if not (args.effort and args.run):
                ap.error("a model vote needs --effort and --run")
            L.register_run(args.root, args.run, args.model, args.effort, date=args.date)
            who_ = model_assessor(args.model, args.effort)
        else:
            who_ = human_assessor(args.human)
        run = args.run or f"human-{args.date}"
        append(args.root, [vote(args.tag, args.answer, who_, run, args.date, args.reason)])
        print(f"recorded: {args.tag!r} {args.answer} by {who(who_)}")
        return 0
    tl = tally(args.root)
    assessed = {k: v for k, v in tl.items() if len(v["votes"]) > 1 or any(x["assessor"]["type"] != "legacy-list" for x in v["votes"])}
    if args.tag:
        v = tl.get(L.norm(args.tag))
        if not v:
            print("no such tag")
            return 1
        for x in v["votes"]:
            print(f"  {x['answer']:7} {who(x['assessor'])}" + (f" · {x['reason']}" if x.get("reason") else ""))
        return 0
    sp = {k: v for k, v in assessed.items() if split(v["votes"])}
    print(f"{len(tl)} tags; {len(assessed)} with at least one vote besides the legacy list; {len(sp)} with differing votes")
    for k, v in sorted(sp.items() if args.splits else [], key=lambda kv: kv[1]["tag"].casefold()):
        s = summary(v["votes"])
        print(f"- {v['tag']}: " + "; ".join(f"{a} [{', '.join(s[a])}]" for a in ANSWERS if s[a]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
