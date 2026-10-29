"""Reviewer answers for packets p007-p009 (skills lexicon). Writes answers/p00N.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CLAIM_KEYS = ["definition", "kind", "certification", "certification_scope", "language_type"]

# Per-entry overrides. Defaults: every claim supports, every variant ok, every relation ok, vote yes.
# "claims": {claim: (verdict, note)}; "bad_variants": {label: note}; "bad_relations": {rel: note};
# "vote": (answer, reason)
J = {
    # ---------------- p007 ----------------
    "conflict-catcher": {
        "claims": {"definition": ("supports", "Casady & Greene utility; discontinued with the end of classic Mac OS")},
        "vote": ("unsure", "Obsolete classic Mac OS utility; a tool skill in principle but essentially absent from current listings"),
    },
    "constituent-relationship-management": {
        "claims": {"kind": ("unsure", "More a practice/skill area (and software category) than a defined method")},
    },
    "constant-contact": {
        "bad_variants": {"Constantcontact": "Run-together misspelling of the brand name (domain form), not a name variant"},
    },
    "contact-management-software": {
        "bad_variants": {"Contact Management Softwares": "Nonstandard plural 'softwares'; a grammatical misspelling"},
    },
    "contour-plowing": {
        "vote": ("unsure", "Soil-conservation farming practice; seldom named as a requirement in job listings"),
    },
    "control-loops": {
        "claims": {"definition": ("supports", "Describes closed (feedback) loops, the usual meaning in process control")},
    },
    "conversational-ai": {
        "claims": {"definition": ("supports", "Phrased as an activity; the term names the technology/field, but the gist is right")},
    },
    "coppermine-photo-gallery": {
        "vote": ("unsure", "Niche, largely dormant open-source PHP gallery; rarely if ever requested in listings"),
    },
    "coreos": {
        "claims": {"definition": ("supports", "CoreOS Container Linux reached end of life in 2020; successors are Fedora CoreOS and RHEL CoreOS")},
    },
    "corona-sdk": {
        "claims": {"definition": ("supports", "Open-sourced and renamed Solar2D in 2020")},
    },
    "coso-framework": {
        "claims": {"kind": ("supports", "Strictly a framework, not a formal standard, but it functions as the de facto internal-control standard")},
    },
    # ---------------- p008 ----------------
    "create-react-app": {
        "claims": {"definition": ("supports", "Officially deprecated by the React team in 2025")},
    },
    "creo-elements-pro": {
        "claims": {"definition": ("supports", "Name used 2010-2011; succeeded by Creo Parametric")},
    },
    "crime-scene-investigation": {
        "bad_variants": {"Crime Scenes (Forensic Evidence)": "Names the places/evidence, not the investigation skill; a catalogue label"},
    },
    "cross-product": {
        "vote": ("no", "A single math operation; listings ask for linear algebra or vector math, not the cross product itself"),
    },
    "cryengine": {
        "bad_variants": {"CryEngines": "Plural of a product name; not a form the engine is called"},
    },
    "cu-seeme": {
        "claims": {"definition": ("supports", "Later commercialised by White Pine Software; long obsolete")},
        "vote": ("unsure", "Obsolete 1990s software; a tool skill in principle but essentially absent from current listings"),
    },
    # ---------------- p009 ----------------
    "darik-s-boot-and-nuke": {
        "claims": {"definition": ("supports", "Free edition largely unmaintained since Blancco bought it; not reliable for SSDs")},
    },
    "dashdb": {
        "vote": ("unsure", "Retired product name (now Db2 Warehouse on Cloud); rare in current listings"),
    },
    "data-as-a-service": {
        "bad_variants": {"Data As A Services": "Ungrammatical plural 'Services'; a misspelling of the name"},
    },
    "data-pipeline": {
        "claims": {"kind": ("unsure", "A pipeline is a system/artefact, not a method; 'knowledge' or 'skill' (building pipelines) fits better")},
    },
    "database-life-cycle": {
        "vote": ("unsure", "Textbook database-design concept; listings seldom name it as a requirement"),
    },
    "database-mirroring": {
        "claims": {"definition": ("supports", "Also the name of a specific, deprecated SQL Server feature")},
    },
}


def build(entry):
    key = entry["key"]
    o = J.get(key, {})
    claims = {}
    for c in CLAIM_KEYS:
        if c in entry:
            verdict, note = o.get("claims", {}).get(c, ("supports", None))
            d = {"verdict": verdict}
            if note:
                d["note"] = note[:150]
            claims[c] = d
    for c in o.get("claims", {}):
        assert c in entry, (key, c)
    bad_v = o.get("bad_variants", {})
    for lab in bad_v:
        assert lab in entry["variants"], (key, lab)
    variants = {
        "ok": [v for v in entry["variants"] if v not in bad_v],
        "bad": [{"label": l, "note": n[:150]} for l, n in bad_v.items()],
    }
    bad_r = o.get("bad_relations", {})
    for r in bad_r:
        assert r in entry["relations"], (key, r)
    relations = {
        "ok": [r for r in entry["relations"] if r not in bad_r],
        "bad": [{"rel": r, "note": n[:150]} for r, n in bad_r.items()],
    }
    ans, reason = o.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason[:150]
    return {"key": key, "claims": claims, "variants": variants, "relations": relations, "job_listing_vote": vote}


def main():
    seen = set()
    for p in ["p007", "p008", "p009"]:
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            pk = json.load(f)
        out = [build(e) for e in pk["entries"]]
        seen.update(e["key"] for e in pk["entries"])
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
        vcnt = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            vcnt[a["job_listing_vote"]["answer"]] += 1
        badv = sum(len(a["variants"]["bad"]) for a in out)
        okv = sum(len(a["variants"]["ok"]) for a in out)
        print(p, len(out), "claims", cnt, "votes", vcnt, "variants ok/bad", okv, badv)
    missing = set(J) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
