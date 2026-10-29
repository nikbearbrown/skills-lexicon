import json, glob, os

GK = "general-knowledge"
reqs = {}
for f in sorted(glob.glob("work/requests/*.json")):
    reqs[json.load(open(f))["term"]] = os.path.basename(f)

out = {}
BAD = []

def put(term, resp):
    if term not in reqs:
        BAD.append(term); return
    assert term not in out, term
    out[term] = resp

def new(term, name, kind, definition, variants=(), relations=(), cert=False, scope=None, lang=None, reason="", note=""):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert and scope:
        e["certification_scope"] = {"value": scope, "basis": GK}
    put(term, {"decision": "new", "variant_of": None, "reason": reason or "A named concept I know from general knowledge.", "entry": e})

def cred(term, name, definition, variants=(), relations=(), scope="single-issuer", reason=""):
    new(term, name, "credential", definition, variants, relations, cert=True, scope=scope,
        reason=reason or "A named credential I know from general knowledge.")

def no(term, reason):
    put(term, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})

def unsure(term, reason):
    put(term, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})

# ---- Certified ... credentials
cred("Certified Medical Billing And Coding Specialist", "Certified Medical Billing and Coding Specialist",
     "A certification for people who prepare healthcare claims and assign diagnosis and procedure codes.", scope=None,
     reason="Several bodies and schools use this title, so the issuer is not given.")
cred("Certified Medical Laboratory Assistant", "Certified Medical Laboratory Assistant",
     "A certification for assistants who collect, prepare and process specimens in a medical laboratory.", scope=None,
     reason="Several bodies use this title, so the issuer is not given.")
cred("Certified Medical-Surgical Registered Nurse", "Certified Medical-Surgical Registered Nurse",
     "A certification for registered nurses who work in medical-surgical nursing, awarded by the Medical-Surgical Nursing Certification Board.",
     variants=["CMSRN"])
cred("Certified Music Therapist", "Certified Music Therapist",
     "A credential showing that a music therapist has met professional certification requirements.", scope=None,
     reason="A music-therapy credential; the issuing body depends on the country, so no scope is given.")
cred("Certified Nephrology Nurse", "Certified Nephrology Nurse",
     "A certification for registered nurses who care for people with kidney disease, awarded by the Nephrology Nursing Certification Commission.")
cred("Certified Network Defense Architecture", "Certified Network Defense Architect",
     "An EC-Council certification for professionals who design and defend secure computer networks.",
     reason="I take this to be the EC-Council CNDA credential; the term as seen says 'Architecture' rather than 'Architect'.")
cred("Certified Neuroscience Registered Nurse", "Certified Neuroscience Registered Nurse",
     "A certification for registered nurses who care for patients with neurological conditions, awarded by the American Board of Neuroscience Nursing.",
     variants=["CNRN"])
cred("Certified Novell Salesperson", "Certified Novell Salesperson",
     "A Novell certification for sales staff who sell Novell products and solutions.")
cred("Certified Nurse Manager And Leader", "Certified Nurse Manager and Leader",
     "A certification for nurses in management and leadership roles, awarded by the AONL Credentialing Center.",
     variants=["CNML"])
cred("Certified Nursing Assistant", "Certified Nursing Assistant",
     "A state-recognised certification for nursing assistants who give basic bedside care under the direction of nurses.",
     variants=["Certified Nurse Assistant", "CNA"], scope="many-issuers",
     reason="A credential each US state certifies under common federal training rules.")
cred("Certified Occupancy Specialist (COS)", "Certified Occupancy Specialist",
     "A housing-industry credential for staff who determine eligibility and manage occupancy in subsidised housing programmes.", scope=None,
     reason="A housing-industry credential; I am not sure of the issuing body, so no scope is given.")
cred("Certified Occupational Health Nurse", "Certified Occupational Health Nurse",
     "A certification for registered nurses who specialise in occupational and workplace health, awarded by the American Board for Occupational Health Nurses.",
     variants=["COHN"])
cred("Certified Ostomy Care Nurse", "Certified Ostomy Care Nurse",
     "A certification for registered nurses who specialise in the care of people with ostomies, awarded by the Wound, Ostomy and Continence Nursing Certification Board.",
     variants=["COCN"])
cred("Certified Outpatient Coder", "Certified Outpatient Coder",
     "An AAPC certification for coders who assign diagnosis and procedure codes to outpatient hospital and facility claims.",
     relations=[("related", "cyv86lx0k4")])

unsure("Certified Packer", "Could be a job title or a trade-specific certificate; I know of no recognised credential by this name.")
unsure("Certified Patient Care", "Looks like a truncated 'Certified Patient Care Technician'; on its own I cannot say which credential it means.")

ptc_def = "A certification for technicians who give hands-on patient care in hospitals and similar settings."
ptc_var = ["Certified Patient Care Technician/Assistant", "CPCT/A"]
cred("Certified Patient Care Technician", "Certified Patient Care Technician", ptc_def, variants=ptc_var, scope=None,
     reason="Several bodies use this title, so the issuer is not given.")
cred("Certified Patient Care Technician/Associate/Nurse Technician", "Certified Patient Care Technician", ptc_def, variants=ptc_var, scope=None,
     reason="Same credential as 'Certified Patient Care Technician' under alternative job titles.")

phon_def = "A certification for registered nurses who care for children with cancer and blood disorders, awarded by the Oncology Nursing Certification Corporation."
cred("Certified Pediatric Hematology Oncology Nurse", "Certified Pediatric Hematology Oncology Nurse", phon_def,
     variants=["CPHON", "Certified Pediatric Oncology Nurse", "CPON"])
cred("Certified Pediatric Oncology Nurse", "Certified Pediatric Hematology Oncology Nurse", phon_def,
     variants=["CPHON", "Certified Pediatric Oncology Nurse", "CPON"],
     reason="I believe this is the earlier name of the Certified Pediatric Hematology Oncology Nurse credential.")
cred("Certified Pediatric Nurse", "Certified Pediatric Nurse",
     "A certification for registered nurses who care for children, awarded by the Pediatric Nursing Certification Board.")
cred("Certified Physician Practice Manager", "Certified Physician Practice Manager",
     "An AAPC certification for managers of physician and medical group practices.", variants=["CPPM"])
cred("Certified Plastic Surgical Nurse", "Certified Plastic Surgical Nurse",
     "A certification for registered nurses in plastic and reconstructive surgery, awarded by the Plastic Surgical Nursing Certification Board.",
     variants=["CPSN"])
cred("Certified Pool & Spa Operator", "Certified Pool & Spa Operator",
     "A certification from the Pool & Hot Tub Alliance for people who operate and maintain swimming pools and spas.",
     variants=["Certified Pool and Spa Operator"])
no("Certified Practitioner", "A generic title that fits many unrelated credentials, so it names no single one.")
cred("Certified Professional Biller (CPB)", "Certified Professional Biller",
     "An AAPC certification for medical billers who prepare, submit and follow up healthcare claims.",
     relations=[("related", "cyv86lx0k4")])
cred("Certified Professional Compliance Officer", "Certified Professional Compliance Officer",
     "An AAPC certification for people who oversee compliance programmes in healthcare organisations.",
     variants=["CPCO"], relations=[("related", "cyv86lx0k4")])
cred("Certified Professional In Healthcare Information And Management Systems",
     "Certified Professional in Healthcare Information and Management Systems",
     "A HIMSS certification for professionals in healthcare information and management systems.",
     variants=["CPHIMS"])
cred("Certified Professional In Healthcare Quality", "Certified Professional in Healthcare Quality",
     "A certification for professionals who work on quality improvement and patient safety in healthcare.", variants=["CPHQ"])
cred("Certified Professional In Healthcare Risk Management", "Certified Professional in Healthcare Risk Management",
     "A certification for professionals who manage risk and patient safety in healthcare, awarded by the American Hospital Association Certification Center.",
     variants=["CPHRM"])
cred("Certified Professional Manager", "Certified Professional Manager",
     "A management certification awarded by the Institute of Certified Professional Managers.")
cred("Certified Professional Medical Services Manager", "Certified Professional Medical Services Management",
     "A certification for professionals who manage medical staff services such as provider credentialing and privileging.",
     variants=["CPMSM"], reason="I believe this is the NAMSS credential Certified Professional Medical Services Management.")
cred("Certified Professional Of Occupancy", "Certified Professional of Occupancy",
     "A housing-industry credential for staff who handle eligibility and occupancy in affordable and subsidised housing.")
cred("Certified Projects Director", "Certified Projects Director",
     "The top level (Level A) of the IPMA four-level project management certification, for directors of large portfolios and programmes.",
     variants=["IPMA Level A"], scope=None,
     reason="I take this to be IPMA Level A; IPMA awards through national member associations, so no scope is given.")
cred("Certified Property Manager", "Certified Property Manager",
     "A real-estate management certification awarded by the Institute of Real Estate Management.")
cred("Certified Public Housing Manager (PHM)", "Certified Public Housing Manager",
     "A certification for managers of public housing properties and programmes.",
     relations=[("related", "w3gh6mctib")])
cred("Certified Radiology Nurse", "Certified Radiology Nurse",
     "A certification for registered nurses who work in radiology and imaging.", scope=None,
     reason="A radiology-nursing board credential; I am not sure of the exact board, so no scope is given.")
cred("Certified Registered Nurse First Assistant", "Certified Registered Nurse First Assistant",
     "A certification for registered nurses who work as first assistants in surgery, awarded by the Competency & Credentialing Institute.",
     variants=["CRNFA"])
cred("Certified Registered Nurse Infusion", "Certified Registered Nurse Infusion",
     "A certification for registered nurses who specialise in infusion therapy, awarded by the Infusion Nurses Certification Corporation.",
     variants=["CRNI"])
cred("Certified Rehabilitation Registered Nurse", "Certified Rehabilitation Registered Nurse",
     "A certification for registered nurses who specialise in rehabilitation nursing, awarded by the Rehabilitation Nursing Certification Board.",
     variants=["CRRN"])
cred("Certified Residential Specialist", "Certified Residential Specialist",
     "A real-estate certification for agents with advanced experience in residential sales, awarded by the Residential Real Estate Council.")
unsure("Certified Retirement Administrator", "Retirement-plan administration credentials exist but I cannot confirm who awards one with this exact name.")
cred("Certified Rhythm Analysis Technician", "Certified Rhythm Analysis Technician",
     "A certification for technicians who monitor and interpret heart rhythms from ECG telemetry.", scope=None,
     reason="I am not certain of the issuing body, so no scope is given.")
cred("Certified Risk Adjustment Coder", "Certified Risk Adjustment Coder",
     "An AAPC certification for coders who assign diagnosis codes used in risk adjustment payment models.",
     relations=[("related", "cyv86lx0k4")])
cred("Certified Senior Project Manager", "Certified Senior Project Manager",
     "Level B of the IPMA four-level project management certification, for managers of complex projects.",
     variants=["IPMA Level B"], scope=None,
     reason="I take this to be IPMA Level B; IPMA awards through national member associations, so no scope is given.")
unsure("Certified Society Of Pain Educators", "The name looks mangled (perhaps a pain-educator credential from a society); I cannot tell what it names.")
cred("Certified Software Test Engineer", "Certified Software Test Engineer",
     "A software testing certification offered by the Quality Assurance Institute (QAI).",
     variants=["CSTE"], relations=[("related", "ss273uzint")])
cred("Certified Specialist in Gerontological Nutrition", "Board Certified Specialist in Gerontological Nutrition",
     "A specialist certification for registered dietitians who work with older adults, awarded by the Commission on Dietetic Registration.")
cred("Certified Specialist in Sports Dietetics", "Board Certified Specialist in Sports Dietetics",
     "A specialist certification for registered dietitians who work with athletes, awarded by the Commission on Dietetic Registration.",
     variants=["CSSD"])
cred("Certified Specialist Of Wine", "Certified Specialist of Wine",
     "A wine knowledge certification awarded by the Society of Wine Educators.")
cred("Certified Supplier Quality Professional (CSQP)", "Certified Supplier Quality Professional",
     "An ASQ certification for professionals who assess and manage the quality of suppliers.", variants=["CSQP"])
cred("Certified Surgical Technologist", "Certified Surgical Technologist",
     "A certification for surgical technologists, awarded by the National Board of Surgical Technology and Surgical Assisting.")
cred("Certified Technical Trainer", "Certified Technical Trainer",
     "A certification showing that a trainer can plan and deliver technical training effectively.", scope=None,
     reason="I believe this is CompTIA's CTT+ but other bodies use the title, so no scope is given.")
cred("Certified Technology Specialist", "Certified Technology Specialist",
     "An AVIXA certification for audiovisual professionals.")
cred("Certified Teststand Developer", "Certified TestStand Developer",
     "A National Instruments certification for developers of automated test sequences with NI TestStand.", variants=["CTD"])
cred("Certified Transport Registered Nurse", "Certified Transport Registered Nurse",
     "A certification for registered nurses who care for patients during air and ground transport, awarded by the Board of Certification for Emergency Nursing.",
     variants=["CTRN"])
unsure("Certified Unix System Administration", "Several vendor Unix administrator certifications exist and the term may also mean the skill; I cannot tell which.")
cred("Certified Urologic Physician'S Assistant", "Certified Urologic Physician Assistant",
     "A certification for physician assistants in urology, awarded by the Certification Board for Urologic Nurses and Associates.",
     variants=["CUPA"])
cred("Certified Urologic Registered Nurse", "Certified Urologic Registered Nurse",
     "A certification for registered nurses in urology, awarded by the Certification Board for Urologic Nurses and Associates.",
     variants=["CURN"])
cred("Certified Wine Educator", "Certified Wine Educator",
     "An advanced wine teaching certification awarded by the Society of Wine Educators.", variants=["CWE"])
cred("Certified Wound And Ostomy Care Nurse", "Certified Wound and Ostomy Care Nurse",
     "A nursing certification for nurses who care for people with wounds and ostomies.", scope=None,
     reason="Matches a wound-and-ostomy nursing board credential, but I am not sure of its exact official title.")
cred("Certified Wound Care Nurse", "Certified Wound Care Nurse",
     "A certification for registered nurses who specialise in wound care, awarded by the Wound, Ostomy and Continence Nursing Certification Board.",
     variants=["CWCN"])

# ---- C-h terms
new("Cfwheels", "CFWheels", "framework",
    "An open-source model-view-controller web framework for CFML (ColdFusion Markup Language).",
    variants=["ColdFusion on Wheels"])
new("Chai (Software)", "Chai.js", "library",
    "An assertion library for JavaScript testing that offers should, expect and assert styles.", variants=["ChaiJS"])
new("Chain Conveyor", "Chain Conveyor", "tool",
    "A conveyor that moves loads along a track using one or more driven chains.")
unsure("Chain Linking", "Means different things (a statistical index method, garment or jewellery work) and nothing here shows which.")
new("Chain of Custody", "Chain of custody", "method",
    "The documented, unbroken record of who held a piece of evidence or sample and when, used to show it was not altered.")
unsure("Chain Reactions", "Could mean nuclear, chemical or general cascading reactions, and nothing here shows which.")
new("Chainer", "Chainer", "framework",
    "An open-source Python deep learning framework from Preferred Networks that builds neural networks as the code runs.")
new("Chakma (Language)", "Chakma", "human-language",
    "An Indo-Aryan language spoken by the Chakma people in Bangladesh and India.", lang="human")
new("Challenge-Handshake Authentication Protocol", "Challenge-Handshake Authentication Protocol", "standard",
    "A challenge-response protocol, used with the Point-to-Point Protocol, that checks a peer's identity by hashing a shared secret with a random challenge.")
new("Chamorro (Language)", "Chamorro", "human-language",
    "An Austronesian language spoken by the Chamorro people of Guam and the Northern Mariana Islands.",
    variants=["CHamoru"], lang="human")
new("Change Agility", "Change agility", "skill",
    "The capacity to adapt quickly and effectively as circumstances and organisational priorities change.")
cred("Change Management Certified Professional", "Change Management Certified Professional",
     "A certification in the principles and practice of organisational change management.", scope=None,
     reason="Several bodies offer change-management certifications and I am not sure of the issuer, so no scope is given.")
new("Change Management Planning", "Change management planning", "skill",
    "Planning how an organisation will move people through a change, including stakeholder engagement, communication and training.")
no("Change Request", "A work item or document in a change process, not a skill.")
new("Changing Oil", "Changing oil", "skill",
    "Draining the used engine oil from a vehicle or machine and refilling it with fresh oil, usually with a new filter.")
new("Channel Sales", "Channel sales", "skill",
    "Selling products or services through partners such as resellers and distributors rather than directly to end customers.")
new("Character Art", "Character art", "skill",
    "Designing and producing the visual appearance of characters for games, animation and film.")
new("Chart.js", "Chart.js", "library",
    "An open-source JavaScript library for drawing charts on an HTML canvas.", variants=["ChartJS"],
    relations=[("related", "ya8of3fs21")])
cred("Chartered Fellow of the Chartered Institute of Personnel and Development (FCIPD)",
     "Chartered Fellow of the Chartered Institute of Personnel and Development",
     "The highest membership grade of the Chartered Institute of Personnel and Development, held by senior HR and people-development professionals.",
     variants=["FCIPD"])
no("Chartered Institute for the Management of Sport and Physical Activity (CIMSPA)",
   "The name of a professional body, not a skill or a credential.")
unsure("Chartered Institute of Management Accountants (CIMA)",
       "Names a professional body; postings usually mean its qualification, so whether to record it as a credential needs a person's call.")
cred("Chartered Member of the Chartered Institute of Personnel and Development (MCIPD)",
     "Chartered Member of the Chartered Institute of Personnel and Development",
     "A membership grade of the Chartered Institute of Personnel and Development for experienced HR and people-development professionals.",
     variants=["MCIPD"])
cred("Chauffeur License", "Chauffeur license",
     "A driver's licence, issued by a state or country, that permits the holder to drive vehicles for hire.",
     variants=["Chauffeur's License"], scope="many-issuers",
     reason="Each US state issues its own chauffeur licence under its own rules.")
new("Chemical Reactions", "Chemical reactions", "knowledge",
    "The processes by which substances change into other substances, and the types, rates and energy changes involved.")
no("Chemistry And Camera Complex", "The name of the ChemCam instrument on the Curiosity rover, not a general skill.")
new("Child And Adolescent Psychiatry", "Child and adolescent psychiatry", "knowledge",
    "The medical specialty that diagnoses and treats mental, emotional and behavioural disorders in children and teenagers.")
new("Child Nutritions", "Child nutrition", "knowledge",
    "The nutritional needs of infants, children and adolescents and how diet meets them.")
no("Childhood Cancer", "A disease, not a skill.")
new("Children'S Health Insurance Program", "Children's Health Insurance Program", "knowledge",
    "The US federal and state programme that provides low-cost health coverage for children in families that earn too much for Medicaid.",
    reason="Knowledge of a named government programme; the tag may also be a benefit, so a person should check.")
new("Children's Ministry", "Children's ministry", "knowledge",
    "The programmes, teaching and pastoral care a church provides for its children.")
new("Chinese Language", "Chinese", "human-language",
    "A group of related Sinitic languages, including Mandarin and Cantonese, spoken mainly in China and written in Chinese characters.",
    lang="human")
new("Chip Design", "Chip design", "skill",
    "Specifying, laying out and verifying the circuits of an integrated circuit.", variants=["Integrated circuit design"])
new("Chipmunk Basic", "Chipmunk Basic", "programming-language",
    "A free BASIC interpreter for several platforms, based on classic Microsoft-style BASIC.", lang="programming")
new("Chipmunk (Computer Physics Engines)", "Chipmunk2D", "library",
    "An open-source 2D rigid-body physics library written in C.")
new("Chlorofluorocarbons", "Chlorofluorocarbons", "knowledge",
    "A class of compounds of carbon, chlorine and fluorine once common as refrigerants and propellants, now phased out because they damage the ozone layer.",
    variants=["Chlorofluorocarbon", "CFCs"])
new("Choral Music", "Choral music", "knowledge",
    "Vocal music written for and performed by a choir.")
unsure("Chango (Language)", "I cannot identify a language called Chango with confidence.")
new("Chordiant (Software)", "Chordiant", "platform",
    "A customer-experience management software suite from Chordiant Software, which Pegasystems acquired in 2010.")

# ---- write
print("BAD", BAD)
missing = [t for t in reqs if t not in out]
assert not missing, missing
os.makedirs("work/responses", exist_ok=True)
for t, r in out.items():
    json.dump(r, open("work/responses/" + reqs[t], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open("work/responses/" + reqs[t], "a").write("\n")
from collections import Counter
print(len(out), Counter(r["decision"] for r in out.values()))
