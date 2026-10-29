import json, glob, os, sys

GK = "general-knowledge"
R = {}  # stem -> answer


def stem(prefix):
    m = [os.path.basename(f)[:-5] for f in glob.glob(f"work/requests/{prefix}-*.json")]
    # prefix must match the whole stem minus the 6-char hash
    m = [s for s in m if s.rsplit("-", 1)[0] == prefix]
    assert len(m) == 1, (prefix, m)
    return m[0]


def new(prefix, reason, name, kind, definition, variants=(), relations=(), verbs=(),
        cert=False, scope=None, lang=None, note=""):
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for (t, tg) in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        assert scope in ("single-issuer", "many-issuers")
        e["certification_scope"] = {"value": scope, "basis": GK}
    R[stem(prefix)] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}


def no(prefix, reason):
    R[stem(prefix)] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(prefix, reason):
    R[stem(prefix)] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


# ---------------- unsure ----------------
unsure("document-enterprise-platform", "I do not recognise this as a specific product or method, and there is no context.")
unsure("duplex", "The bare word could mean printing, housing, telephony, networking or Google Duplex.")
unsure("dynamic-resource-scheduler", "It resembles VMware's Distributed Resource Scheduler but I cannot confirm a product by this exact name.")
unsure("dynamic-ui", "It could be a general technique for runtime-generated interfaces or a named product, and the tag does not say.")
unsure("dynamo", "The bare word could be Autodesk Dynamo, Amazon DynamoDB or the Dynamo paper, and the tag does not say.")
unsure("druid", "The bare word could be Apache Druid (an analytics database) or a religious or fantasy druid.")
unsure("early-childhood-ancillary-certificate", "It sounds like a certificate, but I cannot say who issues it or what it requires.")
unsure("ec-council-certified-security-officer", "I cannot confirm that EC-Council awards a credential with this exact name.")
unsure("eels", "The upper-case form could be electron energy-loss spectroscopy, the band, or the fish; the tag does not say.")
unsure("educational-effectiveness", "It may be an accreditation and assessment concept or just an outcome, and the tag does not say.")
unsure("electronic-loads-analysis", "It could mean analysing programmable electronic test loads or electrical load analysis for a system.")
unsure("electronic-plan-management-system", "It could be a generic category or a specific permitting product, and I cannot tell which.")
unsure("electronic-project-generator", "I do not recognise this as a specific product, method or field.")
unsure("elevation", "The bare word could mean architectural elevation drawings, altitude or something else.")
unsure("emagic-trio", "eMagic was a music-software company, but I do not know a product called Trio and will not guess.")
unsure("employability-development", "It could mean career-readiness coaching or a training programme, and the tag does not say.")
unsure("etudes", "It could be the ETUDES-NG learning management system or the French word for studies; I cannot tell which.")

# ---------------- not a skill ----------------
no("domestic-product", "A generic economics or retail phrase, not a skill.")
no("dress-codes", "A workplace policy, not a skill.")
no("drop-down-list", "A user-interface element, not a skill.")
no("durban-platform-for-enhanced-action", "A UN climate negotiation process, not a skill, tool or standard.")
no("dynamic-communicator", "A descriptive phrase about a person; the skill is communication.")
no("dysarthria", "A medical condition (a motor speech disorder), not a skill.")
no("dyslipidemia", "A medical condition, not a skill.")
no("dry-strength-resin", "A papermaking chemical additive, a material rather than a skill, tool or method.")
no("ecosystem", "A generic word, not a specific skill.")
no("eels-anguilliformes", "A group of fish, not a skill.")
no("effective-coach", "A descriptive phrase about a person; the skill would be coaching.")
no("electrical-circuit-simple-english-wikipe", "A scraped web-page title, not a skill name.")
no("electronic-voice-phenomenon", "A paranormal claim, not a skill.")
no("elements-compounds-and-materials", "A school-curriculum topic heading, not a skill or field.")
no("emc-technician", "A job title, not a skill.")
no("emergency-support", "A generic phrase, not a specific skill.")
no("employability", "A generic quality or outcome, not a skill.")
no("employee-handbooks", "A type of document, not a skill.")

# ---------------- new ----------------
new("document-exploitation", "Document exploitation is an intelligence-gathering practice.",
    "Document exploitation", "skill",
    "Systematically extracting and analysing information from captured or seized documents and media for intelligence or investigative use.")

new("documentation-lifecycle", "A lifecycle model for documentation, comparable to the Database life cycle entry.",
    "Documentation lifecycle", "knowledge",
    "The stages documentation passes through, from planning and writing to review, publication, maintenance and retirement.")

new("dot-js", "doT.js is a JavaScript template engine.",
    "doT.js", "library",
    "A small, fast JavaScript templating library that compiles templates into functions for use in browsers and Node.js.")

new("dot-matrix-printing", "A long-established printing technology.",
    "Dot matrix printing", "knowledge",
    "Printing in which a head of small pins strikes an inked ribbon to form characters and images from patterns of dots.")

new("doubleclick-for-publishers-by-google", "A Google ad-serving product, now part of Google Ad Manager.",
    "DoubleClick for Publishers", "platform",
    "Google's ad-serving platform for publishers to manage, deliver and measure the ads on their sites and apps, now part of Google Ad Manager.",
    variants=["DFP"])

new("draft-boiler", "Boiler draft is a standard boiler-engineering term.",
    "Boiler draft", "knowledge",
    "The pressure difference that moves combustion air and flue gases through a boiler furnace and stack.")

new("dried-blood-spot", "A laboratory sampling method.",
    "Dried blood spot", "method",
    "A sampling method in which drops of blood are collected on filter paper, dried and later analysed in a laboratory.")

new("driver-s-vision-enhancer-optical-devices", "A military thermal-imaging driving aid.",
    "Driver's Vision Enhancer", "tool",
    "A thermal-imaging device that lets a vehicle driver see the road in darkness, smoke, fog or dust.")

new("driving", "Driving is a developed capacity to operate vehicles.",
    "Driving", "skill",
    "Operating a car, truck or other motor vehicle safely on roads.")

new("drug-absorption", "A core pharmacology concept.",
    "Drug absorption", "knowledge",
    "How a drug moves from its site of administration into the bloodstream, and the factors that affect the rate and extent of that movement.")

new("drug-quality-and-security-act", "A US federal law.",
    "Drug Quality and Security Act", "standard",
    "A 2013 US federal law that set national requirements for tracing prescription drugs through the supply chain and for regulating compounding pharmacies.",
    variants=["DQSA"])

new("dry-needling", "A physical-therapy technique.",
    "Dry needling", "method",
    "A therapy technique in which thin needles are inserted into myofascial trigger points to relieve pain and improve movement.")

new("drywall-installation-and-repair", "A construction trade skill.",
    "Drywall installation and repair", "skill",
    "Hanging, taping, finishing and patching gypsum board panels on walls and ceilings.",
    verbs=["install", "repair", "finish"])

new("duala-language", "Duala is a Bantu language of Cameroon.",
    "Duala", "human-language",
    "A Bantu language spoken in and around the city of Douala in Cameroon.",
    lang="human")

new("duck-creek-platform-software", "A commercial insurance software platform.",
    "Duck Creek Platform", "platform",
    "A software platform from Duck Creek Technologies for property and casualty insurers to run policy, billing and claims.")

new("durable-medical-equipment", "A standard healthcare equipment category.",
    "Durable medical equipment", "tool",
    "Reusable medical equipment prescribed for use at home, such as wheelchairs, hospital beds and walkers.",
    relations=[("related", "t5cy0zpwuy")])

new("dust-js", "Dust.js is a JavaScript template library.",
    "Dust.js", "library",
    "A JavaScript templating library with asynchronous rendering that runs in browsers and in Node.js.")

new("dynamic-host-configuration-protocol", "DHCP is a standard network protocol.",
    "Dynamic Host Configuration Protocol", "standard",
    "A network protocol that automatically gives devices an IP address and other network settings.",
    variants=["DHCP"], verbs=["configure"])

new("dynamic-link-libraries", "DLLs are a Windows shared-library mechanism.",
    "Dynamic-link library", "knowledge",
    "The Microsoft Windows format and mechanism for shared code libraries that programs load at run time.",
    variants=["DLL"])

new("e-marketing", "E-marketing is marketing through electronic channels.",
    "E-marketing", "skill",
    "Promoting products and services through electronic channels such as websites, email and social media.",
    variants=["Electronic marketing"])

new("earlgrey-software", "EarlGrey is a Google iOS test framework.",
    "EarlGrey", "framework",
    "An open-source framework from Google for automating user-interface tests of native iOS apps.")

new("early-childhood-mental-health", "A recognised field of practice.",
    "Early childhood mental health", "knowledge",
    "The social and emotional well-being of children from birth to about age five, and the practice of supporting it and treating problems.")

new("earned-value-management-systems-evms", "EVMS is a project-control method.",
    "Earned value management system", "method",
    "An integrated project-management system that compares work done with planned scope, schedule and cost, as set out in the ANSI/EIA-748 guidelines.",
    variants=["EVMS"])

new("earth-leakage-circuit-breaker", "A protective electrical device.",
    "Earth leakage circuit breaker", "tool",
    "A protective switch that cuts the power when current leaks to earth, to reduce the risk of electric shock and fire.",
    variants=["ELCB"])

new("earthing-systems", "Earthing is the UK and international term for grounding.",
    "Earthing systems", "knowledge",
    "The ways of connecting parts of an electrical installation to the ground for safety, such as TN, TT and IT systems.",
    variants=["Grounding systems"])

new("easeljs", "EaselJS is part of the CreateJS suite.",
    "EaselJS", "library",
    "A JavaScript library that provides a display list and interaction model for drawing on the HTML5 canvas.",
    relations=[("part_of", "a6uxgvojco")])

new("ebay-api", "eBay's programming interfaces.",
    "eBay API", "platform",
    "The programming interfaces of the eBay marketplace, used to list, search and manage items and orders from other software.")

new("ecological-study", "An epidemiological study design.",
    "Ecological study", "method",
    "An observational study design in which the units analysed are whole populations or groups rather than individual people.")

new("econometric-model", "A standard economics modelling approach.",
    "Econometric model", "method",
    "A statistical model that uses economic theory and data to estimate the relationships between economic variables.")

new("eddystone", "Eddystone is Google's open BLE beacon format.",
    "Eddystone", "standard",
    "An open Bluetooth Low Energy beacon format from Google that broadcasts identifiers and URLs.")

new("edius", "EDIUS is a video-editing application.",
    "EDIUS", "tool",
    "A non-linear video editing application from Grass Valley.")

new("educational-assessment", "A field within education.",
    "Educational assessment", "knowledge",
    "The process of gathering and interpreting evidence about what learners know and can do.")

new("educational-therapy", "An intervention practice for learning differences.",
    "Educational therapy", "skill",
    "Giving individualised, strategy-based help to learners with learning differences such as dyslexia or ADHD.")

new("eight-disciplines-problem-solving-8d", "8D is a structured team problem-solving method.",
    "Eight Disciplines problem solving", "method",
    "A structured team method, developed in the automotive industry, for finding the root cause of a recurring problem, fixing it and preventing it from returning.",
    variants=["8D"])

new("einstein-analytics", "A Salesforce analytics product.",
    "Einstein Analytics", "platform",
    "Salesforce's analytics and business-intelligence platform, later renamed Tableau CRM and then CRM Analytics.")

new("elastic-beanstalk", "AWS Elastic Beanstalk is an AWS service.",
    "AWS Elastic Beanstalk", "platform",
    "An Amazon Web Services service that deploys and scales web applications and handles provisioning, load balancing and monitoring.")

new("electric-meters", "Metering devices.",
    "Electric meters", "tool",
    "Instruments that measure the electrical energy used by a home, building or circuit.")

new("electric-vehicle", "A vehicle category, treated like the All-terrain vehicle entry.",
    "Electric vehicle", "tool",
    "A vehicle driven by one or more electric motors powered by a battery.")

new("electric-vehicle-infrastructure-training", "EVITP is a US training and certification programme for electricians.",
    "Electric Vehicle Infrastructure Training Program", "credential",
    "A US training and certification programme for electricians who install electric vehicle charging equipment.",
    variants=["EVITP"], cert=True, scope="single-issuer")

new("electrical-diagnostics-and-repairs", "A trade skill.",
    "Electrical diagnostics and repair", "skill",
    "Finding the cause of faults in electrical systems and equipment and fixing them.")

new("electrical-power-quality", "A standard electrical engineering topic.",
    "Electrical power quality", "knowledge",
    "How well the supply voltage and current stay within specified limits, including voltage sags, harmonics and interruptions.")

new("electrical-wirings", "A trade skill.",
    "Electrical wiring", "skill",
    "Installing and connecting electrical cables and devices in buildings and equipment.")

new("electro-mechanical-engineering", "An engineering discipline.",
    "Electromechanical engineering", "knowledge",
    "The branch of engineering that combines electrical and mechanical engineering to design devices such as motors, actuators and robots.",
    variants=["Electro-mechanical engineering"])

new("electron-microscope", "A laboratory instrument.",
    "Electron microscope", "tool",
    "A microscope that images specimens with a beam of electrons, reaching far higher magnification than a light microscope.")

new("electronic-article-surveillance", "A retail anti-theft technology.",
    "Electronic article surveillance", "knowledge",
    "Retail anti-theft technology in which tagged items set off an alarm when carried through detectors at an exit.")

new("electronic-data-capture", "The term is used for electronic collection of data, most often in clinical trials.",
    "Electronic data capture", "tool",
    "Collecting data directly into computer systems instead of on paper, most often in clinical trials using dedicated software.")

new("electronic-prescribing-erx", "E-prescribing is the electronic sending of prescriptions.",
    "Electronic prescribing", "skill",
    "Creating prescriptions on a computer and sending them electronically to a pharmacy.",
    variants=["e-prescribing", "eRx"])

new("electronic-publishing", "Digital publishing practice.",
    "Electronic publishing", "skill",
    "Producing and distributing books, journals and other content in digital formats.",
    variants=["e-publishing"])

new("electrosurgery", "A surgical technique.",
    "Electrosurgery", "method",
    "Using high-frequency electric current to cut, coagulate or destroy tissue during surgery.")

new("elixir-programming-language", "Elixir is a programming language.",
    "Elixir", "programming-language",
    "A dynamic, functional programming language that runs on the Erlang virtual machine.",
    lang="programming")

new("elk-stack", "The ELK stack is now officially called the Elastic Stack.",
    "Elastic Stack", "platform",
    "A set of tools from Elastic, originally Elasticsearch, Logstash and Kibana, used together to collect, search and visualise log and event data.")

new("email-etiquette", "A workplace communication skill.",
    "Email etiquette", "skill",
    "Writing and replying to email in a clear, courteous and appropriate way for the workplace.")

new("email-on-acid", "Email on Acid is an email testing service.",
    "Email on Acid", "tool",
    "A commercial service for previewing and testing how emails display across email clients and devices.")

new("email-service-providers", "A category of services.",
    "Email service providers", "tool",
    "Services that send, deliver and track bulk or transactional email for organisations, such as Mailchimp or SendGrid.")

new("email-software", "A software category, like Antivirus software.",
    "Email software", "tool",
    "Applications for composing, sending, receiving and organising email.")

new("embalming", "A funeral-service skill.",
    "Embalming", "skill",
    "Treating a dead body with preservative chemicals to delay decomposition and prepare it for viewing and burial.")

new("ember-js", "Ember.js is a JavaScript framework.",
    "Ember.js", "framework",
    "A JavaScript framework for building ambitious single-page web applications.",
    variants=["EmberJS"])

new("embroidery-machine-operation", "A manufacturing and craft skill.",
    "Embroidery machine operation", "skill",
    "Setting up and running machines that stitch designs into fabric.")

new("emergency-medical-responder", "EMR is the entry level of the US emergency medical services scope-of-practice model.",
    "Emergency Medical Responder", "credential",
    "An entry-level emergency medical care credential, below Emergency Medical Technician, for giving immediate lifesaving care until more advanced help arrives.",
    cert=True, scope="many-issuers")

new("emergency-nurse-pediatric-course-enpc", "ENPC is a course from the Emergency Nurses Association.",
    "Emergency Nurse Pediatric Course", "credential",
    "A pediatric emergency nursing course from the Emergency Nurses Association whose completion earns a provider card.",
    variants=["ENPC"], cert=True, scope="single-issuer")

new("emergency-procedure", "Emergency procedures are documented steps for emergencies.",
    "Emergency procedures", "knowledge",
    "The documented steps to follow when an emergency such as a fire, injury or equipment failure occurs.")

new("emergency-vehicle-operations", "EVOC is driver training for emergency responders.",
    "Emergency vehicle operations", "skill",
    "Driving ambulances, fire apparatus and police vehicles safely and quickly in emergency response.")

new("emission-calcuations", "Typo for emission calculations; a real environmental skill.",
    "Emission calculations", "skill",
    "Estimating the amount of pollutants or greenhouse gases a source releases, from activity data and emission factors.")

new("emotionally-stable", "Emotional stability is an enduring personal attribute.",
    "Emotional stability", "ability",
    "The tendency to stay calm and even-tempered under pressure.")

new("esg-analysis", "ESG analysis is an investment and corporate analysis skill.",
    "ESG analysis", "skill",
    "Evaluating how a company or investment performs on environmental, social and governance factors.",
    variants=["Environmental, social and governance analysis"])

# ---------------- write ----------------
reqs = sorted(os.path.basename(f)[:-5] for f in glob.glob("work/requests/*.json"))
missing = [s for s in reqs if s not in R]
extra = [s for s in R if s not in reqs]
assert not missing and not extra, (missing, extra)
os.makedirs("work/responses", exist_ok=True)
for s, a in R.items():
    json.dump(a, open(f"work/responses/{s}.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(R), Counter(a["decision"] for a in R.values()))
