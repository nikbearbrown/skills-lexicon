# Schemas and evidence

The lexicon does not decide that something is a skill, an ability, a certification or a language. It gathers **evidence** that it is, and evidence against, with who gave it and how much was checked. Later passes decide what to keep. A value on an entry (`kind`, `certification`, `language_type`) is the current hypothesis of the pass that drafted it, and the `evidence` list says why anyone should believe it. `status: reviewed` is a decision, and only a named person makes it.

## What is in the lexicon, and the four classes

The test for being in the lexicon is that **job listings ask for it**. What they ask for falls into four classes:

| Class | What it is | Basis |
|---|---|---|
| **ability** | An enduring attribute a person has: Oral Comprehension, Spatial Orientation. | O*NET's 52 Abilities (`abilities/`). O*NET may miss some abilities job listings ask for; those are drafted like anything else and lack the O*NET match. |
| **certification** | A credential attested by an official organization: a certification, certificate, licence, permit, endorsement, degree or clearance. | The attestation: the organization's **name** and a **link** to it. |
| **language** | A programming language, a spoken (human) language, or another formal language such as a markup or query language. | `language_type`: `programming`, `spoken`, `other`. |
| **skill** | Whatever is left: something job listings ask for that is not an ability, a certification or a language. Tools, platforms, methods and knowledge areas fall here. | Evidence that listings ask for it (below). |

The class is worked out from `kind` and never stored (`lexicon.top_class`): `ability` is an ability, `credential` a certification, the five language kinds a language, and every other kind a skill. `kind` stays finer than the class and comes from a fixed list, which keeps the O*NET split: `ability`, `skill`, `knowledge`, `work-activity`, then named technology (`tool`, `platform`, `framework`, `library`), the language kinds, `method`, `standard`, `credential`.

A caveat on "whatever is left": it is a residual class, so it grows as other classes are carved out, and it holds quite different things. That is why `kind` is kept underneath it. O*NET's own definitions are tighter (Skills are developed capacities such as Critical Thinking; Knowledge is an organised body of facts) and can be used to split the residue once the O*NET Skills, Knowledge and Technology Skills lists are loaded.

## The schemas

| File | Describes |
|---|---|
| `schemas/entry.schema.json` | Everything an entry can hold. |
| `schemas/evidence.schema.json` | One evidence record on one claim. |
| `schemas/certification.schema.json` | The certification fields: `certification`, `certification_scope`, and the optional `credential` block. |
| `schemas/assessment.schema.json` | One vote on one tag (a line of `data/assessments.jsonl`). |
| `schemas/run.schema.json` | `data/runs.json`: which model, at which effort, made each run. |

A JSON Schema checks shape. Rules across an entry or across entries (every claim of a machine-drafted entry has a `drafted` record, a `reviewed` entry has a backing record for every claim, ids are unique, relation targets exist, every model run is registered) are checked by `python3 -I tools/lexicon.py validate`. All are drafts (v0). `tests/test_schema.py` checks every entry, evidence record, vote and run in the repo against them and needs the `jsonschema` package; the rest of the repo uses only the standard library.

## Who said it: runs, models and effort

Every draft, check and vote by a model names a **run**, and `data/runs.json` records for each run the model, the effort level it ran at (`low` to `max`; `xhigh` is "extra high"), and whether it was the main session or a subagent. The operator supplies these; a model's own statement of who it is is never used. For the three subagents here, the model and effort were read from each subagent's transcript. Another model that checks the work records its own model and effort the same way (`tools/assess.py add`, `tools/crosscheck.py`).

## Votes: does anyone think this tag is something job listings ask for?

`data/assessments.jsonl` holds one line per vote on a tag: `yes`, `no` or `unsure`, who gave it (a person, or a model with its effort), the run, the date, and a reason for `no` and `unsure`. Any number of people and models can vote on one tag. A tag listed in a legacy list counts as one `yes`, worked out from the lists. `python3 -I tools/assess.py tally --splits` shows where voters disagree. A vote backs no claim.

## Evidence for each question

Each piece of evidence is a record on one claim. `matched_source` records, which attach a claim to an outside source, must name the **organization** behind the source and link to it, and say how much was **verified**.

| Question | Evidence that counts | Evidence that does not |
|---|---|---|
| Do job listings ask for it? | Posting counts and quotes (`kind: job-postings`, with `match.count`); an O*NET or BLS listing; votes (not backing) | One model's guess |
| Is it an ability? | A match to the O*NET Abilities list (`kind: onet`, `dump-match`, with the element id and categories) | A model's draft |
| Is it a certification? | The attesting organization's own page (`kind: issuer`, `page-read`), a regulator or standards listing, a Wikipedia or Wikidata dump match (`dump-match`, with the categories that show what kind of thing it is), a person's check | A search result alone, a model's draft or second draft, a legacy list |
| Is it a language, and which kind? | A match in a language reference (for programming languages a language list such as GitHub Linguist or Wikidata; for spoken languages ISO 639, Glottolog or Wikipedia), a person's check | A model's draft |
| Is it a skill? | Posting counts; an O*NET Skills or Technology Skills listing; what is left after the other three | A model's draft |

What backs a claim, in code (`lexicon.backs`): a named person's `checked` with outcome `supports`, or a `matched_source` with outcome `supports` whose verification is `page-read` or `dump-match`. Everything else is recorded and shown but does not back: a model's draft, a model's check or second draft, a legacy list, a vote, and a match seen only in search results (`search-results-only`). A record with outcome `contradicts` counts against the claim, and an unresolved one blocks `reviewed`.

For `certification: true`, the attestation is the organization's name and a link to it, recorded on the evidence (`organization`) and again in `credential.issuers` and `credential.sources`. `certification_scope` is a second claim: whether one body awards it or many.

## The `credential` block

Facts found while checking a certification: official name, acronym, type, specificity (a specific credential, a requirement level such as DoD IAM Level I, a generic programme such as a college certificate in welding, or an occupation), status (active, retired, closed to new candidates, being replaced), issuers, accreditors, the field or fields of work (free text, or a code from ISCED-F 2013, SOC 2018 or O*NET-SOC), level, requirements, renewal, jurisdiction, related credentials, the Wikipedia page, the Wikidata id, and sources, each saying how much was verified. A checked single-issuer credential needs a type, one issuer and at least one source. The description is the entry's own `definition`.

Open in v0: the validator asks for evidence on `certification` and `certification_scope`, not on each part of the block. Revise after the first 25 to 50 credentials are checked; 21 have been.

## Passes

| Pass | Where | State |
|---|---|---|
| Draft from the name alone | any model | done: batches 001 and 002 (141 entries) |
| Second blind draft, recorded as checks | any model | done once, on the pilot |
| O*NET Abilities | this repo | done: 52 entries, backed by an O*NET match |
| Web search of credentials | cloud session | done for 21 credentials, search results only, so backs nothing |
| Read the attesting organization's page | needs open network access | not done |
| O*NET Skills, Knowledge, Technology Skills; BLS; ESCO | needs the database download | not done |
| Wikipedia and Wikidata dump | a cluster with disk, such as Discovery | not done, by design |
| Posting counts from the job listings | wherever the postings are | not done |
| Human review | people | not done |

### Handing back results from a pass run elsewhere

A pass reads the entries (id, `preferred_name`, `variants`, `kind`, `certification`, `certification_scope`), does its matching, and writes a JSON Lines file, one object per result:

```json
{"id": "a1b2c3d4e5", "evidence": {"field": "certification", "by": "source:enwiki-20261001", "action": "matched_source", "kind": "wikipedia", "verification": "dump-match", "outcome": "supports", "ref": "https://en.wikipedia.org/wiki/Advanced_trauma_life_support", "date": "2026-10-29", "run": "wikipedia-dump-1", "organization": {"name": "Wikimedia Foundation", "url": "https://www.wikimedia.org/"}, "match": {"dataset": "enwiki-20261001", "dataset_id": "page_id:123", "method": "redirect", "categories": ["Trauma"]}}, "credential": {}}
```

`evidence` must conform to `schemas/evidence.schema.json`; `credential` is optional and conforms to the `credential` definition in `schemas/certification.schema.json`. A tool that applies such a file to the entries (checking the id exists, refusing to overwrite, validating the dictionary) is the next piece to write.

### Notes for a Wikipedia pass

- The dump is to be downloaded and run on a cluster with the space, not here. I have not checked the dump file names or formats, because this cloud session cannot reach Wikipedia. Check them on dumps.wikimedia.org before writing the job.
- Matching has to cope with redirects (an acronym often redirects to the article), disambiguation pages, and names that mean different things in different places. Record how each match was made, and keep a manual option.
- Wikipedia text is licensed CC BY-SA 4.0. Store ids, URLs, categories and a short quote (up to 200 characters), and write definitions in our own words. Do not copy article text into entries.
- O*NET data is CC BY 4.0: keep the attribution in `THIRD-PARTY-NOTICES.md`.
