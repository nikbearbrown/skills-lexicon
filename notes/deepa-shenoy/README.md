# Deepa Shenoy: notes

Contributor notes for the Irreducibly Human Work Lexicon. Issue: #4.

## Files

| File | What it is |
|---|---|
| `verify_paper_claims.py` | Re-checks every number the manuscript (v0.2) reports against a checkout. Read-only; standard library plus `tools/lexicon.py` for the backing rule. |

Run it from the repository top:

```sh
python3 -I notes/deepa-shenoy/verify_paper_claims.py
```

Each line prints `OK` when the count matches the manuscript, `DIFF` when it does not.

## Reproduction check (2026-11-28)

I ran the script against the pinned commit the manuscript names (`3cd82a4`) and against `main` at `5a2b44d`. Every number matched on both: 14 of 14 checks print `OK`.

| Manuscript number | Result |
|---|---|
| 3,754 canonical concepts; 1,988 skill, 550 knowledge, 67 ability, 290 language, 859 certification | matches |
| 723 entries of kind `skill` | matches |
| 3,555 machine-drafted, 199 proposed, 0 reviewed | matches |
| 17,229 assertion fields, 1,455 backed (8.45%) | matches |
| Backed claims by source | 1,217 descriptions, 120 kinds, 118 definitions, all `dump-match` |
| Claims backed by a person | 0 |
| PostgreSQL example (Postgres; PG case-sensitive with "database" context; broader to SQL with `rolls_up: true`) | matches |
| Service orientation counterexample (definition about helping people, description about software architecture) | matches |

## Roll-up count fix

`scripts/summary_stats.py` counted roll-ups with `r.get('rollup')`, but the schema and `tools/lexicon.py` use `rolls_up`. The count therefore reported 0 while one relation (PostgreSQL → SQL) has `rolls_up: true`. `REPRODUCE.md` already notes the mismatch.

This branch changes:

- `scripts/summary_stats.py`: reads `rolls_up` (one line). Output is now `rollup_enabled: 1`.
- `README.md`: "Relations with count roll-up enabled" from 0 to 1.
- `docs/IRREDUCIBLY-HUMAN-WORK-LEXICON-REPORT.md`: the sentence "No relation has count roll-up enabled" now says one relation does.

Left unchanged on purpose: dated snapshots (`docs/summary-stats-2026-11-14.json`, the paper's `inventory-recount.json`), which record what was run at the time, and the manuscript itself.

## AI use

Claude helped write the check script and draft these notes. I checked each number against the manuscript.
