import json, glob, os
ROOT = "/home/user/rounds/round-07/a4/skills-lexicon"
GK = "general-knowledge"

def requests():
    out = {}
    for f in sorted(glob.glob(ROOT + "/work/requests/*.json")):
        d = json.load(open(f))
        out[d["term"]] = (os.path.basename(f), d)
    return out

def V(label):
    return {"label": label, "basis": GK}

def R(type_, target):
    return {"type": type_, "target": target, "basis": GK}

def VB(verb):
    return {"verb": verb, "basis": GK}

def new(name, kind, definition, variants=(), relations=(), verbs=(), cert=False, scope=None, lang=None, reason="", note=""):
    e = {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
         "variants": [V(v) for v in variants], "relations": list(relations),
         "verbs": [VB(v) for v in verbs],
         "certification": {"value": cert, "basis": GK}}
    if cert:
        assert scope in ("single-issuer", "many-issuers")
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    if note:
        e["annotation_note"] = note
    return {"decision": "new", "variant_of": None, "reason": reason or "A real skill, tool, credential or field with no matching entry in nearest.", "entry": e}

def na(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def variant(target, reason):
    return {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def write(slice_terms, answers):
    reqs = requests()
    missing = [t for t in slice_terms if t not in answers]
    extra = [t for t in answers if t not in slice_terms]
    assert not missing and not extra, (missing, extra)
    os.makedirs(ROOT + "/work/responses", exist_ok=True)
    for t in slice_terms:
        fname, req = reqs[t]
        a = answers[t]
        if a["decision"] == "variant_of":
            assert a["variant_of"] in {n["id"] for n in req["nearest"]}, t
        if a["decision"] == "new":
            for r in a["entry"]["relations"]:
                assert r["target"] in {n["id"] for n in req["nearest"]}, (t, r)
        json.dump(a, open(ROOT + "/work/responses/" + fname, "w"), indent=1, ensure_ascii=False)
    print("wrote", len(slice_terms))

def slice_terms(lo, hi):
    reqs = requests()
    files = sorted(glob.glob(ROOT + "/work/requests/*.json"))
    return [json.load(open(f))["term"] for f in files][lo:hi]
