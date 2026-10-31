#!/usr/bin/env python3
"""Descriptions adapted from Wikipedia leads, with the source, revision and licence recorded on the entry.

    python3 -I scripts/wikipedia_match/descriptions.py packets OUTDIR [--size 60] [--data data/wikipedia-match/20261001]
    python3 -I scripts/wikipedia_match/descriptions.py check-packets OUTDIR [--size 60]
    python3 -I scripts/wikipedia_match/descriptions.py prune     # remove descriptions the check judged wrong-subject
    python3 -I scripts/wikipedia_match/descriptions.py apply OUTDIR --stage rewrite --model-id claude-sonnet-5-5 --effort xhigh --run RUN
    python3 -I scripts/wikipedia_match/descriptions.py apply OUTDIR --stage check   --model-id claude-opus-5-5   --effort xhigh --run RUN

packets: for every entry the resolver judged `same`, one slim item (the entry, the page title and the start of its lead). A model
writes OUTDIR/answers/pNNN.json (see REWRITE_BRIEF), another checks it (see CHECK_BRIEF). apply records the answers.
  rewrite, verdict ok     -> `description` on the entry, a `drafted` record by the rewriting model, and a `matched_source` record
                             naming the Wikipedia revision (a dump match, so it backs the claim; the match was made by a rule, not a person)
  rewrite, other verdicts -> nothing on the entry; a line in description-skipped.jsonl
  check                   -> a `checked` record by the second model: supports if faithful, contradicts otherwise (never backs)
Nothing is overwritten: an entry that already has a description is skipped."""
import argparse
import datetime
import json
import os
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import lexicon as L  # noqa: E402

LEAD_CHARS = 1500
ORG = {"name": "Wikipedia, Wikimedia Foundation", "url": "https://en.wikipedia.org/", "type": "reference-work", "country": "INT"}
LICENCE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
VERDICTS = ("ok", "wrong-subject", "unsure")
CHECKS = ("faithful", "adds-information", "changes-meaning", "wrong-subject")

REWRITE_BRIEF = """Each item is a lexicon entry (a skill, tool, standard, language, credential and so on that job listings ask for) and the start of the
Wikipedia article that was matched to it. Write a description of the thing the entry names, using ONLY facts stated in the lead text.
- 1 to 3 sentences, at most 350 characters, in plain language for a reader who has not met the term. Say what it is, and who makes or uses it
  when the lead says so. Keep a retired or renamed status if the lead says so ("was", "now called").
- Leave out pronunciation, etymology, trademark and ownership detail, release dates and version numbers, long lists, and anything promotional.
- Add no fact that is not in the lead. Do not use your own knowledge, even where you are sure.
- If the lead is about something other than the entry's concept (another sense of the word, a company instead of its product, a much
  broader topic that only mentions it), answer `wrong-subject` and write no description. If the lead is too thin or unclear, answer `unsure`.
Answer shape, a JSON list, one object per item, key copied exactly:
{"key": "<entry key>", "verdict": "ok|wrong-subject|unsure", "description": "<text, only when ok>", "note": "<=150 characters, required unless ok>"}"""

CHECK_BRIEF = """Each item has a Wikipedia lead and a description someone adapted from it for a skills lexicon. Judge the description against the lead only.
- `faithful`: every fact in the description is in the lead, and the meaning is the same (shorter or reworded is fine).
- `adds-information`: the description states something that is not in the lead.
- `changes-meaning`: it states something the lead does not say in that sense, or leaves out a qualifier that reverses it (for example presents a
  retired product as current).
- `wrong-subject`: the lead is not about the thing the entry names (check the entry name and kind), so the description describes the wrong thing.
Do not use your own knowledge to correct the lead. Answer shape, a JSON list, one object per item:
{"key": "<entry key>", "verdict": "faithful|adds-information|changes-meaning|wrong-subject", "note": "<=150 characters, required unless faithful"}"""


def permalink(title, rev_id):
    return "https://en.wikipedia.org/w/index.php?title=%s&oldid=%d" % (urllib.parse.quote(title.replace(" ", "_"), safe="()_,'-.:!"), rev_id)


def load_data(data):
    cands, cats, res = {}, {}, []
    for l in open(os.path.join(data, "candidates.jsonl"), encoding="utf-8"):
        d = json.loads(l); cands[d["page_id"]] = d
    for l in open(os.path.join(data, "categories.jsonl"), encoding="utf-8"):
        d = json.loads(l); cats[d["page_id"]] = d.get("categories", [])
    for l in open(os.path.join(data, "resolved.jsonl"), encoding="utf-8"):
        d = json.loads(l)
        if d["relation"] == "same":
            res.append(d)
    return cands, cats, res


def packets(root, out, size, data):
    cands, cats, res = load_data(data)
    entries, _ = L.load(os.path.join(root, "entries"))
    E = {e["id"]: e for e in entries}
    items = []
    for r in sorted(res, key=lambda r: r["entry_key"]):
        e = E[r["entry_id"]]
        if "description" in e:
            continue
        pg = cands[r["page"]["page_id"]]
        items.append({"key": e["key"], "entry": e["preferred_name"], "kind": e["kind"], "our_definition": e["definition"],
                      "page_title": pg["title"], "lead": pg["lead"][:LEAD_CHARS]})
    os.makedirs(os.path.join(out, "packets"), exist_ok=True)
    os.makedirs(os.path.join(out, "answers"), exist_ok=True)
    for n, i in enumerate(range(0, len(items), size), 1):
        with open(os.path.join(out, "packets", "p%03d.json" % n), "w", encoding="utf-8") as f:
            json.dump({"items": items[i:i + size]}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out, "REWRITE-BRIEF.txt"), "w") as f:
        f.write(REWRITE_BRIEF + "\n")
    with open(os.path.join(out, "CHECK-BRIEF.txt"), "w") as f:
        f.write(CHECK_BRIEF + "\n")
    print("%d items in %d packets under %s" % (len(items), (len(items) + size - 1) // size, out))


def check_packets(root, out, size, data):
    """Packets for the second-model check: every entry with a description, the lead it came from and the description."""
    cands, cats, res = load_data(data)
    entries, _ = L.load(os.path.join(root, "entries"))
    page_of = {r["entry_key"]: r["page"] for r in res}
    items = []
    for e in sorted(entries, key=lambda e: e["key"]):
        if "description" not in e or e["key"] not in page_of:
            continue
        src = e["description"]["source"]
        if any(v.get("field") == "description" and v.get("action") == "checked" for v in e.get("evidence", [])):
            continue
        items.append({"key": e["key"], "entry": e["preferred_name"], "kind": e["kind"], "page_title": src["title"],
                      "lead": cands[src["page_id"]]["lead"][:LEAD_CHARS], "description": e["description"]["text"]})
    os.makedirs(os.path.join(out, "check-packets"), exist_ok=True)
    os.makedirs(os.path.join(out, "answers"), exist_ok=True)
    for n, i in enumerate(range(0, len(items), size), 1):
        with open(os.path.join(out, "check-packets", "c%03d.json" % n), "w", encoding="utf-8") as f:
            json.dump({"items": items[i:i + size]}, f, ensure_ascii=False, indent=1)
    print("%d items in %d check packets under %s" % (len(items), (len(items) + size - 1) // size, out))


def prune(root, data, today):
    """Take off a description that the check judged wrong-subject: its text describes another thing than the entry. The description and its
    evidence records are written to description-skipped.jsonl so nothing is lost; wording problems (changes-meaning, adds-information) stay, flagged."""
    entries, _ = L.load(os.path.join(root, "entries"))
    rows, touched = [], set()
    for e in entries:
        if "description" not in e:
            continue
        bad = [v for v in e.get("evidence", []) if v.get("field") == "description" and v.get("action") == "checked" and v.get("outcome") == "contradicts"
               and str(v.get("note", "")).startswith("wrong-subject")]
        if not bad:
            continue
        rows.append({"entry_key": e["key"], "verdict": "wrong-subject", "removed": today, "note": bad[0]["note"][:200], "description": e["description"],
                     "evidence": [v for v in e["evidence"] if v.get("field") == "description"]})
        e["evidence"] = [v for v in e["evidence"] if v.get("field") != "description"]
        del e["description"]
        touched.add(e["_file"])
    errs = L.validate(entries)
    if errs:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(errs[:4]))
    for e in entries:
        if e["_file"] in touched:
            with open(os.path.join(root, "entries", e["_file"]), "w", encoding="utf-8") as f:
                f.write(json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n")
    with open(os.path.join(data, "description-skipped.jsonl"), "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("removed %d wrong-subject descriptions (kept in description-skipped.jsonl)" % len(rows))
    return len(rows)


def put_after(e, key, value, after="definition"):
    new = {}
    for k, v in e.items():
        new[k] = v
        if k == after:
            new[key] = value
    if key not in new:
        new[key] = value
    return new


def apply(root, out, stage, model, effort, run, today, data, only=None, agent="subagent"):
    entries, _ = L.load(os.path.join(root, "entries"))
    by_key = {e["key"]: i for i, e in enumerate(entries)}
    cands, cats, res = load_data(data)
    page_of = {r["entry_key"]: r["page"] for r in res}
    dump = os.path.basename(os.path.normpath(data))
    by = "model:" + model
    log = {"ok": 0, "skipped": 0, "supports": 0, "contradicts": 0, "problems": 0}
    skipped_rows, touched = [], set()
    for name in sorted(os.listdir(os.path.join(out, "answers"))):
        if not name.endswith(".json") or (only and name[:-5] not in only):
            continue
        for a in json.load(open(os.path.join(out, "answers", name), encoding="utf-8")):
            i = by_key.get(a.get("key"))
            pg = page_of.get(a.get("key"))
            if i is None or pg is None:
                log["problems"] += 1; print("problem: %s: no such entry or no same-page" % a.get("key")); continue
            e = entries[i]
            if stage == "rewrite":
                if "description" in e:
                    log["skipped"] += 1; continue
                if a.get("verdict") != "ok":
                    if a.get("verdict") in VERDICTS:
                        skipped_rows.append({"entry_key": e["key"], "verdict": a["verdict"], "note": str(a.get("note", ""))[:150], "page": pg["title"], "run": run})
                    else:
                        log["problems"] += 1
                    continue
                text = str(a.get("description", "")).strip()
                if not text or len(text) > 700:
                    log["problems"] += 1; print("problem: %s: description empty or over 700 characters" % e["key"]); continue
                c = cands[pg["page_id"]]
                url = permalink(c["title"], c["rev_id"])
                desc = {"text": text, "adapted": True,
                        "source": {"name": "English Wikipedia", "title": c["title"], "page_id": c["page_id"], "rev_id": c["rev_id"],
                                   "rev_timestamp": c["rev_timestamp"], "url": url, "dump": dump, "licence": L.DESCRIPTION_LICENCE, "licence_url": LICENCE_URL}}
                e = put_after(e, "description", desc)
                method = "title" if pg["basis"] in ("exact-title", "title-minus-qualifier") else "redirect"
                e.setdefault("evidence", []).extend([
                    {"field": "description", "by": by, "action": "drafted", "date": today, "run": run,
                     "note": ("adapted from the lead of Wikipedia: %s, revision %d" % (c["title"], c["rev_id"]))[:200]},
                    {"field": "description", "by": "source:wikipedia-enwiki-" + dump, "action": "matched_source", "kind": "wikipedia", "verification": "dump-match",
                     "outcome": "supports", "ref": url, "date": today, "run": run, "organization": dict(ORG),
                     "note": "the page was matched to the entry by title rule and category fit, not by a person",
                     "match": {"dataset": "enwiki-" + dump, "dataset_id": str(c["page_id"]), "method": method, "categories": cats.get(c["page_id"], [])[:15]}}])
                entries[i] = e
                touched.add(e["_file"]); log["ok"] += 1
            else:
                if "description" not in e or any(v.get("field") == "description" and v.get("run") == run for v in e.get("evidence", [])):
                    log["skipped"] += 1; continue
                v = a.get("verdict")
                if v not in CHECKS:
                    log["problems"] += 1; continue
                rec = {"field": "description", "by": by, "action": "checked", "outcome": "supports" if v == "faithful" else "contradicts", "date": today, "run": run}
                if v != "faithful":
                    rec["note"] = ("%s: %s" % (v, a.get("note", "")))[:200]
                e.setdefault("evidence", []).append(rec)
                touched.add(e["_file"]); log[rec["outcome"]] += 1
    errs = L.validate(entries) + L.check_runs(entries, {**L.load_runs(root), run: {"model": model, "effort": effort}})
    if errs:
        raise SystemExit("not saved, the dictionary would not validate: " + "; ".join(errs[:4]))
    L.register_run(root, run, model, effort, agent, date=today)
    for e in entries:
        if e["_file"] in touched:
            with open(os.path.join(root, "entries", e["_file"]), "w", encoding="utf-8") as f:
                f.write(json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n")
    if skipped_rows:
        with open(os.path.join(data, "description-skipped.jsonl"), "a", encoding="utf-8") as f:
            for r in skipped_rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("%s: %d described, %d supports, %d contradicts, %d skipped, %d not used (wrong subject or unsure), %d problems" %
          (stage, log["ok"], log["supports"], log["contradicts"], log["skipped"], len(skipped_rows), log["problems"]))
    return log


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packets"); p.add_argument("out"); p.add_argument("--size", type=int, default=60)
    c = sub.add_parser("check-packets"); c.add_argument("out"); c.add_argument("--size", type=int, default=60)
    r = sub.add_parser("prune")
    q = sub.add_parser("apply"); q.add_argument("out"); q.add_argument("--stage", choices=["rewrite", "check"], required=True)
    q.add_argument("--model-id", required=True); q.add_argument("--effort", required=True, choices=sorted(L.EFFORTS)); q.add_argument("--run", required=True)
    q.add_argument("--only"); q.add_argument("--agent", default="subagent")
    for x in (p, c, r, q):
        x.add_argument("--root", default=ROOT); x.add_argument("--data", default=os.path.join(ROOT, "data", "wikipedia-match", "20261001"))
        x.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    if a.cmd == "packets":
        packets(a.root, a.out, a.size, a.data)
    elif a.cmd == "prune":
        prune(a.root, a.data, a.date)
    elif a.cmd == "check-packets":
        check_packets(a.root, a.out, a.size, a.data)
    else:
        apply(a.root, a.out, a.stage, a.model_id, a.effort, a.run, a.date, a.data, set(a.only.split(",")) if a.only else None, a.agent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
