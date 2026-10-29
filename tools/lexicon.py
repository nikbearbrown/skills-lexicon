"""Skills lexicon: load entries, validate them, build the lookup index. Standard library only.

    python3 -I tools/lexicon.py validate     # exit 1 on any error
    python3 -I tools/lexicon.py index        # writes build/index.json
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUSES = {"machine-drafted", "proposed", "reviewed", "deprecated"}
MATCHES = {"word_ci", "exact_case"}
REL_TYPES = {"broader", "part_of", "related", "contrast"}
UP_TYPES = {"broader", "part_of"}      # edges that can roll a count up to the target
KIND_RE = re.compile(r"^[a-z][a-z-]*$")
ID_RE = re.compile(r"^skill:\d{4,}$")
ACTIONS = {"drafted", "checked", "matched_source"}
OUTCOMES = {"supports", "contradicts"}
BY_RE = re.compile(r"^(model|human|source):\S.*$")
LANGUAGE_TYPES = {"programming", "spoken", "other"}    # other: markup, query, modelling and similar formal languages


def default_match(label):
    """Short or all-caps labels (R, Go, AWS) must match case-exactly; longer ones ignore case."""
    return "exact_case" if len(label) <= 3 or (label.isupper() and len(label) <= 5) else "word_ci"


def norm(label):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", label).strip()).lower()


def load(entries_dir=ROOT / "entries"):
    """Return (entries, errors). A file that is not valid JSON is an error, not a crash."""
    entries, errors = [], []
    for p in sorted(Path(entries_dir).glob("*.json")):
        try:
            d = json.loads(p.read_text("utf-8"))
        except ValueError as e:
            errors.append(f"{p.name}: not valid JSON ({e})")
            continue
        d["_file"] = p.name
        entries.append(d)
    return entries, errors


def forms(e):
    """Every surface form that resolves to this entry: its preferred name plus its variants."""
    ctx = tuple(e.get("needs_context", []))
    yield {"label": e["preferred_name"], "match": e.get("name_match", "word_ci"),
           "needs_context": ctx, "ambiguous": bool(e.get("name_ambiguous"))}
    for v in e.get("variants", []):
        yield {"label": v["label"], "match": v.get("match", "word_ci"),
               "needs_context": tuple(v.get("needs_context", ctx)), "ambiguous": bool(v.get("ambiguous"))}


def claim_keys(e):
    """Every separate assertion an entry makes. Evidence attaches to one of these."""
    keys = {"kind", "definition"}
    keys |= {f"variant:{norm(v['label'])}" for v in e.get("variants", []) if v.get("label")}
    keys |= {f"relation:{r['type']}:{r['target']}" for r in e.get("relations", []) if "type" in r and "target" in r}
    keys |= {f"verb:{norm(v)}" for v in e.get("verbs", [])}
    keys |= {k for k in ("certification", "language_type") if k in e}
    return keys


def backs(ev):
    """Evidence that counts toward 'reviewed': a named person's check, or a matched outside source.
    A model agreeing with a model does not count; two models can share one mistake."""
    return ev.get("outcome") == "supports" and (
        (ev.get("action") == "checked" and str(ev.get("by", "")).startswith("human:"))
        or ev.get("action") == "matched_source")


def check_evidence(e, errs):
    f, claims, evid = e.get("_file", "?"), claim_keys(e), e.get("evidence", [])
    for ev in evid:
        if ev.get("field") not in claims:
            errs.append(f"{f}: evidence for {ev.get('field')!r}, which is not a claim in this entry")
        if not BY_RE.match(str(ev.get("by", ""))):
            errs.append(f"{f}: evidence 'by' must look like model:<id>, human:<name> or source:<name>")
        if ev.get("action") not in ACTIONS:
            errs.append(f"{f}: evidence action must be one of {sorted(ACTIONS)}")
        if not ev.get("date"):
            errs.append(f"{f}: evidence needs a date")
        if ev.get("action") in ("checked", "matched_source") and ev.get("outcome") not in OUTCOMES:
            errs.append(f"{f}: a {ev.get('action')} evidence needs outcome supports or contradicts")
        if ev.get("action") == "matched_source" and not ev.get("ref"):
            errs.append(f"{f}: matched_source evidence needs a ref (URL, code or ad id)")
        if ev.get("action") == "drafted" and str(ev.get("by", "")).startswith("source:"):
            errs.append(f"{f}: a source cannot draft; use matched_source")
    if e.get("status") == "machine-drafted":
        drafted = {ev.get("field") for ev in evid if ev.get("action") == "drafted"}
        for k in sorted(claims - drafted):
            errs.append(f"{f}: machine-drafted entry has no 'drafted' evidence for {k}")
    if e.get("status") == "reviewed":
        backed = {ev.get("field") for ev in evid if backs(ev)}
        for k in sorted(claims - backed):
            errs.append(f"{f}: reviewed entry has no human check or matched source for {k}")
        for ev in evid:
            if ev.get("outcome") == "contradicts":
                errs.append(f"{f}: reviewed entry has unresolved contradicting evidence on {ev.get('field')}")


def validate(entries):
    errs = []
    ids = {}
    for e in entries:
        f = e.get("_file", "?")
        for key in ("id", "preferred_name", "kind", "definition", "status", "provenance"):
            if not e.get(key):
                errs.append(f"{f}: missing {key}")
        if errs and errs[-1].startswith(f"{f}: missing"):
            continue
        if not ID_RE.match(e["id"]):
            errs.append(f"{f}: id {e['id']!r} is not skill:NNNN")
        if e["id"] in ids:
            errs.append(f"{f}: id {e['id']} also used by {ids[e['id']]}")
        ids[e["id"]] = f
        if f != f"{e.get('key', Path(f).stem)}.json" and "key" in e:
            errs.append(f"{f}: key {e['key']!r} does not match the file name")
        if not KIND_RE.match(e["kind"]):
            errs.append(f"{f}: kind {e['kind']!r} must be lower-case words joined by hyphens")
        if "certification" in e and not isinstance(e["certification"], bool):
            errs.append(f"{f}: certification must be true or false")
        if "language_type" in e and e["language_type"] not in LANGUAGE_TYPES:
            errs.append(f"{f}: language_type must be one of {sorted(LANGUAGE_TYPES)}")
        if e["status"] not in STATUSES:
            errs.append(f"{f}: status {e['status']!r} not one of {sorted(STATUSES)}")
        p = e["provenance"]
        if not (isinstance(p, dict) and p.get("source") and p.get("date")):
            errs.append(f"{f}: provenance needs source and date")
        if e["status"] == "reviewed":
            if not (isinstance(p, dict) and p.get("reviewed_by")):
                errs.append(f"{f}: a reviewed entry needs provenance.reviewed_by")
        check_evidence(e, errs)
        if e.get("name_match", "word_ci") not in MATCHES:
            errs.append(f"{f}: name_match must be one of {sorted(MATCHES)}")
        seen = set()
        for fm in forms(e):
            if fm["match"] not in MATCHES:
                errs.append(f"{f}: variant {fm['label']!r} has match {fm['match']!r}")
            if not fm["label"].strip():
                errs.append(f"{f}: empty variant label")
            k = (norm(fm["label"]), fm["needs_context"])
            if k in seen:
                errs.append(f"{f}: {fm['label']!r} listed twice")
            seen.add(k)
        if e["status"] == "deprecated":
            if not e.get("replacements"):
                errs.append(f"{f}: a deprecated entry needs replacements")
    by_id = {e["id"]: e for e in entries if e.get("id")}
    for e in entries:
        f = e.get("_file", "?")
        for r in e.get("relations", []):
            if r.get("type") not in REL_TYPES:
                errs.append(f"{f}: relation type {r.get('type')!r} not one of {sorted(REL_TYPES)}")
            if r.get("target") not in by_id:
                errs.append(f"{f}: relation target {r.get('target')} does not exist")
            elif r["target"] == e["id"]:
                errs.append(f"{f}: relation to itself")
            if "rolls_up" in r and not isinstance(r["rolls_up"], bool):
                errs.append(f"{f}: rolls_up must be true or false")
            if "rolls_up" in r and r.get("type") not in UP_TYPES:
                errs.append(f"{f}: rolls_up only applies to {sorted(UP_TYPES)}")
        for t in e.get("replacements", []):
            if t not in by_id:
                errs.append(f"{f}: replacement {t} does not exist")
    # two concepts may share a surface form only if context separates them or both say it is ambiguous
    groups = {}
    for e in entries:
        if e.get("id") and e.get("preferred_name"):
            for fm in forms(e):
                groups.setdefault(norm(fm["label"]), []).append((e, fm))
    for label, items in groups.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                (a, fa), (b, fb) = items[i], items[j]
                if a["id"] == b["id"]:
                    continue
                ca, cb = set(fa["needs_context"]), set(fb["needs_context"])
                if ca and cb and not (ca & cb):
                    continue
                if fa["ambiguous"] and fb["ambiguous"]:
                    continue
                errs.append(f"'{label}' is claimed by {a['id']} and {b['id']} without separating context; "
                            "give each a different needs_context, or mark both ambiguous")
    # broader / part_of must not loop
    state = {}

    def visit(i, path):
        if state.get(i) == 1:
            errs.append("loop in broader/part_of: " + " -> ".join(path + [i]))
            return
        if state.get(i) == 2 or i not in by_id:
            return
        state[i] = 1
        for r in by_id[i].get("relations", []):
            if r.get("type") in UP_TYPES:
                visit(r["target"], path + [i])
        state[i] = 2
    for i in by_id:
        visit(i, [])
    return errs


def build_index(entries):
    """Surface form -> candidate concepts, plus every relation in both directions."""
    variants, rel = {}, {e["id"]: [] for e in entries}
    inverse = {"broader": "narrower", "part_of": "has_part", "related": "related", "contrast": "contrast"}
    for e in entries:
        if e["status"] == "deprecated":
            continue
        for fm in forms(e):
            variants.setdefault(norm(fm["label"]), []).append(
                {"id": e["id"], "label": fm["label"], "match": fm["match"],
                 "needs_context": list(fm["needs_context"]), "ambiguous": fm["ambiguous"]})
        for r in e.get("relations", []):
            rel[e["id"]].append({"type": r["type"], "target": r["target"], "rolls_up": bool(r.get("rolls_up"))})
            if r["target"] in rel:
                rel[r["target"]].append({"type": inverse[r["type"]], "target": e["id"], "rolls_up": False})
    return {"variants": variants, "relations": rel}


def rollup(entries, concept_id):
    """Ids that also receive a count when concept_id is mentioned: follow only edges marked rolls_up."""
    by_id = {e["id"]: e for e in entries}
    out, todo = [], [concept_id]
    while todo:
        cur = todo.pop()
        for r in by_id[cur].get("relations", []):
            if r.get("type") in UP_TYPES and r.get("rolls_up") is True and r["target"] not in out:
                out.append(r["target"])
                todo.append(r["target"])
    return out


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "validate"
    entries, errs = load()
    errs += validate(entries)
    for m in errs:
        print("ERROR", m)
    if cmd == "index" and not errs:
        out = ROOT / "build"
        out.mkdir(exist_ok=True)
        (out / "index.json").write_text(json.dumps(build_index(entries), indent=1, ensure_ascii=False) + "\n", "utf-8")
        print(f"wrote build/index.json for {len(entries)} entries")
    by = {}
    for e in entries:
        by[e["status"]] = by.get(e["status"], 0) + 1
    total = sum(len(claim_keys(e)) for e in entries if e.get("id"))
    backed = sum(len({ev.get("field") for ev in e.get("evidence", []) if backs(ev)}) for e in entries if e.get("id"))
    print(f"{len(entries)} entries {dict(sorted(by.items()))}; {len(errs)} errors")
    print(f"claims: {total}; backed by a human check or a matched source: {backed}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
