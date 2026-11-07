# Job-posting field survey

Which fields can be read **unambiguously** from a job-posting dataset, that is, from a column that has its own header and values that behave like the field? This survey reports what is there. It decides nothing about which fields to extract.

Run on 2026-11-02 over the Kaggle job-related datasets downloaded to the AI Skunks project space on the Explorer cluster.

## What was surveyed

- 3,310 dataset archives were on the cluster. 2,764 of them contain at least one `.csv` or `.tsv` file; 546 contain none.
- 10,599 tabular files were found. 7 could not be read (4 datasets, 0.14% of the 2,764). 10,591 were read.
- For each file, the first 2,000 rows of every column were profiled. The survey stores column statistics only. **No posting text and no cell values are in these files.**

## What "unambiguous" means here

A column counts for a field only when **both** hold:

1. **The header names the field.** For example `job_title`, `title`, `position` for a job title; `company`, `employer` for a company; `location`, `city`, `country` for a place.
2. **The values behave like that field.**
   - Job title: short values (about seven words or fewer, few long ones) that repeat.
   - Company and location: short names, not links.
   - Date: 80% or more of the values parse as dates. Relative dates ("3 days ago") are rejected, because they need the date of the scrape.
   - Salary: mostly numeric, currency or range values.
   - Employment type, experience level, industry, education, remote: a short list of repeated values (60 or fewer different ones).
   - Skills: delimited short labels that are already structured.
   - Description: marked as free text and never parsed.

At least half of the sampled rows must have a value.

## What it did not read

- Files that are not `.csv` or `.tsv`: 577,350 files inside the archives, mostly text, images, model weights, PDFs, JSON, Word documents and code (`other_members.json` has the counts by extension). Spreadsheets (`.xlsx`) and `.parquet` files are among them and were not read.
- Free-text columns such as descriptions. They are never parsed.
- Anything beyond the first 2,000 rows of each file.

## Known limits of the checks

- The header test is loose. It matches any header containing a field word, so a column such as `company_size` or `company_id` is tested as a company column, and `date` matches any date column, not only the date a job was posted. Treat the counts as an upper bound on usable columns, and read samples before relying on a field.
- A dataset appears once per field however many files it has, but the counts of columns and files are dominated by a few datasets that hold thousands of small files.
- About 10% of datasets (279 of 2,764) share a file name and size with another dataset, so some are repeats or derivatives of one another.

## Licences

The datasets have **different publisher-declared licences**, and most have none recorded in our files. This survey is evidence about structure only. It is not a statement that any dataset may be reused.

## Files

- `summary.json`: for each field type, the number of datasets and files with an unambiguous column, and the most common header names.
- `other_members.json`: counts of the file types that were not read.
- `../../scripts/job_fields/field_survey.py`: the survey script (Python 3.9, reads only).

The per-column statistics file (`columns.jsonl`, 121 MB) is over the 40 MB limit and is not published.

## Rerun on 2026-11-06

The same script (`scripts/job_fields/field_survey.py`, unchanged; sha256 `656f0443f409a80325b9433a9d67cae2726b22539dc99328f5995948462e20cf`) was run again over the same folder. Results are in `summary-20261106.json` and `other_members-20261106.json`; the 2026-11-02 files above are unchanged. The `columns.jsonl` of the rerun is 121 MB and is not published. The whole rerun is a few minutes of compute (12.5 minutes for the survey on 8 cores).

**What changed.** 3,325 dataset archives (3,310 before); 10,640 tabular files; 29 files in 5 datasets could not be read (7 in 4 datasets before; the error kind was not recorded, and the cause was not looked into). Datasets with an unambiguous column: location 1,489 (1,488 before), job title 978 (977), company 901 (900), salary 850 (849), date 713 (712), experience level 656 (655), employment type 461 (460), industry 460 (460), skills list 203 (203). The archive count did not change while the survey ran.

**Findings that the counts above do not show.** These come from reading ten values from three randomly chosen datasets per field (random seed 7) and from the rejected columns. The values are not published.

- *Many matched datasets are not about job postings.* The folder holds everything Kaggle returned for the search term "jobs". Samples included a table of stock prices (matched as a date), workplace injury reports (matched as a location) and an industry-to-industry crosswalk (its industry names matched as job titles). The counts are therefore counts of columns that look like the field, not of job-posting datasets.
- *The header test matches more than it should.* In the top headers: `company_size` (161 columns), `company_id` (69) and `employer_rating` (45) count as company; `education_level` (109) counts as experience level; `id_vivienda`, `id_hogar` and `id_persona` (126, 126, 72) count as job id.
- *The value checks are also too strict in places.* A `Position` column holding ordinary job titles was rejected as "all different" because the table was small. Of the company and location columns rejected, 2,996 and 5,149 failed the "at least half the sampled rows have a value" test, yet samples of some of them showed ordinary values. The cause was not investigated.
- *Repeats.* 326 datasets (280 counting only csv and tsv files) share a file name and size with another dataset. In the samples, the same table appeared in two different datasets.
- *Not read.* 555 of 3,325 archives (16.7%) contain no csv or tsv file. Among the files not read are 4,844 `.parquet` and 550 `.xlsx` files.

**Licences, corrected.** The text above says most datasets have no licence recorded in our files. The download manifest (`manifest.json` in the Kaggle jobs folder on the cluster) records a publisher-declared licence for every one of the 3,325 downloaded datasets. These are declared by the publisher and not independently verified. 1,905 are CC0 (930), CC BY 4.0 (406), Apache 2.0 (330), MIT (227) or ODC-By (12); 571 are "Unknown"; the rest are other terms such as CC BY-SA, CC BY-NC, CC BY-NC-SA, "Other (specified in description)" and "Data files © Original Authors". Among the datasets with an unambiguous column, those with one of the five clear licences are: location 900 of 1,489, job title 579 of 978, company 518 of 901, salary 496 of 850, date 458 of 713, skills list 150 of 203. Datasets without one of these licences may be used for private analysis only. This is still evidence about structure; it is not a statement that any dataset may be reused.

**Use.** Choose datasets for the job-title pilot by looking at them, not by taking every dataset with a matching header.
