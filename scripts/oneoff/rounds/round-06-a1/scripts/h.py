import json, os
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
REQ = ROOT / "work" / "requests"
RESP = ROOT / "work" / "responses"
GK = "general-knowledge"
FILES = sorted(os.listdir(REQ))
KINDS = {"ability","credential","framework","human-language","knowledge","library","markup-language","method",
         "modeling-language","platform","programming-language","skill","standard","style-language","tool","work-activity"}

def _req(i):
    return json.load(open(REQ / FILES[i]))

def ns(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def vo(target, reason):
    return {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def new(name, kind, definition, variants=(), rel=(), verbs=(), cert=False, scope=None, lang=None, reason="", note=""):
    assert kind in KINDS, kind
    assert definition.strip() and "\n" not in definition
    e = {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
         "variants": [{"label": v, "basis": GK} for v in variants],
         "relations": [{"type": t, "target": i, "basis": GK} for (t, i) in rel],
         "verbs": [{"verb": v, "basis": GK} for v in verbs],
         "certification": {"value": cert, "basis": GK},
         "language_type": {"value": lang, "basis": GK},
         "annotation_note": note}
    if cert:
        assert scope in ("single-issuer", "many-issuers")
        e["certification_scope"] = {"value": scope, "basis": GK}
    else:
        assert scope is None
    if lang:
        assert kind.endswith("-language")
    if kind.endswith("-language"):
        assert lang
    if kind == "credential":
        assert cert
    return {"decision": "new", "variant_of": None, "reason": reason or "A named skill, tool or concept with no match in nearest.", "entry": e}

def write_all(answers):
    for i, (term, resp) in answers.items():
        r = _req(i)
        assert r["term"] == term, (i, r["term"], term)
        near = {x["id"] for x in r["nearest"]}
        if resp["decision"] == "variant_of":
            assert resp["variant_of"] in near, (i, term)
        if resp["decision"] == "new":
            for rl in resp["entry"]["relations"]:
                assert rl["target"] in near, (i, term, rl)
        (RESP / FILES[i]).write_text(json.dumps(resp, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print("wrote", len(answers))
