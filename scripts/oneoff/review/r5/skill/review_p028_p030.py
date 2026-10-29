"""Reviewer answers for packets p028-p030 of the skills lexicon.

Every claim defaults to `supports`; the tables below record the exceptions
(contradicts / unsure / supports-with-note), bad variants, bad relations and
job-listing votes other than a plain yes.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PACKETS = ["p028", "p029", "p030"]

# key -> {claim: (verdict, note)}  (claims not listed: supports, no note)
CLAIMS = {
    # p028
    "mass-media": {"definition": ("supports", "Mass media are the channels themselves; the 'study of' framing only fits the knowledge kind.")},
    "master-production-records": {"definition": ("supports", "Also called master batch records in GMP manufacturing.")},
    "mcollective": {"definition": ("supports", "Created by R.I. Pienaar, acquired by Puppet Labs in 2010; deprecated and removed from Puppet 6 (2018).")},
    "mean-js": {"definition": ("supports", "Boilerplate/stack built on AngularJS 1.x rather than modern Angular; project now inactive.")},
    "mechanical-seal": {"kind": ("contradicts", "A machine component that workers fit and repair, not a tool they use; knowledge fits better.")},
    "mcafee-personal-firewall-plus": {"definition": ("supports", "Discontinued consumer product, later folded into McAfee security suites.")},
    # p029
    "mep-design-software": {"definition": ("supports", "Revit MEP was merged into a single Revit product in 2017.")},
    "meter-data-management": {"definition": ("supports", "MDM mainly concerns smart electricity meters (also gas and water); 'flow meters' is an odd lead example.")},
    "meter-operation-code-of-practice-agreement": {"definition": ("supports", "Covers GB electricity meter operators; its rules have since been folded into the Retail Energy Code.")},
    "microblaze": {"kind": ("supports", "A soft-processor IP core; tool is acceptable, platform would also fit.")},
    "microsoft-365": {"definition": ("supports", "Renamed from Office 365 in 2020.")},
    "microsoft-digital-image-suite": {"definition": ("supports", "Discontinued in 2007.")},
    "microsoft-hololens": {"definition": ("supports", "HoloLens 2 was discontinued in 2024.")},
    "microsoft-teams-live-events": {"definition": ("supports", "Being retired by Microsoft in favour of Teams town halls.")},
    "microsoft-works": {"definition": ("supports", "Discontinued in 2009.")},
    "microstrategy-office": {"definition": ("supports", "Legacy add-in; replaced by MicroStrategy for Office.")},
    # p030
    "microstrategy-visual-insight": {"definition": ("supports", "Superseded by MicroStrategy dossiers.")},
    "mike-urban": {"definition": ("supports", "Largely superseded by DHI's MIKE+.")},
    "modo": {"definition": ("supports", "Foundry announced the end of Modo development in 2025.")},
    "moment-js": {"definition": ("supports", "In maintenance mode since 2020; its authors recommend newer libraries.")},
    "mongovue": {"definition": ("supports", "No longer maintained.")},
    "molding": {"definition": ("supports", "For metals this is usually called casting, though metal injection moulding exists.")},
}

# key -> {variant label: note}
BAD_VARIANTS = {
    "medical-equipment": {"Medical Equipments": "Ungrammatical plural of an uncountable noun, not an accepted form."},
    "meter-data-management": {"Meter Data Management (Flow Meters)": "Qualifier narrows the concept to flow meters; not a name in use."},
    "microscopic-anatomy": {"Miscroscopic Anatomy": "Misspelling of 'microscopic'."},
    "microsoft-bot-framework": {"Bot Framework": "Generic phrase; can mean any bot framework (Rasa, Botpress, etc.)."},
    "microstrategy-desktop": {"Microstrategy Desktops": "Pluralised product name; not a form in use."},
    "microstrategy-intelligence-server": {"Microstrategy Intelligence Servers": "Pluralised product name; not a form in use."},
    "molisch-s-test": {"Molisch'S Tests": "Malformed capitalisation and plural of the name."},
    "mortgage-electronic-registration-system": {"MERS": "Also and more widely means Middle East respiratory syndrome."},
}

# key -> {relation string: note}
BAD_RELATIONS = {}

# key -> (answer, reason) for votes other than plain yes
VOTES = {
    # p028
    "market-capitalization": ("unsure", "A financial metric; finance listings may mention it but rarely ask for it as a skill."),
    "market-depth": ("unsure", "Trading concept; rarely requested by name outside trading roles."),
    "mass-media": ("unsure", "Broad subject area; listings usually ask for media relations or journalism instead."),
    "mcafee-personal-firewall-plus": ("unsure", "Discontinued consumer product; at most rare mentions in old IT support listings."),
    "media-ethics": ("unsure", "Occasionally in journalism roles; seldom a stated requirement."),
    "media-transfer-protocol": ("unsure", "Low-level device protocol; only niche device or driver roles mention it."),
    "medical-record-formatting": ("unsure", "Niche; listings usually say medical transcription or documentation."),
    # p029
    "metaverse": ("unsure", "A concept and buzzword; only some tech and marketing listings mention it."),
    "microscopic-anatomy": ("unsure", "Academic subject; mainly teaching or histology roles cite it."),
    "microsoft-bookings": ("unsure", "Rarely named in listings; usually covered by Microsoft 365."),
    "microsoft-digital-image-suite": ("no", "Consumer photo software discontinued in 2007; not a listing requirement."),
    "microsoft-forms": ("unsure", "Rarely named in listings; usually covered by Microsoft 365."),
    "microsoft-language-interface-pack": ("no", "A Windows/Office language add-on, not something listings ask for."),
    "microsoft-lists": ("unsure", "Rarely named in listings; usually covered by Microsoft 365 or SharePoint."),
    "microsoft-paint": ("unsure", "Basic bundled utility; rarely asked for."),
    "microsoft-teams-live-events": ("unsure", "Feature being retired; rarely named in listings."),
    "microsoft-transaction-server": ("unsure", "Obsolete since COM+; appears only in old listings."),
    "microsoft-works": ("unsure", "Discontinued in 2009; appears only in old listings."),
    # p030
    "mind-mapping": ("unsure", "Occasionally listed; more a personal note-taking technique."),
    "models-for-life-contingencies": ("unsure", "Actuarial exam topic; listings ask for exams passed, not this by name."),
    "molecular-engineering": ("unsure", "Academic field; mainly research roles cite it."),
    "molisch-s-test": ("no", "Basic teaching-lab test for carbohydrates; not requested in job listings."),
    "monetdb": ("unsure", "Niche research database; rarely named in listings."),
    "mongovue": ("unsure", "Discontinued GUI client; rarely named in listings."),
    "mosaic-art": ("unsure", "Craft skill; few listings outside art or tile-setting roles."),
    "movable-type": ("unsure", "Legacy blogging CMS; appears mainly in older listings."),
}

CLAIM_FIELDS = ["definition", "kind", "certification", "certification_scope", "language_type"]


def verdict(v, note=None):
    out = {"verdict": v}
    if note:
        out["note"] = note
    return out


def review(entry):
    key = entry["key"]
    claims = {}
    for field in CLAIM_FIELDS:
        if field not in entry:
            continue
        v, note = CLAIMS.get(key, {}).get(field, ("supports", None))
        claims[field] = verdict(v, note)
    bad_v = BAD_VARIANTS.get(key, {})
    variants = {
        "ok": [v for v in entry.get("variants", []) if v not in bad_v],
        "bad": [{"label": v, "note": bad_v[v]} for v in entry.get("variants", []) if v in bad_v],
    }
    bad_r = BAD_RELATIONS.get(key, {})
    relations = {
        "ok": [r for r in entry.get("relations", []) if r not in bad_r],
        "bad": [{"rel": r, "note": bad_r[r]} for r in entry.get("relations", []) if r in bad_r],
    }
    ans, reason = VOTES.get(key, ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    return {"key": key, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


def main():
    all_keys = set()
    for p in PACKETS:
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            packet = json.load(f)
        entries = packet["entries"]
        answers = [review(e) for e in entries]
        for e in entries:
            all_keys.add(e["key"])
            for bad in BAD_VARIANTS.get(e["key"], {}):
                assert bad in e.get("variants", []), (e["key"], bad)
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(answers, f, indent=1, ensure_ascii=False)
        claim_counts = {"supports": 0, "contradicts": 0, "unsure": 0}
        for a in answers:
            for c in a["claims"].values():
                claim_counts[c["verdict"]] += 1
            claim_counts["contradicts"] += len(a["variants"]["bad"]) + len(a["relations"]["bad"])
            claim_counts["supports"] += len(a["variants"]["ok"]) + len(a["relations"]["ok"])
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in answers:
            votes[a["job_listing_vote"]["answer"]] += 1
        print(p, len(answers), "judgements", claim_counts, "votes", votes)
    for table in (CLAIMS, BAD_VARIANTS, BAD_RELATIONS, VOTES):
        missing = set(table) - all_keys
        assert not missing, missing


if __name__ == "__main__":
    main()
