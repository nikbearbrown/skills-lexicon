import json, os

REQ = "work/requests"
OUT = "work/responses"
GK = "general-knowledge"
_files = {}
for _f in sorted(os.listdir(REQ)):
    _d = json.load(open(os.path.join(REQ, _f)))
    assert _d["term"] not in _files, _d["term"]
    _files[_d["term"]] = (_f, _d)
os.makedirs(OUT, exist_ok=True)
_done = set()


def _write(term, resp):
    assert term in _files, "unknown term %r" % term
    assert term not in _done, "twice: %r" % term
    _done.add(term)
    f, d = _files[term]
    if resp["decision"] == "variant_of":
        assert resp["variant_of"] in [n["id"] for n in d["nearest"]], term
    if resp.get("entry"):
        for r in resp["entry"]["relations"]:
            assert r["target"] in [n["id"] for n in d["nearest"]], (term, r)
        assert resp["entry"]["kind"] in d["allowed"]["kinds"], (term, resp["entry"]["kind"])
    json.dump(resp, open(os.path.join(OUT, f), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(OUT, f), "a").write("\n")


def N(term, name, kind, defn, var=(), rel=(), verbs=(), cert=False, scope=None, lang=None,
      note="", reason=None):
    e = {
        "preferred_name": name, "kind": kind, "definition": defn, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in var],
        "relations": [{"type": t, "target": x, "basis": GK} for t, x in rel],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": bool(cert), "basis": GK},
    }
    if cert:
        assert scope in ("single-issuer", "many-issuers"), term
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    e["annotation_note"] = note
    _write(term, {"decision": "new", "variant_of": None,
                  "reason": reason or "A recognised concept with no entry in nearest that is the same.",
                  "entry": e})


def V(term, target, reason):
    _write(term, {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None})


def X(term, reason):
    _write(term, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})


def U(term, reason):
    _write(term, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})
