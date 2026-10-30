# Kaggle occurrence evidence and candidate queue

This release links 2,568 existing lexicon entries to 19,766 source-specific observations in 30 Kaggle datasets. It also supplies 303 pending candidate proposals and two scope holds. No entries, definitions, accepted aliases, or review statuses were changed. Candidate labels are hypotheses awaiting semantic review.

The observations are additive evidence of surface-form usage. A mention does not establish a definition or prove a term is a skill. Curated lists, extracted skill fields and sampled archived job text have distinct source types. Case, context and ambiguity flags remain unresolved where recorded. Counts are record matches, not unique jobs or independent corroboration. See `url-overlap.json` and each source's family/overlap fields before combining sources.

## Files and use

- `observations.jsonl`: entry ID or candidate key, source/version/file/hash, extraction method, counts, matched forms and record locators. CSV record numbers include the header as record 1. Text offsets are zero-based Python string offsets, with an exclusive end.
- `sources.json`: versioned dataset URLs, publisher attribution, license declarations and links, archive/member hashes, field configuration, source families and exclusions. Metadata-only sources have no public observations.
- `candidate-queue.json`: 303 pending proposals and two scope holds, linked to the published observation IDs. Counts are recomputed from this public subset. Alias groupings are proposals, not accepted equivalences.
- `subject-registry.json`: observed subjects pinned to lexicon commit `7531b4c376fd6bc78c1a888cf7a3db035d1915f7` (3,688 entries; 6,625 normalized canonical names/variants).
- `summary.json`: public counts, local coverage and exact omissions. Publication based on main `e8ce1744e920e02889827c32d7b51247501c6e3f`; existing IDs and candidate exact label/variant matches were rechecked against that main checkout. Semantic novelty is still subject to review.
- `prepublication-verification.json`: recorded results of earlier full local archive replay, covering 21,533 observations. This is historical evidence, not a claim that the archive-free verifier replays source records.
- `input-hashes.json` and `manifest.json`: original input fingerprints and this public package's checksums.

Run `python3 tools/verify_kaggle_publication.py` for archive-free schema, linkage, omission and integrity checks (requires `jsonschema`). `tools/publish_kaggle_evidence.py SOURCE_REPO DESTINATION_REPO` regenerates this projection when the original local research ledgers are available; it refuses to overwrite an existing release.

## Publication limits and attribution

The full local collection contains 21,533 observations across 32 datasets. This public projection omits 1,767 observations from two sources pending license clarification, and removes all job-text excerpts. The complete local ledgers remain preserved. Raw datasets and publisher descriptions are not distributed here. Metadata for excluded sources remains to explain coverage. This is not an exhaustive inventory of Kaggle or a complete census of job postings.

Source-specific attribution, versions, URLs and declared licenses are retained in `sources.json`. Source-derived material remains subject to its applicable source terms, including attribution, share-alike, noncommercial or other conditions; the repository's general code license does not relicense third-party material. The observation subsets remain separable by `source_id`. License labels are publisher declarations, not independently verified rights clearance. The transformations are label matching, counting, sampling and removal of job prose; no endorsement by source publishers is implied.

Versioned URLs, CSV record locators, column names, archive/member hashes, text offsets and excerpt hashes permit source replay after restoring the raw ZIPs from recoverable local Trash or obtaining the pinned versions from Kaggle. Archives are not required to read this evidence, but are required to independently replay it. Future availability of Kaggle versions is not guaranteed. No raw archive is committed.
