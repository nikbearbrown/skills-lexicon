import json, glob, os, sys

GK = "general-knowledge"
reqs = {}
for f in sorted(glob.glob("work/requests/*.json")):
    r = json.load(open(f))
    reqs[r["term"]] = (os.path.basename(f), r)

ans = {}

def new(term, name, kind, definition, variants=(), relations=(), cert=False, scope=None, lang=None, note="", reason=None):
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        entry["certification_scope"] = {"value": scope, "basis": GK}
    ans[term] = {"decision": "new", "variant_of": None, "reason": reason or "A recognised skill, tool or body of knowledge with no match in nearest.", "entry": entry}

def no(term, reason):
    ans[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(term, reason):
    ans[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def variant(term, target, reason):
    ans[term] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

# ---- E ----
new("Explosives Detection And Disposal", "Explosives detection and disposal", "skill",
    "Finding explosive devices and materials and making them safe or removing them, as bomb-squad and military ordnance disposal personnel do.")
new("Extended Parallel Process Model", "Extended Parallel Process Model", "knowledge",
    "A health-communication theory, proposed by Kim Witte, that explains how people respond to fear-based messages through their perceived threat and their perceived ability to act against it.",
    variants=["EPPM"])
new("Extended Reality", "Extended reality", "knowledge",
    "An umbrella term for technologies that combine real and virtual environments, including virtual, augmented and mixed reality.",
    variants=["XR"], relations=[("related", "sfte4xs6zx")])
new("Extended Validation Certificates", "Extended validation certificate", "knowledge",
    "A type of TLS/SSL digital certificate issued only after the certificate authority has checked in detail the legal identity of the organisation that requests it.",
    variants=["EV certificate"],
    reason="A kind of digital certificate used on websites, not a credential awarded to a person.")
unsure("Extensible Languages", "Could mean programming languages designed to be extended by their users, or XML-like markup languages; it is not clearly one language or one skill.")
new("Extensive Reading (Language Acquisition)", "Extensive reading", "method",
    "A language-learning approach in which learners read large amounts of easy, enjoyable material to build fluency and vocabulary.",
    note="It is a language-teaching approach, not a language, so the legacy language list is wrong here.",
    reason="A language-teaching method, not a language.")
no("External Affairs", "A department or function name, not a skill.")
no("External Auditor", "A job title, not a skill.")
new("External Stakeholder Management", "External stakeholder management", "skill",
    "Identifying and working with people and organisations outside the company, such as customers, regulators and partners, to understand their interests and keep their support.")
new("Extraction, Transformation, and Loading (ETL)", "Extract, transform, load", "method",
    "A data-integration process that pulls data from source systems, reshapes it, and loads it into a target such as a data warehouse.",
    variants=["ETL", "Extraction, Transformation, and Loading"])
new("Eye Surgeries", "Eye surgery", "knowledge",
    "Surgical operations on the eye and the tissues around it, such as cataract, glaucoma, retinal and corneal surgery.",
    variants=["Ophthalmic surgery"])

# ---- F ----
fsharp = dict(name="F#", kind="programming-language",
    definition="A functional-first programming language for the .NET platform, developed at Microsoft Research.",
    variants=["F Sharp"], lang="programming")
new("F Sharp", fsharp["name"], fsharp["kind"], fsharp["definition"], variants=fsharp["variants"], lang="programming")
new("F Sharp (Programming Language)", fsharp["name"], fsharp["kind"], fsharp["definition"], variants=fsharp["variants"], lang="programming")

new("Facebook", "Facebook", "platform",
    "A social networking platform, owned by Meta, where people and organisations post content, message each other and run ads.")
fa = dict(name="Facebook advertising", kind="skill",
    definition="Creating, targeting and managing paid ads on Facebook through Meta's advertising tools.",
    variants=["Facebook Ads"])
new("Facebook Advert", fa["name"], fa["kind"], fa["definition"], variants=fa["variants"])
new("Facebook Advertising", fa["name"], fa["kind"], fa["definition"], variants=fa["variants"])
unsure("Facebook Content", "Names posts on Facebook rather than clearly a skill; it may mean creating content for Facebook, which a person should decide.")
new("Facebook Marketing", "Facebook marketing", "skill",
    "Promoting a business or brand on Facebook through pages, posts, groups and paid ads.")
new("Facilities Management Administrator (FMA)", "Facilities Management Administrator", "credential",
    "A professional designation in facilities management awarded by BOMI International to people who complete its coursework and exams.",
    cert=True, scope="single-issuer")
new("Facility Maintenance", "Facility maintenance", "skill",
    "Keeping a building and its equipment and systems in working order through routine upkeep and repairs.")
new("Factoring (Finance)", "Factoring (finance)", "knowledge",
    "A way of financing a business in which it sells its unpaid invoices to a third party at a discount in return for immediate cash.")
no("Factory Reset", "A device function, not a skill.")
new("Failure Mode Effects Analysis", "Failure mode and effects analysis", "method",
    "A structured method for listing the ways a product or process could fail, rating the effect and likelihood of each, and deciding what to fix first.",
    variants=["FMEA", "Failure Modes and Effects Analysis"])
unsure("Failure Mode Effects SandsCriticality Analysis", "Looks like a garbled spelling of Failure Mode, Effects and Criticality Analysis (FMECA), a distinct extension of FMEA; the typo should not be stored as a variant without a person looking.")
new("Fair Employment And Housing Act (FEMA)", "Fair Employment and Housing Act", "standard",
    "A California law that prohibits discrimination and harassment in employment and housing; its usual abbreviation is FEHA, not FEMA.",
    variants=["FEHA"])
fali = dict(name="Fali", kind="human-language",
    definition="A group of related languages spoken by the Fali people of northern Cameroon.")
new("Fali (Langauge)", fali["name"], fali["kind"], fali["definition"], lang="human")
new("Fali (Language)", fali["name"], fali["kind"], fali["definition"], lang="human")
no("Familial Advanced Sleep-Phase Syndrome", "A medical condition, not a skill.")
new("Family And Consumer Sciences", "Family and consumer sciences", "knowledge",
    "The field that studies how individuals and families manage daily life, including nutrition, child development, household finance and textiles; historically called home economics.",
    variants=["Home economics"])
unsure("Family And Consumer Sciences Certification", "Could mean the AAFCS professional credential or a state teaching certificate in the subject, which have different issuers; a person should decide.")
new("Family Engagement", "Family engagement", "skill",
    "Involving the families of children or clients in their education, care or services through communication and partnership.")
unsure("Family Mental Health", "Names a subject area or condition rather than a clear skill; I cannot tell what a posting asks for.")
new("Family Ministry", "Family ministry", "knowledge",
    "The programmes, teaching and pastoral care a church provides for families.",
    relations=[("related", "qatr9a0kcz")])
fnp = dict(name="Family Nurse Practitioner", kind="credential",
    definition="A nurse practitioner credential for providing primary care to patients of all ages, from infants to older adults.")
new("Family Nurse Practitioner", fnp["name"], fnp["kind"], fnp["definition"], relations=[("related", "d9k6zlxp17")], cert=True, scope="many-issuers")
new("Family Nursing Practitioner", fnp["name"], fnp["kind"], fnp["definition"], relations=[("related", "d9k6zlxp17")], cert=True, scope="many-issuers")
new("Family Systems Theory", "Family systems theory", "knowledge",
    "A framework in psychology and family therapy that treats the family as an emotional system whose members' behaviour is understood through their relationships; Murray Bowen developed it most fully.")
new("Farm Implements", "Farm implements", "tool",
    "Equipment pulled or powered by a tractor to work the land and crops, such as ploughs, harrows, seeders and mowers.")
new("Farm Management", "Farm management", "skill",
    "Planning and running a farm as a business, including crops, livestock, labour, equipment and finances.")
new("FAS 109 (GAAP)", "FAS 109", "standard",
    "A US accounting standard (FASB Statement No. 109) on how to account for income taxes, now part of ASC Topic 740.",
    variants=["SFAS 109"])
new("Fast.ai", "fastai", "library",
    "A Python deep-learning library built on PyTorch, from the fast.ai research group, that gives high-level components for training neural networks.")
unsure("Fast And Secure Protocols", "May refer to the Fast and Secure Protocol (FASP) used by IBM Aspera, but the plural generic wording does not make that certain.")
new("Fast Esp", "FAST ESP", "platform",
    "An enterprise search platform from FAST Search & Transfer, later part of Microsoft, for indexing and searching large collections of content.",
    variants=["FAST Enterprise Search Platform"])
no("Fecal Incontinence", "A medical symptom or condition, not a skill.")
no("Federal Emergency Management Agency (FEMA)", "A government agency, not a skill.")
new("Federal Geographic Data Committee (FGDC) Standards", "FGDC Standards", "standard",
    "Geospatial data standards, such as metadata standards, endorsed by the US Federal Geographic Data Committee.")
unsure("Federal Loan Regulations", "Too vague to say which regulations are meant, for example student loans or small-business loans.")
no("Federal Reserve Systems", "Names a central bank institution, not a skill.")
no("Feld Entertainment", "A company name, not a skill.")
new("Fellow In The Casualty Actuarial Society", "Fellow of the Casualty Actuarial Society", "credential",
    "The highest actuarial designation awarded by the Casualty Actuarial Society to property and casualty actuaries who pass its exams and meet its other requirements.",
    variants=["FCAS", "Fellow in the Casualty Actuarial Society"], cert=True, scope="single-issuer")
new("Fellow of the Society of Actuaries", "Fellow of the Society of Actuaries", "credential",
    "The highest actuarial designation awarded by the Society of Actuaries to candidates who pass its fellowship exams and meet its other requirements.",
    relations=[("related", "yug6rwwpig")], cert=True, scope="single-issuer")
new("Feminist Theory", "Feminist theory", "knowledge",
    "A body of scholarship that examines gender inequality and women's experience, drawing on many academic fields.")
new("Fiber Channel", "Fibre Channel", "knowledge",
    "A high-speed networking technology, standardised by INCITS, used mainly to connect servers to storage area networks.")
unsure("Fiber Construction", "Probably building fibre-optic cable networks, but it could also mean textile fibre work, and I cannot tell which from the name alone.")
unsure("Fiber Light Identifiers", "Probably a fibre-optic test device, but I am not sure of the exact tool class the name refers to.")
new("Field-Programmable Gate Array", "Field-programmable gate array", "knowledge",
    "An integrated circuit whose logic can be configured after manufacture, using a hardware description language, to implement custom digital circuits.",
    variants=["FPGA"])
new("FigJam (Software)", "FigJam", "tool",
    "Figma's online whiteboard for brainstorming, diagramming and planning with a team.")
new("File Control Block", "File control block", "knowledge",
    "A data structure in an operating system or file system that holds the information needed to manage an open file.")
no("File Import", "A generic software function, not a skill.")
no("File Listing", "A generic software function, not a skill.")
new("FileNet", "IBM FileNet", "platform",
    "IBM's enterprise content management and business process platform for storing, managing and routing documents.",
    variants=["FileNet"])
new("Filleting", "Filleting", "skill",
    "Cutting the flesh from the bones of fish or meat to produce boneless fillets.")
new("Film Scoring", "Film scoring", "skill",
    "Composing and arranging original music to accompany a film or video.")
new("Finacle (Software)", "Finacle", "platform",
    "Infosys's suite of core banking and digital banking software for banks.")
unsure("Final Draft", "Could be the Final Draft screenwriting software or the ordinary phrase 'final draft', and a name that matches everyday words needs a person's decision.")
new("Final Expense Insurance", "Final expense insurance", "knowledge",
    "A small whole-life insurance policy meant to pay for funeral, burial and other end-of-life costs.")
no("Final Grades", "A generic education term, not a skill.")
new("Finance Automation", "Finance automation", "skill",
    "Using software, workflows and scripts to carry out finance tasks such as reconciliations, payables and reporting with little manual work.")
new("Finance Softwares", "Finance software", "tool",
    "Software used to manage money and financial records, such as accounting, budgeting, treasury and reporting systems.")
new("Financial Acumen", "Financial acumen", "skill",
    "Understanding how money, financial statements and financial decisions work, and using that understanding to make sound business choices.")
new("Financial Analytics", "Financial analytics", "skill",
    "Analysing financial data, such as revenue, costs and risk, with statistical and data tools to support decisions.")
variant("Financial Consolidations", "pts4mjn76g", "The plural of Financial consolidation, the same concept.")
no("Financial Crimes Enforcement Networks", "Names a government agency (FinCEN), not a skill.")
no("Financial Data Vendor", "A generic kind of company, not a skill.")
new("Financial Forecast", "Financial forecasting", "skill",
    "Estimating future revenue, costs and cash flow from past results and assumptions.",
    reason="The tag names the output of the skill of financial forecasting.")
no("Financial Future", "A generic phrase, not a skill.")
new("Financial Information EXchange", "Financial Information eXchange", "standard",
    "A messaging standard used to exchange securities trades and market data electronically between financial firms.",
    variants=["FIX Protocol"])
new("Financial Privacy", "Financial privacy", "knowledge",
    "Protecting people's personal financial information and following the rules on how it may be collected, shared and used.")
new("Financial Risk Management", "Financial risk management", "skill",
    "Identifying, measuring and controlling financial risks such as market, credit and liquidity risk.")
new("FINCAD (Software)", "FINCAD", "tool",
    "Financial analytics software for valuing and managing derivatives and other complex financial instruments.")
new("FinCEN 314 Program", "FinCEN 314 program", "standard",
    "The information-sharing rules under Section 314 of the USA PATRIOT Act, run by FinCEN, that let law enforcement and financial institutions share information about suspected money laundering and terrorist financing.")
no("Finch", "An ordinary word for a bird, or a name, not a skill.")
unsure("Fingerprinting", "Could mean forensic or background-check fingerprinting, browser or device fingerprinting, or DNA fingerprinting, and the tag gives no way to choose.")
no("Fire Door", "A physical building item, not a skill.")
new("Firebase Cloud Messaging (FCM)", "Firebase Cloud Messaging", "platform",
    "Google's cloud service for sending push notifications and messages to Android, iOS and web apps.")
unsure("Fireware Update", "Fireware is WatchGuard's firewall operating system, but this could also be a misspelling of firmware update.")
new("First Article Inspections", "First article inspection", "method",
    "A documented check that the first part made from a new design or process meets all drawing and specification requirements.")
unsure("FirstStrike (Financial Software)", "Looks like a financial software product, but I do not know it well enough to define it.")
new("FIS GetPaid (Accounts Receivable Software)", "FIS GetPaid", "tool",
    "FIS's software for managing accounts receivable, credit and collections.")
unsure("Fixative (Perfumery)", "Names an ingredient class in perfumery, not clearly a skill; a person should decide what it stands for.")
no("Fixer", "A job title or generic word, not a skill.")
new("Flagger Certification", "Flagger certification", "credential",
    "A certificate showing that a person has been trained to direct traffic safely through road work zones as a flagger.",
    variants=["Flagger certificate"], cert=True, scope="many-issuers")
no("Flashlight", "An ordinary object, not a skill.")
new("Flask (Web Framework)", "Flask", "framework",
    "A lightweight Python web framework for building web applications and APIs.")
new("Flat Sketching", "Flat sketching", "skill",
    "Drawing flat, two-dimensional technical drawings of garments that show seams, stitching and proportions for design and production.")
new("Flatbed Truck", "Flatbed truck", "tool",
    "A truck with an open, flat cargo bed and no sides or roof, used to haul large or irregular loads.")
new("Flavor Development", "Flavor development", "skill",
    "Creating and refining flavours for food and drink products.")
new("Flexible Single Master Operation", "Flexible Single Master Operations", "knowledge",
    "The specialised domain controller roles in Microsoft Active Directory that only one server at a time may hold, such as schema master and PDC emulator.",
    variants=["FSMO"])
no("Flexible Working", "A work arrangement or benefit, not a skill.")
new("Flight Attendant Certification", "Flight attendant certification", "credential",
    "A credential showing that a person has completed the safety training and met the regulatory requirements to work as cabin crew on commercial flights.",
    cert=True, scope="many-issuers")
no("Flight Dispatcher", "A job title, not a skill.")

# remove the placeholder that new() overwrote
assert ans["Farm Implements"]["decision"] == "new"

missing = [t for t in reqs if t not in ans]
extra = [t for t in ans if t not in reqs]
assert not missing and not extra, (missing, extra)
os.makedirs("work/responses", exist_ok=True)
from collections import Counter
c = Counter()
for t, (fn, r) in reqs.items():
    json.dump(ans[t], open(os.path.join("work/responses", fn), "w"), indent=1, ensure_ascii=False)
    c[ans[t]["decision"]] += 1
print(len(reqs), dict(c))
