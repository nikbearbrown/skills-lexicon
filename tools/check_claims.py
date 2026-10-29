"""Have another model check the claims on entries that already exist, and record what it says as evidence.

    python3 -I tools/check_claims.py packets OUTDIR --size 40 [--class certification] [--unchecked-by RUN]
    python3 -I tools/check_claims.py apply OUTDIR --model-id claude-opus-5-5 --effort xhigh --run 2026-10-30-review-1

packets writes OUTDIR/packets/pNNN.json: slim views of the entries to check. The reviewer writes OUTDIR/answers/pNNN.json,
one answer per entry (see REVIEW_BRIEF). apply records them. For each claim a reviewer judged:
  supports / contradicts  -> a `checked` evidence record by the reviewing model, with the run (which carries its effort);
  unsure                  -> nothing is recorded (there is no evidence either way).
The reviewer also votes on the entry's tag (is it something job listings ask for?), which goes to the vote ledger.
A model's check is recorded and shown but never backs a claim, and an unresolved `contradicts` blocks `reviewed`.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assess as AS  # noqa: E402
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402

CLAIMS = ("definition", "kind", "certification", "certification_scope", "language_type")
VERDICTS = ("supports", "contradicts", "unsure")

REVIEW_BRIEF = """Each packet is a list of dictionary entries about things job listings ask for. Judge every claim from your own
knowledge, independently. You are a reviewer: say `contradicts` when a claim is wrong or misleading, `supports` when it is right,
`unsure` when you cannot tell. Do not be agreeable; a wrong definition marked `supports` is worse than an honest `unsure`.
Drafts written from memory are often wrong about issuers, scope and kind, so check those closely.
- A note is allowed on any verdict, including `supports`: use it for a caveat (for example "retired in 2017").
- A definition that is true but uninformative: `supports` with a note, or `unsure`. Use `contradicts` only when it is wrong or misleading.
- A short form (abbreviation) is an ok variant only if it means this concept and not something else; otherwise mark it bad.
- A course-completion card, a licence endorsement and a level of a leveled scheme all count as certifications if an official body attests them.
Answer shape, one object per entry, in a JSON list:
{"key": "<entry key>",
 "claims": {"definition": {"verdict": "supports|contradicts|unsure", "note": "<=150 chars, required when contradicts"},
            "kind": {...}, "certification": {...}, "certification_scope": {...}, "language_type": {...}},   // only the claims the entry has
 "variants": {"ok": ["<label>"], "bad": [{"label": "<label>", "note": "..."}]},        // judge each variant; leave out any you cannot judge
 "relations": {"ok": ["<type>:<target key>"], "bad": [{"rel": "<type>:<target key>", "note": "..."}]},
 "job_listing_vote": {"answer": "yes|no|unsure", "reason": "<=150 chars, required unless yes"}}
`kind` must be one of the allowed kinds; `certification` is true for a credential attested by an official body (and each level of a
leveled scheme); `language_type` is human (spoken, signed, extinct) or programming (any formal language a computer reads).
`job_listing_vote`: is the concept something job listings ask for (a skill, ability, certification or language)?"""


def view(e, by_id):
    v = {"key": e["key"], "name": e["preferred_name"], "class": L.top_class(e), "kind": e["kind"], "definition": e["definition"]}
    for k in ("certification", "certification_scope", "language_type"):
        if k in e:
            v[k] = e[k]
    v["variants"] = [x["label"] for x in e.get("variants", [])]
    v["relations"] = [f"{r['type']}:{by_id[r['target']]['key']}" for r in e.get("relations", []) if r["target"] in by_id]
    return v


def packets(root, out, size, classes=None, unchecked_by=None, kinds=None):
    entries, _ = L.load(Path(root) / "entries")
    by_id = {e["id"]: e for e in entries}
    pick = []
    for e in sorted(entries, key=lambda e: e["key"]):
        if e["status"] == "deprecated" or e["provenance"]["source"].startswith("imported from O*NET"):
            continue                                 # O*NET abilities already match their source
        if classes and L.top_class(e) not in classes:
            continue
        if kinds and e["kind"] not in kinds:
            continue
        if unchecked_by and any(unchecked_by in str(ev.get("run", "")) for ev in e.get("evidence", [])):
            continue
        pick.append(view(e, by_id))
    d = Path(out) / "packets"
    d.mkdir(parents=True, exist_ok=True)
    (Path(out) / "answers").mkdir(exist_ok=True)
    (Path(out) / "BRIEF.txt").write_text(REVIEW_BRIEF + "\n", "utf-8")
    n = 0
    for i in range(0, len(pick), size):
        n += 1
        (d / f"p{n:03d}.json").write_text(json.dumps({"allowed_kinds": sorted(L.KINDS), "entries": pick[i:i + size]}, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"{len(pick)} entries in {n} packets under {d}")
    return n


def tag_of(e, rows):
    for s in e["provenance"].get("legacy_tag", {}).get("sources", []):
        t = rows.get((s["file"], s["rows"][0]))
        if t:
            return t
    return None


def apply(root, out, model, effort, run, today):
    root = Path(root)
    entries, _ = L.load(root / "entries")
    by_key = {e["key"]: e for e in entries}
    by_id = {e["id"]: e for e in entries}
    key_to_id = {e["key"]: e["id"] for e in entries}
    rows = {}
    for g in T.read_tags(root, [T.TAGS] + list(T.LISTS.values())):
        for s in g["sources"].values():
            rows[(s["file"], s["rows"][0])] = g["term"]
    by = f"model:{model}"
    log = {"supports": 0, "contradicts": 0, "unsure": 0, "skipped": 0, "votes": 0}
    problems, votes, touched = [], [], set()

    def rec(e, field, outcome, note=""):
        if field not in L.claim_keys(e) or any(v.get("field") == field and v.get("run") == run for v in e.get("evidence", [])):
            log["skipped"] += 1
            return
        r = {"field": field, "by": by, "action": "checked", "outcome": outcome, "date": today, "run": run}
        if note:
            r["note"] = note[:200]
        e.setdefault("evidence", []).append(r)
        touched.add(e["_file"])
        log[outcome] += 1

    for p in sorted((Path(out) / "answers").glob("*.json")):
        for a in json.loads(p.read_text("utf-8")):
            e = by_key.get(a.get("key"))
            if not e:
                problems.append(f"{p.name}: no entry {a.get('key')!r}")
                continue
            for c, j in (a.get("claims") or {}).items():
                if c not in CLAIMS or j.get("verdict") not in VERDICTS:
                    problems.append(f"{a['key']}: bad claim {c!r}")
                elif j["verdict"] == "unsure":
                    log["unsure"] += 1
                else:
                    rec(e, c, j["verdict"], j.get("note", ""))
            v = a.get("variants") or {}
            for lab in v.get("ok", []):
                rec(e, f"variant:{L.norm(lab)}", "supports")
            for b in v.get("bad", []):
                rec(e, f"variant:{L.norm(b.get('label', ''))}", "contradicts", b.get("note", ""))
            rl = a.get("relations") or {}
            for r_ in rl.get("ok", []) + [b.get("rel", "") for b in rl.get("bad", [])]:
                t, _, k = r_.partition(":")
                if k not in key_to_id:
                    problems.append(f"{a['key']}: relation target {k!r} unknown")
            for r_ in rl.get("ok", []):
                t, _, k = r_.partition(":")
                if k in key_to_id:
                    rec(e, f"relation:{t}:{key_to_id[k]}", "supports")
            for b in rl.get("bad", []):
                t, _, k = b.get("rel", "").partition(":")
                if k in key_to_id:
                    rec(e, f"relation:{t}:{key_to_id[k]}", "contradicts", b.get("note", ""))
            jv = a.get("job_listing_vote")
            tag = tag_of(e, rows)
            if jv and jv.get("answer") in AS.ANSWERS and tag:
                votes.append(AS.vote(tag, jv["answer"], AS.model_assessor(model, effort), run, today,
                                     reason=jv.get("reason") if jv["answer"] != "yes" else None, entry=e["id"]))
    return entries, touched, votes, log, problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packets")
    p.add_argument("out")
    p.add_argument("--size", type=int, default=40)
    p.add_argument("--class", dest="classes", action="append", choices=["ability", "certification", "language", "skill"])
    p.add_argument("--unchecked-by", help="skip entries that have evidence from any run whose label contains this text, such as 'review'")
    p.add_argument("--root", default=str(L.ROOT))
    q = sub.add_parser("apply")
    q.add_argument("out")
    q.add_argument("--model-id", required=True)
    q.add_argument("--effort", required=True, choices=sorted(L.EFFORTS))
    q.add_argument("--run", required=True)
    q.add_argument("--agent", default="subagent")
    q.add_argument("--date", default=datetime.date.today().isoformat())
    q.add_argument("--root", default=str(L.ROOT))
    q.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "packets":
        packets(a.root, a.out, a.size, a.classes, a.unchecked_by)
        return 0
    entries, touched, votes, log, problems = apply(a.root, a.out, a.model_id, a.effort, a.run, a.date)
    errs = L.validate(entries)
    if errs:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(errs[:4]))
    if not a.dry_run:
        L.register_run(a.root, a.run, a.model_id, a.effort, a.agent, date=a.date)
        for e in entries:
            if e["_file"] in touched:
                (Path(a.root) / "entries" / e["_file"]).write_text(
                    json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n", "utf-8")
        fresh = []
        have = {AS.identity(r) for r in AS.load(a.root)}
        for v in votes:
            if AS.identity(v) not in have:
                fresh.append(v)
        AS.append(a.root, fresh)
        log["votes"] = len(fresh)
    print(("DRY RUN: nothing written. " if a.dry_run else "") + f"{log['supports']} support, {log['contradicts']} contradict, "
          f"{log['unsure']} unsure (not recorded), {log['skipped']} skipped, {log['votes']} votes, on {len(touched)} entries")
    for m in problems[:15]:
        print("  problem:", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
