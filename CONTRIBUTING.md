# Contributing

This is a first pass. Corrections are welcome, especially wrong synonyms, missing variants and wrong relations.

1. Change or add one entry file under `entries/`. Follow [docs/ENTRY-FORMAT.md](docs/ENTRY-FORMAT.md).
2. Run `python3 -I tools/lexicon.py validate` and `python3 -I tests/test_lexicon.py`. Both must pass.
3. Say why in the pull request. Quote an ad, an official page or a standard for any synonym or relation. "Related" is not a reason.
4. Do not mark your own change `reviewed`. A second person does that and records `reviewed_by`.
5. If you disagree with an existing entry, change it and record the disagreement in `notes` so the reviewer sees both sides.

Rules of thumb:
- A synonym means the same concept. If it only resembles it, make a separate entry and a `related` link.
- Do not paste model output as fact. Entries drafted by a model get status `machine-drafted` until a person has checked them.
- Roll-up is a decision, not a default.
