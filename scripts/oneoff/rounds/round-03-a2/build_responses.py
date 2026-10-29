import json, glob, os

GK = "general-knowledge"
R = {}  # term -> response


def V(labels):
    return [{"label": l, "basis": GK} for l in labels]


def rel(t, target):
    return {"type": t, "target": target, "basis": GK}


def entry(name, kind, defn, variants=(), rels=(), cert=False, scope=None):
    e = {"preferred_name": name, "kind": kind, "definition": defn, "definition_basis": GK,
         "variants": V(variants), "relations": list(rels), "verbs": [],
         "certification": {"value": cert, "basis": GK}}
    if cert:
        e["certification_scope"] = {"value": scope or "single-issuer", "basis": GK}
    e["language_type"] = {"value": None, "basis": GK}
    e["annotation_note"] = ""
    return e


def new(term, name, kind, defn, variants=(), rels=(), reason=None):
    R[term] = {"decision": "new", "variant_of": None,
               "reason": reason or "A recognisable skill, tool or body of knowledge that no nearest entry covers.",
               "entry": entry(name, kind, defn, variants, rels)}


def cred(term, name, defn, variants=(), rels=(), scope="single-issuer", reason=None):
    R[term] = {"decision": "new", "variant_of": None,
               "reason": reason or "A certification awarded by one body.",
               "entry": entry(name, "credential", defn, variants, rels, cert=True, scope=scope)}


def nas(term, reason):
    R[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(term, reason):
    R[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def variant(term, target, reason):
    R[term] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


STACK = "A CompTIA stackable certification awarded for holding a specified combination of other CompTIA certifications, {}."

# ---- 0-10
unsure("Compact File Set (CFS)", "I do not recognise this term and cannot say what it refers to.")
new("Compiler Developments", "Compiler development", "skill",
    "Designing and building compilers, the programs that translate source code into machine code or another language.",
    reason="The plural phrase clearly refers to developing compilers.")
unsure("Compiling Tools", "Could mean compilers, build tools or the act of compiling; the phrase is too vague to define.")
new("Complaint Investigations", "Complaint investigation", "skill",
    "Looking into complaints from customers, employees or the public to establish the facts and decide how to resolve them.")
nas("Complex Web Systems", "A generic description of the systems someone works on, not a defined skill.")
new("Compliance Risk Management", "Compliance risk management", "skill",
    "Identifying, assessing and controlling the risk that an organisation breaks laws, regulations or its own policies.")
new("Compliance Testing", "Compliance testing", "method",
    "Checking whether processes, controls or products meet the laws, regulations or standards that apply to them.")
new("Componentone", "ComponentOne", "library",
    "A commercial suite of user-interface controls and data components for .NET and web applications.")
new("Composite Patterns(Software Design Patterns)", "Composite pattern", "method",
    "A structural software design pattern that lets single objects and groups of objects be treated the same way through a shared tree-shaped interface.",
    variants=["Composite design pattern"])
unsure("Composition", "A single generic word that could mean music, writing, photography or software, with no context to choose.")
unsure("Compositions", "A single generic word that could mean music, writing, photography or software, with no context to choose.")

# ---- 11-56 CompTIA
CASP = "CompTIA Advanced Security Practitioner (CASP+)"
cred("CompTIA Advanced Security Practitioner", CASP,
     "A CompTIA certification for experienced security practitioners, covering advanced enterprise security architecture, operations and risk management.",
     variants=["CASP+", "CompTIA CASP+"])
cred("CompTIA CASP CE", CASP,
     "A CompTIA certification for experienced security practitioners, covering advanced enterprise security architecture, operations and risk management.",
     variants=["CASP+", "CompTIA CASP+"],
     reason="The CE form is the same CompTIA certification as CASP+, renewed through continuing education.")
cred("CompTIA CDIA+", "CompTIA CDIA+",
     "A CompTIA certification for document imaging professionals, covering the planning and design of document imaging systems.")
CLOUD = "A CompTIA certification covering the configuration, deployment, security and management of cloud infrastructure."
cred("CompTIA Cloud+", "CompTIA Cloud+", CLOUD)
cred("CompTIA Cloud Admin Professional (CCAP)", "CompTIA Cloud Admin Professional (CCAP)",
     STACK.format("for cloud administration"), variants=["CompTIA CCAP"])
cred("CompTIA Cloud+ CE", "CompTIA Cloud+", CLOUD,
     reason="The CE form is the same CompTIA certification as Cloud+, renewed through continuing education.")
cred("CompTIA Cloud Essentials", "CompTIA Cloud Essentials+",
     "A CompTIA certification covering the business and technical fundamentals of cloud computing.")
cred("CompTIA Convergence Technologies Professional (CTP+)", "CompTIA Convergence Technologies Professional (CTP+)",
     "A CompTIA certification covering convergence technologies, the combining of voice, video and data on shared networks.",
     variants=["CompTIA CTP+"])
CYSA = "A CompTIA certification for security analysts, covering threat detection, vulnerability management and incident response."
cred("CompTIA Cybersecurity Analyst (CySA+)", "CompTIA Cybersecurity Analyst (CySA+)", CYSA,
     variants=["CySA+", "CompTIA CySA+"], rels=[rel("related", "norpz7ekiw")])
cred("CompTIA Cybersecurity Analyst (CySA+) CE", "CompTIA Cybersecurity Analyst (CySA+)", CYSA,
     variants=["CySA+", "CompTIA CySA+"], rels=[rel("related", "norpz7ekiw")],
     reason="The CE form is the same CompTIA certification as CySA+, renewed through continuing education.")
cred("CompTIA Digital Home Technology Integrator (DHTI+)", "CompTIA Digital Home Technology Integrator (DHTI+)",
     "A CompTIA certification for technicians who install and integrate technology systems in homes.",
     variants=["CompTIA DHTI+"])
cred("CompTIA e-Biz+", "CompTIA e-Biz+",
     "A CompTIA certification covering the concepts and technology of electronic business.")
cred("CompTIA Green IT Specialist", "CompTIA Green IT Specialist",
     "A CompTIA certification covering environmentally responsible use and management of IT equipment.")
cred("CompTIA Healthcare IT Technician", "CompTIA Healthcare IT Technician",
     "A CompTIA certification for IT technicians who support healthcare settings, covering topics such as electronic health records and healthcare regulations.")
cred("CompTIA HTI+", "CompTIA HTI+",
     "A CompTIA certification for home technology integrators who install and integrate technology systems in homes.")
cred("CompTIA i-Net+", "CompTIA i-Net+",
     "A CompTIA certification covering foundational knowledge of Internet, intranet and extranet technologies.")
cred("CompTIA Instructor+", "CompTIA Instructor+",
     "A CompTIA certification for people who deliver technical training, covering classroom instruction skills.")
cred("CompTIA IT For Sales", "CompTIA IT for Sales",
     "A CompTIA certification covering IT concepts and terminology for people who sell technology products and services.")
ITF = "A CompTIA entry-level certification covering basic IT concepts such as hardware, software, networking and security."
cred("CompTIA IT Fundamentals", "CompTIA IT Fundamentals+", ITF, variants=["CompTIA ITF+"])
cred("CompTIA IT Operations Specialist (CIOS)", "CompTIA IT Operations Specialist (CIOS)",
     STACK.format("for IT operations"), variants=["CompTIA CIOS"])
cred("CompTIA Linux Network Professional (CLNP)", "CompTIA Linux Network Professional (CLNP)",
     STACK.format("for Linux and network administration"), variants=["CompTIA CLNP"])
cred("CompTIA Linux+ Powered By LPI", "CompTIA Linux+",
     "A CompTIA certification covering the installation, configuration, security and troubleshooting of Linux systems.",
     reason="The LPI-powered form is a version of the CompTIA Linux+ certification.")
cred("CompTIA Mobile App Security+", "CompTIA Mobile App Security+",
     "A CompTIA certification covering how to build and test mobile apps securely.")
variant("CompTIA Mobility+ CE", "ffswfagi3s",
        "The CE form is the same CompTIA Mobility+ certification, renewed through continuing education.")
cred("CompTIA Network+ CE", "CompTIA Network+",
     "A CompTIA certification covering how to configure, manage, secure and troubleshoot wired and wireless networks.",
     rels=[rel("related", "fnhev4v1dn")],
     reason="The CE form is the same CompTIA certification as Network+, renewed through continuing education.")
cred("CompTIA Network Infrastructure Professional (CNIP)", "CompTIA Network Infrastructure Professional (CNIP)",
     STACK.format("for network infrastructure"), variants=["CompTIA CNIP"])
cred("CompTIA Network Security Professional (CNSP)", "CompTIA Network Security Professional (CNSP)",
     STACK.format("for network security"), variants=["CompTIA CNSP"], rels=[rel("related", "norpz7ekiw")])
cred("CompTIA Network Vulnerability Assessment Professional (CNVP)", "CompTIA Network Vulnerability Assessment Professional (CNVP)",
     STACK.format("for network vulnerability assessment"), variants=["CompTIA CNVP"])
cred("CompTIA PenTest+ CE", "CompTIA PenTest+",
     "A CompTIA certification covering penetration testing, vulnerability assessment and vulnerability management.",
     reason="The CE form is the same CompTIA certification as PenTest+, renewed through continuing education.")
cred("CompTIA Printing and Document Imaging (PDI+)", "CompTIA Printing and Document Imaging (PDI+)",
     "A CompTIA certification for technicians who work with printing and document imaging equipment.",
     variants=["CompTIA PDI+"])
cred("CompTIA RFID+", "CompTIA RFID+",
     "A CompTIA certification covering radio-frequency identification (RFID) technology and its deployment.")
cred("CompTIA Secure Cloud Professional (CSCP)", "CompTIA Secure Cloud Professional (CSCP)",
     STACK.format("for secure cloud work"), variants=["CompTIA CSCP"])
cred("CompTIA Secure Infrastructure Specialist (CSIS)", "CompTIA Secure Infrastructure Specialist (CSIS)",
     STACK.format("for secure IT infrastructure"), variants=["CompTIA CSIS"])
cred("CompTIA Security Analytics Expert (CSAE)", "CompTIA Security Analytics Expert (CSAE)",
     STACK.format("for security analytics at expert level"), variants=["CompTIA CSAE"])
cred("CompTIA Security Analytics Professional (CSAP)", "CompTIA Security Analytics Professional (CSAP)",
     STACK.format("for security analytics at professional level"), variants=["CompTIA CSAP"])
cred("CompTIA Security+ CE", "CompTIA Security+",
     "A CompTIA certification covering core cybersecurity skills such as threats, network security, cryptography and risk management.",
     reason="The CE form is the same CompTIA certification as Security+, renewed through continuing education.")
cred("CompTIA Security Infrastructure Expert (CSIE)", "CompTIA Security Infrastructure Expert (CSIE)",
     STACK.format("for security infrastructure at expert level"), variants=["CompTIA CSIE"])
STOR = "A CompTIA certification covering the fundamentals of data storage technology."
cred("CompTIA Storage+ Powered By SNIA", "CompTIA Storage+", STOR,
     reason="The SNIA-powered form is a version of the CompTIA Storage+ certification.")
cred("CompTIA Storage+ Powered By SNIA CE", "CompTIA Storage+", STOR,
     reason="The CE form is the same CompTIA Storage+ certification, renewed through continuing education.")
cred("CompTIA Strata - IT Fundamentals", "CompTIA IT Fundamentals+", ITF, variants=["CompTIA ITF+"],
     reason="Strata IT Fundamentals is an earlier name of the CompTIA IT Fundamentals certification.")
STRATA_UNSURE = "I know CompTIA Strata as a brand of entry-level CompTIA certifications but cannot confirm this credential exists or say what it covers."
for t in ["CompTIA Strata - Network Technology Engineer", "CompTIA Strata - PC Functionality",
          "CompTIA Strata - PC Hardware Technology Engineer", "CompTIA Strata - PC Operating System Engineer",
          "CompTIA Strata - PC Technology"]:
    unsure(t, STRATA_UNSURE)
cred("CompTIA Systems Support Specialist (CSSS)", "CompTIA Systems Support Specialist (CSSS)",
     STACK.format("for systems support"), variants=["CompTIA CSSS"])

# ---- 57-99
new("Computational Design", "Computational design", "skill",
    "Using algorithms and code to generate, analyse and refine designs, as in parametric architecture and product design.")
new("Computer Architecture", "Computer architecture", "knowledge",
    "The design and organisation of a computer's components, such as the processor, memory and instruction set.")
new("Computer Assisted Audit Tools And Techniques (CAATT)", "Computer-assisted audit tools and techniques (CAATTs)", "method",
    "The use of software tools and techniques to analyse data and automate audit procedures.",
    variants=["CAATs", "CAATTs"])
new("Computer-Assisted Qualitative Data Analysis Software", "Computer-assisted qualitative data analysis software (CAQDAS)", "tool",
    "Software for organising, coding and analysing non-numerical data such as interviews, text and recordings.",
    variants=["CAQDAS"])
new("Computer Fraud And Abuse Act", "Computer Fraud and Abuse Act", "standard",
    "A US federal law that prohibits unauthorised access to protected computers and related computer crimes.",
    variants=["CFAA"])
variant("Computer Networking Systems", "fnhev4v1dn",
        "Computer networking systems is another way of saying computer networking.")
new("Computer Sciences", "Computer science", "knowledge",
    "The study of computation, algorithms, data and the design of computer systems and software.")
variant("Computer Security", "norpz7ekiw",
        "Computer security is used as a synonym of cybersecurity, which is protecting information and systems from threats.")
new("Computerized System Validation", "Computerized system validation", "method",
    "The documented process of showing that a computerised system consistently does what it is meant to do, used in regulated industries such as pharmaceuticals.",
    variants=["Computer System Validation"])
new("ComputerRx (Pharmacy Management Software)", "ComputerRx", "tool",
    "A pharmacy management software product used to handle prescriptions and pharmacy operations.")
new("Concision", "Concision", "skill",
    "Expressing ideas clearly in no more words than are needed.")
new("Concourse CI", "Concourse CI", "tool",
    "An open-source continuous integration and delivery system in which pipelines are defined in YAML and tasks run in containers.")
cred("Concrete Strength Testing Technician", "ACI Concrete Strength Testing Technician",
     "An American Concrete Institute certification for technicians who test the strength of concrete.",
     reason="An American Concrete Institute technician certification, not just a job title.")
nas("Concussions", "A medical condition, not a skill.")
unsure("Conditioners (Farming)", "Could mean hay conditioner machines or soil conditioning products; I cannot tell which skill or tool is meant.")
new("Conduct Tours", "Conducting tours", "skill",
    "Leading groups on guided tours and presenting information about the places or facilities visited.")
unsure("Conductor Certification", "Could mean a railroad conductor certification or something else, and I cannot tell which body issues it.")
new("Cone Penetration Tests", "Cone penetration testing", "method",
    "A geotechnical test in which an instrumented cone is pushed into the ground to measure soil properties and layering.",
    variants=["Cone penetration test"])
new("Confirmit", "Confirmit", "platform",
    "A survey and market research software platform for building surveys and analysing responses.")
new("Conflict Catcher", "Conflict Catcher", "tool",
    "A classic Mac OS utility for managing extensions and control panels and finding conflicts between them.")
nas("Confluence (Physical Geography)", "The meeting point of two rivers in physical geography, not a skill and unrelated to the Confluence wiki.")
new("Confluent", "Confluent", "platform",
    "A data streaming platform built on Apache Kafka, offered self-managed as Confluent Platform and as the Confluent Cloud service.")
new("Confocal", "Confocal microscopy", "method",
    "A microscopy technique that uses a pinhole to block out-of-focus light so that thin optical sections of a specimen can be imaged.")
nas("Confrontational", "An adjective describing a personality or style, not a skill.")
new("Consensus Decision-Making", "Consensus decision-making", "method",
    "A group decision process that seeks the agreement of all participants rather than a majority vote.",
    variants=["Consensus decision making"])
unsure("Console System Interface", "I do not recognise this as a specific product or standard and the phrase is too vague to define.")
unsure("Consolidated Media Reports", "Probably a work product, such as a compiled media summary, but I cannot tell what skill is meant.")
new("Consolidation (Financial)", "Financial consolidation", "skill",
    "Combining the financial statements of a parent company and its subsidiaries into a single set of group accounts.")
new("Constantcontact", "Constant Contact", "platform",
    "An online email marketing service for building and sending email campaigns and managing contact lists.")
new("Constituent Relationship Management", "Constituent relationship management", "method",
    "Managing the relationships of a nonprofit or public body with its donors, members and other constituents, usually with CRM software.")
new("Constraint Layout", "ConstraintLayout", "library",
    "An Android layout manager that positions and sizes views using constraints relative to other views and to the parent.")
new("Construct (Game Engine)", "Construct (game engine)", "tool",
    "A 2D game engine from Scirra that uses a visual editor and event sheets so that games can be made with little or no coding.")
new("Construct Study Casts", "Constructing dental study casts", "skill",
    "Pouring and trimming dental impressions in gypsum to make study casts, the models of a patient's teeth used for diagnosis and treatment planning.")
new("Construction Management Software", "Construction management software", "tool",
    "Software for planning, tracking and coordinating construction projects, including schedules, budgets and documents.")
new("Consumer Engagement", "Consumer engagement", "skill",
    "Building and sustaining interaction between a brand and its consumers across channels.")
new("Contact Management Softwares", "Contact management software", "tool",
    "Software for storing and organising contact details and the history of interactions with each contact.")
new("Contact Tracing", "Contact tracing", "method",
    "A public health method of identifying and notifying people who were exposed to someone with an infectious disease, so that spread can be limited.")
nas("Content Assist", "A code-completion feature of an IDE, a UI element rather than a skill.")
nas("Content Editor", "A job title (or an interface element of a content system), not a skill.")
new("Contingency Plan", "Contingency planning", "method",
    "Preparing plans for responding to events that could disrupt normal operations.")
new("Continued Process Verification", "Continued process verification", "method",
    "Ongoing collection and analysis of manufacturing data to confirm that a validated process stays in a state of control, a stage of process validation in regulated industries.")
new("Continuous Passive Motion", "Continuous passive motion", "method",
    "A rehabilitation therapy in which a machine moves a joint through a set range of motion without effort from the patient, often after joint surgery.")
new("Contour Plowing", "Contour plowing", "method",
    "Plowing across a slope along its elevation contours rather than up and down it, to slow water runoff and soil erosion.",
    variants=["Contour ploughing"])

# ---- write
os.chdir("/home/user/rounds/round-03/a2/skills-lexicon")
files = sorted(glob.glob("work/requests/*.json"))
terms = {}
for f in files:
    terms[json.load(open(f))["term"]] = os.path.basename(f)
missing = set(terms) - set(R)
extra = set(R) - set(terms)
assert not missing and not extra, (missing, extra)
os.makedirs("work/responses", exist_ok=True)
from collections import Counter
c = Counter()
for t, fn in terms.items():
    json.dump(R[t], open("work/responses/" + fn, "w"), indent=1, ensure_ascii=False)
    c[R[t]["decision"]] += 1
print(len(terms), dict(c))
