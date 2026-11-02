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
