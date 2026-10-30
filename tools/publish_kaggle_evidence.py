#!/usr/bin/env python3
"""Create an archive-free public projection from the local Kaggle research ledger.

Usage: python3 tools/publish_kaggle_evidence.py SOURCE_REPO DESTINATION_REPO
No downloads, entry edits, or changes to the input ledgers are performed.
"""
import collections
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import parse_qsl, urlsplit

RELEASE = Path('data/source-occurrences/kaggle-publication-2026-10-30')
EXCLUDED = {
    'arbazkhan971/allskillandnonskill': 'Copyright-only declaration; redistribution permission unresolved.',
    'anandhuh/data-science-jobs-in-india': 'Combined database/content license label lacks verified exact license version and URI.',
}
LICENSE_URLS = {
    'CC0: Public Domain': 'https://creativecommons.org/publicdomain/zero/1.0/',
    'Attribution 4.0 International (CC BY 4.0)': 'https://creativecommons.org/licenses/by/4.0/',
    'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'CC BY-NC-SA 4.0': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
    'Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)': 'https://creativecommons.org/licenses/by-nc/4.0/',
    'ODC Attribution License (ODC-By)': 'https://opendatacommons.org/licenses/by/1-0/',
    'Apache 2.0': 'https://www.apache.org/licenses/LICENSE-2.0',
    'GPL 2': 'https://www.gnu.org/licenses/old-licenses/gpl-2.0.html',
    'MIT': 'https://opensource.org/license/mit',
}

def read(path):
    return json.loads(path.read_text())

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def norm(value):
    return ' '.join(unicodedata.normalize('NFKC', value).casefold().split())

def main(src, dest):
    out = dest / RELEASE
    if out.exists():
        raise SystemExit('Refusing to overwrite an existing publication directory')
    out.mkdir(parents=True)
    folders = [src / 'data/source-occurrences' / x for x in ('kaggle', 'kaggle-expansion-2026-10-30')]
    proposal_dir = src / 'data/kaggle-candidates/expansion-2026-10-30'
    sources = {}
    input_hashes = {}
    for folder in folders:
        sources.update(read(folder / 'sources.json'))
        for name in ('sources.json', 'field-observations.jsonl', 'text-observations.jsonl', 'verification.json'):
            input_hashes[str((folder / name).relative_to(src))] = digest(folder / name)
    omitted = collections.Counter()
    rows = []
    quotes_removed = 0
    urls_removed = 0
    for folder in folders:
        for name in ('field-observations.jsonl', 'text-observations.jsonl'):
            for line in (folder / name).read_text().splitlines():
                row = json.loads(line)
                obs = row['observation']
                source = sources[obs['source_id']]
                if source['dataset_ref'] in EXCLUDED:
                    omitted[source['dataset_ref']] += 1
                    continue
                assert source['license_as_recorded'] in LICENSE_URLS, source['license_as_recorded']
                for example in obs['examples']:
                    if 'quote' in example:
                        del example['quote']
                        quotes_removed += 1
                    url = example.get('posting_url')
                    if url:
                        parts = urlsplit(url)
                        sensitive = {'token', 'access_token', 'api_key', 'apikey', 'password', 'secret', 'signature', 'sig', 'email'}
                        if parts.username or any(k.casefold() in sensitive or k.casefold().startswith('x-amz-') for k, _ in parse_qsl(parts.query)):
                            del example['posting_url']
                            urls_removed += 1
                obs['limitations'].append('Public projection omits job-text excerpts; retained hashes and character offsets refer to the original archived text. Source license terms remain applicable.')
                rows.append(row)
    rows.sort(key=lambda r: r['observation']['observation_id'])
    assert len({r['observation']['observation_id'] for r in rows}) == len(rows)
    with (out / 'observations.jsonl').open('w') as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n')
    for sid, source in sources.items():
        source['publication_status'] = 'metadata-only-license-review' if source['dataset_ref'] in EXCLUDED else 'observations-published'
        source['license_url'] = LICENSE_URLS.get(source['license_as_recorded'])
        source['archive_availability'] = 'Raw archive not distributed. Restore the local archive or obtain the pinned version from the publisher to replay.'
        source['public_changes'] = 'Filtered to matched lexicon/candidate terms and record locators; job prose omitted; no source content corrections asserted.'
    write(out / 'sources.json', sources)
    by_subject = collections.defaultdict(list)
    for row in rows:
        by_subject[row.get('id', row.get('candidate_key'))].append(row)
    registry = read(folders[-1] / 'subject-registry.json')
    candidate_keys = {norm(v['subject']['label']): k for k, v in registry.items() if 'candidate_key' in v}
    candidate_files = [('active-queue.json', 'pending'), ('scope-holds.json', 'scope-hold')]
    candidates = []
    current_entries = {}
    current_names = collections.defaultdict(set)
    for path in (dest / 'entries').glob('*.json'):
        entry = read(path)
        current_entries[entry['id']] = entry
        current_names[norm(entry['preferred_name'])].add(entry['id'])
        for variant in entry.get('variants', []):
            if isinstance(variant, str):
                current_names[norm(variant)].add(entry['id'])
            else:
                text = variant.get('label') or variant.get('text') or variant.get('name') or variant.get('form')
                if text:
                    current_names[norm(text)].add(entry['id'])
    for filename, triage in candidate_files:
        input_hashes[str((proposal_dir / filename).relative_to(src))] = digest(proposal_dir / filename)
        for item in read(proposal_dir / filename):
            key = candidate_keys[norm(item['term'])]
            linked = by_subject.get(key, [])
            candidate = {k: item[k] for k in ('term', 'proposed_label_group', 'review_checks', 'review_note', 'nearby_existing_entries', 'semantic_review') if k in item}
            candidate.update(candidate_key=key, review_status='pending', triage=triage,
                             observation_ids=[r['observation']['observation_id'] for r in linked],
                             published_dataset_count=len({sources[r['observation']['source_id']]['dataset_ref'] for r in linked}),
                             published_source_family_count=len({r['observation']['source_family'] for r in linked}),
                             published_field_record_matches=sum(r['observation']['counts']['records'] for r in linked if r['observation']['claim'].endswith('skill-field')),
                             current_main_exact_label_matches=sorted(set().union(*(current_names[norm(v)] for v in item.get('proposed_label_group', [item['term']])))))
            candidates.append(candidate)
    write(out / 'candidate-queue.json', candidates)
    write(out / 'subject-registry.json', {k: registry[k] for k in sorted(by_subject)})
    write(out / 'url-overlap.json', read(folders[-1] / 'url-overlap.json'))
    write(out / 'prepublication-verification.json', {p.name: read(p / 'verification.json') for p in folders})
    write(out / 'input-hashes.json', input_hashes)
    missing_ids = sorted(k for k in by_subject if not k.startswith('kaggle-candidate:') and k not in current_entries)
    assert not missing_ids, missing_ids
    summary = {
        'baseline_commit': '7531b4c376fd6bc78c1a888cf7a3db035d1915f7',
        'publication_base_commit': subprocess.check_output(['git', '-C', str(dest), 'rev-parse', 'HEAD'], text=True).strip(),
        'baseline_entries': 3688, 'baseline_normalized_names_and_variants': 6625,
        'local_observations': len(rows) + sum(omitted.values()),
        'published_observations': len(rows),
        'published_datasets': len({sources[r['observation']['source_id']]['dataset_ref'] for r in rows}),
        'existing_entries_linked': sum(not k.startswith('kaggle-candidate:') for k in by_subject),
        'existing_entry_classes': dict(collections.Counter(v[0]['subject']['entry_class'] for k, v in by_subject.items() if not k.startswith('kaggle-candidate:'))),
        'active_pending_candidates': sum(c['triage'] == 'pending' for c in candidates),
        'scope_holds': sum(c['triage'] == 'scope-hold' for c in candidates),
        'candidates_without_publishable_observations': [c['term'] for c in candidates if not c['observation_ids']],
        'candidates_matching_current_main_labels': {c['term']: c['current_main_exact_label_matches'] for c in candidates if c['current_main_exact_label_matches']},
        'omitted_observations': dict(omitted), 'omission_reasons': EXCLUDED,
        'job_text_excerpts_removed': quotes_removed, 'sensitive_posting_urls_removed': urls_removed,
        'coverage': '32 locally inspected datasets; 35 skill-field files; 1,867,517 skill-field records. Not exhaustive Kaggle coverage. 30 datasets represented in public observations.',
        'source_independence': 'Not established. Known derivative families and partial URL overlap are recorded; counts are not votes or independent jobs.',
        'entry_changes': False,
    }
    write(out / 'summary.json', summary)
    for rel in ['schemas/source-occurrence.schema.json', 'tools/publish_kaggle_evidence.py', 'tools/verify_kaggle_publication.py']:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src / rel, target)
    (out / 'README.md').write_text(f'''# Kaggle occurrence evidence and candidate queue

This release links {summary['existing_entries_linked']:,} existing lexicon entries to {len(rows):,} source-specific observations in 30 Kaggle datasets. It also supplies 303 pending candidate proposals and two scope holds. No entries, definitions, accepted aliases, or review statuses were changed. Candidate labels are hypotheses awaiting semantic review.

The observations are additive evidence of surface-form usage. A mention does not establish a definition or prove a term is a skill. Curated lists, extracted skill fields and sampled archived job text have distinct source types. Case, context and ambiguity flags remain unresolved where recorded. Counts are record matches, not unique jobs or independent corroboration. See `url-overlap.json` and each source's family/overlap fields before combining sources.

## Files and use

- `observations.jsonl`: entry ID or candidate key, source/version/file/hash, extraction method, counts, matched forms and record locators. CSV record numbers include the header as record 1. Text offsets are zero-based Python string offsets, with an exclusive end.
- `sources.json`: versioned dataset URLs, publisher attribution, license declarations and links, archive/member hashes, field configuration, source families and exclusions. Metadata-only sources have no public observations.
- `candidate-queue.json`: 303 pending proposals and two scope holds, linked to the published observation IDs. Counts are recomputed from this public subset. Alias groupings are proposals, not accepted equivalences.
- `subject-registry.json`: observed subjects pinned to lexicon commit `{summary['baseline_commit']}` (3,688 entries; 6,625 normalized canonical names/variants).
- `summary.json`: public counts, local coverage and exact omissions. Publication based on main `{summary['publication_base_commit']}`; existing IDs and candidate exact label/variant matches were rechecked against that main checkout. Semantic novelty is still subject to review.
- `prepublication-verification.json`: recorded results of earlier full local archive replay, covering 21,533 observations. This is historical evidence, not a claim that the archive-free verifier replays source records.
- `input-hashes.json` and `manifest.json`: original input fingerprints and this public package's checksums.

Run `python3 tools/verify_kaggle_publication.py` for archive-free schema, linkage, omission and integrity checks (requires `jsonschema`). `tools/publish_kaggle_evidence.py SOURCE_REPO DESTINATION_REPO` regenerates this projection when the original local research ledgers are available; it refuses to overwrite an existing release.

## Publication limits and attribution

The full local collection contains 21,533 observations across 32 datasets. This public projection omits 1,767 observations from two sources pending license clarification, and removes all job-text excerpts. The complete local ledgers remain preserved. Raw datasets and publisher descriptions are not distributed here. Metadata for excluded sources remains to explain coverage. This is not an exhaustive inventory of Kaggle or a complete census of job postings.

Source-specific attribution, versions, URLs and declared licenses are retained in `sources.json`. Source-derived material remains subject to its applicable source terms, including attribution, share-alike, noncommercial or other conditions; the repository's general code license does not relicense third-party material. The observation subsets remain separable by `source_id`. License labels are publisher declarations, not independently verified rights clearance. The transformations are label matching, counting, sampling and removal of job prose; no endorsement by source publishers is implied.

Versioned URLs, CSV record locators, column names, archive/member hashes, text offsets and excerpt hashes permit source replay after restoring the raw ZIPs from recoverable local Trash or obtaining the pinned versions from Kaggle. Archives are not required to read this evidence, but are required to independently replay it. Future availability of Kaggle versions is not guaranteed. No raw archive is committed.
''')
    tracked_artifacts = list(out.iterdir()) + [dest / p for p in ['schemas/source-occurrence.schema.json', 'tools/publish_kaggle_evidence.py', 'tools/verify_kaggle_publication.py']]
    write(out / 'manifest.json', {str(p.relative_to(dest)): {'sha256': digest(p), 'bytes': p.stat().st_size} for p in sorted(tracked_artifacts) if p.is_file()})
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
