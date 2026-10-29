"""Reviewer answers for packets p010-p012 (skills lexicon). Writes answers/p010.json, p011.json, p012.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
V = {"s": "supports", "c": "contradicts", "u": "unsure"}

# Per entry overrides. Defaults: definition/kind/certification = supports, all variants and relations ok, vote yes.
# d/k/c: (verdict, note); vbad/rbad: {label: note}; vote: (answer, reason)
R = {
    # ---------------- p010 ----------------
    "database-trigger": {},
    "db-access": {},
    "db2-400": {"d": ("s", "DB2/400 later DB2 UDB for iSeries, now Db2 for i; integrated into OS/400 / IBM i.")},
    "dbcc": {"d": ("s", "Correct for SQL Server; Sybase ASE also has DBCC (originally Database Consistency Checker).")},
    "dbfit": {},
    "dbpedia": {"k": ("s", "Really a dataset / knowledge graph; platform is the closest allowed kind.")},
    "dbsnp": {"vbad": {"Single Nucleotide Polymorphism Database[1] (DbSNP)": "Contains a stray Wikipedia citation marker [1]; not a real label."}},
    "dbunit": {},
    "dc-js": {},
    "dcid-6-3": {},
    "deal-shaping": {},
    "dealing-with-enquiries": {},
    "debits-and-credits": {},
    "deboning": {},
    "deburring": {},
    "decision-making-software": {"vote": ("unsure", "Generic software category; listings usually name a specific decision-analysis product.")},
    "decorating": {},
    "deegree": {},
    "defensive-tactics": {},
    "deflashing": {},
    "delivery-pipeline": {},
    "dell-wyse-thin-clients": {},
    "deltek-costpoint": {},
    "demolition": {},
    "dental-plaque-removal": {"d": ("s", "Scaling mainly targets calculus; plaque is also removed by brushing, flossing and prophylaxis polishing.")},
    "dental-records": {},
    "design-consultation": {},
    "design-documentation": {},
    "design-for-manufacturability": {},
    "design-of-experiments": {},
    "design-review": {},
    "design-validation": {},
    "desktop-management": {},
    "desmos": {},
    "destoner": {"d": ("s", "Field destoner is right; the term also names gravity destoners that remove stones from grain, beans or coffee.")},
    "dethatcher": {},
    "developmentally-appropriate-practice": {},
    "devexpress": {},
    "deviation-investigation": {},
    "deviation-management": {},
    # ---------------- p011 ----------------
    "devsecops": {},
    "diagnostic-analysis": {},
    "diagnostic-audiology": {},
    "dialectology": {},
    "dialogflow": {},
    "dictaphone": {"d": ("s", "Dictaphone is originally a trademark (Dictaphone Corp.) used generically for dictation recorders.")},
    "dictation": {},
    "dietetics": {},
    "digital-advertising": {},
    "digital-ai": {"d": ("s", "Formed 2020 from CollabNet VersionOne, XebiaLabs and Arxan; also covers testing and analytics.")},
    "digital-communications": {"d": ("s", "Covers the communications/marketing sense; in engineering the term means digital signal transmission.")},
    "digital-currencies": {},
    "digital-customer-strategy": {},
    "digital-fluency": {},
    "digital-health-technologies": {},
    "digital-humanities": {},
    "digital-journalism": {},
    "digital-merchandising": {},
    "digital-private-network-signalling-system": {},
    "digital-rights-management": {"vbad": {"DRM": "Also Oracle Data Relationship Management, disaster risk management, Direct Rendering Manager."}},
    "digital-skills": {},
    "digital-transformation": {},
    "dijkstra-s-algorithm": {},
    "dimensions-cm": {"d": ("s", "Lineage PVCS Dimensions > Serena > Micro Focus > OpenText.")},
    "direct-digital-control": {},
    "directx-video-acceleration": {"k": ("s", "An API specification rather than a library proper, but library is the closest allowed kind.")},
    "disability-insurance": {},
    "disaster-loans": {},
    "discipleship": {},
    "dispute-management": {},
    "distance-learning": {},
    "divide-and-conquer": {"vote": ("unsure", "Algorithm-design concept; listings usually ask for algorithms generally, rarely this technique by name.")},
    "do-178c": {"d": ("s", "Strictly an accepted means of compliance (FAA AC 20-115), not a mandatory rule, though de facto required.")},
    "docker": {},
    "docsis": {},
    "document-exploitation": {},
    "documentation-lifecycle": {},
    "docusign": {},
    "dod-8500-series": {"d": ("s", "Directive was DoDD 8500.01E; DoDD 8500.01E and DoDI 8500.2 were replaced in 2014 by DoDI 8500.01 Cybersecurity.")},
    "dod-information-assurance-certification-and-accreditation-process": {"d": ("s", "Used 2007-2014; replaced by RMF under DoDI 8510.01 (2014).")},
    # ---------------- p012 ----------------
    "dod-instruction-8510-01": {},
    "dodaf": {},
    "dot-js": {},
    "dot-matrix-printing": {"vote": ("unsure", "Printing technology; listings at most mention operating dot-matrix printers.")},
    "doubleclick-for-publishers": {"vbad": {"DFP": "Also Diploma of Financial Planning and other meanings; ambiguous outside ad-tech context."}},
    "dried-blood-spot": {},
    "driver-s-vision-enhancer": {"d": ("s", "A military vehicle system (e.g. AN/VAS-5).")},
    "driving": {},
    "drug-absorption": {},
    "drug-quality-and-security-act": {"k": ("s", "A statute rather than a technical standard; standard is the closest allowed kind.")},
    "dry-needling": {},
    "drywall-installation-and-repair": {},
    "duck-creek-platform": {},
    "durable-medical-equipment": {},
    "dust-js": {},
    "dynamic-host-configuration-protocol": {},
    "dynamic-link-library": {"vbad": {"DLL": "Also delay-locked loop (electronics) and doubly linked list."}},
    "dynamics-365-field-service": {},
    "e-marketing": {},
    "earlgrey": {},
    "early-childhood-mental-health": {},
    "earned-value-management-system": {"vbad": {"EVMS": "Also Eastern Virginia Medical School, which appears in job listings as an employer."}},
    "earth-leakage-circuit-breaker": {"d": ("s", "Term historically means the voltage-operated type; now often used loosely for current-operated RCDs.")},
    "earthing-systems": {},
    "easeljs": {},
    "ebay-api": {},
    "eclinicalworks": {},
    "ecological-study": {"vote": ("unsure", "Specific epidemiological design; listings usually ask for study design or epidemiology methods broadly.")},
    "econometric-model": {},
    "eddystone": {"d": ("s", "Google ended Nearby support in 2018; the format is little used now.")},
    "edius": {"d": ("s", "Originally developed by Canopus, acquired by Thomson/Grass Valley.")},
    "educational-assessment": {},
    "educational-therapy": {},
    "eight-disciplines-problem-solving": {"d": ("s", "Popularised by Ford Motor Company.")},
    "einstein-analytics": {},
    "elastic-stack": {},
    "electric-meters": {},
    "electric-vehicle": {
        "d": ("s", "Narrow: EVs can also run on fuel cells or overhead lines; battery EV is the common sense."),
        "k": ("u", "In listings mostly a knowledge area (EV systems/technology) rather than a tool operated."),
    },
    "electrical-diagnostics-and-repair": {},
    "electrical-power-quality": {},
}


def verdict(t):
    out = {"verdict": V[t[0]]}
    if t[1]:
        out["note"] = t[1]
    return out


def build(packet):
    with open(os.path.join(HERE, "packets", packet + ".json")) as f:
        data = json.load(f)
    answers = []
    for e in data["entries"]:
        key = e["key"]
        o = R[key]  # KeyError if an entry was not reviewed
        claims = {
            "definition": verdict(o.get("d", ("s", None))),
            "kind": verdict(o.get("k", ("s", None))),
        }
        if "certification" in e:
            claims["certification"] = verdict(o.get("c", ("s", None)))
        for extra in ("certification_scope", "language_type"):
            if extra in e:
                raise ValueError(f"{key} has {extra}; needs explicit review")
        vbad = o.get("vbad", {})
        for lab in vbad:
            assert lab in e["variants"], (key, lab)
        rbad = o.get("rbad", {})
        for rel in rbad:
            assert rel in e["relations"], (key, rel)
        vote = o.get("vote", ("yes", None))
        jv = {"answer": vote[0]}
        if vote[1]:
            jv["reason"] = vote[1]
        answers.append({
            "key": key,
            "claims": claims,
            "variants": {
                "ok": [v for v in e["variants"] if v not in vbad],
                "bad": [{"label": k, "note": n} for k, n in vbad.items()],
            },
            "relations": {
                "ok": [r for r in e["relations"] if r not in rbad],
                "bad": [{"rel": k, "note": n} for k, n in rbad.items()],
            },
            "job_listing_vote": jv,
        })
    with open(os.path.join(HERE, "answers", packet + ".json"), "w") as f:
        json.dump(answers, f, indent=1, ensure_ascii=False)
    return answers


def tally(ans):
    c = {"supports": 0, "contradicts": 0, "unsure": 0}
    v = {"yes": 0, "no": 0, "unsure": 0}
    for a in ans:
        for cl in a["claims"].values():
            c[cl["verdict"]] += 1
        c["supports"] += len(a["variants"]["ok"]) + len(a["relations"]["ok"])
        c["contradicts"] += len(a["variants"]["bad"]) + len(a["relations"]["bad"])
        v[a["job_listing_vote"]["answer"]] += 1
    return c, v


if __name__ == "__main__":
    for p in ("p010", "p011", "p012"):
        ans = build(p)
        for a in ans:
            for cl in a["claims"].values():
                assert len(cl.get("note", "")) <= 150, (a["key"], cl)
                if cl["verdict"] == "contradicts":
                    assert cl.get("note")
            for b in a["variants"]["bad"]:
                assert len(b["note"]) <= 150
            assert len(a["job_listing_vote"].get("reason", "")) <= 150
        print(p, len(ans), *tally(ans))
