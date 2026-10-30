#!/usr/bin/env python3
"""Validate the published projection without opening or downloading raw archives."""
import collections
import hashlib
import json
from pathlib import Path
import sys
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/source-occurrences/kaggle-publication-2026-10-30'

def read(name):
    return json.loads((OUT / name).read_text())

def main():
    for rel, item in read('manifest.json').items():
        path = ROOT / rel
        assert path.stat().st_size == item['bytes'], rel
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], rel
    schema = json.loads((ROOT / 'schemas/source-occurrence.schema.json').read_text())
    validator = jsonschema.Draft202012Validator(schema)
    sources, registry, summary = read('sources.json'), read('subject-registry.json'), read('summary.json')
    observations, subjects, refs = {}, set(), set()
    by_candidate = collections.defaultdict(set)
    for line in (OUT / 'observations.jsonl').open():
        row = json.loads(line)
        validator.validate(row)
        obs = row['observation']
        oid = obs['observation_id']
        assert oid not in observations, oid
        observations[oid] = row
        key = row.get('id', row.get('candidate_key'))
        subjects.add(key)
        assert row['subject'] == registry[key]['subject'], key
        source = sources[obs['source_id']]
        assert source['publication_status'] == 'observations-published'
        assert source['dataset_ref'] not in summary['omission_reasons']
        for a, b in [('member', 'member'), ('member_sha256', 'member_sha256'), ('dataset_version', 'version'), ('source_url', 'url'), ('license_as_recorded', 'license_as_recorded')]:
            assert obs[a] == source[b], (oid, a)
        assert all('quote' not in example for example in obs['examples'])
        c = obs['counts']
        assert c['records'] == c['records_without_resolution_flags'] + c['records_requiring_resolution']
        refs.add(source['dataset_ref'])
        if 'candidate_key' in row:
            by_candidate[key].add(oid)
    queue = read('candidate-queue.json')
    assert len({c['candidate_key'] for c in queue}) == len(queue)
    for candidate in queue:
        assert candidate['review_status'] == 'pending'
        assert set(candidate['observation_ids']) == by_candidate[candidate['candidate_key']]
        linked = [observations[oid]['observation'] for oid in candidate['observation_ids']]
        assert candidate['published_dataset_count'] == len({sources[o['source_id']]['dataset_ref'] for o in linked})
        assert candidate['published_source_family_count'] == len({o['source_family'] for o in linked})
        assert candidate['published_field_record_matches'] == sum(o['counts']['records'] for o in linked if o['claim'].endswith('skill-field'))
    assert len(observations) == summary['published_observations']
    assert len(refs) == summary['published_datasets']
    assert len(subjects - set(by_candidate)) == summary['existing_entries_linked']
    assert len(observations) + sum(summary['omitted_observations'].values()) == summary['local_observations']
    assert sum(c['triage'] == 'pending' for c in queue) == summary['active_pending_candidates']
    assert sum(c['triage'] == 'scope-hold' for c in queue) == summary['scope_holds']
    print(json.dumps({'passed': True, 'schema_valid_observations': len(observations), 'datasets': len(refs), 'candidate_proposals_including_scope_holds': len(queue), 'raw_archives_read': 0}, indent=2))

if __name__ == '__main__':
    main()
