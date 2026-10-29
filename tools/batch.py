"""Write one batch of drafted entries as a pair of files in data/: a JSON file and a Markdown view of it.

    python3 -I tools/batch.py 2026-10-29-pilot-100-tags

The batch is every entry drafted in that run (by the run label on its evidence), plus the tags the run
resolved without a new entry: added as a variant, not a skill, or unsure. entries/*.json stays the source
of truth for each entry; the pair is generated from it and must not be edited by hand. The Markdown is
rendered from the JSON file written beside it, so the two cannot disagree.
Files are named data/skills_batch_NNN.json and .md. Re-running a run reuses its batch number; a new run takes the next.
Entries are listed by name, because ids are random and carry no order.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assess as AS  # noqa: E402
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402

MARK = {"drafted": "○", "backed": "✔", "contradicted": "✖"}


def claim_state(e, key):
    """backed / contradicted / drafted, from the evidence on one claim."""
    evs = [ev for ev in e.get("evidence", []) if ev.get("field") == key]
    if any(ev.get("outcome") == "contradicts" for ev in evs):
        return "contradicted"
    return "backed" if any(L.backs(ev) for ev in evs) else "drafted"


def basis(e, key):
    for ev in e.get("evidence", []):
        if ev.get("field") == key and ev.get("action") == "drafted":
            return ev.get("note", "").replace("basis: ", "")
    return ""


FLAG = {"disagrees_with_legacy": " ⚠ **disagrees with the legacy list/class, check it**",
        "not_in_legacy": " ⚠ the legacy lists/class do not say so, check it"}


def flagged(e, key):
    for ev in e.get("evidence", []):
        if ev.get("field") == key and ev.get("flag"):
            return FLAG.get(ev["flag"], "")
    return ""


def where(lt):
    """Where a legacy tag came from: each file, its rows and its class."""
    parts = [f"`{Path(s['file']).name}` row {', '.join(map(str, s['rows']))} ({s['class']})" for s in lt["sources"]]
    return "legacy tag: " + "; ".join(parts)


def extras(e, key, runs):
    """Who else has looked at this claim: second drafts, checks, and attesting sources, with how much was verified."""
    out = []
    for ev in e.get("evidence", []):
        if ev.get("field") != key:
            continue
        by = ev["by"]
        if ev["action"] == "checked":
            who = by.split(":", 1)[1] + (f" ({runs[ev['run']]['effort']})" if by.startswith("model:") and ev.get("run") in runs else "")
            out.append(f"{who} agrees" if ev["outcome"] == "supports" else f"{who} disagrees ({ev.get('note', '')})")
        elif ev["action"] == "matched_source":
            org = ev.get("organization", {})
            out.append(f"{org.get('name', by)} [{ev.get('verification')}] {ev['outcome']}")
    return " — " + "; ".join(out) if out else ""


def votes_for(root, entries):
    """entry id -> the votes on its tag, worked out from the legacy lists and data/assessments.jsonl."""
    rows = {}
    for g in T.read_tags(root, [T.TAGS] + list(T.LISTS.values())):
        for s in g["sources"].values():
            rows[(s["file"], s["rows"][0])] = L.norm(g["term"])
    tl = AS.tally(root)
    out = {}
    for e in entries:
        for s in e["provenance"].get("legacy_tag", {}).get("sources", []):
            key = rows.get((s["file"], s["rows"][0]))
            if key in tl:
                regs = L.load_runs(root)
                def tag_(v):
                    a = regs.get(v.get("run"), {}).get("agent")
                    return AS.who(v["assessor"])[:-1] + f", {a})" if v["assessor"]["type"] == "model" and a else AS.who(v["assessor"])
                out[e["id"]] = [{"answer": v["answer"], "by": tag_(v), "run": v.get("run")} for v in tl[key]["votes"]]
                break
    return out


def collect(root, run):
    entries, errs = L.load(Path(root) / "entries")
    if errs:
        raise SystemExit("; ".join(errs))
    new = [e for e in entries if f"run {run}," in e["provenance"]["source"]]
    new_ids = {e["id"] for e in new}
    added = []
    for e in entries:
        if e["id"] in new_ids:
            continue
        for ev in e.get("evidence", []):
            if ev.get("run") == run and ev["field"].startswith("variant:"):
                added.append({"term": ev["field"][8:], "added_to": e["id"], "name": e["preferred_name"], "note": ev.get("note", "")})
    dec_path = Path(root) / "data" / "term-decisions.json"
    decisions = [d for d in json.loads(dec_path.read_text("utf-8")) if d.get("run") == run] if dec_path.exists() else []
    rows = {L.norm(g["term"]): g for g in T.read_tags(root, [T.TAGS] + list(T.LISTS.values()))}

    def with_rows(d):
        g = rows.get(L.norm(d["term"]))
        out = {"term": d["term"], "reason": d["reason"]}
        if g:
            out["legacy_tag"] = T.origin(g)
        return out
    return {
        "new": sorted(({k: v for k, v in e.items() if not k.startswith("_")} for e in new), key=lambda e: e["preferred_name"].casefold()),
        "variants_added": added,
        "not_a_skill": [with_rows(d) for d in decisions if d["decision"] == "not_a_skill"],
        "unsure": [with_rows(d) for d in decisions if d["decision"] == "unsure"],
    }


def batch_number(root, run):
    """The number of the existing batch for this run, else the next free one."""
    nums = {}
    for p in sorted((Path(root) / "data").glob("skills_batch_*.json")):
        nums[int(p.stem.rsplit("_", 1)[1])] = json.loads(p.read_text("utf-8")).get("batch", {}).get("run")
    for n, r in nums.items():
        if r == run:
            return n
    return max(nums, default=0) + 1


def build(root, run):
    c = collect(root, run)
    if not c["new"]:
        raise SystemExit(f"no entries were drafted in run {run!r}")
    n = batch_number(root, run)
    models = sorted({ev["by"] for e in c["new"] for ev in e["evidence"] if ev["by"].startswith("model:")})
    legacy = any(e["provenance"].get("legacy_tag") for e in c["new"])
    used = {ev["run"] for e in c["new"] for ev in e["evidence"] if ev.get("run")}
    runs = {k: v for k, v in L.load_runs(root).items() if k in used}
    doc = {
        "batch": {
            "number": n, "run": run, "models": models, "date": c["new"][0]["provenance"]["date"],
            "source": T.TAGS if legacy else c["new"][0]["provenance"]["source"].split(", run ")[0],
            "counts": {"new_entries": len(c["new"]), "variants_added": len(c["variants_added"]),
                       "not_a_skill": len(c["not_a_skill"]), "unsure": len(c["unsure"])},
            "generated": "from entries/*.json by tools/batch.py; do not edit by hand",
            "status": "machine-drafted: no claim in this batch is backed by a human check or a matched source",
        },
        "runs": runs, "votes": votes_for(root, c["new"]),
        "entries": c["new"], "variants_added": c["variants_added"],
        "not_a_skill": c["not_a_skill"], "unsure": c["unsure"],
    }
    return doc, f"skills_batch_{n:03d}"


def render_md(doc, names):
    b = doc["batch"]
    runs = doc.get("runs", {})
    out = [f"# Skills lexicon batch {b['number']:03d}", "",
           f"Run `{b['run']}` · {b['date']} · " + (f"drafted by {', '.join(f'`{m}`' for m in b['models'])} · " if b['models'] else "imported from a source, not drafted by a model · ")
           + f"source `{b['source']}`", "",
           "**Generated from the JSON file beside this one. Do not edit it; correct `entries/<key>.json` instead.**", "",
           "Every claim below carries a marker: ○ drafted by a model, not yet checked · ✔ backed by a human check or a matched source · "
           "✖ contradicted. The words after a claim say what the model said it was based on, then who else has looked at it. "
           "Only ✔ counts. Votes say who thinks the tag is something job listings ask for; they back nothing. "
           "Class is worked out from kind: ability, certification, language, or skill (what is left).", "",
           "| New entries | Added as a variant | Not a skill | Unsure |", "|---|---|---|---|",
           "| {new_entries} | {variants_added} | {not_a_skill} | {unsure} |".format(**b["counts"]), "", "---", ""]
    for e in doc["entries"]:
        lt = e["provenance"].get("legacy_tag", {})
        src = where(lt) if lt else e["provenance"]["source"]
        flag = " ⚠ class conflict in the legacy lists" if lt.get("class_conflict") else ""
        out += [f"## {e['preferred_name']}", "",
                f"`{e['id']}` · {L.top_class(e)} · {e['kind']} · {e['status']} · {src}{flag}", ""]

        def line(label, text, key):
            b_ = basis(e, key)
            out.append(f"- **{label}:** {text} {MARK[claim_state(e, key)]}" + (f" _{b_}_" if b_ else "") + f"{flagged(e, key)}{extras(e, key, runs)}")
        vs = doc.get("votes", {}).get(e["id"])
        if vs:
            groups = {}
            for v in vs:
                groups.setdefault(v["answer"], []).append(v["by"])
            out.append("- **Votes (is it something job listings ask for?):** " + " · ".join(f"{a}: {', '.join(groups[a])}" for a in ("yes", "unsure", "no") if a in groups))
        line("Definition", e["definition"], "definition")
        line("Kind", e["kind"], "kind")
        for i in e.get("identifiers", []):
            out.append(f"- **Identifier:** {i['scheme']} `{i['code']}`")
        if "certification" in e:
            line("Certification", "yes" if e["certification"] else "no", "certification")
        if "certification_scope" in e:
            line("Certification scope", {"single-issuer": "one issuer", "many-issuers": "many issuers"}[e["certification_scope"]], "certification_scope")
        if "language_type" in e:
            line("Language type", e["language_type"], "language_type")
        c = e.get("credential")
        if c:
            iss = "; ".join(f"{i['name']}" + (f" ({i['url']})" if i.get("url") else "") for i in c.get("issuers", [])) or "not mapped yet"
            out.append(f"- **Credential:** {c.get('official_name', e['preferred_name'])} · {c['credential_type']} · {c.get('specificity', '')} · "
                       f"status {c.get('status', 'unknown')} · issuer: {iss}")
            if c.get("fields"):
                out.append(f"  - field: {', '.join(f['label'] for f in c['fields'])}" + (f" · level: {c['level']['label']}" + (f" (rank {c['level']['rank']} of {c['level']['of']} in {c['level'].get('scheme', 'its ladder')})" if c['level'].get('rank') and c['level'].get('of') else "") if c.get("level") else ""))
            for s in c["sources"][:4]:
                out.append(f"  - source ({s['kind']}, {s['verification']}): {s['url']}")
        if e.get("notes"):
            out.append(f"- **Note:** {e['notes']} ⚠")
        for v in e.get("variants", []):
            line("Also written", v["label"], f"variant:{L.norm(v['label'])}")
        for r in e.get("relations", []):
            line("Relation", f"{r['type']} → {names.get(r['target'], r['target'])} (`{r['target']}`)", f"relation:{r['type']}:{r['target']}")
        for v in e.get("verbs", []):
            line("Verb", v, f"verb:{L.norm(v)}")
        out.append("")
    if doc["variants_added"]:
        out += ["---", "", "## Added as a variant of an existing entry", ""]
        out += [f"- {v['term']} → **{v['name']}** (`{v['added_to']}`) ○" for v in doc["variants_added"]] + [""]
    for key, title in (("not_a_skill", "Not a skill"), ("unsure", "Unsure: needs a person")):
        if doc[key]:
            out += ["---", "", f"## {title}", ""]
            for d in doc[key]:
                lt = d.get("legacy_tag")
                out.append(f"- **{d['term']}** ({where(lt)[12:]}): {d['reason']}" if lt else f"- **{d['term']}**: {d['reason']}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--root", default=str(L.ROOT))
    a = ap.parse_args(argv)
    doc, stem = build(a.root, a.run)
    entries, _ = L.load(Path(a.root) / "entries")
    names = {e["id"]: e["preferred_name"] for e in entries}
    d = Path(a.root) / "data"
    d.mkdir(exist_ok=True)
    (d / f"{stem}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", "utf-8")
    written = json.loads((d / f"{stem}.json").read_text("utf-8"))      # render from what was written
    (d / f"{stem}.md").write_text(render_md(written, names), "utf-8")
    print(f"wrote data/{stem}.json and data/{stem}.md: {doc['batch']['counts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
