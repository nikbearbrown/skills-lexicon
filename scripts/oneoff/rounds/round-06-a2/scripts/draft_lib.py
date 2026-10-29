import glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = sorted(glob.glob(os.path.join(ROOT, "requests", "*.json")))
GK = "general-knowledge"
LANG_KINDS = {"human-language": "human", "programming-language": "programming", "markup-language": "programming",
              "style-language": "programming", "modeling-language": "programming"}


def _req(i, term):
    r = json.load(open(FILES[i]))
    assert r["term"] == term, (i, term, r["term"])
    return r, os.path.basename(FILES[i])


def _write(i, term, resp):
    r, name = _req(i, term)
    json.dump(resp, open(os.path.join(ROOT, "responses", name), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(ROOT, "responses", name), "a").write("\n")


def new(i, term, name, kind, definition, *, variants=(), relations=(), verbs=(), cert=False, scope=None,
        note="", reason=None):
    r, _ = _req(i, term)
    ids = {n["id"] for n in r["nearest"]}
    for t, tgt in relations:
        assert tgt in ids, (term, tgt)
    lang = LANG_KINDS.get(kind)
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tgt, "basis": GK} for t, tgt in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": bool(cert), "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        assert scope in ("single-issuer", "many-issuers"), term
        entry["certification_scope"] = {"value": scope, "basis": GK}
    _write(i, term, {"decision": "new", "variant_of": None, "reason": reason or f"{name} is a recognised {kind.replace('-', ' ')}.",
                     "entry": entry})


def variant(i, term, target, reason):
    r, _ = _req(i, term)
    assert target in {n["id"] for n in r["nearest"]}
    _write(i, term, {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None})


def no(i, term, reason):
    _write(i, term, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})


def unsure(i, term, reason):
    _write(i, term, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})
