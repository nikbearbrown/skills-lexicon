import json, glob, os

GK = "general-knowledge"
HERE = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(HERE, "requests")
OUT = os.path.join(HERE, "responses")
R = {}   # file stem -> response dict


def var(label):
    return {"label": label, "basis": GK}


def rel(type_, target):
    return {"type": type_, "target": target, "basis": GK}


def new(stem, name, kind, definition, variants=(), relations=(), verbs=(), cert=False, scope=None,
        lang=None, note="", reason=""):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [var(v) for v in variants],
        "relations": list(relations),
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    R[stem] = {"decision": "new", "variant_of": None, "reason": reason or "A real skill, tool, method or credential not among the nearest entries.", "entry": e}


def variant(stem, target, reason):
    R[stem] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


def nas(stem, reason):
    R[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    R[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


# ---- variants of existing entries
variant("citrix-certified-integratrion-architectu-d58adb", "wvdtj7lc5u", "Misspelling of Citrix Certified Integration Architect.")
variant("clinical-documentation-integrity-cdi-8fef44", "rb9mtm72hn", "CDI is the practice of reviewing clinical records, called documentation improvement or integrity; the credentials are CDIP and CCDS, not CDI itself.")
variant("collaborative-planning-forecasting-and-r-63462c", "qwg7xy898e", "CPFR is the abbreviation of the same supply-chain practice.")
variant("collaborative-planning-forecasting-sands-df6352", "qwg7xy898e", "Garbled spelling of Collaborative Planning, Forecasting and Replenishment.")
variant("combat-lifesaving-5a3fae", "qd53zc2hjj", "Same US Army combat lifesaver training under a different wording.")
variant("comptia-casp-ce-fcc329", "bsoj3bsv0c", "CE marks the continuing-education-renewable CompTIA CASP certification, not a different one.")
variant("comptia-cloud-ce-dcb3d8", "ovpx8drnxm", "CE marks the continuing-education-renewable CompTIA Cloud+ certification, not a different one.")
variant("comptia-cybersecurity-analyst-cysa-ce-282e91", "z3axh23kba", "CE marks the continuing-education-renewable CompTIA CySA+ certification, not a different one.")
variant("comptia-storage-powered-by-snia-ce-d03bca", "baeme4up8o", "CE marks the continuing-education-renewable CompTIA Storage+ certification, not a different one.")
variant("comptia-strata-it-fundamentals-2dde8c", "tdarv8o1wa", "Strata IT Fundamentals was the earlier name of the CompTIA IT Fundamentals certification.")
variant("cucumberjs-f27ba9", "zgnj6ebugu", "Spelling of Cucumber.js without the dot.")
variant("data-as-a-services-cf802c", "xb17x3c064", "Plural misspelling of Data as a Service.")

# ---- new entries
new("dermatology-nurse-certified-3f422f", "Dermatology Nurse Certified", "credential",
    "A certification for registered nurses who work in dermatology, awarded by the Dermatology Nursing Certification Board.",
    cert=True, scope="single-issuer")

new("design-consultation-ad2797", "Design consultation", "skill",
    "Advising clients on design choices, such as the look, layout or function of a space, product or service.")
new("design-documentation-cddec6", "Design documentation", "skill",
    "Writing and maintaining the drawings, specifications and notes that record how something is designed.")
unsure("design-driven-development-819591", "Not an established term I can pin down; it could mean design-led product development or a software practice.")
new("design-for-manufacturability-industrial--6c3490", "Design for manufacturability", "method",
    "Designing a product so that it is easy and cheap to make, by taking production methods and limits into account from the start.",
    variants=["Design for manufacturing"])
new("design-of-experiments-3ff6b0", "Design of experiments", "method",
    "Planning experiments so that the effects of several factors on a result can be measured efficiently and fairly.",
    variants=["Experimental design"])
new("design-review-fc92bb", "Design review", "method",
    "A formal checkpoint where a design is examined against its requirements so that problems are found before work continues.")
new("design-validation-80680c", "Design validation", "method",
    "Checking, usually by testing, that a finished design meets the needs of its users and its intended use.")
new("desktop-management-415835", "Desktop management", "skill",
    "Setting up, updating, securing and supporting an organisation's desktop computers and their software.")
new("desmos-mathematics-software-b5b40b", "Desmos", "tool",
    "A free online graphing calculator and set of maths learning tools.")
new("destoner-27c699", "Destoner", "tool",
    "A farm machine that separates stones and clods from soil, used to prepare fields for root crops such as potatoes.")
new("detail-conscious-c00172", "Attention to detail", "ability",
    "Being careful about small details and thorough in checking that work is accurate and complete.",
    variants=["Detail oriented"])
nas("detergent-f26b23", "A cleaning substance, not a skill.")
unsure("determinism-2956ef", "Could mean the philosophical idea, a physics principle or a computing property; the intended sense is unclear.")
new("dethatcher-195b52", "Dethatcher", "tool",
    "A machine or hand tool that removes thatch, the layer of dead grass and roots, from a lawn.")
unsure("develop-business-management-dea4af", "Looks like a fragment of a longer phrase; I cannot tell what is meant.")
new("developed-vetting-dv-89fac8", "Developed Vetting", "credential",
    "The highest level of UK government security clearance, for roles with frequent and uncontrolled access to top secret assets.",
    variants=["DV clearance"], cert=True, scope="single-issuer")
new("developing-training-materials-4ad58f", "Training material development", "skill",
    "Creating the guides, slides, exercises and other content used to teach people a job or a product.")
new("developmentally-appropriate-practice-5aae9e", "Developmentally appropriate practice", "method",
    "An approach to early childhood teaching that fits activities to children's age, individual needs and cultural background, as set out by the National Association for the Education of Young Children.")
new("devexpress-bdb370", "DevExpress", "library",
    "A suite of user-interface component and reporting libraries for .NET, web and other application development, sold by the company DevExpress.")
new("deviation-investigations-a9a2c5", "Deviation investigation", "skill",
    "Finding the cause of a departure from an approved procedure or specification, mainly in regulated manufacturing such as pharmaceuticals, and recording the findings.")
new("deviation-management-f6c99f", "Deviation management", "method",
    "The process of recording, investigating, assessing and closing out departures from approved procedures in regulated manufacturing such as pharmaceuticals.")
new("devsecops-d4236f", "DevSecOps", "method",
    "Building security checks into every stage of software development and delivery as part of a DevOps workflow.",
    relations=[rel("related", "d4xxm6t88j")])
new("dhivehi-language-472c92", "Dhivehi", "human-language",
    "The Indo-Aryan language of the Maldives, written in the Thaana script.",
    variants=["Divehi"], lang="human")
nas("diabetes-mellitus-type-2-e16a0e", "A medical condition, not a skill.")
new("diagnostic-analysis-1a3bcc", "Diagnostic analysis", "skill",
    "Examining data or a system's behaviour to work out why something happened or went wrong.")
new("diagnostic-audiology-894f52", "Diagnostic audiology", "knowledge",
    "The branch of audiology that tests hearing and balance to identify and measure disorders.")
new("dialectology-39fa30", "Dialectology", "knowledge",
    "The study of regional and social varieties of a language.")
unsure("dialer-management-platform-c97a29", "Could be contact-centre dialer software or a generic phrase; not clearly an established product category.")
unsure("dialog-system-for-sturctured-programming-0362db", "I cannot identify a specific product or method by this name and will not guess a definition.")
new("dialogflow-google-service-167c2b", "Dialogflow", "platform",
    "Google Cloud's platform for building chatbots and voice agents that understand natural language.",
    variants=["Google Dialogflow"])
new("dictaphone-7701ec", "Dictaphone", "tool",
    "A device for recording speech so that it can be played back and typed up later.")
new("dictation-2a7fe4", "Dictation", "skill",
    "Taking down spoken words as text, or speaking text aloud so that it can be recorded and typed up.")
nas("dietary-supplements-3dd195", "A product category, not a skill.")
new("dietetic-technician-registered-dtr-ndtr-0b4c24", "Nutrition and Dietetics Technician, Registered", "credential",
    "A credential from the Commission on Dietetic Registration for nutrition and dietetics technicians who have completed an accredited programme and passed the registration exam.",
    variants=["Dietetic Technician, Registered", "NDTR", "DTR"], cert=True, scope="single-issuer")
new("dietetics-f7fd09", "Dietetics", "knowledge",
    "The science and practice of using food and nutrition to promote health and treat disease.")
new("digital-ads-618ebe", "Digital advertising", "skill",
    "Planning, buying and running paid advertisements on digital channels such as search, social media and websites.")
new("digital-advertising-5481c1", "Digital advertising", "skill",
    "Planning, buying and running paid advertisements on digital channels such as search, social media and websites.",
    relations=[rel("related", "kt2njukdr4")])
new("digital-ai-d1833e", "Digital.ai", "platform",
    "A software delivery platform from the company Digital.ai that covers agile planning, release and deployment automation, and application security.")
new("digital-communications-e9d583", "Digital communications", "skill",
    "Communicating with people through digital channels such as email, messaging, video calls and social media.",
    relations=[rel("broader", "gisypzf6gf")])
new("digital-currencies-108967", "Digital currencies", "knowledge",
    "Money that exists only in electronic form, including cryptocurrencies and central bank digital currencies.")
new("digital-customer-strategy-4a4c9f", "Digital customer strategy", "skill",
    "Defining how a business will attract, serve and keep customers through digital channels, and the plan for achieving that.",
    relations=[rel("related", "im4b8pvk0p"), rel("related", "v059qbltq4")])
unsure("digital-ecosystems-617d38", "A concept used in several senses (business platforms, IT estates, ecology-inspired models); not clearly a skill.")
new("digital-fluency-12909b", "Digital fluency", "skill",
    "Using digital tools confidently and choosing the right one for the task.")
new("digital-health-technologies-683155", "Digital health technologies", "knowledge",
    "Technologies used in health care and wellbeing, such as telehealth, electronic health records, wearables and health apps.")
new("digital-humanities-e272a2", "Digital humanities", "knowledge",
    "A field that applies computing methods, such as text analysis and digital archives, to the study of the humanities.")
new("digital-journalism-c223b6", "Digital journalism", "skill",
    "Gathering and reporting news for online outlets, using digital tools such as social media, multimedia and audience analytics.")
unsure("digital-marketing-tags-f328e6", "Could mean tracking tags placed on web pages or just a topic label; the sense is unclear.")
new("digital-merchandising-07e76c", "Digital merchandising", "skill",
    "Selecting, arranging and promoting products on a website or app to help shoppers find and buy them.")
new("digital-private-network-signalling-syste-174b77", "Digital Private Network Signalling System", "standard",
    "A signalling protocol, developed by British Telecom, that lets private telephone exchanges of different makers share calls and features over digital links.",
    variants=["DPNSS"])
new("digital-rights-management-a14cbe", "Digital rights management", "knowledge",
    "Technology and policy for controlling how copyrighted digital content can be accessed, copied and shared.",
    variants=["DRM"])
new("digital-skills-b001c6", "Digital skills", "skill",
    "Being able to use computers, software and online services to do everyday and work tasks.")
nas("digital-small-and-medium-enterprises-sme-5e7fda", "A type of business, not a skill.")
new("digital-transformation-0d6ef9", "Digital transformation", "method",
    "Using digital technology to change how an organisation works, serves its customers and competes.")
new("dijkstra-s-algorithm-1b0846", "Dijkstra's algorithm", "method",
    "An algorithm that finds the shortest paths from one node of a weighted graph to all the others, as long as no edge weight is negative.",
    variants=["Dijkstra algorithm"])
new("dimensions-cm-4cc756", "Dimensions CM", "tool",
    "Software for version control and for managing changes and releases of software assets, now sold by OpenText.")
new("dinka-language-eea309", "Dinka", "human-language",
    "A Nilotic language spoken by the Dinka people of South Sudan.", lang="human")
nas("diphtheria-905e7a", "A disease, not a skill.")
new("diploma-in-hotel-management-and-catering-fc8fe3", "Diploma in Hotel Management and Catering Technology", "credential",
    "A diploma, awarded by technical boards and polytechnic institutions in India, covering hotel operations, food production and catering.",
    cert=True, scope="many-issuers")
new("direct-digital-control-3cb9fa", "Direct digital control", "knowledge",
    "Using microprocessor-based controllers, rather than analogue ones, to control building systems such as heating, ventilation and cooling.")
new("directx-video-acceleration-452d09", "DirectX Video Acceleration", "library",
    "A Microsoft programming interface that lets video decoding and processing run on a computer's graphics hardware.",
    variants=["DXVA"])
nas("dirichlet-a6f1bd", "A mathematician's surname that appears in many different concept names, not a skill by itself.")
new("disability-insurance-20901c", "Disability insurance", "knowledge",
    "Insurance that pays part of a person's income if illness or injury stops them from working.")
new("disaster-loans-ffc9da", "Disaster loans", "knowledge",
    "Loans that help people and businesses repair or rebuild after a disaster, most notably the low-interest loans made by the US Small Business Administration.")
nas("discharges-f5afb7", "A generic plural noun with several unrelated meanings, not a skill.")
new("discipleship-25a431", "Discipleship", "skill",
    "Teaching and mentoring people in Christian faith and practice, often one to one or in small groups.")
unsure("discrimination-testing-50fb3b", "Two unrelated senses are possible (sensory-science tests and civil-rights audit testing).")
nas("dishwashers-8e55d7", "An appliance or a job title, not a skill.")
new("dispute-management-e2bb4d", "Dispute management", "skill",
    "Handling and resolving disagreements or contested claims, such as disputed payments, between parties.")
unsure("dissipation-thermodynamics-669d0c", "A physical phenomenon; unclear whether it is meant as a body of knowledge or a skill.")
new("distance-learning-23830b", "Distance learning", "method",
    "Teaching and learning in which students and instructors are in different places, usually connected by online tools.",
    relations=[rel("related", "w1blu9iu00")])
unsure("distribution-softwares-de96e3", "Could mean software for managing wholesale distribution or software distribution; the sense is unclear.")
nas("dithiothreitol-fc9735", "A laboratory chemical, not a skill.")
new("divemaster-dm-qualification-fe9487", "Divemaster", "credential",
    "A professional scuba-diving rating for people who lead and supervise certified divers, awarded by diving training agencies such as PADI, SSI and NAUI.",
    cert=True, scope="many-issuers")
new("divide-and-conquer-45c53e", "Divide and conquer", "method",
    "An algorithm design technique that splits a problem into smaller subproblems, solves each, and combines the results.")
new("docker-9f1141", "Docker", "platform",
    "A platform for building, shipping and running applications in containers.",
    verbs=["containerize", "deploy"])
nas("docket-court-e2132e", "A court's list of cases or a record of one, not a skill.")
new("docking-molecular-c3c304", "Molecular docking", "method",
    "A computational method that predicts how a small molecule, such as a drug candidate, binds to a target protein.")
new("docsis-6781b3", "DOCSIS", "standard",
    "The CableLabs family of standards for carrying internet data over cable television networks.",
    variants=["Data Over Cable Service Interface Specification"])
new("doctor-of-dental-medicine-dmd-68e46d", "Doctor of Dental Medicine", "credential",
    "A professional doctoral degree in dentistry, awarded by dental schools in the United States and elsewhere.",
    variants=["DMD"], cert=True, scope="many-issuers")
new("doctor-of-dental-surgery-dds-7c4117", "Doctor of Dental Surgery", "credential",
    "A professional doctoral degree in dentistry, awarded by dental schools in the United States and elsewhere.",
    variants=["DDS"], cert=True, scope="many-issuers")
new("doctor-of-medicine-md-e283f6", "Doctor of Medicine", "credential",
    "A professional doctoral degree in medicine that qualifies graduates to go on to practise as physicians.",
    cert=True, scope="many-issuers")
new("doctor-of-nursing-practice-706c1d", "Doctor of Nursing Practice", "credential",
    "A practice-focused doctoral degree in nursing for advanced clinical practice, leadership and nursing care improvement.",
    variants=["DNP"], cert=True, scope="many-issuers")
new("doctor-of-pharmacy-pharmd-dcae66", "Doctor of Pharmacy", "credential",
    "A professional doctoral degree in pharmacy that qualifies graduates to go on to practise as pharmacists.",
    variants=["PharmD"], cert=True, scope="many-issuers")
new("doctor-of-veterinary-medicine-dvm-vmd-4a1d7e", "Doctor of Veterinary Medicine", "credential",
    "A professional doctoral degree in veterinary medicine, awarded as DVM by most schools and as VMD by the University of Pennsylvania.",
    variants=["DVM", "VMD"], cert=True, scope="many-issuers")
new("docusign-software-f88174", "DocuSign", "platform",
    "A platform for sending, signing and managing agreements electronically.")
new("dod-information-assurance-certification--4f1d4e", "DoD Information Assurance Certification and Accreditation Process", "method",
    "The US Department of Defense process, used before the Risk Management Framework replaced it, for certifying and accrediting the security of information systems.",
    variants=["DIACAP"],
    note="The legacy list calls it a certification, but it accredits information systems and is not a credential awarded to a person.")
new("dodaf-5854c0", "DoDAF", "framework",
    "The US Department of Defense's architecture framework, which defines viewpoints and models for describing enterprise and system architectures.",
    variants=["DoD Architecture Framework", "Department of Defense Architecture Framework"])

# ---- write
reqs = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(REQ, "*.json")))
missing = [r for r in reqs if r not in R]
extra = [r for r in R if r not in reqs]
assert not missing and not extra, (missing, extra)
os.makedirs(OUT, exist_ok=True)
for stem, resp in R.items():
    with open(os.path.join(OUT, stem + ".json"), "w", encoding="utf-8") as fh:
        json.dump(resp, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
import collections
print(len(R), collections.Counter(r["decision"] for r in R.values()))
