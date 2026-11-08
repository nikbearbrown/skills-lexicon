# O*NET technology names matched to the lexicon

For two O*NET releases, every distinct technology name in O*NET's table of software and technology used by occupations, with how many occupations list it, O*NET's own **Hot Technology** and **In Demand** flags, and which lexicon entries it matches. Nothing here is decided: these are matches, hints and counts for a person.

| Release | O*NET table | Folder |
|---|---|---|
| 31.0 (current) | Software Skills | `31.0/` |
| 30.2 | Technology Skills | `30.2/` |

O*NET 31.0 renamed the table (Technology Skills became Software Skills) and its name column ("Example" became "Workplace Example"). The script accepts both. In the 31.0 output the fields `commodity_codes` and `commodity_titles` hold O\*NET's **element ID and element name** (31.0 has no commodity columns); in the 30.2 output they hold the UNSPSC commodity code and title.

## Files

- `31.0/matches.jsonl`, `30.2/matches.jsonl`: one line per distinct technology name: `example`, `n_occupations`, `n_hot_occupations`, `n_in_demand_occupations`, `hot`, `in_demand`, `commodity_codes`, `commodity_titles`, `match`, `entries`, `contained_entries`.
- `31.0/summary.json`, `30.2/summary.json`: counts and the columns used.
- `../../scripts/onet_match/match_onet_tech.py`: the script (Python 3.9, reads only).

## How to read `match`

- `exact`: the name, or the name without a bracketed part or a trailing word such as "software", equals a lexicon entry's preferred name or a variant, after normalising case and spacing. `entries` lists them.
- `contains`: the name does not match exactly but contains a lexicon form of four or more characters. **This is a hint, not a match.** It is often wrong (for example "Microsoft SQL Server Reporting Services" contains "reporting", "Azure DevOps Services" contains "devops").
- `none`: no exact match and no contained form. This mixes two cases: the lexicon really has no entry (for example Git, GitHub, MySQL, MongoDB, Jenkins, Apache Kafka, Splunk, Django, Microsoft Excel), and the lexicon has the concept under a different name than O\*NET's style ("Structured query language SQL", "Atlassian JIRA"). Exact matching cannot tell them apart.
- `n_occupations` counts occupations (O\*NET-SOC codes) that list the name; it is not a count of jobs or postings and is not market share.

## Counts

| | 31.0 | 30.2 |
|---|---|---|
| Rows in the table | 31,821 | 32,773 |
| Distinct technology names | 8,753 | 8,785 |
| exact / contains / none | 193 / 426 / 8,134 | 197 / 425 / 8,163 |
| Hot technology names | 176 | 171 |
| Hot: exact / contains / none | 49 / 21 / 106 | 48 / 21 / 102 |
| In-demand names | 285 | 277 |

The lexicon used for matching was the checkout at `/projects/aiskunks/skills-lexicon` on the Explorer cluster (commit `e8ce174`, 3,688 entries). Run on 2026-11-07 as a Slurm job (1 min 41 s). No model was involved.

## Source and licence

This product includes information from the O\*NET 31.0 and 30.2 Databases by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), used under the CC BY 4.0 license. O\*NET(R) is a trademark of USDOL/ETA. The counts and matches here were produced from that information by the Skills Lexicon project; USDOL/ETA has not approved, endorsed or tested these modifications.

## Checksums (sha256)

```
f42dc69fe0147cab1e79e1f312f5f09c7a6ec3a983c77eff5341a890ea510aec  31.0/matches.jsonl
a5541d0b23d7b8886741c7a2d3133ffcc97e6041a09deb397bdc8a7447ccb3c1  31.0/summary.json
e2afea6f9d5b79549c872c1fe989dd44f0426ef3a9fc63576c23209b72aa940f  30.2/matches.jsonl
3eec46402840c888ff853b594e7f9617962363d63859f7e7e7c5bfb4e251dacb  30.2/summary.json
db2099622123cb31bffd3275312691a70fd25aaf08c14dbe2808eb5d8d76fa0a  ../../scripts/onet_match/match_onet_tech.py
```
