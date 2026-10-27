"""One-off import of the jobs.humanitarians.ai skills registry into entries/.

    python3 -I scripts/import_registry.py <path to data/skills/registry.json>

Legacy row ids are NOT copied: the site keeps the original rows private. The registry's
'narrower' relation (this concept is narrower than the target) becomes 'broader' on this
entry; no roll-up decision is made, so rolls_up is left unset (counts stay direct).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from lexicon import norm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def match_for(label):
    return "exact_case" if len(label) <= 3 or (label.isupper() and len(label) <= 5) else "word_ci"


def main(path):
    reg = json.loads(Path(path).read_text("utf-8"))
    concepts = reg["concepts"]
    owners = {}
    for c in concepts:
        for lab, ctx in [(c["name"], c["contexts"])] + [(a["label"], a["contexts"]) for a in c["aliases"]]:
            owners.setdefault(norm(lab), []).append((c["id"], set(ctx)))

    def ambiguous(cid, lab, ctx):
        for oid, octx in owners[norm(lab)]:
            if oid != cid and not (ctx and octx and not (ctx & octx)):
                return True
        return False

    out = ROOT / "entries"
    for c in concepts:
        e = {"id": c["id"], "key": c["key"], "preferred_name": c["name"], "kind": c["kind"],
             "definition": c["definition"]}
        if match_for(c["name"]) != "word_ci":
            e["name_match"] = match_for(c["name"])
        if c["contexts"]:
            e["needs_context"] = c["contexts"]
        if ambiguous(c["id"], c["name"], set(c["contexts"])):
            e["name_ambiguous"] = True
        e["variants"] = []
        for a in c["aliases"]:
            if norm(a["label"]) == norm(c["name"]) and set(a["contexts"]) <= set(c["contexts"]):
                continue   # the registry lists the name again as an alias (differs only in case)
            v = {"label": a["label"], "match": match_for(a["label"])}
            if a["contexts"]:
                v["needs_context"] = a["contexts"]
            if ambiguous(c["id"], a["label"], set(a["contexts"] or c["contexts"])):
                v["ambiguous"] = True
            e["variants"].append(v)
        e["relations"] = [{"type": {"narrower": "broader"}.get(r["relation"], r["relation"]), "target": r["targetId"]}
                          for r in c["relations"]]
        e["verbs"] = []
        e["status"] = c["status"]
        e["provenance"] = {"source": f"imported from the jobs.humanitarians.ai skills registry {reg['version']}",
                           "date": c["provenance"]["date"], "review": c["provenance"]["review"], "reviewed_by": None}
        if c.get("replacements"):
            e["replacements"] = c["replacements"]
        (out / f"{c['key']}.json").write_text(json.dumps(e, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"wrote {len(concepts)} entries")


if __name__ == "__main__":
    main(sys.argv[1])
