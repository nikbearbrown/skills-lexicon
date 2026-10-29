import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Caveat notes on definition (verdict stays "supports" unless overridden).
DEF_NOTES = {
    "bachelor-s-in-dietetics": "Caveat: since 2024 US RDN exam eligibility also requires a graduate degree.",
    "bachelor-s-in-education": "Often the B.Ed.; a state/national teaching licence is a separate credential.",
    "bachelor-s-in-elementary-education": "A state teaching licence is a separate credential.",
    "bachelor-s-in-fine-arts": "Often the BFA (Bachelor of Fine Arts) professional degree, or a BA in fine arts.",
    "bachelor-s-in-nursing": "BSN/BN/BScN; RN licensure (e.g. NCLEX) is separate.",
    "bachelor-s-in-pharmacy": "US BS Pharm phased out (PharmD is entry-level since mid-2000s); B.Pharm still common elsewhere.",
    "bachelor-s-in-physical-therapy": "US entry-level PT degree is now the DPT; bachelor's PT degrees (BPT, BSc Physiotherapy) exist outside the US.",
    "bachelor-s-in-performance-arts": "Usually named 'Performing Arts'.",
    "bachelor-s-in-structural-engineering": "Uncommon standalone major; often civil engineering with a structural focus.",
    "bachelor-s-in-veterinary-science": "In UK/Aus/India the BVSc is the professional vet degree; in the US usually a pre-vet science degree.",
    "bachelor-s-in-social-work": "BSW; social work licensure is separate.",
    "certificate-in-aircraft-maintenance": "FAA Part 147 programmes often run 18-24 months; distinct from the FAA A&P mechanic certificate.",
    "certificate-in-barbering": "State barber licence (board exam) is a separate credential.",
    "certificate-in-nail-technician": "Name usually 'nail technology'; state nail-tech licence is separate.",
    "certificate-in-paramedic": "Programmes often 12-18 months; practising also needs state licence/NREMT certification.",
    "certificate-in-pharmacy-technician": "National certification (PTCB/NHA) is separate.",
    "certificate-in-physical-therapy-assistant": "US PTAs need an associate degree from a CAPTE-accredited programme plus licence; certificates are mostly aide-level.",
    "diploma-in-cosmetology": "State cosmetology licence is separate.",
    "diploma-in-emergency-medical-technician-emt": "In the US EMT is a short course leading to state/NREMT certification, not a diploma; diploma form common in India.",
    "diploma-in-esthetics": "State esthetician licence is separate.",
    "diploma-in-massage-therapy": "State/provincial massage licence is separate.",
    "driver-s-license": "Issued by states, provinces or national authorities.",
    "master-s-in-art": "Vague: may be an MA or MFA in art.",
}

VOTE_OVERRIDES = {
    "certificate-in-physical-therapy-assistant": (
        "unsure",
        "PTA listings ask for an accredited associate degree plus state licence; short certificates are rarely asked for.",
    ),
}


def judge(entry):
    key = entry["key"]
    claims = {}
    d = {"verdict": "supports"}
    if key in DEF_NOTES:
        d["note"] = DEF_NOTES[key]
    claims["definition"] = d
    if "kind" in entry:
        claims["kind"] = {"verdict": "supports" if entry["kind"] == "credential" else "contradicts"}
    if "certification" in entry:
        claims["certification"] = {"verdict": "supports" if entry["certification"] is True else "contradicts"}
    if "certification_scope" in entry:
        claims["certification_scope"] = {
            "verdict": "supports" if entry["certification_scope"] == "many-issuers" else "contradicts"
        }
    for c in claims.values():
        if c["verdict"] == "contradicts" and "note" not in c:
            raise SystemExit(f"missing note for contradicts in {key}")
    ans = {
        "key": key,
        "claims": claims,
        "variants": {"ok": list(entry.get("variants", [])), "bad": []},
        "relations": {"ok": list(entry.get("relations", [])), "bad": []},
    }
    if key in VOTE_OVERRIDES:
        a, r = VOTE_OVERRIDES[key]
        ans["job_listing_vote"] = {"answer": a, "reason": r}
    else:
        ans["job_listing_vote"] = {"answer": "yes"}
    return ans


def main():
    for p in ("p004", "p005", "p006"):
        with open(os.path.join(BASE, "packets", f"{p}.json")) as f:
            packet = json.load(f)
        out = [judge(e) for e in packet["entries"]]
        for a in out:
            for c in a["claims"].values():
                assert len(c.get("note", "")) <= 150, (a["key"], c)
            assert len(a["job_listing_vote"].get("reason", "")) <= 150
        with open(os.path.join(BASE, "answers", f"{p}.json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        counts = {"supports": 0, "contradicts": 0, "unsure": 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                counts[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        print(p, len(out), counts, votes)


if __name__ == "__main__":
    main()
