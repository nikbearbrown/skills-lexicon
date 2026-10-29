import json, glob, os, re, unicodedata

REQ = "work/requests"
OUT = "work/responses"

KEEP = {"english": "English", "hvac": "HVAC", "emt": "EMT"}

FIELD = {
    "Foreign Languages": "foreign languages",
    "HVAC (Heating, Ventilation, and Air Conditioning) Repair": "heating, ventilation and air conditioning (HVAC) repair",
    "Emergency Medical Technician (EMT)": "emergency medical technician (EMT) training",
    "Physical Therapist Assistant": "physical therapist assisting",
    "Occupational Therapy Assistant": "occupational therapy assisting",
    "Dental Assistant": "dental assisting",
    "Nail Technician": "nail technology",
    "Paramedic": "paramedic training",
    "Pharmacy Technician": "pharmacy technician training",
    "Physical Therapy Assistant": "physical therapy assisting",
    "Veterinary Assistant": "veterinary assisting",
    "Medical Assistant": "medical assisting",
    "Veterinary Technology": "veterinary technology",
    "Performance Arts": "the performing arts",
    "Legal Studies": "legal studies",
}

PREFIXES = [
    ("Associate of Applied Science in ", "AAS"),
    ("Associate of Arts in ", "AA"),
    ("Associate of Science in ", "AS"),
    ("Bachelor's in ", "BACH"),
    ("Master's in ", "MAST"),
    ("Certificate in ", "CERT"),
    ("Diploma in ", "DIP"),
]

# relations: field text (after the prefix) -> list of target ids; each must be in that request's nearest
REL = {
    "Biomedical Equipment Technology": ["uxw4bog89z"],
    "Dental Assisting": ["hncua46gpo"],
    "Respiratory Therapy": ["dc088s7z0a"],
    "Public Health": ["jy5oyf5bao", "svio15mnpv"],
    "Business Administration": ["kyg8c9ysbl", "zr4o6v40dh", "ui0e3c544g"],
    "Pharmacy": ["b7mk8spxib", "lnbqfri4k9"],
    "Physical Therapy": ["d52wj7x3wm"],
    "Veterinary Science": ["ebrrubk4b4"],
    "Fine Arts": ["lxs84b3199"],
    "Computer Science": ["oxu0hc83pv"],
    "Cybersecurity": ["norpz7ekiw"],
    "Software Engineering": ["qmravcc671"],
    "Game Design": ["r8kn0vxljj"],
    "Art History": ["lkf15jjd0m"],
    "Mathematics": ["so9zp6tzyh"],
    "Public Policy": ["aqa8dgmx72"],
    "Real Estate": ["yeanq8udmx"],
    "Special Education": ["yplq0w5d56"],
    "Nursing": ["c4tp7yji9k", "gg2k98nhyp"],
    "Nursing (ADN)": ["gg2k98nhyp"],
    "Medical Billing and Coding": ["hqymi9wcca", "q6b708utin"],
    "Medical Assistant": ["pj8vtw9tl2", "fcjozwj5xy"],
    "Surgical Technology": ["uwo025jkxk"],
    "Emergency Medical Technician (EMT)": ["w809rqc0ip"],
    "Dental Assistant": ["hncua46gpo"],
}
# only valid for these levels (so a bachelor's-level relation is not hung on a diploma by accident)
REL_LEVEL = {
    "Biomedical Equipment Technology": {"AS"}, "Dental Assisting": {"AS"}, "Respiratory Therapy": {"AS"},
    "Public Health": {"AS", "BACH"}, "Business Administration": {"AS", "BACH"}, "Pharmacy": {"BACH"},
    "Physical Therapy": {"BACH"}, "Veterinary Science": {"BACH"}, "Fine Arts": {"BACH"},
    "Computer Science": {"BACH"}, "Cybersecurity": {"BACH"}, "Software Engineering": {"BACH"},
    "Game Design": {"BACH"}, "Art History": {"BACH"}, "Mathematics": {"BACH"}, "Public Policy": {"BACH"},
    "Real Estate": {"BACH"}, "Special Education": {"BACH"}, "Nursing": {"BACH"}, "Nursing (ADN)": {"AS"},
    "Medical Billing and Coding": {"DIP"}, "Medical Assistant": {"DIP"}, "Surgical Technology": {"DIP"},
    "Emergency Medical Technician (EMT)": {"DIP"}, "Dental Assistant": {"CERT"},
}

# definition overrides (full sentence)
DEF = {
    "Associate of Science in Nursing (ADN)": "A usually two-year associate degree in nursing, awarded as an Associate of Science by community colleges and some universities, that prepares graduates to take the registered-nurse licensing exam.",
    "Associate of Science in Pre-Dentistry": "A usually two-year Associate of Science degree with a pre-dentistry emphasis, meant to prepare students to transfer into a bachelor's programme on the way to dental school.",
    "Associate of Science in Pre-Pharmacy": "A usually two-year Associate of Science degree with a pre-pharmacy emphasis, meant to prepare students to transfer into a pharmacy programme.",
    "Associate of Science in Pre-Engineering": "A usually two-year Associate of Science degree with a pre-engineering emphasis, meant to prepare students to transfer into a bachelor's engineering programme.",
    "Bachelor's in Nursing": "An undergraduate degree in nursing, awarded by universities and colleges.",
}

def words_lower(s):
    out = []
    for w in re.split(r"(\s+)", s):
        core = re.sub(r"[^A-Za-z]", "", w).lower()
        if core in KEEP:
            out.append(w.replace(core, KEEP[core]) if w.lower() == w else re.sub(core, KEEP[core], w, flags=re.I))
        else:
            out.append(w.lower())
    return "".join(out)

def build(req):
    term = req["term"]
    near = {n["id"] for n in req["nearest"]}
    for pre, lvl in PREFIXES:
        if term.startswith(pre):
            rest = term[len(pre):]
            break
    else:
        raise SystemExit("no prefix: " + term)
    f = FIELD.get(rest) or words_lower(rest)
    pref = term
    variants = []
    if term == "Associate of Science in Nursing (ADN)":
        pref = "Associate of Science in Nursing"
    if lvl == "AAS":
        d = f"A usually two-year applied associate degree in {f}, awarded by community and technical colleges and aimed at preparing graduates for work in the field."
        variants.append(f"AAS in {rest}")
    elif lvl == "AA":
        d = f"A usually two-year associate degree in {f}, awarded by community colleges and some universities."
        variants.append(f"AA in {rest}")
    elif lvl == "AS":
        d = f"A usually two-year Associate of Science degree in {f}, awarded by community colleges and some universities."
    elif lvl == "BACH":
        d = f"An undergraduate degree in {f}, awarded by universities and colleges."
        variants += [f"Bachelor's degree in {rest}", f"Bachelors degree in {rest}"]
    elif lvl == "MAST":
        d = f"A postgraduate degree in {f}, awarded by universities."
        variants += [f"Master's degree in {rest}", f"Masters degree in {rest}"]
    elif lvl == "CERT":
        d = f"A certificate awarded by a college or training school on completing a short programme of study in {f}."
    elif lvl == "DIP":
        d = f"A vocational diploma awarded on completing a programme of study in {f}."
    d = DEF.get(term, d)
    key = rest
    if term == "Associate of Science in Nursing (ADN)":
        key = "Nursing (ADN)"
    rels = []
    if key in REL and lvl in REL_LEVEL[key]:
        for t in REL[key]:
            if t not in near:
                raise SystemExit(f"{term}: relation target {t} not in nearest")
            rels.append({"type": "related", "target": t, "basis": "general-knowledge"})
    ent = {
        "preferred_name": pref, "kind": "credential", "definition": d, "definition_basis": "general-knowledge",
        "variants": [{"label": v, "basis": "general-knowledge"} for v in variants],
        "relations": rels, "verbs": [],
        "certification": {"value": True, "basis": "general-knowledge"},
        "certification_scope": {"value": "many-issuers", "basis": "general-knowledge"},
        "language_type": {"value": None, "basis": "general-knowledge"},
        "annotation_note": "",
    }
    return {"decision": "new", "variant_of": None,
            "reason": "Names an academic or vocational credential awarded by many schools, so a new credential entry.",
            "entry": ent}

def main():
    os.makedirs(OUT, exist_ok=True)
    files = sorted(glob.glob(f"{REQ}/*.json"))
    seen = {}
    for f in files:
        req = json.load(open(f))
        resp = build(req)
        for lab in [resp["entry"]["preferred_name"]] + [v["label"] for v in resp["entry"]["variants"]]:
            n = lab.lower()
            if n in seen:
                raise SystemExit(f"label clash {lab!r}: {seen[n]} vs {req['term']}")
            seen[n] = req["term"]
        json.dump(resp, open(os.path.join(OUT, os.path.basename(f)), "w"), indent=1)
    print(len(files), "written")

main()
