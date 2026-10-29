"""Reviewer answers for packets p013-p015 of the skills lexicon."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

S = "supports"
C = "contradicts"
U = "unsure"

# Overrides per key. Anything not listed: definition/kind/certification supports,
# every variant ok, every relation ok, vote yes.
OV = {
    # ---------------- p013 ----------------
    "email-service-providers": {
        "definition": (S, "Marketing sense; 'email service provider' can also mean mailbox providers such as Gmail."),
    },
    "emission-calculations": {
        "bad_variants": {"Emission Calcuations": "Misspelling of 'Calculations'."},
    },
    "endovascular-aneurysm-repair": {
        "bad_variants": {"EndoVasculars Aneurysm Repair": "Malformed/misspelled form ('Endovasculars')."},
    },
    "endpoint-detection-and-response": {
        "bad_variants": {"EDR": "Also means event data recorder (vehicles), Bluetooth Enhanced Data Rate and EDR environmental database reports."},
    },
    "engineered-materials-arrestor-system": {
        "definition": (S, "Classic beds are crushable cellular concrete; newer ones use foamed silica (glass)."),
        "vote": (U, "A physical airport safety system; only niche airport engineering/operations listings mention it."),
    },
    # ---------------- p014 ----------------
    "engineering-statics": {
        "definition": (S, "Strictly bodies in equilibrium (at rest or moving at constant velocity)."),
    },
    "enterprise-performance-management": {
        "bad_variants": {"EPM": "Also Enterprise Project Management (e.g. Microsoft Project Server EPM)."},
    },
    "enterprisedb": {
        "definition": (S, "EnterpriseDB is mainly the company; its product is EDB Postgres Advanced Server."),
    },
    "enzyme-analysis": {
        "bad_variants": {"Enzyme Aanlysis": "Misspelling of 'Analysis'."},
    },
    "erikson-s-stages-of-psychosocial-development": {
        "vote": (U, "Developmental theory; listings usually ask for child development knowledge in general, rarely this theory."),
    },
    "estate-valuation": {
        "definition": (S, "Also used for valuing landed or real-estate property, especially in UK usage."),
    },
    "etiology": {
        "vote": (U, "General medical concept; seldom a stated requirement on its own."),
    },
    # ---------------- p015 ----------------
    "excess-return": {
        "vote": (U, "Finance metric; listings cite it as a goal (generate excess returns) more than a skill."),
    },
    "expectancy-theory": {
        "vote": (U, "Motivation theory taught in management courses; rarely named in job listings."),
    },
    "extended-parallel-process-model": {
        "bad_variants": {"EPPM": "Also Oracle Primavera EPPM (Enterprise Project Portfolio Management), common in listings."},
        "vote": (U, "Niche health-communication theory; at most in public-health research listings."),
    },
    "extended-reality": {
        "bad_variants": {"XR": "Also the X-ray modality abbreviation in radiology (and iPhone XR)."},
    },
    "extended-validation-certificate": {
        "vote": (U, "Narrow PKI concept; rarely a stated requirement."),
    },
    "extensive-reading": {
        "vote": (U, "Language-teaching approach; appears only occasionally in ESL/EFL teacher listings."),
    },
    "extract-transform-load": {
        "bad_variants": {"ETL": "Also Intertek's ETL safety listing mark (UL/ETL) in product-compliance listings."},
    },
    "failure-mode-and-effects-analysis": {
        "definition": (S, "Ratings usually also include detectability (risk priority number)."),
    },
    "fair-employment-and-housing-act": {
        "definition": (S, "Accurate; the FEHA/FEMA remark is editorial rather than definition."),
        "kind": (S, "A statute; 'standard' is the nearest allowed kind."),
        "bad_variants": {"Fair Employment And Housing Act (FEMA)": "FEMA is the Federal Emergency Management Agency; the act is FEHA."},
    },
    "fast-esp": {
        "definition": (S, "Microsoft bought FAST in 2008; ESP has since been discontinued."),
    },
    "fibre-channel": {
        "kind": (S, "Could equally be 'standard' (INCITS T11 protocol family)."),
        "bad_variants": {"Fiber Channel": "Misspelling; the standard's official name is 'Fibre Channel' even in US usage."},
    },
}


def claim(v):
    verdict, note = v if isinstance(v, tuple) else (v, None)
    out = {"verdict": verdict}
    if note:
        assert len(note) <= 150, note
        out["note"] = note
    return out


def review(entry):
    key = entry["key"]
    ov = OV.get(key, {})
    claims = {}
    for c in ("definition", "kind", "certification", "certification_scope", "language_type"):
        if c in entry:
            claims[c] = claim(ov.get(c, S))
    bad_v = ov.get("bad_variants", {})
    for b in bad_v:
        assert b in entry["variants"], (key, b)
    variants = {
        "ok": [v for v in entry["variants"] if v not in bad_v],
        "bad": [{"label": k, "note": n} for k, n in bad_v.items()],
    }
    bad_r = ov.get("bad_relations", {})
    relations = {
        "ok": [r for r in entry["relations"] if r not in bad_r],
        "bad": [{"rel": k, "note": n} for k, n in bad_r.items()],
    }
    ans, reason = ov.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        assert len(reason) <= 150, reason
        vote["reason"] = reason
    return {"key": key, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


def main():
    used = set()
    for p in ("p013", "p014", "p015"):
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            entries = json.load(f)["entries"]
        out = [review(e) for e in entries]
        used.update(e["key"] for e in entries)
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        print(p, len(out), "entries", cnt, votes,
              "bad variants:", sum(len(a["variants"]["bad"]) for a in out))
    missing = set(OV) - used
    assert not missing, missing


if __name__ == "__main__":
    main()
