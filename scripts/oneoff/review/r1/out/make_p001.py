import json, collections

S = {"verdict": "supports"}
def C(note): return {"verdict": "contradicts", "note": note}
def U(note): return {"verdict": "unsure", "note": note}
def full(defn=S, kind=S, cert=S, scope=S):
    return {"definition": defn, "kind": kind, "certification": cert, "certification_scope": scope}
YES = {"answer": "yes"}
def rel(ok=(), bad=()): return {"ok": list(ok), "bad": list(bad)}
def var(ok=(), bad=()): return {"ok": list(ok), "bad": list(bad)}

answers = [
 {"key": "activity-director-certified", "claims": full(),
  "variants": var(), "relations": rel(), "job_listing_vote": YES},
 {"key": "acute-care-nurse-practitioner", "claims": full(),
  "variants": var(), "relations": rel(["related:adult-gerontology-acute-care-nurse-practitioner"]), "job_listing_vote": YES},
 {"key": "adult-gerontology-acute-care-nurse-practitioner", "claims": full(),
  "variants": var(["Adult/Gerontology Acute Care Nurse Practitioner", "AG-ACNP"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "advanced-trauma-life-support", "claims": full(),
  "variants": var(["ATLS"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "american-board-of-medical-laboratory-immunology-certification", "claims": full(),
  "variants": var(["American Board Of Medical Laboratory Immunology (ABMLI) Certified", "ABMLI certification", "ABMLI", "ABMLI Certified"]),
  "relations": rel(), "job_listing_vote": YES},
 {"key": "american-board-of-medical-microbiology-certification", "claims": full(),
  "variants": var(["ABMM Certified", "ABMM certification", "ABMM"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "asq-certification", "claims": full(),
  "variants": var(["(American Society For Quality) ASQ Certified", "American Society for Quality certification", "ASQ certified"]),
  "relations": rel(), "job_listing_vote": YES},
 {"key": "certified-forensic-computer-examiner", "claims": full(),
  "variants": var(["Certified Forensic Computer Examination", "CFCE"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "certified-pediatric-emergency-nurse", "claims": full(),
  "variants": var(["CPEN"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "certified-professional-geologist", "claims": full(),
  "variants": var(["CPG"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "comptia-mobility", "claims": full(),
  "variants": var(), "relations": rel(), "job_listing_vote": YES},
 {"key": "cpc-coder",
  "claims": {"definition": C("Misleading: CPC is AAPC's medical (physician/outpatient) coding credential; bare 'coding' reads as software coding."),
             "kind": S},
  "variants": var(["CPC", "Certified Professional Coder (CPC)"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "cpc-collector",
  "claims": {"definition": U("Too vague to verify: presumably debt/accounts-receivable collection, but issuer is unnamed and I cannot confirm it."),
             "kind": S},
  "variants": var(["CPC", "Certified Professional Collector (CPC)"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "doctor-of-physical-therapy", "claims": full(),
  "variants": var(["DPT"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "doctor-of-public-health", "claims": full(),
  "variants": var(["DrPH"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "doubles-triples-endorsement", "claims": full(),
  "variants": var(["Doubles Endorsement"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "drone-pilot-certificate", "claims": full(),
  "variants": var(["Remote Pilot Certificate"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "iam-level-i-certification", "claims": full(),
  "variants": var(), "relations": rel(), "job_listing_vote": YES},
 {"key": "master-of-laws", "claims": full(),
  "variants": var(["LL.M."]), "relations": rel(), "job_listing_vote": YES},
 {"key": "master-of-laws-in-taxation", "claims": full(),
  "variants": var(["LL.M. in Taxation", "Master of Laws in Tax"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "master-s-certificate-in-project-management",
  "claims": full(defn=C("Often a non-credit executive/continuing-ed certificate (e.g. Schulich, Villanova), not a graduate-credit programme.")),
  "variants": var(["Masters Certificate In Project Management"]), "relations": rel(["related:project-management"]), "job_listing_vote": YES},
 {"key": "neonatal-resuscitation-program", "claims": full(),
  "variants": var(["Neonatal Resuscitation Programs", "NRP"]), "relations": rel(), "job_listing_vote": YES},
 {"key": "passenger-endorsement", "claims": full(),
  "variants": var(), "relations": rel(), "job_listing_vote": YES},
 {"key": "restricted-radiotelephone-operator-permit", "claims": full(),
  "variants": var(), "relations": rel(), "job_listing_vote": YES},
 {"key": "saca-certified-industry-4-0-associate-basic-operations", "claims": full(),
  "variants": var(["SACA Certified Industry 4.0 Associate Basic Operations"]), "relations": rel(), "job_listing_vote": YES},
]

# consistency checks against the packet
packet = json.load(open("/home/user/review/r1/out/packets/p001.json"))
entries = {e["key"]: e for e in packet["entries"]}
assert [a["key"] for a in answers] == [e["key"] for e in packet["entries"]]
claim_fields = ["definition", "kind", "certification", "certification_scope", "language_type"]
for a in answers:
    e = entries[a["key"]]
    assert set(a["claims"]) == {f for f in claim_fields if f in e}, a["key"]
    judged = a["variants"]["ok"] + [b["label"] for b in a["variants"]["bad"]]
    assert set(judged) <= set(e["variants"]), a["key"]
    rj = a["relations"]["ok"] + [b["rel"] for b in a["relations"]["bad"]]
    assert set(rj) <= set(e["relations"]), a["key"]
    for c in a["claims"].values():
        assert len(c.get("note", "")) <= 150, (a["key"], len(c["note"]))
        if c["verdict"] == "contradicts": assert c.get("note")

json.dump(answers, open("/home/user/review/r1/out/answers/p001.json", "w"), indent=1)
cnt = collections.Counter(c["verdict"] for a in answers for c in a["claims"].values())
print(dict(cnt), "variants ok/bad:", sum(len(a["variants"]["ok"]) for a in answers), sum(len(a["variants"]["bad"]) for a in answers))
