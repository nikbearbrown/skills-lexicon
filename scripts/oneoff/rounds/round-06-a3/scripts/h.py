import json, os, glob
ROOT = "/home/user/rounds/round-06/a3/skills-lexicon/work"
GK = "general-knowledge"
CERT_KINDS = {"credential"}

def _req(stem):
    p = f"{ROOT}/requests/{stem}.json"
    assert os.path.exists(p), stem
    return json.load(open(p))

def _write(stem, resp):
    os.makedirs(f"{ROOT}/responses", exist_ok=True)
    with open(f"{ROOT}/responses/{stem}.json", "w") as f:
        json.dump(resp, f, indent=1, ensure_ascii=False)
        f.write("\n")

def N(stem, name, kind, defn, variants=(), rel=(), cert=False, scope=None, lang=None, note="", reason=None):
    req = _req(stem)
    near = {n["id"] for n in req["nearest"]}
    assert kind in req["allowed"]["kinds"], (stem, kind)
    if cert:
        assert scope in ("single-issuer", "many-issuers"), stem
    else:
        assert scope is None, stem
    assert defn.endswith("."), (stem, defn)
    relations = []
    for t, tgt in rel:
        assert t in req["allowed"]["relation_types"], (stem, t)
        assert tgt in near, (stem, tgt)
        relations.append({"type": t, "target": tgt, "basis": GK})
    e = {
        "preferred_name": name, "kind": kind, "definition": defn, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": relations,
        "verbs": [],
        "certification": {"value": bool(cert), "basis": GK},
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    e["annotation_note"] = note
    _write(stem, {"decision": "new", "variant_of": None,
                  "reason": reason or f"{req['term']} is a recognised {kind} that no nearest entry covers.",
                  "entry": e})

def NS(stem, reason):
    _req(stem)
    _write(stem, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})

def U(stem, reason):
    _req(stem)
    _write(stem, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})
