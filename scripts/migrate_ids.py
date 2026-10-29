"""One-off: replace every entry's `skill:NNNN` id with a random 10-character id.

    python3 -I scripts/migrate_ids.py [--dry-run]

The old id is kept in `former_ids`, so anything that still says skill:0082 (the registry, old notes) can be
resolved with lexicon.find(). Every reference to an old id is rewritten: relation targets, replacements, and the
claim keys inside evidence records (relation:broader:<id>). Entries that already have a valid new-style id are left alone. A 10-character id with no digit (an early draft
of the format) is re-issued, and is not recorded as a former id because it was never published.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402

OLD = re.compile(r"skill:\d{4,}")
NO_DIGIT = re.compile(r"[a-z][a-z0-9]{9}")


def rewrite(x, mapping):
    """Replace old ids inside every string of a JSON value."""
    if isinstance(x, str):
        pat = re.compile("|".join(re.escape(k) for k in sorted(mapping, key=len, reverse=True))) if mapping else None
        return pat.sub(lambda m: mapping[m.group(0)], x) if pat else x
    if isinstance(x, list):
        return [rewrite(v, mapping) for v in x]
    if isinstance(x, dict):
        return {k: (v if k == "former_ids" else rewrite(v, mapping)) for k, v in x.items()}
    return x


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(L.ROOT))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    entries, errs = L.load(Path(a.root) / "entries")
    if errs:
        raise SystemExit("; ".join(errs))
    taken = {e["id"] for e in entries} | {f for e in entries for f in e.get("former_ids", [])}
    mapping = {}
    for e in entries:
        if OLD.fullmatch(e["id"]) or (NO_DIGIT.fullmatch(e["id"]) and not L.ID_RE.match(e["id"])):
            mapping[e["id"]] = L.new_id(taken)
            taken.add(mapping[e["id"]])
    for e in entries:
        file = e.pop("_file")
        out = rewrite(e, mapping)
        if e["id"] in mapping:
            rest = {k: v for k, v in out.items() if k != "id"}
            former = {*e.get("former_ids", []), *([e["id"]] if OLD.fullmatch(e["id"]) else [])}
            out = {"id": mapping[e["id"]], **({"former_ids": sorted(former)} if former else {}), **rest}
        if not a.dry_run:
            (Path(a.root) / "entries" / file).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"{'would give' if a.dry_run else 'gave'} {len(mapping)} entries a new id")
    return 0


if __name__ == "__main__":
    sys.exit(main())
