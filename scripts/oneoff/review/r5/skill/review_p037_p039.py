#!/usr/bin/env python3
"""Independent review of packets p037-p039; writes answers/p037.json .. p039.json."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

S = {"verdict": "supports"}


def sup(note=None):
    d = {"verdict": "supports"}
    if note:
        d["note"] = note
    return d


def con(note):
    return {"verdict": "contradicts", "note": note}


def uns(note=None):
    d = {"verdict": "unsure"}
    if note:
        d["note"] = note
    return d


# Per-entry overrides. Anything not listed: definition/kind/certification supports,
# all variants ok, all relations ok, vote yes.
# fields: d=definition, k=kind, c=certification, bad={variant: note}, badrel={rel: note}, vote=(answer, reason)
R = {
    # ---------------- p037 ----------------
    "phpwebsite": {"d": sup("Appalachian State University project; long discontinued")},
    "pivotal-tracker": {"d": sup("Shut down by Broadcom in April 2025")},
    "pixijs": {"d": sup("v8 also renders with WebGPU")},
    "plant-design-management-system": {"d": sup("Originally CADCentre's; largely succeeded by AVEVA E3D")},
    "platform-as-a-service": {"bad": {"Platform As A Services": "Garbled plural; not a real form of the term"}},
    "polycom": {"d": sup("Poly was formed from Plantronics + Polycom in 2018-19 and is now part of HP")},
    "positive-airway-pressure": {"bad": {"Positive Airway Pressure (CPAB/BiPAP)": "Misspells CPAP as 'CPAB'"}},
    "point-to-point-tunneling-protocol": {"d": sup("Now considered insecure and deprecated")},
    "postorder-traversal": {"vote": ("unsure", "Granular textbook algorithm concept; listings ask for data structures/algorithms, rarely this traversal")},
    # ---------------- p038 ----------------
    "predictive-analytics-software": {"bad": {"Predictive Analytics Softwares": "'Softwares' is a nonstandard plural"}},
    "prestodb": {"d": sup("Presto Foundation under the Linux Foundation since 2019; Trino is the separate fork")},
    "price-to-book-ratio": {"vote": ("unsure", "A single valuation metric; finance listings rarely ask for it by name")},
    "prince2": {"c": sup("The method itself is not a credential; PRINCE2 Foundation/Practitioner (PeopleCert/AXELOS) are")},
    "process-hazard-analysis": {"bad": {"Process Hazard Anlysis": "Misspelling of 'Analysis'"}},
    "process-state": {"vote": ("unsure", "Single OS textbook concept; not normally a job requirement")},
    "processing-js": {"d": sup("Processing is a text language for visual arts, not a 'visual programming language'; project archived 2018")},
    # ---------------- p039 ----------------
    "programmatic-media-buying": {"d": sup("Also covers non-auction deals such as programmatic guaranteed and private marketplaces")},
    "programmer-s-hierarchical-interactive-graphics-system": {"d": sup("ANSI X3.144-1988, ISO 9592; long obsolete")},
    "prosecutor-s-management-information-system": {"d": sup("Generic; specifically PROMIS, INSLAW's 1970s case-management system for US prosecutors")},
    "protractor": {"d": sup("Deprecated; end of life in 2023")},
    "ptas-reduction": {"vote": ("no", "Theoretical complexity-theory concept, not a job-listing requirement")},
    "pug": {"d": sup("Formerly named Jade")},
    "puphpet": {"d": sup("Project is defunct")},
    "puppeteer": {"d": sup("Now also drives Firefox")},
    "python-server-pages": {"k": uns("PSP is a templating technique with several implementations (mod_python, Webware), not one framework")},
    "qarun": {"d": sup("Discontinued; Compuware's testing tools went to Micro Focus in 2009")},
}


def judge(entry):
    key = entry["key"]
    o = R.get(key, {})
    claims = {}
    if "definition" in entry:
        claims["definition"] = o.get("d", dict(S))
    if "kind" in entry:
        claims["kind"] = o.get("k", dict(S))
    if "certification" in entry:
        claims["certification"] = o.get("c", dict(S))
    for extra in ("certification_scope", "language_type"):
        if extra in entry:
            claims[extra] = o.get(extra, dict(S))
    bad_v = o.get("bad", {})
    variants = {"ok": [v for v in entry.get("variants", []) if v not in bad_v],
                "bad": [{"label": v, "note": n} for v, n in bad_v.items()]}
    for v in bad_v:
        assert v in entry.get("variants", []), (key, v)
    bad_r = o.get("badrel", {})
    relations = {"ok": [r for r in entry.get("relations", []) if r not in bad_r],
                 "bad": [{"rel": r, "note": n} for r, n in bad_r.items()]}
    vote = o.get("vote")
    jv = {"answer": "yes"} if vote is None else {"answer": vote[0], "reason": vote[1]}
    return {"key": key, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": jv}


def main():
    seen = set()
    for p in ("p037", "p038", "p039"):
        with open(os.path.join(BASE, "packets", p + ".json")) as f:
            pk = json.load(f)
        kinds = set(pk["allowed_kinds"])
        out = []
        for e in pk["entries"]:
            assert e["kind"] in kinds, e["key"]
            seen.add(e["key"])
            out.append(judge(e))
        for a in out:
            for c in a["claims"].values():
                if "note" in c:
                    assert len(c["note"]) <= 150, (a["key"], c["note"])
            if "reason" in a["job_listing_vote"]:
                assert len(a["job_listing_vote"]["reason"]) <= 150, a["key"]
        with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        print(p, len(out))
    missing = set(R) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
