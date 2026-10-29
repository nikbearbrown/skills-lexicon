#!/usr/bin/env python3
"""Independent review of packets p040-p042. Writes answers/p040.json .. p042.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Claim-level overrides: key -> {claim: (verdict, note)}. Anything not listed is "supports" with no note.
CLAIMS = {
    # p040
    "quantum-merlin-arthur": {"definition": ("supports", "Strictly the quantum analogue of MA (bounded-error, polynomial-size proof); 'quantum NP' is the usual gloss")},
    "quicktime-vr": {"definition": ("supports", "Discontinued; QuickTime X dropped QTVR playback")},
    "qumu": {"definition": ("supports", "Qumu was acquired by Enghouse Systems in 2023")},
    "readyapi": {"definition": ("supports", "Core is functional, security and load testing plus virtualization; monitoring was mainly via AlertSite")},
    "quartile": {"definition": ("supports", "The word can also name each of the four groups themselves")},
    # p041
    "requirejs": {"definition": ("supports", "Legacy; largely superseded by ES modules and bundlers")},
    "resorcerer": {"definition": ("supports", "Made by Mathemaesthetics; obsolete with classic Mac OS")},
    "rethinkdb": {"definition": ("supports", "Company shut down in 2016; now community-maintained under the Linux Foundation")},
    "right-to-financial-privacy-act": {"definition": ("supports", "Applies to federal government authorities only, not state or local agencies")},
    "rightnow-crm": {"definition": ("supports", "Deal announced Oct 2011, closed Jan 2012; now Oracle B2C Service")},
    "reporting": {"definition": ("supports", "True but very generic")},
    # p042
    "risa-3d": {"definition": ("supports", "RISA has been part of Nemetschek since 2022")},
    "robomongo": {"definition": ("supports", "Robo 3T was later folded into Studio 3T Free")},
    "rsa-archer": {"definition": ("supports", "Sold by RSA to Cinven in 2023; now branded simply Archer")},
    "salesforce-datorama": {"definition": ("supports", "Renamed Marketing Cloud Intelligence in 2021")},
    "salesforce-social-studio": {"definition": ("supports", "Retired by Salesforce in November 2023")},
    "sage-mas-90": {"definition": ("supports", "Originally from State of the Art Inc., which Sage bought in 1998")},
    "sailing-instruction": {"definition": ("supports", "True but uninformative")},
    "sap-fiori": {"kind": ("supports", "A design system/UX; SAPUI5 is the underlying code framework")},
}

# Bad variants: key -> {label: note}. Every other variant is judged ok.
BAD_VARIANTS = {
    # p040
    "quantum-merlin-arthur": {"QMA": "QMA also names a quick-lock RF coaxial connector type"},
    "rally-software": {"Rally Softwares": "Malformed plural of a product name"},
    "real-estate": {"Real Estates": "Non-standard plural of a mass noun"},
    "real-estate-owned": {"REO": "REO also means rare-earth oxide"},
    "recruitment-consulting": {"Recruiment Consultancy": "Misspelling of Recruitment"},
    # p041
    "refrigeration-compressors": {"Refrigeration Compressors|": "Stray pipe character; data artefact"},
    "registered-education-savings-plan": {
        "Registered Education Savings Planning": "Not a name used for the plan; malformed",
        "RESP": "RESP also names the Redis Serialization Protocol; 'Resp' also respiratory",
    },
    "relational-database-management-system": {"Relational Database Management System (RDMS)": "Acronym misspelled; the short form is RDBMS"},
    "reporting": {"Reportng": "Misspelling"},
    "rhinoceros-3d": {"Rhino": "Rhino also names Mozilla's JavaScript engine and other products"},
    "right-to-financial-privacy-act": {"RFPA": "RFPA is widely used for RF power amplifier"},
    # p042
    "risk-adjustment-coding": {"Risk Adjustment Coding (RAC)": "RAC in US healthcare means Recovery Audit Contractor; not a standard short form here"},
    "sap-adaptive-server-enterprise": {"Sybase (Software)": "Sybase is the former company; also IQ, SQL Anywhere, PowerBuilder"},
    "sap-gui": {"SAP GUIing": "Not a real form; malformed"},
}

# Bad relations: key -> {rel: note}. Every other relation is judged ok.
BAD_RELATIONS = {}

# Votes: key -> (answer, reason). Unlisted keys get "yes".
VOTES = {
    # p040
    "quantitative-models-of-the-action-potential": ("unsure", "Niche academic topic; at most named in computational neuroscience research posts"),
    "quantum-merlin-arthur": ("no", "Theoretical complexity class, not something listings ask for"),
    "quantum-spin-hall-effect": ("no", "Condensed-matter physics phenomenon, not a job requirement"),
    "quartile": ("no", "Basic statistics term; listings ask for statistics, not quartiles"),
    "quicktime-vr": ("no", "Obsolete Apple technology, discontinued"),
    "qumu": ("unsure", "Niche enterprise video product; rarely named in listings"),
    "random-testing": ("unsure", "Usually requested as fuzzing or property-based testing instead"),
    "random-variable": ("no", "Basic probability concept, not a job requirement"),
    "rankine-cycle": ("unsure", "Thermodynamics concept; only occasionally named for power-plant roles"),
    "reduction-complexity": ("no", "Theoretical computer science concept"),
    "reference-range": ("unsure", "Lab knowledge assumed by roles but rarely named as a requirement"),
    # p041
    "resorcerer": ("no", "Obsolete classic Mac OS tool"),
    "responsive-teaching": ("unsure", "Listings mostly say 'culturally responsive teaching', a distinct concept"),
    "rethinkdb": ("unsure", "Database largely abandoned commercially; rarely requested"),
    "ribosomal-intergenic-spacer-analysis": ("no", "Niche lab technique, rarely if ever named in listings"),
    "rights-issue": ("unsure", "Finance concept; named only in some corporate-actions or ECM roles"),
    "riot-js": ("unsure", "Very niche UI library; rarely requested"),
    # p042
    "robomongo": ("unsure", "Minor MongoDB GUI client; occasionally listed"),
    "rockmelt": ("no", "Defunct browser, discontinued 2013-14"),
    "routing-table-maintenance-protocol": ("no", "Obsolete AppleTalk protocol"),
    "rubber-tyred-metro": ("no", "A kind of transit system, not a skill"),
    "sales-journal": ("unsure", "Bookkeeping concept, rarely named on its own"),
    "salesforce-social-studio": ("unsure", "Product retired in 2023; only in older listings"),
}


def review(entry):
    key = entry["key"]
    out = {"key": key, "claims": {}}
    over = CLAIMS.get(key, {})
    for claim in ("definition", "kind", "certification", "certification_scope", "language_type"):
        if claim not in entry:
            continue
        verdict, note = over.get(claim, ("supports", None))
        c = {"verdict": verdict}
        if note:
            c["note"] = note[:150]
        out["claims"][claim] = c
    if entry.get("variants"):
        bad = BAD_VARIANTS.get(key, {})
        out["variants"] = {
            "ok": [v for v in entry["variants"] if v not in bad],
            "bad": [{"label": v, "note": bad[v][:150]} for v in entry["variants"] if v in bad],
        }
        missing = set(bad) - set(entry["variants"])
        assert not missing, (key, missing)
    if entry.get("relations"):
        badr = BAD_RELATIONS.get(key, {})
        out["relations"] = {
            "ok": [r for r in entry["relations"] if r not in badr],
            "bad": [{"rel": r, "note": badr[r][:150]} for r in entry["relations"] if r in badr],
        }
    ans, reason = VOTES.get(key, ("yes", None))
    v = {"answer": ans}
    if reason:
        v["reason"] = reason[:150]
    out["job_listing_vote"] = v
    return out


def main():
    all_keys = set()
    for p in ("p040", "p041", "p042"):
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            packet = json.load(f)
        answers = [review(e) for e in packet["entries"]]
        all_keys |= {e["key"] for e in packet["entries"]}
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(answers, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        bad_v = 0
        for a in answers:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
            bad_v += len(a.get("variants", {}).get("bad", []))
        print(p, len(answers), cnt, votes, "bad variants:", bad_v)
    for d in (CLAIMS, BAD_VARIANTS, BAD_RELATIONS, VOTES):
        stray = set(d) - all_keys
        assert not stray, stray


if __name__ == "__main__":
    main()
