import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402

P = {"source": "test", "date": "2026-10-27"}
_REAL = L.load()[0]


def eid(i):
    """A valid made-up id for a test entry."""
    return f"a{i:09d}"


def I(old):
    """The current id of a real entry, found by the id it had before ids became random."""
    return L.find(_REAL, old)["id"]


def entry(i, name, **kw):
    e = {"id": eid(i), "preferred_name": name, "kind": "skill", "definition": "d",
         "status": "proposed", "provenance": dict(P), "_file": f"{i}.json"}
    e.update(kw)
    return e


class Ids(unittest.TestCase):
    def test_new_ids_are_ten_characters_of_letters_and_digits(self):
        taken = set()
        for _ in range(500):
            i = L.new_id(taken)
            taken.add(i)
            self.assertRegex(i, r"^[a-z0-9]{10}$")
            self.assertTrue(i[0].isalpha() and any(c.isdigit() for c in i))     # starts with a letter, has a digit
        self.assertEqual(len(taken), 500)

    def test_new_id_avoids_taken_ids_in_any_case(self):
        self.assertNotIn("abc1234567", {L.new_id({"ABC1234567"}) for _ in range(50)})

    def test_bad_ids_are_rejected(self):
        for bad in ("skill:0001", "abcdefghij", "1abcdefghi", "ABCDEFGHI1", "abc123", "abcdefghi12"):
            self.assertTrue(any("must be 10" in m for m in L.validate([entry(1, "A", id=bad)])), bad)
        self.assertEqual(L.validate([entry(1, "A", id="a1b2c3d4e5")]), [])

    def test_find_matches_current_and_former_ids_ignoring_case(self):
        e = entry(1, "A", former_ids=["skill:0007"])
        self.assertIs(L.find([e], e["id"].upper()), e)
        self.assertIs(L.find([e], "SKILL:0007"), e)
        self.assertIsNone(L.find([e], "skill:0008"))

    def test_a_former_id_cannot_belong_to_two_entries(self):
        a, b = entry(1, "A", former_ids=["skill:0007"]), entry(2, "B", former_ids=["skill:0007"])
        self.assertTrue(any("former id" in m for m in L.validate([a, b])))


class DedupeIds(unittest.TestCase):
    def setUp(self):
        import importlib.util
        import json
        import tempfile
        spec = importlib.util.spec_from_file_location("dedupe_ids", Path(__file__).resolve().parent.parent / "scripts" / "dedupe_ids.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.json = json
        self.root = Path(tempfile.mkdtemp())
        (self.root / "entries").mkdir()

    def write(self, name, n, **kw):
        e = {k: v for k, v in entry(n, name, **kw).items() if k != "_file"}
        (self.root / "entries" / f"{name.lower()}.json").write_text(self.json.dumps(e))
        return e

    def read(self):
        return {p.stem: self.json.loads(p.read_text()) for p in (self.root / "entries").glob("*.json")}

    def test_second_duplicate_gets_a_new_id_and_the_first_keeps_it(self):
        a = self.write("A", 1)
        b = self.write("B", 1, relations=[{"type": "related", "target": eid(1)}])     # same id as A
        before = self.read()
        self.mod.main(["--root", str(self.root)])                                     # report only
        self.assertEqual(self.read(), before)
        self.mod.main(["--root", str(self.root), "--apply"])
        got = self.read()
        self.assertEqual(got["a"]["id"], a["id"])
        self.assertRegex(got["b"]["id"], L.ID_RE)
        self.assertNotEqual(got["b"]["id"], a["id"])
        self.assertEqual(got["b"]["relations"], b["relations"])                       # references are left for a person
        self.assertEqual(L.validate(L.load(self.root / "entries")[0]), [])

    def test_ids_that_differ_only_in_case_count_as_duplicates(self):
        a = self.write("A", 1)
        self.write("B", 2)
        b = self.read()["b"]
        b["id"] = a["id"].upper()
        (self.root / "entries" / "b.json").write_text(self.json.dumps(b))
        self.mod.main(["--root", str(self.root), "--apply"])
        self.assertNotEqual(L.norm_id(self.read()["b"]["id"]), L.norm_id(a["id"]))

    def test_nothing_to_do_when_ids_are_unique(self):
        self.write("A", 1)
        self.write("B", 2)
        before = self.read()
        self.mod.main(["--root", str(self.root), "--apply"])
        self.assertEqual(self.read(), before)


class CertificationScope(unittest.TestCase):
    def test_scope_needs_a_certification_and_an_allowed_value(self):
        self.assertEqual(L.validate([entry(1, "A", certification=True, certification_scope="many-issuers")]), [])
        self.assertTrue(any("certification_scope must be" in m for m in L.validate([entry(1, "A", certification=True, certification_scope="several")])))
        self.assertTrue(any("only applies" in m for m in L.validate([entry(1, "A", certification=False, certification_scope="single-issuer")])))
        self.assertTrue(any("only applies" in m for m in L.validate([entry(1, "A", certification_scope="single-issuer")])))

    def test_scope_is_a_claim_so_a_drafted_entry_needs_evidence_for_it(self):
        e = entry(1, "A", status="machine-drafted", certification=True, certification_scope="single-issuer", provenance=dict(P),
                  evidence=[{"field": k, "by": "model:m", "action": "drafted", "date": "2026-10-29"} for k in ("kind", "definition", "certification")])
        self.assertTrue(any("certification_scope" in m for m in L.validate([e])))


class Backing(unittest.TestCase):
    def test_what_backs_a_claim(self):
        src = {"action": "matched_source", "by": "source:enwiki-20261001", "outcome": "supports", "ref": "u", "date": "2026-10-29"}
        self.assertTrue(L.backs({**src, "verification": "page-read"}))
        self.assertTrue(L.backs({**src, "verification": "dump-match"}))
        self.assertFalse(L.backs({**src, "verification": "search-results-only"}))     # a search snippet is not a verified source
        self.assertFalse(L.backs(src))                                                # unstated verification does not back
        self.assertFalse(L.backs({**src, "verification": "page-read", "outcome": "contradicts"}))
        self.assertTrue(L.backs({"action": "checked", "by": "human:Bear", "outcome": "supports"}))
        self.assertFalse(L.backs({"action": "checked", "by": "model:m", "outcome": "supports"}))

    def test_a_matched_source_must_say_how_much_was_verified(self):
        e = entry(1, "A", evidence=[{"field": "kind", "by": "source:x", "action": "matched_source", "outcome": "supports",
                                     "ref": "u", "date": "2026-10-29"}])
        self.assertTrue(any("needs verification" in m for m in L.validate([e])))
        e["evidence"][0]["verification"] = "search-results-only"
        self.assertEqual(L.validate([e]), [])


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
        e = entry(1, "A", relations=[{"type": "broader", "target": eid(99)}, {"type": "related", "target": eid(1)},
                                      {"type": "sibling", "target": eid(1)}])
        m = " | ".join(L.validate([e]))
        self.assertIn("does not exist", m)
        self.assertIn("itself", m)
        self.assertIn("not one of", m)

    def test_loop_in_broader(self):
        a = entry(1, "A", relations=[{"type": "broader", "target": eid(2)}])
        b = entry(2, "B", relations=[{"type": "part_of", "target": eid(1)}])
        self.assertTrue(any("loop" in m for m in L.validate([a, b])))

    def test_reviewed_needs_reviewer_and_sources(self):
        e = entry(1, "A", status="reviewed", relations=[{"type": "related", "target": eid(2)}])
        m = " | ".join(L.validate([e, entry(2, "B")]))
        self.assertIn("reviewed_by", m)
        self.assertIn("no human check or matched source", m)

    def test_rolls_up_only_on_up_relations(self):
        e = entry(1, "A", relations=[{"type": "related", "target": eid(2), "rolls_up": True}])
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
                         ev("definition", "source:onet", "matched_source", "supports", ref="https://example.org/x", verification="page-read")])
        self.assertEqual(L.validate([good]), [])
        bad = reviewed([ev("kind", "human:Bear", "checked", "supports"),
                        ev("definition", "source:onet", "matched_source", "supports", verification="page-read")])
        self.assertTrue(any("needs a ref" in m for m in L.validate([bad])))

    def test_a_match_seen_only_in_search_results_does_not_make_an_entry_reviewable(self):
        e = reviewed([ev("kind", "human:Bear", "checked", "supports"),
                      ev("definition", "source:web", "matched_source", "supports", ref="https://example.org/x", verification="search-results-only")])
        self.assertTrue(any("no human check or matched source for definition" in m for m in L.validate([e])))

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
        self.assertEqual([c["id"] for c in self.idx["variants"]["postgres"]], [I("skill:0082")])

    def test_pg_needs_context_and_is_case_sensitive(self):
        c = self.idx["variants"]["pg"][0]
        self.assertEqual((c["match"], c["needs_context"]), ("exact_case", ["database"]))

    def test_cpc_is_ambiguous_between_two_concepts(self):
        c = self.idx["variants"]["cpc"]
        self.assertEqual(len(c), 2)
        self.assertTrue(all(x["ambiguous"] for x in c))

    def test_rollup_follows_only_marked_edges(self):
        self.assertEqual(L.rollup(self.entries, I("skill:0082")), [I("skill:0046")])   # PostgreSQL -> SQL
        self.assertEqual(L.rollup(self.entries, I("skill:0083")), [])               # PL/pgSQL -> nothing

    def test_inverse_relations_are_derived(self):
        types = {(r["type"], r["target"]) for r in self.idx["relations"][I("skill:0082")]}
        self.assertIn(("has_part", I("skill:0083")), types)
        sql = {(r["type"], r["target"]) for r in self.idx["relations"][I("skill:0046")]}
        self.assertIn(("narrower", I("skill:0082")), sql)
        self.assertIn(("contrast", I("skill:0084")), sql)   # stored once on NoSQL, visible from SQL

    def test_deprecated_entries_are_not_matched(self):
        a = entry(1, "Old", status="deprecated", replacements=[eid(2)])
        self.assertNotIn("old", L.build_index([a, entry(2, "New")])["variants"])


if __name__ == "__main__":
    unittest.main()
