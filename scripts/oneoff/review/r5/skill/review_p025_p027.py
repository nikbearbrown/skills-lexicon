"""Reviewer answers for packets p025-p027 (skills lexicon). Run: python3 review_p025_p027.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Per-entry overrides. Anything not listed: claim = supports, variant/relation = ok, vote = yes.
# claim overrides: (verdict, note); variant/relation bad: {label: note}; vote: (answer, reason)
R = {
    # ---------------- p025 ----------------
    "jdesktop-network-components": {
        "vote": ("unsure", "Defunct mid-2000s Sun/SwingLabs project; rarely if ever named in listings"),
    },
    "jive-software": {
        "definition": ("supports", "The name is the vendor; the product is Jive, owned by Aurea since 2017"),
    },
    "joint-clearance-and-access-verification-system": {
        "definition": ("supports", "JPAS, including JCAVS, was retired in 2021 and replaced by DISS"),
    },
    "jsperf": {
        "definition": ("supports", "The original jsperf.com was offline for years"),
        "vote": ("unsure", "Niche benchmark site; seldom a listed requirement"),
    },
    "jtrac": {
        "variants_bad": {
            "JTrac - Open Source And Customizable Issue-Tracking In Java": "A website title/tagline, not a name for the tool",
        },
    },
    "kairosdb": {
        "definition": ("supports", "Began as an OpenTSDB rewrite that also supported HBase; Cassandra is its main store"),
    },
    "kinetic-typography": {
        "variants_bad": {
            "Kinetics (Typography)": "'Kinetics' is a physics/chemistry term, not a name for kinetic typography",
        },
    },
    "know-your-third-party-ky3p": {
        "definition": ("supports", "IHS Markit platform, now part of S&P Global"),
    },
    "kyoto-protocol": {
        "kind": ("supports", "A treaty; 'standard' fits only in the sense of binding rules, as for laws"),
        "vote": ("unsure", "A treaty largely superseded by the Paris Agreement; only occasionally cited in climate-policy roles"),
    },
    # ---------------- p026 ----------------
    "labview": {
        "definition": ("supports", "NI is now part of Emerson (2023); the language itself is called G"),
    },
    "laser-printing": {
        "vote": ("unsure", "A printing technology; listings rarely ask for it as a skill"),
    },
    "learning-agility": {
        "kind": ("unsure", "Defined as a capacity; 'ability' may fit better than 'skill'"),
    },
    "lego-digital-designer": {
        "definition": ("supports", "Discontinued by LEGO in 2016"),
        "vote": ("unsure", "Discontinued hobby software; rarely if ever requested"),
    },
    "levelator": {
        "definition": ("supports", "From The Conversations Network; no longer developed or supported"),
        "vote": ("unsure", "Discontinued free utility; rarely requested"),
    },
    # ---------------- p027 ----------------
    "logic-diagrams": {
        "kind": ("unsure", "A diagram notation; 'knowledge' or 'skill' fits better than 'method'"),
    },
    "low-risk-neonatal-nursing": {
        "certification": ("supports", "The area itself is not a credential; NCC's RNC-LRN certification exists separately"),
    },
    "luigi": {
        "definition": ("supports", "Luigi resolves job dependencies; timed triggering is usually left to cron"),
    },
    "macintosh-application-environment": {
        "definition": ("supports", "Ran on SPARC Solaris and HP-UX; discontinued in 1998"),
        "vote": ("unsure", "Discontinued in 1998; unlikely in current listings"),
    },
}

CLAIMS = ["definition", "kind", "certification", "certification_scope", "language_type"]


def verdict(v):
    out = {"verdict": v[0]}
    if v[1]:
        out["note"] = v[1][:150]
    return out


def review(entry):
    o = R.get(entry["key"], {})
    claims = {}
    for c in CLAIMS:
        if c in entry:
            claims[c] = verdict(o.get(c, ("supports", "")))
    vbad = o.get("variants_bad", {})
    variants = {
        "ok": [v for v in entry.get("variants", []) if v not in vbad],
        "bad": [{"label": v, "note": n} for v, n in vbad.items() if v in entry.get("variants", [])],
    }
    rbad = o.get("relations_bad", {})
    relations = {
        "ok": [r for r in entry.get("relations", []) if r not in rbad],
        "bad": [{"rel": r, "note": n} for r, n in rbad.items() if r in entry.get("relations", [])],
    }
    ans, reason = o.get("vote", ("yes", ""))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason[:150]
    return {"key": entry["key"], "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


def main():
    seen = set()
    for p in ["p025", "p026", "p027"]:
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            entries = json.load(f)["entries"]
        out = [review(e) for e in entries]
        seen.update(e["key"] for e in entries)
        os.makedirs(os.path.join(HERE, "answers"), exist_ok=True)
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        vcnt = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            vcnt[a["job_listing_vote"]["answer"]] += 1
        nbad = sum(len(a["variants"]["bad"]) for a in out)
        print(p, len(out), cnt, vcnt, "bad variants:", nbad)
    missing = set(R) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
