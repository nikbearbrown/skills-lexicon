"""Build reviewer answers for packets p004-p006 from per-entry overrides.

Default for every claim is `supports`, every variant/relation ok, vote yes;
OVR lists the deviations and notes decided during review.
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
CLAIMS = ["definition", "kind", "certification", "certification_scope", "language_type"]

RETIRED = "Retired CompTIA certification."

# key -> {"claims": {claim: (verdict, note)}, "bad_var": {label: note},
#         "bad_rel": {rel: note}, "vote": (answer, reason)}
OVR = {
    # ---------------- p004 ----------------
    "certified-patient-care-technician": {
        "claims": {"definition": ("supports", "Usually NHA's CPCT/A credential.")},
        "bad_var": {"Certified Patient Care Technician/Associate/Nurse Technician":
                    "Garbled job-title string, not a name of this credential."},
    },
    "certified-physician-practice-manager": {
        "bad_var": {"CPPM": "Also Aruba ClearPass Policy Manager (CPPM) in networking listings."},
    },
    "certified-professional-in-healthcare-quality": {
        "claims": {"definition": ("supports", "Awarded by NAHQ.")},
    },
    "certified-professional-medical-services-management": {
        "claims": {"definition": ("supports", "Awarded by NAMSS.")},
    },
    "certified-public-housing-manager": {
        "claims": {"definition": ("supports", "Usually NAHRO's PHM."),
                   "certification_scope": ("unsure", "NAHRO's PHM is best known, but Nan McKay also certifies Public Housing Managers.")},
    },
    "certified-radiology-nurse": {
        "claims": {"definition": ("supports", "CRN, awarded by the Radiologic Nursing Certification Board.")},
    },
    "certified-rhythm-analysis-technician": {
        "claims": {"definition": ("supports", "CRAT, awarded by Cardiovascular Credentialing International.")},
    },
    "certified-software-test-engineer": {
        "bad_var": {"CSTE": "Also Council of State and Territorial Epidemiologists."},
    },
    "certified-technical-trainer": {
        "claims": {"definition": ("supports", "Usually CompTIA CTT+.")},
    },
    "certified-teststand-developer": {
        "claims": {"definition": ("supports", "NI is now part of Emerson.")},
        "bad_var": {"CTD": "Also Common Technical Document, cumulative trauma disorder, CTD ocean sensor."},
    },
    "certified-urologic-physician-assistant": {
        "bad_var": {"CUPA": "Also CUPA-HR and California's Certified Unified Program Agency."},
    },
    "certified-wine-educator": {
        "bad_var": {"CWE": "Also Common Weakness Enumeration in security listings."},
    },
    "certified-wound-and-ostomy-care-nurse": {
        "claims": {"definition": ("supports", "WOCNCB's CWON (Certified Wound Ostomy Nurse).")},
    },
    # ---------------- p005 ----------------
    "change-management-certified-professional": {
        "claims": {"definition": ("supports", "Generic; issuer not named (cf. ACMP's CCMP, Prosci).")},
    },
    "chartered-fellow-of-the-chartered-institute-of-personnel-and-development": {
        "claims": {"definition": ("supports", "Highest earned grade; Companion is an honorary grade.")},
    },
    "citrix-certified-administrator": {
        "claims": {"definition": ("supports", "Legacy name; replaced c.2013 by Citrix Certified Associate (CCA-V/CCA-N).")},
    },
    "citrix-certified-integration-architect": {
        "claims": {"definition": ("supports", "Legacy Citrix credential, retired.")},
        "bad_var": {"Citrix Certified Integratrion Architecture": "Misspelling, not a name form."},
    },
    "combat-lifesaver": {
        "claims": {"definition": ("supports", "Now taught as TCCC Combat Lifesaver.")},
    },
    "comptia-advanced-security-practitioner-casp": {
        "claims": {"definition": ("supports", "Renamed CompTIA SecurityX in late 2024.")},
    },
    "comptia-cdia": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-convergence-technologies-professional-ctp": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-digital-home-technology-integrator-dhti": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-e-biz": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-green-it-specialist": {"claims": {"definition": ("supports", "Retired; sold as CompTIA Strata Green IT.")}},
    "comptia-healthcare-it-technician": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-hti": {"claims": {"definition": ("supports", "Retired; predecessor of DHTI+.")}},
    "comptia-i-net": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-instructor": {
        "claims": {"definition": ("unsure", "I know no CompTIA 'Instructor+'; CompTIA's trainer credential is CTT+.")},
        "vote": ("unsure", "Cannot confirm this credential exists."),
    },
    "comptia-it-for-sales": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-it-fundamentals": {
        "claims": {"definition": ("supports", "Replaced by CompTIA Tech+ in 2024.")},
    },
    "comptia-mobile-app-security": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-printing-and-document-imaging-pdi": {"claims": {"definition": ("supports", RETIRED)}},
    "comptia-rfid": {"claims": {"definition": ("supports", RETIRED)}},
    # ---------------- p006 ----------------
    "comptia-storage": {"claims": {"definition": ("supports", RETIRED)}},
    "cpr-for-the-professional-rescuer": {
        "claims": {"definition": ("supports", "Red Cross now names it CPR/AED for Professional Rescuers.")},
    },
    "doctor-of-dental-medicine": {
        "bad_var": {"DMD": "Also Duchenne muscular dystrophy."},
    },
    "doctor-of-dental-surgery": {
        "bad_var": {"DDS": "Also Data Distribution Service and Disability Determination Services."},
    },
    "doctor-of-medicine": {
        "claims": {"definition": ("supports", "In the UK and Commonwealth MD is usually a research doctorate.")},
    },
    "doctor-of-veterinary-medicine": {
        "bad_var": {"DVM": "Also digital voltmeter in electronics listings.",
                    "VMD": "Also the UK Veterinary Medicines Directorate."},
    },
    "enhanced-security-check-esc-clearance": {
        "bad_var": {"eSC": "Case-insensitively ESC: European Society of Cardiology, electronic stability control."},
    },
    "gerontological-nurse-practitioner": {
        "claims": {"definition": ("supports", "ANCC retired GNP-BC in 2015 for adult-gerontology NP certs."),
                   "certification_scope": ("unsure", "Standalone GNP-BC was ANCC only; successor AG-NP certs come from ANCC and AANPCB.")},
    },
}


def judge(entry):
    o = OVR.get(entry["key"], {})
    claims = {}
    for c in CLAIMS:
        if c not in entry:
            continue
        verdict, note = o.get("claims", {}).get(c, ("supports", None))
        claims[c] = {"verdict": verdict}
        if note:
            claims[c]["note"] = note
    ans = {"key": entry["key"], "claims": claims}
    bad_var = o.get("bad_var", {})
    for label in bad_var:
        assert label in entry["variants"], (entry["key"], label)
    ans["variants"] = {
        "ok": [v for v in entry["variants"] if v not in bad_var],
        "bad": [{"label": v, "note": n} for v, n in bad_var.items()],
    }
    bad_rel = o.get("bad_rel", {})
    ans["relations"] = {
        "ok": [r for r in entry["relations"] if r not in bad_rel],
        "bad": [{"rel": r, "note": n} for r, n in bad_rel.items()],
    }
    answer, reason = o.get("vote", ("yes", None))
    ans["job_listing_vote"] = {"answer": answer}
    if reason:
        ans["job_listing_vote"]["reason"] = reason
    return ans


def main():
    seen = set()
    for p in ("p004", "p005", "p006"):
        with open(os.path.join(BASE, "packets", p + ".json")) as f:
            entries = json.load(f)["entries"]
        out = [judge(e) for e in entries]
        seen.update(e["key"] for e in entries)
        for a in out:
            for c in a["claims"].values():
                assert len(c.get("note", "")) <= 150
                assert c["verdict"] != "contradicts" or c.get("note")
        with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        nbad = 0
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
            nbad += len(a["variants"]["bad"]) + len(a["relations"]["bad"])
        print(p, len(out), cnt, votes, "bad variants/relations:", nbad)
    missing = set(OVR) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
