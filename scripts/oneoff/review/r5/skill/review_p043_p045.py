"""Reviewer judgments for packets p043-p045; writes answers/p043.json .. p045.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
S = "supports"
C = "contradicts"
U = "unsure"

# key -> judgments. d = definition, k = kind, c = certification (default supports),
# vbad = {variant: note} (all other variants ok), rbad = {rel: note}, vote = (answer, reason)
J = {
    # ---------------- p043 ----------------
    "sap-is-retail": {},
    "sap-lumira": {"d": (S, "Being phased out in favour of SAP Analytics Cloud.")},
    "sap-materials-management": {"vbad": {"SAP Meterial Management": "Misspelling of 'Material'."}},
    "sap-netweaver-process-integration": {"d": (S, "Later bundled as SAP Process Orchestration; successor is SAP Integration Suite.")},
    "sap-quality-management": {},
    "sap-s-4hana": {},
    "sap-sovereign-cloud": {},
    "sap-technology-consulting": {"vbad": {"SAP Technology Consultanting": "Misspelling ('Consultanting')."}},
    "savon": {},
    "scaffold-building": {},
    "scala-js": {},
    "scalding": {"d": (S, "Built on top of Cascading.")},
    "scara-robot": {"k": (S, "A robot type; 'tool' would also fit, as for other machines.")},
    "schema-markup": {"k": (S, "Uses the schema.org vocabulary standard; 'skill' would also fit.")},
    "schematic-diagrams": {},
    "scholarship-of-teaching-and-learning": {},
    "school-counseling": {},
    "schoology": {"d": (S, "PowerSchool acquired Schoology in 2019.")},
    "scientific-computing": {"vbad": {"Scientific Computating": "Misspelling ('Computating')."}},
    "scientific-modelling": {},
    "scikit-learn": {},
    "scope-statement": {},
    "screen-design": {},
    "screen-reader": {},
    "screw-conveyor": {},
    "script-writing": {},
    "sd-card": {"vote": (U, "A storage medium; seldom asked for as a skill in its own right.")},
    "seamanship": {},
    "seating-guests": {},
    "section-drawings": {},
    "secure-coding": {},
    "secure-shell": {},
    "secured-transactions": {},
    "security-information-and-event-management": {},
    "security-management": {},
    "security-onion": {},
    "security-operations": {},
    "seeder": {},
    "seesaw-software": {},
    "segment-software": {"d": (S, "Twilio acquired Segment in 2020.")},
    # ---------------- p044 ----------------
    "selenium": {},
    "seliwanoff-s-test": {"vote": (U, "Teaching-lab carbohydrate test; rarely named in job listings.")},
    "sequel-pro": {"d": (S, "Open source and no longer maintained; Sequel Ace is the active fork.")},
    "sequelize": {},
    "serial-ata": {},
    "serial-line-internet-protocol": {
        "vbad": {
            "Serial Line Internet Protocolss": "Misspelling ('Protocolss').",
            "SLIP": "Collides with the common word 'slip' (packing slip, pay slip, slip and fall).",
        },
        "vote": (U, "Legacy protocol; rarely named in current listings."),
    },
    "service-desk": {},
    "service-level-requirement": {},
    "service-orientation": {"d": (S, "Matches O*NET's soft-skill sense, not service-oriented architecture.")},
    "servicenow": {},
    "servicenow-discovery": {},
    "sex-therapy": {},
    "sha-256": {},
    "sha-512": {},
    "shaolin-kung-fu": {"vote": (U, "Martial art; only asked for in instructor roles.")},
    "sharable-content-object-reference-model": {"d": (S, "Developed by the US ADL Initiative.")},
    "shared-vision-planning": {"vote": (U, "Niche US Army Corps of Engineers planning method; rarely in listings.")},
    "sharefile": {"d": (C, "Not originally Citrix: founded independently (2005), bought by Citrix 2011, owned by Progress since 2024.")},
    "sharp-zaurus": {"vote": ("no", "Discontinued PDA line; not a current job requirement.")},
    "shepard-s-citations": {},
    "ship-handling": {},
    "shipping-and-receiving": {},
    "shipping-management": {},
    "shoulder-surgery": {},
    "shower-installation": {},
    "shrink-wrapping": {},
    "shuttle-car-operation": {"d": (S, "Diesel and battery shuttle cars also exist.")},
    "signalling-connection-control-part": {},
    "signalling-system-no-7": {},
    "silk-test": {
        "d": (C, "Micro Focus was bought by OpenText in 2023; Silk Test is now an OpenText product."),
        "vbad": {"SilkTesting": "Garbled form of the product name, not used."},
    },
    "simple-interrupted-suture": {},
    "simple-mail-transfer-protocol": {},
    "simple-public-key-infrastructure": {
        "d": (S, "RFC 2693 is Experimental; SPKI merged with SDSI."),
        "vbad": {"SPKI": "Also widely means X.509 SubjectPublicKeyInfo (e.g. SPKI pinning)."},
        "vote": (U, "Experimental IETF scheme; rarely named in listings."),
    },
    "simplelegal": {},
    "simputer": {"vote": ("no", "Obsolete early-2000s device; not a job requirement.")},
    "single-in-line-memory-module": {"vote": ("no", "Obsolete memory form factor; not asked for in current listings.")},
    "single-sign-on": {},
    "site-reliability-engineering": {},
    "skip-tracing": {},
    "sluice-gate": {
        "vbad": {"Sluce Gates": "Misspelling of 'Sluice'."},
        "vote": (U, "A water-control structure; named only in some dam/canal operator roles."),
    },
    # ---------------- p045 ----------------
    "slurm-workload-manager": {},
    "smart-buildings": {},
    "smart-lighting": {},
    "smart-meter-systems": {},
    "smart-pig": {},
    "smartbidnet": {},
    "smartphone-operation": {},
    "snort": {"d": (S, "Originally Sourcefire, now Cisco.")},
    "snow-software": {"d": (S, "Snow Software was acquired by Flexera in 2024.")},
    "social-and-behavior-change-communication": {},
    "social-determinants-of-health": {},
    "social-emotional-learning": {
        "vbad": {"SEL": "Also Schweitzer Engineering Laboratories (SEL relays), common in power/utility listings."},
    },
    "social-impact-bond": {},
    "social-media-advertising": {},
    "social-media-analytics": {},
    "social-media-content-creation": {},
    "social-media-content-management": {},
    "social-media-management": {},
    "social-media-optimization": {},
    "social-sustainability": {},
    "sociology-of-education": {},
    "socket-478": {"vote": ("no", "Obsolete CPU socket; not asked for in current listings.")},
    "socket-5": {"vote": ("no", "Obsolete 1990s CPU socket; not asked for in current listings.")},
    "sockjs": {},
    "softrax": {},
    "software-defined-wan": {
        "vbad": {"Software-Defined Networking Wide Area Network (SD-WAN)": "Garbled expansion; SD-WAN is software-defined wide area network."},
    },
    "software-quality-assurance": {},
    "software-quality-management": {},
    "software-reliability-testing": {},
    "software-testing-life-cycle": {},
    "soil-fertility-treatment": {},
    "solar-panel": {},
    "solar-street-light": {"vote": (U, "A product; rarely a listed skill except for installers.")},
    "sonicstage": {
        "d": (S, "Discontinued in the early 2010s."),
        "vote": ("no", "Discontinued consumer music software; not a job requirement."),
    },
    "sonicwall": {},
    "soot-blower": {},
    "source-insight": {"d": (C, "Vendor is Source Dynamics, Inc., not 'SI Software'.")},
    "sourcegear-vault": {"vote": (U, "Legacy niche version control system; seldom named in listings.")},
    "sovereign-cloud": {},
    "spacy": {"d": (S, "Developed by Explosion.")},
}


def verdict(v):
    out = {"verdict": v[0]}
    if len(v) > 1 and v[1]:
        out["note"] = v[1]
    return out


def build(packet):
    with open(os.path.join(HERE, "packets", f"{packet}.json")) as f:
        data = json.load(f)
    allowed = set(data["allowed_kinds"])
    answers = []
    for e in data["entries"]:
        key = e["key"]
        j = J[key]
        claims = {}
        if "definition" in e:
            claims["definition"] = verdict(j.get("d", (S,)))
        if "kind" in e:
            assert e["kind"] in allowed, key
            claims["kind"] = verdict(j.get("k", (S,)))
        if "certification" in e:
            claims["certification"] = verdict(j.get("c", (S,)))
        for extra in ("certification_scope", "language_type"):
            if extra in e:
                claims[extra] = verdict(j[extra])
        vbad = j.get("vbad", {})
        for lbl in vbad:
            assert lbl in e.get("variants", []), (key, lbl)
        rbad = j.get("rbad", {})
        for r in rbad:
            assert r in e.get("relations", []), (key, r)
        ans = {
            "key": key,
            "claims": claims,
            "variants": {
                "ok": [v for v in e.get("variants", []) if v not in vbad],
                "bad": [{"label": l, "note": n} for l, n in vbad.items()],
            },
            "relations": {
                "ok": [r for r in e.get("relations", []) if r not in rbad],
                "bad": [{"rel": r, "note": n} for r, n in rbad.items()],
            },
        }
        vote = j.get("vote", ("yes",))
        jv = {"answer": vote[0]}
        if len(vote) > 1:
            jv["reason"] = vote[1]
        ans["job_listing_vote"] = jv
        answers.append(ans)
    keys = [e["key"] for e in data["entries"]]
    assert len(keys) == len(answers)
    with open(os.path.join(HERE, "answers", f"{packet}.json"), "w") as f:
        json.dump(answers, f, indent=1, ensure_ascii=False)
    return answers


def counts(answers):
    c = {S: 0, C: 0, U: 0}
    v = {"yes": 0, "no": 0, "unsure": 0}
    for a in answers:
        for cl in a["claims"].values():
            c[cl["verdict"]] += 1
        v[a["job_listing_vote"]["answer"]] += 1
    return c, v


if __name__ == "__main__":
    for p in ("p043", "p044", "p045"):
        a = build(p)
        c, v = counts(a)
        print(p, len(a), c, v)
