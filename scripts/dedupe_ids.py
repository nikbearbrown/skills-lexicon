"""Find entries that share an id and give the second one a new random id.

    python3 -I scripts/dedupe_ids.py [--apply]

Without --apply it only reports. Entries are taken in file-name order; the first keeps the id, each later one
gets a new id. Ids are compared ignoring case. Only the entry's own `id` changes. Anything elsewhere that
pointed at the shared id (a relation target, a replacement, an evidence key such as relation:broader:<id>) was
written when the two entries were indistinguishable, so it cannot be sorted out by a script: it is listed
for a person, and it now points at the first entry.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402


def references(entries, dup):
    """Where an id is mentioned apart from an entry's own `id`: (file, what)."""
    out = []
    for e in entries:
        for r in e.get("relations", []):
            if L.norm_id(r.get("target", "")) == dup:
                out.append((e["_file"], f"relation {r.get('type')} -> {dup}"))
        for t in e.get("replacements", []):
            if L.norm_id(t) == dup:
                out.append((e["_file"], f"replacement {dup}"))
        for ev in e.get("evidence", []):
            if dup in L.norm_id(ev.get("field", "")) and ev["field"].startswith("relation:"):
                out.append((e["_file"], f"evidence for {ev['field']}"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    entries, errs = L.load(Path(a.root) / "entries")
    if errs:
        raise SystemExit("; ".join(errs))
    taken = {x for e in entries for x in [e["id"], *e.get("former_ids", [])]}
    first, changed = {}, 0
    for e in entries:
        key = L.norm_id(e["id"])
        if key not in first:
            first[key] = e
            continue
        new = L.new_id(taken)
        taken.add(new)
        changed += 1
        print(f"{e['_file']}: id {e['id']} is also used by {first[key]['_file']}; {'new id' if a.apply else 'would become'} {new}")
        for f, what in references(entries, key):
            print(f"    check: {f}: {what} (now points at {first[key]['_file']})")
        if a.apply:
            e["id"] = new
            file = e.pop("_file")
            rest = {k: v for k, v in e.items() if k != "id"}
            (Path(a.root) / "entries" / file).write_text(json.dumps({"id": new, **rest}, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"{changed} duplicate id(s){'' if a.apply or not changed else '; run with --apply to change them'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
