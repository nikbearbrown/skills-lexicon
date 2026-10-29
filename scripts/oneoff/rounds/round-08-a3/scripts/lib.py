import json, os, sys
GK = "general-knowledge"

def N(name, kind, definition, reason, variants=(), rels=(), verbs=(), cert=False, scope=None, lang=None, note=""):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": g, "basis": GK} for t, g in rels],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        assert scope in ("single-issuer", "many-issuers")
        e["certification_scope"] = {"value": scope, "basis": GK}
    else:
        assert scope is None
    return {"decision": "new", "variant_of": None, "reason": reason, "entry": e}

def NS(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def U(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def AAS(field, phrase, rels=()):
    name = "Associate of Applied Science in " + field
    d = ("An applied associate degree, typically two years of study and awarded by a college, with a major in "
         + phrase + ".")
    return N(name, "credential", d, "A degree, which is a credential awarded by many colleges.",
             variants=["AAS in " + field], rels=rels, cert=True, scope="many-issuers")

def write_all(answers, only_terms=None):
    reqdir = "work/requests"; outdir = "work/responses"
    os.makedirs(outdir, exist_ok=True)
    by_term = {}
    for f in sorted(os.listdir(reqdir)):
        r = json.load(open(os.path.join(reqdir, f)))
        by_term[r["term"]] = (f, r)
    n = 0
    for term, ans in answers.items():
        assert term in by_term, "unknown term " + repr(term)
        f, r = by_term[term]
        ids = {x["id"] for x in r["nearest"]}
        if ans["entry"]:
            for rel in ans["entry"]["relations"]:
                assert rel["target"] in ids, (term, rel)
        json.dump(ans, open(os.path.join(outdir, f), "w"), ensure_ascii=False, indent=1)
        n += 1
    return n
