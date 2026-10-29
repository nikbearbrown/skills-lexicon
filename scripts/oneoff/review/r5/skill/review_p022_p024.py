"""Dump reviewer answers for packets p022-p024 into answers/."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
S, C, U = "supports", "contradicts", "unsure"

# Per-entry judgements. Anything not listed defaults to: definition/kind/certification
# supports, every variant ok, every relation ok, vote yes.
# Fields: d = (verdict, note) for definition, k = (verdict, note) for kind,
# vb = {variant: note} bad variants, rb = {rel: note} bad relations,
# v = (answer, reason) job listing vote.
J = {
    # ---------------- p022 ----------------
    "ids-infolease": {"d": (S, "Made by International Decision Systems (IDS), since rebranded Solifi.")},
    "ieee-1394": {"d": (S, "Apple developed it; FireWire is Apple's brand name (Sony's is i.LINK).")},
    "imac-g4": {"v": ("no", "A specific discontinued computer model, not a skill listings ask for.")},
    "imac-g5": {"v": ("no", "A specific discontinued computer model, not a skill listings ask for.")},
    "inbound-logistics": {"d": (S, "Purchasing is often treated separately (Porter puts procurement in support activities).")},
    "incurred-but-not-reported": {"d": (S, "Strictly unreported claims; reported-but-unsettled claims sit in case reserves (RBNS), with IBNER for shortfalls.")},
    "indexeddb": {"k": (S, "A W3C browser API; 'tool' is acceptable.")},
    "individualized-education-program": {"vb": {"IEP": "Also Intensive English Program, common in ESL teaching listings."}},
    "information-hiding": {"v": ("unsure", "A design principle; listings usually ask for OOP or encapsulation rather than naming it.")},
    "infusion-enterprise-control-system": {
        "d": (S, "Schneider Electric acquired Invensys in 2014; the InFusion brand has since faded."),
        "v": ("unsure", "Niche, largely retired product brand; rarely named in listings."),
    },
    "ingres": {"d": (S, "Commercialised by Relational Technology Inc. (renamed Ingres Corp.), then ASK, Computer Associates, a 2005 spin-out and Actian.")},
    # ---------------- p023 ----------------
    "instagram-stories": {"k": (S, "A feature of Instagram; 'tool' is acceptable.")},
    "intel-viiv": {"v": ("no", "A retired Intel marketing brand for PCs, not a skill.")},
    "intended-nationally-determined-contributions": {
        "v": ("unsure", "Historical term; climate-policy listings now ask about NDCs."),
    },
    "internet-protocol-suite": {"vb": {"Internet Protocolss": "Misspelling."}},
    "interqual": {"d": (S, "Now sold by Optum (formerly Change Healthcare).")},
    "intradermal-injection": {"vb": {"Intradermal": "Bare adjective; also used for intradermal sutures, tests and other routes of use."}},
    "intravenous-infusion": {"vb": {"Intravenous (IV) Fusions": "Misspelling of infusions."}},
    "invision": {"d": (S, "Shut down at the end of 2024; still common in older listings.")},
    # ---------------- p024 ----------------
    "io-js": {"v": ("no", "Short-lived fork merged into Node.js in 2015; listings ask for Node.js.")},
    "ioffice": {"d": (S, "iOFFICE merged with SpaceIQ and is now part of Eptura.")},
    "ireport-designer": {"d": (S, "Retired in 2015, replaced by Jaspersoft Studio.")},
    "iso-9000": {"d": (S, "The single ISO 9000 standard (fundamentals and vocabulary) sets out the vocabulary; the family also includes 9001 and 9004.")},
    "iso-iec-27000-series": {"vb": {"ISO/IEC 27001 Series": "Names the single 27001 standard, not the 27000 family."}},
    "iso-iec-9075-sql-standard": {"d": (S, "ANSI published SQL first (1986); ISO followed in 1987 and ANSI now adopts the ISO/IEC text.")},
    "iss-environmental-control-and-life-support-system": {
        "v": ("unsure", "Very specific system; aerospace listings usually ask for ECLSS in general."),
    },
    "it-s-lemma": {"v": ("unsure", "A single theorem; quant listings ask for stochastic calculus rather than naming it.")},
    "itu-t-t-30": {"vb": {"T.30 Standars": "Misspelling."}},
    "jafan": {"d": (S, "Largely superseded by DoD Manual 5205.07 and the Joint SAP Implementation Guide (JSIG).")},
    "java-archive": {"vb": {"JAR": "Also Joint Aviation Requirements (JAR-145, JAR-OPS) and the ordinary word jar."}},
    "java-communications-api": {"v": ("unsure", "Old, niche Sun API; rarely named in listings.")},
    "java-persistence-api-2-0": {"k": (S, "Strictly an API specification (JSR 317) implemented by Hibernate, EclipseLink etc.")},
}

CLAIM_FIELDS = [("definition", "d"), ("kind", "k"), ("certification", "c"),
                ("certification_scope", "cs"), ("language_type", "lt")]


def verdict(v):
    out = {"verdict": v[0]}
    if len(v) > 1 and v[1]:
        out["note"] = v[1][:150]
    return out


def build(packet):
    data = json.load(open(os.path.join(HERE, "packets", f"{packet}.json")))
    answers = []
    for e in data["entries"]:
        j = J.get(e["key"], {})
        claims = {}
        for field, short in CLAIM_FIELDS:
            if field in e:
                claims[field] = verdict(j.get(short, (S,)))
        vb = j.get("vb", {})
        variants = {"ok": [x for x in e.get("variants", []) if x not in vb],
                    "bad": [{"label": k, "note": n} for k, n in vb.items()]}
        assert all(k in e.get("variants", []) for k in vb), e["key"]
        rb = j.get("rb", {})
        relations = {"ok": [r for r in e.get("relations", []) if r not in rb],
                     "bad": [{"rel": k, "note": n} for k, n in rb.items()]}
        vote = j.get("v", ("yes", ""))
        jv = {"answer": vote[0]}
        if vote[1]:
            jv["reason"] = vote[1][:150]
        answers.append({"key": e["key"], "claims": claims, "variants": variants,
                        "relations": relations, "job_listing_vote": jv})
    unknown = set(J) - {e["key"] for e in data["entries"]}
    return answers, unknown


if __name__ == "__main__":
    all_unknown = set(J)
    for p in ["p022", "p023", "p024"]:
        ans, _ = build(p)
        all_unknown -= {a["key"] for a in ans}
        with open(os.path.join(HERE, "answers", f"{p}.json"), "w") as f:
            json.dump(ans, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in ans:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        badv = sum(len(a["variants"]["bad"]) for a in ans)
        print(p, len(ans), cnt, votes, "bad variants:", badv)
    assert not all_unknown, all_unknown
