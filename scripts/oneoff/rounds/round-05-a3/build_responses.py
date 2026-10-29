import json, glob, os, sys

REQ = "work/requests"
OUT = "work/responses"
GK = "general-knowledge"
R = {}  # file stem -> response dict


def new(stem, name, kind, definition, variants=(), relations=(), cert=False, scope=None, lang=None, reason="", note=""):
    e = {
        "preferred_name": name,
        "kind": kind,
        "definition": definition,
        "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    R[stem] = {"decision": "new", "variant_of": None, "reason": reason or "A recognisable skill, tool, method or field.", "entry": e}


def no(stem, reason):
    R[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    R[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


new("gynaecology-5692be", "Gynaecology", "knowledge",
    "The branch of medicine that deals with the health of the female reproductive system.",
    variants=["Gynecology"], reason="A medical specialty, so a field of knowledge.")

new("h-262-mpeg-2-part-2-00bd1e", "H.262/MPEG-2 Part 2", "standard",
    "A video compression standard published jointly by ITU-T as H.262 and by ISO/IEC as MPEG-2 Part 2.",
    variants=["H.262", "MPEG-2 Part 2", "MPEG-2 Video"], reason="A published video coding standard.")

new("hadoop-distributed-file-system-a88508", "Hadoop Distributed File System", "tool",
    "The distributed file system of Apache Hadoop, which stores large files across many machines.",
    variants=["HDFS"], relations=[("related", "h4ck1veoae")], reason="A named storage component of Apache Hadoop.")

new("hadrons-partical-physics-f0c368", "Hadron physics", "knowledge",
    "The study of hadrons, the composite particles such as protons and neutrons that are made of quarks and held together by the strong interaction.",
    reason="A topic within particle physics; the tag misspells particle.")

new("hair-clipper-9b5162", "Hair clipper", "tool",
    "An electric device with a moving blade that is used to cut or trim hair, common in barbering.",
    reason="A piece of equipment barbers are asked to use.")

no("hairnet-09f1ba", "An item of protective clothing, not a skill.")

new("hammer-file-system-69f75f", "HAMMER file system", "tool",
    "A file system created for the DragonFly BSD operating system, with snapshots and fine-grained history.",
    reason="A named file system.")

new("hammer-js-773253", "Hammer.js", "library",
    "A JavaScript library that recognises touch gestures such as swipe, pinch and rotate in web pages.",
    variants=["HammerJS"], reason="A named JavaScript library.")

new("hand-lettering-58df4f", "Hand lettering", "skill",
    "Drawing letters by hand as decorative artwork, rather than typing them or using a typeface.",
    reason="A developed craft capacity.")

new("hand-therapy-6d49ee", "Hand therapy", "skill",
    "Rehabilitating injuries and conditions of the hand, wrist and arm, usually as an occupational or physical therapist.",
    reason="A clinical rehabilitation specialty.")

new("handle-systems-1bcf0e", "Handle System", "standard",
    "A system for assigning, managing and resolving persistent identifiers for digital objects, specified in IETF RFCs and run by CNRI.",
    reason="A specified identifier infrastructure; kind is the closest fit.")

new("handlebars-js-372b1d", "Handlebars.js", "library",
    "A JavaScript templating library that builds HTML from templates with placeholders for data.",
    reason="A named JavaScript library.")

new("hapi-js-636970", "hapi", "framework",
    "A Node.js framework for building web applications and services, with configuration-driven routing and plugins.",
    variants=["Hapi.js", "Hapijs"], reason="A named Node.js framework; Hapi.js and Hapijs are the same concept.")
new("hapijs-5565ac", "hapi", "framework",
    "A Node.js framework for building web applications and services, with configuration-driven routing and plugins.",
    variants=["Hapi.js", "Hapijs"], reason="A named Node.js framework; Hapi.js and Hapijs are the same concept.")

new("hardware-configuration-management-4487a7", "Hardware configuration management", "skill",
    "Tracking and controlling the versions, settings and changes of hardware components and systems.",
    reason="A developed management capacity.")

new("hardware-description-language-208c47", "Hardware description language", "modeling-language",
    "A class of specialised computer languages, such as VHDL and Verilog, used to describe the structure and behaviour of electronic circuits.",
    lang="programming", reason="A class of formal languages for modelling circuits; not a single language.")

new("hashistack-software-70f065", "HashiStack", "platform",
    "An informal name for the group of HashiCorp infrastructure tools, such as Terraform, Vault, Consul and Nomad.",
    reason="An informal name for a product suite.")

new("havigannada-dialects-ec294b", "Havyaka Kannada", "human-language",
    "A dialect of Kannada traditionally spoken by the Havyaka Brahmin community in Karnataka and nearby areas.",
    variants=["Havigannada"], lang="human", reason="A spoken dialect, treated as a human language.")

new("hawaiian-language-474321", "Hawaiian", "human-language",
    "A Polynesian language native to Hawaii and one of the two official languages of the state.",
    variants=["ʻŌlelo Hawaiʻi"], lang="human", reason="A human language.")

new("haya-language-889510", "Haya", "human-language",
    "A Bantu language spoken by the Haya people, mainly in the Kagera region of northwestern Tanzania.",
    lang="human", reason="A human language.")

new("hazard-analysis-and-critical-control-poi-debee1", "Hazard Analysis and Critical Control Points", "method",
    "A systematic, preventive approach to food safety that finds hazards and sets controls at the critical points where they can be prevented or removed.",
    variants=["HACCP"], reason="A named food-safety method.")

new("hazardous-material-containment-and-contr-fc4dd1", "Hazardous material containment and control", "skill",
    "Preventing and containing releases of hazardous materials and controlling people's exposure to them.",
    reason="A developed safety capacity.")

new("hazardous-material-handling-30805b", "Hazardous material handling", "skill",
    "Storing, moving and using hazardous materials safely and in line with the rules for them.",
    variants=["Hazmat handling"], reason="A developed safety capacity.")

new("hazmat-endorsement-7cb8e5", "Hazmat endorsement", "credential",
    "A commercial driver's licence endorsement that permits transporting hazardous materials, issued after a security background check.",
    variants=["Hazardous materials endorsement"],
    relations=[("related", "sli7qqx1gw"), ("related", "xpo0iet9cq")],
    cert=True, scope="many-issuers", reason="A licence endorsement that each US state issues under common federal rules.")

new("head-mounted-displays-hmd-ac85dc", "Head-mounted display", "tool",
    "A display worn on the head, such as a virtual or augmented reality headset, that places images in front of the user's eyes.",
    reason="A category of hardware used in virtual and augmented reality.")

no("headlamp-6909ba", "An item of equipment worn on the head, not a skill.")

new("health-and-wellness-coaching-887cb0", "Health and wellness coaching", "skill",
    "Guiding clients to set and reach health and lifestyle goals through structured conversations and support for behaviour change.",
    reason="A developed capacity to coach others.")

new("health-care-finance-administration-hcfa--ec94bd", "HCFA regulations", "standard",
    "Medicare and Medicaid rules issued by the US Health Care Financing Administration, which was renamed the Centers for Medicare & Medicaid Services in 2001.",
    variants=["Health Care Financing Administration regulations"],
    reason="Regulations of a named US agency; the tag spells Financing as Finance.")

new("health-economics-and-outcomes-research-h-d847ae", "Health economics and outcomes research", "knowledge",
    "The field that applies economic and outcomes-measurement methods to judge the value, cost and effects of health care interventions.",
    variants=["HEOR"], reason="A research field.")

unsure("health-insurance-portability-and-account-4b6d7c",
       "It looks like a level of a HIPAA certification scheme, but I cannot name the body that awards it.")
unsure("health-insurance-portability-and-account-95b551",
       "It looks like a level of a HIPAA certification scheme, but I cannot name the body that awards it.")

unsure("health-products-health-canada-4bf996",
       "It could mean a product category regulated by Health Canada or knowledge of that regulation, and I cannot tell which.")

new("health-safety-and-environment-04b9ce", "Health, safety and environment", "knowledge",
    "The field concerned with protecting people and the environment from workplace hazards and with meeting the related legal requirements.",
    reason="A recognised workplace field.")

no("health-savings-account-de012a", "A tax-advantaged financial account, usually offered as a benefit, not a skill.")

new("healthcare-delivery-science-a6ad49", "Healthcare delivery science", "knowledge",
    "The study of how health care services are organised, delivered and improved to raise quality, access and value.",
    reason="An academic and professional field.")

new("healthcare-effectiveness-data-and-inform-4cae9d", "Healthcare Effectiveness Data and Information Set", "standard",
    "A set of standardised measures of health plan performance, maintained by the National Committee for Quality Assurance.",
    variants=["HEDIS"], reason="A published measure set.")

new("healthcare-facilities-planning-1b4ff3", "Healthcare facilities planning", "skill",
    "Planning the space, equipment and services of hospitals and other health care buildings.",
    reason="A developed planning capacity.")

new("healthcare-industry-knowledge-9f5afd", "Healthcare industry knowledge", "knowledge",
    "Understanding of how the health care sector works, including its providers, payers, regulation and terminology.",
    reason="General domain knowledge of one sector; broad.")

new("healthcare-quality-186ab2", "Healthcare quality", "knowledge",
    "The study and practice of measuring and improving the safety, effectiveness and patient focus of health care services.",
    reason="A recognised field within health care management.")

no("healthcare-reforms-669553", "A policy topic or set of events, not a skill or field.")

new("healthcare-strategy-49c556", "Healthcare strategy", "skill",
    "Setting long-term goals and plans for a health care organisation, such as its services, markets and partnerships.",
    reason="A developed planning capacity.")

new("hearing-aid-software-ebb66c", "Hearing aid software", "tool",
    "Software used to fit, program and adjust hearing aids to a person's hearing loss.",
    reason="A software category, like the existing Email software entry.")

no("hearing-impairment-2f596e", "A condition, not a skill.")
no("heartworm-0a161e", "A parasitic disease of animals, not a skill.")

new("heat-bending-of-wood-b544af", "Heat bending of wood", "skill",
    "Shaping wood into curves by softening it with heat or steam and bending it around a form.",
    reason="A woodworking technique.")

new("heatmap-ee8162", "Heatmap", "method",
    "A data visualisation that shows the size of values as colours across a grid or an area.",
    variants=["Heat map"], reason="A visualisation technique.")

new("heavy-equipment-operation-40cb73", "Heavy equipment operation", "skill",
    "Operating large construction and earthmoving machines such as excavators, bulldozers and loaders.",
    reason="A developed operating capacity.")

no("heavy-industry-c3a964", "An industry sector, not a skill.")

new("heavy-vehicle-operation-d71f2f", "Heavy vehicle operation", "skill",
    "Driving large road vehicles such as trucks and buses.",
    reason="A developed driving capacity.")

no("hepatitis-b-b5bb08", "A disease, not a skill.")
no("heritage-tourism-819fdf", "A segment of the tourism industry, not a skill.")

new("heritrix-2885d4", "Heritrix", "tool",
    "An open-source, archival-quality web crawler developed by the Internet Archive.",
    reason="A named web crawler.")

unsure("high-integrity-065cc8",
       "It could be a personal trait or high-integrity software engineering, and with no context I cannot tell which.")
unsure("high-integrity-b9a29b",
       "It could be a personal trait or high-integrity software engineering, and with no context I cannot tell which.")

new("higher-education-law-627bc3", "Higher education law", "knowledge",
    "The body of law that governs colleges and universities, including student rights, accreditation, funding and employment.",
    reason="A legal practice area.")

new("higher-education-policy-547de2", "Higher education policy", "knowledge",
    "The study and practice of the public and institutional rules, funding and governance that shape colleges and universities.",
    reason="A policy field.")

new("higher-national-certificate-9293ab", "Higher National Certificate", "credential",
    "A UK vocational qualification of about one year of full-time higher-education study, awarded by bodies such as Pearson and the Scottish Qualifications Authority.",
    variants=["HNC"], cert=True, scope="many-issuers",
    reason="A qualification awarded by more than one UK body.")

unsure("highly-confident-letter-4f7097", "I do not know what this term refers to.")

new("hindii-4c153d", "HincII", "tool",
    "A type II restriction enzyme, formerly named HindII, that cuts DNA at a specific six-base recognition sequence.",
    variants=["HindII"], reason="A named laboratory enzyme; HindII is its former name.")

new("hindiii-43ec5c", "HindIII", "tool",
    "A type II restriction enzyme from Haemophilus influenzae that cuts DNA at the sequence AAGCTT.",
    reason="A named laboratory enzyme.")

new("hindsight-bias-cefcff", "Hindsight bias", "knowledge",
    "The tendency, after an outcome is known, to believe one would have predicted it.",
    reason="A named concept in psychology and decision-making.")

no("hints-eef8e8", "A generic word, not a skill.")

new("historic-preservation-4c5691", "Historic preservation", "knowledge",
    "The field of protecting and conserving historic buildings, sites and objects.",
    reason="A recognised professional field.")

no("historical-events-1fbe5f", "A generic phrase, not a skill.")

new("historical-linguistics-e9f48c", "Historical linguistics", "knowledge",
    "The study of how languages change over time and how they are related to one another.",
    relations=[("related", "hm380yneeh")], reason="A branch of linguistics.")

new("history-of-education-97aeed", "History of education", "knowledge",
    "The study of how education and schooling have developed over time.",
    reason="An academic field.")

new("history-of-medicine-78175f", "History of medicine", "knowledge",
    "The study of how medical practice, knowledge and institutions have developed over time.",
    reason="An academic field.")

new("history-of-philosophy-067e91", "History of philosophy", "knowledge",
    "The study of how philosophical ideas and thinkers have developed over time.",
    relations=[("related", "fkdu4zhgon")], reason="An academic field.")

new("history-of-science-f1e65e", "History of science", "knowledge",
    "The study of how scientific ideas, methods and institutions have developed over time.",
    reason="An academic field.")

new("hockett-s-design-features-96bcfd", "Hockett's design features", "knowledge",
    "A set of features proposed by the linguist Charles Hockett that characterise human language and set it apart from animal communication.",
    reason="A named framework in linguistics.")

new("hokkien-dialects-50cd9c", "Hokkien", "human-language",
    "A group of Southern Min varieties of Chinese from Fujian, also spoken in Taiwan and Southeast Asia.",
    lang="human", reason="A spoken language group.")

new("hololens-9ca595", "Microsoft HoloLens", "tool",
    "A mixed-reality headset made by Microsoft that overlays holograms on the user's view of the real world.",
    reason="A named hardware product.")

no("holoprosencephaly-84740c", "A medical condition, not a skill.")
no("home-healthcare-dfc486", "A care setting or service sector, not a skill.")

new("honeypot-b37e6e", "Honeypot", "tool",
    "A decoy system or resource set up to attract attackers so their methods can be detected and studied.",
    reason="A security tool.")

unsure("hooking-a186a7",
       "The term has several unrelated senses, such as software function hooking and rug hooking, and there is no context to choose.")

new("hootsuite-social-media-management-softwa-c7ceae", "Hootsuite", "platform",
    "A social media management platform for scheduling posts, monitoring accounts and reporting on results.",
    reason="A named product.")

no("hop-networking-332817", "A term for one step between network devices, not a skill.")

new("hopi-language-4daaad", "Hopi", "human-language",
    "A Uto-Aztecan language spoken by the Hopi people of northeastern Arizona.",
    lang="human", reason="A human language.")

no("horticultural-therapist-assistant-25fafd", "Reads as a job title, not a skill.")
no("hospitality-network-c1ac01", "A generic phrase, not a skill.")

new("host-based-security-system-hbss-154962", "Host Based Security System", "platform",
    "The US Department of Defense's endpoint security suite, built on McAfee ePolicy Orchestrator, for monitoring and protecting hosts.",
    variants=["HBSS"], reason="A named security suite.")

new("hotel-and-restaurant-management-9f470a", "Hotel and restaurant management", "skill",
    "Running the operations of hotels and restaurants, including staff, service, finances and guest satisfaction.",
    reason="A developed management capacity.")

new("hotel-management-874e0a", "Hotel management", "skill",
    "Overseeing the daily operation of a hotel, including rooms, staff, finances and guest service.",
    reason="A developed management capacity.")

new("hotjava-3cfb44", "HotJava", "tool",
    "A web browser written in Java by Sun Microsystems in the 1990s.",
    relations=[("related", "ls6hrpynv0")], reason="A named web browser.")

no("hotline-cc8563", "A generic word, not a skill.")

new("hp-2100-b64c02", "HP 2100", "tool",
    "A series of 16-bit minicomputers made by Hewlett-Packard from the 1960s.",
    reason="A named hardware product line.")

new("hp-9845c-1e2028", "HP 9845C", "tool",
    "A colour-display model of Hewlett-Packard's HP 9845 series of technical desktop computers.",
    reason="A named hardware product.")

new("hp-application-lifecycle-management-alm-eef312", "HP Application Lifecycle Management", "tool",
    "HP's software suite for managing requirements, testing and defects across the life of a software application.",
    variants=["HP ALM"], reason="A named HP product.")

new("hp-brio-5d69af", "HP Brio", "tool",
    "A line of business desktop personal computers sold by Hewlett-Packard.",
    reason="A named hardware product line.")

new("hp-jornada-pda-f4a613", "HP Jornada", "tool",
    "A line of Hewlett-Packard handheld computers and personal digital assistants running Windows CE.",
    reason="A named hardware product line.")

new("hp-newwave-97a6b5", "HP NewWave", "platform",
    "A graphical, object-oriented desktop environment from Hewlett-Packard that ran on top of Microsoft Windows.",
    reason="A named software environment.")

unsure("hp-omni-10-3a03e8",
       "It could be an HP tablet or part of the HP Omni all-in-one range, and I am not sure which.")

new("hp-quality-centers-690963", "HP Quality Center", "tool",
    "A test management tool from HP, originally developed by Mercury Interactive, for managing requirements, test cases and defects.",
    reason="A named HP product; the tag pluralises Center.")

new("hp-systems-insight-manager-b95699", "HP Systems Insight Manager", "tool",
    "HP software for monitoring and managing HP servers, storage and network devices from one console.",
    variants=["HP SIM"], reason="A named HP product.")

new("hp-winrunner-8dbab5", "HP WinRunner", "tool",
    "An automated functional testing tool, originally from Mercury Interactive, that records and replays user actions on graphical applications.",
    reason="A named testing tool.")

new("hr-analytics-946948", "HR analytics", "skill",
    "Analysing workforce data to inform decisions about hiring, retention, pay and performance.",
    variants=["People analytics"], reason="A developed analytical capacity.")

new("html-emails-9e56de", "HTML emails", "skill",
    "Designing and coding email messages in HTML, allowing for the uneven way email clients display them.",
    variants=["HTML email"], reason="A developed web-coding capacity.")

new("hvac-automation-systems-7a127b", "HVAC automation systems", "knowledge",
    "Systems that automatically monitor and control heating, ventilation and air conditioning equipment in buildings.",
    reason="Follows the existing Barcode systems entry, a technology area.")

new("hvac-controls-b8b1c8", "HVAC controls", "knowledge",
    "The sensors, thermostats and controllers that regulate heating, ventilation and air conditioning equipment.",
    reason="Follows the existing Barcode systems entry, a technology area.")

# ---- write ----
stems = sorted(os.path.basename(f)[:-5] for f in glob.glob(f"{REQ}/*.json"))
missing = [s for s in stems if s not in R]
extra = [s for s in R if s not in stems]
if missing or extra:
    print("missing", missing, "extra", extra)
    sys.exit(1)
os.makedirs(OUT, exist_ok=True)
for s in stems:
    req = json.load(open(f"{REQ}/{s}.json"))
    ids = {n["id"] for n in req["nearest"]}
    for r in (R[s].get("entry") or {}).get("relations", []):
        assert r["target"] in ids, (s, r)
    kinds = req["allowed"]["kinds"]
    if R[s]["entry"]:
        assert R[s]["entry"]["kind"] in kinds, (s, R[s]["entry"]["kind"])
    json.dump(R[s], open(f"{OUT}/{s}.json", "w"), ensure_ascii=False, indent=1)
    open(f"{OUT}/{s}.json", "a").write("\n")
from collections import Counter
print(Counter(R[s]["decision"] for s in stems))
