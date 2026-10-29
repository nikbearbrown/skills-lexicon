import json, os
GK = "general-knowledge"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "responses")
REQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "requests")

def nas(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def variant(target, reason):
    return {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def new(name, kind, definition, variants=(), rels=(), cert=False, scope=None, lang=None, note="", reason=None):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": g, "basis": GK} for t, g in rels],
        "verbs": [],
        "certification": {"value": bool(cert), "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    return {"decision": "new", "variant_of": None, "reason": reason or "A recognised skill, tool or concept that none of the nearest entries covers.", "entry": e}

def write(answers):
    for stem, ans in answers.items():
        assert os.path.exists(os.path.join(REQ, stem + ".json")), stem
        if ans["decision"] == "new":
            e = ans["entry"]
            assert e["certification"]["value"] is False or e.get("certification_scope", {}).get("value") in ("single-issuer", "many-issuers"), stem
        with open(os.path.join(OUT, stem + ".json"), "w", encoding="utf-8") as f:
            json.dump(ans, f, indent=1, ensure_ascii=False)
            f.write("\n")
    print("wrote", len(answers))
