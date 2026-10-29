# Schemas and evidence

The schemas say what data goes with a skill and what counts as evidence for it. Evidence does not have to be gathered in one pass: a later pass, run somewhere else, can hand back records of the shape below and they attach to the entry by its id.

| File | Describes |
|---|---|
| `schemas/entry.schema.json` | Everything an entry can hold. |
| `schemas/evidence.schema.json` | One evidence record on one claim. |
| `schemas/certification.schema.json` | The certification fields: `certification`, `certification_scope`, and the optional `credential` block. |

A JSON Schema checks shape. Rules that look across an entry or across entries (every claim of a machine-drafted entry has a `drafted` record, a `reviewed` entry has a backing record for every claim, ids are unique, relation targets exist) are checked by `python3 -I tools/lexicon.py validate`. Both are drafts (v0). `tests/test_schema.py` checks every entry and evidence record in the repo against them, and needs the `jsonschema` package; everything else in the repo uses only the standard library.

## What is the provenance that this is a certification?

The claim is `certification: true` on an entry. Each piece of evidence for it is one record with `field: "certification"`.

| Evidence | Record | Backs the claim? |
|---|---|---|
| The issuing body's own page names it as a certification, certificate, licence or degree | `matched_source`, `by: source:<issuer>`, `kind: issuer`, `verification: page-read`, `ref`: the URL, `note`: a short quote, `date`: when it was read | Yes |
| A regulator or standards body lists it (FAA, FCC, a state licensing agency, the Department of Defense) | the same, with `kind: regulator` or `standard` | Yes |
| A Wikipedia or Wikidata record, matched against a downloaded dump | `matched_source`, `by: source:enwiki-<date>`, `kind: wikipedia`, `verification: dump-match`, `ref`, and `match`: dataset, record id, how it matched (title, redirect, acronym, category), and the categories or classes that show what kind of thing the record is | Yes, as corroboration. A page shows the credential is notable. A missing page shows nothing. |
| Only a search result was seen, the page was not opened | `matched_source` with `verification: search-results-only` | No. It is recorded and visible. |
| A person checked it | `checked`, `by: human:<name>`, `outcome: supports` or `contradicts` | Yes |
| A model drafted it | `drafted`, `by: model:<id>`, `note: basis: general-knowledge` | No |
| A model checked it, or a second draft agreed | `checked`, `by: model:<id>` | No. Two drafts by one model can share a mistake. |
| A legacy list or class says so | not evidence; recorded as `provenance.legacy_tag`, and a `flag` when it disagrees | No |

A record that finds the opposite uses `outcome: contradicts`. An unresolved contradiction blocks `reviewed`.

`certification_scope` is a second claim with its own records. The first thing a source shows for it is who awards the credential: one issuer, or many.

## The `credential` block

Facts found while checking: official name, acronym, type (certification, licence, endorsement, degree and so on), issuers, the field or fields of work (free text, or a code from ISCED-F 2013, SOC 2018 or O*NET-SOC), level, requirements, renewal, jurisdiction, the Wikipedia page, the Wikidata id, and a list of sources, each saying how much was verified. A checked single-issuer credential needs at least a type, one issuer and one source. The description is the entry's own `definition`.

Open in v0: the validator does not yet ask for evidence on each part of the `credential` block, only on the claims `certification` and `certification_scope`. The block is revised after the first 25 to 50 credentials are checked.

## Passes

| Pass | Where | State |
|---|---|---|
| Draft from the name alone | any model | done: 225 entries, batches 001 and 002 |
| Second blind draft, to find disagreement | any model | done once on the pilot; a disagreement says where to look, never backs a claim |
| Web search | cloud session | search results only, so cannot back a claim |
| Read the issuer's page | needs open network access | not done |
| Wikipedia and Wikidata dump | a cluster with disk, such as Discovery | not done, by design |
| O*NET, ESCO, SFIA import | a cluster or any machine | not done |
| Human review | people | not done |

### Handing back results from a pass run elsewhere

A pass reads the entries (id, `preferred_name`, `variants`, `kind`, `certification`, `certification_scope`), does its matching, and writes a JSON Lines file, one object per result:

```json
{"id": "a1b2c3d4e5", "evidence": {"field": "certification", "by": "source:enwiki-20261001", "action": "matched_source", "kind": "wikipedia", "verification": "dump-match", "outcome": "supports", "ref": "https://en.wikipedia.org/wiki/Advanced_trauma_life_support", "date": "2026-10-29", "run": "wikipedia-dump-1", "match": {"dataset": "enwiki-20261001", "dataset_id": "page_id:123", "method": "redirect", "categories": ["Trauma"]}}, "credential": {}}
```

`evidence` must conform to `schemas/evidence.schema.json`; `credential` is optional and conforms to the `credential` definition in `schemas/certification.schema.json`. A tool that applies such a file to the entries (checking the id exists, refusing to overwrite, validating the dictionary) is the next piece to write.

### Notes for a Wikipedia pass

- I have not checked the dump file names or formats, because this cloud session cannot reach Wikipedia. Check them on dumps.wikimedia.org before writing the job.
- Matching has to cope with redirects (an acronym often redirects to the article), disambiguation pages, and names that mean different things in different places. Record how each match was made, and keep a manual option.
- Wikipedia text is licensed CC BY-SA 4.0. Store ids, URLs, categories and a short quote (up to 200 characters), and write definitions in our own words. Do not copy article text into entries.
