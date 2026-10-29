import json, os, sys
GK = "general-knowledge"
REQ = "work/requests"
RESP = "work/responses"

def V(*labels):
    return [{"label": l, "basis": GK} for l in labels]

def R(typ, target):
    return {"type": typ, "target": target, "basis": GK}

def new(reason, name, kind, definition, variants=(), relations=(), cert=False, scope=None,
        lang=None, note="", verbs=()):
    e = {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
         "variants": V(*variants), "relations": list(relations),
         "verbs": [{"verb": v, "basis": GK} for v in verbs],
         "certification": {"value": bool(cert), "basis": GK}}
    if cert:
        assert scope in ("single-issuer", "many-issuers"), name
        e["certification_scope"] = {"value": scope, "basis": GK}
    else:
        assert scope is None
    e["language_type"] = {"value": lang, "basis": GK}
    e["annotation_note"] = note
    return {"decision": "new", "variant_of": None, "reason": reason, "entry": e}

def nas(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def variant(target, reason):
    return {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def write(answers):
    for stem, resp in answers.items():
        path = os.path.join(REQ, stem + ".json")
        assert os.path.exists(path), "no such request: " + stem
        req = json.load(open(path))
        near = {n.get("id") for n in req["nearest"]}
        if resp["decision"] == "variant_of":
            assert resp["variant_of"] in near, stem
        if resp["decision"] == "new":
            for r in resp["entry"]["relations"]:
                assert r["target"] in near, (stem, r)
            assert resp["entry"]["kind"] in req["allowed"]["kinds"], stem
        with open(os.path.join(RESP, stem + ".json"), "w") as f:
            json.dump(resp, f, indent=1, ensure_ascii=False)
            f.write("\n")
    print("wrote", len(answers))
