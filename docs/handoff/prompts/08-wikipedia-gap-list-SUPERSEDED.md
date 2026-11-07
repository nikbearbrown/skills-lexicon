> SUPERSEDED. The gap-list idea (find major software on Wikipedia that the lexicon lacks) needs infobox types and inbound-link counts, which the processed Wikipedia build does not have. See docs/handoff/HANDOFF.md, open item on the gap list.

# Prompt for Claude Code: find the major software on Wikipedia that the lexicon is missing

Yes, this is possible, and it is a better test than my list. I picked Git, Jira, MySQL and the rest from memory. This pass enumerates every Wikipedia article that is software, a programming language, a file format or an operating system, ranks them by how many other articles link to them, and checks each against the lexicon. Nothing depends on what I thought of.

Run it in Claude Code on your own computer, in the same setup as the cluster prompt (it needs ssh to the cluster, the repo checkout and the dump from that prompt).

Three things to know before you run it:

- **Wikipedia is not job demand.** It has an article for every obscure program. A pass over it finds what is major and missing, but it cannot tell you what employers ask for. Combine its output with the Kaggle occurrence counts: a term that is major on Wikipedia and also appears in thousands of job-skill fields is the strong candidate.
- **It covers tools, platforms, languages and formats only.** "Stakeholder management" or "root cause analysis" have no software infobox. Those gaps need another source (O\*NET Skills and Knowledge are the natural one).
- **Licence.** Wikipedia text is CC BY-SA 4.0. The cleaned lead is published only with its attribution and licence, in its own file; descriptions later written from it carry the same marker.

If the pass works, it does two jobs at once. The missing list feeds the drafting pipeline. The matched list is the first chance to attach a source match, read directly from the dump, to existing entries; that kind of evidence can back a claim, which no model's opinion can.

## The prompt (paste this)

```
You are working on the Skills Lexicon project. On our university cluster (the Explorer cluster) in the AI Skunks project folder there is a checkout of the repository at <AI Skunks folder>/skills-lexicon and the English Wikipedia dump at <AI Skunks folder>/enwiki/latest/ (a link to the dated folder; the files are enwiki-<date>-pages-articles-multistream.xml.bz2 and the matching -index.txt.bz2). Use the paths and ssh setup you found when you set that up. You run on my own computer and reach the cluster over ssh.

GOAL

Find every English Wikipedia article about software, a programming language, a file format or an operating system. Rank them by how many other Wikipedia articles link to them. Check each against the lexicon (3,688 entries) and produce a list of the important ones the lexicon does not have. This is a gap test, so it must not depend on any list of names I give you.

RULES

- No sudo. Do not change anything on the cluster outside the AI Skunks folder. Do not decompress the whole dump to disk; stream it. Do not run heavy work on a login node: use the cluster's batch system (Slurm, as an array job over chunks of the dump) and check its documentation or ask me for the right partition and limits.
- Never put a password in a command; if two-factor approval is needed, tell me.
- Wikipedia text is CC BY-SA 4.0 and that is fine to use, with attribution. Published files may contain the cleaned lead paragraph of an article, but only together with its title, page id, revision id, permalink and the dump date, and in a file whose header states the licence (CC BY-SA 4.0, adapted from English Wikipedia). Do not publish text beyond the lead.
- Do not special-case any names to make the tests below pass. If a test fails, find the reason in the method and fix the method.
- Work in small steps. Run each step on a tiny part of the dump first (the first chunk only), show me the result, and only then run it on all of it.
- Stop and ask me if anything is unclear: Slurm partition, paths, or a choice between two reasonable methods.

METHOD

1. Read the multistream index file. It lists the byte offset of each compressed stream (about 100 articles per stream). Use those offsets to split the dump into chunks that Slurm tasks can read independently with random access. Redirect pages are in the dump too (they carry a redirect target): keep all of them as a from-title to to-title table.
2. Infobox survey. In a first pass over the chunks, count the infobox template names used by articles (the text starting with {{Infobox ...), and write the top 400 with counts to a file. Show me the top 60. Then propose which template names mean software, programming language, file format, operating system, markup or query language, web browser, library or framework, technical standard or protocol. Exclude video games, hardware and companies. Use the real names you find in the survey; do not assume them. Write the final list of included template names to a file and keep it as part of the results. Proceed with your proposal, but show it to me with 30 random included articles (title and infobox name) so I can check it.
3. Extraction. For each article that uses an included infobox template, record: title, page id, revision id, the permalink (https://en.wikipedia.org/w/index.php?title=...&oldid=<revision id>), the infobox template name, and these infobox fields when present: developer, released, programming language, operating system, genre or type, license, website. Also record every redirect title that points to the article, and the count of OTHER articles that link to it (count wikilinks in article text, resolve redirects to their targets, ignore links from the article to itself, and count each linking article once). Also record the cleaned lead: the first paragraph of the article text with all wikitext removed (use a wikitext parser such as mwparserfromhell, not regular expressions): no templates, no pronunciation, no citation markers like [3], no link or bold markup. If the first paragraph is under 200 characters, add the second. If an article's first paragraph is empty or is only a hatnote, say so rather than guessing. Record a flag when the article is a disambiguation page.

Categories. Wikipedia assigns categories partly through templates, so the article text alone misses some. Get the true membership from the dump's categorylinks table: download from the same dated dump folder the files enwiki-<date>-categorylinks.sql.gz, enwiki-<date>-page.sql.gz and enwiki-<date>-linktarget.sql.gz, plus the pagelinks table enwiki-<date>-pagelinks.sql.gz if you want the inbound-link counts from it instead of scanning (say which you used). Fetch them the same way as the first dump (on my computer, verify the checksums, copy to the cluster), after telling me how big they are. For every extracted article keep ALL its categories, and mark each as a maintenance category (hidden or tracking categories such as articles with short descriptions, or pages using templates with missing data; use the page_props hidden-category flag if the dump has it, otherwise a clear rule you write down) or not. Keep the non-maintenance ones as tags for that article; do not discard any for taste. Also keep each category's parent categories (the Category pages are in the dump; confirm that) so we can build broader and narrower relations, and mark categories that are really facets (a year like 2014 software, a licence like Software using the Apache license, an implementation language like Free software programmed in Go) by a simple pattern rule you describe to me.
4. Matching. Load the lexicon with its own code (inside the repo, python3 -I tools/lexicon.py, and import lexicon as L; use L.load to read the entries, L.forms for each entry's preferred name and variants, L.norm to normalise). A Wikipedia article matches an entry when the normalised title, the title without a trailing parenthesis (for example Git (software) becomes git), or any of its redirect titles equals a normalised name or variant of the entry. Record which entry matched and through which title. Also record separate near matches (a close spelling, or a title that contains an entry's name) but do not count them as matches.
5. Report. Count articles by infobox type, matched and unmatched. Write the unmatched list sorted by inbound-link count. Show me the top 100 unmatched with title, infobox type, developer and inbound count, and show how many unmatched articles have at least 10, 100, 1000 and 5000 inbound links.

TESTS (run these before you give me the final numbers)

A. Extraction recall. These names must each be found as an extracted article (as the title or as a redirect): Git, Jira, MySQL, Kubernetes, MongoDB, Jenkins, Django, Redis, GitHub, Snowflake, Microsoft Azure, Apache Kafka, Splunk, Terraform, Ansible, Slack, Confluence, Adobe Photoshop, Microsoft Excel, AutoCAD, Oracle Database, Python, SQL, Docker, Java, JavaScript, PostgreSQL, React, TensorFlow, MATLAB, Linux. Some of these may legitimately use a different infobox or be spelled differently on Wikipedia (for example Excel is Microsoft Excel). For every name that is NOT found, tell me why and what article it is, and whether my infobox list should include its template. This list measures how well the extraction finds the software it should.
B. Matching expectations. In the lexicon today, these are already entries: Python, SQL, Docker, Java, JavaScript, PostgreSQL, React, TensorFlow, MATLAB, Linux (as Linux systems administration may fail to match; report it). These are NOT entries: Git, Jira, MySQL, Kubernetes, MongoDB, Jenkins, Django, Redis, GitHub, Snowflake, Microsoft Azure, Apache Kafka, Splunk, Terraform, Ansible, Slack, Confluence, Adobe Photoshop, Microsoft Excel, AutoCAD, Oracle Database. Report any case where your matching result disagrees with this, and explain it.
C2. Lead and category check. For Kubernetes, Git, MySQL, Jenkins and Django, show me the cleaned lead and the list of non-maintenance categories exactly as you will store them, plus the disambiguation flag. For the Kubernetes article I expect categories such as Containerization software, Orchestration software, Cloud infrastructure, Linux containerization, 2014 software, Free software programmed in Go and Software using the Apache license; tell me which of these you did and did not get, and why.
C. Precision. From the unmatched articles with at least 100 inbound links, give me a random sample of 100 as a table (title, infobox type, developer, inbound count) so I can mark which are real things job listings could ask for. Do not judge them yourself.
D. Threshold. Report the inbound-link count of each name in test B's NOT-entries list, and the lowest of them. I will use that to choose a cut-off.

OUTPUT

- On the cluster: <AI Skunks folder>/wikipedia-software-gap/<dump date>/ with the survey, the included-template list, all extracted articles (with cleaned lead, permalink and categories), the redirect table, the category table with parents, the matched and unmatched files, the test results, and the code and the Slurm scripts.
- On my computer: a new branch of my local clone of the skills-lexicon repository named data/wikipedia-software-gap-<dump date>, off the current main, holding the code and the results. Put the cleaned leads in their own file with a header stating the licence, the source and the dump date; the other files carry only ids, titles, links, counts and categories. Add a README that states the dump date, the exact included templates, the method, that the leads are CC BY-SA 4.0 text adapted from English Wikipedia, and that an inbound-link count measures importance on Wikipedia, not job demand. Run python3 -I tools/lexicon.py validate before committing and report its last line. Commit and push the branch. Do not merge it, do not open a pull request, and do not touch main.

WHEN YOU ARE DONE

Tell me, in plain text: how many articles you found per infobox type; how many matched and how many are unmatched; the results of tests A to D; the sizes and paths of the outputs; the branch name and commit hash; how long the cluster jobs took; and anything that failed or that you skipped. Do not say a test passed unless you ran it and saw it pass.
```

## What comes after

When the files are back, I can turn the unmatched list into candidates for the drafting pipeline in the same way as the Kaggle ones, with the Wikipedia article recorded as the source. I would cut the list using test D and the Kaggle counts together before drafting, so we do not spend credits on obscure software.
