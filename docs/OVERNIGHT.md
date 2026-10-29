# Overnight run, 2026-10-29

Working on branch `overnight-1`; `main` is untouched. Everything here is `machine-drafted`: nothing is reviewed by a person and nothing backs a claim except the O*NET matches.

**Plan.** (1) Draft the unresolved legacy tags in parallel rounds of three agents, 100 tags each, ingesting centrally so a clash is rejected and retried. (2) Have a different model check the claims on entries that exist, recording its model and effort. (3) Web-check certifications and languages (search results only). Stop at about $120 total spend.

**Model and effort.** All drafting agents: `claude-sonnet-5-5`, subagents, effort read from each transcript. Reviewers are named in `data/runs.json`.

## Rounds

| Round | Run labels | New | Variant | Not a skill | Unsure | Rejected | Spend after |
|---|---|---|---|---|---|---|---|
| 1 | round-01-a1, a2, a3 | 207 | 2 | 31 | 54 | 6 (same-concept pairs) | $18.81 |

Notes on round 1: agents drafted 100 tags each. The six rejected tags are same-concept pairs the agents deliberately answered as new; they stay unresolved and are retried with the first entry visible. Cost reported by the session after round 1: $18.81 (the three subagents used about 411k tokens in all). Spend is estimated with a cautious $3 extra per round, in case subagent tokens are not in the session's figure, and the run stops at $120 on that estimate.

## Reviews by a second model

| Review | Model, effort | Entries | Checks | Contradicts | Unsure |
|---|---|---|---|---|---|
| review-1-opus (certifications, first 25) | claude-opus-5-5, xhigh | 25 | 129 | 2 | 1 |

A reviewer is more agreeable than a drafter, so a high rate of `supports` is weak evidence; the contradictions and unsures are the signal. The brief was clarified after review 1 (notes allowed on `supports`; how to treat uninformative definitions and ambiguous abbreviations).
