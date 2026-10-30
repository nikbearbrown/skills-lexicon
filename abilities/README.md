# O*NET abilities

## Executive summary

**What it is.** O*NET's ratings of how much of each of the 52 human abilities an occupation calls for, on the 0 to 7 level scale: 894 occupations × 52 abilities = **46,488 rows**, with the standard error, confidence-interval bounds, rater count and rating date for each. It is the data behind the "Abilities the work calls for" chart in the jobs explorer, which plots six of the 894 occupations.

**What is new here.** `onet-ability-ratings-all-occupations.csv` holds all 894 occupations with all 15 columns of the export. `onet-occupations.csv` gives each occupation's title. The older files in this folder (`onet-abilities.json`, `onet-ability-ratings.json`, `README-onet.md`) are unchanged: they hold the 52 definitions and the same ratings for six occupations only. The six-occupation values match the full file exactly (312 of 312 rows).

**Release: O\*NET 30.2.** The export was taken from the explorer project's database on 2026-08-10 and did not record its release. It has since been checked against `Abilities.txt` in the O*NET 30.2 text database (February 2026): all 46,488 level rows match it on every field, with no differences. Rating dates run from 12/2004 to 08/2025. That file is dated 2025-08-17 inside the archive, so an earlier release may carry identical values; the content is 30.2's. The explorer project had listed the release as unresolved; this check resolves it.

**Read it correctly.** Each rating describes what an *occupation* demands. It is not an assessment of a person and not an AI replacement probability. This export has no population reference bands.

**Licence.** O*NET data is CC BY 4.0. These files are modified (reformatted, joined to titles). See [Attribution](#attribution).

## Files

| File | Rows | What it holds |
|---|---|---|
| `onet-ability-ratings-all-occupations.csv` | 46,488 | Level (`LV`) ratings, all 15 export columns, 894 occupations × 52 abilities. New. |
| `onet-occupations.csv` | 1,016 | `soc_code` and `title` for every O*NET-SOC occupation in the export, including the 122 that have no ability ratings. Join on `soc_code`. New. |
| `onet-abilities.json` | 52 | Ability ids, names, definitions, category, subcategory. Unchanged. |
| `onet-ability-ratings.json` | 312 | Ratings for six occupations (Computer Programmers, Software Developers, Graphic Designers, Registered Nurses, Customer Service Representatives, Carpenters), with 10 of the 15 columns. Unchanged. |
| `README-onet.md` | | Earlier note on the two JSON files. Unchanged. |

## Columns

`onet-ability-ratings-all-occupations.csv`, in export order. Values are kept as text exactly as exported, so `4.880` stays `4.880`. Booleans are `true` or `false`. CSV lines end in CRLF, like the other CSVs in this repository.

| Column | Meaning |
|---|---|
| `soc_code` | O*NET-SOC occupation code, e.g. `15-1252.00` (Software Developers). |
| `element_id` | O*NET content-model id of the ability, e.g. `1.A.1.a.2`. |
| `element_name` | Ability name, e.g. Written Comprehension. |
| `category` | `cognitive`, `psychomotor`, `physical` or `sensory`. Derived from the `element_id` prefix when the database was built, not a column of O*NET's own Abilities file. |
| `subcategory` | The ability's group, e.g. Verbal Abilities. Derived the same way. |
| `scale_id` | Always `LV`, the level scale. O*NET also rates importance (`IM`); those rows are not in this export. |
| `data_value` | The rating: how much of the ability the occupation requires, 0 to 7. Observed here: 0.0 to 6.0. |
| `n` | Number of raters. Always 8 in this export. |
| `standard_error` | Standard error of the rating. |
| `lower_ci`, `upper_ci` | Lower and upper confidence-interval bounds for `data_value`. The confidence level is O*NET's; the export does not restate it. |
| `recommend_suppress` | `true` where O*NET recommends not using the value because of low precision (68 rows, 40 occupations). The explorer shows these as "Withheld". |
| `not_relevant` | `true` where O*NET marks the ability as not relevant to the occupation (7,410 rows; the value is 1.12 or lower, and 0 in 5,753 of them). The explorer draws these as hollow dots. |
| `date_updated` | Month and year (`MM/YYYY`) the rating was last updated. Earliest 12/2004, latest 08/2025. |
| `domain_source` | Who rated it. `Analyst` in every row: occupational analysts, not job holders. |

O*NET's own names for the same columns in `Abilities.txt`, in order: O*NET-SOC Code, Element ID, Element Name, (no category or subcategory), Scale ID, Data Value, N, Standard Error, Lower CI Bound, Upper CI Bound, Recommend Suppress (Y/N), Not Relevant (Y/N), Date, Domain Source.

`onet-occupations.csv` keeps two of the seven columns of the source occupations export (`soc_code`, `title`); the rest (`soc_code_bls`, `description`, `job_zone`, `major_group_code`, `major_group_name`) are left out.

## The 0 to 7 level scale

`LV` is O*NET's level scale for abilities. A higher value means the occupation calls for more of that ability: Written Comprehension is 4.380 for Software Developers, while abilities marked `not_relevant` are 1.12 or lower. The scale runs 0 to 7, and the highest value in this export is 6.0. O*NET anchors the scale with example tasks per ability, in `Level Scale Anchors.txt` of the 30.2 database (for Oral Comprehension, level 2 is "Understand a television commercial" and level 4 is "Understand a coach's oral instructions for a sport"). Those anchors are not copied here.

Example row, Software Developers, Written Comprehension: `data_value` 4.380, interval 3.7402 to 5.0098, `n` 8.

## What this is not

- **Not a personal assessment.** The ratings describe what an occupation demands, not what a person can do.
- **Not an AI replacement probability.** Employment changes have many causes. These ratings do not identify the effect of AI.
- **No reference bands.** Population reference bands (workforce or field averages) are not available in this export. Nothing here estimates them.
- **Small samples.** `n` is 8 analysts for every row. The intervals say how much those eight differ, not how much occupations vary across workers.
- **A snapshot.** These are O*NET 30.2 values. O*NET updates ratings in later releases; check the current release before citing a rating as current.

## Where it came from

The Irreducibly Human AI Exposure Explorer database, table `onet_abilities`, filtered to `scale_id = 'LV'`, exported 2026-08-10 as `abilities-lv.json` (46,488 rows; SHA-256 `77e8bcc921540801105291bab505b9907b060cb156c2e061e7cff01b702a5ade`). The same database fed the jobs explorer's six-occupation file. `onet-occupations.csv` comes from the export of the same date, table `onet_occupations`.

The CSVs were written from those JSON files with Python's `csv` module and checked by reading them back: all 46,488 rows and 15 columns equal the source values. Nothing was recalculated, rounded, filtered or filled in.

**Check against O\*NET.** The JSON export was compared with `Abilities.txt` from `db_30_2_text` (archive `onet-30.2.zip`, SHA-256 `b5479271931796b838f7173dc0f673a9ec961b7833ac87168fd11e92e7453741`, downloaded from https://www.onetcenter.org/dl_files/database/db_30_2_text.zip on 2026-10-24; `Abilities.txt` SHA-256 `822f866b0f441376edc8a282bf0f77c8c3f687c456dcd607b12de86fccba8e71`). That file has 92,976 rows: 46,488 `IM` (importance) and 46,488 `LV` (level). The `LV` rows and the export have the same keys (`soc_code` plus `element_id`), and every value, interval, count, flag, date and source agrees. Numbers were compared as decimals, since the export writes `4.880` where O*NET writes `4.88`. The `IM` rows are not copied here. The ability CSV has SHA-256 `c475c952425e90e7c4e0a27ec2ce80a4476101d175580b6747b624410729bcba`.

## Attribution

This folder includes information from the O\*NET 30.2 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET® is a trademark of USDOL/ETA. Humanitarians AI has modified all or some of this information: it reformatted the data from JSON to CSV, added occupation titles, and, for the six-occupation file, selected a subset of occupations and columns. USDOL/ETA has not approved, endorsed, or tested these modifications.

- O*NET database releases: https://www.onetcenter.org/db_releases.html
- Licence guidance and attribution wording: https://www.onetcenter.org/license_db.html
- Creative Commons Attribution 4.0 International: https://creativecommons.org/licenses/by/4.0/
