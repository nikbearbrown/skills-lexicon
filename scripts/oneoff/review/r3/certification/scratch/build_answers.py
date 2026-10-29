import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PK = os.path.join(HERE, '..', 'packets')
OUT = os.path.join(HERE, '..', 'answers')
S, C, U = 'supports', 'contradicts', 'unsure'

# Overrides per key: claim verdicts (default supports), notes, bad variants, bad relations, vote.
# Format: key -> dict(definition=(verdict, note), kind=..., certification=..., certification_scope=...,
#                     bad_variants={label: note}, bad_relations={rel: note}, vote=(answer, reason))
O = {
    # ---------------- p007 ----------------
    'giac-certification': dict(definition=(S, 'GIAC was founded by the SANS Institute in 1999.')),
    'giac-certified-enterprise-defender': dict(
        bad_variants={'GCED': 'Also UNESCO shorthand for Global Citizenship Education, common in education job ads.'}),
    'gis-certificate': dict(definition=(S, 'Academic certificate; distinct from the GISP professional certification of GISCI.')),
    'google-ads-certification': dict(definition=(S, 'Several Google Ads certifications exist (Search, Display, Video, Shopping, Measurement, etc.).')),
    'google-analytics-certification': dict(definition=(S, 'Formerly the Google Analytics Individual Qualification (GAIQ).')),
    'google-digital-marketing-certificate': dict(definition=(S, 'Name is shared by the Coursera Digital Marketing & E-commerce cert and the Digital Garage course certificate.')),
    'graduate-realtor-institute': dict(certification_scope=(U, 'One NAR-owned designation awarded through NAR-affiliated state associations; arguably single-issuer.')),
    'hazmat-endorsement': dict(definition=(S, 'US CDL "H" endorsement; needs a TSA security threat assessment and knowledge test, issued by state DMVs.')),
    'higher-national-certificate': dict(definition=(S, 'RQF level 4 / SCQF level 7; Pearson BTEC in England, Wales and NI, SQA in Scotland.')),
    'housing-credit-certified-professional': dict(definition=(S, 'HCCP is awarded by the National Association of Home Builders (NAHB).')),
    'iam-level-ii-certification': dict(
        definition=(S, 'DoD 8570.01-M has been superseded by DoD 8140 (manual 8140.03), though listings still use the term.'),
        certification=(S, 'A category met by holding an approved cert (e.g. CISSP, CISM), not a credential itself.')),
    'iam-level-iii-certification': dict(
        definition=(S, 'DoD 8570.01-M has been superseded by DoD 8140 (manual 8140.03), though listings still use the term.'),
        certification=(S, 'A category met by holding an approved cert (e.g. CISSP, CISM), not a credential itself.')),
    'iat-level-i-certification': dict(
        definition=(S, 'DoD 8570.01-M has been superseded by DoD 8140 (manual 8140.03), though listings still use the term.'),
        certification=(S, 'A category met by holding an approved cert (e.g. A+, Network+), not a credential itself.')),
    'iat-level-ii-certification': dict(
        definition=(S, 'DoD 8570.01-M has been superseded by DoD 8140 (manual 8140.03), though listings still use the term.'),
        certification=(S, 'A category met by holding an approved cert (e.g. Security+, GSEC), not a credential itself.')),
    'iat-level-iii-certification': dict(
        definition=(S, 'DoD 8570.01-M has been superseded by DoD 8140 (manual 8140.03), though listings still use the term.'),
        certification=(S, 'A category met by holding an approved cert (e.g. CISSP, CASP+), not a credential itself.')),
    'international-computer-driving-licence': dict(definition=(S, 'ECDL was the European name, ICDL the name elsewhere until the brand was unified; also has advanced modules.')),
    # ---------------- p008 ----------------
    'international-general-certificate-of-secondary-education': dict(definition=(S, '"IGCSE" is Cambridge\'s brand; Pearson Edexcel and others call theirs "International GCSE".')),
    'ipma-certified-project-management-associate': dict(certification_scope=(U, 'One IPMA-defined scheme awarded by IPMA member associations\' certification bodies; arguably single-issuer.')),
    'itil-expert': dict(definition=(S, 'ITIL Master sat above Expert; MALC exam also required for the 22 credits; v3 scheme now retired.')),
    'itil-foundation': dict(definition=(S, 'Owned by AXELOS, now PeopleCert; current version is ITIL 4 Foundation.')),
    'itil-practitioner': dict(definition=(S, 'Describes the 2016 v3-era exam, since withdrawn; ITIL 4 also has newer "Practitioner" practice modules.')),
    'kenya-certificate-of-primary-education': dict(definition=(S, 'Phased out under the CBC reform; last sat in 2023, replaced by KPSEA.')),
    'leadership-certificate': dict(definition=(S, 'Generic; covers many unrelated programmes.')),
    'licensed-practical-nurse': dict(definition=(S, 'Also a regulated title in Canada; called LVN in California and Texas.')),
    'licensed-professional-engineer': dict(definition=(S, 'Also used for P.Eng. licences in Canada and similar elsewhere.')),
    'master-of-health-administration': dict(
        bad_variants={'MHA': 'Also Mental Health Act (UK) and Ministry of Home Affairs, both common in job ads.'}),
    'master-of-public-administration': dict(
        bad_variants={'MPA': 'Also Master of Professional Accounting (e.g. UT Austin), MPa pressure unit, marine protected area.'}),
    'medication-aide-assistant-certification-examination': dict(
        definition=(S, 'NCSBN\'s MACE exam, used by several state boards to certify medication aides.'),
        kind=(S, 'Names an exam; credential is the closest allowed kind.'),
        certification=(S, 'Passing leads to state certification as a medication aide.'),
        certification_scope=(U, 'The exam is NCSBN\'s alone; the resulting certification is state-issued.')),
    'microsoft-certified-systems-administrator': dict(definition=(S, 'Retired; MCSA later meant Microsoft Certified Solutions Associate, itself retired in 2021.')),
    'microsoft-dynamics-365-field-service-certification': dict(definition=(S, 'Formally Dynamics 365 Field Service Functional Consultant Associate (MB-240).')),
    'mobile-electronics-certified-professional': dict(definition=(S, 'Run by the Consumer Technology Association (formerly CEA).')),
    'nurse-practitioner': dict(definition=(S, 'US-centric; NP is also a regulated role in Canada, Australia and elsewhere.')),
    'occupational-health-and-safety-technologist': dict(definition=(S, 'Originally from CCHEST, which merged into BCSP.')),
    # ---------------- p009 ----------------
    'oracle-certified-associate': dict(definition=(S, 'Some tracks had Junior/Foundations Associate levels; Oracle has since renamed many credentials.')),
    'oracle-certified-master': dict(definition=(S, 'OCM typically requires advanced training and a multi-hour hands-on practical exam.')),
    'oracle-database-11g-administrator-certified-associate': dict(definition=(S, 'Legacy credential for a retired database version.')),
    'osha-safety-certificate': dict(
        definition=(S, 'OSHA says Outreach DOL cards are not certification; other "OSHA" certificates come from training providers.'),
        certification_scope=(U, 'Outreach cards are OSHA-issued via trainers, but many "OSHA certificates" are issued by private providers.')),
    'peace-officer-certification': dict(definition=(S, 'Usually a state POST body rather than a local one.')),
    'pediatric-advanced-life-support': dict(
        definition=(S, 'AHA originated PALS, but the American Red Cross and others also run PALS courses.'),
        certification_scope=(C, 'Not single-issuer: American Red Cross and other providers also award PALS cards.')),
    'pega-certified-business-architect': dict(definition=(S, 'Issuer is Pegasystems.')),
    'psychiatric-mental-health-nurse-practitioner': dict(certification_scope=(U, 'Board certification (PMHNP-BC) is ANCC\'s; licences are state-issued; scope depends on reading.')),
    'registered-clinical-exercise-physiologist': dict(
        definition=(S, 'ACSM credential, reportedly folded into ACSM-CEP; UK also has a Register of Clinical Exercise Physiologists.'),
        bad_variants={'RCEP': 'Also the Regional Comprehensive Economic Partnership trade agreement.'}),
    'registered-dietitian': dict(
        definition=(S, 'US definition; also a regulated title elsewhere (e.g. UK HCPC, Canadian provinces). CDR now needs a graduate degree.'),
        certification_scope=(S, 'Single-issuer for the US credential; other countries regulate the title separately.')),
    'red-hat-certified-engineer': dict(definition=(S, 'Current RHCE centres on Ansible automation.')),
}

def claim(v):
    if isinstance(v, tuple):
        verdict, note = v
        d = {'verdict': verdict}
        if note:
            assert len(note) <= 150, (note, len(note))
            d['note'] = note
        return d
    return {'verdict': v}

CLAIMS = ['definition', 'kind', 'certification', 'certification_scope', 'language_type']

for p in ['p007', 'p008', 'p009']:
    entries = json.load(open(os.path.join(PK, p + '.json')))['entries']
    out = []
    for e in entries:
        o = O.get(e['key'], {})
        claims = {}
        for c in CLAIMS:
            if c in e:
                claims[c] = claim(o.get(c, S))
        bv = o.get('bad_variants', {})
        for lab in bv:
            assert lab in e.get('variants', []), (e['key'], lab)
            assert len(bv[lab]) <= 150
        variants = {'ok': [v for v in e.get('variants', []) if v not in bv],
                    'bad': [{'label': k, 'note': n} for k, n in bv.items()]}
        br = o.get('bad_relations', {})
        relations = {'ok': [r for r in e.get('relations', []) if r not in br],
                     'bad': [{'rel': k, 'note': n} for k, n in br.items()]}
        ans, reason = o.get('vote', ('yes', None))
        vote = {'answer': ans}
        if reason:
            vote['reason'] = reason
        out.append({'key': e['key'], 'claims': claims, 'variants': variants,
                    'relations': relations, 'job_listing_vote': vote})
    unknown = set(O) - {e['key'] for e in entries}
    json.dump(out, open(os.path.join(OUT, p + '.json'), 'w'), indent=1, ensure_ascii=False)
    # tally
    cnt = {S: 0, C: 0, U: 0}
    for a in out:
        for c in a['claims'].values():
            cnt[c['verdict']] += 1
    vc = {}
    for a in out:
        vc[a['job_listing_vote']['answer']] = vc.get(a['job_listing_vote']['answer'], 0) + 1
    nbv = sum(len(a['variants']['bad']) for a in out)
    nov = sum(len(a['variants']['ok']) for a in out)
    print(p, len(out), 'claims', cnt, 'votes', vc, 'variants ok/bad', nov, nbv)

all_keys = set()
for p in ['p007', 'p008', 'p009']:
    all_keys |= {e['key'] for e in json.load(open(os.path.join(PK, p + '.json')))['entries']}
missing = set(O) - all_keys
assert not missing, missing
