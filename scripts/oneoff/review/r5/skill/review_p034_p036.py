"""Reviewer answers for packets p034-p036 (skills lexicon). Writes answers/p034.json .. p036.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

S = "supports"
C = "contradicts"
U = "unsure"

# Per-entry overrides. Anything not listed: every claim supports, every variant ok,
# every relation ok, vote yes.
# Fields: claims {claim: (verdict, note)}, bad_variants {label: note},
#         bad_relations {rel: note}, vote (answer, reason)
REVIEW = {
    # ---------------- p034 ----------------
    "operations-administration-maintenance-and-provisioning": {
        "bad_variants": {
            "Operations Administration Maintenance SandsProvisioning (OAMP)":
                "Garbled label: 'SandsProvisioning' is a typo for 'and Provisioning'.",
        },
    },
    "oracle-eu-sovereign-cloud": {
        "vote": (U, "Narrow regional cloud offering; listings ask for OCI or Oracle Cloud, rarely this region set by name."),
    },
    "oracle-fixed-assets": {
        "bad_variants": {"Oracle Fixed Assets|": "Stray pipe character; a data-entry typo, not a real name."},
    },
    "organic-composition-of-capital": {
        "vote": ("no", "Concept of Marxian economic theory, not a skill or requirement listings ask for."),
    },
    # ---------------- p035 ----------------
    "overhead-camshaft-engine": {
        "vote": (U, "Engine-design concept; mechanic listings ask for engine repair, rarely OHC knowledge by name."),
    },
    "overhead-valve-engine": {
        "vote": (U, "Engine-design concept; mechanic listings ask for engine repair, rarely OHV knowledge by name."),
    },
    "oxidation-processes": {
        "bad_variants": {"Oxidattion Processes": "Misspelling of 'Oxidation'."},
        "vote": (U, "Broad chemistry concept; appears in some chemical/water-treatment roles but vague as a requirement."),
    },
    "package-json": {
        "claims": {"kind": (U, "A project manifest file, not a tool; 'knowledge' may fit better among the allowed kinds.")},
        "vote": (U, "A file inside Node.js projects; listings ask for Node.js/npm rather than package.json itself."),
    },
    "palm-os": {
        "claims": {"definition": (S, "Developed by Palm Computing/Palm Inc., later spun off to PalmSource; discontinued.")},
    },
    "paperwork-reduction-act": {
        "claims": {"kind": (S, "A statute (1980) rather than a technical standard; acceptable as a compliance standard.")},
    },
    "parasympathetic-nervous-system": {
        "bad_variants": {"Parasypathetic Nervous System": "Misspelling of 'Parasympathetic'."},
        "vote": ("no", "Anatomy/physiology concept, not something job listings ask for as a skill."),
    },
    "paris-agreement": {
        "vote": (U, "A treaty; knowledge of it is occasionally sought in climate-policy roles but rarely a listed skill."),
    },
    "pathlore": {
        "claims": {"definition": (S, "Pathlore was acquired by SumTotal Systems in 2005.")},
    },
    "pdf-viewer": {
        "vote": (U, "Generic everyday software category; rarely a stated requirement."),
    },
    "pelvic-floor": {
        "vote": (U, "Anatomical structure; listings ask for pelvic-floor therapy/rehab rather than the anatomy itself."),
    },
    # ---------------- p036 ----------------
    "penology": {
        "vote": (U, "Academic field; occasionally named in corrections or criminology roles."),
    },
    "percona-xtradb": {
        "claims": {"definition": (S, "Ships in Percona Server for MySQL; MariaDB used it as default only up to 10.1.")},
    },
    "periscope": {
        "vote": (U, "Defunct consumer streaming app; once listed in social-media roles, rarely asked for now."),
    },
    "periscope-data": {
        "claims": {"definition": (S, "Merged with Sisense in 2019 and folded into its product.")},
    },
    "personal-communications-service": {
        "vote": (U, "Telecom spectrum/service class; listings rarely ask for PCS knowledge by name."),
    },
    "personal-printer-data-stream": {
        "claims": {"definition": (S, "Specifically for IBM's personal/Proprinter line, later carried on by Lexmark.")},
        "vote": (U, "Obscure printer command language; rarely a listed requirement."),
    },
    "personal-protective-equipment": {
        "bad_variants": {"PPE": "Also widely means 'property, plant and equipment' in accounting."},
    },
    "pet-insurance": {
        "vote": (U, "An insurance product; product knowledge occasionally asked in insurance sales/service roles."),
    },
    "pet-insurance-sales": {
        "claims": {"definition": (S, "True but restates the name.")},
    },
    "philosophy-of-religion": {
        "vote": (U, "Academic field; appears mainly as an area of specialisation in academic hiring."),
    },
    "philosophy-of-science": {
        "vote": (U, "Academic field; appears mainly as an area of specialisation in academic hiring."),
    },
}

CLAIM_KEYS = ("definition", "kind", "certification", "certification_scope", "language_type")


def build(entry):
    key = entry["key"]
    r = REVIEW.get(key, {})
    claims = {}
    for c in CLAIM_KEYS:
        if c in entry:
            verdict, note = r.get("claims", {}).get(c, (S, None))
            obj = {"verdict": verdict}
            if note:
                obj["note"] = note
            claims[c] = obj
    bad_v = r.get("bad_variants", {})
    for label in bad_v:
        assert label in entry.get("variants", []), (key, label)
    variants = {
        "ok": [v for v in entry.get("variants", []) if v not in bad_v],
        "bad": [{"label": v, "note": n} for v, n in bad_v.items()],
    }
    bad_r = r.get("bad_relations", {})
    for rel in bad_r:
        assert rel in entry.get("relations", []), (key, rel)
    relations = {
        "ok": [x for x in entry.get("relations", []) if x not in bad_r],
        "bad": [{"rel": x, "note": n} for x, n in bad_r.items()],
    }
    ans, reason = r.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    return {"key": key, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


def main():
    seen = set()
    for p in ("p034", "p035", "p036"):
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            packet = json.load(f)
        out = []
        for e in packet["entries"]:
            seen.add(e["key"])
            out.append(build(e))
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        nbv = sum(len(a["variants"]["bad"]) for a in out)
        nbr = sum(len(a["relations"]["bad"]) for a in out)
        print(p, len(out), cnt, votes, "bad variants", nbv, "bad relations", nbr)
    missing = set(REVIEW) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
