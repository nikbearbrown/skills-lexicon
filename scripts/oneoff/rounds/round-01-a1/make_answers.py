import json, os, glob, sys
ROOT = "/home/user/rounds/round-01/a1/skills-lexicon/work"
GK = "general-knowledge"

def B(v):  # basis wrapper
    return {"value": v, "basis": GK}

def ns(reason):
    return {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def un(reason):
    return {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

def vo(target, reason):
    return {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}

def new(name, kind, definition, reason, variants=(), relations=(), verbs=(), cert=False, scope=None,
        lang=None, note=""):
    if kind.endswith("-language"):
        lang = lang or ("human" if kind == "human-language" else "programming")
    e = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": B(cert),
        "language_type": B(lang),
        "annotation_note": note,
    }
    if cert:
        e["certification_scope"] = B(scope)
    return {"decision": "new", "variant_of": None, "reason": reason, "entry": e}

A = {}
# nearest ids
ACNP, AGACNP, ATLS, AWS, ABMM, DRONE = "oaaan86zwe", "u0nv7nrdlk", "q9s4sj8gqa", "h00skqgqmn", "mbal4qqzlq", "ypvc3ra1n1"

A["adrenal-diseases-and-disorders-5e358a"] = ns("A group of medical conditions, not a skill; the skill would be diagnosing or treating them.")
A["adrenal-glands-4a5875"] = ns("An organ of the body, not a skill.")
A["adult-acute-care-nurse-practitioner-dccdc0"] = new(
    "Adult Acute Care Nurse Practitioner", "credential",
    "A nurse practitioner credential for caring for acutely ill adult patients.",
    "A nurse practitioner specialty credential, narrower than Acute Care Nurse Practitioner.",
    relations=[("broader", ACNP), ("related", AGACNP)], cert=True, scope="many-issuers")
A["adult-nurse-practitioner-d22422"] = new(
    "Adult Nurse Practitioner", "credential",
    "A nurse practitioner credential for providing primary care to adult patients.",
    "A nurse practitioner specialty credential for adult care.", cert=True, scope="many-issuers")
A["adult-trauma-life-support-db2495"] = un("I do not recognise a credential with this exact name; it may be a garbled Advanced Trauma Life Support, which I cannot confirm.")
A["advanced-automatic-collision-notificatio-6b3527"] = new(
    "Advanced Automatic Collision Notification", "knowledge",
    "Vehicle telematics that automatically alert emergency services after a crash and send data about how severe it was.",
    "A named vehicle-safety telematics technology that postings could ask for knowledge of.")
A["advanced-cardiovascular-life-support-acl-5482ba"] = new(
    "Advanced Cardiovascular Life Support", "credential",
    "A course and certification in the emergency treatment of cardiac arrest and other life-threatening cardiovascular conditions, developed by the American Heart Association.",
    "A well-known life-support certification; the legacy certification list is right.",
    variants=["ACLS", "Advanced Cardiac Life Support"], relations=[("related", ATLS)], cert=True, scope="single-issuer")
A["advanced-certified-fund-raising-executiv-92b055"] = new(
    "Advanced Certified Fund Raising Executive", "credential",
    "An advanced professional certification for senior fundraising executives.",
    "The ACFRE fundraising credential.", variants=["ACFRE"], cert=True, scope="single-issuer")
A["advanced-certified-hospice-and-palliativ-9ab7b1"] = new(
    "Advanced Certified Hospice and Palliative Nurse", "credential",
    "A certification for advanced practice nurses in hospice and palliative care, awarded by the Hospice and Palliative Credentialing Center.",
    "The ACHPN nursing credential.", variants=["ACHPN"], cert=True, scope="single-issuer")
A["advanced-individual-training-cd9b91"] = ns("A stage of US Army training, not a skill or a credential.")
A["advanced-logic-199537"] = un("Too vague to tell: it could mean advanced symbolic logic, digital logic design or something else.")
A["advanced-logic-research-5eca0d"] = ns("Advanced Logic Research was a personal-computer maker, so this is a company name.")
A["advanced-oncology-certified-clinical-nur-d262ce"] = new(
    "Advanced Oncology Certified Clinical Nurse Specialist", "credential",
    "A certification for clinical nurse specialists in oncology, awarded by the Oncology Nursing Certification Corporation.",
    "Looks like the truncated name of the AOCNS credential.", variants=["AOCNS"], cert=True, scope="single-issuer")
A["advanced-oncology-certified-nurse-practi-f4ae5c"] = new(
    "Advanced Oncology Certified Nurse Practitioner", "credential",
    "A certification for nurse practitioners in oncology, awarded by the Oncology Nursing Certification Corporation.",
    "The AOCNP nursing credential.", variants=["AOCNP"], cert=True, scope="single-issuer")
A["advanced-public-health-nursing-95acca"] = un("It could be a board certification in advanced public health nursing or just the nursing specialty, and the name alone does not say which.")
A["advanced-queuing-936ad8"] = new(
    "Oracle Advanced Queuing", "tool",
    "A message-queuing feature built into Oracle Database for passing messages between applications.",
    "Almost certainly Oracle's Advanced Queuing feature, though the tag omits the vendor.", variants=["Oracle AQ"])
A["advanced-state-of-networking-c4b584"] = un("I cannot tell what this names; it may be a course or a garbled phrase rather than a recognised skill.")
A["advertising-design-8c4c5b"] = new(
    "Advertising design", "skill",
    "Creating the visual look of advertisements, such as layouts, imagery and typography.",
    "A recognised design discipline.")
A["advocacy-b8c612"] = un("A broad word covering policy, patient, client and other advocacy, and the tag does not say which sense is meant.")
A["aerial-lift-certification-bd4d14"] = new(
    "Aerial lift certification", "credential",
    "A certificate showing that a person has been trained to operate aerial lifts such as boom lifts and scissor lifts.",
    "An operator-training credential; the legacy certification list is right.",
    variants=["Aerial lift operator certification"], cert=True, scope="many-issuers")
A["aerospace-industries-ec11c9"] = ns("An industry, not a skill.")
A["aerospike-63bb46"] = new(
    "Aerospike Database", "tool",
    "A distributed NoSQL database built for fast, large-scale key-value access.",
    "The Aerospike database product, which is the usual meaning in job postings.", verbs=["query"])
A["aesthetics-e041e1"] = un("Ambiguous: it could be the branch of philosophy, cosmetic skin-care work or visual appearance in design.")
A["affordable-housing-manager-certification-9a2867"] = un("The name suggests a credential for managers of affordable housing, but I cannot identify which body or credential it refers to.")
A["ageing-0b4f42"] = ns("A life process, not a skill; the related field would be gerontology.")
A["agile-certified-practitioner-c955a5"] = new(
    "PMI Agile Certified Practitioner", "credential",
    "A Project Management Institute certification for practitioners of agile approaches such as Scrum, Kanban and Lean.",
    "Most likely the PMI-ACP credential, which the legacy lists do not call a certification.",
    variants=["PMI-ACP"], cert=True, scope="single-issuer")
A["agile-software-development-f6f3ca"] = new(
    "Agile software development", "method",
    "An approach to building software in short iterative cycles with frequent feedback and close collaboration.",
    "A well-known software development method.", variants=["Agile development"])
A["agricultural-machinery-41c95c"] = new(
    "Agricultural machinery", "tool",
    "Machines used in farming, such as tractors, combine harvesters, ploughs and seed drills.",
    "A class of equipment that postings ask people to operate or maintain.")
A["agricultural-modeling-and-training-syste-d4ab67"] = un("It looks like a company or training-product brand rather than a skill, but I cannot confirm.")
A["agrochemical-984361"] = ns("A class of substances, not a skill.")
A["aids-certified-registered-nurse-e955cf"] = new(
    "AIDS Certified Registered Nurse", "credential",
    "A nursing certification for registered nurses who care for people with HIV and AIDS.",
    "The ACRN nursing credential.", variants=["ACRN"], cert=True, scope="single-issuer")
A["ainu-language-4824c9"] = new(
    "Ainu", "human-language",
    "A critically endangered language of the Ainu people of northern Japan.",
    "A human language; the legacy language list is right.", variants=["Ainu language"])
A["air-flow-tests-0172f9"] = un("Several fields test airflow (ductwork, wind tunnels, breathing), and the tag does not say which.")
A["air-pollutions-e15e2f"] = ns("A phenomenon, not a skill.")
A["air-routing-international-47dfff"] = ns("Air Routing International is an aviation trip-support company, so this is a company name.")
A["air-travel-organiser-s-licensing-432e10"] = new(
    "Air Travel Organisers' Licensing", "standard",
    "A UK Civil Aviation Authority scheme that requires travel businesses selling flight-inclusive packages to hold a licence that protects customers' money.",
    "A UK licensing regulation (ATOL); the licences are held by businesses, so the scheme itself is not a personal certification.",
    variants=["ATOL"])
A["airbox-632b82"] = un("Airbox names several unrelated things (a vehicle intake part, consumer devices), and the tag gives no way to choose.")
A["airline-transport-pilot-certificate-atp-77ee17"] = new(
    "Airline Transport Pilot certificate", "credential",
    "The highest-level pilot certificate issued by the US Federal Aviation Administration, required for airline captains.",
    "An FAA pilot certificate.", variants=["ATP certificate"], relations=[("related", DRONE)],
    cert=True, scope="single-issuer")
A["airworthiness-engineering-750280"] = new(
    "Airworthiness engineering", "knowledge",
    "Engineering that demonstrates and maintains that an aircraft meets the requirements for safe flight.",
    "A recognised aerospace engineering field.")
A["ajax-programming-language-2a30c6"] = un("Ajax is a web technique, not a programming language, and it matches an existing Ajax entry (k5f5yj60ou) that was not in this request's nearest list, so I cannot name it as variant_of.")
A["akan-language-f0659e"] = new(
    "Akan", "human-language",
    "A language spoken mainly in Ghana, with varieties such as Twi and Fante.",
    "A human language; the legacy language list is right.", variants=["Akan language"])
A["alasset-1c16ed"] = un("I do not know what Alasset is.")
A["aldus-photostyler-976cc0"] = new(
    "Aldus PhotoStyler", "tool",
    "A discontinued Windows image-editing program first released by Aldus.",
    "A named, now discontinued, software product.")
A["alembics-8eade6"] = un("The plural of alembic, a distillation apparatus; it is unclear what skill is meant.")
A["alexa-actionable-analytics-for-the-web-6c1070"] = new(
    "Alexa Internet", "tool",
    "Amazon's web-traffic analytics and site-ranking service, which was shut down in 2022.",
    "The Alexa web-analytics service, not the Amazon voice assistant.")
A["algebraic-logic-functional-programming-l-1c3a45"] = new(
    "Algebraic Logic Functional", "programming-language",
    "A programming language that combines functional and logic programming.",
    "A research programming language (ALF).")
A["alibaba-cloud-e69cb7"] = new(
    "Alibaba Cloud", "platform",
    "The cloud-computing services of Alibaba Group.",
    "A named cloud platform.", variants=["Aliyun"], verbs=["deploy"])
A["alienvault-64ada2"] = new(
    "AlienVault", "tool",
    "Security-monitoring software, notably the USM and OSSIM products, from the company later acquired by AT&T.",
    "A security product family; the tag could also name the company.")
A["alkalinity-f987d1"] = ns("A chemical property, not a skill.")
A["all-terrain-vehicle-044696"] = new(
    "All-terrain vehicle", "tool",
    "A motorised off-road vehicle with low-pressure tyres, designed for rough terrain.",
    "A class of vehicle that postings may ask people to operate.")
A["all-terrain-vehicle-atv-certification-d980a1"] = new(
    "All-terrain vehicle certification", "credential",
    "A certificate showing completion of rider-safety training for operating all-terrain vehicles.",
    "A rider-training credential; the legacy certification list is right.",
    variants=["ATV certification"], cert=True, scope="many-issuers")
A["allergen-labelling-049b99"] = new(
    "Allergen labelling", "skill",
    "Declaring the allergens in food products on packaging or menus as the law requires.",
    "A food-safety and compliance task.")
A["alljoyn-48b889"] = new(
    "AllJoyn", "framework",
    "An open-source software framework for discovering and communicating between nearby connected devices, originally from Qualcomm.",
    "A named IoT framework.")
A["alloyui-dfff2b"] = new(
    "AlloyUI", "framework",
    "A JavaScript user-interface framework from Liferay, built on YUI and Bootstrap.",
    "A named front-end framework.")
A["allyship-af1205"] = new(
    "Allyship", "skill",
    "Actively supporting the inclusion and rights of groups one does not belong to, for example by speaking up and sharing opportunities.",
    "A workplace practice that postings ask for.")
A["alooma-cb224b"] = new(
    "Alooma", "tool",
    "A cloud service for building data pipelines that move data from many sources into data warehouses, acquired by Google in 2019.",
    "A named data-integration product.")
A["alt-js-41f0b7"] = un("It could be the Alt Flux library for React or a reference to altJS languages that compile to JavaScript.")
A["alterations-1acf2c"] = new(
    "Garment alterations", "skill",
    "Adjusting finished garments, for example by hemming or taking them in or out, so they fit a customer.",
    "Almost certainly the tailoring sense, though the tag is a single generic word.",
    variants=["Clothing alterations"])
A["alternative-dispute-resolution-dcec79"] = new(
    "Alternative dispute resolution", "method",
    "Ways of settling disputes without a court trial, such as mediation and arbitration.",
    "A recognised legal and workplace method.")
A["alternative-lending-de39d7"] = ns("An industry segment (non-bank lending), not a skill.")
A["alternative-transients-program-2ff810"] = new(
    "Alternative Transients Program", "tool",
    "Simulation software for electromagnetic transients in electrical power systems, derived from the EMTP.",
    "A named power-systems simulation program.", variants=["ATP-EMTP"])
A["aluminium-smelting-5c07bc"] = new(
    "Aluminium smelting", "method",
    "The industrial process of making aluminium metal from alumina by electrolysis in a molten bath.",
    "An industrial production process.")
A["alzheimer-s-disease-cf9593"] = ns("A medical condition, not a skill; the skill would be caring for or treating patients with it.")
A["amalgam-4deec4"] = un("Ambiguous: it could be dental amalgam, a mercury alloy or something else, and the tag does not say.")
A["amazon-appstream-95ab8f"] = new(
    "Amazon AppStream 2.0", "tool",
    "An Amazon Web Services service that streams desktop applications from AWS to a user's web browser.",
    "A named AWS service; the original AppStream was an earlier version of the same line.")
A["amazon-emr-321dd8"] = new(
    "Amazon EMR", "tool",
    "An Amazon Web Services service for running big-data frameworks such as Apache Spark and Hadoop on managed clusters.",
    "A named AWS service.", variants=["Amazon Elastic MapReduce", "AWS EMR"], relations=[("part_of", AWS)])
A["amazon-kindle-fire-f22d16"] = new(
    "Amazon Fire tablet", "platform",
    "Amazon's line of Android-based tablets, sold as the Kindle Fire when first launched in 2011.",
    "A hardware and software platform; the tag uses the older product name.", variants=["Kindle Fire"])
A["amazon-simpledb-e213fd"] = new(
    "Amazon SimpleDB", "tool",
    "An Amazon Web Services non-relational database service that stores items made of attributes without a fixed schema.",
    "A named AWS service.", variants=["AWS SimpleDB"], relations=[("part_of", AWS)], verbs=["query"])
A["ambari-e2a464"] = new(
    "Apache Ambari", "tool",
    "An Apache project for provisioning, managing and monitoring Hadoop clusters.",
    "A named Apache project.", verbs=["manage"])
A["amcharts-3f3db3"] = new(
    "amCharts", "library",
    "A JavaScript library for building interactive charts and maps.",
    "A named charting library.")
A["america-s-labor-market-information-syste-28c4f6"] = un("It looks like a US Department of Labor data programme, and it is unclear whether it is meant as a tool or a topic of knowledge.")
A["american-board-of-medical-microbiology-a-45a08d"] = vo(ABMM, "The same certification as the existing American Board of Medical Microbiology entry, which already lists ABMM Certified.")
A["american-board-of-neurophysiologic-monit-b85b25"] = new(
    "American Board of Neurophysiologic Monitoring certification", "credential",
    "Certification by the American Board of Neurophysiologic Monitoring in intraoperative neurophysiologic monitoring.",
    "A board certification; the legacy list is right, and the tag is the board's name used for its credential.",
    cert=True, scope="single-issuer")
A["american-board-of-optometry-certified-dc3c70"] = new(
    "American Board of Optometry certification", "credential",
    "Board certification awarded by the American Board of Optometry to optometrists who show advanced knowledge and clinical skill.",
    "A board certification; the legacy list is right.", cert=True, scope="single-issuer")
A["american-board-of-optometry-ecb3fd"] = new(
    "American Board of Optometry certification", "credential",
    "Board certification awarded by the American Board of Optometry to optometrists who show advanced knowledge and clinical skill.",
    "The bare board name in a skills list stands for its certification, the same concept as 'American Board Of Optometry Certified'.",
    cert=True, scope="single-issuer")
A["american-board-of-pathology-certificatio-9cd689"] = new(
    "American Board of Pathology certification", "credential",
    "Board certification awarded by the American Board of Pathology to pathologists in anatomic, clinical and other pathology specialties.",
    "A board certification; the legacy list is right.", variants=["ABPath certification"], cert=True, scope="single-issuer")
A["american-culinary-federation-3c1206"] = new(
    "American Culinary Federation certification", "credential",
    "Professional certifications for cooks and chefs awarded by the American Culinary Federation, at several levels up to Certified Master Chef.",
    "The tag names the federation; the credential family is what a posting would ask for.",
    variants=["ACF certification"], cert=True, scope="single-issuer")
A["american-medical-technologists-3645d9"] = new(
    "American Medical Technologists certification", "credential",
    "Certifications awarded by American Medical Technologists to allied health professionals such as medical technologists, medical assistants and phlebotomists.",
    "The tag names the certifying body; the credential family is what a posting would ask for.",
    variants=["AMT certification"], cert=True, scope="single-issuer")
A["american-nuclear-society-7c27c0"] = ns("A professional society, i.e. an organisation, not a skill or credential.")
A["american-osteopathic-board-of-nuclear-me-7ba1ff"] = new(
    "American Osteopathic Board of Nuclear Medicine certification", "credential",
    "Board certification in nuclear medicine awarded by the American Osteopathic Board of Nuclear Medicine to osteopathic physicians.",
    "A board certification; the legacy list is right.", variants=["AOBNM certification", "AOBNM"],
    cert=True, scope="single-issuer")
A["american-production-and-inventory-contro-612af5"] = new(
    "ASCM certification", "credential",
    "Supply-chain and operations-management certifications, such as CPIM and CSCP, awarded by the Association for Supply Chain Management, formerly APICS.",
    "APICS is now ASCM; the legacy list is right.", variants=["APICS certification", "APICS certified"],
    cert=True, scope="single-issuer")
A["american-safety-health-associates-90b662"] = ns("An organisation name, not a skill.")
A["american-sign-language-4f4f3b"] = new(
    "American Sign Language", "human-language",
    "A sign language used mainly by Deaf communities in the United States and English-speaking Canada.",
    "A human (signed) language; the legacy language list is right.")
A["american-society-of-pension-professional-76e959"] = new(
    "American Society of Pension Professionals and Actuaries certification", "credential",
    "Retirement-plan credentials, such as the Qualified Pension Administrator and Qualified 401(k) Administrator, awarded by ASPPA, which is part of the American Retirement Association.",
    "The tag names the certifying body; the credential family is what a posting would ask for.",
    variants=["ASPPA certification", "ASPPA"], cert=True, scope="single-issuer")
A["american-traffic-safety-services-associa-fed3bd"] = new(
    "ATSSA certification", "credential",
    "Traffic-control and roadway-safety certificates, such as flagger and traffic control technician, awarded by the American Traffic Safety Services Association.",
    "A credential family from one body; the legacy list is right.",
    variants=["ATSSA certificate", "American Traffic Safety Services Association certificate"],
    cert=True, scope="single-issuer")
A["american-welding-society-certification-60033a"] = new(
    "American Welding Society certification", "credential",
    "Welding-related certifications awarded by the American Welding Society, such as Certified Welder and Certified Welding Inspector.",
    "A credential family from one body; the legacy list is right.", cert=True, scope="single-issuer")
A["american-welding-society-codes-77d724"] = new(
    "American Welding Society codes", "standard",
    "The welding codes and standards published by the American Welding Society, such as AWS D1.1 for structural steel.",
    "Published welding standards, not a credential.")
A["amiga-personal-computers-7dee13"] = new(
    "Amiga", "platform",
    "A line of personal computers launched by Commodore in 1985, known for its graphics and sound.",
    "A named computer platform.")
A["amino-acid-0b45c8"] = ns("A class of molecules, not a skill.")
A["amplifyjs-491ca7"] = un("It could be the AmplifyJS utility library or AWS Amplify's JavaScript library, and the tag does not say which.")
A["amplitude-modulation-signalling-systems-cb319b"] = un("It is probably the AM Signalling System standard for data on AM radio, but I am not certain.")
A["anaconda-software-d699e9"] = new(
    "Anaconda", "tool",
    "A distribution of Python and R with a package and environment manager, aimed at data science.",
    "Most likely the Anaconda data-science distribution, though another software product shares the name.")
A["analogue-electronics-dcd2fe"] = new(
    "Analogue electronics", "knowledge",
    "Electronics that works with continuously varying signals rather than digital ones, as in amplifiers and filters.",
    "A standard electronics field.", variants=["Analog electronics"])
A["analysis-of-variance-4c08fc"] = new(
    "Analysis of variance", "method",
    "A statistical method that tests whether the means of several groups differ by comparing variation between and within the groups.",
    "A standard statistical method.", variants=["ANOVA"])
A["analytical-dashboard-aef326"] = ns("A kind of report or user-interface output, not a skill; the skill would be building dashboards.")
A["analytics-js-8f6c4f"] = un("Two different libraries share this name, Segment's analytics.js and the Google Analytics analytics.js.")
A["anam-language-14c731"] = un("Several small languages have similar names, and I cannot say with confidence which one 'Anam' means.")
A["anaplan-c36d97"] = new(
    "Anaplan", "platform",
    "A cloud platform for business planning, forecasting and modelling.",
    "A named planning platform.")
A["anchoring-8dbc77"] = ns("A generic word with unrelated senses (a cognitive bias, a negotiating tactic, rigging, news presenting), not one skill.")
A["ancient-history-9555f0"] = new(
    "Ancient history", "knowledge",
    "The study of human history from the earliest written records to the end of antiquity.",
    "A school and university subject.")

reqs = sorted(os.path.basename(f)[:-5] for f in glob.glob(ROOT + "/requests/*.json"))
missing = [r for r in reqs if r not in A]
extra = [k for k in A if k not in reqs]
print("requests", len(reqs), "answers", len(A), "missing", missing, "extra", extra)
if missing or extra:
    sys.exit(1)
os.makedirs(ROOT + "/responses", exist_ok=True)
for k, v in A.items():
    with open(f"{ROOT}/responses/{k}.json", "w", encoding="utf-8") as fh:
        json.dump(v, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
import collections
print(collections.Counter(v["decision"] for v in A.values()))
