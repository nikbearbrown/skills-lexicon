import json, os, glob, sys
ROOT = '/home/user/rounds/round-05/a1/skills-lexicon'
GK = 'general-knowledge'
answers = {}

def gk(x): return {"value": x, "basis": GK}

def new(slug_prefix, name, kind, definition, reason, variants=(), relations=(), verbs=(),
        cert=False, scope=None, lang=None, note=""):
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for (t, tg) in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": gk(cert),
        "language_type": gk(lang),
        "annotation_note": note,
    }
    if cert:
        entry["certification_scope"] = gk(scope)
    answers[slug_prefix] = {"decision": "new", "variant_of": None, "reason": reason, "entry": entry}

def variant(slug, target, reason):
    answers[slug] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def nas(slug, reason):
    answers[slug] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(slug, reason):
    answers[slug] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

variant('f-sharp-programming-language', 'wonwpe2z38', 'Same language as F#, written out as F Sharp.')
variant('fali-language', 'q0vx2lgkj8', 'Same language as the existing Fali entry.')
variant('family-nursing-practitioner', 's67dm9xjpz', 'Almost certainly a misspelling of Family Nurse Practitioner.')

new('flight-planning', 'Flight planning', 'skill',
    'Preparing a flight by choosing the route, altitude, fuel and alternates from weather, airspace and aircraft performance information.',
    'A recognised aviation skill; the nearest entry is a different concept.', verbs=['perform'])
new('flipped-classroom-model', 'Flipped classroom', 'method',
    'A teaching approach in which students meet new material before class, usually by video or reading, and class time is used for practice and discussion.',
    'A named teaching method.', verbs=['implement'])
new('floating-point', 'Floating-point arithmetic', 'knowledge',
    'How computers represent and calculate with real numbers as a sign, a significand and an exponent, including rounding and precision limits.',
    'A computing concept; the nearest entries are unrelated.')
nas('floor-area', 'A measurement of a building or room, not a skill.')
nas('floor-care-technician', 'A job title.')
unsure('fluid-hyper-text-markup-language-fhtml', 'I do not recognise FHTML as an established markup language and will not guess a definition.')
new('fluid-statics', 'Fluid statics', 'knowledge',
    'The branch of fluid mechanics that studies fluids at rest, including pressure, buoyancy and the forces fluids exert on surfaces.',
    'A standard physics and engineering field; the nearest entries are unrelated.')
new('flutter-software', 'Flutter', 'framework',
    "Google's open-source toolkit for building natively compiled mobile, web and desktop apps from one codebase, written in the Dart language.",
    'A named software framework; no nearest entry is the same.', verbs=['build', 'develop'])
unsure('flutter-valves', 'It could mean valve flutter (a valve instability) or a type of valve; I cannot tell which is meant.')
nas('fluvial', 'An adjective meaning relating to rivers, not a skill by itself.')
unsure('flux', 'Ambiguous: could be the Flux GitOps tool, the Flux UI pattern, solder flux, the physics quantity or others.')
new('flux-analysis', 'Flux analysis', 'skill',
    'Comparing financial statement figures from one period to another and investigating and explaining the changes.',
    'The usual accounting sense; the term has other senses in science, so a person should confirm.',
    verbs=['perform', 'prepare'])
new('flux-cd', 'Flux CD', 'tool',
    'A GitOps tool, part of the Cloud Native Computing Foundation, that keeps Kubernetes clusters in line with configuration stored in Git.',
    'A named open-source tool.', variants=['FluxCD'], verbs=['deploy', 'configure'])
nas('focusing', 'A generic word with several unrelated meanings.')
new('foglight-database-software', 'Foglight', 'tool',
    "Quest Software's performance monitoring product for databases, applications and infrastructure.",
    'A named commercial monitoring product.', verbs=['monitor', 'configure'])
new('folk-music', 'Folk music', 'knowledge',
    'Traditional music of a community or region, often passed on by ear, and the styles descended from it.',
    'A music genre and body of knowledge.', verbs=['perform', 'teach'])
new('font-awesome', 'Font Awesome', 'library',
    'A toolkit of scalable vector icons, supplied as icon fonts and SVG, that web developers add to sites and apps.',
    'A named web icon library.', verbs=['use', 'integrate'])
new('food-economics', 'Food economics', 'knowledge',
    'The study of how food is produced, priced, distributed and consumed, and of the markets and policies around it.',
    'An applied economics field.')
new('food-microbiology', 'Food microbiology', 'knowledge',
    'The study of the microorganisms that spoil food, cause foodborne illness or are used to make foods such as cheese and yoghurt.',
    'A standard food science field.')
new('food-plating-and-presentation', 'Food plating and presentation', 'skill',
    'Arranging and garnishing prepared food on a plate or serving dish so that it looks appealing.',
    'A culinary skill.', verbs=['perform'])
new('food-preservation', 'Food preservation', 'skill',
    'Treating or storing food, for example by canning, freezing, drying, salting or pickling, to stop it spoiling.',
    'A food handling skill; the nearest entry is unrelated.')
new('food-process-engineering', 'Food process engineering', 'knowledge',
    'The branch of engineering that designs and runs the processes and equipment that turn raw agricultural materials into food products.',
    'A recognised engineering field; the nearest entries are other engineering fields.')
new('food-procurement', 'Food procurement', 'skill',
    'Sourcing, buying and receiving food products for an organisation, including choosing suppliers and negotiating prices.',
    'A purchasing skill.')
new('food-safety', 'Food safety', 'knowledge',
    'Practices for handling, preparing and storing food so that it does not cause illness.',
    'A standard public health and food service field.')
new('food-science', 'Food science', 'knowledge',
    'The study of the physical, chemical and biological nature of food and of how it is processed, preserved and made safe.',
    'A standard science field.', relations=[('related', 'xl6126omq1')])
new('food-systems-management', 'Food systems management', 'skill',
    'Managing a food service operation, including menu planning, purchasing, production, sanitation and service.',
    'Dietetics and food service management term; some uses mean the wider food supply chain.')
nas('foods', 'A generic plural word, at most a school subject name.')
new('footprinting', 'Footprinting', 'method',
    'The first step of a security assessment, collecting information about a target organisation, its networks and systems to plan later testing.',
    'A security term; the nearest entries are unrelated.', verbs=['perform'])
new('forced-draft-systems', 'Forced draft systems', 'knowledge',
    'Boiler and furnace air systems in which fans push combustion air into the furnace at above atmospheric pressure.',
    'A power and heating plant concept; the nearest entries are unrelated.')
new('foreign-account-tax-compliance-act', 'Foreign Account Tax Compliance Act', 'standard',
    'A 2010 United States law that requires foreign financial institutions to report accounts held by US taxpayers to the US tax authority.',
    'A named statute.', variants=['FATCA'])
new('forensic-dentistry-dentistry-branches', 'Forensic dentistry', 'knowledge',
    'The use of dental knowledge in legal matters, chiefly identifying human remains from dental records and features.',
    'A recognised branch of dentistry.', variants=['Forensic odontology'])
unsure('forensic-examiner-certification', 'Names no issuing body or discipline; forensic examiner certificates exist in several fields from several bodies.')
unsure('forge', 'Ambiguous: Minecraft Forge, Laravel Forge, Autodesk Forge, Atlassian Forge or metal forging.')
new('forklift-certification', 'Forklift certification', 'credential',
    'A certificate showing that a person has been trained and evaluated to operate a forklift safely.',
    'A credential for powered equipment operation; related to other lift certifications but a different concept.',
    relations=[('related', 'nuvqasz51i'), ('related', 'umpb7it897')],
    cert=True, scope='many-issuers')
new('forklift-safety', 'Forklift safety', 'knowledge',
    'Safe operating and working practices around forklifts, such as load handling, travel rules, inspection and pedestrian safety.',
    'A workplace safety topic.')
new('forklift-truck', 'Forklift truck', 'tool',
    'A powered industrial truck with forks at the front for lifting, carrying and stacking pallets and other loads.',
    'Equipment; the nearest entry is a different vehicle.', variants=['Forklift', 'Fork truck', 'Lift truck'],
    verbs=['operate'])
unsure('forming', 'Ambiguous: could be metal forming, plastics forming or an ordinary word.')
new('forth', 'Forth', 'programming-language',
    'A stack-based, extensible programming language created by Charles H. Moore.',
    'A well-known programming language.', lang='programming')
new('framer-js', 'Framer.js', 'library',
    'A JavaScript library for building interactive prototypes of user interfaces, originally the engine behind the Framer prototyping tool.',
    'A named JavaScript library; the near entries are other libraries.')
new('framerjs', 'Framer.js', 'library',
    'A JavaScript library for building interactive prototypes of user interfaces, originally the engine behind the Framer prototyping tool.',
    'Same concept as Framer.js, written without the dot.')
new('franchise-sales', 'Franchise sales', 'skill',
    'Selling franchise opportunities to prospective franchisees.',
    'A sales specialty; the nearest entries are different concepts.', verbs=['sell'])
new('fraud-prevention-and-detection', 'Fraud prevention and detection', 'skill',
    'Putting controls in place to stop fraud and analysing transactions and behaviour to spot it when it happens.',
    'A recognised risk and finance skill.')
new('fraud-risk-assessments', 'Fraud risk assessment', 'method',
    'A structured review that identifies where and how fraud could occur in an organisation and how likely and damaging it would be.',
    'A named assessment method.', verbs=['conduct'])
new('fraud-risk-management', 'Fraud risk management', 'skill',
    'Identifying, assessing and controlling the risk of fraud against an organisation.',
    'A recognised risk skill, related to other risk management entries.',
    relations=[('related', 'vivxc5g99i'), ('related', 'qbsb11tob5')])
new('free-body-diagrams', 'Free body diagrams', 'method',
    'Sketches of one body isolated from its surroundings that show every force and moment acting on it, used to solve mechanics problems.',
    'A standard mechanics technique.', verbs=['draw'])
new('free-lossless-audio-codec-flac', 'Free Lossless Audio Codec', 'standard',
    'An open, royalty-free format for compressing digital audio without losing any of the original data.',
    'A named audio format.', variants=['FLAC'])
unsure('free-trade-zones', 'Names a type of place; whether it means customs and trade-compliance knowledge needs a person to decide.')
nas('freezing', 'A generic word with several unrelated meanings.')
unsure('frege', 'Could be the Frege programming language for the JVM or the philosopher Gottlob Frege.')
new('freight-handling', 'Freight handling', 'skill',
    'Loading, unloading, moving and securing freight at docks, warehouses and terminals.',
    'A logistics skill.', verbs=['perform'])
new('freight-handling-equipment', 'Freight handling equipment', 'tool',
    'Equipment used to move and load freight, such as forklifts, pallet jacks, conveyors and dock levelers.',
    'A category of logistics equipment.', verbs=['operate'])
new('freight-inspection', 'Freight inspection', 'skill',
    'Checking shipments for damage, correct count and conformity with shipping documents when they are received or sent.',
    'A logistics skill; the nearest entries are different concepts.', verbs=['perform'])
nas('fresh-product', 'A generic product category, not a skill.')
new('freshchat', 'Freshchat', 'platform',
    'A messaging and live chat product from Freshworks that businesses use to talk with customers.',
    'A named customer messaging product.', verbs=['configure', 'use'])
new('frisby-js', 'Frisby.js', 'framework',
    'A Node.js framework for writing tests of REST API endpoints.',
    'A named JavaScript testing framework.', verbs=['write'])
new('frisian-language', 'Frisian', 'human-language',
    'A group of closely related West Germanic languages spoken in the Netherlands and Germany, of which West Frisian is the most widely spoken.',
    'A human language.', lang='human')
new('frontify-software', 'Frontify', 'platform',
    'A cloud platform for brand management that stores brand guidelines and assets and shares them across teams.',
    'A named commercial platform; the nearest entries are other products.')
new('fuel-cell', 'Fuel cell', 'knowledge',
    'A device that converts the chemical energy of a fuel, commonly hydrogen, directly into electricity through an electrochemical reaction.',
    'A standard energy technology.')
new('full-cycle-sales', 'Full-cycle sales', 'skill',
    'Handling the whole sales process alone, from finding prospects through negotiation to closing the deal.',
    'A recognised sales role style.')
unsure('full-option-science-systems', 'A named K-8 science curriculum (FOSS), but none of the allowed kinds clearly fits a curriculum.')
new('full-stack-observability', 'Full-stack observability', 'skill',
    'Observability across every layer of a system, from infrastructure and network to applications and user experience.',
    'A narrower form of Observability.', relations=[('broader', 'f4pwxnygi1')])
new('full-stack-software-engineering', 'Full-stack software engineering', 'skill',
    'Building both the user-facing front end and the server-side back end of software.',
    'A common engineering skill, narrower than software engineering.',
    relations=[('broader', 'qmravcc671'), ('related', 'hty63xrb26')])
unsure('funcitonal-process', 'A misspelt phrase; it may be the function-point sizing term or a generic phrase, and I cannot tell which.')
new('functional-independence-measure-fim', 'Functional Independence Measure', 'tool',
    "An 18-item clinical scale that rates a patient's need for help with daily activities, used mainly in rehabilitation.",
    'A named clinical assessment instrument, not a credential.',
    note='FIM is a patient assessment scale, not a credential, so the legacy certification list is mistaken.')
unsure('fundamental-modeling-concepts', 'May be the Fundamental Modeling Concepts (FMC) notation for software systems or just a generic phrase; I cannot tell.')
unsure('funnels', 'Ambiguous: sales or marketing funnels, or the physical object.')
nas('furnishing', 'A generic word for supplying furniture, not a skill.')
new('fuseesb', 'Fuse ESB', 'platform',
    'An open-source enterprise service bus based on Apache ServiceMix, from FuseSource and later part of Red Hat Fuse.',
    'Run-together spelling of the Fuse ESB integration product.', verbs=['deploy', 'configure'])
new('g-suite', 'Google Workspace', 'platform',
    "Google's subscription suite of cloud productivity and collaboration apps such as Gmail, Docs, Drive and Meet, known as G Suite until its 2020 rename.",
    'G Suite is the former name of Google Workspace.', verbs=['administer', 'use'])
new('gaelic-language', 'Gaelic', 'human-language',
    'The Goidelic Celtic languages, namely Irish, Scottish Gaelic and Manx, with the word most often meaning Scottish Gaelic or Irish depending on context.',
    'A human language name that covers more than one language.', lang='human')
new('gait-training', 'Gait training', 'method',
    'A physical therapy technique that helps people relearn or improve walking.',
    'A rehabilitation method; the nearest entries are different concepts.', verbs=['provide'])
new('gallio', 'Gallio', 'platform',
    'An open-source test automation platform for .NET that runs tests written with several test frameworks, including MbUnit.',
    'A named .NET testing platform.', verbs=['run'])
new('galo-language', 'Galo', 'human-language',
    'A Tibeto-Burman language spoken mainly in Arunachal Pradesh, India.',
    'A human language.', lang='human')
new('gambas', 'Gambas', 'programming-language',
    'A free, object-oriented BASIC-like programming language and development environment for Linux.',
    'A named programming language.', lang='programming')
new('game-art', 'Game art', 'skill',
    'Creating the visual assets of video games, such as characters, environments, props and effects.',
    'A recognised games production skill.', verbs=['create'])
new('game-design', 'Game design', 'skill',
    'Designing the rules, mechanics, systems and content of a game.',
    'A recognised games skill; the nearest entries are other design fields.', verbs=['design'])
new('garifuna-language', 'Garifuna', 'human-language',
    'An Arawakan language spoken by the Garifuna people along the Caribbean coast of Central America.',
    'A human language.', lang='human')
nas('garmin', 'A company name.')
new('gas-meter-systems', 'Gas meter systems', 'knowledge',
    'Devices and supporting systems that measure, record and report the gas a customer uses, including mechanical and smart gas meters.',
    'A utility metering topic; the nearest entries are unrelated.')
new('gastric-bypass-surgeries', 'Gastric bypass surgery', 'knowledge',
    'A bariatric operation that makes a small stomach pouch and reroutes the small intestine to limit how much food is eaten and absorbed.',
    'A specific bariatric operation, narrower than Bariatric surgery.', relations=[('broader', 'dfc9xr7d51')])
nas('gastrointestinal-bleeding', 'A medical condition or symptom, not a skill.')

giac = [
 ('giac-certified-enterprise-defender-gced', 'GIAC Certified Enterprise Defender', 'GCED',
  'A GIAC certification for practitioners who defend enterprise networks and systems with defensive techniques and tools.', []),
 ('giac-cyber-threat-intelligence', 'GIAC Cyber Threat Intelligence', 'GCTI',
  'A GIAC certification for analysts who collect, analyse and apply cyber threat intelligence.', [('related', 'ajeetx04pv')]),
 ('giac-exploit-researcher-and-advanced-pen', 'GIAC Exploit Researcher and Advanced Penetration Tester', 'GXPN',
  'A GIAC certification for advanced penetration testers who find and exploit vulnerabilities in systems, networks and software.', []),
 ('giac-global-industrial-cyber-security-pr', 'GIAC Global Industrial Cyber Security Professional', 'GICSP',
  'A GIAC certification on securing industrial control systems, bridging IT, engineering and cybersecurity.', []),
 ('giac-information-security-fundamentals', 'GIAC Information Security Fundamentals', 'GISF',
  'An entry-level GIAC certification covering core information security concepts.', []),
 ('giac-network-forensic-analyst', 'GIAC Network Forensic Analyst', 'GNFA',
  'A GIAC certification for investigators who analyse network traffic and evidence in forensic investigations.', []),
 ('giac-penetration-tester', 'GIAC Penetration Tester', 'GPEN',
  'A GIAC certification for penetration testers who run structured security tests of systems and networks.', []),
 ('giac-security-essentials-certification', 'GIAC Security Essentials', 'GSEC',
  'A GIAC certification covering the essential information security skills and terms expected of hands-on security practitioners.', []),
 ('giac-web-application-defender', 'GIAC Web Application Defender', 'GWEB',
  'A GIAC certification for people who defend web applications and understand web application security.', []),
 ('giac-web-application-penetration-tester', 'GIAC Web Application Penetration Tester', 'GWAPT',
  'A GIAC certification for testers who assess the security of web applications.', []),
]
for slug, name, acr, d, rel in giac:
    new(slug, name, 'credential', d, 'A GIAC certification, awarded only by GIAC.',
        variants=[acr], relations=rel, cert=True, scope='single-issuer')

new('gis-certificate', 'GIS certificate', 'credential',
    'A certificate awarded for completing a course of study in geographic information systems.',
    'A credential awarded by many institutions.', cert=True, scope='many-issuers')
new('gis-mapping', 'GIS mapping', 'skill',
    'Making and analysing maps with geographic information systems.',
    'A recognised geospatial skill; Crime mapping is a related application.',
    relations=[('related', 'dob6za2tys')], verbs=['create'])
new('gmp-self-inspection', 'GMP self-inspection', 'method',
    'An internal inspection a manufacturer carries out to check its own operations against good manufacturing practice requirements.',
    'A quality assurance method; the nearest entry is a different inspection.', verbs=['conduct'])
new('gre-generic-routing-encapsulation-tunnel', 'Generic Routing Encapsulation', 'standard',
    'A tunnelling protocol, defined in RFC 2784, that wraps packets of one network protocol inside IP packets so they can cross another network.',
    'A networking protocol, commonly called GRE tunneling.', verbs=['configure'])
new('gsm-radio-access-networks', 'GSM radio access network', 'knowledge',
    'The part of a GSM mobile network, made up of base transceiver stations and base station controllers, that connects phones to the core network.',
    'A telecom network concept.')
unsure('gsm-services', 'Probably telecom services on GSM networks, but the phrase is too vague to define confidently.')

# ---- write ----
reqs = sorted(glob.glob(os.path.join(ROOT, 'work/requests/*.json')))
os.makedirs(os.path.join(ROOT, 'work/responses'), exist_ok=True)
used = set()
missing = []
for f in reqs:
    b = os.path.basename(f)
    stem = b[:-5]
    # match by slug prefix: stem minus trailing -<6 hex>
    slug = stem.rsplit('-', 1)[0]
    if slug not in answers:
        missing.append(stem); continue
    used.add(slug)
    with open(os.path.join(ROOT, 'work/responses', b), 'w') as fh:
        json.dump(answers[slug], fh, indent=1, ensure_ascii=False)
print('requests', len(reqs), 'written', len(used), 'missing', missing, 'unused', set(answers) - used)
