"""Import the O*NET abilities as `ability` entries, each with O*NET as the attesting organization.

    python3 -I scripts/import_onet_abilities.py [abilities/onet-abilities.json]

The file holds the O*NET 30.2 abilities under CC BY 4.0 (see THIRD-PARTY-NOTICES.md): element id, name, definition,
category and subcategory. Every entry gets a `matched_source` evidence record for `kind` (O*NET lists it under Abilities) and for
`definition` (the text is O*NET's), both `dump-match` because the data is the O*NET database file itself. The entries
stay `proposed`: a source match is not a person's review. Skills, Knowledge and Work Activities are not in those
files and come later, from the O*NET database download.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RUN, DATE, VERSION = "2026-10-29-onet-abilities-import", "2026-10-29", "30.2"
ORG = {"name": "O*NET, U.S. Department of Labor, Employment and Training Administration", "url": "https://www.onetcenter.org/",
       "type": "government", "country": "US"}


def main(path=ROOT / "abilities" / "onet-abilities.json"):
    d = json.loads(Path(path).read_text("utf-8"))
    entries, _ = L.load(ROOT / "entries")
    taken = {x["id"] for x in entries} | {f for x in entries for f in x.get("former_ids", [])}
    keys = {x.get("key") for x in entries}
    have = {tuple(i.values()) for e in entries for i in e.get("identifiers", [])}
    n = 0
    for a in d["abilities"]:
        if ("onet-element", a["element_id"]) in have:
            continue
        cat, subcat = a["category"], a.get("subcategory")
        cats = ["Abilities", cat] + ([subcat] if subcat else [])
        ev = lambda field, note: {   # noqa: E731
            "field": field, "by": f"source:onet-{VERSION}", "action": "matched_source", "kind": "onet", "verification": "dump-match",
            "outcome": "supports", "ref": f"onet:{a['element_id']}", "date": DATE, "run": RUN, "note": note, "organization": ORG,
            "match": {"dataset": f"onet-{VERSION}", "dataset_id": a["element_id"], "method": "import", "categories": cats}}
        key = I.slugify(a["name"], keys)
        keys.add(key)
        new_id = L.new_id(taken)
        taken.add(new_id)
        e = {"id": new_id, "key": key, "preferred_name": a["name"], "kind": "ability", "definition": a["definition"].strip(),
             "identifiers": [{"scheme": "onet-element", "code": a["element_id"]}],
             "variants": [], "relations": [], "verbs": [], "status": "proposed",
             "provenance": {"source": f"imported from O*NET {VERSION} Abilities (USDOL/ETA, CC BY 4.0) "
                                      f"abilities/onet-abilities.json, run {RUN}",
                            "date": DATE, "review": "Awaiting taxonomy owner review", "reviewed_by": None},
             "evidence": [ev("kind", f"O*NET {VERSION} lists it under Abilities, {cat}" + (f", {subcat}" if subcat else "")),
                          ev("definition", f"the definition is O*NET {VERSION}'s text")]}
        (ROOT / "entries" / f"{key}.json").write_text(json.dumps(e, indent=1, ensure_ascii=False) + "\n", "utf-8")
        n += 1
    print(f"wrote {n} ability entries")


if __name__ == "__main__":
    main(*sys.argv[1:2])
