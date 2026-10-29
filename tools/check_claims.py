"""Have another model check the claims on entries that already exist, and record what it says as evidence.

    python3 -I tools/check_claims.py packets OUTDIR --size 40 [--class certification] [--unchecked-by RUN]
    python3 -I tools/check_claims.py apply OUTDIR --model-id claude-opus-5-5 --effort xhigh --run 2026-10-30-review-1
    python3 -I tools/check_claims.py build-reviews         # reviews/: packets by class and for tags, for outside models (see reviews/README.md)
    python3 -I tools/check_claims.py check-answers FILE... # check answer files are well formed before sending them
    python3 -I tools/check_claims.py apply-reviews         # record the answer files outside models left in reviews/answers/

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
leveled scheme); `certification_scope` is single-issuer (one body issues it, such as AWS Certified Solutions Architect) or many-issuers
(many bodies issue it, such as a bachelor's degree); `language_type` is human (spoken, signed, extinct) or programming (any formal
language a computer reads).
`job_listing_vote`: is the concept something job listings ask for (a skill, ability, certification or language)?"""


def view(e, by_id):
    v = {"key": e["key"], "name": e["preferred_name"], "class": L.top_class(e), "kind": e["kind"], "definition": e["definition"]}
    for k in ("certification", "certification_scope", "language_type"):
        if k in e:
            v[k] = e[k]
    v["variants"] = [x["label"] for x in e.get("variants", [])]
    v["relations"] = [f"{r['type']}:{by_id[r['target']]['key']}" for r in e.get("relations", []) if r["target"] in by_id]
    return v


def packets(root, out, size, classes=None, unchecked_by=None, kinds=None, scaffold=True):
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
    if scaffold:
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


def apply(root, out, model, effort, run, today, only=None, answers=None, entries=None):
    root = Path(root)
    entries = entries if entries is not None else L.load(root / "entries")[0]
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

    sources = [(p.name, json.loads(p.read_text("utf-8"))) for p in sorted((Path(out) / "answers").glob("*.json")) if not only or p.stem in only] \
        if answers is None else [("answers", answers)]
    for pname, lst in sources:
        p = Path(pname)
        for a in lst:
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


TAG_BRIEF = """Each packet is a list of tags from job-listing tag lists. For each, vote on one question: is this something job listings ask for,
as an ability, a certification, a language (spoken or programming) or a skill (a tool, method, standard, area of knowledge)?
- `yes`: a real, specific thing an employer could ask a candidate for. `no`: not that (a person or company name, a physical object, a
  sentence fragment, a section heading, a typo, a generic word). `unsure`: you do not know what the tag is, or it could go either way.
- Give a `reason` (at most 150 characters) for every `no` and every `unsure`. A reason is optional for `yes`.
- Vote on the tag as written. Do not look up other models' answers; they are not in the packet on purpose.
Answer shape, one object per tag, in a JSON list:
{"tag": "<the tag exactly as shown>", "job_listing_vote": {"answer": "yes|no|unsure", "reason": "<=150 chars"}}"""


def build_reviews(root, size=40, tag_size=100):
    """Everything an outside reviewer needs under reviews/: packets by class, tag packets, the brief and the answers folder."""
    r = Path(root) / "reviews"
    for cls in ("certification", "language", "ability", "skill"):
        packets(root, r / cls, size, [cls], scaffold=False)
    tag_packets(root, r / "tags", tag_size)
    (r / "BRIEF.md").write_text("# What to judge\n\n## Entry packets (certification, language, ability, skill)\n\n" + REVIEW_BRIEF
                                + "\n\n## Tag packets (tags)\n\n" + TAG_BRIEF + "\n", "utf-8")
    for d in ("answers", "applied"):
        (r / d).mkdir(exist_ok=True)
        (r / d / ".gitkeep").write_text("", "utf-8")


def tag_packets(root, out, size):
    """Packets of every tag that has no entry: the ones a model answered no or unsure to, and the ones nobody has looked at yet.
    Only the tag and where the legacy lists put it are shown, never an earlier answer, so each opinion is independent."""
    root = Path(root)
    entries, _ = L.load(root / "entries")
    forms = {L.norm(fm["label"]) for e in entries for fm in L.forms(e)}
    groups = T.read_tags(root, [T.TAGS] + list(T.LISTS.values()))
    items = [{"tag": g["term"], "legacy_class": "/".join(T.classes(g)), "in_lists": T.in_lists(g)}
             for g in sorted(groups, key=lambda g: g["term"].casefold()) if L.norm(g["term"]) not in forms]
    d = Path(out) / "packets"
    d.mkdir(parents=True, exist_ok=True)
    for n, i in enumerate(range(0, len(items), size), 1):
        (d / f"p{n:03d}.json").write_text(json.dumps({"type": "tags", "tags": items[i:i + size]}, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"{len(items)} tags in {(len(items) + size - 1) // size} packets under {d}")


def shape_problems(answers, tags):
    """What is wrong with the structure of an outside reviewer's answers, so a malformed file is refused whole rather than half applied."""
    out = []
    isd, isl, iss = (lambda x: isinstance(x, dict)), (lambda x: isinstance(x, list)), (lambda x: isinstance(x, str))
    for i, a in enumerate(answers):
        if not isd(a):
            out.append(f"answer {i} is not an object")
            continue
        jv = a.get("job_listing_vote")
        if jv is not None and not (isd(jv) and jv.get("answer") in AS.ANSWERS):
            out.append(f"answer {i}: job_listing_vote needs answer yes, no or unsure")
        if tags:
            if not iss(a.get("tag")) or not jv:
                out.append(f"answer {i}: a tag answer needs `tag` and `job_listing_vote`")
            continue
        if not iss(a.get("key")):
            out.append(f"answer {i}: needs `key`")
        for c, j in (a.get("claims") or {}).items() if isd(a.get("claims") or {}) else [("claims", None)]:
            if not (isd(j) and j.get("verdict") in VERDICTS and c in CLAIMS):
                out.append(f"answer {i}: claim {c!r} needs a verdict of supports, contradicts or unsure")
            elif j["verdict"] == "contradicts" and not iss(j.get("note")):
                out.append(f"answer {i}: claim {c!r} says contradicts and needs a note")
        for field, ok_is, bad_key in (("variants", iss, "label"), ("relations", iss, "rel")):
            v = a.get(field) or {}
            if not isd(v) or not isl(v.get("ok", [])) or not isl(v.get("bad", [])) or not all(ok_is(x) for x in v.get("ok", [])) \
                    or not all(isd(b) and iss(b.get(bad_key)) for b in v.get("bad", [])):
                out.append(f"answer {i}: {field} must be {{\"ok\": [text], \"bad\": [{{\"{bad_key}\": text, \"note\": text}}]}}")
    return out


def read_answer_file(p, today):
    """((doc, model, effort, date, is_tag_file), []) for a good answer file, or (None, [what is wrong])."""
    import re
    try:
        doc = json.loads(Path(p).read_text("utf-8"))
        r = doc["reviewer"]
        model, effort = str(r["model"]).strip(), str(r.get("effort", "unknown")).strip()
        date = str(r.get("date") or today)
        assert re.fullmatch(r"[A-Za-z0-9._:+/ -]{1,60}", model) and effort in L.EFFORTS and isinstance(doc["answers"], list)
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", date)
    except Exception as e:  # noqa: BLE001
        return None, [f"not a valid answer file ({type(e).__name__}); it needs `reviewer` {{model, effort}} with effort one of {sorted(L.EFFORTS)}, a date as YYYY-MM-DD if any, and `answers`"]
    tags = str(doc.get("packet", "")).startswith("tags")
    sp = shape_problems(doc["answers"], tags)
    return (None, sp) if sp else ((doc, model, effort, date, tags), [])


def apply_reviews(root, today):
    """Apply every file in reviews/answers/: {"reviewer": {"model", "effort", "date"?}, "packet": "...", "answers": [...]}.
    The reviewer's model and effort are self-reported, so the run is registered as `external` and says so. A file that is
    malformed is refused whole and left where it is."""
    import re
    root = Path(root)
    ad = root / "reviews" / "answers"
    done = root / "reviews" / "applied"
    log, bad, votes, moved = [], [], [], []
    entries, _ = L.load(root / "entries")
    touched, runs = set(), {}
    for p in sorted(ad.glob("*.json")) if ad.is_dir() else []:
        head, sp = read_answer_file(p, today)
        if sp:
            bad += [f"{p.name}: {m}" for m in sp[:5]]
            continue
        doc, model, effort, date, tags = head
        run = f"external-{date}-{re.sub(r'[^a-z0-9]+', '-', model.lower()).strip('-')}-{effort}"
        known = runs.get(run) or L.load_runs(root).get(run)
        if known and (known["model"], known["effort"]) != (model, effort):
            bad.append(f"{p.name}: run {run!r} already belongs to {known['model']} at {known['effort']}; spell the model name the same way every time")
            continue
        runs[run] = {"model": model, "effort": effort, "date": date}
        if tags:
            for a in doc["answers"]:
                jv = a["job_listing_vote"]
                votes.append(AS.vote(a["tag"], jv["answer"], AS.model_assessor(model, effort), run, date, reason=jv.get("reason") if jv["answer"] != "yes" else None))
            log.append(f"{p.name}: {len(doc['answers'])} tag votes")
        else:
            _, t, v, lg, pr = apply(root, None, model, effort, run, date, answers=doc["answers"], entries=entries)
            touched |= t
            votes += v
            bad += [f"{p.name}: {m}" for m in pr]
            log.append(f"{p.name}: {lg['supports']} support, {lg['contradicts']} contradict, {lg['unsure']} unsure, {len(v)} votes")
        moved.append(p)
    errs = L.validate(entries) + L.check_runs(entries, {**L.load_runs(root), **runs})
    if errs:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(errs[:4]))
    for run, r in runs.items():
        L.register_run(root, run, r["model"], r["effort"], "external", date=r["date"], note="an outside model; model and effort are self-reported by the reviewer and not verified")
    for e in entries:
        if e["_file"] in touched:
            (root / "entries" / e["_file"]).write_text(json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n", "utf-8")
    have = {AS.identity(r) for r in AS.load(root)}
    fresh = []
    for v in votes:
        if AS.identity(v) not in have:
            have.add(AS.identity(v))
            fresh.append(v)
    AS.append(root, fresh)
    if moved:
        done.mkdir(parents=True, exist_ok=True)
        for p in moved:
            p.rename(done / p.name)
    print("\n".join(log + bad) + f"\n{len(fresh)} votes recorded")
    return log, bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packets")
    p.add_argument("out")
    p.add_argument("--size", type=int, default=40)
    p.add_argument("--class", dest="classes", action="append", choices=["ability", "certification", "language", "skill"])
    p.add_argument("--unchecked-by", help="skip entries that have evidence from any run whose label contains this text, such as 'review'")
    p.add_argument("--root", default=str(L.ROOT))
    t_ = sub.add_parser("tag-packets")
    t_.add_argument("out")
    t_.add_argument("--size", type=int, default=40)
    t_.add_argument("--root", default=str(L.ROOT))
    b_ = sub.add_parser("build-reviews", help="write reviews/: the packets, the brief and the answers folder, for outside reviewers")
    b_.add_argument("--size", type=int, default=40)
    b_.add_argument("--tag-size", type=int, default=100)
    b_.add_argument("--root", default=str(L.ROOT))
    c_ = sub.add_parser("check-answers", help="check that answer files are well formed before sending them; changes nothing")
    c_.add_argument("files", nargs="+")
    r_ = sub.add_parser("apply-reviews", help="apply the answer files in reviews/answers/ from outside reviewers")
    r_.add_argument("--date", default=datetime.date.today().isoformat())
    r_.add_argument("--root", default=str(L.ROOT))
    q = sub.add_parser("apply")
    q.add_argument("out")
    q.add_argument("--model-id", required=True)
    q.add_argument("--effort", required=True, choices=sorted(L.EFFORTS))
    q.add_argument("--run", required=True)
    q.add_argument("--agent", default="subagent")
    q.add_argument("--date", default=datetime.date.today().isoformat())
    q.add_argument("--root", default=str(L.ROOT))
    q.add_argument("--dry-run", action="store_true")
    q.add_argument("--only", help="comma-separated packet names to apply, such as p001,p002")
    a = ap.parse_args(argv)
    if a.cmd == "check-answers":
        worst = 0
        for f in a.files:
            head, sp = read_answer_file(f, datetime.date.today().isoformat())
            print(f"{f}: " + (f"ok, {len(head[0]['answers'])} answers from {head[1]} at {head[2]} effort" if head else "; ".join(sp[:5])))
            worst |= bool(sp)
        return worst
    if a.cmd == "build-reviews":
        build_reviews(a.root, a.size, a.tag_size)
        return 0
    if a.cmd == "tag-packets":
        tag_packets(a.root, a.out, a.size)
        return 0
    if a.cmd == "apply-reviews":
        apply_reviews(a.root, a.date)
        return 0
    if a.cmd == "packets":
        packets(a.root, a.out, a.size, a.classes, a.unchecked_by)
        return 0
    entries, touched, votes, log, problems = apply(a.root, a.out, a.model_id, a.effort, a.run, a.date, set(a.only.split(",")) if a.only else None)
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
