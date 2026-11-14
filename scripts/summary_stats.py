"""Print reproducible summary counts from the current checkout as JSON (no writes).

    python3 -I scripts/summary_stats.py

Classes use lexicon.top_class; backing uses lexicon.backs. Counts describe
records and claims, not validated human capabilities or labor-market demand.
"""
import collections
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import lexicon as L
import tags_to_candidates as T


def tally(values):
    return dict(sorted(collections.Counter(values).items()))


def jsonl(path):
    return [json.loads(line) for line in path.read_text('utf-8').splitlines() if line.strip()]


def main():
    entries, errors = L.load(ROOT / 'entries')
    errors += L.validate(entries) + L.check_runs(entries, L.load_runs(ROOT))
    if errors:
        raise SystemExit('\n'.join(errors))
    forms = {L.norm(f['label']) for e in entries for f in L.forms(e)}
    relations = [r for e in entries for r in e.get('relations', [])]
    backed = {(e['id'], v['field']) for e in entries for v in e.get('evidence', []) if L.backs(v)}
    human_backed = {(e['id'], v['field']) for e in entries for v in e.get('evidence', [])
                    if L.backs(v) and v['by'].startswith('human:')}
    contradictions = [(e['id'], v) for e in entries for v in e.get('evidence', [])
                      if v['action'] == 'checked' and v.get('outcome') == 'contradicts' and v['by'].startswith('model:')]
    reviewers = collections.defaultdict(set)
    for eid, ev in contradictions:
        reviewers[(eid, ev['field'])].add(ev['by'])
    groups = T.read_tags(ROOT, [T.TAGS] + list(T.LISTS.values()))
    tags = {L.norm(g['term']) for g in groups}
    decisions = json.loads((ROOT / 'data/term-decisions.json').read_text('utf-8'))
    decided = {L.norm(d['term']) for d in decisions}
    abilities = json.loads((ROOT / 'abilities/onet-abilities.json').read_text('utf-8'))['abilities']
    with (ROOT / 'abilities/onet-occupations.csv').open(encoding='utf-8', newline='') as f:
        occupations = list(csv.DictReader(f))
    with (ROOT / 'abilities/onet-ability-ratings-all-occupations.csv').open(encoding='utf-8', newline='') as f:
        ratings = list(csv.DictReader(f))
    votes = jsonl(ROOT / 'data/assessments.jsonl')
    result = {
        'entries': len(entries),
        'classes': tally(L.top_class(e) for e in entries),
        'kinds': {k: sum(e['kind'] == k for e in entries) for k in sorted(L.KINDS)},
        'statuses': {s: sum(e['status'] == s for e in entries) for s in sorted(L.STATUSES)},
        'variants': sum(len(e.get('variants', [])) for e in entries),
        'entries_with_variants': sum(bool(e.get('variants')) for e in entries),
        'distinct_normalized_names_and_variants': len(forms),
        'relations': {'total': len(relations), 'by_type': tally(r['type'] for r in relations),
                      'rollup_enabled': sum(bool(r.get('rollup')) for r in relations)},
        'claims': {'total': sum(len(L.claim_keys(e)) for e in entries), 'backed': len(backed),
                   'human_backed': len(human_backed)},
        'descriptions': sum('description' in e for e in entries),
        'contradictions': {'records': len(contradictions), 'entries': len({eid for eid, _ in contradictions}),
                           'claims_with_two_or_more_models': sum(len(s) >= 2 for s in reviewers.values()),
                           'description_claims': len({eid for eid, v in contradictions if v['field'] == 'description'})},
        'votes': {'records': len(votes), 'answers': tally(v['answer'] for v in votes)},
        'legacy_tags': {'distinct_across_three_lists': len(tags), 'matched_to_names_or_variants': len(tags & forms),
                        'with_recorded_decisions': len(tags & decided), 'matched_and_decided': len(tags & forms & decided),
                        'decision_only': len((tags & decided) - forms), 'unresolved': len(tags - forms - decided),
                        'decision_records': tally(d['decision'] for d in decisions),
                        'distinct_per_file': {f: len(T.read_tags(ROOT, [f])) for f in [T.TAGS] + list(T.LISTS.values())}},
        'wikipedia_resolved': tally(r['relation'] for r in jsonl(ROOT / 'data/wikipedia-match/20261001/resolved.jsonl')),
        'onet_abilities': {'definitions': len(abilities), 'categories': tally(a['category'] for a in abilities),
                           'occupation_titles': len(occupations), 'rated_occupations': len({r['soc_code'] for r in ratings}),
                           'rating_rows': len(ratings), 'unique_occupation_ability_pairs': len({(r['soc_code'], r['element_id']) for r in ratings}),
                           'suppressed_rows': sum(r['recommend_suppress'] == 'true' for r in ratings),
                           'not_relevant_rows': sum(r['not_relevant'] == 'true' for r in ratings)},
        'credential_scope': tally(e.get('certification_scope', 'unset') for e in entries if e['kind'] == 'credential'),
        'language_type_flags': tally(e.get('language_type', 'unset') for e in entries if L.top_class(e) == 'language'),
        'validation_errors': 0,
    }
    assert sum(result['classes'].values()) == len(entries)
    assert sum(result['kinds'].values()) == len(entries)
    assert sum(result['wikipedia_resolved'].values()) == len(entries)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
