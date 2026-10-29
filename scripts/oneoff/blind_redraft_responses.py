import json, sys
from pathlib import Path

ROOT = Path("/home/user/agent2/skills-lexicon/work")
GK = "general-knowledge"
R = {}


def new(stem, name, kind, defn, variants=(), rels=(), verbs=(), cert=False, lang=None, note="", reason=""):
    R[stem] = {
        "decision": "new", "variant_of": None,
        "reason": reason or "A real skill, tool, credential or concept that I know from general knowledge.",
        "entry": {
            "preferred_name": name, "kind": kind, "definition": defn, "definition_basis": GK,
            "variants": [{"label": v, "basis": GK} for v in variants],
            "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in rels],
            "verbs": [{"verb": v, "basis": GK} for v in verbs],
            "certification": {"value": cert, "basis": GK},
            "language_type": {"value": lang, "basis": GK},
            "annotation_note": note,
        }}


def nas(stem, reason):
    R[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    R[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def variant(stem, target, reason):
    R[stem] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


new("3d-solid-and-surface-modeling-b5ebe3", "3D solid and surface modeling", "skill",
    "Creating three-dimensional computer models of objects using solid modeling and surface modeling techniques, usually in CAD software.")

new("additive-manufacturing-b9e88c", "Additive manufacturing", "method",
    "Manufacturing that builds objects layer by layer by adding material from a digital design, as in 3D printing.",
    variants=["3D printing"])

new("administering-blood-tests-a72b3d", "Administering blood tests", "skill",
    "Carrying out blood tests on patients, typically by collecting a blood sample and having it analysed.")

unsure("adult-gerontology-acute-care-nurse-pract-b0eb75",
       "Names a nurse-practitioner role (a job title) that is also a certification track, and the tag does not say which is meant.")

new("advanced-trauma-life-support-51489a", "Advanced Trauma Life Support", "credential",
    "A trauma training course from the American College of Surgeons that teaches a systematic approach to assessing and treating injured patients and is completed with a provider certificate.",
    variants=["ATLS"], cert=True)

nas("advisories-32da62", "A generic word with no skill, tool or credential behind it.")

nas("agile-edge-technologies-db566e", "Looks like a company name, not a skill.")

new("american-board-of-medical-laboratory-imm-ec032f", "American Board of Medical Laboratory Immunology certification", "credential",
    "A certification awarded by the American Board of Medical Laboratory Immunology to laboratory scientists qualified in medical laboratory immunology.",
    variants=["ABMLI certification"], cert=True)

new("arkit-dab330", "ARKit", "framework",
    "Apple's software framework for building augmented reality experiences on iOS and iPadOS devices.")

unsure("aws-big-data-358dde",
       "Could mean the retired AWS Certified Big Data - Specialty certification or AWS big data services in general, and the tag does not say which.")

new("aymara-language-d8ba9b", "Aymara", "human-language",
    "An Aymaran language spoken by the Aymara people of the Andes, mainly in Bolivia, Peru and Chile.",
    lang="spoken")

nas("betfair-bd7059", "A company (betting exchange), not a skill.")

nas("bleeding-756b11", "A generic medical word, not a skill.")

new("board-support-package-software-c9e11f", "Board support package", "knowledge",
    "The layer of low-level software, such as the bootloader and hardware drivers, that lets an operating system run on a particular hardware board.")

new("cadvisor-99cd55", "cAdvisor", "tool",
    "An open-source tool, originally from Google, that collects and exposes resource usage and performance data for running containers.")

nas("catering-companies-17c486", "Names a type of business, not a skill.")

nas("cbht-dt-65ad5a", "Appears to be a television station call sign (a broadcaster), not a skill.")

new("certified-forensic-computer-examination-328603", "Certified Forensic Computer Examiner", "credential",
    "A professional certification from the International Association of Computer Investigative Specialists (IACIS) for examiners of digital evidence on computers.",
    variants=["CFCE"], cert=True,
    reason="Almost certainly the IACIS CFCE credential, whose official title is Certified Forensic Computer Examiner.")

new("certified-pediatric-emergency-nurse-cffb01", "Certified Pediatric Emergency Nurse", "credential",
    "A certification from the Board of Certification for Emergency Nursing for registered nurses who work in pediatric emergency care.",
    variants=["CPEN"], cert=True)

new("certified-professional-geologist-f55817", "Certified Professional Geologist", "credential",
    "A professional certification from the American Institute of Professional Geologists for qualified practising geologists.",
    cert=True)

new("comptia-mobility-3c683e", "CompTIA Mobility+", "credential",
    "A vendor-neutral CompTIA certification covering the management and security of mobile devices in an enterprise.",
    cert=True)

unsure("core-api-e7e4af",
       "'Core API' is the name of an API in many unrelated products and the tag gives no sign which one is meant.")

new("dagger-2-7bf164", "Dagger 2", "framework",
    "A compile-time dependency injection framework for Java and Android, maintained by Google.")

new("data-wrangling-d60444", "Data wrangling", "skill",
    "Cleaning, restructuring and combining raw data into a form suitable for analysis.",
    variants=["data munging"], rels=[("related", "uclexd8uv3")], verbs=["clean", "transform"])

unsure("database-programmer-s-toolkits-8b1a37",
       "I cannot tell what this refers to; it may be a generic set of database programming tools or a specific product I do not recognise.")

new("dbvisualizer-6181d1", "DbVisualizer", "tool",
    "A universal database client and SQL tool for querying and managing many kinds of databases.",
    verbs=["query"])

new("deposition-geology-ffcdb3", "Deposition (geology)", "knowledge",
    "The geological process by which sediments, soil or rock fragments are laid down on a surface by wind, water, ice or gravity.")

unsure("design-surface-e25869",
       "Could mean the visual designer area of an IDE such as Visual Studio, surface design in CAD, or something else; the tag does not say.")

unsure("deterministic-methods-7abc97",
       "A very broad phrase for approaches that give the same result for the same input, with no domain stated, so it is unclear what skill is meant.")

new("doctor-of-physical-therapy-65aabb", "Doctor of Physical Therapy", "credential",
    "A professional doctoral degree that qualifies graduates to practise as physical therapists.",
    variants=["DPT"], cert=True)

new("doctor-of-public-health-2a8819", "Doctor of Public Health", "credential",
    "A professional doctoral degree in public health.",
    variants=["DrPH"], cert=True)

new("doubles-endorsement-04842a", "Doubles/triples endorsement", "credential",
    "A commercial driver's licence endorsement that permits the holder to tow double or triple trailers.",
    cert=True)

new("drone-pilot-certificate-ecf021", "Drone pilot certificate", "credential",
    "A certificate issued by an aviation authority, such as the US FAA's remote pilot certificate, showing that a person is qualified to fly unmanned aircraft.",
    variants=["remote pilot certificate"], cert=True)

new("dynamic-cycle-counting-4fa066", "Dynamic cycle counting", "method",
    "A form of inventory cycle counting in which counts are triggered by events, such as a stock movement or an empty bin, rather than by a fixed schedule.")

new("electronic-paper-650333", "Electronic paper", "knowledge",
    "A display technology that mimics the look of ink on paper by reflecting ambient light instead of emitting its own.",
    variants=["e-paper"])

new("esker-software-a3498a", "Esker", "platform",
    "A cloud software platform from the company Esker that automates document-based business processes such as order-to-cash and procure-to-pay.")

new("express-js-9fa594", "Express.js", "framework",
    "A minimal web application framework for Node.js.",
    variants=["ExpressJS"])

unsure("flexi-photoshop-plugin-55aa33",
    "I do not recognise a Photoshop plugin called Flexi well enough to say what it does.")

new("french-languages-c09310", "French", "human-language",
    "A Romance language spoken in France and many other countries, and an official language of numerous international organisations.",
    variants=["French language"], lang="spoken")

unsure("functional-analysis-90aa89",
       "Ambiguous: it is a branch of mathematics but is also used in systems engineering and behaviour analysis, and the tag gives no domain.")

nas("good-driving-record-e7fc83", "A hiring requirement about a person's history, not a skill.")

nas("hotel-industry-bf4022", "Names an industry, not a skill.")

new("html-formatting-4f71d7", "HTML formatting", "skill",
    "Applying HTML tags and attributes to structure and present text and other content on a web page.")

new("iam-level-i-certification-55d038", "IAM Level I", "standard",
    "A category of the US Department of Defense information assurance workforce requirements (DoD 8570) for information assurance managers, met by holding one of several approved baseline certifications.",
    cert=False,
    note="It is a DoD workforce qualification level met by any of several approved certifications, not a single credential issued by one body.",
    reason="Most likely the DoD 8570 IAM Level I workforce category, which is a requirement level rather than a credential.")

new("ibm-power8-microprocessors-e58f6f", "IBM POWER8", "knowledge",
    "IBM's POWER8 line of microprocessors, introduced in 2014 for its Power Systems servers.",
    variants=["POWER8"])

new("insightvm-vulnerability-scanning-softwar-36fc93", "InsightVM", "tool",
    "A vulnerability management product from Rapid7 that scans systems for security weaknesses.",
    verbs=["scan"])

new("interactive-3d-b99f50", "Interactive 3D", "skill",
    "Creating three-dimensional content that users can explore or manipulate in real time.")

unsure("intermediate-language-e80d98",
       "Could mean a compiler or virtual-machine intermediate representation such as .NET CIL, or an intermediate proficiency level in a spoken language; the tag does not say which.")

nas("ironworker-d4ab11", "A job title (a trade), not a skill.")

new("jacoco-325777", "JaCoCo", "tool",
    "A free Java code coverage library that measures how much of a program's code is run by its tests.")

new("jsdata-2a4512", "JSData", "library",
    "A JavaScript library that manages an in-memory store of application data and maps it to backend resources through adapters.",
    reason="I know js-data as a JavaScript data-store library; it is unrelated to Java despite the similar spelling.")

new("karaf-02ed79", "Apache Karaf", "platform",
    "An Apache runtime container for deploying and managing OSGi-based Java applications.",
    verbs=["deploy"])

nas("law-enforcement-operations-5b1ab8", "Names a field of work or sector rather than a specific skill.")

nas("living-conditions-0e76da", "A generic phrase, not a skill.")

nas("management-training-e2822e", "A generic phrase that could mean giving or having had training; not a defined skill.")

new("marathi-language-06f8a1", "Marathi", "human-language",
    "An Indo-Aryan language spoken mainly in the Indian state of Maharashtra, where it is the official language.",
    lang="spoken")

new("master-of-laws-7d7cf3", "Master of Laws", "credential",
    "A postgraduate law degree, usually taken after a first law degree.",
    cert=True)

new("master-of-laws-in-taxation-b2481b", "Master of Laws in Taxation", "credential",
    "A postgraduate law degree that specialises in tax law.",
    cert=True)

nas("masterpiece-99d118", "A generic word, not a skill.")

new("masters-certificate-in-project-managemen-0135b7", "Master's Certificate in Project Management", "credential",
    "A graduate-level university certificate in project management that is shorter than a master's degree.",
    rels=[("related", "z83cabeb9c")], cert=True)

new("media-center-markup-language-02a87e", "Media Center Markup Language", "markup-language",
    "An XML-based markup language used to build user interfaces for applications in Microsoft's Windows Media Center.",
    variants=["MCML"], lang="other")

new("mixed-reality-46185f", "Mixed reality", "knowledge",
    "A technology that blends real-world and digital objects so that they interact in real time, as in headsets such as Microsoft HoloLens.")

unsure("multi-programming-monitor-control-progra-98159c",
       "I do not recognise this term well enough to say what it is; it may be a historical operating-system component.")

new("natural-language-understanding-bd7bc3", "Natural language understanding", "method",
    "The part of natural language processing concerned with getting computers to grasp the meaning and intent of human language.",
    variants=["NLU"], rels=[("broader", "d168utcmjy")],
    note="Natural language understanding is a field of study within natural language processing, not a language.",
    reason="A subfield of NLP, not a language and not the same concept as NLP.")

new("neonatal-resuscitation-programs-b414d3", "Neonatal Resuscitation Program", "credential",
    "A training program developed by the American Academy of Pediatrics that teaches the steps of resuscitating newborns and is completed with a provider credential.",
    variants=["NRP"], cert=True)

new("nfpa-70e-23f786", "NFPA 70E", "standard",
    "A US National Fire Protection Association standard that sets requirements for electrical safety in the workplace.")

new("objective-c-progamming-language-194b1a", "Objective-C", "programming-language",
    "An object-oriented programming language that adds Smalltalk-style messaging to C, used mainly for Apple's macOS and iOS software.",
    variants=["Objective C", "Obj-C"], lang="programming")

unsure("obstacles-to-troop-movement-087ff6",
       "Sounds like a phrase from military terrain analysis, but I cannot tell what skill it would stand for.")

nas("outbreak-c3dc83", "A generic word for a disease outbreak, not a skill.")

new("passenger-endorsement-3b13cf", "Passenger endorsement", "credential",
    "A commercial driver's licence endorsement that allows the holder to drive vehicles carrying many passengers, such as buses.",
    cert=True)

nas("pedals-cb6a2a", "A generic word for a hardware part, not a skill.")

new("phoenician-language-54daed", "Phoenician", "human-language",
    "An extinct Northwest Semitic language of the Phoenicians, written in the Phoenician alphabet.",
    lang="spoken")

new("plumbing-drawing-f89dc0", "Plumbing drawing", "skill",
    "Preparing or reading technical drawings that show how pipes, fixtures and fittings are laid out in a building.")

new("production-support-0a56cd", "Production support", "skill",
    "In software and IT operations, keeping live systems running by monitoring them and investigating and fixing problems that users report.",
    verbs=["monitor", "troubleshoot"],
    reason="A common IT operations skill; in manufacturing the phrase can mean something different, so the definition says IT.")

nas("professional-services-24720d", "Names an industry or line of business, not a skill.")

new("prosystem-fx-engagement-tax-software-b594c1", "ProSystem fx Engagement", "tool",
    "Software from Wolters Kluwer CCH that accounting firms use to manage engagements and electronic workpapers.")

new("reading-gauges-9e8a05", "Reading gauges", "skill",
    "Reading the values shown on gauges and dials, such as pressure, temperature and level gauges, to monitor equipment.")

new("regulation-sho-47698f", "Regulation SHO", "regulation",
    "A US Securities and Exchange Commission regulation that governs short selling of equity securities.")

new("restricted-radiotelephone-operator-permi-996fd9", "Restricted Radiotelephone Operator Permit", "credential",
    "A permit issued by the US Federal Communications Commission that allows its holder to operate certain radiotelephone stations, such as aircraft radios.",
    cert=True)

new("saca-certified-industry-4-0-associate-ba-fcec76", "SACA Certified Industry 4.0 Associate Basic Operations", "credential",
    "A certification offered by SACA that attests to basic operating knowledge of Industry 4.0 smart manufacturing systems.",
    cert=True)

unsure("safety-trained-supervision-1b30a7",
       "Possibly the Safety Trained Supervisor (STS) credential, but I am not certain the tag means that and will not guess.")

new("screening-resumes-952e1b", "Screening resumes", "skill",
    "Reviewing candidates' resumes to decide who meets a role's requirements and should go forward in hiring.")

new("searchable-ornithological-research-archi-3893f2", "Searchable Ornithological Research Archive", "tool",
    "An online archive that gives free access to the full text of back issues of ornithological journals.",
    variants=["SORA"])

new("security-check-sc-54d5b8", "Security Check (SC)", "clearance",
    "A UK government security clearance level, granted after vetting, that allows regular access to secret material.",
    variants=["SC clearance"], cert=False,
    reason="A UK security clearance level; I treat it as a vetting status rather than a certificate, licence or permit.")

nas("short-films-c2297a", "Names a type of media product, not a skill.")

new("slovene-language-d03f87", "Slovene", "human-language",
    "A South Slavic language spoken mainly in Slovenia, where it is the official language.",
    variants=["Slovenian"], lang="spoken")

new("software-as-a-service-saas-a3bd38", "Software as a service", "knowledge",
    "A software delivery model in which a provider hosts an application and customers use it over the internet, usually by subscription.",
    variants=["SaaS"])

new("software-localization-1c4939", "Software localization", "skill",
    "Adapting software to the language, formats and cultural conventions of different regions.",
    variants=["software localisation"])

nas("solutions-focused-c9c4e8", "An adjective describing a disposition rather than a defined skill.")

new("spatial-temporal-reasoning-f4d81d", "Spatial-temporal reasoning", "ability",
    "The ability to reason about the positions of objects and how they change over time.")

nas("submit-button-3930f6", "A user-interface element, not a skill.")

nas("tabbed-ddfb29", "A generic adjective for a user-interface layout, not a skill.")

new("tl-9000-2279e7", "TL 9000", "standard",
    "A quality management system standard for the telecommunications industry that builds on ISO 9001.",
    variants=["TL9000"])

new("ultratax-22b61c", "UltraTax CS", "tool",
    "Thomson Reuters professional tax preparation software used by accounting firms.")

variant("ux-research-b80ca4", "enec00k7dc",
        "UX research and user research are used interchangeably for investigating user needs and behaviour to inform design.")

new("va-loans-7c13ae", "VA loans", "knowledge",
    "Home loans for US veterans, service members and eligible spouses that are guaranteed by the Department of Veterans Affairs.")

new("visme-software-16498e", "Visme", "tool",
    "An online tool for creating presentations, infographics and other visual content.")

new("windows-software-development-8d5da9", "Windows software development", "skill",
    "Building applications that run on the Microsoft Windows operating system.")

new("xbrl-c42369", "XBRL", "markup-language",
    "An XML-based standard markup language for tagging and exchanging business and financial reporting data.",
    variants=["eXtensible Business Reporting Language"], lang="other")

new("yahoo-messenger-9631b2", "Yahoo Messenger", "tool",
    "A discontinued instant messaging service and client from Yahoo, shut down in 2018.")

# ---- write, checking coverage against the request files ----
req_dir, out_dir = ROOT / "requests", ROOT / "responses"
out_dir.mkdir(exist_ok=True)
stems = sorted(p.stem for p in req_dir.glob("*.json"))
missing = [s for s in stems if s not in R]
extra = [s for s in R if s not in stems]
if missing or extra:
    print("missing", missing, "extra", extra)
    sys.exit(1)
for s in stems:
    (out_dir / f"{s}.json").write_text(json.dumps(R[s], indent=1, ensure_ascii=False) + "\n", "utf-8")
import collections
print(len(stems), collections.Counter(r["decision"] for r in R.values()))
