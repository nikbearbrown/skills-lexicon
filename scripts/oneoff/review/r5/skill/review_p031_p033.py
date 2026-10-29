"""Reviewer answers for packets p031-p033 (skills lexicon). Writes answers/p031.json .. p033.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
S, C, U = "supports", "contradicts", "unsure"

# Per entry: overrides only. Defaults: definition/kind/certification supports, every variant and
# relation ok, vote yes. Overrides:
#   d/k/c: (verdict, note)   vb: {variant: note}   rb: {rel: note}   v: (answer, reason)
R = {}

# ---------------- p031 ----------------
R["p031"] = {
    "moz-pro": dict(vb={"Moz": "names the company Moz, which also sells Moz Local, STAT etc.; not only Moz Pro"}),
    "mp-m": dict(v=(U, "obsolete Digital Research OS from ~1980; essentially absent from current listings")),
    "mri-software": dict(d=(S, "true but vague; MRI Software is the Ohio-based vendor and its real estate software")),
    "mud-pump": dict(k=(S, "equipment rather than a hand tool, but tool is the closest allowed kind")),
    "nagle-s-algorithm": dict(v=(U, "narrow TCP implementation detail; rarely named as a listing requirement")),
    "naked-short-selling": dict(v=(U, "a market practice; appears only incidentally in compliance/trading roles")),
    "namenode": dict(k=(U, "an HDFS master daemon/component of Hadoop, not a standalone tool; knowledge fits better")),
    "national-geothermal-data-system": dict(v=(U, "niche DOE data catalogue; rarely named in job listings")),
    "nationwide-multistate-licensing-system": dict(
        d=(S, "SRR is a CSBS subsidiary; also hosts federal registry of MLOs")),
    "navigational-aid": dict(k=(U, "buoys/beacons are infrastructure, not tools; as a skill it is knowledge of navaids")),
}

# ---------------- p032 ----------------
R["p032"] = {
    "net-promoter-score": dict(k=(S, "strictly a metric; method is the closest allowed kind")),
    "nexpose": dict(d=(S, "on-premises scanner; Rapid7 now leads with InsightVM")),
    "nganimate": dict(v=(U, "narrow AngularJS (legacy) module; rarely named on its own in listings")),
    "nice-unix-utility": dict(v=(U, "a single shell command; rarely a listed requirement")),
    "nih-stroke-scale": dict(c=(S, "the scale itself is not a credential; NIHSS certification is a separate thing")),
    "nist-cybersecurity-framework": dict(d=(S, "CSF 2.0 (2024) added a sixth function, Govern")),
    "nitrogen-phosphorus-detector": dict(
        vb={"Nitrogen Phosphorous Detector": "misspelling: the element is phosphorus; phosphorous is an adjective"}),
    "no-child-left-behind-act": dict(
        k=(U, "a federal statute, not a technical standard; knowledge fits better"),
        v=(U, "repealed/replaced by ESSA in 2015; now rarely asked for")),
    "non-facility-associated-signalling": dict(
        d=(S, "strictly one D channel serving several PRI interfaces (T1 spans) in an NFAS group"),
        v=(U, "narrow legacy ISDN telephony detail; seldom named in listings")),
    "non-fungible-tokens": dict(vb={"NFT": "also nutrient film technique (hydroponics) and other expansions"}),
    "nosetests": dict(d=(S, "nose is unmaintained since ~2015; nose2/pytest succeeded it")),
    "npm": dict(d=(S, "npm says the name is not officially an acronym, though Node Package Manager is common")),
    "nuance-pdf-converter": dict(d=(S, "sold to Kofax in 2019 and rebranded Kofax Power PDF")),
    "nuodb": dict(d=(S, "acquired by Dassault Systemes in 2020")),
    "nutanix": dict(d=(S, "Nutanix is the company; definition describes its HCI/cloud platform")),
}

# ---------------- p033 ----------------
R["p033"] = {
    "nutanix-ahv": dict(k=(S, "a hypervisor; platform would also fit")),
    "nutanix-calm": dict(d=(S, "renamed NCM Self-Service (Nutanix Cloud Manager) in 2023")),
    "object-oriented-programming": dict(
        k=(S, "a paradigm; method is a reasonable allowed kind"),
        vb={"OOP": "also widely used for out-of-pocket (costs) in healthcare/finance listings"}),
    "oclc-connexion": dict(d=(S, "being phased out in favour of WorldShare Record Manager")),
    "ocunit": dict(v=(U, "obsolete since XCTest (Xcode 5, 2013); rarely in current listings")),
    "online-demonstration": dict(vb={"Online Demostration": "misspelling of demonstration"}),
    "open-network-computing": dict(v=(U, "legacy Sun technology family; rarely named as such in listings")),
    "openni": dict(d=(S, "OpenNI org closed in 2014 after Apple bought PrimeSense; OpenNI2 lives on"),
                   v=(U, "niche, largely legacy depth-camera SDK; rarely named in listings")),
}


def verdict(t):
    out = {"verdict": t[0]}
    if len(t) > 1 and t[1]:
        out["note"] = t[1][:150]
    return out


def build(packet_id):
    with open(os.path.join(HERE, "packets", packet_id + ".json")) as f:
        pk = json.load(f)
    ov = R[packet_id]
    keys = {e["key"] for e in pk["entries"]}
    unknown = set(ov) - keys
    assert not unknown, (packet_id, unknown)
    answers = []
    for e in pk["entries"]:
        o = ov.get(e["key"], {})
        claims = {"definition": verdict(o.get("d", (S,)))}
        if "kind" in e:
            assert e["kind"] in pk["allowed_kinds"], e["key"]
            claims["kind"] = verdict(o.get("k", (S,)))
        for name, short in (("certification", "c"), ("certification_scope", "cs"), ("language_type", "lt")):
            if name in e:
                claims[name] = verdict(o.get(short, (S,)))
        vb = o.get("vb", {})
        rb = o.get("rb", {})
        assert set(vb) <= set(e.get("variants", [])), e["key"]
        assert set(rb) <= set(e.get("relations", [])), e["key"]
        variants = {
            "ok": [v for v in e.get("variants", []) if v not in vb],
            "bad": [{"label": k, "note": n[:150]} for k, n in vb.items()],
        }
        relations = {
            "ok": [r for r in e.get("relations", []) if r not in rb],
            "bad": [{"rel": k, "note": n[:150]} for k, n in rb.items()],
        }
        ans, *reason = o.get("v", ("yes",))
        vote = {"answer": ans}
        if reason and reason[0]:
            vote["reason"] = reason[0][:150]
        assert ans == "yes" or "reason" in vote, e["key"]
        for c in claims.values():
            assert c["verdict"] != C or "note" in c, e["key"]
        answers.append({"key": e["key"], "claims": claims, "variants": variants,
                        "relations": relations, "job_listing_vote": vote})
    with open(os.path.join(HERE, "answers", packet_id + ".json"), "w") as f:
        json.dump(answers, f, indent=1, ensure_ascii=False)
    return answers


if __name__ == "__main__":
    for pid in ("p031", "p032", "p033"):
        a = build(pid)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for x in a:
            for c in x["claims"].values():
                cnt[c["verdict"]] += 1
            votes[x["job_listing_vote"]["answer"]] += 1
        vb = sum(len(x["variants"]["bad"]) for x in a)
        rb = sum(len(x["relations"]["bad"]) for x in a)
        print(pid, len(a), cnt, votes, "bad variants", vb, "bad relations", rb)
