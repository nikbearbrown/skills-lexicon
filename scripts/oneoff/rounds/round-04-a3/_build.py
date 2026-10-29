import json, glob, os, sys

GK = "general-knowledge"
A = {}  # term -> answer dict


def ann(cert=False, scope=None, lang=None):
    d = {"certification": {"value": cert, "basis": GK}}
    if cert:
        d["certification_scope"] = {"value": scope, "basis": GK}
    d["language_type"] = {"value": lang, "basis": GK}
    return d


def new(term, name, kind, definition, variants=(), relations=(), cert=False, scope=None, lang=None, reason=None):
    entry = {
        "preferred_name": name,
        "kind": kind,
        "definition": definition,
        "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
        "verbs": [],
    }
    entry.update(ann(cert, scope, lang))
    A[term] = {"decision": "new", "variant_of": None, "reason": reason or "A recognised skill or body of knowledge that is not among the nearest entries.", "entry": entry}


def nas(term, reason):
    A[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(term, reason):
    A[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def variant(term, target, reason):
    A[term] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


new("Employee Relations", "Employee relations", "skill",
    "Managing the relationship between an employer and its workforce, including handling grievances, conduct issues and communication.")

new("Employee Relations Investigations", "Employee relations investigations", "skill",
    "Investigating workplace complaints and suspected misconduct, such as harassment or policy breaches, to establish the facts and recommend action.",
    relations=[("related", "x5fnpmr8pm")])

new("Employer Branding", "Employer branding", "skill",
    "Shaping and promoting how an organisation is seen as a place to work, in order to attract and keep employees.",
    relations=[("broader", "gxe2qfkmua")])

new("Employment Compliance", "Employment compliance", "skill",
    "Making sure an organisation follows employment laws and regulations, such as those on pay, working hours and discrimination.")

unsure("Empower", "Empower could be a chromatography data software product, a retirement-services brand or the ordinary verb, and there are no quotes to tell which.")

new("Ems Dispatch", "EMS dispatch", "skill",
    "Taking emergency calls and sending and coordinating ambulances and other emergency medical services.")

unsure("Encompass", "Encompass names several unrelated products and companies (for example a mortgage loan origination system), and nothing here shows which one is meant.")

new("Encounter Data Management", "Encounter data management", "skill",
    "Collecting, checking and submitting the records of healthcare visits and services, such as the encounter data that health plans report to government programs.")

new("Endevor", "Endevor", "tool",
    "Software configuration management tool, from CA and now Broadcom, for controlling changes to source code and other components on mainframe systems.",
    variants=["CA Endevor"])

unsure("Endo (Language)", "I cannot confidently identify which language or dialect is called Endo, and the name may refer to more than one.")

new("Endocannabinoid System", "Endocannabinoid system", "knowledge",
    "The network of cannabinoid receptors and naturally made cannabinoid-like molecules in the body that helps regulate functions such as mood, appetite, pain and sleep.")

new("Endocrine Disorders", "Endocrine disorders", "knowledge",
    "Medical knowledge of conditions caused by hormone-producing glands working abnormally, such as diabetes and thyroid disease.")

new("Endodontics", "Endodontics", "knowledge",
    "The dental specialty concerned with diseases of the tooth pulp and the tissues around the tooth root, including root canal treatment.")

new("Endotracheal Suctioning", "Endotracheal suctioning", "skill",
    "Clearing secretions from the airway of a patient with an endotracheal tube by passing a suction catheter through the tube.")

new("EndoVasculars Aneurysm Repair", "Endovascular aneurysm repair", "skill",
    "A minimally invasive procedure that repairs an aortic aneurysm by placing a stent graft inside the vessel through small incisions in the groin.",
    variants=["EVAR"])

new("Endpoint Detection and Response", "Endpoint detection and response", "tool",
    "Security software that continuously monitors computers and other endpoints for suspicious activity and helps investigate and respond to threats.",
    variants=["EDR"])

nas("Endpoint Devices", "A category of hardware (computers, phones and the like), not a skill or a named product.")

new("Endpoint Engineering", "Endpoint engineering", "skill",
    "Designing, deploying and maintaining the configuration, software and security controls of an organisation's end-user devices such as laptops and phones.")

new("Endpoint Management", "Endpoint management", "skill",
    "Configuring, patching, monitoring and securing the end-user devices of an organisation from a central point.",
    relations=[("related", "yapu6om8hs")])

new("Endpoint Security", "Endpoint security", "skill",
    "Protecting end-user devices such as laptops, servers and phones from malware, intrusion and data loss.",
    relations=[("broader", "norpz7ekiw")])

new("Enemas", "Enema administration", "skill",
    "Giving a patient fluid through the rectum to empty the bowel or to deliver medicine.")

new("Energy Control Procedures", "Energy control procedures", "method",
    "Written steps for shutting down, isolating and locking out the hazardous energy sources of a machine before anyone services it.")

unsure("Energy Design Resources", "This looks like the name of a program or website rather than a skill, but I cannot confirm that from the name alone.")

new("Energy System Transition", "Energy system transition", "knowledge",
    "The shift of energy production and use from fossil fuels to low-carbon and renewable sources.")

variant("Engelska", "tsdlbd9gt0", "Engelska is the Swedish word for English, so it names the same language as the English entry.")

new("Engineer in Training", "Engineer in Training", "credential",
    "A US designation given by a state licensing board to a graduate engineer who has passed the Fundamentals of Engineering exam, the first step toward a Professional Engineer licence.",
    variants=["EIT", "Engineer Intern"], cert=True, scope="many-issuers")

new("Engineered Materials Arrestor Systems", "Engineered materials arrestor system", "knowledge",
    "A runway-end safety system of crushable concrete blocks that slows and stops an aircraft that overruns the runway.")

new("Engineering Drawing", "Engineering drawing", "skill",
    "Preparing or reading technical drawings that follow standard conventions to show the shape, dimensions and tolerances of parts and assemblies.",
    relations=[("related", "rbg0r9t749")])

new("Engineering Economics", "Engineering economics", "knowledge",
    "The application of economic analysis, such as cost-benefit comparison, present worth and break-even analysis, to engineering decisions.")

new("Engineering Education", "Engineering education", "knowledge",
    "The teaching of engineering and the study of how engineering is best learned.")

new("Engineering Mathematics", "Engineering mathematics", "knowledge",
    "The mathematics, such as calculus, linear algebra and differential equations, used to model and solve engineering problems.")

nas("Engineering, Other", "A residual category label from a classification scheme, not a skill.")

new("Engineering Statics", "Engineering statics", "knowledge",
    "The branch of mechanics that analyses the forces on structures and bodies that are at rest.")

new("Engineering Statistics", "Engineering statistics", "knowledge",
    "The use of statistical methods, such as design of experiments, reliability analysis and quality control, to solve engineering problems.",
    relations=[("broader", "ww4glmysl2")])

new("Enhanced Data GSM Environment", "Enhanced Data rates for GSM Evolution", "standard",
    "A mobile data technology that raises data rates on GSM networks, often called 2.75G.")

new("Enhanced Prudential Standards", "Enhanced prudential standards", "standard",
    "US Federal Reserve rules, required by the Dodd-Frank Act, that set stricter capital, liquidity and risk-management requirements for large bank holding companies.")

new("Enhanced Security Check (eSC)", "Enhanced Security Check (eSC) clearance", "credential",
    "A UK government security clearance level that adds further checks to the Security Check (SC) level.",
    variants=["eSC"], relations=[("related", "b01cze4ssf")], cert=True, scope="single-issuer")

new("EnodeB", "eNodeB", "knowledge",
    "The base station in a 4G LTE radio network that connects mobile devices to the core network.",
    variants=["eNB", "evolved Node B"])

new("Enscape (VR Rendering Software)", "Enscape", "tool",
    "Real-time rendering and virtual-reality software that works inside architectural design programs such as Revit and SketchUp.")

new("Ensemble Conducting", "Ensemble conducting", "skill",
    "Directing a group of musicians, such as an orchestra, band or choir, in rehearsal and performance by setting tempo, giving cues and shaping the interpretation.")

new("Ensemble Methods", "Ensemble methods", "method",
    "Machine learning techniques that combine the predictions of several models, as in bagging, boosting and stacking, to get a more accurate result.",
    variants=["Ensemble learning"])

unsure("Enterprise Application Platform", "This may be the generic category of application servers or Red Hat's JBoss Enterprise Application Platform, and there are no quotes to tell which.")

unsure("Enterprise Data Headers", "I do not know what this term refers to.")

new("Enterprise Integration", "Enterprise integration", "skill",
    "Connecting an organisation's separate applications and data sources so that they exchange data and work together.")

new("Enterprise Network Security", "Enterprise network security", "skill",
    "Protecting an organisation's networks and the systems on them from attack, misuse and unauthorised access.",
    relations=[("broader", "norpz7ekiw")])

new("Enterprise Performance Management (EPM)", "Enterprise performance management", "method",
    "The processes and software an organisation uses to plan, budget, forecast and report on its financial and operating performance.",
    variants=["EPM", "Corporate performance management"])

new("Enterprisedb", "EnterpriseDB", "tool",
    "A commercial database product, built on PostgreSQL with added enterprise features and Oracle compatibility, from the company EnterpriseDB (EDB).",
    )

nas("Enthusiastic Worker", "A personal trait or description, not a skill.")

nas("Entrepreneurial Cultures", "A description of a type of workplace culture, not a skill.")

new("Entrepreneurial Operating System (EOS)", "Entrepreneurial Operating System", "method",
    "A business management system from Gino Wickman, set out in the book Traction, that organises a company around vision, people, data, issues, process and traction.")

new("Environmental Anthropology", "Environmental anthropology", "knowledge",
    "The study of the relationships between human societies and their natural environments.")

new("Environmental Finance", "Environmental finance", "knowledge",
    "The area of finance concerned with environmental issues, such as carbon markets, green bonds and funding for conservation and clean energy.")

new("Environmental Impact Statement", "Environmental impact statement preparation", "skill",
    "Researching and writing the report, such as one required under the US National Environmental Policy Act, that assesses the significant environmental effects of a proposed project.")

new("Environmental Journalism", "Environmental journalism", "skill",
    "Reporting and writing news about the environment, climate and natural resources.")

new("Environmental Scanning", "Environmental scanning", "method",
    "Systematically gathering and analysing information about external trends, competitors and events that could affect an organisation's strategy.")

unsure("Environmental Security", "It could mean environmental change as a security issue, or the physical protection of a site's environmental conditions, and nothing here shows which.")

new("Environmental Social And Governance (ESG) Issues", "Environmental, social and governance", "knowledge",
    "The environmental, social and governance factors used to judge how sustainable and ethical an organisation's conduct is.",
    variants=["ESG"])

new("Enzyme Aanlysis", "Enzyme analysis", "skill",
    "Measuring the activity or amount of enzymes in a sample, for example to study a reaction or to help diagnose disease.",
    reason="A misspelling of enzyme analysis, which is a laboratory skill not among the nearest entries.")

new("Enzyme-Linked Immunosorbent Assay (ELISA)", "Enzyme-linked immunosorbent assay", "method",
    "A laboratory test that uses antibodies linked to an enzyme to detect and measure a substance, such as a protein or hormone, in a sample.",
    variants=["ELISA"])

new("Epic Asap", "Epic ASAP", "tool",
    "The emergency department module of Epic Systems' electronic health record software.")

new("Epic Beacon", "Epic Beacon", "tool",
    "The oncology module of Epic Systems' electronic health record software, used to plan and document cancer treatment such as chemotherapy.")

new("Epic Willow", "Epic Willow", "tool",
    "The pharmacy module of Epic Systems' electronic health record software, covering medication orders, verification and dispensing.")

new("Epinephrine Administration", "Epinephrine administration", "skill",
    "Giving epinephrine (adrenaline) to a patient, for example to treat a severe allergic reaction or in cardiac arrest.")

unsure("Equalization", "It could mean audio or signal equalization, pay or tax equalization, or something else, and there are no quotes to tell which.")

new("Equipment Design", "Equipment design", "skill",
    "Designing machines, apparatus or process equipment so that they meet functional, safety and manufacturing requirements.")

new("Equipment Engineering", "Equipment engineering", "skill",
    "Engineering work to specify, install, maintain and improve the machines and equipment used in production.")

new("Equities", "Equities", "knowledge",
    "Securities that represent ownership in a company, and the markets where they are bought and sold.")

new("Ergonomic Assessments", "Ergonomic assessment", "skill",
    "Evaluating workstations, tasks and equipment for factors that can cause strain or injury, and recommending changes.")

new("Erikson'S Stages Of Psychosocial Development", "Erikson's stages of psychosocial development", "knowledge",
    "Erik Erikson's theory that a person passes through eight life stages, each marked by a psychological conflict to resolve.")

nas("Error Message", "A user-interface element, not a skill.")

new("Erwin (Data Modeling Software)", "erwin Data Modeler", "tool",
    "Software for designing, documenting and generating database structures, originally ERwin and now sold by Quest Software.",
    variants=["ERwin", "CA ERwin"], relations=[("related", "pgwo2h5tp6")])

new("Es2015", "ECMAScript 2015", "programming-language",
    "The 2015 edition of the ECMAScript standard on which JavaScript is based, which added classes, modules, arrow functions and promises.",
    variants=["ES6", "ECMAScript 6"], lang="programming")

new("Estate Valuation", "Estate valuation", "skill",
    "Working out the value of the property and other assets of a deceased person's estate, for example for probate or tax.")

nas("Estimators", "A job title (people who estimate costs), not a skill.")

new("Ethical AI", "Ethical AI", "knowledge",
    "Designing, building and using artificial intelligence systems in ways that are fair, transparent, accountable and respectful of human rights.")

nas("Ethical Conduct", "A general expectation of behaviour rather than a developed skill or a specific body of knowledge.")

new("Etiology", "Etiology", "knowledge",
    "The study of the causes of diseases and other conditions.")

new("European Computing Driving Licence (ECDL)", "International Computer Driving Licence", "credential",
    "An entry-level computer skills certification, earlier known as the European Computer Driving Licence, awarded after tests at approved centres under the ICDL Foundation.",
    variants=["ICDL", "ECDL", "European Computer Driving Licence"], cert=True, scope="single-issuer")

new("Evaluate Food Palatability", "Food palatability evaluation", "skill",
    "Judging how acceptable food is to eat in terms of taste, texture, smell and appearance.")

new("Evaluate Information", "Information evaluation", "skill",
    "Judging the accuracy, relevance and reliability of information and its sources.")

new("Event Sponsorships", "Event sponsorship", "skill",
    "Finding and managing companies that fund or support an event in return for promotion of their brand.")

unsure("Event Tracing (Software)", "It could be the general technique of recording events as software runs or Event Tracing for Windows, and there are no quotes to tell which.")

new("Evidence Collection", "Evidence collection", "skill",
    "Gathering, documenting and preserving physical or digital evidence for an investigation or legal case.")

new("Ewondo (Language)", "Ewondo", "human-language",
    "A Bantu language spoken by the Beti people of central Cameroon, around Yaoundé.",
    lang="human")

unsure("Exact Sciences", "It could be the company of that name or the general phrase for the quantitative sciences such as mathematics and physics, and nothing here shows which.")

new("Examination Of Legal Documents", "Examination of legal documents", "skill",
    "Reading legal documents such as contracts, deeds and filings to check that they are accurate, complete and valid.")

new("Excel Pivot Tables", "Excel PivotTables", "skill",
    "Using the PivotTable feature of Microsoft Excel to summarise, group and analyse large tables of data.")

new("Excel Pivot Tables And Charts", "Excel PivotTables and PivotCharts", "skill",
    "Using the PivotTable and PivotChart features of Microsoft Excel to summarise data and show the results in charts.")

new("Excess Return", "Excess return", "knowledge",
    "The return on an investment above that of a benchmark or the risk-free rate.")

new("Excision of Skin Lesions", "Excision of skin lesions", "skill",
    "Surgically cutting out a skin lesion, such as a mole, cyst or skin cancer, usually with a margin of healthy tissue.")

nas("Execute Plans", "A generic phrase for carrying out plans, not a specific skill.")

new("Executive Presentations", "Executive presentations", "skill",
    "Preparing and giving short, focused presentations to senior leaders so that they can make decisions.")

new("Executive Protection", "Executive protection", "skill",
    "Protecting senior executives and other high-profile people from harm through security planning, advance work and close protection.")

new("Executive Relationship Management", "Executive relationship management", "skill",
    "Building and maintaining working relationships with senior executives of customers, partners or the organisation itself.")

new("Executive Search", "Executive search", "skill",
    "Finding, assessing and recruiting candidates for senior leadership roles, usually on behalf of a client organisation.")

nas("Executive Summary", "A section of a report, not a skill.")

new("Expanded Functions Dental Assistant", "Expanded Functions Dental Assistant", "credential",
    "A state-recognised credential that lets a dental assistant do extra tasks, such as placing and finishing restorations, under a dentist's supervision.",
    variants=["EFDA", "Expanded Function Dental Assistant"], cert=True, scope="many-issuers")

new("Expectancy Theory", "Expectancy theory", "knowledge",
    "Victor Vroom's theory that people choose how to act according to what they expect the outcome to be and how much they value it.",
    variants=["Vroom's expectancy theory"])

new("Experiential Marketing", "Experiential marketing", "skill",
    "Marketing that engages customers through live, immersive brand experiences such as events and pop-up shops.")

new("Explosive Detection", "Explosive detection", "skill",
    "Finding hidden explosives using methods such as trained dogs, trace detectors and screening equipment.")


def main():
    files = sorted(glob.glob("work/requests/*.json"))
    terms = {}
    for f in files:
        r = json.load(open(f))
        terms[os.path.basename(f)] = r
    missing = [r["term"] for r in terms.values() if r["term"] not in A]
    extra = [t for t in A if t not in {r["term"] for r in terms.values()}]
    if missing or extra:
        print("missing", missing, "extra", extra)
        sys.exit(1)
    os.makedirs("work/responses", exist_ok=True)
    for name, r in terms.items():
        json.dump(A[r["term"]], open(os.path.join("work/responses", name), "w"), indent=1, ensure_ascii=False)
        open(os.path.join("work/responses", name), "a").write("\n")
    from collections import Counter
    print(len(terms), Counter(a["decision"] for a in A.values()))


main()
