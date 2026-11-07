# Cluster setup: the repository and the Wikipedia dump

**Status: DONE (kept as a record; do not run again)**


Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
I need you to set up two things on our university cluster (the Explorer cluster), inside our project folder, called AI Skunks (one word; probably aiskunks): a copy of a public GitHub repository, and the latest English Wikipedia dump. You are running on my own computer, which can reach the cluster over ssh. I am not sure whether the cluster can reach the internet. If it can (from a login node, a data-transfer node or a batch job where that is allowed), download directly on the cluster. If it cannot, download on my computer and copy over. Find that out by testing; do not assume it.

THE TWO THINGS

1. The repository https://github.com/nikbearbrown/skills-lexicon (public, default branch main). It goes in a folder named skills-lexicon (lower case, with a hyphen, no spaces) directly inside the AI Skunks folder, as a real git checkout with its .git folder.
2. The latest finished English Wikipedia dump from https://dumps.wikimedia.org/enwiki/ , in a folder named enwiki inside the AI Skunks folder, in a sub-folder named for the dump date.

RULES

- Do not run sudo. Do not change anything on the cluster outside the AI Skunks folder. Do not change my ~/.ssh/config; if you think it needs a change, tell me what and let me decide.
- Never ask me for a password and never put one in a command. If the cluster asks for two-factor approval, stop and tell me so I can approve it. To avoid repeated approvals, you may open one shared connection with ssh options ControlMaster=auto, ControlPersist=2h and a ControlPath in /tmp.
- Do not download Wikidata or anything else beyond the two things above (the repository and the Wikipedia files named in step 5).
- Do not decompress the Wikipedia dump. Keep it as downloaded.
- If anything is unclear (which folder is AI Skunks, which ssh host, whether a big download is allowed where you want to do it), stop and ask me. A wrong guess here costs a lot of time and disk.

STEPS

Step 1. Connect. Look in my ~/.ssh/config for the cluster host (a name mentioning explorer, or a neu.edu host). Run  ssh <host> hostname  to check it works. If you cannot tell which host is the cluster, ask me.

Step 2. Find the AI Skunks folder. On the cluster, look for it (try ls of /projects, /work, /scratch and my home folder, and check my groups with the groups command). It may be spelled aiskunks, ai-skunks, AI_Skunks or similar. Show me the candidates and the free space (df -h on that path, and the quota command the cluster provides if there is one). If there is more than one candidate or you are not sure, ask me before creating anything. Tell me how much space is free: the Wikipedia dump needs about 30 GB for the compressed files.

Step 3. Test the internet from the cluster. From the login node run  curl -sI --max-time 20 https://github.com  and  curl -sI --max-time 20 https://dumps.wikimedia.org  and report both results. Also read the cluster's documentation, or ask me, about a data-transfer node: many clusters have a separate node for large downloads and forbid big transfers on the login node. Do not run a large download on a login node unless the cluster's rules say it is fine. If the cluster can reach both sites from an allowed place, you may download there directly and skip the copy through my computer. If not, use my computer as the middle step as described below.

Step 4. The repository.
- Clone it on my computer into a temporary folder:  git clone https://github.com/nikbearbrown/skills-lexicon  (full clone, keep .git).
- Copy it to <AI Skunks folder>/skills-lexicon on the cluster with  rsync -a --partial -e ssh  (include the .git folder). If the folder already exists on the cluster, do not overwrite it: show me what is there and ask.
- Check it. On the cluster: the git HEAD commit must equal the HEAD of my local clone; the entries folder must hold 3688 json files (the count when this was written; if it differs, tell me the number rather than treating it as a failure); and  python3 -I tools/lexicon.py validate  run inside the folder must end with "0 errors" (if python3 is missing on the login node, tell me instead of installing anything). Report the commit hash.
- If git works from the cluster directly, tell me, so later updates can use  git pull  there. Otherwise later updates mean repeating this step.

Step 5. The Wikipedia dump.
- Find the latest FINISHED dump. Open https://dumps.wikimedia.org/enwiki/ , look at the dated folders (named YYYYMMDD), and pick the newest one in which the file enwiki-<date>-pages-articles-multistream.xml.bz2 is complete (a status page or the dumpstatus.json file in the folder says each job is "done"). Do not use the folder named "latest" for the download itself: use the dated folder so the date is recorded and the checksums match.
- Files to get from that dated folder: enwiki-<date>-pages-articles-multistream.xml.bz2 and enwiki-<date>-pages-articles-multistream-index.txt.bz2, and also these database tables, which a later analysis needs: enwiki-<date>-categorylinks.sql.gz, enwiki-<date>-page.sql.gz, enwiki-<date>-linktarget.sql.gz and enwiki-<date>-pagelinks.sql.gz (tell me their sizes first; pagelinks is large). Also get the checksum file for that date (enwiki-<date>-sha1sums.txt, or the md5sums file if there is no sha1 one). The main file is about 25 GB, so before downloading check the free disk space on my computer and tell me if it is not enough.
- Download politely: one connection at a time, resumable (curl -L -C - --retry 5, or wget -c), run in the background with a log file so a dropped connection does not lose progress. dumps.wikimedia.org limits connections and can be slow; if it is far too slow, you may use a mirror listed on https://dumps.wikimedia.org/mirrors.html and tell me which.
- Verify the checksums on my computer against the checksum file. Do not copy anything that fails.
- Copy to <AI Skunks folder>/enwiki/<date>/ on the cluster with  rsync -a --partial --progress -e ssh . Verify the checksums again on the cluster. Run that check as a batch job or in the background if it is long.
- Then make a link  <AI Skunks folder>/enwiki/latest  pointing to the <date> folder, and write a small README.txt inside the <date> folder that records: the source URL, the dump date, the file names and sizes, the checksums, and today's date.
- Do not delete my local copy of the dump or the temporary clone. When everything is verified, tell me how much space they use and ask whether to delete them.

WHEN YOU ARE DONE

Report in plain text: the full path of the AI Skunks folder you used; whether the cluster can reach the internet (the two curl results) and whether a transfer node exists; the repository path and commit hash and whether validation said 0 errors; the dump date, file names, sizes and whether the checksums matched on both sides; how much space is used and how much is left; and anything that failed or that you skipped. Do not claim a step worked unless you saw it work.

----- next paste -----

You are working on the Skills Lexicon project. On our university cluster (the Explorer cluster) in our AI Skunks project folder (one word, probably aiskunks) there is a checkout of the repository at <AI Skunks folder>/skills-lexicon and the English Wikipedia dump at <AI Skunks folder>/enwiki/latest/ (a link to the dated folder; the files are enwiki-<date>-pages-articles-multistream.xml.bz2 and the matching -index.txt.bz2). Use the paths and ssh setup you found when you set that up. You run on my own computer and reach the cluster over ssh.

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

Categories. Wikipedia assigns categories partly through templates, so the article text alone misses some. Get the true membership from the dump's categorylinks table: download from the same dated dump folder the files enwiki-<date>-categorylinks.sql.gz, enwiki-<date>-page.sql.gz and enwiki-<date>-linktarget.sql.gz, plus the pagelinks table enwiki-<date>-pagelinks.sql.gz if you want the inbound-link counts from it instead of scanning (say which you used). They should already be in the dump folder from the setup step; if any are missing, fetch them the same way as the first dump (directly on the cluster if it can reach the internet, otherwise on my computer, verify the checksums, copy over), after telling me how big they are. For every extracted article keep ALL its categories, and mark each as a maintenance category (hidden or tracking categories such as articles with short descriptions, or pages using templates with missing data; use the page_props hidden-category flag if the dump has it, otherwise a clear rule you write down) or not. Keep the non-maintenance ones as tags for that article; do not discard any for taste. Also keep each category's parent categories (the Category pages are in the dump; confirm that) so we can build broader and narrower relations, and mark categories that are really facets (a year like 2014 software, a licence like Software using the Apache license, an implementation language like Free software programmed in Go) by a simple pattern rule you describe to me.
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
