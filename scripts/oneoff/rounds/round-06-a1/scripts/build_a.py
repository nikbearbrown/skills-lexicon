import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from h import *

A = {}

A[0] = ("Framerjs", vo("cr8hoe2lk8", "Framerjs is the Framer.js library written without the dot."))
A[1] = ("Goal Oriented", vo("g32rgj6uc5", "The same trait as Goal-oriented, written without the hyphen."))
A[2] = ("Gruntjs", vo("kx6hq4bfym", "Gruntjs is the Grunt.js task runner written without the dot."))
A[3] = ("Gsuite", vo("xxggdc82ng", "G Suite is the former name of Google Workspace."))
A[4] = ("IAd (Apple'S Advertising Platform)", vo("zmnv3c76qo", "Same Apple advertising platform as iAd, with a descriptive gloss."))

A[5] = ("Image Segmentation", new(
    "Image segmentation", "method",
    "Dividing a digital image into regions, such as separating objects from the background, so that each part can be analysed."))

A[6] = ("Imaging", unsure("A bare word that could mean medical imaging, digital imaging, system imaging or scientific imaging."))

A[7] = ("Imaging Informatics", new(
    "Imaging informatics", "knowledge",
    "The field that applies information technology to medical images, covering how they are acquired, stored, shared and analysed.",
    rel=[("broader", "fn8par41c3")]))

A[8] = ("Imaging Technology", unsure("Too broad to define: it spans medical, photographic and scientific imaging."))
A[9] = ("Immigration", unsure("A bare topic word that could mean immigration law, visa processing or the social topic."))
A[10] = ("Immigration Issues", ns("A generic topic phrase, not a skill."))

A[11] = ("Immunization", new(
    "Immunization", "knowledge",
    "The use of vaccines to make people resistant to specific infectious diseases, including which vaccines are given, when and to whom."))

A[12] = ("Immunohaematology", new(
    "Immunohaematology", "knowledge",
    "The branch of laboratory medicine that studies blood-group antigens and antibodies, used for blood typing and for matching blood before a transfusion.",
    variants=["Immunohematology"]))

A[13] = ("Immutable.js", new(
    "Immutable.js", "library",
    "A JavaScript library from Facebook that provides persistent immutable data structures such as List, Map and Set.",
    variants=["ImmutableJS"]))

_impact = dict(
    kind="framework",
    definition="A JavaScript game engine for making 2D games that run in the browser on the HTML5 canvas.",
    variants=["ImpactJS"])
A[14] = ("Impact.js", new("Impact.js", _impact["kind"], _impact["definition"], variants=_impact["variants"]))
A[15] = ("Impactjs", new("Impact.js", _impact["kind"], _impact["definition"], variants=_impact["variants"]))

A[16] = ("Impulse Control Disorder", ns("A medical condition, not a skill."))

A[17] = ("In-Memory Database System", new(
    "In-memory database", "knowledge",
    "A database management system that keeps its data mainly in a computer's main memory instead of on disk, to give faster access.",
    variants=["Main memory database"],
    rel=[("broader", "sai8akfwpi")]))

A[18] = ("Inbound Logistics", new(
    "Inbound logistics", "knowledge",
    "The part of logistics that brings materials, parts and goods from suppliers into a business, including purchasing, transport, receiving and storage."))

A[19] = ("Incentive Spirometry", new(
    "Incentive spirometry", "method",
    "A breathing exercise in which a patient inhales deeply through a handheld device that shows how much air is drawn in, to keep the lungs expanded and help prevent complications such as pneumonia after surgery."))

A[20] = ("Incident Report", new(
    "Incident reporting", "skill",
    "Writing a factual, timely record of an accident, injury, security event or other incident, including what happened, who was involved and what was done."))

A[21] = ("Incurred But Not Reported", new(
    "Incurred but not reported", "knowledge",
    "In insurance, the estimated cost of claims for events that have already happened but have not yet been reported to or settled by the insurer.",
    variants=["IBNR"]))

A[22] = ("Indemnity", ns("A legal and insurance term for compensation or protection against loss, not a skill."))

A[23] = ("Indentation Hardness", new(
    "Indentation hardness", "knowledge",
    "A measure of how well a material resists being permanently dented by a hard point pressed into it, found with tests such as Brinell, Vickers and Rockwell."))

A[24] = ("Independent Films", ns("A category of films, not a skill."))
A[25] = ("Independent Pharmacy", ns("A type of workplace, not a skill."))
A[26] = ("Independent Studies", ns("A course format, not a skill."))
A[27] = ("Independent Test Organization (Quality)", ns("A type of organisation, not a skill."))

A[28] = ("Indexeddb", new(
    "IndexedDB", "tool",
    "A database built into web browsers, used from JavaScript to store large amounts of structured data on the user's device.",
    verbs=["use"]))

A[29] = ("Indicators", ns("A generic word, not a skill."))

A[30] = ("Individual Life Insurance", new(
    "Individual life insurance", "knowledge",
    "Life insurance bought by one person for themselves, rather than as group cover through an employer, that pays a benefit to named beneficiaries on death.",
    rel=[("related", "yjhzrcmw7v")]))

A[31] = ("Individual Training And Readiness System (Army Database)", unsure("I do not know this US Army system well enough to define it."))

A[32] = ("Individualized Education Programs (IEP)", new(
    "Individualized Education Program", "knowledge",
    "In the United States, the written plan required by special-education law that sets out the learning goals and support for a student with a disability.",
    variants=["IEP", "Individualized Education Plan"]))

A[33] = ("Individualized Family Service Plans (IFSP)", new(
    "Individualized Family Service Plan", "knowledge",
    "In the United States, the written plan for an infant or toddler with a developmental delay that sets out early-intervention services for the child and family.",
    variants=["IFSP"]))

A[34] = ("Industrial Internet of Things (IIoT)", new(
    "Industrial Internet of Things", "knowledge",
    "Internet-connected sensors, machines and control systems in industry that collect and share data to monitor and improve operations.",
    variants=["IIoT", "Industrial IoT"]))

A[35] = ("Industrial Statistics", new(
    "Industrial statistics", "knowledge",
    "The use of statistical methods in industry, such as quality control, design of experiments and reliability analysis, to improve production and products.",
    rel=[("broader", "ww4glmysl2"), ("related", "mcd36zu7px")]))

A[36] = ("Industrial Wastewater", unsure("Names a substance rather than a skill or field; unclear if it means treatment, regulation or something else."))
A[37] = ("Industrialisation", ns("A historical and economic process, not a skill."))

A[38] = ("Infant Development", new(
    "Infant development", "knowledge",
    "How babies grow and change in their first years, including physical, thinking, language and social development."))

A[39] = ("Infection Control Certification", unsure("Generic: it could mean the CBIC Certification in Infection Control or any training certificate, so no single credential can be named."))

A[40] = ("Influencing Skills", new(
    "Influencing", "skill",
    "Persuading other people to adopt an idea or take action without relying on formal authority."))

A[41] = ("Influxdb", new(
    "InfluxDB", "tool",
    "An open-source time-series database from InfluxData for storing and querying timestamped data such as metrics and events.",
    verbs=["query"]))

A[42] = ("Infoblox IPAM", new(
    "Infoblox IPAM", "tool",
    "IP address management software from Infoblox that tracks and administers an organisation's IP address space along with its DNS and DHCP records."))

A[43] = ("Infographics (Illustration)", new(
    "Infographics", "skill",
    "Designing infographics, which present information or data visually through illustration, charts and short text."))

A[44] = ("Inform", unsure("A bare word that could be the Inform interactive-fiction language or the ordinary verb."))

A[45] = ("Information Advice And Guidance", new(
    "Information, advice and guidance", "skill",
    "In the United Kingdom, helping people choose learning and career options by giving them impartial information, advice and guidance."))

A[46] = ("Information Advice And Guidance (IAG) Qualification", new(
    "Information, advice and guidance qualification", "credential",
    "A UK vocational qualification showing competence in giving people information, advice and guidance on learning and work, offered by several awarding organisations.",
    cert=True, scope="many-issuers"))

A[47] = ("Information Engineering", unsure("Could mean a software and data-modelling methodology, an electronics-and-computing degree, or other things."))

A[48] = ("Information Hiding", new(
    "Information hiding", "method",
    "A software design principle in which a module keeps its internal details private behind a stable interface, so changes inside it do not affect the rest of the program."))

A[49] = ("Information Industry", ns("An industry, not a skill."))

write_all(A)
