"""Check model answers and save the good ones as machine-drafted entries. Nothing is saved unless the whole dictionary still validates.

    python3 -I tools/ingest.py work --model-id claude-sonnet-5-5 --run 2026-10-27-pilot [--dry-run]

The operator names the model (--model-id) and the run; the model's own claim about who it is is never used.
Claims a model marked basis "guess" are dropped, as are relations to ids that do not exist.
Answers that fail go to work/rejected/ with the reasons; "not a skill" and "unsure" go to data/term-decisions.json
so the same term is not asked again.
"""
import argparse
import copy
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402

DECISIONS = {"new", "variant_of", "not_a_skill", "unsure"}
BASIS = {"posting", "general-knowledge", "guess"}
NOTE_MAX = 200


def slugify(name, taken):
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "entry"
    key, n = base, 2
    while key in taken:
        key, n = f"{base}-{n}", n + 1
    return key


def evidence(field, by, run, today, basis, quote):
    note = f"basis: {basis}"
    if basis == "posting" and quote:
        note += f"; quote: {quote}"[:NOTE_MAX]
    return {"field": field, "by": by, "action": "drafted", "date": today, "run": run, "note": note}


def annotate(e, req, out, ev, dropped, by, run, today):
    """Add the `certification` and `language_type` annotations the model gave, each as its own claim.
    A legacy list or class is only a hint: when the model and the hint differ, the evidence record is flagged
    for a person. A model that says "not a language" leaves no field, so the disagreement goes in `notes`."""
    o = req.get("origin") or {}
    lists, cls = o.get("in_lists") or [], (o.get("class") or "").split("/")
    legacy = {"certification": "certification" in lists or "Certification" in cls,
              "language_type": "language" in lists or "Language" in cls}
    why = (e.get("annotation_note") or "").strip()
    used = False                       # the note is kept once: with the disagreement it explains, else with the scope
    for key in ("certification", "certification_scope", "language_type"):
        ann = e.get(key)
        if not isinstance(ann, dict) or "value" not in ann:
            continue
        v, b = ann["value"], ann.get("basis")
        if b not in BASIS or b == "guess":
            dropped.append(f"{key}: basis {b!r}")
            continue
        if (key == "certification" and not isinstance(v, bool)) or (key == "language_type" and v is not None and v not in L.LANGUAGE_TYPES) \
                or (key == "certification_scope" and v not in L.CERT_SCOPES):
            dropped.append(f"{key}: value {v!r} not allowed")
            continue
        if key == "certification_scope":
            if out.get("certification") is True:                 # only a certification has a scope
                out[key] = v
                rec = evidence(key, by, run, today, b, "")
                if why and not used:
                    rec["note"] = (rec["note"] + "; " + why)[:NOTE_MAX]
                ev.append(rec)
            else:
                dropped.append("certification_scope: the entry is not a certification")
            continue
        yes = v if key == "certification" else v is not None
        flag = text = None
        if o and legacy[key] and not yes:
            flag, text, used = "disagrees_with_legacy", "; disagrees with the legacy list/class: " + why, True
        elif o and yes and not legacy[key]:
            flag, text = "not_in_legacy", "; no legacy list/class says so"
        if key == "language_type" and v is None:
            if flag:
                out["notes"] = (out.get("notes", "") + " The model says this is not a language; the legacy list/class says it is. " + why).strip()
            continue
        out[key] = v
        rec = evidence(key, by, run, today, b, "")
        rec["note"] = (rec["note"] + (text or ""))[:NOTE_MAX]
        if flag:
            rec["flag"] = flag
        ev.append(rec)


def build_new(resp, req, entries, by, run, today):
    """Return (entry, dropped notes). Raises ValueError when the answer cannot be used at all."""
    e = resp.get("entry")
    if not isinstance(e, dict):
        raise ValueError("decision is 'new' but there is no entry")
    for k in ("preferred_name", "kind", "definition"):
        if not isinstance(e.get(k), str) or not e[k].strip():
            raise ValueError(f"entry.{k} is missing")
    quote = (req.get("quotes") or [{}])[0].get("quote", "")
    dropped, ev = [], []
    dbasis = e.get("definition_basis")
    if dbasis not in BASIS or dbasis == "guess":
        raise ValueError("definition_basis must be 'posting' or 'general-knowledge'; a guessed definition is not kept")
    taken = {x["id"] for x in entries} | {f for x in entries for f in x.get("former_ids", [])}
    out = {"id": L.new_id(taken), "preferred_name": e["preferred_name"].strip(),
           "kind": e["kind"].strip(), "definition": e["definition"].strip()}
    out["key"] = slugify(out["preferred_name"], {x.get("key") for x in entries})
    if L.default_match(out["preferred_name"]) != "word_ci":
        out["name_match"] = L.default_match(out["preferred_name"])
    ev += [evidence("definition", by, run, today, dbasis, quote), evidence("kind", by, run, today, f"{dbasis} (with the definition)", quote)]
    variants, seen = [], {L.norm(out["preferred_name"])}
    term = req["term"]
    if L.norm(term) not in seen:
        variants.append({"label": term, "match": L.default_match(term)})
        seen.add(L.norm(term))
        seen_in = "listed in the legacy tag list" if req.get("origin") else "observed in postings"
        ev.append({"field": f"variant:{L.norm(term)}", "by": by, "action": "drafted", "date": today, "run": run,
                   "note": (seen_in + "; the model chose the canonical name" + (f"; quote: {quote}" if quote else ""))[:NOTE_MAX]})
    for v in e.get("variants") or []:
        lab, b = (v.get("label") or "").strip(), v.get("basis")
        if not lab or L.norm(lab) in seen:
            continue
        if b not in BASIS or b == "guess":
            dropped.append(f"variant {lab!r}: basis {b!r}")
            continue
        variants.append({"label": lab, "match": L.default_match(lab)})
        seen.add(L.norm(lab))
        ev.append(evidence(f"variant:{L.norm(lab)}", by, run, today, b, quote))
    rels = []
    for r in e.get("relations") or []:
        t, tgt, b = r.get("type"), r.get("target"), r.get("basis")
        found = L.find(entries, tgt) if isinstance(tgt, str) else None     # ids are case-insensitive; a former id still resolves
        if t not in L.REL_TYPES or found is None:
            dropped.append(f"relation {t} -> {tgt}: unknown type or target")
        elif b not in BASIS or b == "guess":
            dropped.append(f"relation {t} -> {tgt}: basis {b!r}")
        else:
            rels.append({"type": t, "target": found["id"]})
            ev.append(evidence(f"relation:{t}:{found['id']}", by, run, today, b, quote))
    verbs = []
    for v in e.get("verbs") or []:
        w, b = (v.get("verb") or "").strip(), v.get("basis")
        if not w or L.norm(w) in {L.norm(x) for x in verbs}:
            continue
        if b not in BASIS or b == "guess":
            dropped.append(f"verb {w!r}: basis {b!r}")
            continue
        verbs.append(w)
        ev.append(evidence(f"verb:{L.norm(w)}", by, run, today, b, quote))
    annotate(e, req, out, ev, dropped, by, run, today)
    origin = req.get("origin")
    prov = {"source": (f"drafted by {by}, run {run}, from the name in the legacy tag list alone; no posting or outside source checked"
                       if origin else f"drafted by {by}, run {run}, from job postings"),
            "date": today, "reviewed_by": None}
    if origin:
        prov["legacy_tag"] = origin
    out.update({"variants": variants, "relations": rels, "verbs": verbs, "status": "machine-drafted",
                "provenance": prov, "evidence": ev})
    return out, dropped


def add_variant(resp, req, entries, by, run, today):
    tid = resp.get("variant_of")
    tgt = L.find(entries, tid) if isinstance(tid, str) else None
    if tgt is None:
        raise ValueError(f"variant_of {tid!r} does not exist")
    if tgt["status"] == "reviewed":
        raise ValueError(f"{tid} is reviewed; adding a claim would unreview it, so propose it as a pull request")
    term = req["term"]
    quote = (req.get("quotes") or [{}])[0].get("quote", "")
    tgt.setdefault("variants", []).append({"label": term, "match": L.default_match(term)})
    tgt.setdefault("evidence", []).append(
        {"field": f"variant:{L.norm(term)}", "by": by, "action": "drafted", "date": today, "run": run,
         "note": ("same concept as " + tgt["preferred_name"] + (", listed in the legacy tag list"
                  if req.get("origin") else ", seen in postings; quote: " + quote))[:NOTE_MAX]})
    return tgt


def clean(e):
    return {k: v for k, v in e.items() if not k.startswith("_")}


def ingest(work, root, by, run, today, dry=False):
    root, work = Path(root), Path(work)
    entries, errs = L.load(root / "entries")
    if errs + L.validate(entries):
        raise SystemExit("dictionary does not validate before ingest; fix it first")
    dec_path = root / "data" / "term-decisions.json"
    decisions = json.loads(dec_path.read_text("utf-8")) if dec_path.exists() else []
    report = {"new": [], "variant": [], "not_a_skill": [], "unsure": [], "rejected": [], "dropped_claims": 0}
    for rp in sorted((work / "responses").glob("*.json")):
        name = rp.name
        req_p = work / "requests" / name
        if not req_p.exists() or (work / "done" / name).exists():
            continue
        req = json.loads(req_p.read_text("utf-8"))
        try:
            resp = json.loads(rp.read_text("utf-8"))
            if resp.get("decision") not in DECISIONS:
                raise ValueError(f"decision must be one of {sorted(DECISIONS)}")
            if resp["decision"] in ("not_a_skill", "unsure"):
                decisions.append({"term": req["term"], "decision": resp["decision"], "by": by, "run": run, "date": today,
                                  "reason": str(resp.get("reason", ""))[:200]})
                report[resp["decision"]].append(req["term"])
                outcome = None
            else:
                trial = copy.deepcopy(entries)
                if resp["decision"] == "new":
                    new, dropped = build_new(resp, req, trial, by, run, today)
                    new["_file"] = new["key"] + ".json"
                    trial.append(new)
                    report["dropped_claims"] += len(dropped)
                    label = new["preferred_name"]
                else:
                    tgt = add_variant(resp, req, trial, by, run, today)
                    new, dropped, label = tgt, [], f"{req['term']} -> {tgt['preferred_name']}"
                problems = L.validate(trial)
                if problems:
                    raise ValueError("; ".join(problems[:4]))
                entries = trial
                report["new" if resp["decision"] == "new" else "variant"].append(label)
                outcome = new
        except (ValueError, KeyError, TypeError) as e:
            report["rejected"].append((req["term"], str(e)))
            if not dry:
                (work / "rejected").mkdir(parents=True, exist_ok=True)
                (work / "rejected" / name).write_text(json.dumps({"errors": str(e), "request": req["term"]}, indent=1) + "\n", "utf-8")
            continue
        if not dry:
            (work / "done").mkdir(parents=True, exist_ok=True)
            (work / "done" / name).write_text("{}\n", "utf-8")
            if outcome:
                (root / "entries" / outcome["_file"]).write_text(
                    json.dumps(clean(outcome), indent=1, ensure_ascii=False) + "\n", "utf-8")
    if not dry and decisions:
        dec_path.parent.mkdir(exist_ok=True)
        dec_path.write_text(json.dumps(decisions, indent=1, ensure_ascii=False) + "\n", "utf-8")
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work")
    ap.add_argument("--model-id", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    r = ingest(a.work, a.root, "model:" + a.model_id, a.run, a.date, a.dry_run)
    print(("DRY RUN: nothing written. " if a.dry_run else "") +
          f"new {len(r['new'])}, variants {len(r['variant'])}, not a skill {len(r['not_a_skill'])}, "
          f"unsure {len(r['unsure'])}, rejected {len(r['rejected'])}, claims dropped {r['dropped_claims']}")
    for term, why in r["rejected"]:
        print(f"  rejected {term!r}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
