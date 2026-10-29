"""Scratch script: builds work/responses/*.json answers for the legacy-tag requests."""
import json
import os
import sys

WORK = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(WORK, "requests")
OUT = os.path.join(WORK, "responses")
GK = "general-knowledge"

A = {}  # request file stem -> response dict


def variant_of(stem, target, reason):
    A[stem] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


def not_skill(stem, reason):
    A[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    A[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def new(stem, name, kind, definition, reason, variants=(), relations=(), cert=False, scope=None, lang=None):
    e = {
        "preferred_name": name,
        "kind": kind,
        "definition": definition,
        "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": "",
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    A[stem] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}


def human_language(stem, name, definition, variants=()):
    new(stem, name, "human-language", definition, "A human language.", variants=variants, lang="human")


# ---- variants -------------------------------------------------------------------------------
variant_of("american-board-of-optometry-ecb3fd", "f07mdjv1v0",
           "The body's name is how the existing entry's certification is already listed, as with the other American Board entries.")
variant_of("antivirus-softwares-2cd20f", "cs0zix8jdm", "Plural form of the same category of software.")
variant_of("application-integreation-architecture-9a8515", "dy5sokpl37",
           "A misspelling of Application Integration Architecture, which the existing entry already lists as a name for Oracle AIA.")
variant_of("associates-degree-in-nursing-996edc", "gg2k98nhyp", "Same degree, written with a plural possessive.")
variant_of("babylonjs-f0000b", "n225fen24i", "Babylon.js written without the dot.")

# ---- new entries ----------------------------------------------------------------------------
new("barcode-systems-46a33b", "Barcode systems", "knowledge",
    "Technology that encodes data as patterns of bars or modules and reads it with scanners to identify products, items or locations.",
    "A body of technology knowledge.")
new("bariatric-surgeries-66398a", "Bariatric surgery", "knowledge",
    "Operations such as gastric bypass and sleeve gastrectomy that change the stomach or digestive tract to treat severe obesity.",
    "A surgical field.", variants=["Bariatric surgeries"])
new("baseline-personnel-security-standard-bps-dc1ce2", "Baseline Personnel Security Standard", "standard",
    "The UK government's minimum set of pre-employment checks, covering identity, right to work, employment history and unspent criminal convictions.",
    "A named UK government personnel security standard.", variants=["BPSS"])
new("basex-5e3f4c", "BaseX", "tool",
    "A lightweight open-source XML database and XQuery processor.", "A named XML database product.")
new("basic-automotive-maintenance-certificate-d37187", "Basic automotive maintenance certificate", "credential",
    "A short vocational certificate, usually from a college or training school, showing completion of introductory training in routine vehicle servicing.",
    "A certificate that many schools award.", cert=True, scope="many-issuers")
new("basic-block-908f2a", "Basic block", "knowledge",
    "A straight-line sequence of program instructions with one entry point and one exit and no branching in between, used in compiler analysis and optimisation.",
    "A compiler-theory concept.")
new("basic-life-support-a36521", "Basic Life Support", "credential",
    "A certification in emergency care for cardiac arrest, choking and breathing emergencies, including CPR and use of an AED, for healthcare providers and other rescuers.",
    "A widely required life-saving certification.", variants=["Basic Life Support certification"],
    relations=[("related", "uqnp4t4487")], cert=True, scope="many-issuers")
new("basic-life-support-bls-instructor-certif-970701", "Basic Life Support instructor certification", "credential",
    "A certification, issued by training organisations such as the American Heart Association and the American Red Cross, that qualifies a person to teach and certify others in Basic Life Support.",
    "An instructor credential distinct from the provider-level Basic Life Support certification.", cert=True, scope="many-issuers")
human_language("bassa-language-a5ff97", "Bassa",
               "A Kru language of Liberia spoken by the Bassa people, not to be confused with the Bantu language Basaa of Cameroon.")
human_language("batak-language-d02a53", "Batak",
               "A group of related Austronesian languages spoken by the Batak peoples of northern Sumatra, Indonesia.")
new("batman-js-7fcc80", "Batman.js", "framework",
    "A JavaScript framework, created at Shopify, for building single-page web applications.", "A named JavaScript framework.")
new("baton-law-enforcement-8c9493", "Police baton", "tool",
    "A short club or telescoping rod carried by police and security officers for defensive control.",
    "A defensive tool used in law enforcement.")
new("battery-technology-battery-f5612a", "Battery technology", "knowledge",
    "The science and engineering of electrochemical cells that store and deliver electrical energy, including their chemistries, design, charging and management.",
    "A technical field.")
new("battle-management-military-terminology-425381", "Battle management", "skill",
    "Directing and coordinating military forces and assets during an operation, using real-time information about the battle.",
    "A military command-and-control capacity.")
new("bed-mobility-72c62d", "Bed mobility", "skill",
    "Helping a patient roll, shift position and move between lying and sitting in bed, and judging how much help they need.",
    "A patient-care skill in nursing and therapy.")
new("behavior-change-communication-72da4f", "Behavior change communication", "method",
    "A public-health approach that uses targeted communication to encourage individuals and communities to adopt healthier behaviours.",
    "A named public-health communication approach.", variants=["Behaviour change communication"])
new("behavioural-science-385dd2", "Behavioural science", "knowledge",
    "The study of human and animal behaviour through observation and experiment, drawing on fields such as psychology, sociology and economics.",
    "A field of study.", variants=["Behavioral science"])
human_language("bemba-language-bemba-380e2c", "Bemba",
               "A Bantu language spoken mainly in northern Zambia and nearby parts of the Democratic Republic of the Congo.")
new("benchmarking-project-management-e686a7", "Project benchmarking", "method",
    "Comparing a project's performance, processes or practices with those of similar projects or recognised good practice to find ways to improve.",
    "A project-management technique.", relations=[("broader", "z83cabeb9c")])
new("benefits-realisation-management-90f9f7", "Benefits realisation management", "method",
    "A discipline of identifying, planning, tracking and delivering the benefits that a project or programme is meant to produce.",
    "A named change-management and programme-management approach.", variants=["Benefits realization management"])
human_language("benga-language-ab98a6", "Benga",
               "A Bantu language spoken along the coast of Equatorial Guinea and Gabon.")
human_language("bengali-language-1f4086", "Bengali",
               "An Indo-Aryan language spoken mainly in Bangladesh and the Indian state of West Bengal.", variants=["Bangla"])
human_language("berber-language-05c2c4", "Berber",
               "A family of related Afro-Asiatic languages spoken across North Africa, also known as the Amazigh languages.",
               variants=["Amazigh"])
new("bereavement-care-8a0f69", "Bereavement care", "skill",
    "Supporting people who are grieving after the death of someone close to them.", "A care and counselling skill.")
new("berkeley-data-analytics-stack-bdas-49d75d", "Berkeley Data Analytics Stack", "platform",
    "The open-source big-data software stack developed at UC Berkeley's AMPLab, whose components include Apache Spark and Apache Mesos.",
    "A named software stack.", variants=["BDAS"])
new("bidirectional-streams-over-synchronous-h-6cf7c3", "Bidirectional-streams Over Synchronous HTTP", "standard",
    "An XMPP extension protocol (XEP-0124) that emulates a long-lived two-way connection between client and server using ordinary HTTP request and response pairs.",
    "A named protocol specification.")
new("big-o-1110ad", "Big O notation", "knowledge",
    "Notation that describes how an algorithm's running time or memory use grows with the size of its input, giving an upper bound.",
    "Big O is the common short name for Big O notation.", variants=["Big-O notation"])
new("bigfix-endpoint-management-software-860270", "BigFix", "platform",
    "An endpoint management platform, now sold by HCL Software, for patching, configuring and securing computers across a network.",
    "A named endpoint management product.", variants=["HCL BigFix", "IBM BigFix"])
new("bill-of-materials-b26459", "Bill of materials", "knowledge",
    "A structured list of the raw materials, parts, assemblies and quantities needed to make a product.",
    "A core manufacturing concept.", variants=["Bills of materials"])
new("binary-ninja-reverse-engineering-softwar-9723ea", "Binary Ninja", "tool",
    "A reverse-engineering platform from Vector 35 for disassembling, decompiling and analysing compiled programs.",
    "A named reverse-engineering product.")
new("binary-options-c595eb", "Binary options", "knowledge",
    "Financial options that pay a fixed amount or nothing, depending on whether an underlying asset meets a set condition at expiry.",
    "A financial instrument.")
new("biochemical-genetics-054677", "Biochemical genetics", "knowledge",
    "The study of how genes control biochemical processes in the body, including inherited metabolic disorders.",
    "A field of genetics.")
new("bioconductor-61e11d", "Bioconductor", "platform",
    "An open-source project that distributes R packages for analysing genomic and other biological data.",
    "A named bioinformatics software project.")
new("biological-applications-of-bifurcation-t-ade669", "Biological applications of bifurcation theory", "knowledge",
    "The use of bifurcation theory, which studies how the behaviour of a dynamical system changes qualitatively as its parameters vary, to model biological systems.",
    "A specialised area of mathematical biology.")
new("biomedical-auditor-certification-30c2f2", "ASQ Certified Biomedical Auditor", "credential",
    "A certification from ASQ for auditors who assess quality systems and regulatory compliance in the biomedical and medical-device industries.",
    "A named ASQ credential.", variants=["Certified Biomedical Auditor"], cert=True, scope="single-issuer")
new("biomedical-informatics-38f23d", "Biomedical informatics", "knowledge",
    "The field that applies information science and computing to the collection, storage and analysis of biological and medical data.",
    "A field of study.")
new("biomolecular-engineering-6bed3c", "Biomolecular engineering", "knowledge",
    "Engineering that designs and modifies biological molecules such as proteins and nucleic acids for use in medicine, industry and research.",
    "A field of engineering.")
new("biopesticide-379aff", "Biopesticide", "knowledge",
    "Pest-control agents made from natural materials such as microbes, plants and minerals.",
    "A class of agricultural products that people need knowledge of.")
new("biopython-7c6de9", "Biopython", "library",
    "An open-source Python library of tools for computational biology and bioinformatics, such as reading sequence files and working with protein structures.",
    "A named Python library.", relations=[("related", "pk7cebmtg6")])
new("biosensors-8503da", "Biosensors", "knowledge",
    "Devices that pair a biological recognition element, such as an enzyme or antibody, with a transducer to detect a specific substance.",
    "A technical field.", variants=["Biosensor"])
new("bioterrorism-preparedness-and-response-f4dbd6", "Bioterrorism preparedness and response", "knowledge",
    "Planning for, detecting and responding to the deliberate release of biological agents that cause disease.",
    "A public-health and emergency-management field.")
new("bismuth-sulfite-agar-cae66c", "Bismuth sulfite agar", "knowledge",
    "A selective culture medium used in microbiology to isolate Salmonella, especially Salmonella Typhi, from samples.",
    "A laboratory culture medium.")
new("bit-ly-a0ed6b", "Bitly", "platform",
    "A link-management platform that shortens web addresses and tracks how the short links are used.",
    "A named link-shortening service.", variants=["Bit.ly"])
new("blackline-accounting-software-a32861", "BlackLine", "platform",
    "A cloud platform for automating financial close tasks such as account reconciliation and transaction matching.",
    "A named accounting software product, as the tag itself says.", relations=[("broader", "a0cpzx7lc1")])
new("blended-learning-371caf", "Blended learning", "method",
    "A teaching approach that combines online digital media with traditional face-to-face classroom instruction.",
    "A named instructional approach.")
new("blender-game-engine-fc4040", "Blender Game Engine", "tool",
    "The built-in real-time 3D game and interactive-content engine that shipped with Blender until version 2.80.",
    "A named game engine.")
new("boa-constructor-a744ad", "Boa Constructor", "tool",
    "A cross-platform integrated development environment and GUI builder for Python and wxPython, written in Python.",
    "A named development tool.")
new("board-certified-behavior-analyst-cb5935", "Board Certified Behavior Analyst", "credential",
    "A graduate-level certification, awarded by the Behavior Analyst Certification Board, for practitioners of applied behavior analysis.",
    "A named professional credential.", variants=["BCBA"], cert=True, scope="single-issuer")
new("board-certified-pharmacotherapy-speciali-fcbad9", "Board Certified Pharmacotherapy Specialist", "credential",
    "A specialty certification awarded by the Board of Pharmacy Specialties to pharmacists who show advanced skill in drug therapy.",
    "A named pharmacy credential.", variants=["BCPS"], cert=True, scope="single-issuer")
new("board-certified-specialist-in-renal-nutr-debeb2", "Board Certified Specialist in Renal Nutrition", "credential",
    "A specialty certification in kidney nutrition for registered dietitians, awarded by the Commission on Dietetic Registration.",
    "A named dietetics credential.", cert=True, scope="single-issuer")
new("board-certified-transplant-pharmacist-bc-593729", "Board Certified Transplant Pharmacist", "credential",
    "A specialty certification awarded by the Board of Pharmacy Specialties to pharmacists who show advanced skill in transplant pharmacy.",
    "A named pharmacy credential.", variants=["BCTXP"], cert=True, scope="single-issuer")
new("boating-license-1fcb77", "Boating license", "credential",
    "A licence or certificate, issued by a state or country, that allows a person to operate a recreational boat.",
    "A licence that many states and countries issue.", variants=["Boating licence"], cert=True, scope="many-issuers")
new("body-contouring-e50576", "Body contouring", "skill",
    "Performing cosmetic procedures that reduce fat or tighten and reshape areas of the body.",
    "A cosmetic-treatment skill.")
new("bodyattack-a72312", "BODYATTACK", "method",
    "A Les Mills group fitness class of high-energy athletic moves such as running and jumping, set to music.",
    "A named group fitness programme.")
new("bodypumps-068010", "BODYPUMP", "method",
    "A Les Mills group fitness class of barbell strength training with many repetitions, set to music.",
    "A named group fitness programme.")
new("bonjour-f30ecb", "Bonjour", "tool",
    "Apple's implementation of zero-configuration networking, which lets devices and services on a local network find each other automatically.",
    "Read as the Apple networking technology, the likeliest meaning in a skills list.")
new("boolean-algebra-7f117e", "Boolean algebra", "knowledge",
    "The branch of algebra in which variables take the values true or false and are combined with operations such as AND, OR and NOT.",
    "A branch of mathematics and logic.")
new("boolean-search-e15975", "Boolean search", "method",
    "Searching by combining terms with operators such as AND, OR and NOT, as in recruiting and research databases.",
    "A named search technique.", relations=[("contrast", "vw3ut9lcco")])
new("boom-lift-certification-7c5e30", "Boom lift certification", "credential",
    "A certificate showing that a person has been trained to operate boom lifts, aerial work platforms with an extending arm.",
    "A narrower credential than aerial lift certification, which also covers scissor lifts.",
    relations=[("broader", "umpb7it897")], cert=True, scope="many-issuers")
new("border-studies-b8a785", "Border studies", "knowledge",
    "An interdisciplinary field that studies political borders and boundaries and how they shape people, places and states.",
    "A field of study.")
new("bot-framework-9854dd", "Microsoft Bot Framework", "framework",
    "Microsoft's software development kit and set of services for building, connecting and deploying conversational bots.",
    "A named Microsoft framework.", variants=["Bot Framework"])
new("box-api-7b00c0", "Box API", "platform",
    "The programming interface of the Box cloud content-management service, used to manage files, folders, users and permissions from other software.",
    "A named product API.", relations=[("broader", "xe2d2jfa1r")])
new("box-backup-28c883", "Box Backup", "tool",
    "An open-source automatic online backup system with a client and a server.",
    "A named open-source backup project.")
new("brand-communication-568686", "Brand communication", "skill",
    "Conveying a brand's identity, message and values to its audiences through consistent channels and content.",
    "A marketing skill.", relations=[("related", "oz39xhtj91")])
new("brand-strategy-9061bb", "Brand strategy", "skill",
    "Defining a brand's long-term purpose, audience, positioning and identity so that its choices stay consistent.",
    "A marketing skill.")
new("branding-d17dc3", "Branding", "skill",
    "Creating and managing the name, identity and reputation by which a product, organisation or person is recognised.",
    "A marketing skill.", relations=[("related", "oz39xhtj91")])
new("breast-surgeries-e6b18f", "Breast surgery", "knowledge",
    "Surgical operations on the breast, such as lumpectomy, mastectomy, reconstruction and augmentation.",
    "A surgical field.", variants=["Breast surgeries"])
for stem in ("breeze-js-e22e87", "breeze-js-javascript-library-f1dcb2"):
    new(stem, "Breeze.js", "library",
        "A JavaScript library for managing data in rich client applications, with querying, caching and change tracking against a server.",
        "A named JavaScript library.")
new("brightway-8d566b", "Brightway", "framework",
    "An open-source Python framework for life cycle assessment, used to model the environmental impacts of products and processes.",
    "A named life cycle assessment framework.", variants=["Brightway2"])

# ---- not a skill ----------------------------------------------------------------------------
not_skill("binding-7f0043", "A bare generic word with several unrelated senses, such as data binding, bookbinding and legal binding.")
not_skill("biomedical-equipment-technician-6e468d", "A job title, not a skill.")
not_skill("blackmagic-275f27", "A company or brand name; its products, such as DaVinci Resolve, are the skills.")
not_skill("blindness-fe2688", "A medical condition, not a skill.")
not_skill("boiler-operator-58ebeb", "A job title, not a skill.")
not_skill("boiler-room-2adafb", "A place, or sales slang, not a skill.")
not_skill("bosun-df592d", "A ship's rank or job title, not a skill.")
not_skill("breakage-b22c98", "A generic word for damage or loss, not a skill.")
not_skill("breast-cancer-awareness-1b3a3e", "An awareness-campaign topic, not a skill.")
not_skill("bridges-49939a", "A bare plural noun with many senses (structures, dental work, networks, card games), not a skill.")
not_skill("bridging-1ea3c2", "A bare generic word with many senses, not a skill.")
not_skill("briquette-16c093", "A product, a compressed block of fuel, not a skill.")

# ---- unsure ---------------------------------------------------------------------------------
unsure("basic-shift-management-b404bd", "Could be a supervisory skill or the name of a training course, and I cannot tell which.")
unsure("batch-sheets-6be2ca", "Probably a production record used in manufacturing, but the name alone does not tell me what is asked of the worker.")
unsure("bentley-comms-386843", "I do not know what this is; it may be a company or a product name.")
unsure("bigtable-implementations-5c6212", "Unclear whether it means Google's Bigtable product or Bigtable-style stores such as HBase.")
unsure("bilingue-e0ac02", "French for bilingual; it names no language, so it is unclear whether a generic entry is wanted.")
unsure("bioinformatic-harvester-f1280d", "I think it is a meta-search tool for protein and gene data, but I am not sure enough to define it.")
unsure("blister-pack-df96f8", "Names a packaging product; unclear whether the skill meant is packaging work, machine operation or something else.")
unsure("bloodstains-f6e155", "Could mean bloodstain pattern analysis, stain removal or laboratory testing, and the name alone does not say.")
unsure("bonzai-3d-73d260", "I believe it is 3D modelling software but cannot confirm the maker or details.")
unsure("bridge-building-8fc13e", "Could mean civil engineering work or building relationships, and the name alone does not say.")
unsure("broadband-distribution-specialist-9f8f95", "Looks like a cable-industry specialist certification, but I cannot confirm the exact name or issuer.")
unsure("broadband-premises-specialist-be9155", "Looks like a cable-industry specialist certification, but I cannot confirm the exact name or issuer.")
unsure("broadband-telecomcenter-specialist-2df5fb", "Looks like a cable-industry specialist certification, but I cannot confirm the exact name or issuer.")


def main():
    stems = sorted(f[:-5] for f in os.listdir(REQ) if f.endswith(".json"))
    missing = [s for s in stems if s not in A]
    extra = [s for s in A if s not in stems]
    if missing or extra:
        print("MISSING", missing)
        print("EXTRA", extra)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    for s in stems:
        req = json.load(open(os.path.join(REQ, s + ".json"), encoding="utf-8"))
        ids = {n["id"] for n in req["nearest"]}
        r = A[s]
        if r["variant_of"] and r["variant_of"] not in ids:
            raise SystemExit(f"{s}: variant_of not in nearest")
        if r["entry"]:
            for rel in r["entry"]["relations"]:
                if rel["target"] not in ids:
                    raise SystemExit(f"{s}: relation target {rel['target']} not in nearest")
            if r["entry"]["kind"] not in req["allowed"]["kinds"]:
                raise SystemExit(f"{s}: bad kind")
        with open(os.path.join(OUT, s + ".json"), "w", encoding="utf-8") as fh:
            json.dump(r, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    from collections import Counter
    print(Counter(A[s]["decision"] for s in stems), len(stems))


main()
