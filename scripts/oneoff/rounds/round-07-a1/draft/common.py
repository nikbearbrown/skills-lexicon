import glob, json, os

REQS = sorted(glob.glob('work/requests/*.json'))
GK = 'general-knowledge'
KINDS = set(json.load(open(REQS[0]))['allowed']['kinds'])
SEEN = set()


def _req(i, term):
    r = json.load(open(REQS[i]))
    assert r['term'] == term, (i, r['term'], term)
    return r


def _write(i, resp):
    assert i not in SEEN, i
    SEEN.add(i)
    with open('work/responses/' + os.path.basename(REQS[i]), 'w', encoding='utf-8') as f:
        json.dump(resp, f, indent=1, ensure_ascii=False)
        f.write('\n')


def NEW(i, term, name, kind, definition, reason, variants=(), rel=(), cert=False, scope=None, lang=None, note=''):
    r = _req(i, term)
    assert kind in KINDS, kind
    near = {x['id'] for x in r['nearest']}
    relations = []
    for t, tgt in rel:
        assert tgt in near, (i, tgt)
        relations.append({'type': t, 'target': tgt, 'basis': GK})
    if cert:
        assert scope in ('single-issuer', 'many-issuers')
    entry = {
        'preferred_name': name, 'kind': kind, 'definition': definition, 'definition_basis': GK,
        'variants': [{'label': v, 'basis': GK} for v in variants],
        'relations': relations,
        'verbs': [],
        'certification': {'value': bool(cert), 'basis': GK},
        'language_type': {'value': lang, 'basis': GK},
        'annotation_note': note,
    }
    if cert:
        entry['certification_scope'] = {'value': scope, 'basis': GK}
    _write(i, {'decision': 'new', 'variant_of': None, 'reason': reason, 'entry': entry})


def VAR(i, term, target, reason):
    r = _req(i, term)
    assert target in {x['id'] for x in r['nearest']}, (i, target)
    _write(i, {'decision': 'variant_of', 'variant_of': target, 'reason': reason, 'entry': None})


def NAS(i, term, reason):
    _req(i, term)
    _write(i, {'decision': 'not_a_skill', 'variant_of': None, 'reason': reason, 'entry': None})


def UNS(i, term, reason):
    _req(i, term)
    _write(i, {'decision': 'unsure', 'variant_of': None, 'reason': reason, 'entry': None})
