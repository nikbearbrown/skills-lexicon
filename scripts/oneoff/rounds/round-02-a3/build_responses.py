"""Scratch: builds work/responses/*.json from my answers, keyed by the request's position in the sorted listing."""
import json, glob, os
GK = "general-knowledge"
reqs = sorted(glob.glob("work/requests/*.json"))
A = {}   # n -> (expected term fragment, answer dict)

def b(v):
    return {"value": v, "basis": GK}

def new(n, frag, name, kind, definition, variants=(), relations=(), verbs=(), cert=False, scope=None, lang=None, reason=None):
    e = {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
         "variants": [{"label": v, "basis": GK} for v in variants],
         "relations": [{"type": t, "target": x, "basis": GK} for t, x in relations],
         "verbs": [{"verb": v, "basis": GK} for v in verbs],
         "certification": b(cert)}
    if cert and scope:
        e["certification_scope"] = b(scope)
    e["language_type"] = b(lang)
    e["annotation_note"] = ""
    A[n] = (frag, {"decision": "new", "variant_of": None, "reason": reason or f"{name} is a recognised {kind}; no entry in nearest is the same concept.", "entry": e})

def no(n, frag, reason):
    A[n] = (frag, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None})

def uns(n, frag, reason):
    A[n] = (frag, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None})

def cred(n, frag, name, definition, variants=(), relations=(), scope="single-issuer"):
    new(n, frag, name, "credential", definition, variants, relations, cert=True, scope=scope)

# ---- non-credentials -------------------------------------------------------
new(1, "Cartodb", "CARTO", "platform",
    "A cloud platform for analysing and mapping location data, formerly called CartoDB.")
new(2, "Cartographic Design", "Cartographic design", "skill",
    "Designing maps so that geographic data is clear and readable, through choices of symbols, colour, labelling and scale.")
no(3, "Cartoonist", "A job title for an artist, not a skill.")
new(4, "Case Analysis", "Case analysis", "skill",
    "Examining the facts and issues of a particular case, such as a legal, business or clinical case, to reach reasoned conclusions or recommendations.")
uns(5, "Case Class", "Probably Scala's case class language feature, but no Scala entry was shown and it is unclear whether a single language feature is a skill entry.")
new(6, "Case Method", "Case method", "method",
    "A teaching approach in which students learn by studying and discussing real or realistic cases, common in business and law schools.")
no(7, "Case Sensitive", "An adjective describing text matching, not a skill.")
new(8, "Casperjs", "CasperJS", "tool",
    "An open-source tool, written in JavaScript, for scripting navigation and tests of web pages in headless browsers such as PhantomJS and SlimerJS.")
new(9, "Cassandra", "Apache Cassandra", "tool",
    "An open-source distributed NoSQL database that stores data in wide columns and is built to stay available across many servers.",
    verbs=["query", "administer"])
new(10, "Castilian Spanish", "Castilian Spanish", "human-language",
    "The standard variety of the Spanish language as spoken in Spain, especially in its central and northern regions.", lang="human")
new(11, "Casualty Movement", "Casualty movement", "skill",
    "Moving injured or ill people from where they were hurt to places where they can be treated, including loading and transporting them.")
new(12, "Catalan", "Catalan", "human-language",
    "A Romance language spoken mainly in Catalonia, the Balearic Islands, Valencia and Andorra, where it is the official language.",
    variants=["Català"], lang="human")
new(13, "CatBoost", "CatBoost", "library",
    "An open-source gradient-boosting library, originally from Yandex, that trains decision-tree models and handles categorical features directly.",
    relations=[("related", "ydp6a13kjq"), ("broader", "flxbx98seh")], verbs=["train"])
no(14, "Cause Of Action", "A legal term for the facts that give a right to sue, not a skill, tool or field.")
no(15, "Cd Rom", "A storage medium, not a skill or a product one operates.")
new(16, "Cebas FinalRender", "cebas finalRender", "tool",
    "A rendering plug-in from cebas Visual Technology for producing photorealistic images in 3D software such as Autodesk 3ds Max and Maya.")
no(17, "Cefprozil", "The name of an antibiotic medicine, not a skill, like a condition or symptom.")
new(18, "Celoxis", "Celoxis", "tool",
    "Web-based project and portfolio management software for planning work, tracking time and resources, and reporting on projects.")
uns(19, "Census Building", "The phrase is unclear; it could mean building a population count, a building survey or something else.")
no(20, "Census", "A generic word for counting a population (or a patient count), not a skill.")
uns(21, "Centering", "Could be centering clay in pottery, the Centering group prenatal care model or something else; the tag does not say which.")
new(22, "CentiLeo Renderer", "CentiLeo", "tool",
    "A GPU-based 3D renderer that produces images from 3D scenes, offered as a plug-in for 3D modelling software.")
no(23, "Ceramic Tile", "A building material, not a skill; the skill would be tile setting.")
new(24, "Cerner", "Cerner", "platform",
    "Electronic health record software from the company Cerner, now part of Oracle Health, that hospitals use to chart, order and review patient information.")
new(25, "Ceros", "Ceros", "platform",
    "A cloud platform for designing interactive online content such as ebooks, microsites and lookbooks without writing code.")

# ---- credentials -----------------------------------------------------------
cred(26, "Certificate Of Advanced Graduate Study", "Certificate of Advanced Graduate Study",
     "A post-master's credential awarded by universities for a defined programme of advanced graduate study beyond the master's degree.",
     variants=["CAGS", "Certificate of Advanced Graduate Studies"], scope="many-issuers")
cred(27, "Certificate Of Clinical Competence In Speech", "Certificate of Clinical Competence in Speech-Language Pathology",
     "The professional certificate from the American Speech-Language-Hearing Association showing a speech-language pathologist has met its academic, clinical-practicum and examination requirements.",
     variants=["CCC-SLP"])
uns(28, "Certification Healthcare Leadership", "Does not name a specific credential I can identify; it may be a garbled name for one of several healthcare leadership certifications.")
cred(29, "Certification in Neurophysiologic Intraoperative", "Certification in Neurophysiologic Intraoperative Monitoring",
     "A certification for professionals who monitor the nervous system with electrical tests during surgery to help protect it from injury.",
     variants=["CNIM"], relations=[("related", "rfizzr2lin")])
cred(30, "Certification In Transportation And Logistics", "Certification in Transportation and Logistics",
     "A professional certification in transportation and logistics management.")
uns(31, "Certification Of Disability Management", "Several credentials fit this wording (for example CDMS and CDMP) and the tag does not say which.")
uns(32, "Certification Of Italian As A Foreign", "Several bodies, such as the universities of Siena, Perugia and Roma Tre, award certificates with this kind of name, and I cannot tell which is meant.")
cred(33, "Certified Addictions Registered Nurse", "Certified Addictions Registered Nurse",
     "A certification for registered nurses who specialise in caring for people with addictions, awarded by the Addictions Nursing Certification Board.",
     variants=["CARN"])
cred(34, "Certified Alcoholism And Drug Abuse", "Certified Alcoholism and Drug Abuse Counselor",
     "A credential for counselors who treat people with alcohol and drug problems.", scope=None)
cred(35, "Certified Ambulatory Perianesthesia", "Certified Ambulatory Perianesthesia Nurse",
     "A certification from the American Board of Perianesthesia Nursing Certification for nurses who care for ambulatory patients before and after anesthesia.")
cred(36, "Certified Analytics Professional", "Certified Analytics Professional",
     "A certification from INFORMS for analytics practitioners who have shown skill across the whole analytics process, from framing the problem to deploying the solution.")
cred(37, "Certified Apartment Manager", "Certified Apartment Manager",
     "A certification from the National Apartment Association for managers of apartment communities.")
cred(38, "Certified Associate in Python", "Certified Associate in Python Programming",
     "An associate-level certification from the Python Institute showing that someone can write and understand programs in Python.")
cred(39, "Certified Associate Project Management", "Certified Associate in Project Management",
     "An entry-level project management certification from the Project Management Institute for people who are new to the field.",
     relations=[("related", "z83cabeb9c")])
cred(40, "Certified Asthma Educator", "Certified Asthma Educator",
     "A certification showing that a health professional can teach people with asthma and their families how to manage the condition.",
     variants=["AE-C"], relations=[("related", "mhz7f3lsy1")])
cred(41, "Certified Bariatric Nurse", "Certified Bariatric Nurse",
     "A certification for nurses who care for patients with severe obesity, including before and after weight-loss surgery.")
cred(42, "Certified Bath Designer", "Certified Bath Designer",
     "A certification from the National Kitchen & Bath Association for designers who plan bathrooms.")
cred(43, "Certified Biomedical Equipment Technician", "Certified Biomedical Equipment Technician",
     "A certification for technicians who install, maintain and repair medical equipment such as patient monitors and infusion pumps.",
     variants=["CBET"])
cred(44, "Certified Breast Care Nurse", "Certified Breast Care Nurse",
     "A certification from the Oncology Nursing Certification Corporation for nurses who care for patients with breast cancer and other breast conditions.",
     variants=["CBCN"])
cred(45, "Certified Cardiographic Technician", "Certified Cardiographic Technician",
     "A certification from Cardiovascular Credentialing International for technicians who record and check electrocardiograms and related heart tests.")
cred(46, "Certified Case Manager", "Certified Case Manager",
     "A certification from the Commission for Case Manager Certification for case managers who coordinate health and social care for clients.")
cred(47, "Certified Child Life Specialist", "Certified Child Life Specialist",
     "A certification from the Association of Child Life Professionals for specialists who help children and families cope with illness, injury and hospital care.",
     variants=["CCLS"])
cred(48, "Certified Clinical Hemodialysis Technician", "Certified Clinical Hemodialysis Technician",
     "A certification from the Nephrology Nursing Certification Commission for technicians who give hemodialysis treatments in clinical settings.",
     variants=["CCHT"])
cred(49, "Certified Clinical Medical Assistant", "Certified Clinical Medical Assistant",
     "A certification from the National Healthcareer Association for medical assistants who do clinical tasks such as taking vital signs and drawing blood.",
     variants=["CCMA"])
cred(50, "Certified Clinical Research Associate", "Certified Clinical Research Associate",
     "A certification from the Association of Clinical Research Professionals for people who monitor clinical trials at study sites.",
     variants=["CCRA"])
cred(51, "Certified Clinical Transplant Coordinators", "Certified Clinical Transplant Coordinator",
     "A certification for coordinators who manage the clinical care of organ-transplant patients before and after their transplants.",
     variants=["CCTC"])
cred(52, "Certified Coding Associate", "Certified Coding Associate",
     "An entry-level medical coding certification from the American Health Information Management Association.")
cred(53, "Certified Coding Specialist", "Certified Coding Specialist",
     "A medical coding certification from the American Health Information Management Association for coders who assign codes to hospital records.")
cred(54, "Certified Continence Care Nurse", "Certified Continence Care Nurse",
     "A certification from the Wound, Ostomy and Continence Nursing Certification Board for nurses who care for people with bladder and bowel incontinence.",
     variants=["CCCN"])
cred(55, "Certified Control Systems Technician", "Certified Control Systems Technician",
     "A certification from the International Society of Automation, offered at three levels, for technicians who calibrate, install and troubleshoot control systems and instruments.",
     variants=["CCST"])
cred(56, "Certified Corrections Nurse", "Certified Correctional Nurse",
     "A certification for nurses who work in correctional facilities such as jails and prisons.")
uns(57, "Certified Corrections Nurse Management", "The wording looks like a garbled Certified Correctional Nurse Manager, but I cannot be sure which credential is meant.")
cred(58, "Certified Culinary Administration", "Certified Culinary Administrator",
     "An American Culinary Federation certification for chefs who hold administrative roles in running foodservice operations.",
     relations=[("broader", "gakz93rpch")])
cred(59, "Certified Diabetes Educator", "Certified Diabetes Care and Education Specialist",
     "A certification for health professionals who teach people to manage diabetes; it replaced the title Certified Diabetes Educator in 2020.",
     variants=["CDCES"])
cred(60, "Certified Dialysis Nurse", "Certified Dialysis Nurse",
     "A certification from the Nephrology Nursing Certification Commission for nurses who care for dialysis patients.")
uns(61, "Certified Distance Learning Administrator", "I cannot confirm this credential exists under this name or which body would issue it.")
cred(62, "Certified Diversity Recruiter", "Certified Diversity Recruiter",
     "A certification for recruiters who find and hire candidates from diverse backgrounds.")
cdip_def = "A certification from the American Health Information Management Association for people who review clinical documentation so that it accurately and completely reflects a patient's care and condition."
cdip_var = ["Certified Documentation Improvement Practitioner", "CDIP"]
cred(63, "Certified Documentation Improvement Practitioner", "Certified Documentation Integrity Practitioner", cdip_def, variants=cdip_var)
cred(64, "Certified Documentation Integrity Practitioner", "Certified Documentation Integrity Practitioner", cdip_def, variants=cdip_var)
uns(65, "Certified E-Marketer", "I cannot identify a credential by this name or its issuing body.")
cred(66, "Certified Energy Manager", "Certified Energy Manager",
     "A certification from the Association of Energy Engineers for professionals who manage energy use and efficiency in buildings and facilities.")
uns(67, "Certified Environmental Drycleaner", "I cannot identify a credential by this name or its issuing body.")
uns(68, "Certified First Assistant", "Several surgical-assisting credentials have similar names, and I cannot tell which is meant.")
cred(69, "Certified First Responder", "Certified First Responder",
     "A credential for people trained to give emergency care at the scene before an ambulance crew arrives.",
     scope="many-issuers")
cred(70, "Certified Flight Registered Nurse", "Certified Flight Registered Nurse",
     "A certification from the Board of Certification for Emergency Nursing for registered nurses who care for patients during air and ground transport.",
     variants=["CFRN"])
cred(71, "Certified Foot Care Nurse", "Certified Foot Care Nurse",
     "A certification from the Wound, Ostomy and Continence Nursing Certification Board for nurses who assess and care for patients' feet.",
     variants=["CFCN"])
cred(72, "Certified Forklift Operator", "Certified Forklift Operator",
     "Proof that a worker has been trained and evaluated to operate forklifts safely, as US workplace-safety rules require an employer to certify.",
     scope="many-issuers")
cred(73, "Certified Gastroenterology Registered Nurse", "Certified Gastroenterology Registered Nurse",
     "A certification from the American Board of Certification for Gastroenterology Nurses for registered nurses who work in gastroenterology and endoscopy.",
     variants=["CGRN"])
uns(74, "Certified Grounds Management", "The wording looks like a garbled Certified Grounds Manager credential, but I cannot be sure which credential is meant.")
uns(75, "Certified Health Coach", "A generic title that many unrelated programmes award, so it does not name one credential.")
cred(76, "Certified Health Data Analyst", "Certified Health Data Analyst",
     "A certification from the American Health Information Management Association for professionals who acquire, analyse and report on health data.",
     variants=["CHDA"])
cred(77, "Certified Hemodialysis Technician", "Certified Hemodialysis Technician",
     "A certification for technicians who give hemodialysis treatments to patients with kidney failure.")
cred(78, "Certified Histotechnician", "Certified Histotechnician",
     "A certification from the ASCP Board of Certification for histotechnicians, who prepare thin tissue sections and stains for microscope examination.",
     variants=["HT(ASCP)"])
cred(79, "Certified Histotechnologist", "Certified Histotechnologist",
     "A certification from the ASCP Board of Certification for histotechnologists, who do more advanced tissue-preparation and staining work and may supervise others.",
     variants=["HTL(ASCP)"])
cred(80, "Certified Hospice And Palliative Care Administrator", "Certified Hospice and Palliative Care Administrator",
     "A certification from the Hospice and Palliative Credentialing Center for administrators of hospice and palliative care programmes.",
     variants=["CHPCA"], relations=[("related", "trs7y2g1ej")])
cred(81, "Certified Hospice And Palliative Licensed", "Certified Hospice and Palliative Licensed Nurse",
     "A certification from the Hospice and Palliative Credentialing Center for licensed practical and vocational nurses who care for hospice and palliative patients.",
     variants=["CHPLN"], relations=[("related", "trs7y2g1ej")])
cred(82, "Certified Hospice And Palliative Nurses", "Certified Hospice and Palliative Nurse",
     "A certification from the Hospice and Palliative Credentialing Center for registered nurses who care for hospice and palliative patients.",
     variants=["CHPN"], relations=[("related", "trs7y2g1ej")])
cred(83, "Certified Hospice And Palliative Nursing Assistant", "Certified Hospice and Palliative Nursing Assistant",
     "A certification from the Hospice and Palliative Credentialing Center for nursing assistants who care for hospice and palliative patients.",
     variants=["CHPNA"], relations=[("related", "trs7y2g1ej")])
cred(84, "Certified In Logistics", "Certified in Logistics, Transportation and Distribution",
     "A certification from the Association for Supply Chain Management for professionals who plan and manage logistics, transportation and distribution.",
     variants=["CLTD"])
cred(85, "Certified In Public Health", "Certified in Public Health",
     "A certification from the National Board of Public Health Examiners for public health graduates who show broad knowledge of the field.")
cred(86, "Certified Information Privacy Professional", "Certified Information Privacy Professional",
     "A certification from the International Association of Privacy Professionals showing knowledge of privacy law and practice, offered for different regions.")
cred(87, "Certified Information System Auditor", "Certified Information Systems Auditor",
     "A certification from ISACA for professionals who audit, control and assure the security of information systems.")
cred(88, "Certified Inpatient Coder", "Certified Inpatient Coder",
     "A medical coding certification from AAPC for coders who assign diagnosis and procedure codes to hospital inpatient records.",
     relations=[("related", "cyv86lx0k4")])
uns(89, "Certified Instrumentation Specialist", "Several instrumentation credentials have similar names, and I cannot tell which is meant.")
cred(90, "Certified Insurance Counselors", "Certified Insurance Counselor",
     "A designation from the National Alliance for Insurance Education & Research for insurance professionals who complete courses in coverage and risk.")
cred(91, "Certified Insurance Service Representatives", "Certified Insurance Service Representative",
     "A designation from the National Alliance for Insurance Education & Research for customer-service staff in insurance agencies.",
     variants=["CISR"])
cred(92, "Certified IRB Manager", "Certified IRB Manager",
     "A credential for managers of institutional review boards, the committees that review the ethics of research involving people.")
cred(93, "Certified Irrigation Designer", "Certified Irrigation Designer",
     "A certification from the Irrigation Association for designers of irrigation systems.")
cred(94, "Certified Labview Developer", "Certified LabVIEW Developer",
     "A certification from National Instruments showing that someone can design, build and debug well-structured LabVIEW applications.")
cred(95, "Certified Managed Care Nurse", "Certified Managed Care Nurse",
     "A certification from the American Board of Managed Care Nursing for nurses who work in managed care.",
     variants=["CMCN"])
cred(96, "Certified Management Accountant", "Certified Management Accountant",
     "A certification from the Institute of Management Accountants for accountants skilled in financial planning, analysis and control.")
uns(97, "Certified Manager Of Housing", "I cannot tell which body issues this credential or confirm the name.")
uns(98, "Certified Manufacturing Specialist", "Several manufacturing credentials have similar names, and I cannot tell which is meant.")
cma_def = "A certification from the American Association of Medical Assistants for medical assistants who pass its examination."
cred(99, "Certified Medical Assistant", "Certified Medical Assistant", cma_def, variants=["CMA (AAMA)"])
cred(100, "Certified Medical Assistant (CMA)", "Certified Medical Assistant", cma_def, variants=["CMA (AAMA)"])

# ---- write -----------------------------------------------------------------
assert sorted(A) == list(range(1, 101)), sorted(set(range(1, 101)) - set(A))
os.makedirs("work/responses", exist_ok=True)
counts = {}
for n, (frag, ans) in A.items():
    path = reqs[n - 1]
    term = json.load(open(path))["term"]
    assert frag.lower() in term.lower(), (n, frag, term)
    if ans["decision"] == "new":
        tgt = {x["id"] for x in json.load(open(path))["nearest"]}
        for r in ans["entry"]["relations"]:
            assert r["target"] in tgt, (n, r)
    open("work/responses/" + os.path.basename(path), "w").write(json.dumps(ans, indent=1, ensure_ascii=False) + "\n")
    counts[ans["decision"]] = counts.get(ans["decision"], 0) + 1
print(counts)
