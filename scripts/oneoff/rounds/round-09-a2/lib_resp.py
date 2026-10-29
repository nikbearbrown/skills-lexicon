"""Scratch helpers for writing answers; lives in work/ only."""
import glob, json, os, re

GK = "general-knowledge"
REQ = {}
for _f in sorted(glob.glob("work/requests/*.json")):
    _r = json.load(open(_f))
    _t = re.sub(r"\s*\((Programming Language|Language)\)\s*$", "", _r["term"]).strip()
    assert _t not in REQ, _t
    REQ[_t] = (os.path.basename(_f), _r)
WRITTEN = set()


def _write(term, resp):
    fn, _ = REQ[term]
    assert term not in WRITTEN, term
    WRITTEN.add(term)
    json.dump(resp, open(os.path.join("work/responses", fn), "w"), indent=1, ensure_ascii=False)
    open(os.path.join("work/responses", fn), "a").write("\n")


def nid(req, name):
    hits = [n["id"] for n in req["nearest"] if n["name"] == name]
    assert len(hits) == 1, (req["term"], name, hits)
    return hits[0]


def variant_of(term, target_name, reason=None):
    _, req = REQ[term]
    _write(term, {"decision": "variant_of", "variant_of": nid(req, target_name),
                  "reason": reason or f"Same concept as the existing entry {target_name}; only the legacy label differs.",
                  "entry": None})


def unsure(term, reason):
    _write(term, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})


def not_a_skill(term, reason):
    _write(term, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})


def new(term, name, kind, definition, variants=(), rels=(), verbs=(), lang="programming", note="", reason=None, lang_basis_note=None):
    _, req = REQ[term]
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": nid(req, n), "basis": GK} for t, n in rels],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": False, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    _write(term, {"decision": "new", "variant_of": None,
                  "reason": reason or "A named skill with no matching entry among the nearest.", "entry": entry})


def human(term, name, definition, variants=(), rels=(), reason=None):
    new(term, name, "human-language", definition, variants, rels, ("speak", "write"), "human",
        reason=reason or "A human language with no matching entry among the nearest.")


def prog(term, name, definition, variants=(), rels=(), kind="programming-language", verbs=("write",), reason=None):
    new(term, name, kind, definition, variants, rels, verbs, "programming",
        reason=reason or "A programming language with no matching entry among the nearest.")


def finish(expected):
    missing = [t for t in expected if t not in WRITTEN]
    assert not missing, missing
