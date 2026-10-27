import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402

P = {"source": "test", "date": "2026-10-27"}


def entry(i, name, **kw):
    e = {"id": f"skill:{i:04d}", "preferred_name": name, "kind": "skill", "definition": "d",
         "status": "proposed", "provenance": dict(P), "_file": f"{i}.json"}
    e.update(kw)
    return e


class Validate(unittest.TestCase):
    def test_real_entries_are_clean(self):
        entries, errs = L.load()
        self.assertEqual(errs + L.validate(entries), [])
        self.assertGreaterEqual(len(entries), 84)

    def test_duplicate_id(self):
        self.assertTrue(any("also used" in m for m in L.validate([entry(1, "A"), entry(1, "B")])))

    def test_shared_label_without_context_is_an_error(self):
        a, b = entry(1, "Swift"), entry(2, "SWIFT network", variants=[{"label": "swift"}])
        self.assertTrue(any("claimed by" in m for m in L.validate([a, b])))

    def test_shared_label_ok_when_contexts_differ(self):
        a = entry(1, "Swift", needs_context=["software"])
        b = entry(2, "SWIFT network", variants=[{"label": "Swift", "needs_context": ["finance"]}])
        self.assertEqual(L.validate([a, b]), [])

    def test_shared_label_ok_when_both_say_ambiguous(self):
        a = entry(1, "CPC", name_ambiguous=True)
        b = entry(2, "Coder", variants=[{"label": "cpc", "ambiguous": True}])
        self.assertEqual(L.validate([a, b]), [])

    def test_same_label_twice_in_one_entry(self):
        self.assertTrue(any("listed twice" in m for m in L.validate([entry(1, "Python", variants=[{"label": "python"}])])))

    def test_missing_target_self_relation_and_bad_type(self):
        e = entry(1, "A", relations=[{"type": "broader", "target": "skill:0099"}, {"type": "related", "target": "skill:0001"},
                                      {"type": "sibling", "target": "skill:0001"}])
        m = " | ".join(L.validate([e]))
        self.assertIn("does not exist", m)
        self.assertIn("itself", m)
        self.assertIn("not one of", m)

    def test_loop_in_broader(self):
        a = entry(1, "A", relations=[{"type": "broader", "target": "skill:0002"}])
        b = entry(2, "B", relations=[{"type": "part_of", "target": "skill:0001"}])
        self.assertTrue(any("loop" in m for m in L.validate([a, b])))

    def test_reviewed_needs_reviewer_and_sources(self):
        e = entry(1, "A", status="reviewed", relations=[{"type": "related", "target": "skill:0002"}])
        m = " | ".join(L.validate([e, entry(2, "B")]))
        self.assertIn("reviewed_by", m)
        self.assertIn("no human check or matched source", m)

    def test_rolls_up_only_on_up_relations(self):
        e = entry(1, "A", relations=[{"type": "related", "target": "skill:0002", "rolls_up": True}])
        self.assertTrue(any("rolls_up only" in m for m in L.validate([e, entry(2, "B")])))

    def test_deprecated_needs_replacement(self):
        self.assertTrue(any("replacements" in m for m in L.validate([entry(1, "A", status="deprecated")])))


def ev(field, by, action, outcome=None, **kw):
    d = {"field": field, "by": by, "action": action, "date": "2026-10-27"}
    if outcome:
        d["outcome"] = outcome
    d.update(kw)
    return d


def reviewed(evidence):
    e = entry(1, "A", status="reviewed", provenance={**P, "reviewed_by": "human:Bear"})
    e["evidence"] = evidence
    return e


class Evidence(unittest.TestCase):
    full = [("kind",), ("definition",)]

    def test_human_checks_make_an_entry_reviewable(self):
        e = reviewed([ev(k, "human:Bear", "checked", "supports") for k in ("kind", "definition")])
        self.assertEqual(L.validate([e]), [])

    def test_a_matched_source_counts_but_needs_a_ref(self):
        good = reviewed([ev("kind", "human:Bear", "checked", "supports"),
                         ev("definition", "source:onet", "matched_source", "supports", ref="https://example.org/x")])
        self.assertEqual(L.validate([good]), [])
        bad = reviewed([ev("kind", "human:Bear", "checked", "supports"),
                        ev("definition", "source:onet", "matched_source", "supports")])
        self.assertTrue(any("needs a ref" in m for m in L.validate([bad])))

    def test_models_agreeing_never_make_an_entry_reviewed(self):
        e = reviewed([ev(k, f"model:{m}", "checked", "supports") for k in ("kind", "definition")
                      for m in ("claude-sonnet-5-5", "other-model")])
        self.assertTrue(any("no human check or matched source" in m for m in L.validate([e])))

    def test_unresolved_contradiction_blocks_review(self):
        e = reviewed([ev(k, "human:Bear", "checked", "supports") for k in ("kind", "definition")]
                     + [ev("definition", "human:Ana", "checked", "contradicts")])
        self.assertTrue(any("contradicting" in m for m in L.validate([e])))

    def test_evidence_must_point_at_a_real_claim(self):
        e = entry(1, "A", evidence=[ev("variant:ghost", "model:x", "drafted")])
        self.assertTrue(any("not a claim" in m for m in L.validate([e])))

    def test_machine_drafted_needs_drafting_evidence_for_every_claim(self):
        e = entry(1, "A", status="machine-drafted", evidence=[ev("kind", "model:x", "drafted")])
        self.assertTrue(any("no 'drafted' evidence for definition" in m for m in L.validate([e])))

    def test_who_and_what_are_checked(self):
        e = entry(1, "A", evidence=[ev("kind", "somebody", "checked"), ev("definition", "model:x", "guessed")])
        m = " | ".join(L.validate([e]))
        self.assertIn("'by' must look like", m)
        self.assertIn("action must be one of", m)
        self.assertIn("needs outcome", m)

    def test_a_source_cannot_draft(self):
        e = entry(1, "A", evidence=[ev("kind", "source:onet", "drafted")])
        self.assertTrue(any("cannot draft" in m for m in L.validate([e])))


class Index(unittest.TestCase):
    def setUp(self):
        self.entries, _ = L.load()
        self.idx = L.build_index(self.entries)

    def test_postgres_resolves_to_postgresql(self):
        self.assertEqual([c["id"] for c in self.idx["variants"]["postgres"]], ["skill:0082"])

    def test_pg_needs_context_and_is_case_sensitive(self):
        c = self.idx["variants"]["pg"][0]
        self.assertEqual((c["match"], c["needs_context"]), ("exact_case", ["database"]))

    def test_cpc_is_ambiguous_between_two_concepts(self):
        c = self.idx["variants"]["cpc"]
        self.assertEqual(len(c), 2)
        self.assertTrue(all(x["ambiguous"] for x in c))

    def test_rollup_follows_only_marked_edges(self):
        self.assertEqual(L.rollup(self.entries, "skill:0082"), ["skill:0046"])   # PostgreSQL -> SQL
        self.assertEqual(L.rollup(self.entries, "skill:0083"), [])               # PL/pgSQL -> nothing

    def test_inverse_relations_are_derived(self):
        types = {(r["type"], r["target"]) for r in self.idx["relations"]["skill:0082"]}
        self.assertIn(("has_part", "skill:0083"), types)
        sql = {(r["type"], r["target"]) for r in self.idx["relations"]["skill:0046"]}
        self.assertIn(("narrower", "skill:0082"), sql)
        self.assertIn(("contrast", "skill:0084"), sql)   # stored once on NoSQL, visible from SQL

    def test_deprecated_entries_are_not_matched(self):
        a = entry(1, "Old", status="deprecated", replacements=["skill:0002"])
        self.assertNotIn("old", L.build_index([a, entry(2, "New")])["variants"])


if __name__ == "__main__":
    unittest.main()
