"""Compare two independent drafts of the same legacy tags and list where they disagree.

    python3 -I scripts/compare_runs.py --a-root <dir> --a-run <label> --b-root <dir> --b-run <label> [--out report.md]

Each root is a skills-lexicon folder; each run is the label the drafts were ingested under. Tags are matched by
their text. Compared exactly: the decision (new, variant of, not a skill, unsure), kind, certification,
language_type, variants, relations and verbs. Definitions cannot be compared by a script, so they are shown
side by side with a rough word-overlap score, and low scores are listed for a person.

A disagreement says where to look first. Agreement says nothing about whether either draft is true: two runs
of one model can share a mistake, and the validator never counts a model's agreement as backing a claim.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402
import tags_to_candidates as T  # noqa: E402


def outcomes(root, run):
    """norm(tag) -> {'decision', 'entry'?, 'target'?, 'reason'?} for everything the run resolved."""
    root = Path(root)
    entries, _ = L.load(root / "entries")
    by_rows = {}
    for g in T.read_tags(root, [T.TAGS] + list(T.LISTS.values())):
        for s in g["sources"].values():
            by_rows[(s["file"], s["rows"][0])] = g["term"]
    out = {}
    new_ids = set()
    for e in entries:
        if f"run {run}," in e["provenance"]["source"]:
            new_ids.add(e["id"])
            for s in e["provenance"].get("legacy_tag", {}).get("sources", []):
                term = by_rows.get((s["file"], s["rows"][0]))
                if term:
                    out[L.norm(term)] = {"decision": "new", "term": term, "entry": e}
                    break
    for e in entries:
        if e["id"] in new_ids:
            continue
        for ev in e.get("evidence", []):
            if ev.get("run") == run and ev["field"].startswith("variant:"):
                out[ev["field"][8:]] = {"decision": "variant_of", "term": ev["field"][8:], "target": e["preferred_name"], "target_id": e["id"]}
    dec = root / "data" / "term-decisions.json"
    for d in (json.loads(dec.read_text("utf-8")) if dec.exists() else []):
        if d.get("run") == run:
            out[L.norm(d["term"])] = {"decision": d["decision"], "term": d["term"], "reason": d["reason"]}
    return out


def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - {"a", "an", "the", "of", "and", "or", "to", "for", "in", "on", "by", "is", "that", "as", "with"}


def overlap(x, y):
    a, b = words(x), words(y)
    return len(a & b) / len(a | b) if a | b else 1.0


def labels(e):
    return {L.norm(v["label"]) for v in e.get("variants", [])}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a-root", required=True)
    ap.add_argument("--a-run", required=True)
    ap.add_argument("--b-root", required=True)
    ap.add_argument("--b-run", required=True)
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    A, B = outcomes(a.a_root, a.a_run), outcomes(a.b_root, a.b_run)
    a_names = {e["id"]: e["preferred_name"] for e in L.load(Path(a.a_root) / "entries")[0]}
    b_names = {e["id"]: e["preferred_name"] for e in L.load(Path(a.b_root) / "entries")[0]}
    tags = sorted(set(A) | set(B))
    both, diffs, only = [], [], []
    for t in tags:
        x, y = A.get(t), B.get(t)
        if x is None or y is None:
            only.append((t, "A" if x else "B", (x or y)["decision"]))
        elif x["decision"] != y["decision"]:
            diffs.append((x["term"], [("decision", x["decision"] + (f" ({x['reason']})" if x.get("reason") else ""),
                                       y["decision"] + (f" ({y['reason']})" if y.get("reason") else ""))]))
        elif x["decision"] == "new":
            both.append((x, y))
        else:
            both.append((x, y))
    fields = []
    low = []
    for x, y in both:
        if x["decision"] != "new":
            if x["decision"] == "variant_of" and x["target"] != y["target"]:
                diffs.append((x["term"], [("variant of", x["target"], y["target"])]))
            continue
        ea, eb = x["entry"], y["entry"]
        d = []
        if L.norm(ea["preferred_name"]) != L.norm(eb["preferred_name"]):
            d.append(("name", ea["preferred_name"], eb["preferred_name"]))
        for k in ("kind", "certification", "language_type"):
            if ea.get(k) != eb.get(k):
                d.append((k, ea.get(k), eb.get(k)))
        if labels(ea) != labels(eb):
            d.append(("variants only in A / only in B", sorted(labels(ea) - labels(eb)), sorted(labels(eb) - labels(ea))))
        ra = {(r["type"], a_names.get(r["target"], r["target"])) for r in ea.get("relations", [])}
        rb = {(r["type"], b_names.get(r["target"], r["target"])) for r in eb.get("relations", [])}
        if ra != rb:
            d.append(("relations only in A / only in B", sorted(ra - rb), sorted(rb - ra)))
        va, vb = {L.norm(v) for v in ea.get("verbs", [])}, {L.norm(v) for v in eb.get("verbs", [])}
        if va != vb:
            d.append(("verbs only in A / only in B", sorted(va - vb), sorted(vb - va)))
        s = overlap(ea["definition"], eb["definition"])
        if s < 0.35:
            low.append((x["term"], round(s, 2), ea["definition"], eb["definition"]))
        if d:
            diffs.append((x["term"], d))
    n_new = sum(1 for x, y in both if x["decision"] == "new")
    lines = [f"# Comparison of two drafts of the same tags", "",
             f"A = `{a.a_run}` in `{a.a_root}`. B = `{a.b_run}` in `{a.b_root}`.", "",
             f"- Tags resolved by both: {len(both) + sum(1 for _, ds in diffs if ds and ds[0][0] == 'decision')} of {len(tags)}"
             + (f"; resolved by only one run: {len(only)}" if only else ""),
             f"- Same decision on {len(both)} tags ({n_new} of them new entries in both).",
             f"- Tags with at least one disagreement: {len(diffs)}.",
             f"- New entries whose definitions overlap little (score under 0.35): {len(low)}.", "",
             "A disagreement is where to look first. Agreement proves nothing: two drafts by one model can share a mistake.", ""]
    if only:
        lines += ["## Resolved by only one run", ""] + [f"- {t}: only {w} ({d})" for t, w, d in only] + [""]
    lines += ["## Disagreements", ""]
    for term, ds in diffs:
        lines.append(f"### {term}")
        lines += [f"- **{f}** — A: {x!r} · B: {y!r}" for f, x, y in ds]
        lines.append("")
    if low:
        lines += ["## Definitions that differ a lot", ""]
        for term, s, da, db in low:
            lines += [f"### {term} (overlap {s})", f"- A: {da}", f"- B: {db}", ""]
    text = "\n".join(lines).rstrip() + "\n"
    if a.out:
        Path(a.out).write_text(text, "utf-8")
        print(f"wrote {a.out}: {len(tags)} tags, {len(diffs)} with a disagreement, {len(low)} definitions to read")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
