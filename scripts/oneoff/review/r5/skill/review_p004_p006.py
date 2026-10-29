#!/usr/bin/env python3
"""Reviewer answers for packets p004-p006 of the skills lexicon."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
S, C, U = "supports", "contradicts", "unsure"

# Per-entry overrides. Anything not listed: every claim supports, every variant/relation ok, vote yes.
# claims: {claim: (verdict, note)}; badv: {variant: note}; badr: {rel: note}; vote: (answer, reason)
O = {
    # ---------------- p004 ----------------
    "cardiopulmonary-resuscitation": {
        "claims": {"certification": (S, "Entry is the procedure itself; the CPR card listings ask for is a separate credential")},
    },
    "cardiovascular-physiology": {
        "badv": {"CardioVasculars Physiology": "Malformed spelling, not a real form of the name"},
    },
    "casperjs": {
        "claims": {"definition": (S, "Project archived/unmaintained since about 2017")},
    },
    "cdc-cyber": {
        "claims": {"definition": (S, "Line ran through the 1970s and 1980s")},
        "vote": ("no", "Obsolete 1970s-80s hardware line; not requested in current listings"),
    },
    "cebas-finalrender": {
        "claims": {"definition": (S, "Maya (and C4D) versions were early Stage-1 releases; current versions target 3ds Max")},
    },
    "cfwheels": {
        "claims": {"definition": (S, "Project has since been renamed simply Wheels")},
    },
    "chainer": {
        "claims": {"definition": (S, "In maintenance mode since 2019; PFN moved to PyTorch")},
    },
    "chemical-reactions": {
        "vote": ("unsure", "Basic chemistry topic; listings rarely name it as a requirement"),
    },
    "child-nutrition": {
        "badv": {"Child Nutritions": "Ungrammatical plural, not a real form of the term"},
    },
    "children-s-health-insurance-program": {
        "claims": {"definition": (S, "Jointly funded federal-state program created in 1997")},
    },
    # ---------------- p005 ----------------
    "chlorofluorocarbons": {
        "badv": {"CFCs": "Also means controlled foreign corporations in tax listings"},
        "vote": ("unsure", "A chemical class; asked only indirectly via refrigerant handling (EPA 608)"),
    },
    "chromatography-software": {
        "badv": {"Chromatography Softwares": "Nonstandard plural 'softwares'"},
    },
    "chronometer": {
        "vote": ("no", "A timekeeping instrument, not a skill listings ask for"),
    },
    "circulatory-system": {
        "vote": ("unsure", "Anatomy topic; listings ask for anatomy and physiology broadly"),
    },
    "cisco-ucs-director": {
        "claims": {"definition": (S, "Product has reached end of sale/end of life")},
    },
    "clarizen": {
        "claims": {"definition": (S, "Acquired by Planview in 2021, now Planview AdaptiveWork")},
    },
    "clean-air-act": {
        "claims": {"kind": (S, "A statute; standard is the nearest allowed kind")},
    },
    "clean-water-act": {
        "claims": {"kind": (S, "A statute; standard is the nearest allowed kind")},
    },
    "client-access-license": {
        "vote": ("unsure", "Licensing concept; mostly named only in software-licensing roles"),
    },
    "clinical-pastoral-education": {
        "claims": {
            "definition": (S, "ACPE is the main US accreditor; CPSP also certifies"),
            "kind": (U, "A training programme; completed units act as a credential in chaplain listings"),
            "certification": (U, "Units completed at accredited centres are a required qualification, arguably a credential"),
        },
    },
    "cocoonjs": {
        "claims": {"definition": (S, "Later Cocoon.io; discontinued")},
    },
    "cognitive-load": {
        "vote": ("unsure", "Psychology concept; occasionally cited in UX or instructional design"),
    },
    # ---------------- p006 ----------------
    "collaboration-software": {
        "badv": {"Collaborative Softwares": "Nonstandard plural 'softwares'"},
    },
    "collaborative-planning-forecasting-and-replenishment": {
        "badv": {"Collaborative Planning Forecasting SandsReplenishment": "Garbled text ('SandsReplenishment')"},
    },
    "color-rendering-index": {
        "vote": ("unsure", "A lighting metric; mentioned only in niche lighting roles"),
    },
    "common-language-specification": {
        "claims": {"definition": (S, "Part of the ECMA-335 CLI; rules for CLS-compliant interoperable code")},
        "vote": ("unsure", ".NET internals detail; rarely requested by name"),
    },
    "commons-based-peer-production": {
        "vote": ("no", "An economics concept, not a job requirement"),
    },
    "componentone": {
        "claims": {"definition": (S, "Now sold by MESCIUS (formerly GrapeCity)")},
    },
    "composite-pattern": {
        "claims": {"definition": (S, "Objects compose into a tree; the interface is uniform rather than tree-shaped")},
        "vote": ("unsure", "Listings ask for design patterns generally, rarely this one by name"),
    },
    "computer-fraud-and-abuse-act": {
        "claims": {"kind": (S, "A statute; standard is the nearest allowed kind")},
        "vote": ("unsure", "Named only in some cyber-law or compliance listings"),
    },
    "concurrent-engineering": {
        "badv": {"Simultaneous Engineering Wikipedia": "Scraping artifact: includes 'Wikipedia'"},
    },
    "confirmit": {
        "claims": {"definition": (S, "Merged with FocusVision into Forsta in 2021")},
    },
}

CLAIM_KEYS = ["definition", "kind", "certification", "certification_scope", "language_type"]


def judge(entry):
    key = entry["key"]
    o = O.get(key, {})
    claims = {}
    for ck in CLAIM_KEYS:
        if ck in entry:
            verdict, note = o.get("claims", {}).get(ck, (S, None))
            c = {"verdict": verdict}
            if note:
                c["note"] = note
            claims[ck] = c
    badv = o.get("badv", {})
    for v in badv:
        assert v in entry.get("variants", []), (key, v)
    variants = {
        "ok": [v for v in entry.get("variants", []) if v not in badv],
        "bad": [{"label": v, "note": n} for v, n in badv.items()],
    }
    badr = o.get("badr", {})
    relations = {
        "ok": [r for r in entry.get("relations", []) if r not in badr],
        "bad": [{"rel": r, "note": n} for r, n in badr.items()],
    }
    ans, reason = o.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    return {"key": key, "claims": claims, "variants": variants, "relations": relations,
            "job_listing_vote": vote}


def main():
    seen = set()
    for p in ["p004", "p005", "p006"]:
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            pk = json.load(f)
        out = [judge(e) for e in pk["entries"]]
        seen.update(e["key"] for e in pk["entries"])
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        nbv = sum(len(a["variants"]["bad"]) for a in out)
        print(p, len(out), cnt, votes, "bad variants:", nbv)
    missing = set(O) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
