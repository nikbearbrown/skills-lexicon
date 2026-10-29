# Overnight run, 2026-10-29

Working on branch `overnight-1`; `main` is untouched. Everything here is `machine-drafted`: nothing is reviewed by a person and nothing backs a claim except the O*NET matches.

**Plan.** (1) Draft the unresolved legacy tags in parallel rounds of three agents, 100 tags each, ingesting centrally so a clash is rejected and retried. (2) Have a different model check the claims on entries that exist, recording its model and effort. (3) Web-check certifications and languages (search results only). Stop at about $120 total spend.

**Model and effort.** All drafting agents: `claude-sonnet-5-5`, subagents, effort read from each transcript. Reviewers are named in `data/runs.json`.

## Rounds

| Round | Run labels | New | Variant | Not a skill | Unsure | Rejected | Spend after |
|---|---|---|---|---|---|---|---|
| 1 | round-01-a1, a2, a3 | 207 | 2 | 31 | 54 | 6 (same-concept pairs) | $18.81 |

Notes on round 1: agents drafted 100 tags each. The six rejected tags are same-concept pairs the agents deliberately answered as new; they stay unresolved and are retried with the first entry visible. Cost: the session's figure after round 1 was $18.81 and after round 2 and three Opus reviews $25.88. It appears to cover the main session only, so subagents are estimated from their own transcripts (token counts priced at the rates the session's own figures imply): about $10 for 14 Sonnet runs and $2 to $10 for 5 Opus runs. The run stops at $120 on reported plus estimated.

## Reviews by a second model

| Review | Model, effort | Entries | Checks | Contradicts | Unsure |
|---|---|---|---|---|---|
| review-1-opus (certifications, first 25) | claude-opus-5-5, xhigh | 25 | 129 | 2 | 1 |

A reviewer is more agreeable than a drafter, so a high rate of `supports` is weak evidence; the contradictions and unsures are the signal. The brief was clarified after review 1 (notes allowed on `supports`; how to treat uninformative definitions and ambiguous abbreviations).

| round 2 | a1, a2, a3, a4 | 293 new | 5 variants | 42 not a skill | 54 unsure | 6 rejected | 777 entries in all |
| review-2a-opus (skills, 120 entries) | claude-opus-5-5, xhigh | 120 | 433 | 3 | 2 |
| review-2b-opus (skills, 120 entries) | claude-opus-5-5, xhigh | 120 | 438 | 10 | 0 |
| review-2c-opus (skills 98, languages 32, abilities 3) | claude-opus-5-5, xhigh | 133 | 415 | 36 | 2 |

**Canary test of the reviewer.** Twenty certification entries, eight with a deliberately wrong definition or kind (wrong issuer, a master's degree called doctoral, an endorsement given the wrong meaning), twelve untouched. The Opus reviewer contradicted all 8 planted errors and none of the 12 untouched entries. The planted errors were blatant, so this shows the reviewer is not simply agreeing; it does not show it would catch subtle errors. The canary entries were never in the repository.

Reviewer notes on the brief (not yet acted on): abbreviations such as DL, PG, RAG, LLM and ASIC were marked bad variants because they mean other things in listings; misspelled variants were marked bad; `knowledge` versus `standard` for standards documents (ARP4754, ASC 340, NFPA 70E, TL 9000) was contradicted.

| round 03 | 03-a1, 03-a2, 03-a3, 03-a4 | 273 new | 8 variants | 49 not a skill | 58 unsure | 12 rejected | 1050 entries in all |

| round 04 | 04-a1, 04-a2, 04-a3, 04-a4 | 273 new | 14 variants | 57 not a skill | 51 unsure | 5 rejected | 1323 entries in all |

| round 05 | 05-a1, 05-a2, 05-a3, 05-a4 | 305 new | 3 variants | 36 not a skill | 47 unsure | 9 rejected | 1628 entries in all |

| round 06 | 06-a1, 06-a2, 06-a3, 06-a4 | 544 new | 9 variants | 119 not a skill | 114 unsure | 14 rejected | 2172 entries in all |
