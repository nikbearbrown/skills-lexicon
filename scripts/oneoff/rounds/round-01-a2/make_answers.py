"""Scratch script: builds the 100 draft answers and writes them to work/responses/. Not part of the dictionary."""
import glob
import json
import os
from collections import Counter

ROOT = "/home/user/rounds/round-01/a2/skills-lexicon"
GK = "general-knowledge"
A = {}


def new(stem, name, kind, definition, variants=(), relations=(), verbs=(), cert=False, scope=None,
        lang=None, reason="A recognisable skill, tool or field with no matching entry nearby.", note="",
        scope_basis=GK):
    entry = {
        "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tg, "basis": GK} for t, tg in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        entry["certification_scope"] = {"value": scope, "basis": scope_basis}
    assert stem not in A, stem
    A[stem] = {"decision": "new", "variant_of": None, "reason": reason, "entry": entry}


def not_skill(stem, reason):
    assert stem not in A, stem
    A[stem] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(stem, reason):
    assert stem not in A, stem
    A[stem] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def variant(stem, target, reason):
    assert stem not in A, stem
    A[stem] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


# ---------------------------------------------------------------- 0-9
new("ancient-philosophy-3be4e5", "Ancient philosophy", "knowledge",
    "The study of the philosophical thought of the ancient Greek and Roman worlds, such as Plato, Aristotle and the Stoics.")
new("andragogy-36dca9", "Andragogy", "knowledge",
    "The theory and practice of teaching and training adults, as distinct from teaching children.")
new("android-applications-258076", "Android app development", "skill",
    "Building applications that run on the Android mobile operating system.",
    variants=["Android application development"])
new("android-ui-2657df", "Android UI development", "skill",
    "Building the screens and controls of an Android app, using Android's view system or Jetpack Compose.")
not_skill("anemia-6d85e7", "A medical condition, not a skill.")
new("anglo-american-cataloguing-rules-c6d0a4", "Anglo-American Cataloguing Rules", "standard",
    "A set of rules for describing and cataloguing library materials, published jointly by library associations in the US, UK and Canada.",
    variants=["AACR2"])
new("angular-cli-e4edf3", "Angular CLI", "tool",
    "The official command-line tool for creating, building, testing and serving Angular projects.",
    relations=[("related", "fcadn3ihwg")])
new("anim8or-20d89b", "Anim8or", "tool",
    "A free 3D modelling and animation program for Windows.")
new("animal-science-902a5f", "Animal science", "knowledge",
    "The study of farm and other domestic animals, including their breeding, nutrition, health and management.")
new("animated-explainer-videos-4516e9", "Animated explainer video production", "skill",
    "Making short animated videos that explain a product, idea or process.")

# ---------------------------------------------------------------- 10-19
new("anma-massage-7ae756", "Anma massage", "skill",
    "A traditional Japanese form of massage that uses kneading and pressing of the body.")
new("anthropometrics-651d33", "Anthropometrics", "knowledge",
    "The measurement of human body dimensions such as height, weight and limb proportions, used for example in ergonomics and health.",
    variants=["Anthropometry"])
new("anti-bribery-and-corruption-1d1ec5", "Anti-bribery and corruption", "knowledge",
    "The laws, policies and controls that organisations use to prevent, detect and respond to bribery and corruption.")
new("anti-malware-software-5ad0c4", "Antivirus software", "tool",
    "Software that detects, blocks and removes malicious software such as viruses, worms and ransomware from a computer or network.",
    variants=["Antivirus", "Anti-virus software"])
unsure("anti-money-laundering-professional-certi-87e152",
       "Reads as a family of anti-money-laundering certifications from several bodies rather than one identifiable credential, so the issuer is unclear.")
new("antics3d-90deeb", "Antics3D", "tool",
    "Software for making 3D computer animations.")
new("antivirus-softwares-2cd20f", "Antivirus software", "tool",
    "Software that detects, blocks and removes malicious software such as viruses, worms and ransomware from a computer or network.",
    variants=["Antivirus", "Anti-virus software"],
    reason="Same concept as the Anti-Malware Software tag in this slice, so it shares the preferred name.")
unsure("apache-0b5958",
       "Alone it could mean the Apache HTTP Server, the Apache Software Foundation or any of its many projects.")
new("apache-airflow-fa6b74", "Apache Airflow", "platform",
    "An open-source platform for writing, scheduling and monitoring data workflows as Python code.",
    verbs=["schedule"])
new("apache-ants-93fd38", "Apache Ant", "tool",
    "A Java-based build automation tool that is driven by XML build files.")

# ---------------------------------------------------------------- 20-29
new("apache-beam-8ce768", "Apache Beam", "framework",
    "An open-source programming model for defining batch and streaming data-processing pipelines that run on engines such as Apache Spark, Apache Flink and Google Cloud Dataflow.")
new("apache-cocoon-ab9cd2", "Apache Cocoon", "framework",
    "A Java web development framework built around pipelines that process XML.")
new("apache-gump-f072c3", "Apache Gump", "tool",
    "A continuous-integration tool that builds and tests many open-source projects together against the latest source of each other.")
new("apache-jena-5a900e", "Apache Jena", "framework",
    "A Java framework for building semantic web and linked-data applications, with an RDF API and a SPARQL query engine.")
new("apache-juddi-91f233", "Apache jUDDI", "platform",
    "An open-source Java implementation of the UDDI (Universal Description, Discovery and Integration) registry for web services.",
    variants=["jUDDI"])
new("apache-lenya-4e5c01", "Apache Lenya", "platform",
    "A Java content management system that is built on Apache Cocoon and stores content as XML.")
new("apache-nifi-b9437f", "Apache NiFi", "platform",
    "A system for automating the movement of data between systems, in which data flows are designed in a web-based interface.")
new("apache-objectrelationalbridge-ojb-8bcc3f", "Apache ObJectRelationalBridge", "library",
    "A Java object-relational mapping tool that stores and retrieves Java objects in relational databases.",
    variants=["Apache OJB", "OJB"])
new("apache-ofbiz-2d6f35", "Apache OFBiz", "platform",
    "An open-source Java platform for enterprise resource planning and e-commerce, made of a framework and ready-made business applications.",
    variants=["OFBiz"])
new("apache-openejb-30e226", "Apache OpenEJB", "platform",
    "A lightweight container that implements the Enterprise JavaBeans (EJB) specification and can run standalone or embedded in another server.")

# ---------------------------------------------------------------- 30-39
new("apache-spark-c4d64a", "Apache Spark", "framework",
    "An open-source engine for large-scale data processing and analytics, with programming interfaces for Scala, Java, Python and R.")
new("api-design-144104", "API design", "skill",
    "Designing the interface through which other programs use a service, including its resources, operations, data formats and errors.")
new("api-gateway-aec0b7", "API gateway", "tool",
    "A server that sits in front of backend services and routes, secures and manages the API requests that clients send to them.")
new("api-management-6a600b", "API management", "skill",
    "Publishing, securing, monitoring and versioning APIs across their lifetime, often with an API gateway and a developer portal.")
new("apollo-graphql-cc277d", "Apollo GraphQL", "platform",
    "Apollo's platform and open-source tools, such as Apollo Client and Apollo Server, for building, running and querying GraphQL APIs.")
unsure("appbuilder-38d77a",
       "Several unrelated products are called AppBuilder, and nothing here says which one is meant.")
not_skill("appendto-89e08d",
          "The name of a jQuery-focused company and of a jQuery method, not a skill.")
new("appian-software-e4d1f2", "Appian", "platform",
    "A low-code platform for building business process, workflow and case management applications.")
new("apple-device-enrollment-program-dep-4270d8", "Apple Device Enrollment Program", "platform",
    "An Apple program, now called Automated Device Enrollment, that lets an organisation enrol company-owned Apple devices in its device-management system automatically when they are first switched on.",
    variants=["Automated Device Enrollment"])
new("apple-ios-9b28e5", "iOS", "platform",
    "The mobile operating system that Apple makes for the iPhone.",
    variants=["Apple iOS", "iPhone OS"])

# ---------------------------------------------------------------- 40-49
new("apple-os-x-d5e640", "macOS", "platform",
    "Apple's operating system for Mac computers, called OS X or Mac OS X before 2016.",
    variants=["OS X", "Mac OS X"])
new("appletviewer-97b8dd", "appletviewer", "tool",
    "A command-line tool in the Java Development Kit that runs Java applets without a web browser.")
unsure("application-analytics-26791a",
       "Could mean usage analytics for apps, application performance analytics or a vendor product, and the tag alone does not say which.")
new("application-controls-ae7120", "Application controls", "knowledge",
    "The checks built into a business application, automated or manual, that make sure transactions are processed completely, accurately and with proper authorisation, as examined in IT audit.")
new("application-delivery-controller-c9128e", "Application delivery controller", "tool",
    "A network device or service placed in front of application servers that balances traffic and adds features such as SSL offloading, caching and application firewalling.")
new("application-delivery-network-0a3f17", "Application delivery network", "knowledge",
    "A set of network technologies, such as load balancers and WAN optimisation, that together keep web applications fast, available and secure.")
unsure("application-end-6c2ff5",
       "A fragment I cannot match to any known skill, tool or method.")
new("application-integration-architecture-fd9c6d", "Oracle Application Integration Architecture", "framework",
    "Oracle's service-oriented framework, with pre-built integration packs, for connecting Oracle and other enterprise business applications.",
    variants=["Oracle AIA"])
new("application-integreation-architecture-9a8515", "Oracle Application Integration Architecture", "framework",
    "Oracle's service-oriented framework, with pre-built integration packs, for connecting Oracle and other enterprise business applications.",
    variants=["Oracle AIA"],
    reason="Misspelling of Application Integration Architecture, the same concept as the other tag in this slice.")
new("application-monitoring-03f2b4", "Application monitoring", "skill",
    "Tracking the availability, performance and errors of a running software application.")

# ---------------------------------------------------------------- 50-59
new("application-pool-d31012", "Application pool", "knowledge",
    "In Microsoft Internet Information Services (IIS), a group of web applications that share a worker process and settings and are isolated from applications in other pools.")
new("application-programming-interface-a63f73", "Application programming interface", "knowledge",
    "A defined set of operations and data formats through which one piece of software lets other programs use its functions.",
    variants=["API", "APIs"])
new("application-specific-integrated-curcuits-da368e", "Application-specific integrated circuit", "knowledge",
    "An integrated circuit designed for one particular purpose or product rather than for general-purpose use.",
    variants=["ASIC", "ASICs", "Application Specific Integrated Circuits"])
new("applied-element-method-b6c8c6", "Applied element method", "method",
    "A numerical method in structural engineering that models a structure as small rigid elements joined by springs, so that its behaviour can be simulated up to collapse.")
new("applied-linguistics-4f232f", "Applied linguistics", "knowledge",
    "The study of language-related problems in real-world settings, such as language teaching, translation and language policy.")
unsure("applied-marketing-4439d8",
       "Reads as a course or programme label, and I cannot tell which defined skill it names beyond marketing in general.")
new("applied-statistics-cd459b", "Applied statistics", "knowledge",
    "The use of statistical methods to analyse data and solve practical problems in a particular field, as opposed to developing statistical theory.",
    relations=[("broader", "ecoz6ylymx")])
new("applixware-27bdcf", "Applixware", "tool",
    "An office productivity suite for Unix and Linux systems made by Applix.")
not_skill("appreciative-433abe", "A generic adjective, not a skill.")
new("appsflyer-saas-3f0e3f", "AppsFlyer", "platform",
    "A platform for mobile attribution and marketing analytics that shows which campaigns lead to app installs and in-app activity.")

# ---------------------------------------------------------------- 60-69
new("appsheet-22af40", "AppSheet", "platform",
    "Google's no-code platform for building apps from data in spreadsheets and databases.")
new("apptio-financial-software-4a95c0", "Apptio", "platform",
    "Software for technology business management that tracks, allocates and reports on the cost of IT.")
unsure("appworld-42aabc",
       "Could be a benchmark for AI agents, an app store or some other product, and nothing here says which.")
new("aquatic-facility-operator-abd7c3", "Aquatic Facility Operator", "credential",
    "A certification showing that someone is trained to operate and maintain a swimming pool or other aquatic facility, including water treatment and safety.",
    cert=True, scope="single-issuer", scope_basis="guess",
    reason="A pool-operator certification, but the legacy list does not say which body awards it.")
new("ar-drone-7f6af4", "Parrot AR.Drone", "tool",
    "A quadcopter drone made by Parrot that is flown from a smartphone or tablet.")
new("arachnophilia-ad77e8", "Arachnophilia", "tool",
    "A free text editor for writing web pages and other code.")
new("arangodb-5fc1b4", "ArangoDB", "platform",
    "A multi-model database that stores documents, graphs and key-value data and is queried with its own language, AQL.")
new("araxis-merge-302ddb", "Araxis Merge", "tool",
    "A commercial tool for comparing and merging files, folders and documents, made by Araxis.")
unsure("arbitrage-trading-program-ecdc8e",
       "Could be an arbitrage trading strategy or a named investment product, and the tag does not say which.")
new("archaeology-db85dc", "Archaeology", "knowledge",
    "The study of past human societies through the excavation and analysis of their material remains.")

# ---------------------------------------------------------------- 70-79
new("archimate-fbf894", "ArchiMate", "modeling-language",
    "An open modelling language, maintained by The Open Group, for describing enterprise architecture across business, application and technology layers.",
    lang="programming")
new("architectural-rendering-defc48", "Architectural rendering", "skill",
    "Producing realistic images of a planned building or interior from a 3D design model.")
new("architectural-visualization-9941c0", "Architectural visualization", "skill",
    "Producing images, animations or virtual walkthroughs that show how a planned building or space will look before it is built.")
new("archiva-ef9f3f", "Apache Archiva", "tool",
    "A repository manager that stores and serves build artifacts such as Maven packages.")
new("arcsight-enterprise-security-manager-155fb5", "ArcSight Enterprise Security Manager", "platform",
    "A security information and event management (SIEM) product that collects and correlates security events from across an organisation to detect threats.",
    variants=["ArcSight ESM"])
new("areca-backup-8e103b", "Areca Backup", "tool",
    "A free, open-source file backup application written in Java.")
new("argo-cd-3501e6", "Argo CD", "tool",
    "A declarative GitOps continuous-delivery tool that keeps applications on Kubernetes in sync with configuration stored in Git.",
    variants=["ArgoCD"], verbs=["deploy"])
new("arithmetics-0771a7", "Arithmetic", "knowledge",
    "The branch of mathematics that deals with calculating with numbers using addition, subtraction, multiplication and division.")
unsure("armadillo-407456",
       "Armadillo names both a C++ linear algebra library and a line of embedded boards, and is also an animal, so I cannot tell which is meant.")
new("armed-forces-health-longitudinal-technol-faaeb6", "Armed Forces Health Longitudinal Technology Application", "tool",
    "The electronic health record system that the US Department of Defense used across its Military Health System to document patient care.",
    variants=["AHLTA"])

# ---------------------------------------------------------------- 80-89
not_skill("armed-guard-b86b48", "A job title for a security role, not a skill.")
new("arquillian-software-febb62", "Arquillian", "framework",
    "A Java testing framework that runs tests inside a real container or server so that code can be tested in its target environment.")
new("arrange-catering-8b13f9", "Arranging catering", "skill",
    "Organising food and drink service for an event, including choosing caterers, menus and quantities.")
new("arranging-conferences-3e8283", "Arranging conferences", "skill",
    "Planning and organising a conference, including its venue, schedule, speakers and attendee logistics.")
unsure("arrow-security-7d06b4",
       "Looks like a company or product name, and I cannot identify it as a skill or tool.")
new("art-education-a0f6c4", "Art education", "knowledge",
    "The teaching and learning of the visual arts, and the study of how to teach them.")
new("art-history-c43fab", "Art history", "knowledge",
    "The academic study of the history of visual art, including its styles, artists and the contexts in which it was made.")
new("art-theory-4c0fd7", "Art theory", "knowledge",
    "The study of the principles, purposes and meaning of the visual arts and of how they are made, judged and interpreted.")
new("arterial-blood-gases-ab0e0c", "Arterial blood gas testing", "knowledge",
    "A blood test on a sample taken from an artery that measures oxygen, carbon dioxide and the acid-base balance of the blood.",
    variants=["Arterial blood gas"],
    relations=[("related", "zko5ukvqdy")])
new("artificial-intelligence-4add51", "Artificial intelligence", "knowledge",
    "The field of computer science concerned with building systems that perform tasks that normally need human intelligence, such as learning, reasoning and perception.",
    variants=["AI"])

# ---------------------------------------------------------------- 90-99
new("artificial-intelligence-risk-94eb37", "Artificial intelligence risk", "knowledge",
    "The study of the harms that artificial intelligence systems can cause, such as bias, security failures and misuse, and of how to reduce them.")
variant("artificial-neural-networks-f6c160", "tx96mffcus",
        "Artificial neural networks are the same concept as the existing Neural networks entry.")
unsure("artisan-fd2f8e",
       "An everyday word for a craftsperson and also the name of Laravel's command-line tool, so I cannot tell which is meant.")
new("artstation-e02377", "ArtStation", "platform",
    "An online platform where digital artists, mainly in games, film and animation, show portfolios and sell assets.")
new("as-built-drawings-8ef387", "As-built drawings", "skill",
    "Preparing or reading drawings that record a building or system as it was actually built, including changes made during construction.")
new("ashampoo-burning-studio-75b317", "Ashampoo Burning Studio", "tool",
    "Software made by Ashampoo for burning data, music and video to CDs, DVDs and Blu-ray discs.")
new("asphalt-batch-mix-plant-2eac32", "Asphalt batch mix plant", "tool",
    "A production facility that dries and heats aggregate and mixes it with bitumen in measured batches to make hot-mix asphalt.")
new("assembly-drawing-461db4", "Assembly drawing", "skill",
    "Preparing or reading technical drawings that show how the parts of a product or machine fit together.")
new("assess-patient-needs-e63135", "Assessing patient needs", "skill",
    "Evaluating a patient's physical, emotional and practical needs so that their care can be planned.")
unsure("asset-analytics-3b010e",
       "Could refer to analytics on physical assets, financial assets or a vendor product, and the tag does not say which.")


def main():
    req = sorted(glob.glob(f"{ROOT}/work/requests/*.json"))
    stems = {os.path.basename(p)[:-5] for p in req}
    assert set(A) == stems, (sorted(stems - set(A)), sorted(set(A) - stems))
    os.makedirs(f"{ROOT}/work/responses", exist_ok=True)
    for stem, ans in A.items():
        with open(f"{ROOT}/work/responses/{stem}.json", "w", encoding="utf-8") as f:
            json.dump(ans, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print(len(A), Counter(a["decision"] for a in A.values()))


main()
