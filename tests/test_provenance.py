import csv
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
import assess as AS  # noqa: E402
import crosscheck as X  # noqa: E402
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402
import make_requests as M  # noqa: E402
import tags_to_candidates as T  # noqa: E402
import test_pipeline as TP  # noqa: E402


def tag_root(tag="Frobnicate Cert", answer=None, run="run-a", model="m1", effort="high", classes=("Skill",)):
    """A temp folder with the real entries, a tag list that has `tag` on line 7, and one tag drafted from it."""
    root = TP.temp_root()
    (root / "data").mkdir()
    shutil.copy(ROOT / "data" / "runs.json", root / "data" / "runs.json")
    for name in [T.TAGS] + list(T.LISTS.values()):
        with open(root / name, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Tag", "Class"])
            if name == T.TAGS:
                for i in range(5):
                    w.writerow([f"Filler {i}", "Skill"])
                w.writerow([tag, classes[0]])
    work = root / "work"
    entries, _ = L.load(root / "entries")
    cand = {"term": tag, "n_postings": 0, "quotes": [],
            "origin": {"sources": [{"file": T.TAGS, "rows": [7], "class": classes[0]}], "class": classes[0], "in_lists": []}}
    (work / "requests").mkdir(parents=True)
    (work / "responses").mkdir()
    for name, req in M.make([cand], entries, 0).items():
        (work / "requests" / name).write_text(json.dumps(req))
        (work / "responses" / name).write_text(json.dumps(answer or TP.tag_answer(kind="tool")))
    I.ingest(work, root, "model:" + model, run, "2026-10-29", effort=effort, agent="subagent")
    return root


class Runs(unittest.TestCase):
    def test_register_and_refuse_a_conflict(self):
        root = Path(tempfile.mkdtemp())
        L.register_run(root, "r1", "m1", "xhigh", "subagent", date="2026-10-29")
        L.register_run(root, "r1", "m1", "xhigh")                       # same again is fine, and keeps what is recorded
        self.assertEqual(L.load_runs(root)["r1"]["agent"], "subagent")
        self.assertEqual(L.load_runs(root)["r1"]["date"], "2026-10-29")
        with self.assertRaises(ValueError):
            L.register_run(root, "r1", "m1", "low")
        with self.assertRaises(ValueError):
            L.register_run(root, "r2", "m1", "extra")

    def test_a_model_run_must_be_registered_and_match(self):
        e = {"_file": "a.json", "evidence": [{"field": "kind", "by": "model:m1", "action": "drafted", "date": "d", "run": "r1"}]}
        self.assertTrue(L.check_runs([e], {}))
        self.assertTrue(L.check_runs([e], {"r1": {"model": "other", "effort": "high"}}))
        self.assertEqual(L.check_runs([e], {"r1": {"model": "m1", "effort": "high"}}), [])

    def test_the_real_repo_registers_every_run(self):
        entries, _ = L.load()
        self.assertEqual(L.check_runs(entries, L.load_runs()), [])


class Votes(unittest.TestCase):
    def test_ingest_records_the_run_and_a_vote_per_tag(self):
        root = tag_root()
        self.assertEqual(L.load_runs(root)["run-a"]["effort"], "high")
        v = AS.load(root)
        self.assertEqual(len(v), 1)
        self.assertEqual((v[0]["answer"], v[0]["assessor"]), ("yes", {"type": "model", "model": "m1", "effort": "high"}))
        self.assertTrue(v[0]["entry"])

    def test_no_and_unsure_votes_carry_the_reason(self):
        root = tag_root(answer={"decision": "not_a_skill", "variant_of": None, "reason": "A UI part.", "entry": None})
        v = AS.load(root)[0]
        self.assertEqual((v["answer"], v["reason"]), ("no", "A UI part."))

    def test_the_same_assessor_cannot_vote_twice_in_a_run(self):
        root = tag_root()
        with self.assertRaises(ValueError):
            AS.append(root, [AS.vote("Frobnicate Cert", "no", AS.model_assessor("m1", "high"), "run-a", "2026-10-29")])
        AS.append(root, [AS.vote("Frobnicate Cert", "no", AS.model_assessor("m2", "low"), "run-b", "2026-10-30", reason="x")])   # another model is fine
        AS.append(root, [AS.vote("Frobnicate Cert", "yes", AS.human_assessor("Bear"), "human-1", "2026-10-30")])

    def test_the_legacy_list_counts_as_one_yes_and_votes_can_split(self):
        root = tag_root()
        AS.append(root, [AS.vote("Frobnicate Cert", "no", AS.model_assessor("m2", "low"), "run-b", "2026-10-30", reason="x")])
        t = AS.tally(root)["frobnicate cert"]
        s = AS.summary(t["votes"])
        self.assertEqual(s["yes"], ["legacy tag lists", "m1 (high)"])
        self.assertEqual(s["no"], ["m2 (low)"])
        self.assertTrue(AS.split(t["votes"]))

    def test_cli_adds_a_human_vote_and_a_model_vote_needs_effort_and_run(self):
        root = tag_root()
        AS.main(["add", "Frobnicate Cert", "yes", "--human", "Bear", "--root", str(root), "--date", "2026-10-30"])
        self.assertEqual(AS.load(root)[-1]["assessor"], {"type": "human", "name": "Bear"})
        with self.assertRaises(SystemExit):
            AS.main(["add", "Frobnicate Cert", "no", "--model", "m3", "--root", str(root)])
        AS.main(["add", "Frobnicate Cert", "unsure", "--model", "m3", "--effort", "max", "--run", "run-c", "--reason", "r", "--root", str(root)])
        self.assertEqual(L.load_runs(root)["run-c"]["effort"], "max")


class Crosscheck(unittest.TestCase):
    def test_a_second_draft_is_recorded_as_checks_that_never_back(self):
        a = tag_root(answer=TP.tag_answer(kind="tool", certification={"value": False, "basis": "general-knowledge"}), run="run-a", model="m1")
        b = tag_root(answer=TP.tag_answer(kind="platform", certification={"value": False, "basis": "general-knowledge"}), run="run-b", model="m2", effort="low")
        L.register_run(a, "run-b", "m2", "low", "subagent")
        entries, log = X.crosscheck(a, "run-a", b, "run-b", "m2", "low", "2026-10-30")
        got = {(f, o) for _, f, o in log}
        self.assertEqual(got, {("kind", "contradicts"), ("certification", "supports")})
        e = next(x for x in entries if x["key"] == "frobnicate-cert")
        rec = next(v for v in e["evidence"] if v["field"] == "kind" and v["action"] == "checked")
        self.assertEqual((rec["by"], rec["run"]), ("model:m2", "run-b"))
        self.assertIn("platform", rec["note"])
        self.assertFalse(any(L.backs(v) for v in e["evidence"] if v["action"] == "checked"))
        self.assertEqual(L.validate(entries) + L.check_runs(entries, L.load_runs(a)), [])

    def test_old_kind_words_are_mapped_before_comparing(self):
        a = tag_root(answer=TP.tag_answer(kind="credential"), run="run-a")
        b = tag_root(answer=TP.tag_answer(kind="credential"), run="run-b", model="m2")
        # the second draft used a word the kind list no longer has
        p = b / "entries" / "frobnicate-cert.json"
        d = json.loads(p.read_text())
        d["kind"] = "clearance"
        p.write_text(json.dumps(d))
        L.register_run(a, "run-b", "m2", "high")
        _, log = X.crosscheck(a, "run-a", b, "run-b", "m2", "high", "2026-10-30")
        self.assertEqual([(f, o) for _, f, o in log if f == "kind"], [("kind", "supports")])


class Classes(unittest.TestCase):
    def test_the_four_way_split_comes_from_kind(self):
        for kind, cls in (("ability", "ability"), ("credential", "certification"), ("programming-language", "language"),
                          ("human-language", "language"), ("markup-language", "language"), ("tool", "skill"),
                          ("knowledge", "skill"), ("method", "skill"), ("standard", "skill"), ("skill", "skill")):
            self.assertEqual(L.top_class({"kind": kind}), cls, kind)

    def test_every_allowed_kind_has_a_class(self):
        self.assertTrue({L.top_class({"kind": k}) for k in L.KINDS} <= {"ability", "certification", "language", "skill"})

    def test_the_o_net_abilities_are_abilities_and_backed_by_o_net(self):
        entries, _ = L.load()
        ab = [e for e in entries if any(i["scheme"] == "onet-element" for i in e.get("identifiers", []))]
        self.assertEqual(len(ab), 52)
        for e in ab:
            self.assertEqual(L.top_class(e), "ability")
            self.assertTrue(any(L.backs(v) and v["field"] == "kind" and v["organization"]["url"].startswith("https://www.onetcenter.org") for v in e["evidence"]))


class WebCheck(unittest.TestCase):
    def test_a_search_only_check_is_recorded_but_backs_nothing(self):
        spec = importlib.util.spec_from_file_location("apply_web_check", ROOT / "scripts" / "apply_web_check.py")
        W = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(W)
        root = tag_root(answer=TP.tag_answer(certification={"value": True, "basis": "general-knowledge"},
                                             certification_scope={"value": "single-issuer", "basis": "general-knowledge"}))
        findings = [{"input_name": "Frobnicate Cert", "verdict": "real", "official_name": "Frobnicate Certified", "acronym": "FC",
                     "issuer": {"name": "Frob Institute", "type": "professional-body", "country": "United States"},
                     "official_url": "https://frob.example/cert/fc", "wikipedia_url": None, "supporting_snippet": "FC is awarded by the Frob Institute.",
                     "credential_type": "certification", "field": ["frobnication"], "level": "professional", "requirements": "An exam.",
                     "jurisdiction": "United States", "draft_definition_check": {"result": "supports", "note": "Matches."}, "other_sources": []}]
        fp = root / "findings.json"
        fp.write_text(json.dumps(findings))
        W.main([str(fp), "--run", "web-1", "--model-id", "m9", "--effort", "xhigh", "--root", str(root)])
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        src = next(v for v in e["evidence"] if v["action"] == "matched_source")
        self.assertEqual((src["verification"], src["organization"]["url"]), ("search-results-only", "https://frob.example/"))
        self.assertFalse(L.backs(src))
        self.assertEqual(e["credential"]["issuers"][0]["name"], "Frob Institute")
        self.assertEqual(L.validate(L.load(root / "entries")[0]), [])
        entries, _ = L.load(root / "entries")
        self.assertEqual(L.check_runs(entries, L.load_runs(root)), [])



class CheckClaims(unittest.TestCase):
    def setUp(self):
        import check_claims as CC
        self.CC = CC
        self.root = tag_root(answer=TP.tag_answer(kind="tool", certification={"value": False, "basis": "general-knowledge"},
                                                   variants=[{"label": "FC", "basis": "general-knowledge"}]))
        self.out = self.root / "review"

    def answer(self, a):
        self.CC.packets(self.root, self.out, 10, classes=["skill"])
        (self.out / "answers" / "p001.json").write_text(json.dumps(a))

    def run_apply(self, dry=False):
        entries, touched, votes, log, problems = self.CC.apply(self.root, self.out, "rev-model", "max", "review-1", "2026-10-30")
        return entries, touched, votes, log, problems

    def test_packets_skip_o_net_and_hold_slim_views(self):
        self.CC.packets(self.root, self.out, 10)
        p = json.loads((self.out / "packets" / "p001.json").read_text())
        self.assertIn("allowed_kinds", p)
        self.assertTrue(all(e["key"] for e in p["entries"]))
        self.assertTrue((self.out / "BRIEF.txt").exists())

    def test_verdicts_become_checks_and_unsure_records_nothing(self):
        self.answer([{"key": "frobnicate-cert", "claims": {"definition": {"verdict": "supports"}, "kind": {"verdict": "contradicts", "note": "it is a method"},
                                                         "certification": {"verdict": "unsure"}},
                      "variants": {"ok": ["FC"]}, "job_listing_vote": {"answer": "unsure", "reason": "unclear"}}])
        entries, touched, votes, log, problems = self.run_apply()
        e = next(x for x in entries if x["key"] == "frobnicate-cert")
        checks = {(v["field"], v["outcome"]) for v in e["evidence"] if v["action"] == "checked" and v["run"] == "review-1"}
        self.assertEqual(checks, {("definition", "supports"), ("kind", "contradicts"), ("variant:fc", "supports")})
        self.assertEqual((log["unsure"], len(votes), problems), (1, 1, []))
        self.assertEqual(votes[0]["assessor"], {"type": "model", "model": "rev-model", "effort": "max"})
        self.assertFalse(any(L.backs(v) for v in e["evidence"] if v["action"] == "checked"))
        L.register_run(self.root, "review-1", "rev-model", "max")
        self.assertEqual(L.validate(entries) + L.check_runs(entries, L.load_runs(self.root)), [])

    def test_a_claim_the_entry_does_not_have_is_skipped_and_unknown_entries_are_reported(self):
        self.answer([{"key": "frobnicate-cert", "claims": {"language_type": {"verdict": "supports"}}},
                     {"key": "no-such-entry", "claims": {}}])
        _, _, _, log, problems = self.run_apply()
        self.assertEqual(log["skipped"], 1)
        self.assertEqual(len(problems), 1)

    def test_the_same_run_does_not_record_twice(self):
        a = [{"key": "frobnicate-cert", "claims": {"definition": {"verdict": "supports"}}}]
        self.answer(a)
        entries, *_ = self.run_apply()
        e = next(x for x in entries if x["key"] == "frobnicate-cert")
        n = len(e["evidence"])
        self.CC.apply(self.root, self.out, "rev-model", "max", "review-1", "2026-10-30")      # in memory again: still one record per claim
        self.assertEqual(sum(1 for v in e["evidence"] if v["run"] == "review-1"), 1)
        self.assertEqual(len(e["evidence"]), n)


if __name__ == "__main__":
    unittest.main()
