"""Scratch script: builds work/responses/*.json from the answers below. Not part of the dictionary."""
import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
GK = "general-knowledge"
R = {}


def variant(stem, target, reason):
    R[stem] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


def no(stem, reason):
    R[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    R[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def new(stem, name, kind, definition, reason, variants=(), relations=(), verbs=(), cert=False, scope=None,
        lang=None, note=""):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    e["annotation_note"] = note
    R[stem] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}


# ---------------------------------------------------------------- variants of existing entries
variant("breeze-js-javascript-library-f1dcb2", "ip67ypemwd",
        "Same JavaScript data library as Breeze.js; the bracketed text is a tagging artefact.")
variant("certified-documentation-integrity-practi-9fce57", "winu2cliaj",
        "CDIP is the abbreviation of the same AHIMA certification.")
variant("certified-medical-assistant-cma-2e0bd6", "pj8vtw9tl2",
        "CMA is the usual abbreviation of the AAMA Certified Medical Assistant credential.")
variant("certified-patient-care-technician-associ-3e168e", "f881v6vufj",
        "The slash-joined name is the same patient care technician/associate certification with extra alternative titles.")

# ---------------------------------------------------------------- new entries
new("choreography-4aaafc", "Choreography", "skill",
    "Designing and arranging sequences of movement, most often for dance, theatre and film performances.",
    "A developed creative skill, known from general knowledge.")

new("chromatography-softwares-66cafa", "Chromatography software", "tool",
    "Software that controls chromatography instruments and collects, processes and reports the data they produce.",
    "A category of laboratory software, like the existing Accounting software entry.")

new("chronometer-568b07", "Chronometer", "tool",
    "A precise timekeeping instrument, originally built to keep accurate time at sea so that longitude could be found.",
    "An instrument rather than a skill; kept as a tool.")

no("chrysler-lh-platform-e32c96",
   "A car manufacturer's vehicle platform (a product line), not a skill, tool or method.")

new("circular-economy-a3608b", "Circular economy", "knowledge",
    "An economic approach that keeps products and materials in use as long as possible through reuse, repair, remanufacturing and recycling, so that waste is designed out.",
    "A recognised field of knowledge.")

new("circulatory-systems-b2688f", "Circulatory system", "knowledge",
    "The organ system, made up of the heart, blood vessels and blood, that carries oxygen, nutrients and waste around the body.",
    "Anatomy and physiology knowledge.")

new("cisco-certified-network-associate-securi-99de06", "CCNA Security", "credential",
    "A Cisco associate-level certification for network engineers who secure Cisco network devices and infrastructure.",
    "A Cisco certification, named like the existing CCNP Security entry.",
    variants=["Cisco Certified Network Associate Security"],
    relations=[("related", "aksp1d11ue")],
    cert=True, scope="single-issuer")

new("cisco-certified-support-technician-ccst-ca9cf8", "Cisco Certified Support Technician", "credential",
    "An entry-level Cisco certification for people starting out in IT support, networking or cybersecurity roles.",
    "A Cisco certification; the short form CCST is left out because the dictionary already gives it to the ISA control systems certification.",
    cert=True, scope="single-issuer")

new("cisco-intersight-c8c470", "Cisco Intersight", "platform",
    "Cisco's cloud-based platform for managing and monitoring Cisco UCS servers and other data-centre infrastructure from one place.",
    "A named Cisco product.")

no("cisco-softwares-d89048",
   "A vendor name plus a generic word, an umbrella over many unrelated products rather than one tool.")

new("cisco-ucs-director-d8f77e", "Cisco UCS Director", "platform",
    "Cisco software for automating the provisioning and management of compute, network and storage resources in data centres built on Cisco UCS.",
    "A named Cisco product.")

new("citrix-certified-administrator-21f1d5", "Citrix Certified Administrator", "credential",
    "A Citrix certification showing that a person can administer Citrix products such as application and desktop virtualisation.",
    "A Citrix certification awarded by Citrix.",
    cert=True, scope="single-issuer")

for _stem, _term in (("citrix-certified-integration-architectur-49cf8d", "Integration Architecture"),
                     ("citrix-certified-integratrion-architectu-d58adb", "Integratrion Architecture")):
    new(_stem, "Citrix Certified Integration Architect", "credential",
        "A Citrix certification for architects who design integrated solutions built on Citrix products.",
        "The tag is a variant spelling of the Citrix integration architect certification.",
        cert=True, scope="single-issuer")

unsure("citrix-rallydev-44ce38",
       "RallyDev is Rally's agile project-management tool, but Citrix is not its vendor, so the tag looks mis-joined.")

new("citrix-sharefile-91ef0d", "ShareFile", "platform",
    "A cloud service for storing, sharing and collaborating on business files securely, originally from Citrix.",
    "A named file-sharing product; the Citrix prefix is added as a variant.")

no("civil-designer-b2a454", "A job title; none of the nearest entries is the same concept.")

new("civil-engineering-design-28e7ea", "Civil engineering design", "skill",
    "Planning and specifying infrastructure and structures such as roads, bridges, drainage and water systems so that they meet engineering requirements.",
    "A core civil engineering skill.")

no("civil-war-ab9460", "A historical event whose meaning depends on the country, not a skill.")

new("claim-processing-5ab619", "Claim processing", "skill",
    "Receiving, checking and deciding insurance or benefit claims, and then paying or denying them.",
    "A common insurance and benefits task.",
    relations=[("related", "oq06rmk4iu")])

new("claims-modeling-e46649", "Claims modeling", "skill",
    "Building statistical models of how often insurance claims occur and how large they are, to price risk and set reserves.",
    "Insurance analytics skill; the meaning is taken from insurance usage.")

new("clarizen-54d44d", "Clarizen", "platform",
    "A cloud-based work and project management platform for planning projects, tracking tasks and managing resources.",
    "A named software product.")

new("clash-detection-075e8f", "Clash detection", "method",
    "Checking a combined 3D model of a building or plant for places where parts from different disciplines, such as pipes and beams, occupy the same space.",
    "A building information modelling practice.")

no("class-members-26bc7e",
   "A generic phrase with no single skill meaning (class action members, or fields and methods of a programming class).")

new("classification-and-regression-tree-cart-7d5843", "Classification and Regression Tree", "method",
    "A decision-tree method that repeatedly splits data into groups to predict either a category (classification) or a number (regression).",
    "A well-known machine learning method.")

new("clean-air-act-20b65c", "Clean Air Act", "standard",
    "The United States federal law that limits air pollution and gives the Environmental Protection Agency power to set and enforce air quality and emission standards.",
    "A regulation.")

new("clean-water-act-460d81", "Clean Water Act", "standard",
    "The United States federal law that regulates the discharge of pollutants into US waters and sets water quality standards for surface waters.",
    "A regulation.")

no("cleaning-agent-78ad9a", "A generic substance, not a skill, tool or method.")

new("cleardb-02701a", "ClearDB", "platform",
    "A managed cloud database service that provides replicated MySQL databases, commonly used as an add-on on platforms such as Heroku.",
    "A named database service.")

no("clickable-d84530", "A generic interface word, not a skill.")

new("client-access-licensing-2ec0a5", "Client access license", "knowledge",
    "A licensing model used by server software, notably from Microsoft, in which each user or device needs a licence to connect to the server.",
    "Software licensing knowledge.")

new("client-confidentiality-e47fae", "Client confidentiality", "skill",
    "Keeping information that clients share private and disclosing it only with their consent or as the law requires.",
    "A professional practice asked for in many roles.",
    verbs=["maintain"])

unsure("client-specific-sales-8588c3",
       "Unclear whether it means account-based selling or simply selling to one named client.")

new("climate-variability-and-change-b5c719", "Climate variability and change", "knowledge",
    "The study of natural variation in climate over time and of long-term shifts in it, with their causes and impacts.",
    "A field of knowledge.")

new("clinical-data-repository-f17b68", "Clinical data repository", "tool",
    "A database that gathers patient data from several clinical systems in one place so that it can be viewed, reported on and reused.",
    "A category of health IT system.")

new("clinical-documentation-improvement-7fca62", "Clinical documentation improvement", "skill",
    "Reviewing and clarifying patient records so that they accurately and completely describe a patient's condition and care, for coding, billing and quality reporting.",
    "A health information management practice; the credential for it is a separate entry.",
    relations=[("related", "winu2cliaj")])

new("clinical-documentation-integrity-cdi-8fef44", "Clinical documentation improvement", "skill",
    "Reviewing and clarifying patient records so that they accurately and completely describe a patient's condition and care, for coding, billing and quality reporting.",
    "The same practice as clinical documentation improvement; 'integrity' is the newer name.",
    relations=[("related", "winu2cliaj")],
    note="CDI names the practice, not a credential; the credential is the Certified Documentation Integrity Practitioner.")

new("clinical-informatics-8aaa40", "Clinical informatics", "knowledge",
    "The use of information science and computing to improve patient care and clinical workflows in health-care settings.",
    "A field within biomedical informatics.",
    relations=[("broader", "fn8par41c3")])

new("clinical-laboratory-phlebotomy-89452e", "Clinical laboratory phlebotomy", "skill",
    "Drawing blood from patients, in a clinical laboratory or collection site, for laboratory testing.",
    "A hands-on clinical skill.")

new("clinical-medical-ethics-0011fc", "Clinical medical ethics", "knowledge",
    "Applying ethical principles to decisions in patient care, such as consent, confidentiality and end-of-life treatment.",
    "A field of knowledge.")

no("clinical-nurse-specialists-cns-2b05e5",
   "An advanced-practice nursing job title, not a skill; the specific certification already has its own entry.")

new("clinical-pastoral-education-94428a", "Clinical pastoral education", "knowledge",
    "A programme of supervised, hands-on training in spiritual care for chaplains and ministers, accredited in the United States by the Association for Clinical Pastoral Education.",
    "A training programme rather than a credential; the classification is a judgement a person should check.",
    note="CPE is an accredited training programme measured in units, not a credential awarded by an official body; board certification for chaplains is separate.")

no("clinical-team-lead-50c66e", "A job title.")

unsure("clinical-works-88b8da",
       "Probably eClinicalWorks electronic health record software, but the name is ambiguous and I am not sure.")

no("clip-arts-80fc6c", "A generic type of ready-made image, not a skill or tool.")
no("clipboard-5efe0c", "A generic object or interface element, not a skill.")

new("closed-circuit-television-camera-ce75cc", "Closed-circuit television camera", "tool",
    "A video camera whose signal goes to a limited set of monitors or recorders rather than being broadcast openly, typically used for security and surveillance.",
    "A piece of equipment named in postings.",
    variants=["CCTV camera"])

new("cloud-access-security-broker-tools-casbs-9ddf21", "Cloud access security broker", "tool",
    "Security software or a service placed between an organisation's users and its cloud services to enforce security policies such as visibility, data protection and threat detection.",
    "A recognised category of security tool.",
    variants=["CASB"])

new("cloud-computing-security-94a5a9", "Cloud computing security", "knowledge",
    "Protecting the data, applications and infrastructure that run in cloud computing environments.",
    "A recognised security field.",
    relations=[("related", "lpsnz8mgp5")])

new("cloud-native-development-7eb471", "Cloud-native development", "skill",
    "Building applications designed to run in the cloud, typically as containerised microservices managed by automated platforms such as Kubernetes.",
    "A recognised development approach.")

new("cloud9-d5fdf6", "AWS Cloud9", "tool",
    "An Amazon Web Services cloud-based integrated development environment for writing, running and debugging code in a web browser.",
    "Cloud9 is the Amazon-owned cloud IDE.")

new("cloudwatch-0a7756", "Amazon CloudWatch", "tool",
    "An Amazon Web Services service that collects metrics, logs and events from AWS resources and applications for monitoring, alarms and troubleshooting.",
    "Cloudwatch is the AWS monitoring service.",
    variants=["AWS CloudWatch"],
    relations=[("related", "kba5p9by94")])

unsure("co-counselling-616a0f",
       "Could mean peer co-counselling (taking turns as counsellor) or two counsellors working together, and I cannot tell which.")

unsure("coaching-and-athletic-training-bc5f8e",
       "Joins two separate concepts, sports coaching and athletic training, and athletic training already has its own entry.")

new("coastal-engineering-0f8ad9", "Coastal engineering", "knowledge",
    "The branch of civil engineering that designs and manages structures and measures at the shoreline, such as sea walls, harbours and erosion protection.",
    "An engineering field.")

new("cocoa-touch-f0b910", "Cocoa Touch", "framework",
    "Apple's set of application frameworks, including UIKit, for building apps for iPhone, iPad and other iOS-family devices.",
    "A named Apple framework layer.")

new("cocoapods-d10635", "CocoaPods", "tool",
    "A dependency manager for Swift and Objective-C projects that downloads and links third-party libraries.",
    "A named developer tool.")

new("cocoonjs-b3a6a9", "CocoonJS", "tool",
    "A tool from Ludei that packages HTML5 and JavaScript apps and games as native mobile apps with accelerated canvas rendering.",
    "A named mobile development tool; the description is from memory and should be checked.")

unsure("coder-certification-e8b8de",
       "Too generic: it could mean a medical coding certification from AAPC or AHIMA, or something else.")

unsure("cognition-processing-fd4bcb",
       "Unclear whether it means cognitive processing in psychology, Cognitive Processing Therapy, or something else.")

new("cognitive-computing-e4b89d", "Cognitive computing", "knowledge",
    "Computing systems that imitate aspects of human thinking, such as learning, reasoning and understanding language, using methods like machine learning and natural language processing.",
    "A recognised field of knowledge.")

new("cognitive-load-cc5292", "Cognitive load", "knowledge",
    "The amount of mental effort being used in working memory at a given time, a concept used in teaching and interface design to avoid overloading people.",
    "A concept from educational and cognitive psychology.")

for _stem in ("collaborative-planning-forecasting-and-r-2cef24",
              "collaborative-planning-forecasting-and-r-63462c",
              "collaborative-planning-forecasting-sands-df6352"):
    new(_stem, "Collaborative Planning, Forecasting and Replenishment", "method",
        "A supply-chain practice in which trading partners jointly plan, forecast and replenish stock using shared data.",
        "A recognised supply-chain method; this tag is one of several spellings of it.",
        variants=["CPFR"])

no("collaborative-research-network-121941",
   "A name for a kind of organisation or programme, not a skill.")

new("collaborative-skills-ed9b76", "Collaboration", "skill",
    "Working jointly with others, sharing information and effort, to reach a shared goal.",
    "A general interpersonal skill.")

new("collaborative-softwares-b76c04", "Collaboration software", "tool",
    "Software that lets groups work together on shared tasks and documents, for example through shared files, chat and project boards.",
    "A software category, like the existing Accounting software entry.")

no("color-blindness-dd069b", "A vision condition, not a skill.")

new("color-matching-41c13e", "Color matching", "skill",
    "Choosing or adjusting colours so that a product or print matches a reference colour, as in paint, printing, textiles and cosmetics.",
    "A practical colour skill.",
    variants=["Colour matching"])

new("color-rendering-index-d7986e", "Color rendering index", "knowledge",
    "A scale up to 100 that rates how faithfully a light source shows the colours of objects compared with a reference light.",
    "A lighting measurement concept.")

unsure("coloring-97f703",
       "Could mean hair colouring, colouring in illustration, or something else, and the tag gives no context.")

new("colors-materials-and-finish-cmf-design-2c78f2", "Color, material and finish design", "skill",
    "Choosing and specifying the colours, materials and surface finishes of a product as part of industrial design.",
    "A recognised industrial design specialism.",
    variants=["CMF design"])

no("comat-technologies-d44f6c", "A company name.")

for _stem in ("combat-life-saver-3e8b17", "combat-lifesaving-5a3fae"):
    new(_stem, "Combat Lifesaver", "credential",
        "A US Army course and designation in advanced first aid for battlefield injuries, given to soldiers who are not medics.",
        "The Army combat lifesaver course and designation; the two tags are spellings of one concept.",
        cert=True, scope="single-issuer")

new("combine-harvester-f56b7e", "Combine harvester", "tool",
    "A farm machine that cuts, threshes and cleans grain crops in a single pass.",
    "Agricultural equipment.")

no("commercial-aviation-7933ae", "An industry sector, not a skill.")
no("commercial-construction-00b2e0", "An industry sector, not a skill.")

new("commercial-loan-documentation-338d78", "Commercial loan documentation", "skill",
    "Preparing and reviewing the agreements and security documents that set out the terms of a commercial loan.",
    "A banking and legal task.")

new("commercial-off-the-shelf-bc4973", "Commercial off-the-shelf", "knowledge",
    "Ready-made hardware or software products bought from a supplier and used as they are, rather than built specially for the buyer.",
    "A procurement and engineering concept.",
    variants=["COTS", "Commercial off the shelf"])

new("commissioning-qualification-validation-c-b76aa6", "Commissioning, qualification and validation", "method",
    "Engineering activities, common in pharmaceutical manufacturing, that verify and document that facilities, equipment and systems are installed correctly and perform as intended.",
    "A regulated-industry engineering method.",
    variants=["CQV"])

new("common-criteria-cd89ce", "Common Criteria", "standard",
    "The international standard, ISO/IEC 15408, for evaluating the security of IT products.",
    "A published standard.",
    variants=["ISO/IEC 15408"])

new("common-language-specification-858a18", "Common Language Specification", "standard",
    "A set of rules in Microsoft's .NET Framework that languages must follow so that code written in one .NET language can be used from another.",
    "A specification for .NET language interoperability, not a language itself.",
    note="It is a rule set for .NET language interoperability, not a language.")

new("commonjs-dc827f", "CommonJS", "standard",
    "A specification for JavaScript modules and other server-side interfaces, best known for the require and module.exports module format used by Node.js.",
    "A named specification.")

new("commons-based-peer-production-d38c1f", "Commons-based peer production", "knowledge",
    "A way of producing goods in which many people collaborate voluntarily without central ownership or markets, as in open-source software and Wikipedia.",
    "A concept from economics and sociology.")

new("communication-ade0d5", "Communication", "skill",
    "Conveying information and ideas clearly to others through speaking, writing and listening.",
    "A general workplace skill.")

unsure("communication-certificates-65429f",
       "Too generic: it could mean a university communication certificate or a specific certification.")

new("communication-softwares-353878", "Communication software", "tool",
    "Software for exchanging messages and conversations between people, such as email, chat, voice calls and video conferencing.",
    "A software category, like the existing Accounting software entry.")

new("communication-theories-78221a", "Communication theories", "knowledge",
    "Theories that explain how people and groups create, send and interpret messages.",
    "A field of knowledge.")

unsure("communications-690476",
       "Could mean communication skills, a communications department, public relations or telecommunications.")

new("community-advocacy-4fd6bb", "Community advocacy", "skill",
    "Speaking up for a community's needs and rights and helping its members influence the decisions that affect them.",
    "A community-work skill.")

new("community-nutrition-690dca", "Community nutrition", "knowledge",
    "The part of nutrition concerned with improving the diet and health of groups and populations through education, programmes and policy.",
    "A public-health nutrition field.")

new("community-resilience-6b036c", "Community resilience", "knowledge",
    "The capacity of a community to prepare for, withstand and recover from disasters and other disruptions.",
    "A concept from emergency management and public health.")

new("comptia-a-ce-332be8", "CompTIA A+", "credential",
    "A CompTIA entry-level certification showing skills in supporting and troubleshooting computer hardware, operating systems and networks.",
    "The CE suffix marks the continuing-education renewal of the same CompTIA A+ certification.",
    variants=["CompTIA A+ certification"],
    relations=[("related", "ffswfagi3s")],
    cert=True, scope="single-issuer")

new("costar-real-estate-manager-saas-5bd0fd", "CoStar Real Estate Manager", "platform",
    "A CoStar Group cloud software product for managing leases, property portfolios and real-estate costs.",
    "A named software product; the SAAS suffix is added as a variant.")


def main():
    req = {p.stem for p in (WORK / "requests").glob("*.json")}
    got = set(R)
    if req != got:
        print("missing:", sorted(req - got))
        print("extra:", sorted(got - req))
        sys.exit(1)
    out = WORK / "responses"
    out.mkdir(exist_ok=True)
    for stem, resp in R.items():
        (out / f"{stem}.json").write_text(json.dumps(resp, indent=1, ensure_ascii=False) + "\n", "utf-8")
    from collections import Counter
    print(Counter(r["decision"] for r in R.values()), len(R))


main()
