"""Operator-side script: writes the model's answers for the pilot requests into work/responses/.
The answers are mine, drafted from general knowledge. Nothing here was checked against a source."""
import json
import sys
from pathlib import Path

work = Path(sys.argv[1])
G = "general-knowledge"


KIND_LANG = {"programming-language": "programming", "human-language": "spoken", "markup-language": "other"}


def N(name, kind, definition, variants=(), rels=(), verbs=(), cert=None, lang="auto", note=""):
    """cert defaults to True for credentials; lang defaults from the kind. Override when the default is wrong."""
    cert = (kind == "credential") if cert is None else cert
    lt = KIND_LANG.get(kind) if lang == "auto" else lang
    return {"decision": "new", "variant_of": None, "reason": "a skill, tool, credential, language or body of knowledge",
            "entry": {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": G,
                      "variants": [{"label": v, "basis": G} for v in variants],
                      "relations": [{"type": t, "target": x, "basis": G} for t, x in rels],
                      "verbs": [{"verb": v, "basis": G} for v in verbs],
                      "certification": {"value": cert, "basis": G},
                      "language_type": {"value": lt, "basis": G},
                      "annotation_note": note}}


def NOT(why):
    return {"decision": "not_a_skill", "variant_of": None, "reason": why, "entry": None}


def UNS(why):
    return {"decision": "unsure", "variant_of": None, "reason": why, "entry": None}


def VAR(target, why):
    return {"decision": "variant_of", "variant_of": target, "reason": why, "entry": None}


A = {
    "3d Solid And Surface Modeling": N("3D solid and surface modeling", "skill", "Building three-dimensional models of objects as solids and as surfaces in CAD software.", verbs=["model"]),
    "Additive Manufacturing": N("Additive manufacturing", "method", "Making physical objects by adding material layer by layer from a digital model, as in 3D printing.", verbs=["design for", "operate"]),
    "Administering Blood Tests": N("Administering blood tests", "skill", "Performing blood tests on patients, typically drawing a sample and preparing it for laboratory analysis."),
    "Adult/Gerontology Acute Care Nurse Practitioner": N("Adult-Gerontology Acute Care Nurse Practitioner", "credential", "A nurse practitioner certification for caring for acutely ill adult and older-adult patients.", variants=["AG-ACNP"]),
    "Advanced Trauma Life Support": N("Advanced Trauma Life Support", "credential", "A trauma-care training course and certification from the American College of Surgeons on the first assessment and management of injured patients.", variants=["ATLS"]),
    "Advisories": NOT("A generic noun for a notice or warning, not a skill."),
    "Agile Edge Technologies": UNS("Looks like a company name, but I cannot confirm that or any skill it might stand for."),
    "American Board Of Medical Laboratory Immunology (ABMLI) Certified": N("American Board of Medical Laboratory Immunology certification", "credential", "Certification by the American Board of Medical Laboratory Immunology in medical laboratory immunology.", variants=["ABMLI certification", "ABMLI"]),
    "Arkit": N("ARKit", "framework", "Apple's framework for building augmented reality apps on iOS and iPadOS.", verbs=["build", "integrate"]),
    "AWS Big Data": N("AWS big data", "skill", "Using Amazon Web Services' data analytics and big data services, such as EMR, Redshift and Kinesis, to store and process large datasets."),
    "Aymara (Language)": N("Aymara", "human-language", "An indigenous language of the Andes spoken mainly in Bolivia, Peru and Chile."),
    "Betfair": NOT("A betting exchange company and website, not a skill."),
    "Bleeding": NOT("A symptom or print term, not a skill on its own."),
    "Board Support Package (Software)": N("Board support package", "skill", "Developing the low-level code and drivers that let an operating system run on a specific hardware board.", variants=["BSP"], verbs=["develop", "port"]),
    "Cadvisor": N("cAdvisor", "tool", "A Google-developed tool that collects and exposes resource usage and performance data for running containers.", verbs=["deploy", "configure"]),
    "Catering Companies": NOT("Names a type of employer, not a skill."),
    "CBHT-DT": NOT("A television station call sign, not a skill."),
    "Certified Forensic Computer Examination": N("Certified Forensic Computer Examiner", "credential", "A digital forensics certification from the International Association of Computer Investigative Specialists.", variants=["CFCE"]),
    "Certified Pediatric Emergency Nurse": N("Certified Pediatric Emergency Nurse", "credential", "A nursing certification from the Board of Certification for Emergency Nursing for nurses who care for children in emergencies.", variants=["CPEN"]),
    "Certified Professional Geologist": N("Certified Professional Geologist", "credential", "A professional certification for geologists from the American Institute of Professional Geologists.", variants=["CPG"]),
    "Certified Retirement Administrator": N("Certified Retirement Administrator", "credential", "A professional certification for people who administer retirement plans."),
    "CompTIA Mobility+": N("CompTIA Mobility+", "credential", "A CompTIA certification covering the management and support of mobile devices and the systems that manage them."),
    "Core Api": UNS("Could mean several different APIs; the tag alone does not say which."),
    "Dagger 2": N("Dagger 2", "framework", "A dependency injection framework for Java and Android that generates its code at compile time.", variants=["Dagger2"]),
    "Data Wrangling": N("Data wrangling", "skill", "Cleaning, reshaping and combining raw data so it can be analysed.", variants=["Data munging"], rels=[("related", "skill:0004")], verbs=["clean", "transform"]),
    "Database Programmer'S Toolkits": UNS("Unclear whether this names a product, a category of libraries or a skill."),
    "Dbvisualizer": N("DbVisualizer", "tool", "A graphical database client for browsing, querying and administering many kinds of databases.", verbs=["query with"]),
    "Deposition (Geology)": N("Deposition (geology)", "knowledge", "The geological process by which sediment, soil or rock is laid down on a landform or land mass."),
    "Design Surface": UNS("Could be a software design-time surface, a physical work surface or something else."),
    "Deterministic methods": N("Deterministic methods", "method", "Methods whose result is fully determined by their inputs, with no randomness involved."),
    "Doctor Of Physical Therapy": N("Doctor of Physical Therapy", "credential", "A doctoral degree that qualifies graduates to practise as physical therapists in the United States.", variants=["DPT"]),
    "Doctor Of Public Health": N("Doctor of Public Health", "credential", "A doctoral degree in public health focused on professional practice and leadership.", variants=["DrPH"]),
    "Doubles Endorsement": N("Doubles/triples endorsement", "credential", "A commercial driver's licence endorsement that permits towing two or three trailers."),
    "Drone Pilot Certificate": N("Drone pilot certificate", "credential", "A certificate that allows a person to fly small unmanned aircraft commercially; in the United States, the FAA Remote Pilot Certificate under Part 107.", variants=["Remote Pilot Certificate"]),
    "Dynamic Cycle Counting": N("Dynamic cycle counting", "method", "Cycle counting of inventory in which the timing of each count is set by rules such as item value, movement or error history."),
    "Electronic Paper": N("Electronic paper", "knowledge", "Display technology that mimics ink on paper, reflecting light and holding an image without power, as used in e-readers.", variants=["E-paper"]),
    "Esker (Software)": N("Esker", "tool", "Cloud software for automating document-based business processes such as accounts payable and order processing."),
    "Express.js": N("Express.js", "framework", "A minimal web application framework for Node.js.", variants=["ExpressJS"]),
    "Flexi (Photoshop Plugin)": UNS("I do not know this plugin."),
    "French Languages": N("French", "human-language", "A Romance language spoken in France and many other countries.", variants=["French language"]),
    "Good Driving Record": NOT("A job requirement, not a skill."),
    "Functional Analysis": UNS("Means different things in mathematics, systems engineering and behavioural analysis; the tag does not say which."),
    "Short Films": NOT("A type of film, not a skill on its own."),
    "Hotel Industry": NOT("Names an industry sector, not a skill."),
    "Html Formatting": N("HTML formatting", "skill", "Marking up and styling text and page content with HTML tags."),
    "IAM Level I Certification": N("IAM Level I certification", "credential", "An information assurance management qualification at Level I, as defined in the U.S. Department of Defense 8570 workforce framework."),
    "IBM POWER8 Microprocessors": N("IBM POWER8", "platform", "IBM's eighth-generation POWER microprocessor family for servers, released in 2014.", variants=["POWER8"]),
    "InsightVM (Vulnerability Scanning Software)": N("InsightVM", "tool", "Rapid7's vulnerability management software, which scans systems for security weaknesses and helps prioritise fixes.", variants=["Rapid7 InsightVM"], verbs=["configure", "run scans with"]),
    "Interactive 3D": N("Interactive 3D", "skill", "Building three-dimensional content that users can rotate, explore or manipulate in real time, for example in a browser or game engine."),
    "Intermediate Language": UNS("Could mean a compiler intermediate language or an intermediate level of proficiency in a human language."),
    "Ironworker": NOT("A job title for a trade, not a skill."),
    "Jacoco": N("JaCoCo", "library", "A free Java code coverage library that measures how much of a program its tests run."),
    "Jsdata": N("JSData", "library", "A framework-agnostic JavaScript library for managing application data in a client-side store."),
    "Karaf": N("Apache Karaf", "platform", "An Apache runtime container for deploying and managing OSGi-based Java applications.", variants=["Karaf"]),
    "Law Enforcement Operations": N("Law enforcement operations", "knowledge", "Planning and carrying out the work of police and other law enforcement agencies."),
    "Living Conditions": NOT("A generic phrase for circumstances, not a skill."),
    "Management Training": UNS("Could mean delivering training to managers or having received it; the tag does not say."),
    "Marathi (Language)": N("Marathi", "human-language", "An Indo-Aryan language spoken mainly in the Indian state of Maharashtra."),
    "Master Of Laws": N("Master of Laws", "credential", "A postgraduate law degree taken after a first law degree.", variants=["LL.M."]),
    "Master Of Laws in Taxation": N("Master of Laws in Taxation", "credential", "A postgraduate law degree that specialises in tax law.", variants=["LL.M. in Taxation", "Master of Laws in Tax"]),
    "Masterpiece": NOT("A generic noun, not a skill."),
    "Masters Certificate In Project Management": N("Master's certificate in project management", "credential", "A graduate-level certificate programme in project management, shorter than a master's degree.", rels=[("related", "skill:0074")]),
    "Media Center Markup Language": N("Media Center Markup Language", "markup-language", "An XML-based markup language used to build user interfaces for Windows Media Center applications.", variants=["MCML"]),
    "Mixed Reality": N("Mixed reality", "knowledge", "Technology that blends real and virtual objects so that they interact in real time."),
    "Multi-Programming Monitor Control Program": UNS("I do not recognise this system."),
    "Natural Language Understanding": N("Natural language understanding", "knowledge", "The part of natural language processing concerned with getting machines to grasp the meaning and intent of human language.", variants=["NLU"], rels=[("broader", "skill:0039")], note="A field of study about language, not a language that people speak or program in."),
    "Neonatal Resuscitation Programs": N("Neonatal Resuscitation Program", "credential", "A training programme from the American Academy of Pediatrics and the American Heart Association on resuscitating newborns.", variants=["NRP"]),
    "Nfpa 70e": N("NFPA 70E", "knowledge", "A National Fire Protection Association standard for electrical safety in the workplace in the United States."),
    "Objective-C (Progamming Language)": N("Objective-C", "programming-language", "An object-oriented extension of C used for Apple's macOS and iOS software.", variants=["Obj-C"]),
    "Obstacles To Troop Movement": NOT("A phrase describing a battlefield condition, not a skill."),
    "Outbreak": NOT("A generic noun for a sudden spread of disease, not a skill."),
    "Passenger Endorsement": N("Passenger endorsement", "credential", "A commercial driver's licence endorsement that permits driving vehicles that carry passengers, such as buses."),
    "Pedals": NOT("A physical part, not a skill."),
    "Phoenician (Language)": N("Phoenician", "human-language", "An extinct Canaanite language of the ancient Phoenicians, written in the Phoenician alphabet."),
    "Plumbing Drawing": N("Plumbing drawing", "skill", "Preparing or reading technical drawings that show the layout of pipes and fixtures in a building."),
    "Production Support": N("Production support", "skill", "Monitoring and troubleshooting a live system to resolve problems that affect users.", verbs=["troubleshoot", "monitor"]),
    "Professional Services": NOT("Names a business line or sector, not a skill."),
    "ProSystem Fx Engagement (Tax Software)": N("CCH ProSystem fx Engagement", "tool", "Wolters Kluwer CCH software that accounting firms use to manage engagements and workpapers."),
    "Reading Gauges": N("Reading gauges", "skill", "Reading analog or digital gauges to check pressure, temperature, levels or flow on equipment."),
    "Regulation SHO": N("Regulation SHO", "knowledge", "A U.S. Securities and Exchange Commission regulation governing short sales of securities, including locate and close-out requirements."),
    "Restricted Radiotelephone Operator Permit": N("Restricted Radiotelephone Operator Permit", "credential", "A U.S. Federal Communications Commission permit that allows a person to operate certain radio equipment, such as aircraft and marine radios."),
    "SACA Certified Industry 4.0 Associate Basic Operations": N("SACA Certified Industry 4.0 Associate, Basic Operations", "credential", "A certification from the Smart Automation Certification Alliance for basic operations in Industry 4.0 manufacturing environments."),
    "Safety Trained Supervision": N("Safety Trained Supervisor", "credential", "A safety credential for supervisors trained to manage workplace safety.", variants=["STS"]),
    "Screening Resumes": N("Screening resumes", "skill", "Reviewing resumes to pick the candidates who match a job's requirements.", verbs=["screen", "shortlist"]),
    "Searchable Ornithological Research Archive (SORA)": NOT("Names a digital archive of ornithology literature, not a skill."),
    "Security Check (SC)": N("Security Check (SC) clearance", "credential", "A UK government security clearance level that allows regular access to secret assets.", variants=["SC clearance"]),
    "Slovene Language": N("Slovene", "human-language", "A South Slavic language spoken mainly in Slovenia.", variants=["Slovenian"]),
    "Software as a Service (SaaS)": N("Software as a service", "knowledge", "A way of delivering software over the internet by subscription, hosted by the provider instead of installed by the customer.", variants=["SaaS"]),
    "Software Localization": N("Software localization", "skill", "Adapting software to a specific language and region, including translating text and adjusting formats such as dates and currencies.", variants=["Software localisation", "L10n"]),
    "Solutions-focused": NOT("An adjective for an attitude, not a defined skill."),
    "Spatial Temporal Reasoning": N("Spatial-temporal reasoning", "ability", "The ability to understand and mentally work with how objects and events are arranged in space and change over time."),
    "Submit Button": NOT("A user interface element, not a skill."),
    "Tabbed": NOT("An adjective for a user interface layout, not a skill."),
    "Tanker And Hazmat Combo X Endorsement": N("Tanker and hazmat combination (X) endorsement", "credential", "A commercial driver's licence endorsement that combines the tank vehicle (N) and hazardous materials (H) endorsements."),
    "TL 9000": N("TL 9000", "knowledge", "A quality management system standard for the telecommunications industry, built on ISO 9001.", variants=["TL9000"]),
    "UltraTax": N("UltraTax CS", "tool", "Thomson Reuters software that accounting firms use to prepare tax returns.", verbs=["prepare returns in"]),
    "UX Research": VAR("skill:0054", "Same concept as user research."),
    "Va Loans": N("VA loans", "knowledge", "Mortgage loans guaranteed by the U.S. Department of Veterans Affairs for eligible service members and veterans."),
    "Visme (Software)": N("Visme", "tool", "An online tool for making presentations, infographics and other visual content."),
    "Windows Software Development": N("Windows software development", "skill", "Writing software that runs on the Microsoft Windows operating system.", verbs=["develop"]),
    "Xbrl": N("XBRL", "markup-language", "An XML-based standard language for tagging and exchanging business and financial reporting data."),
    "Yahoo Messenger": N("Yahoo Messenger", "tool", "An instant messaging service from Yahoo, shut down in 2018."),
}

(work / "responses").mkdir(exist_ok=True)
seen = set()
for p in sorted((work / "requests").glob("*.json")):
    t = json.loads(p.read_text("utf-8"))["term"]
    if t not in A:
        sys.exit(f"no answer for {t!r}")
    (work / "responses" / p.name).write_text(json.dumps(A[t], indent=1, ensure_ascii=False) + "\n", "utf-8")
    seen.add(t)
extra = set(A) - seen
if extra:
    print(f"warning: answers with no request (not used): {sorted(extra)}")
kinds = {}
for a in A.values():
    kinds[a["decision"]] = kinds.get(a["decision"], 0) + 1
print(len(seen), "answers written", kinds)
