# Data sources on the cluster: WordNet, O*NET, ESCO

**Status: DONE except ESCO (needs Bear at the terms form; licence not yet found)**

This page was last edited to add ESCO as a download step; the run that happened used the earlier look-only ESCO step.

Paste the block below into Claude Code on Bear's Mac (it needs ssh to the cluster). Written for a Claude Code that has never seen this project.

```
You are Claude Code on Bear's Mac, logged in to the Explorer cluster over ssh (host alias: explorer).

GOAL
Add four open language and skills resources to the cluster as data sources, next to the Wikipedia dump, so later jobs can read them: (1) Princeton WordNet 3.1, (2) the current Open English WordNet, (3) the O*NET database (text version, including the Skills, Knowledge and Technology Skills tables), (4) ESCO, the European Commission's classification of occupations, skills and qualifications (European Skills, Competences, Qualifications and Occupations), and, if one officially exists, the ESCO to O*NET crosswalk. Nothing is analysed here: this job downloads, verifies, records provenance, and reports.

PATHS (use exactly these; invent none)
- Project folder (group aiskunks): /projects/aiskunks
- Write only under these new folders: /projects/aiskunks/wordnet/pwn-3.1/ , /projects/aiskunks/wordnet/oewn-<release>/ , /projects/aiskunks/onet/<release>/ , /projects/aiskunks/esco/<version>/ , and /projects/aiskunks/skills-lexicon-work/data-sources/ (for the check script and notes)
- Already there, do not touch: /projects/aiskunks/skills-lexicon (git checkout), /projects/aiskunks/enwiki/ (Wikipedia dump)

RULES
No sudo. Stay inside /projects/aiskunks. No passwords, keys or tokens anywhere. Delete nothing, and if a destination folder already exists with files, STOP and ask. Do not edit the lexicon checkout. Many small files are slow on /projects (about 2 files per second): keep each source as its downloaded archive plus its extracted folder, which is a few dozen files at most. Python on the login node is 3.9: scripts must be 3.9 compatible. Use tar over ssh to copy from the Mac (not rsync). Setgid is on the project folders: keep the group. Only use a source whose licence is clear and recorded; if a licence is unclear, do not download it and report why.

STEP 0. Where to download from.
On the cluster login node run: curl -sI --max-time 20 https://wordnetcode.princeton.edu , curl -sI --max-time 20 https://github.com , curl -sI --max-time 20 https://www.onetcenter.org . Report the three results. For each source below, download directly on the cluster if its host answers there and a download of this size is allowed on a login node (these files are small: tens of MB). Otherwise download on the Mac into a temporary folder outside any repository and copy over with tar over ssh. Say which route you used for each.

STEP 1. Princeton WordNet 3.1.
- Find the database download on https://wordnet.princeton.edu/download/current-version (the 3.1 database files, expected as wn3.1.dict.tar.gz at wordnetcode.princeton.edu). Also read https://wordnet.princeton.edu/license-and-commercial-use and save its text.
- Put the archive and its extracted folder in /projects/aiskunks/wordnet/pwn-3.1/ . Keep the licence file that comes in the archive.
- Write /projects/aiskunks/wordnet/pwn-3.1/README.txt with: the source URL, today's date, the sha256 of the archive, the licence name and its notice text exactly as published, and the sentence "WordNet is a registered trademark of Princeton University; this copy is unmodified."

STEP 2. Open English WordNet (the maintained fork).
- Find the latest release from https://en-word.net/ or its GitHub project (globalwordnet/english-wordnet). Take the plain English WordNet release file in XML (not a database for a specific tool). Read the licence on that page and in the project, and record it. If you cannot find a clear licence statement, STOP and report; do not download.
- Put it in /projects/aiskunks/wordnet/oewn-<release year>/ with a README.txt that records the URL, the release, today's date, the sha256, and the licence as stated.

STEP 3. O*NET database, text version.
- From https://www.onetcenter.org/database.html find the current release (the earlier notes say 30.2) and its text-format zip (expected name like db_30_2_text.zip). Read its licence page https://www.onetcenter.org/license_db.html and record it (CC BY 4.0 with attribution is what we expect; confirm).
- Put the zip and the extracted folder in /projects/aiskunks/onet/<release>/ with a README.txt (URL, release, date, sha256, licence, the attribution text O*NET asks for).
- Confirm these files exist after extraction and report each one's line count: Skills.txt, Knowledge.txt, Abilities.txt, Technology Skills.txt, Work Activities.txt, Occupation Data.txt, plus whichever other file lists "hot technology" or "in demand" flags. The extracted file names may have spaces; do not rename anything.

STEP 4. A small check script.
Write /projects/aiskunks/skills-lexicon-work/data-sources/check_sources.py exactly as follows and run it with python3 -I:

    #!/usr/bin/env python3
    """Counts for the three sources, and a few lookups. Python 3.9. Reads only."""
    import glob
    import gzip
    import os
    import re
    import sys

    PWN = "/projects/aiskunks/wordnet/pwn-3.1"
    OEWN = sorted(glob.glob("/projects/aiskunks/wordnet/oewn-*"))
    ONET = sorted(glob.glob("/projects/aiskunks/onet/*"))
    ESCO = sorted(glob.glob("/projects/aiskunks/esco/*"))


    def pwn_counts():
        dict_dir = next((os.path.join(r, "dict") for r, d, f in os.walk(PWN) if "dict" in d), None)
        if not dict_dir:
            print("PWN: no dict folder found under", PWN)
            return None
        out = {}
        for pos in ("noun", "verb", "adj", "adv"):
            n = 0
            with open(os.path.join(dict_dir, "data." + pos), encoding="utf-8", errors="replace") as f:
                for line in f:
                    if not line.startswith("  "):
                        n += 1
            out[pos] = n
        print("PWN 3.1 synsets by part of speech:", out, "total", sum(out.values()))
        return dict_dir


    def pwn_lookup(dict_dir, words):
        for w in words:
            hits = []
            for pos in ("noun", "verb", "adj", "adv"):
                with open(os.path.join(dict_dir, "index." + pos), encoding="utf-8", errors="replace") as f:
                    for line in f:
                        if line.startswith(w + " "):
                            hits.append((pos, int(line.split()[2])))
                            break
            print("  lemma %-12s senses by pos: %s" % (w, hits or "none"))


    def oewn_counts():
        for d in OEWN:
            for p in glob.glob(os.path.join(d, "*.xml*")):
                op = gzip.open if p.endswith(".gz") else open
                n = 0
                with op(p, "rt", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        n += len(re.findall(r"<Synset ", line))
                print("OEWN", os.path.basename(p), "synsets:", n)


    def onet_counts():
        for d in ONET:
            for p in sorted(glob.glob(os.path.join(d, "**", "*.txt"), recursive=True)):
                with open(p, encoding="utf-8", errors="replace") as f:
                    n = sum(1 for _ in f)
                print("O*NET", os.path.relpath(p, d), "lines:", n)


    def esco_counts():
        for d in ESCO:
            for p in sorted(glob.glob(os.path.join(d, "**", "*.csv"), recursive=True)):
                with open(p, encoding="utf-8", errors="replace") as f:
                    n = sum(1 for _ in f)
                print("ESCO", os.path.relpath(p, d), "lines:", n)


    if __name__ == "__main__":
        dd = pwn_counts()
        if dd:
            pwn_lookup(dd, ["python", "java", "negotiation", "reasoning", "auditing", "kubernetes", "git", "jira", "swahili"])
        oewn_counts()
        onet_counts()
        esco_counts()

Report the whole output.

STEP 5. ESCO.
- Open https://esco.ec.europa.eu/en/use-esco/download . Report the current version. I expect a release in the v1.2 series (v1.2.0 from 2024 and possibly a 1.2.1 update) with about 3,039 occupations and 13,939 skills in 28 languages, but report what the page actually says. Read the terms or licence statement for ESCO on that site and save its text beside the data. I expect free use with attribution; confirm it.
- If the data is a plain download link (or a documented file or API download) and the terms allow it, download the CSV package for English, covering all of the classification: occupations, skills, skill groups and the skills hierarchy, the occupation-to-skill relations (essential or optional), and the broader/narrower relations. Put it in /projects/aiskunks/esco/<version>/ . Also report the size of the full multilingual package, but do not download it. Skip the RDF format.
- If getting the file needs a form, an account, a login, a captcha, or accepting terms in a browser, do NOT fill in, click through or script around anything on Bear's behalf. STOP and tell Bear exactly which page and button to use, the file name expected, and the folder to put it in (on the Mac, then copied with tar over ssh to /projects/aiskunks/esco/<version>/); continue when the file is there.
- Write /projects/aiskunks/esco/<version>/README.txt with the URL, version, date, sha256 of the archive, the terms as stated, and the attribution text ESCO asks for.
- Crosswalk: look on esco.ec.europa.eu and on onetcenter.org for an official mapping between ESCO occupations and O*NET-SOC occupation codes. I believe one has been published but I have not seen it; report whether it exists, where, its format and its licence. Download it into /projects/aiskunks/esco/crosswalk/ only if it is a plain link with a clear licence; otherwise report and wait.

CHECKS
a. For each of the three sources the folder exists, the archive's sha256 in README.txt matches `sha256sum` run again on the cluster, and a LICENSE or licence text is saved beside it.
b. check_sources.py ran with no error. Expected: WordNet 3.1 total on the order of 117,000 synsets (nouns about 82,000, verbs about 13,800, adjectives about 18,000, adverbs about 3,600); "python" has more than one noun sense; "kubernetes" and "jira" have none; "negotiation", "reasoning" and "auditing" are found. If a number is far off, say so and why.
c. The O*NET folder has the Skills, Knowledge, Abilities, Technology Skills and Work Activities tables with non-trivial line counts (Technology Skills should have thousands of lines). The ESCO folder has, for English, the occupations table (about 3,000 rows), the skills table (about 13,900 rows), the skill groups and hierarchy tables, and the occupation-to-skill relations table (tens of thousands of rows); give each file's real name and row count, since the names may differ from these.
d. ls -ld on each new folder: group aiskunks, setgid bit present.
e. Nothing else under /projects/aiskunks changed: git -C /projects/aiskunks/skills-lexicon status --porcelain prints nothing.

STOP AND ASK IF: ESCO needs a form, login or terms click-through; a destination folder already has files; a licence is missing, unclear or different from expected; a download host cannot be reached from either place; any checksum differs; the files are far larger than expected (more than 500 MB for any source); check_sources.py fails.

REPORT BACK (short, plain text)
For each source: the route (cluster or Mac), the exact release, the archive size, the sha256, the licence as stated, the folder path (four sources). The full output of check_sources.py. Results of checks a to e. The ESCO findings from step 5: version, terms, what was downloaded, whether the O*NET crosswalk exists. Anything that failed or was skipped. Do not say a check passed unless you ran it and saw it pass.
```
