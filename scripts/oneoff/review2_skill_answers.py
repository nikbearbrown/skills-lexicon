import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# Overrides; anything not listed: claim = supports, variant = ok, relation = ok, vote = yes.
DEF = {
    # p004
    "apple-device-enrollment-program": ("supports", "Now part of Apple Business Manager / Apple School Manager."),
    "appletviewer": ("supports", "Deprecated in JDK 9 and removed in JDK 11."),
    "applixware": ("supports", "Originally Applix Inc.; later sold by VistaSource and long discontinued."),
    "apptio": ("supports", "Apptio has been owned by IBM since 2023."),
    "architectural-rendering": ("supports", "Renderings can also be hand-drawn or non-photorealistic, not only realistic images from 3D models."),
    "arcsight-enterprise-security-manager": ("supports", "Now an OpenText product (via HP and Micro Focus)."),
    "armed-forces-health-longitudinal-technology-application": ("supports", "Being replaced by MHS GENESIS."),
    "arp4754": ("supports", "Revisions ARP4754A (2010) and ARP4754B (2023) are current usage."),
    # p005
    "artstation": ("supports", "Owned by Epic Games."),
    "asp-net-web-api": ("supports", "Its features were merged into ASP.NET Core MVC."),
    "atomic-layer-deposition": ("supports", "Growth per cycle is often less than a full monolayer."),
    "autoshade": ("supports", "AutoShade was a standalone companion program to AutoCAD rather than a plug-in."),
    "avantgo": ("supports", "Service shut down in 2009."),
    # p006
    "avid-elastic-reality": ("supports", "Originally developed by Elastic Reality Inc.; Avid acquired it in 1995."),
    "aws": ("supports", "True but thin: omits that Amazon provides it; the second clause is a scoping note, not a definition."),
    "azure-application-insights": ("supports", "Now a feature of Azure Monitor."),
    "blast-radius": ("supports", "Thin: should name the IT/SRE/security context (extent of impact of a failure, change or compromise)."),
    "board-support-package": ("supports", "A BSP is the software layer itself; the definition describes the activity of building one."),
    "branding": ("contradicts", "Key 'branding' is broader than the name; positioning is a distinct place vs competitors in the audience's mind, not just a promise."),
}

KIND = {
    "arp4754": ("contradicts", "An SAE Aerospace Recommended Practice is a standards document; kind 'standard' fits."),
    "asc-340": ("contradicts", "A codified US GAAP accounting-standard topic; kind 'standard' fits."),
    "arterial-blood-gas-testing": ("supports", "Could equally be a clinical skill (drawing and interpreting ABGs)."),
}

BAD_VARIANTS = {
    "application-specific-integrated-circuit": {
        "Application Specific Integrated Curcuits": "Misspelling of 'Circuits'.",
        "ASIC": "Ambiguous in listings: also Australian Securities and Investments Commission and Aviation Security Identification Card.",
    },
    "armed-forces-health-longitudinal-technology-application": {
        "Armed Forces Health Longitudinal Technology Application (AHTLA)": "Acronym misspelled; it is AHLTA.",
    },
    "autonomic-nervous-system": {
        "Autonomic Servous System": "Misspelling ('Servous').",
    },
    "blast-radius": {
        "blast radius": "Bare term's main sense is a literal explosion radius; it names the measure, not the analysis.",
    },
    "board-support-package": {
        "BSP": "Ambiguous: also binary space partitioning, bulk synchronous parallel, IATA Billing and Settlement Plan.",
    },
    "branding": {
        "positioning": "Generic word; also patient, product or GPS positioning; not specific to brand positioning.",
    },
}

BAD_RELATIONS = {}

VOTE = {
    "artstation": ("no", "Portfolio-hosting website; listings ask for a portfolio link there, not a skill."),
    "automotive-finance": ("no", "An industry/sector; listings cite it as industry experience rather than as a skill."),
    "automotive-loans": ("unsure", "A loan product; listings mention auto-lending experience, but the product itself is not a skill."),
    "autonomic-nervous-system": ("unsure", "Anatomical system; appears only as subject knowledge in niche clinical or research listings."),
    "blast-radius": ("unsure", "SRE/security jargon; mentioned as a design concern, rarely as a named required skill."),
}


def verdict(v):
    verdict_, note = v
    out = {"verdict": verdict_}
    if note:
        assert len(note) <= 150, note
        out["note"] = note
    return out


def build(packet):
    data = json.load(open(os.path.join(BASE, "packets", packet + ".json")))
    allowed = set(data["allowed_kinds"])
    answers = []
    for e in data["entries"]:
        k = e["key"]
        assert e["kind"] in allowed, k
        claims = {
            "definition": verdict(DEF.get(k, ("supports", None))),
            "kind": verdict(KIND.get(k, ("supports", None))),
        }
        if "certification" in e:
            assert e["certification"] is False, k
            claims["certification"] = {"verdict": "supports"}
        for extra in ("certification_scope", "language_type"):
            assert extra not in e, (k, extra)
        bad = BAD_VARIANTS.get(k, {})
        for lbl in bad:
            assert lbl in e["variants"], (k, lbl)
        variants = {
            "ok": [v for v in e["variants"] if v not in bad],
            "bad": [{"label": v, "note": bad[v]} for v in e["variants"] if v in bad],
        }
        brel = BAD_RELATIONS.get(k, {})
        relations = {
            "ok": [r for r in e["relations"] if r not in brel],
            "bad": [{"rel": r, "note": brel[r]} for r in e["relations"] if r in brel],
        }
        ans, reason = VOTE.get(k, ("yes", None))
        vote = {"answer": ans}
        if reason:
            assert len(reason) <= 150
            vote["reason"] = reason
        answers.append({"key": k, "claims": claims, "variants": variants,
                        "relations": relations, "job_listing_vote": vote})
    return answers


used = set(DEF) | set(KIND) | set(BAD_VARIANTS) | set(VOTE)
seen = set()
for p in ("p004", "p005", "p006"):
    ans = build(p)
    seen |= {a["key"] for a in ans}
    with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
        json.dump(ans, f, indent=1, ensure_ascii=False)
    c = {"supports": 0, "contradicts": 0, "unsure": 0}
    for a in ans:
        for cl in a["claims"].values():
            c[cl["verdict"]] += 1
    vb = sum(len(a["variants"]["bad"]) for a in ans)
    vo = sum(len(a["variants"]["ok"]) for a in ans)
    ro = sum(len(a["relations"]["ok"]) for a in ans)
    rb = sum(len(a["relations"]["bad"]) for a in ans)
    votes = {"yes": 0, "no": 0, "unsure": 0}
    for a in ans:
        votes[a["job_listing_vote"]["answer"]] += 1
    print(p, len(ans), c, "variants ok/bad", vo, vb, "relations ok/bad", ro, rb, votes)
assert used <= seen, used - seen
