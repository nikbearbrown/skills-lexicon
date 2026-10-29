"""Write one batch of drafted entries as a pair of files in data/: a JSON file and a Markdown view of it.

    python3 -I tools/batch.py 2026-10-29-pilot-100-tags

The batch is every entry drafted in that run (by the run label on its evidence), plus the tags the run
resolved without a new entry: added as a variant, not a skill, or unsure. entries/*.json stays the source
of truth for each entry; the pair is generated from it and must not be edited by hand. The Markdown is
rendered from the JSON file written beside it, so the two cannot disagree.
Files are named data/skills_<first id>-<last id>.json and .md, with ids zero-padded to 5 digits.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402

MARK = {"drafted": "○", "backed": "✔", "contradicted": "✖"}


def number(e):
    return int(e["id"][6:])


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
        "new": sorted(({k: v for k, v in e.items() if not k.startswith("_")} for e in new), key=number),
        "variants_added": added,
        "not_a_skill": [with_rows(d) for d in decisions if d["decision"] == "not_a_skill"],
        "unsure": [with_rows(d) for d in decisions if d["decision"] == "unsure"],
    }


def build(root, run):
    c = collect(root, run)
    if not c["new"]:
        raise SystemExit(f"no entries were drafted in run {run!r}")
    first, last = number(c["new"][0]), number(c["new"][-1])
    models = sorted({ev["by"] for e in c["new"] for ev in e["evidence"]})
    doc = {
        "batch": {
            "run": run, "models": models, "date": c["new"][0]["provenance"]["date"],
            "source": T.TAGS, "id_range": [f"skill:{first:05d}", f"skill:{last:05d}"],
            "counts": {"new_entries": len(c["new"]), "variants_added": len(c["variants_added"]),
                       "not_a_skill": len(c["not_a_skill"]), "unsure": len(c["unsure"])},
            "generated": "from entries/*.json by tools/batch.py; do not edit by hand",
            "status": "machine-drafted: no claim in this batch is backed by a human check or a matched source",
        },
        "entries": c["new"], "variants_added": c["variants_added"],
        "not_a_skill": c["not_a_skill"], "unsure": c["unsure"],
    }
    return doc, f"skills_{first:05d}-{last:05d}"


def render_md(doc, names):
    b = doc["batch"]
    out = [f"# Skills lexicon batch {b['id_range'][0].split(':')[1]}–{b['id_range'][1].split(':')[1]}", "",
           f"Run `{b['run']}` · {b['date']} · drafted by {', '.join(f'`{m}`' for m in b['models'])} · source `{b['source']}`", "",
           "**Generated from the JSON file beside this one. Do not edit it; correct `entries/<key>.json` instead.**", "",
           "Every claim below carries a marker: ○ drafted by a model, not yet checked · ✔ backed by a human check or a matched source · "
           "✖ contradicted. The words after a claim say what the model said it was based on. "
           "Only ✔ counts. Nothing in this batch has it yet.", "",
           "| New entries | Added as a variant | Not a skill | Unsure |", "|---|---|---|---|",
           "| {new_entries} | {variants_added} | {not_a_skill} | {unsure} |".format(**b["counts"]), "", "---", ""]
    for e in doc["entries"]:
        lt = e["provenance"].get("legacy_tag", {})
        src = where(lt) if lt else e["provenance"]["source"]
        flag = " ⚠ class conflict in the legacy lists" if lt.get("class_conflict") else ""
        out += [f"## {e['preferred_name']}", "",
                f"`{e['id']}` · {e['kind']} · {e['status']} · {src}{flag}", ""]

        def line(label, text, key):
            out.append(f"- **{label}:** {text} {MARK[claim_state(e, key)]} _{basis(e, key)}_{flagged(e, key)}")
        line("Definition", e["definition"], "definition")
        line("Kind", e["kind"], "kind")
        if "certification" in e:
            line("Certification", "yes" if e["certification"] else "no", "certification")
        if "language_type" in e:
            line("Language type", e["language_type"], "language_type")
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
