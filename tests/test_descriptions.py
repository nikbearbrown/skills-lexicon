import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import lexicon as L  # noqa: E402

spec = importlib.util.spec_from_file_location("descriptions", ROOT / "scripts" / "wikipedia_match" / "descriptions.py")
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)


def entry(i, key, name, kind="tool"):
    return {"id": i, "key": key, "preferred_name": name, "kind": kind, "definition": "A thing we wrote.", "status": "proposed",
            "provenance": {"source": "test", "date": "2026-10-31"}}


class Descriptions(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "entries").mkdir()
        (self.d / "data").mkdir()
        shutil.copy(ROOT / "data" / "runs.json", self.d / "data" / "runs.json")
        for e in (entry("aaaaaaaaa1", "git", "Git"), entry("aaaaaaaaa2", "mercury", "Mercury", "knowledge"), entry("aaaaaaaaa3", "jira", "Jira")):
            (self.d / "entries" / (e["key"] + ".json")).write_text(json.dumps(e))
        self.w = self.d / "wiki" / "20261001"
        self.w.mkdir(parents=True)
        pages = {1: ("Git", 111), 2: ("Mercury (planet)", 222), 3: ("Jira (software)", 333)}
        (self.w / "candidates.jsonl").write_text("\n".join(json.dumps({"page_id": k, "title": t, "rev_id": r, "rev_timestamp": "2026-09-30T00:00:00Z", "lead": "Lead of " + t + ".", "disambiguation": False}) for k, (t, r) in pages.items()))
        (self.w / "categories.jsonl").write_text("\n".join(json.dumps({"page_id": k, "title": t, "categories": ["Version control"]}) for k, (t, r) in pages.items()))
        rows = [{"entry_id": "aaaaaaaaa1", "entry_key": "git", "relation": "same", "page": {"page_id": 1, "title": "Git", "basis": "exact-title"}},
                {"entry_id": "aaaaaaaaa2", "entry_key": "mercury", "relation": "same", "page": {"page_id": 2, "title": "Mercury (planet)", "basis": "title-minus-qualifier"}},
                {"entry_id": "aaaaaaaaa3", "entry_key": "jira", "relation": "related", "page": {"page_id": 3, "title": "Jira (software)", "basis": "redirect"}}]
        (self.w / "resolved.jsonl").write_text("\n".join(json.dumps(r) for r in rows))
        self.out = self.d / "out"

    def answers(self, rows):
        (self.out / "answers").mkdir(parents=True, exist_ok=True)
        (self.out / "answers" / "p001.json").write_text(json.dumps(rows))

    def load(self):
        es, _ = L.load(self.d / "entries")
        return {e["key"]: e for e in es}

    def test_packets_hold_only_same_relation_entries(self):
        D.packets(str(self.d), str(self.out), 10, str(self.w))
        items = json.loads((self.out / "packets" / "p001.json").read_text())["items"]
        self.assertEqual(sorted(i["key"] for i in items), ["git", "mercury"])          # jira is only related

    def test_rewrite_records_text_source_and_evidence_and_skips_wrong_subject(self):
        D.packets(str(self.d), str(self.out), 10, str(self.w))
        self.answers([{"key": "git", "verdict": "ok", "description": "A system that tracks changes to files."},
                      {"key": "mercury", "verdict": "wrong-subject", "note": "the lead is about the planet"}])
        log = D.apply(str(self.d), str(self.out), "rewrite", "claude-sonnet-5-5", "xhigh", "2026-10-31-desc-a", "2026-10-31", str(self.w))
        es = self.load()
        g = es["git"]
        self.assertEqual(g["description"]["source"]["url"], "https://en.wikipedia.org/w/index.php?title=Git&oldid=111")
        self.assertEqual({(v["action"], v["field"]) for v in g["evidence"]}, {("drafted", "description"), ("matched_source", "description")})
        self.assertTrue(any(L.backs(v) for v in g["evidence"]))                          # a dump match backs the claim
        self.assertNotIn("description", es["mercury"])
        self.assertEqual(log["ok"], 1)
        self.assertEqual(json.loads((self.w / "description-skipped.jsonl").read_text().splitlines()[0])["verdict"], "wrong-subject")
        self.assertEqual(L.validate(list(es.values())) + L.check_runs(list(es.values()), L.load_runs(self.d)), [])
        self.assertEqual(L.load_runs(self.d)["2026-10-31-desc-a"]["model"], "claude-sonnet-5-5")

    def test_check_never_backs_and_nothing_is_overwritten(self):
        self.answers([{"key": "git", "verdict": "ok", "description": "A system that tracks changes to files."}])
        D.apply(str(self.d), str(self.out), "rewrite", "claude-sonnet-5-5", "xhigh", "run-a", "2026-10-31", str(self.w))
        self.answers([{"key": "git", "verdict": "ok", "description": "Something else entirely."}])
        D.apply(str(self.d), str(self.out), "rewrite", "claude-sonnet-5-5", "xhigh", "run-b", "2026-10-31", str(self.w))
        self.assertEqual(self.load()["git"]["description"]["text"], "A system that tracks changes to files.")
        self.answers([{"key": "git", "verdict": "adds-information", "note": "mentions a vendor not in the lead"}])
        D.apply(str(self.d), str(self.out), "check", "claude-opus-5-5", "xhigh", "run-c", "2026-10-31", str(self.w))
        ev = [v for v in self.load()["git"]["evidence"] if v["action"] == "checked"]
        self.assertEqual((ev[0]["outcome"], ev[0]["by"]), ("contradicts", "model:claude-opus-5-5"))
        self.assertFalse(L.backs(ev[0]))

    def test_prune_removes_only_wrong_subject_descriptions_and_keeps_the_record(self):
        self.answers([{"key": "git", "verdict": "ok", "description": "A system that tracks changes to files."}, {"key": "mercury", "verdict": "ok", "description": "A planet."}])
        D.apply(str(self.d), str(self.out), "rewrite", "claude-sonnet-5-5", "xhigh", "run-a", "2026-10-31", str(self.w))
        self.answers([{"key": "git", "verdict": "wrong-subject", "note": "the lead is about the company"}, {"key": "mercury", "verdict": "changes-meaning", "note": "tense"}])
        D.apply(str(self.d), str(self.out), "check", "claude-opus-5-5", "xhigh", "run-c", "2026-10-31", str(self.w))
        self.assertEqual(D.prune(str(self.d), str(self.w), "2026-10-31"), 1)
        es = self.load()
        self.assertNotIn("description", es["git"])
        self.assertIn("description", es["mercury"])                                     # a wording problem is flagged, not removed
        row = json.loads((self.w / "description-skipped.jsonl").read_text().splitlines()[-1])
        self.assertEqual((row["entry_key"], len(row["evidence"])), ("git", 3))
        self.assertEqual(L.validate(list(es.values())), [])

    def test_validator_rejects_a_description_without_its_source_evidence_or_licence(self):
        e = entry("aaaaaaaaa9", "x", "X")
        e["_file"] = "x.json"
        src = {"name": "English Wikipedia", "title": "X", "page_id": 1, "rev_id": 5, "rev_timestamp": "t", "dump": "20261001",
               "url": "https://en.wikipedia.org/w/index.php?title=X&oldid=5", "licence": "CC BY-SA 4.0", "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/"}
        e["description"] = {"text": "Words.", "adapted": True, "source": dict(src)}
        errs = []
        L.check_description(e, errs)
        self.assertTrue(any("matched_source" in m for m in errs))
        e["evidence"] = [{"field": "description", "by": "source:wikipedia", "action": "matched_source", "ref": src["url"], "outcome": "supports", "date": "d",
                          "verification": "dump-match", "organization": {"name": "W", "url": "https://en.wikipedia.org/"}}]
        errs = []
        L.check_description(e, errs)
        self.assertEqual(errs, [])
        e["description"]["source"]["licence"] = "MIT"
        e["description"]["adapted"] = False
        errs = []
        L.check_description(e, errs)
        self.assertEqual(len(errs), 2)


if __name__ == "__main__":
    unittest.main()
