# Which sources we use

The lexicon exists to gather evidence with a known source. A source is only as good as our right to use it, so one rule decides what goes in.

**Use a source only if its licence is clear and we can name it. If the licence is unclear, missing, or only a copyright notice, ignore the source.** Do not argue a source in. Leaving one out costs a little coverage; including one we cannot use costs the whole repository's standing.

What follows from the rule:

- Every source we use is named with its licence, its version and a link, in `THIRD-PARTY-NOTICES.md` and in the record that cites it (`organization` on a `matched_source` evidence record, or the source file for bulk evidence).
- A source we ignore is not silently dropped. It is listed with the reason, so the next person does not redo the work. The Kaggle release records its two omitted sources this way (`summary.json`: one copyright-only declaration, one database licence without a verified version).
- A licence a publisher declares is recorded as declared and marked "not independently verified". We do not upgrade it.
- Licence conditions travel with the data. Attribution, share-alike and non-commercial terms are recorded per source and the data stays separable by source, so any source can be removed later without touching the rest.
- We copy facts, names, identifiers, counts and links. We do not copy prose from a source into the repository unless its licence allows it and the notice says so.
- Only a person's check or a source matched by reading the source itself (`page-read`, `dump-match`) backs a claim. A model's opinion never does, and neither does a search result. See `docs/SCHEMAS.md`.

Sources in use or planned:

| Source | Licence | Used for | Status |
|---|---|---|---|
| O*NET 30.2 | CC BY 4.0 | abilities and their ratings | in the repository |
| English Wikipedia dump | CC BY-SA 4.0 | matching articles to entries; titles, ids and links only | planned (dump on the cluster) |
| Kaggle datasets | declared per dataset | occurrence counts of skill labels | on a branch, not merged; sources with unclear licences already left out |
| Outside model reviews | none claimed on the answers | opinions, recorded as evidence that never backs a claim | pull request and a branch, not merged |
