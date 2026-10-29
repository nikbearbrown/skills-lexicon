import json, os

BASE = "/home/user/review/r3/certification"
S, C, U = "supports", "contradicts", "unsure"

# Per-entry overrides; anything not listed defaults to supports / all variants ok / all relations ok / vote yes.
# claim overrides: {claim: (verdict, note)}
# bad variants: {label: note}; bad relations: {rel: note}; vote: (answer, reason)
OV = {
    # ---- p001 ----
    "adult-acute-care-nurse-practitioner": {
        "claims": {"definition": (S, "Retired to renewal-only; succeeded by AGACNP"),
                   "certification_scope": (S, "Awarded by ANCC (ACNP-BC) and AACN (ACNPC), not one body")}},
    "adult-nurse-practitioner": {
        "claims": {"definition": (S, "Retired to renewal-only; succeeded by AGPCNP"),
                   "certification_scope": (S, "Awarded by ANCC (ANP-BC) and AANPCB (A-NP), not one body")}},
    "advanced-cardiovascular-life-support": {
        "claims": {"certification_scope": (C, "AHA created ACLS, but Heart and Stroke Foundation of Canada, ASHI/HSI and others issue ACLS cards")}},
    "advanced-certified-fund-raising-executive": {
        "claims": {"definition": (S, "Issuer is the Association of Fundraising Professionals (AFP)")}},
    "airline-transport-pilot-certificate": {
        "claims": {"definition": (S, "Since 2013 US airline first officers also need an ATP (or R-ATP); other states issue an ATPL")}},
    "american-medical-technologists-certification": {
        "bad_var": {"AMT certification": "AMT also means FAA Aviation Maintenance Technician certification"}},
    "aquatic-facility-operator": {
        "claims": {"definition": (S, "The AFO programme is run by the National Recreation and Park Association")}},
    "assisted-housing-manager-ahm": {
        "claims": {"certification_scope": (U, "Cannot confirm which body awards AHM")},
        "bad_var": {"AHM": "AHM also means AHIP's Academy for Healthcare Management and other things"}},
    "association-management-specialist-ams": {
        "bad_var": {"AMS": "AMS is highly ambiguous (American Meteorological Society, etc.)"}},
    "bachelor-of-science-in-pharmacy": {
        "claims": {"definition": (S, "Phased out in the US (PharmD is entry degree since ~2005); still awarded elsewhere")}},
    # ---- p002 ----
    "board-certified-specialist-in-sports-dietetics": {
        "bad_var": {"CSSD": "CSSD also means Central Sterile Services Department in hospitals"}},
    "boating-license": {
        "claims": {"definition": (S, "Many US states issue a boating safety education card rather than a licence")}},
    "ccna-security": {
        "claims": {"definition": (S, "Retired in February 2020 when Cisco consolidated CCNA")}},
    "certification-in-neurophysiologic-intraoperative-monitoring": {
        "claims": {"definition": (S, "Issuer (not named) is ABRET")}},
    "certification-in-transportation-and-logistics": {
        "claims": {"definition": (S, "Uninformative; it is the CTL of the American Society of Transportation and Logistics")}},
    "certified-alcoholism-and-drug-abuse-counselor": {
        "claims": {"definition": (S, "Awarded by state boards (e.g. Massachusetts), so varies by state")}},
    "certified-asthma-educator": {
        "claims": {"definition": (S, "Issuer is the National Asthma Educator Certification Board")}},
    "certified-bariatric-nurse": {
        "claims": {"definition": (S, "Issuer is the American Society for Metabolic and Bariatric Surgery")}},
    "certified-biomedical-equipment-technician": {
        "claims": {"definition": (S, "Issuer is the AAMI Credentials Institute")},
        "bad_var": {"CBET": "CBET also means competency-based education and training"}},
    "certified-clinical-transplant-coordinator": {
        "claims": {"definition": (S, "Issuer is the American Board for Transplant Certification")}},
    "certified-control-systems-technician": {
        "bad_var": {"CCST": "CCST also means Cisco Certified Support Technician"}},
    "certified-correctional-nurse": {
        "claims": {"definition": (S, "ACA's credential is titled Certified Corrections Nurse; NCCHC separately has CCHP-RN")}},
    "certified-diabetes-care-and-education-specialist": {
        "claims": {"definition": (S, "Issuer is CBDCE (formerly NCBDE)")}},
    "certified-diversity-recruiter": {
        "claims": {"definition": (S, "Issuer is AIRS (ADP)")}},
    # ---- p003 ----
    "certified-first-responder": {
        "claims": {"definition": (S, "US level now called Emergency Medical Responder")}},
    "certified-flight-registered-nurse": {
        "claims": {"definition": (S, "CFRN is flight-focused; BCEN's CTRN covers ground transport")}},
    "certified-hemodialysis-technician": {
        "claims": {"certification_scope": (C, "Title used by BONENT (CHT) and by state programmes such as California CDPH; not one issuer")}},
    "certified-industrial-hygienist": {
        "claims": {"definition": (S, "Issuer is the Board for Global EHS Credentialing (formerly ABIH)")},
        "bad_var": {"CIH": "CIH also means Chartered Institute of Housing (UK)"}},
    "certified-irb-manager": {
        "claims": {"definition": (S, "Issuer is PRIM&R")}},
    "certified-labview-developer": {
        "claims": {"definition": (S, "NI is now part of Emerson")}},
    "certified-medical-billing-and-coding-specialist": {
        "claims": {"definition": (S, "Generic; NHA's comparable credential is Certified Billing and Coding Specialist")}},
    "certified-music-therapist": {
        "claims": {"definition": (S, "Uninformative; CMT is a legacy AAMT designation, current US credential is MT-BC")}},
    "certified-network-defense-architect": {
        "claims": {"definition": (U, "CNDA was EC-Council's CEH exam for government/military staff; a design focus is doubtful; legacy")}},
    "certified-novell-salesperson": {
        "claims": {"definition": (S, "Legacy credential; Novell no longer exists independently")}},
    "certified-nurse-midwife": {
        "bad_var": {"Nurse Midwife": "Occupation title, not the AMCB credential; also used for non-certified roles abroad"}},
    "certified-nursing-assistant": {
        "bad_var": {"CNA": "CNA also means CNA Financial and Novell Certified NetWare Administrator"}},
    "certified-occupancy-specialist": {
        "claims": {"definition": (S, "Issued by the National Center for Housing Management")}},
}

CLAIMS = ["definition", "kind", "certification", "certification_scope", "language_type"]


def judge(entry, kinds):
    key = entry["key"]
    ov = OV.get(key, {})
    claims = {}
    for c in CLAIMS:
        if c not in entry:
            continue
        if c in ov.get("claims", {}):
            v, n = ov["claims"][c]
            claims[c] = {"verdict": v, "note": n} if n else {"verdict": v}
        elif c == "kind":
            claims[c] = {"verdict": S if entry["kind"] in kinds and entry["kind"] == "credential" else C}
        else:
            claims[c] = {"verdict": S}
    bad_var = ov.get("bad_var", {})
    variants = {"ok": [v for v in entry.get("variants", []) if v not in bad_var],
                "bad": [{"label": v, "note": n} for v, n in bad_var.items() if v in entry.get("variants", [])]}
    assert len(variants["ok"]) + len(variants["bad"]) == len(entry.get("variants", [])), key
    bad_rel = ov.get("bad_rel", {})
    relations = {"ok": [r for r in entry.get("relations", []) if r not in bad_rel],
                 "bad": [{"rel": r, "note": n} for r, n in bad_rel.items()]}
    vote = ov.get("vote", ("yes", None))
    jv = {"answer": vote[0]}
    if vote[1]:
        jv["reason"] = vote[1]
    for c in claims.values():
        assert len(c.get("note", "")) <= 150
    return {"key": key, "claims": claims, "variants": variants, "relations": relations, "job_listing_vote": jv}


used = set()
for p in ["p001", "p002", "p003"]:
    with open(os.path.join(BASE, "packets", p + ".json")) as f:
        pk = json.load(f)
    out = [judge(e, pk["allowed_kinds"]) for e in pk["entries"]]
    used |= {e["key"] for e in pk["entries"]}
    with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
        json.dump(out, f, indent=1)
    cnt = {S: 0, C: 0, U: 0}
    votes = {"yes": 0, "no": 0, "unsure": 0}
    vb = 0
    for a in out:
        for c in a["claims"].values():
            cnt[c["verdict"]] += 1
        votes[a["job_listing_vote"]["answer"]] += 1
        vb += len(a["variants"]["bad"])
    print(p, len(out), cnt, votes, "bad variants:", vb)

missing = set(OV) - used
assert not missing, missing
