"""Scratch script: build the 100 answers for work/requests/ and write them to work/responses/."""
import json
import glob
import os

ROOT = "/home/user/rounds/round-01/a3/skills-lexicon"
GK = "general-knowledge"

req_files = sorted(glob.glob(f"{ROOT}/work/requests/*.json"))
terms = [json.load(open(f))["term"] for f in req_files]

ANS = {}  # term -> answer


def new(term, name, kind, definition, reason, variants=(), relations=(), cert=False, scope=None, lang=None, note=""):
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
        "annotation_note": note,
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    ANS[term] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}


def no(term, reason):
    ANS[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(term, reason):
    ANS[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


AWS = "h00skqgqmn"       # Amazon Web Services (nearest of the AWS CLI / AWS SDK requests)
DEVOPS = "d4xxm6t88j"    # DevOps (nearest of Azure DevOps)
CYBER = "norpz7ekiw"     # Cybersecurity (nearest of Azure Security)
SWENG = "qmravcc671"     # Software engineering (nearest of Back End)

# ---------------------------------------------------------------- 0-9
new("Asset Turnovers", "Asset turnover", "knowledge",
    "A financial ratio that compares a company's sales with its assets to show how efficiently the assets are used to generate revenue.",
    "Asset turnover is a standard financial-analysis ratio; plural form of the tag.",
    variants=["Asset turnover ratio"])
unsure("Assigned Amount Units",
       "Names a Kyoto Protocol emissions unit (an instrument), and it is unclear whether a posting wants it as a skill; left for a person.")
new("Assisted Housing Manager Certification (AHM)", "Assisted Housing Manager (AHM)", "credential",
    "A professional certification for managers of assisted (government-subsidised) rental housing programmes.",
    "I recall AHM as a US assisted-housing manager designation but cannot name the issuer with confidence.",
    variants=["AHM"], cert=True, scope="single-issuer")
new("Associate Degree In Nursing", "Associate degree in nursing", "credential",
    "A two-year undergraduate nursing degree, usually awarded by community colleges, that prepares graduates to take the registered-nurse licensing exam.",
    "A degree, so a credential; awarded by many colleges.",
    cert=True, scope="many-issuers")
unsure("Associate Electronics Technician",
       "Could be an associate-level electronics technician certification or just a job title; the tag alone does not say which.")
new("Associate of the Society of Actuaries", "Associate of the Society of Actuaries", "credential",
    "An actuarial designation awarded by the Society of Actuaries to candidates who pass its associateship exams and meet its other requirements; it ranks below Fellow.",
    "ASA is the Society of Actuaries' associate-level designation.",
    cert=True, scope="single-issuer")
new("Associate Professional In Talent Development", "Associate Professional in Talent Development", "credential",
    "A certification from the Association for Talent Development aimed at early-career talent development (workplace learning) professionals.",
    "APTD is an ATD certification.",
    variants=["APTD"], cert=True, scope="single-issuer")
unsure("Associate Project Management",
       "Could mean PMI's CAPM, an associate degree in project management, or an associate-level job; the tag alone does not say which.")
new("Associates Degree In Nursing", "Associate degree in nursing", "credential",
    "A two-year undergraduate nursing degree, usually awarded by community colleges, that prepares graduates to take the registered-nurse licensing exam.",
    "Same concept as 'Associate Degree In Nursing'; identical preferred_name given on purpose so it is retried as a variant.",
    cert=True, scope="many-issuers")
new("Association Management Specialist (AMS)", "Association Management Specialist (AMS)", "credential",
    "A professional designation for community (homeowner) association managers, awarded by Community Associations Institute.",
    "I recall AMS as a Community Associations Institute designation; moderately sure that is what the tag means.",
    variants=["AMS"], cert=True, scope="single-issuer")

# ---------------------------------------------------------------- 10-19
no("Association Of Professional Notaries", "An association (an organisation), not a skill.")
new("Asthma Education", "Asthma education", "skill",
    "Teaching people with asthma and their caregivers to recognise triggers, use medicines and inhalers correctly and follow an asthma action plan.",
    "A recognisable patient-education practice.")
new("Async Await Pattern", "Async/await", "method",
    "A programming pattern, supported by syntax in languages such as C#, JavaScript and Python, that lets asynchronous operations be written in code that reads like sequential steps.",
    "Well-known concurrency pattern.")
new("Athletic Training", "Athletic training", "knowledge",
    "The health-care field concerned with preventing, assessing, treating and rehabilitating injuries and illnesses related to sport and physical activity.",
    "The field of athletic trainers; the credential is a separate thing.")
new("Atlassian Confluence", "Atlassian Confluence", "tool",
    "Atlassian's web-based team workspace and wiki for creating, organising and sharing documents and project knowledge.",
    "Named Atlassian product; full name used because 'Confluence' alone is an everyday word.")
new("Atlassian Crucible", "Atlassian Crucible", "tool",
    "Atlassian's web-based tool for peer code review, in which developers comment on each other's changes before they are accepted.",
    "Named Atlassian product; full name used because 'Crucible' alone is an everyday word.")
new("Atomic Layer Deposition", "Atomic layer deposition", "method",
    "A thin-film deposition technique that builds a material one atomic layer at a time through alternating, self-limiting gas-phase surface reactions.",
    "Standard semiconductor and materials process.",
    variants=["ALD"])
new("AtScale (Software)", "AtScale", "platform",
    "A semantic-layer platform that sits between data warehouses and business-intelligence tools so that different tools use the same business definitions of data.",
    "Named analytics software; '(Software)' is only a legacy disambiguator.")
new("Attorney-Client Privilege", "Attorney-client privilege", "knowledge",
    "The legal protection that keeps confidential communications between a lawyer and client, made to obtain legal advice, from being disclosed without the client's consent.",
    "A legal doctrine, so knowledge.",
    variants=["Attorney client privilege"])
unsure("Audio Equipments",
       "A generic category of hardware; unclear whether the skill meant is operating, setting up or maintaining audio gear.")

# ---------------------------------------------------------------- 20-29
unsure("Audiography", "I am not sure what this is; it may be a rare term for hearing testing (audiometry) but I cannot confirm that.")
no("Audit Process Tools", "A generic phrase that names no specific tool or method.")
unsure("Audit Processes",
       "Close to auditing or knowledge of audit procedures, but I cannot say it is exactly the same concept as Auditing.")
no("Audit Schedules", "A generic work item (a plan or document), not a skill in itself.")
new("Auditd", "auditd", "tool",
    "The user-space daemon of the Linux Audit system, which collects kernel audit events and writes them to log files for security auditing.",
    "Named Linux tool.")
new("Auditing", "Auditing", "skill",
    "Examining records, processes or systems to check that they are accurate and comply with requirements or controls.",
    "A well-known professional skill.")
new("Auditing Inpatient Coding", "Auditing inpatient coding", "skill",
    "Reviewing the diagnosis and procedure codes assigned to hospital inpatient stays to check that they are accurate, supported by the record and compliant with coding rules.",
    "Names an activity in medical coding.",
    note="The tag names an activity, not a credential, and I know no certification with this exact name.")
new("Auditing Outpatient Coding", "Auditing outpatient coding", "skill",
    "Reviewing the diagnosis and procedure codes assigned to outpatient (ambulatory) encounters to check that they are accurate, supported by the record and compliant with coding rules.",
    "Names an activity in medical coding.",
    note="The tag names an activity, not a credential, and I know no certification with this exact name.")
unsure("Auditing Wireless Networks Certification",
       "Possibly a wireless-auditing certification such as GIAC's GAWN, but the tag is only a descriptive phrase and the issuer is unclear.")
unsure("Auditor'S Report",
       "Names a document type (the auditor's opinion on financial statements); unclear whether it is wanted as a skill, so left for a person.")

# ---------------------------------------------------------------- 30-39
unsure("Aura Framework",
       "Could be Salesforce's Aura (Lightning) component framework or the unrelated Aura.js library; the tag alone does not say which.")
new("Aural Rehabilitation", "Aural rehabilitation", "skill",
    "Therapy and training that help people with hearing loss communicate, using residual hearing, hearing devices, speech-reading and communication strategies.",
    "Recognised audiology practice.",
    variants=["Audiologic rehabilitation", "Auditory rehabilitation"])
new("Aurelia", "Aurelia", "framework",
    "An open-source JavaScript front-end framework for building single-page web applications.",
    "Well-known JavaScript framework.")
new("Authorised Capital", "Authorised capital", "knowledge",
    "The maximum amount of share capital a company is permitted to issue under its constitutional documents.",
    "A corporate-finance and company-law concept.",
    variants=["Authorized capital", "Authorised share capital"])
new("AuthorIT (Software)", "Author-it", "tool",
    "Software for writing, managing and publishing technical documentation and other content from reusable components.",
    "Named content-authoring software; '(Software)' is only a legacy disambiguator.",
    variants=["AuthorIT"])
no("Autism", "A medical condition, not a skill.")
new("Autism (Therapies)", "Autism therapy", "skill",
    "Providing therapies and interventions, such as applied behavior analysis and speech, occupational and social-skills therapy, for people on the autism spectrum.",
    "The tag names therapy practice for autism, unlike the plain condition.",
    variants=["Autism therapies"])
new("Auto Glass Installation And Repair", "Auto glass installation and repair", "skill",
    "Replacing and repairing vehicle windshields and windows, including removing damaged glass and bonding in new glass.",
    "A clear trade skill.")
unsure("Autobahn",
       "Could be the German motorway system or the Autobahn WebSocket/WAMP libraries; the tag alone does not say which.")
new("Autodesk 123D", "Autodesk 123D", "tool",
    "A discontinued family of free Autodesk apps for 3D modelling, scanning and digital fabrication.",
    "Named (retired) Autodesk product family.")

# ---------------------------------------------------------------- 40-49
no("Autodesk Developer Network", "A vendor developer programme (an organisation), not a skill.")
unsure("Autolayout",
       "Could be Apple's Auto Layout, Figma's auto layout or automatic chip layout; the tag alone does not say which.")
unsure("Automated Hacking Machines", "I do not know what this refers to.")
new("Automated Information Systems Security", "Automated information systems security", "knowledge",
    "The protection of computer-based information systems and the data they process, a term used in US government and military guidance.",
    "Dated US government term for information-systems security.")
unsure("Automatic File Distributor", "I do not know what this refers to; it may be a product or just a descriptive phrase.")
unsure("Automatic Property Extraction", "I do not know what this refers to; it could be a programming or a data-extraction term.")
unsure("Automation Clips",
       "Possibly a feature of music software such as FL Studio, or something else; I cannot tell whether it is a skill.")
unsure("Automation Controls",
       "Could mean industrial automation and control systems or software-automation controls; the tag alone does not say which.")
new("Automotive Detailing", "Automotive detailing", "skill",
    "Thoroughly cleaning, polishing and protecting the interior and exterior of a vehicle.",
    "A clear trade skill.",
    variants=["Auto detailing", "Car detailing"])
new("Automotive Finance", "Automotive finance", "knowledge",
    "The field of financing vehicle purchases and leases, including the loans, leases, lenders and dealers involved.",
    "A recognised area of consumer finance.")

# ---------------------------------------------------------------- 50-59
new("Automotive Loans", "Automotive loans", "knowledge",
    "Loans taken out to buy a vehicle, usually secured by the vehicle itself.",
    "Consumer-lending product area.",
    variants=["Auto loans"])
new("Autonomic Servous System", "Autonomic nervous system", "knowledge",
    "The part of the nervous system that regulates involuntary body functions such as heart rate, digestion and breathing.",
    "Misspelling of 'Autonomic nervous system'.")
new("Autoregressive Integrated Moving Average (ARIMA)", "Autoregressive integrated moving average", "method",
    "A statistical time-series model that forecasts a series from its own past values and past forecast errors, after differencing the series to remove trends.",
    "Standard forecasting method.",
    variants=["ARIMA"])
new("Autoshade", "Autoshade", "tool",
    "A discontinued Autodesk add-on for producing shaded, rendered images of AutoCAD models.",
    "Named (retired) Autodesk program; moderately sure.")
no("Auxiliary Air Control Valves (AAC)", "A physical engine component, not a skill.")
new("AvantGo", "AvantGo", "platform",
    "A discontinued service that delivered web content and enterprise applications to handheld devices such as Palm and Pocket PC PDAs.",
    "Named (retired) mobile platform.")
no("Avaya (Telecommunications)", "A company; its products (for example Avaya Aura) would be separate entries.")
unsure("Aviation Digital", "I do not know what this refers to.")
new("Aviation Medical Examination", "Aviation medical examination", "skill",
    "Performing medical examinations to decide whether pilots and other aviation personnel meet the medical standards required for flying duties.",
    "Recognised aviation-medicine activity.")
no("Aviation Technology", "A broad industry or field label, not a specific skill.")

# ---------------------------------------------------------------- 60-69
new("Avid Elastic Reality", "Avid Elastic Reality", "tool",
    "A discontinued Avid application for warping and morphing images and video.",
    "Named (retired) Avid product.")
new("Avid Media Composer (Software)", "Avid Media Composer", "tool",
    "Avid's professional non-linear video-editing software.",
    "Named product; '(Software)' is only a legacy disambiguator.")
new("Aws Cli", "AWS Command Line Interface", "tool",
    "A command-line tool from Amazon Web Services for managing and automating AWS services from a terminal or script.",
    "Named AWS tool.",
    variants=["AWS CLI"], relations=[("related", AWS)])
new("Aws Lambda", "AWS Lambda", "tool",
    "An Amazon Web Services compute service that runs code in response to events without the user provisioning or managing servers.",
    "Named AWS service.")
new("Aws Sdk", "AWS SDK", "library",
    "Amazon Web Services' software development kits, available for languages such as JavaScript, Python, Java and Go, for calling AWS services from application code.",
    "Named AWS libraries.",
    variants=["AWS SDKs"], relations=[("related", AWS)])
new("Axios", "Axios", "library",
    "A promise-based JavaScript HTTP client library for web browsers and Node.js.",
    "Well-known JavaScript library.")
unsure("Azari (Language)",
       "Azari can mean Azerbaijani (Azeri) or a different, extinct Iranian language of the same region; the tag alone does not say which.")
new("Azure Application Insights", "Azure Application Insights", "tool",
    "A Microsoft Azure application performance monitoring service that collects telemetry such as requests, failures and traces from running applications.",
    "Named Azure service.")
new("Azure Data Factory", "Azure Data Factory", "tool",
    "A Microsoft Azure cloud service for building and scheduling data-integration pipelines that move and transform data.",
    "Named Azure service.")
new("Azure DevOps", "Azure DevOps", "platform",
    "Microsoft's set of services for planning work, hosting code, and building, testing and releasing software, including Boards, Repos and Pipelines.",
    "Named Microsoft platform; related to, not the same as, the DevOps method.",
    relations=[("related", DEVOPS)])

# ---------------------------------------------------------------- 70-79
new("Azure Internet of Things (IoT)", "Azure IoT", "tool",
    "Microsoft Azure's set of services, such as IoT Hub and IoT Central, for connecting Internet of Things devices to the cloud and managing the data they send.",
    "Named Azure services family.",
    variants=["Azure Internet of Things"])
new("Azure Monitor", "Azure Monitor", "tool",
    "A Microsoft Azure service that collects, analyses and acts on metrics, logs and other telemetry from cloud and on-premises resources.",
    "Named Azure service.")
new("Azure Policy", "Azure Policy", "tool",
    "A Microsoft Azure service that defines and enforces rules on cloud resources so that they stay compliant with an organisation's standards.",
    "Named Azure service.")
new("Azure Security", "Azure Security", "skill",
    "Securing workloads and data on Microsoft Azure using its security services and controls, such as identity and access management, key management and network protection.",
    "Cloud-security practice on Azure; narrower than cybersecurity.",
    relations=[("broader", CYBER)])
new("Azure Sentinel", "Microsoft Sentinel", "tool",
    "Microsoft's cloud-native security information and event management (SIEM) and security orchestration, automation and response (SOAR) service.",
    "Azure Sentinel was renamed Microsoft Sentinel; the old name is kept as a variant.",
    variants=["Azure Sentinel"])
new("B-Tree", "B-tree", "knowledge",
    "A self-balancing tree data structure that keeps sorted data in nodes with many children, widely used for indexes in databases and file systems.",
    "Standard computer-science data structure.")
new("Babylon.js", "Babylon.js", "framework",
    "An open-source JavaScript and TypeScript engine for building 3D graphics, games and interactive experiences in web browsers.",
    "Well-known web 3D engine.")
new("Babylonjs", "Babylon.js", "framework",
    "An open-source JavaScript and TypeScript engine for building 3D graphics, games and interactive experiences in web browsers.",
    "Same concept as 'Babylon.js'; identical preferred_name given on purpose so it is retried as a variant.")
new("Bachelor Of Science in Business", "Bachelor of Science in Business", "credential",
    "An undergraduate degree in business studies, awarded as a Bachelor of Science by universities and colleges.",
    "A degree, so a credential; awarded by many universities.",
    cert=True, scope="many-issuers")
new("Bachelor Of Science in Business Administration", "Bachelor of Science in Business Administration", "credential",
    "An undergraduate degree in business administration, awarded as a Bachelor of Science by universities and colleges.",
    "A degree, so a credential; awarded by many universities.",
    variants=["BSBA"], cert=True, scope="many-issuers")

# ---------------------------------------------------------------- 80-89
new("Bachelor Of Science in Nursing (BSN)", "Bachelor of Science in Nursing", "credential",
    "A bachelor's-level nursing degree, awarded by universities and colleges, that prepares graduates for registered-nurse licensure.",
    "A degree, so a credential; awarded by many universities.",
    variants=["BSN"], cert=True, scope="many-issuers")
new("Bachelor Of Science In Pharmacy", "Bachelor of Science in Pharmacy", "credential",
    "An undergraduate degree in pharmacy, awarded as a Bachelor of Science by universities and colleges.",
    "A degree, so a credential; awarded by many universities.",
    cert=True, scope="many-issuers")
new("Back End (Software Engineering)", "Back-end development", "skill",
    "Building and maintaining the server-side parts of software, such as application logic, databases and APIs.",
    "Common software-development specialism; narrower than software engineering.",
    variants=["Backend development", "Back end development"], relations=[("broader", SWENG)])
unsure("Back Pressures",
       "Could be backpressure (flow control) in software streams or back pressure in engines and fluid systems; the tag alone does not say which.")
new("Backbone.Js", "Backbone.js", "library",
    "A lightweight JavaScript library that gives web applications structure through models, views, collections and routers.",
    "Well-known JavaScript library.")
new("Bacnet", "BACnet", "standard",
    "A communication protocol for building automation and control systems, standardised as ASHRAE 135 and ISO 16484-5.",
    "Published building-automation protocol standard.")
new("Bacon.js", "Bacon.js", "library",
    "A JavaScript library for functional reactive programming that models events and changing values as observable streams.",
    "Named JavaScript library.")
new("Bacteria Cultures", "Bacterial culture", "method",
    "Growing bacteria in a laboratory on or in nutrient media in order to isolate, identify or study them.",
    "Standard microbiology laboratory technique.")
new("Bacteriology", "Bacteriology", "knowledge",
    "The branch of microbiology that studies bacteria.",
    "A scientific field.")
unsure("Bahasa (Language)",
       "'Bahasa' just means 'language'; in postings it means Indonesian or Malay, and the tag alone does not say which.")

# ---------------------------------------------------------------- 90-99
no("Bakeries", "A type of business or place, not a skill.")
new("Balafon", "Balafon", "skill",
    "Playing the balafon, a West African tuned percussion instrument with wooden bars over gourd resonators, struck with mallets.",
    "Musical-instrument skill.")
unsure("Bali Action Plan",
       "Names a UN climate-negotiation decision document; unclear whether it is wanted as a skill, so left for a person.")
new("Balloon Modelling", "Balloon modelling", "skill",
    "Twisting and shaping long, narrow balloons into figures and decorations.",
    "A recognised entertainer's craft.",
    variants=["Balloon modeling", "Balloon twisting"])
new("Banner Ads", "Banner advertising", "skill",
    "Creating and managing banner ads, the rectangular graphic display advertisements placed on web pages and apps.",
    "Online display-advertising practice.",
    variants=["Banner ads"])
new("Banner Advertising", "Banner advertising", "skill",
    "Creating and managing banner ads, the rectangular graphic display advertisements placed on web pages and apps.",
    "Same concept as 'Banner Ads'; identical preferred_name given on purpose so it is retried as a variant.")
new("Banyan Vines", "Banyan VINES", "platform",
    "A discontinued network operating system from Banyan Systems, used on enterprise networks in the 1980s and 1990s.",
    "Named (retired) network operating system; fairly sure the tag means this and not the plant.")
new("BIND", "BIND", "tool",
    "Berkeley Internet Name Domain, the widely used open-source DNS server software maintained by the Internet Systems Consortium.",
    "Named DNS software; the all-caps name should match case-exactly because 'bind' is an everyday word.",
    variants=["Berkeley Internet Name Domain"])
no("BIPOC", "A demographic term (Black, Indigenous and People of Color), not a skill.")
unsure("BIRCH",
       "Could be the BIRCH clustering algorithm, but the tag alone does not say so; it is also a tree and other things.")

# ---------------------------------------------------------------- write
assert set(ANS) == set(terms), (set(terms) - set(ANS), set(ANS) - set(terms))
os.makedirs(f"{ROOT}/work/responses", exist_ok=True)
counts = {}
for f, t in zip(req_files, terms):
    a = ANS[t]
    assert len(a["reason"]) <= 200, (t, len(a["reason"]))
    counts[a["decision"]] = counts.get(a["decision"], 0) + 1
    with open(f"{ROOT}/work/responses/{os.path.basename(f)}", "w", encoding="utf-8") as fh:
        json.dump(a, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
print(counts, len(ANS))
