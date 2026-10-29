"""Scratch helper: builds answers in the draft-entry shape and writes them to work/responses/."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REQ, RESP = HERE / "requests", HERE / "responses"
RESP.mkdir(exist_ok=True)
GK = "general-knowledge"
DONE = []


def _req(stem):
    p = REQ / f"{stem}.json"
    if not p.exists():
        raise SystemExit(f"no request {stem}")
    return json.loads(p.read_text("utf-8"))


def _write(stem, resp):
    (RESP / f"{stem}.json").write_text(json.dumps(resp, indent=1, ensure_ascii=False) + "\n", "utf-8")
    DONE.append(stem)


def ns(stem, reason):
    _req(stem)
    _write(stem, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})


def un(stem, reason):
    _req(stem)
    _write(stem, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})


def vo(stem, tid, reason):
    r = _req(stem)
    assert tid in {n["id"] for n in r["nearest"]}, (stem, tid)
    _write(stem, {"decision": "variant_of", "variant_of": tid, "reason": reason, "entry": None})


def new(stem, name, kind, definition, variants=(), relations=(), verbs=(), cert=False, scope=None, lang=None,
        reason=None, note=""):
    r = _req(stem)
    assert kind in r["allowed"]["kinds"], (stem, kind)
    ids = {n["id"] for n in r["nearest"]}
    rels = []
    for t, tid in relations:
        assert t in r["allowed"]["relation_types"] and tid in ids, (stem, t, tid)
        rels.append({"type": t, "target": tid, "basis": GK})
    assert lang in (None, "human", "programming"), (stem, lang)
    if lang == "human":
        assert kind == "human-language", stem
    if lang == "programming":
        assert kind in ("programming-language", "markup-language", "style-language", "modeling-language"), stem
    if kind.endswith("language"):
        assert lang, stem
    if cert:
        assert scope in ("single-issuer", "many-issuers"), stem
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": rels,
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": bool(cert), "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        entry["certification_scope"] = {"value": scope, "basis": GK}
    _write(stem, {"decision": "new", "variant_of": None,
                  "reason": reason or "A recognised skill, tool, method, language or credential.", "entry": entry})
