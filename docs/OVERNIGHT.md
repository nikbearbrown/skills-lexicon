# Overnight run, 2026-10-29

Worked on the branch `overnight-1` and merged into `main` on 2026-10-29 once drafting and the second-model checks were done. Everything here is `machine-drafted`: nothing is reviewed by a person and nothing backs a claim except the O*NET matches.

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

| round 07 | 07-a1, 07-a2, 07-a3, 07-a4 | 574 new | 11 variants | 108 not a skill | 95 unsure | 12 rejected | 2746 entries in all |

## Drafting finished (rounds 8 to 11)

The budget was lifted from $120 toward the credit balance for one job: draft the remaining tags. Round 8 (four agents of 200) and round 9 (two agents, 200 and 199) cleared them, round 10 (four tags) retried the duplicates, and the last two (UML and Zend PHP Certification) were filed as variants by the main session, because the drafting agents kept naming them as new entries and the nearest-entry list did not show the existing ones.

| Round | Run labels | New | Variant | Not a skill | Unsure | Rejected | Entries after |
|---|---|---|---|---|---|---|---|
| 08 | 08-a1 to 08-a4 | 595 | 13 | 95 | 90 | 7 | 3341 |
| 09 | 09-a1, 09-a2 | 347 | 44 | 0 | 4 | 4 | 3688 |
| 10 | 10-a1 | 0 | 1 | 0 | 1 | 2 | 3688 |
| 11 | 11-main (main session) | 0 | 2 | 0 | 0 | 0 | 3688 |

Round 8 was mostly degrees: one agent got 200 associate, bachelor's and master's degrees in a named field, which a model wrote from a template (the definition changes with the degree level and the field). They are real things job listings ask for, but they are the least informative entries in the lexicon and the likeliest to be merged or generalised later. Round 9 was the last certification-list tags (degrees again) and 199 languages, of which 40 were variants of an existing language.

Drafted entries per round are in `data/skills_batch_*.md`. Rounds 6 to 9 used 200 tags per agent.

## Reviews of the new entries (second model)

| Review | Model, effort | Entries | Contradicts recorded |
|---|---|---|---|
| review-3a-opus (certifications 1 to 120) | claude-opus-5-5, xhigh | 120 | 11 |
| review-3b-opus (certifications 121 to 240) | claude-opus-5-5, xhigh | 120 | 12 |
| review-3c-opus (certifications 241 to 360) | claude-opus-5-5, xhigh | 120 | 5 |
| review-3d-opus (certifications 361 to 402, languages 88, abilities 10) | claude-opus-5-5, xhigh | 140 | 9 |

Every certification, language and ability entry drafted from the tag lists has now been checked once by a different model. The contradictions are listed in `docs/REVIEW-FLAGS.md` (100 records on 84 entries; about 70 of them are short forms judged ambiguous, such as CWE, AMT, AHM or CSSD, which should not be variants). The 1,796 skill entries drafted in rounds 1 to 7 have not had a second-model check; the skill entries drafted before round 1 and the registry skills did, in reviews 1 and 2.

## Reviews of the rounds 8 and 9 entries (second model)

| Review | Model, effort | Entries | Supports | Contradicts |
|---|---|---|---|---|
| review-4a-opus (certifications 1 to 120 of the unchecked set) | claude-opus-5-5, xhigh | 120 | 594 | 1 |
| review-4b-opus (certifications 121 to 240) | claude-opus-5-5, xhigh | 120 | 688 | 0 |
| review-4c-opus (certifications 241 to 360) | claude-opus-5-5, xhigh | 120 | 736 | 0 |
| review-4d-opus (certifications 361 to 432, languages 1 to 40, abilities 2) | claude-opus-5-5, xhigh | 114 | 646 | 4 |
| review-4e-opus (languages 41 to 170) | claude-opus-5-5, xhigh | 130 | 700 | 1 |

That is 604 entries and 6 contradictions (about 1 per 100), against 2 to 27 per 100 entries in the earlier reviews (mostly 4 to 10). Do not read this as the new entries being better. Most of the 432 certifications are degrees and certificates written from a template ("Master's in X", "PhD in X"), where one definition and one `certification_scope` fit every entry and the reviewer, a more agreeable role than the drafter, had nothing to catch. The reviewers' own reports say as much ("every entry follows one template"). The signal is in the `unsure` and `no` votes, which are many: associate transfer degrees and niche doctorates that listings rarely name (review 4a alone gave 18 `no` and 25 `unsure` votes on 120 entries, and 4e one more `unsure` on a dialect). Contradictions are listed in `docs/REVIEW-FLAGS.md`.

## Second-model check of the skills (review 5)

The last unchecked entries, the 2,134 skills drafted in rounds 1 to 9, were checked by 18 Opus reviewers (`review-5a-opus` to `review-5r-opus`, claude-opus-5-5 at xhigh, model and effort read from each transcript), three packets of 40 each (the last 94 entries).

| | |
|---|---|
| Entries checked | 2,134 |
| Claims judged `supports` | 7,748 |
| Claims judged `contradicts` | 116 on 112 entries: 105 variants, 7 definitions, 2 kinds, 2 relations |
| Claims judged `unsure` (nothing recorded) | 15 |
| Votes on the entry | 1,885 yes, 67 no, 182 unsure |

Almost all the contradictions are variants. Reviewers marked a variant bad when it is a misspelling or scraping leftover ("Softwares", "Anlysis", "Women'S…") or a short form that also means something else (DRM, DLL, CFCs, EDR, ETL). The 7 definitions are specific factual errors: wrong original vendor (Btrieve, Handle System, ShareFile, Source Insight, TIBCO Spotfire) and a wrong former name (HincII). The 2 kinds are iBeacon (a standard, not a platform) and Mechanical seal (a machine part, not a tool). Reviewers mostly accepted the kind of each entry, so `kind` is the claim a person should look at next: the `unsure` verdicts concentrate on `kind`, for things filed as a tool, method, library or standard that are really files, laws or specifications.

As with the earlier reviews, a reviewer is more agreeable than a drafter, so a 98% `supports` rate is weak evidence; the contradictions, unsures and `no` votes are the signal. The first-pass drafts were not bad at the level a reviewer can see from memory. They may be wrong in ways memory cannot show, which is what the source-matching passes are for.

## End state

- **3688 entries**: 2472 skill, 859 certification, 290 language, 67 ability (52 of them O*NET).
- **15880 claims**; 104 are backed by a matched source (the O*NET abilities) and none by a person.
- **8480 votes** in the ledger, each with model and effort.
- **No tag is unresolved.** 1,162 tags got no entry: 564 were judged not a skill and 598 left unsure by the drafting model. The unsure ones could be re-drafted by a stronger model.
- **Second-model check:** every entry that did not come from O\*NET has had one, by a model other than the drafter. None has had a check by a person.
- 133 tests pass. Merged into `main` as a fast-forward from `overnight-1`; later reviews were committed directly to `main`.
- Spend: the session reported $96.02 at the last reading, after the skill reviews. The credit meter followed the session figure plus about $9 (a screenshot read $74 used when the session reported $65.06), so about $105 of the $250 credit. `scripts/subagent_cost.py` over-counts and is not the cost basis.
