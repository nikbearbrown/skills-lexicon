# Skills lexicon

## Executive summary

**What it is.** A shared dictionary of skills, tools and abilities as they appear in job ads and on resumes. Each concept has one canonical name, the other ways people write it, and its relations to other concepts (broader, part of, related, contrast). It is built so others can add to it and correct it.

**Why it exists.** To count skills in job postings you have to know that "Postgres" and "PostgreSQL" are one skill, that "Swift" can mean two things, and that PostgreSQL is a kind of SQL. The counts on the explorer are only as good as this dictionary.

**State.** First pass. 277 entries: 81 imported from the jobs.humanitarians.ai skills registry (status `proposed`), 3 drafted examples, 141 drafted from two 100-tag batches of the legacy tag lists (`data/skills_batch_001` and `002`), and the 52 O*NET abilities (`abilities/`, `data/skills_batch_003`). Each batch is a `.json` and a `.md`. The drafted entries are `machine-drafted`, written by a model from general knowledge with no source checked. Nothing is `reviewed`. Of 994 claims, 104 are backed by a matched source (the O*NET abilities) and none by a person. 128 tests pass.

**Licence and owner.** MIT, copyright Humanitarians AI Incorporated (see `LICENSE`). **Not decided yet:** who reviews entries.

## How it works

- What is in the lexicon is what job listings ask for, in four classes: abilities (basis: O*NET), certifications (attested by an organization, named and linked), languages, and skills (what is left). We gather evidence for and against, with who gave it, which model and at what effort; later passes decide. See [docs/SCHEMAS.md](docs/SCHEMAS.md).
- One JSON file per concept in `entries/`. Format: [docs/ENTRY-FORMAT.md](docs/ENTRY-FORMAT.md). JSON Schemas for entries, evidence and certifications, and what counts as evidence: [docs/SCHEMAS.md](docs/SCHEMAS.md).
- Synonyms and spelling variants are not entries. They are `variants` of the canonical entry.
- Relations connect concept to concept. Roll-up (a mention of PostgreSQL also counting toward SQL) is an explicit, per-link choice, off by default.
- Every claim can carry evidence: who drafted it (a named model and run, or a person), who checked it, and which outside source it was matched to. A model agreeing with a model never counts as a check; a person's check or a matched source does.
- Status: `machine-drafted`, `proposed`, `reviewed`, `deprecated`. Only `reviewed` entries should feed published counts.
- **Growing it from postings:** scripts find known and unknown skills, and any language model drafts entries for the unknown ones. See [docs/PIPELINE.md](docs/PIPELINE.md) and [skills/draft-entry/SKILL.md](skills/draft-entry/SKILL.md).
- `python3 -I tools/lexicon.py validate` checks every entry. `python3 -I tools/lexicon.py index` builds `build/index.json`, the surface-form lookup the extractor reads. `python3 -I tests/test_lexicon.py` and `python3 -I tests/test_pipeline.py` run the tests.

## Known limits

- The 81 imported concepts were written to resolve course tags, so their variants are thin for matching real ads.
- Relations imported from the registry carry no roll-up decision and no source.
- The three drafted entries have not been checked against any source.
- NanoLex was the format model; its entries appear model-written and are not used as a source here.
- No prior-art check against ESCO, O*NET technology skills or Lightcast has been done.
- The extractor and drafter are tested with a fake model endpoint and stub commands. The drafter has been run once with a real model, on 100 legacy tags, answering from the tag name alone. Neither has been run on real postings.
- The legacy certification and language lists are unchecked. The pilot model's `certification` and `language_type` answers are flagged where they differ from a list, but agreement with a list proves nothing.
