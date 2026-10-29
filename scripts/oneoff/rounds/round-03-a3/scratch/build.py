import json, glob, os, collections

GK = "general-knowledge"
reqdir = "work/requests"
outdir = "work/responses"
os.makedirs(outdir, exist_ok=True)

reqs = {}
for f in sorted(glob.glob(reqdir + "/*.json")):
    r = json.load(open(f))
    reqs[r["term"]] = (os.path.basename(f), r)

ans = {}

def NS(term, reason):
    ans[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def UN(term, reason):
    ans[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def NEW(term, name, kind, definition, reason, variants=(), relations=(), cert=False, scope=None,
        lang=None, note=None):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    if note:
        e["annotation_note"] = note
    ans[term] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}

UN("Contouring", "Could mean makeup, body, map or radiotherapy contouring, and the nearest entry (body contouring) is only one of them.")
NS("Contract Manufacturer", "A type of company, not a skill.")
NS("Contract Research Organization", "A type of company, not a skill.")
NEW("Contract Reviews", "Contract review", "skill",
    "Reading a contract to check its terms, obligations and risks against what a party needs or the law allows.",
    "Contract review is a recognised legal and commercial skill.")
NS("Control Arms Campaign", "The name of an advocacy campaign, not a skill.")
NEW("Control Loops", "Control loops", "knowledge",
    "Feedback arrangements in which a controller compares a measured value with a setpoint and adjusts an output to keep them close, as in process and automation engineering.",
    "A standard control-engineering concept; no nearest entry covers it.",
    variants=["Control loop"])
NS("Control Risks", "A consultancy company name, not a skill.")
UN("Control Tables", "Used in programming, ETL and control engineering with different meanings, and the tag does not say which.")
NEW("Control Valves And Flow Characteristics", "Control valves and flow characteristics", "knowledge",
    "How valves that regulate fluid flow in process plants work, and how the flow through them changes with valve opening (for example linear, equal-percentage and quick-opening).",
    "A real process-engineering topic, though the tag joins two ideas.")
NEW("ControlLogix", "ControlLogix", "platform",
    "A family of programmable automation controllers from Rockwell Automation (Allen-Bradley) that run industrial machines and processes.",
    "A named industrial control product line.")
NEW("ControlUp", "ControlUp", "tool",
    "Software for monitoring and troubleshooting virtual desktops, servers and end-user devices in IT environments.",
    "A named IT monitoring product.")
NS("Convention Agreement in 1992", "A dated international agreement named by year, which is not a skill.")
NEW("Conversational AI", "Conversational AI", "knowledge",
    "Building software, such as chatbots and voice assistants, that talks with people in everyday language.",
    "A recognised AI field.",
    variants=["Conversational artificial intelligence"],
    relations=[("related", "vxpeg21e33")])
NEW("Convolutional Neural Networks", "Convolutional neural networks", "knowledge",
    "A type of neural network that applies learned filters across grid-like data such as images, widely used in computer vision.",
    "A standard machine-learning architecture; a narrower kind of neural network.",
    variants=["Convolutional neural network", "ConvNet"],
    relations=[("broader", "tx96mffcus")])
NS("Copenhagen Accord", "The name of a 2009 climate agreement, not a skill.")
NEW("Copier Troubleshooting", "Copier troubleshooting", "skill",
    "Diagnosing and fixing faults in photocopiers and multifunction office machines, such as paper jams and print-quality problems.",
    "A practical office-equipment maintenance skill.")
NEW("Coping Saw", "Coping saw", "tool",
    "A hand saw with a thin, narrow blade held in a U-shaped frame, used to cut curves in wood and to trim moulding joints.",
    "A named hand tool.")
NEW("Coppermine Photo Gallery (Free Image Galleries)", "Coppermine Photo Gallery", "tool",
    "A free, open-source web application, written in PHP, for hosting and managing online photo galleries.",
    "A named software product.")
NEW("Copywriting", "Copywriting", "skill",
    "Writing text for advertising, marketing and other persuasive material.",
    "A standard marketing skill, broader than AI copywriting.",
    relations=[("related", "o0bkdduxor")])
NS("Core Competency", "A generic business-strategy phrase, not a specific skill.")
NS("Core Services", "A generic business phrase, not a skill.")
NEW("Coreos", "CoreOS", "platform",
    "A minimal Linux-based operating system built for running applications in containers on clusters of servers.",
    "A named operating system, now discontinued.")
NEW("CoreSpotlight", "Core Spotlight", "framework",
    "An Apple framework for adding an app's content to the on-device Spotlight search index.",
    "A named Apple developer framework.")
NS("Cornelia De Lange Syndrome (CDLS)", "A genetic medical condition, not a skill.")
NEW("Corona (Software Development Kit)", "Corona SDK", "framework",
    "A cross-platform software development kit for building 2D mobile apps and games with the Lua scripting language.",
    "A named game and app development kit.")
NEW("Coronal Polishing", "Coronal polishing", "skill",
    "Polishing the crown surfaces of teeth to remove plaque and stain, a task often done by dental assistants and hygienists.",
    "A dental procedure skill.")
NEW("Coronal Polishing Certificate", "Coronal polishing certificate", "credential",
    "A certificate showing that a dental assistant has been trained in coronal polishing, which some US states require before they may do it.",
    "A credential, as the legacy certification list says.",
    cert=True, scope="many-issuers")
NEW("Corporate Communications", "Corporate communications", "skill",
    "Managing an organisation's messages to employees, investors, the media and the public.",
    "A standard communications discipline.",
    variants=["Corporate communication"],
    relations=[("related", "ii8017l1zt")])
UN("Corporate Distribution", "Could mean a company's distribution channels, distribution of goods, or tax distributions, and nothing here says which.")
NEW("Corporate Finance", "Corporate finance", "knowledge",
    "The field concerned with how companies raise money, invest it and manage their capital to create value for their owners.",
    "A standard finance field.")
NEW("Corporate Governance Of Information Technology", "IT governance", "knowledge",
    "The structures and processes by which an organisation directs and controls its use of information technology.",
    "The tag matches the title of the IT governance standard ISO/IEC 38500, which describes this concept.",
    variants=["Corporate governance of information technology"])
NEW("Correspondent Banking", "Correspondent banking", "knowledge",
    "Arrangements in which one bank provides services such as payments and account access to another bank, often across borders.",
    "A standard banking practice.")
NEW("Cosmetic Dermatology", "Cosmetic dermatology", "knowledge",
    "The branch of dermatology that improves the appearance of skin, hair and nails, for example with fillers, lasers and peels.",
    "A recognised medical subspecialty.")
NEW("Cost Accounting", "Cost accounting", "knowledge",
    "The part of accounting that records and analyses the costs of making goods or providing services so managers can control and price them.",
    "A standard accounting field.")
NEW("Cost Estimate", "Cost estimating", "skill",
    "Predicting what a project, product or job will cost before it is done.",
    "The tag is the noun for the output; the skill is cost estimating.",
    variants=["Cost estimation"])
NEW("Cost To Serve", "Cost to serve", "method",
    "A way of working out how much it costs a business to serve each customer, product or channel, counting activities such as delivery, handling and support.",
    "A known supply-chain and finance analysis approach.")
NEW("Costpoint", "Deltek Costpoint", "platform",
    "Enterprise resource planning software from Deltek, used mainly by government contractors and project-based businesses for accounting, project costing and billing.",
    "A named ERP product.")
NEW("Counter Terrorist Check (CTC)", "Counter Terrorist Check (CTC) clearance", "credential",
    "A UK government security clearance level, below Security Check (SC), for roles with unescorted access to sensitive sites or close contact with people at risk from terrorism.",
    "A UK security clearance level, parallel to the existing SC clearance entry.",
    variants=["Counter Terrorist Check", "CTC clearance"],
    relations=[("related", "b01cze4ssf")],
    cert=True, scope="single-issuer")
NS("Counterclaim", "A legal pleading term, not a skill.")
NEW("Counterparty Risk", "Counterparty risk", "knowledge",
    "The risk that the other party to a financial contract will fail to meet its obligations.",
    "A standard finance and risk concept.")
NS("Court Staff", "A group of workers (job titles), not a skill.")
NS("Craft Business", "A kind of business, not a skill.")
NEW("Craniofacial Surgery", "Craniofacial surgery", "knowledge",
    "The surgical specialty that repairs and reshapes the skull, face and jaws, including congenital differences such as cleft lip and palate.",
    "A recognised surgical specialty.")
NEW("Create React App", "Create React App", "tool",
    "A command-line tool from Facebook that sets up a new React web application with a ready-made build configuration.",
    "A named developer tool.")
NEW("Create Read Update and Delete (CRUD)", "CRUD", "knowledge",
    "The four basic operations of persistent data storage: create, read, update and delete.",
    "A standard software and database concept.",
    variants=["CRUD operations"])
NEW("Createjs", "CreateJS", "library",
    "A suite of JavaScript libraries for building interactive HTML5 canvas content, including EaselJS, TweenJS, SoundJS and PreloadJS.",
    "A named JavaScript library suite.")
NEW("Creative Arts Therapy", "Creative arts therapy", "skill",
    "Using art, music, dance or drama in a therapeutic setting to support people's emotional and mental health.",
    "A recognised therapy discipline.",
    relations=[("related", "y757v7j4f6")])
UN("Creative Design", "Too general to tell whether it means graphic design, advertising creative or another design discipline.")
NS("Creative Industries", "An industry sector, not a skill.")
NEW("Creative Problem-Solving", "Creative problem-solving", "skill",
    "Finding original solutions to problems by generating and testing new ideas.",
    "A recognised general work skill.",
    variants=["Creative problem solving"])
NS("Credit Card Fraud", "Names a type of crime, not a skill; detecting or investigating it would be the skill.")
NEW("Credit Risk Analysis", "Credit risk analysis", "skill",
    "Assessing how likely a borrower is to fail to repay and how much a lender could lose if that happens.",
    "A standard finance skill.")
NEW("Creo Elements/Pro (Computer-Aided Design Software)", "Creo Elements/Pro", "tool",
    "A parametric 3D computer-aided design package from PTC, formerly known as Pro/ENGINEER.",
    "A named CAD product.")
NEW("Crestron (A/V Systems)", "Crestron", "platform",
    "Control and automation systems for audio-visual equipment, lighting, shades and building technology, made by Crestron Electronics.",
    "A named control-system product line, used here as the skill of working with it.")
NEW("Crestron Certified Programmer", "Crestron Certified Programmer", "credential",
    "A certification from Crestron showing that a person can program Crestron control systems.",
    "A vendor credential, as the legacy certification list says.",
    cert=True, scope="single-issuer")
NEW("Crestron Programming", "Crestron programming", "skill",
    "Writing the control programs that run Crestron audio-visual and automation systems.",
    "A product-specific programming skill, parallel to AMX programming.",
    relations=[("related", "ppo11nahux")])
NEW("Crime Analysis", "Crime analysis", "skill",
    "Studying crime reports and data to find patterns and help police prevent and solve crimes.",
    "A recognised law-enforcement analysis skill.")
NEW("Crime Mapping", "Crime mapping", "skill",
    "Plotting crime data on maps to find hotspots and patterns that guide policing.",
    "A recognised law-enforcement analysis skill.")
UN("Crime Reporting", "Could mean writing police crime reports, journalism about crime, or statistical crime reporting.")
NEW("Crime Scenes (Forensic Evidence)", "Crime scene investigation", "skill",
    "Securing, documenting and collecting physical evidence at the place where a crime happened.",
    "The tag names the place and its evidence; the skill is investigating it.")
NEW("Criminal Intelligence", "Criminal intelligence", "knowledge",
    "Information about criminals, their networks and activities that police gather and analyse to prevent and investigate crime.",
    "A recognised policing field.")
NS("Criminal Records", "Names a kind of document, not a skill.")
UN("Crisis Prevention", "Could be the general skill of defusing crises or the Crisis Prevention Institute's training; the tag does not say.")
UN("Criteria Api", "Several Java persistence libraries have a Criteria API (JPA, Hibernate, Spring Data), and the tag does not say which.")
NEW("Critical Path Method", "Critical path method", "method",
    "A project scheduling technique that finds the longest chain of dependent tasks, which sets the shortest possible project duration.",
    "A standard project-management method.")
NEW("Critical Reflection", "Critical reflection", "skill",
    "Examining your own assumptions, actions and experience in order to learn from them and improve practice.",
    "A recognised skill in education, nursing and social work.")
NEW("Critical Test Results Management (CTRM)", "Critical test results management", "method",
    "The process of promptly telling the responsible clinician about dangerous laboratory or imaging results and recording that it was done.",
    "The full name is clear and is a healthcare process; the abbreviation CTRM is also used in commodity trading, so it is not offered as a variant.")
NEW("Crop Farming", "Crop farming", "knowledge",
    "Growing crops such as grains, vegetables and fruit, including preparing soil, planting, tending and harvesting.",
    "A body of farming practice, though it could also be read as an industry.")
NEW("Cross-Domain Solutions", "Cross-domain solutions", "knowledge",
    "Security systems that let information move between networks of different classification levels under strict controlled rules.",
    "A recognised government and defence security field.",
    variants=["Cross Domain Solutions"])
NEW("Cross-Platform Applications", "Cross-platform app development", "skill",
    "Building applications that run on more than one operating system or device type from a shared codebase.",
    "The tag names the product; the skill is building such apps.",
    variants=["Cross-platform application development"])
NEW("Cross Product", "Cross product", "knowledge",
    "An operation on two three-dimensional vectors that gives a third vector perpendicular to both.",
    "A standard mathematics concept, though 'cross product' is also used loosely for a Cartesian product in databases.",
    variants=["Vector product"])
UN("Crouton", "Could be an Android notification library, a ChromeOS tool or a food, and the tag does not say.")
NEW("CryEngines", "CryEngine", "tool",
    "A game engine from Crytek for building 3D games and real-time visualisations.",
    "A named game engine.")
NEW("Cryptocurrency", "Cryptocurrency", "knowledge",
    "Digital money secured by cryptography and usually run on decentralised blockchain networks, such as Bitcoin.",
    "A recognised technology and finance field.")
UN("Cryptocurrency Exchanges", "Names a type of marketplace or business, and it is unclear whether it means trading on, building or running one.")
NS("Cubic Motion", "A company name, not a skill.")
NEW("Cucumber.js", "Cucumber.js", "tool",
    "The JavaScript implementation of Cucumber, which runs plain-language Gherkin specifications as automated tests.",
    "A named testing tool; the same concept as the Cucumberjs tag.")
NEW("Cucumber (Software)", "Cucumber", "tool",
    "A behaviour-driven development tool that runs plain-language Gherkin specifications as automated tests.",
    "A named testing tool.")
NEW("Cucumberjs", "Cucumber.js", "tool",
    "The JavaScript implementation of Cucumber, which runs plain-language Gherkin specifications as automated tests.",
    "A named testing tool; the same concept as the Cucumber.js tag.")
NS("Cultural Tourism", "Names a segment of the tourism industry, not a skill.")
UN("Culturally Responsive", "An adjective that usually completes a phrase such as culturally responsive teaching, and the tag does not say which.")
NEW("Culturally Sensitive", "Cultural sensitivity", "skill",
    "Recognising and respecting differences in cultural background, beliefs and customs when dealing with people.",
    "The adjective points at a recognised interpersonal skill.")
NS("Culture Industry", "A critical-theory term or a sector name, not a skill.")
NEW("Culture Transformation", "Culture transformation", "skill",
    "Changing the shared values, habits and behaviours of an organisation so that it can reach a new goal.",
    "A recognised organisational-change skill.")
NEW("Cunit", "CUnit", "framework",
    "A lightweight unit testing framework for writing, administering and running tests in C.",
    "A named C testing framework.")
NEW("Curate Content", "Content curation", "skill",
    "Selecting, organising and presenting existing material from many sources for a chosen audience.",
    "A recognised content-marketing skill.")
NS("Curb Appeals", "Names a quality of a property (an outcome), not a skill.")
NEW("Cured-In-Place Pipes", "Cured-in-place pipe", "method",
    "A trenchless method of repairing a damaged pipe by inserting a resin-soaked liner that is hardened in place to form a new pipe inside the old one.",
    "A recognised pipe rehabilitation method.")
NEW("Curriculum Evaluation", "Curriculum evaluation", "skill",
    "Judging how well a curriculum meets its goals and how well students learn from it.",
    "A recognised education skill.")
NEW("Curriculum Planning", "Curriculum planning", "skill",
    "Deciding what a course or programme will teach and in what order, including its goals, content and assessment.",
    "A recognised education skill.")
NS("Cursor (Graphical User Interface Elements)", "A user-interface element, not a skill.")
UN("Custom Design Lean Mfg Systems", "Reads like a fragment of a resume line about designing lean manufacturing systems, not an established term.")
NEW("Custom Post Types", "Custom post types", "knowledge",
    "A WordPress feature that lets developers define their own kinds of content, beyond built-in posts and pages, with their own fields and templates.",
    "A named WordPress feature.",
    variants=["Custom post type"])
UN("Custom Url", "Could mean vanity URLs, URL rewriting or custom domains, and the tag does not say which.")
NEW("Customer Engagement Planning", "Customer engagement planning", "skill",
    "Planning how and when a business will interact with its customers across channels to keep them interested and loyal.",
    "A recognised marketing and customer-management skill.")
NEW("Customer Engagement Strategy", "Customer engagement strategy", "skill",
    "Defining the long-term approach a business uses to build relationships with customers and keep them active.",
    "A recognised marketing and customer-management skill.")
NEW("Customer Experience Strategy (CX)", "Customer experience strategy", "skill",
    "Defining how a business wants customers to experience it across every contact, and the plan for achieving that.",
    "A recognised customer-experience skill.",
    variants=["CX strategy"],
    relations=[("related", "sixghka9vw")])
NEW("Customer Insight", "Customer insight", "skill",
    "Using data and research on customer behaviour and needs to understand customers and guide business decisions.",
    "A recognised marketing and analytics skill.")
NEW("Customer Success", "Customer success", "skill",
    "Helping customers get the results they bought a product for, so that they keep using and renewing it.",
    "A recognised business function and skill, mainly in software companies.")
NS("Customer Support Analyst", "A job title, not a skill.")

missing = set(reqs) - set(ans)
extra = set(ans) - set(reqs)
assert not missing, missing
assert not extra, extra
cnt = collections.Counter()
for term, a in ans.items():
    fname, r = reqs[term]
    # check relation targets are in nearest
    ids = {n["id"] for n in r["nearest"]}
    if a["entry"]:
        for rel in a["entry"]["relations"]:
            assert rel["target"] in ids, (term, rel)
    cnt[a["decision"]] += 1
    json.dump(a, open(os.path.join(outdir, fname), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(outdir, fname), "a").write("\n")
print(len(ans), dict(cnt))
