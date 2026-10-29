import json, glob, os

ROOT = "/home/user/rounds/round-07/a3/skills-lexicon"
FILES = sorted(glob.glob(ROOT + "/work/requests/*.json"))
GK = "general-knowledge"
OUT = ROOT + "/work/responses"


def _write(idx, term, resp):
    path = FILES[idx]
    req = json.load(open(path))
    assert req["term"] == term, (idx, req["term"], term)
    json.dump(resp, open(os.path.join(OUT, os.path.basename(path)), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(OUT, os.path.basename(path)), "a").write("\n")


def new(idx, term, name, kind, definition, variants=(), relations=(), cert=False, scope=None,
        lang=None, note="", reason=None):
    ent = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [],
        "certification": {"value": bool(cert), "basis": GK},
    }
    if cert:
        assert scope in ("single-issuer", "many-issuers")
        ent["certification_scope"] = {"value": scope, "basis": GK}
    ent["language_type"] = {"value": lang, "basis": GK}
    ent["annotation_note"] = note
    resp = {"decision": "new", "variant_of": None, "reason": reason or "A recognised skill, tool, method or credential that no nearest entry covers.",
            "entry": ent}
    _write(idx, term, resp)


def no(idx, term, reason):
    _write(idx, term, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})


def unsure(idx, term, reason):
    _write(idx, term, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})


def variant(idx, term, target, reason):
    _write(idx, term, {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None})
