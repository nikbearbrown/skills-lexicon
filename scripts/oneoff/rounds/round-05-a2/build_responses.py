import json, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(ROOT, "requests")
OUT = os.path.join(ROOT, "responses")
GK = "general-knowledge"

def V(*labels):
    return [{"label": l, "basis": GK} for l in labels]

def R(typ, target):
    return {"type": typ, "target": target, "basis": GK}

def new(slug, name, kind, definition, variants=(), relations=(), cert=False, scope=None, lang=None, reason=None, note=""):
    e = {"preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
         "variants": V(*variants), "relations": list(relations), "verbs": [],
         "certification": {"value": cert, "basis": GK}}
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    e["language_type"] = {"value": lang, "basis": GK}
    e["annotation_note"] = note
    return slug, {"decision": "new", "variant_of": None, "reason": reason or "A named skill, tool or concept I know from general knowledge.", "entry": e}

def no(slug, reason):
    return slug, {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}

def unsure(slug, reason):
    return slug, {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}

A = []
add = A.append

add(new("gatsby-js-c58b9c", "Gatsby", "framework", "A free, open-source framework built on React for making fast websites and apps, often from content sources such as CMSs and Markdown files.", ["GatsbyJS"]))
add(new("gel-electrophoresis-of-nucleic-acids-1d6341", "Gel electrophoresis of nucleic acids", "method", "A laboratory technique that separates DNA or RNA fragments by size by pulling them through a gel with an electric field."))
add(new("gemology-76e419", "Gemology", "knowledge", "The study, identification and grading of gemstones."))
add(new("general-administrative-and-clerical-task-79849f", "General administrative and clerical tasks", "skill", "Routine office work such as filing, data entry, answering phones and keeping records."))
add(new("general-anaesthesia-e138ff", "General anaesthesia", "skill", "Giving and managing drugs that put a patient into a reversible, unconscious state with no sensation, so that surgery can be done.", ["General anesthesia"]))
add(new("general-certificate-of-education-gce-e6e300", "General Certificate of Education", "credential", "UK-style academic qualifications, such as A Levels, awarded by several exam boards.", cert=True, scope="many-issuers"))
add(new("general-certificate-of-secondary-educati-c041b3", "General Certificate of Secondary Education", "credential", "Subject qualifications taken in England, Wales and Northern Ireland at about age 16 and awarded by several exam boards.", ["GCSE"], cert=True, scope="many-issuers"))
add(new("general-finance-d817a0", "General finance", "knowledge", "The broad field of how money is raised, invested and managed by individuals, businesses and governments."))
add(new("general-packet-radio-service-b99a32", "General Packet Radio Service", "standard", "A packet-switched mobile data service for 2G and 3G GSM networks, defined in standards from ETSI and 3GPP.", ["GPRS"]))
add(new("general-sciences-91a734", "General sciences", "knowledge", "A broad introduction to the natural sciences, such as biology, chemistry, physics and earth science."))
add(new("generalized-linear-model-59227e", "Generalized linear model", "method", "A statistical model that extends linear regression to outcomes that are not normally distributed by using a link function.", ["Generalised linear model"]))
add(unsure("genie-fb9e76", "Many unrelated products and languages are called Genie, and nothing here shows which one is meant."))
add(new("gensim-c6a410", "Gensim", "library", "A Python library for topic modelling, document similarity and word embeddings on large text collections."))
add(new("geodjango-61a327", "GeoDjango", "library", "A module included with Django (django.contrib.gis) that adds support for geographic data, spatial databases and spatial queries to web applications."))
add(new("geographic-coordinate-system-727c81", "Geographic coordinate system", "knowledge", "A reference system that gives any position on the Earth's surface by latitude and longitude."))
add(new("geologic-modelling-c85a2a", "Geologic modelling", "skill", "Building computer models of rock layers, faults and other subsurface structures to understand the geology of a site."))
add(new("geospatial-databases-640a72", "Geospatial databases", "knowledge", "Databases that store and index data tied to places, such as points, lines and polygons, and answer spatial queries."))
add(new("geospatial-datasets-9af229", "Geospatial data", "knowledge", "Data that describes the location and attributes of features on the Earth, such as vector maps and raster imagery."))
add(new("geospatial-information-technology-git-19887c", "Geospatial information technology", "knowledge", "The technologies used to collect, store, analyse and display location-based data, such as GIS, GPS and remote sensing."))
add(new("gerontological-nurse-practitioner-d8d0b6", "Gerontological Nurse Practitioner", "credential", "A nurse practitioner credential for providing primary care to older adults.",
        relations=[R("related", "u0nv7nrdlk"), R("related", "d9k6zlxp17")], cert=True, scope="many-issuers"))
add(new("gestionnaire-libre-de-parc-informatique--0d02cf", "GLPI", "tool", "An open-source web application, developed in France, for managing IT assets and running a help desk.", ["Gestionnaire Libre de Parc Informatique"]))
add(new("gherkin-scripting-language-f2ee62", "Gherkin", "programming-language", "A plain-text domain-specific language that uses Given, When and Then keywords to write behaviour specifications that tools such as Cucumber can run.", lang="programming"))
add(new("ghidra-reverse-engineering-software-eb6029", "Ghidra", "tool", "A free, open-source software reverse-engineering suite from the US National Security Agency for disassembling and decompiling programs.",
        relations=[R("related", "tdp9wsve0r")]))
add(new("gikuyu-language-a1f8a2", "Gikuyu", "human-language", "A Bantu language spoken mainly by the Kikuyu people of central Kenya.", ["Kikuyu"], lang="human"))
add(new("giraph-0f5e6a", "Apache Giraph", "framework", "An open-source system for large-scale graph processing, built on Hadoop and modelled on Google's Pregel.", ["Giraph"]))
add(new("glass-installing-bb9e6e", "Glass installation", "skill", "Cutting, fitting and sealing glass panes, such as windows, doors and mirrors, in frames and openings.", relations=[R("related", "a9sbyr46z1")]))
add(new("global-information-assurance-certificati-d59698", "GIAC certification", "credential", "The information-security certifications, such as GSEC and GCIH, awarded by Global Information Assurance Certification (GIAC).", ["GIAC"], cert=True, scope="single-issuer"))
add(unsure("global-information-systems-d57398", "It could mean worldwide information systems or be a mistake for Geographic Information Systems, and nothing here settles which."))
add(new("global-mapper-bee3de", "Global Mapper", "tool", "GIS software from Blue Marble Geographics for viewing, editing and analysing geospatial data."))
add(unsure("global-methods-aa8fca", "A vague label I cannot tie to one skill or field."))
add(new("go-to-market-strategy-7dc073", "Go-to-market strategy", "skill", "Planning how a company will bring a product or service to its target customers, including positioning, pricing and sales channels.", ["GTM strategy"]))
add(new("goal-focused-3f3576", "Goal-oriented", "ability", "A tendency to set clear objectives and keep working steadily toward reaching them."))
add(new("goal-oriented-174ea0", "Goal-oriented", "ability", "A tendency to set clear objectives and keep working steadily toward reaching them."))
add(new("goal-setting-6aa366", "Goal setting", "skill", "Defining clear objectives and the steps and timeline needed to reach them."))
add(new("goanimate-69ea33", "Vyond", "tool", "A cloud-based tool for making animated videos from templates and characters, called GoAnimate before 2018."))
add(new("gold-panning-7900f4", "Gold panning", "skill", "Separating gold from sand and gravel by swirling the material with water in a shallow pan."))
add(new("google-advanced-analytics-certificate-d96282", "Google Advanced Data Analytics Professional Certificate", "credential", "Google's online professional certificate covering statistics, regression and machine learning for data analysis.", cert=True, scope="single-issuer"))
add(new("google-adwords-7e71b8", "Google Ads", "platform", "Google's online advertising platform for running paid search and display ads, called AdWords before 2018.", ["AdWords"]))
add(new("google-adwords-certification-d69a10", "Google Ads Certification", "credential", "Google's certifications, taken through its Skillshop learning platform, showing skill with Google Ads, formerly AdWords.", cert=True, scope="single-issuer"))
add(new("google-analytics-certification-c291a4", "Google Analytics Certification", "credential", "Google's certification, taken through its Skillshop learning platform, showing skill with Google Analytics.", cert=True, scope="single-issuer"))
add(new("google-associate-cloud-engineer-9e9115", "Google Cloud Certified Associate Cloud Engineer", "credential", "A Google Cloud certification showing that a person can deploy applications, monitor operations and manage solutions on Google Cloud.", cert=True, scope="single-issuer"))
add(new("google-bard-566f82", "Google Bard", "tool", "Google's conversational AI chatbot, launched in 2023 and renamed Gemini in 2024."))
add(new("google-business-intelligence-certificate-c5c4c2", "Google Business Intelligence Professional Certificate", "credential", "Google's online professional certificate covering how to build data models, pipelines, dashboards and reports for business decisions.", cert=True, scope="single-issuer"))
add(new("google-business-profile-b37768", "Google Business Profile", "tool", "The free Google tool that lets a business manage how it appears in Google Search and Maps, formerly called Google My Business.", ["Google My Business"]))
add(new("google-cloud-platform-gcp-4037fc", "Google Cloud Platform", "platform", "Google's suite of cloud computing services, including computing, storage, databases and machine learning."))
add(new("google-cybersecurity-professional-certif-c0e6c6", "Google Cybersecurity Professional Certificate", "credential", "Google's online professional certificate covering security fundamentals, networks, Linux, SQL and incident response for entry-level security roles.", cert=True, scope="single-issuer"))
add(new("google-dart-24ba50", "Dart", "programming-language", "A programming language developed by Google, used mainly with the Flutter framework to build apps for several platforms.", lang="programming"))
add(new("google-data-analytics-certificate-e22588", "Google Data Analytics Professional Certificate", "credential", "Google's online professional certificate covering data cleaning, analysis, spreadsheets, SQL, R and visualisation for entry-level data analyst roles.", cert=True, scope="single-issuer"))
add(new("google-digital-marketing-certificate-44f4f2", "Google Digital Marketing Certificate", "credential", "A Google-issued online certificate covering digital marketing skills such as search, social media and e-commerce.", cert=True, scope="single-issuer"))
add(new("google-f77562", "Google+", "platform", "Google's social network, launched in 2011 and shut down for consumers in 2019."))
add(new("google-it-automation-certificate-1b659d", "Google IT Automation with Python Professional Certificate", "credential", "Google's online professional certificate covering Python scripting, Git and automating IT tasks.", cert=True, scope="single-issuer"))
add(new("google-it-support-certificate-3aa42f", "Google IT Support Professional Certificate", "credential", "Google's online professional certificate covering troubleshooting, networking, operating systems, system administration and security for entry-level IT support roles.", cert=True, scope="single-issuer"))
add(new("google-jamboard-5b2cd8", "Google Jamboard", "tool", "Google's digital whiteboard app for collaborative sketching and note-taking, retired by Google at the end of 2024.", ["Jamboard"]))
add(new("google-kubernetes-engine-gke-81d536", "Google Kubernetes Engine", "platform", "Google Cloud's managed service for running containerised applications on Kubernetes.", ["GKE"]))
add(new("google-optimize-f13b30", "Google Optimize", "tool", "A Google tool for running website A/B tests and personalisation experiments, discontinued in 2023."))
add(new("google-professional-cloud-architect-a7cbf9", "Google Cloud Certified Professional Cloud Architect", "credential", "A Google Cloud certification showing that a person can design and manage secure, scalable cloud solutions on Google Cloud.", cert=True, scope="single-issuer"))
add(new("google-project-management-certificate-93cc4c", "Google Project Management Professional Certificate", "credential", "Google's online professional certificate covering project planning, execution and agile practice.",
        relations=[R("related", "z83cabeb9c")], cert=True, scope="single-issuer"))
add(new("google-sheets-729b91", "Google Sheets", "tool", "Google's web-based spreadsheet application for creating, editing and sharing spreadsheets online."))
add(new("google-slides-3dc242", "Google Slides", "tool", "Google's web-based application for creating, editing and sharing presentation slides online."))
add(new("google-ux-design-certificate-216e84", "Google UX Design Professional Certificate", "credential", "Google's online professional certificate covering user research, wireframes, prototypes and usability testing.", cert=True, scope="single-issuer"))
add(new("gopro-832457", "GoPro", "tool", "A brand of small, rugged action cameras used to record video during activities."))
add(new("gosystems-tax-software-007364", "GoSystem Tax RS", "tool", "Thomson Reuters software used by accounting firms to prepare and file tax returns."))
add(new("government-engagement-1c9759", "Government engagement", "skill", "Building and managing relationships with government officials and agencies to inform policy or win public-sector support."))
add(new("government-finance-ff8af1", "Government finance", "knowledge", "The field concerned with how governments raise revenue, budget, spend and manage debt."))
add(unsure("grace-01c952", "Grace could be a name, a product or a framework, and nothing here shows which."))
add(new("graduate-realtor-institute-86429a", "Graduate REALTOR Institute", "credential", "A real-estate designation of the National Association of Realtors, awarded by state Realtor associations to agents who complete a set of advanced courses.", cert=True, scope="many-issuers"))
add(unsure("grammars-8f8e9e", "It could mean grammar as a language skill or formal grammars in computing, and nothing here settles which."))
add(unsure("graphdb-d0b71a", "It could mean Ontotext's GraphDB product or graph databases in general, and nothing here settles which."))
add(new("graphical-evaluation-and-review-techniqu-055dc3", "Graphical Evaluation and Review Technique", "method", "A network-analysis technique for planning projects whose activities have uncertain outcomes and may loop back."))
add(unsure("graphics-animation-system-for-profession-fb7cab", "It may be an early PC animation program called GRASP, but I cannot confirm that from memory."))
add(new("graphics-api-00ef15", "Graphics API", "knowledge", "Programming interfaces, such as OpenGL, Vulkan and DirectX, that let software send drawing commands to graphics hardware."))
add(new("graphics-interchange-format-acdb09", "Graphics Interchange Format", "standard", "A bitmap image file format, introduced by CompuServe in 1987, that supports 256 colours per frame and simple animation.", ["GIF"]))
add(new("graphite-220c98", "Graphite", "tool", "An open-source monitoring tool that stores numeric time-series data and draws graphs from it."))
add(new("graphql-3407b2", "GraphQL", "programming-language", "A query language for APIs, with a server-side runtime, that lets clients ask for exactly the data they need.",
        relations=[R("related", "nkt2stz7xu")], lang="programming"))
add(new("great-circle-e43c21", "Great circle", "knowledge", "A circle on a sphere whose centre is the sphere's centre, whose arcs are the shortest routes between two points on the Earth's surface."))
add(new("greeks-finance-c85aae", "Greeks (finance)", "knowledge", "The measures of how an option's price changes with other factors, such as delta, gamma, theta, vega and rho.", ["Option Greeks"]))
add(new("green-bond-e91b0d", "Green bond", "knowledge", "A bond whose proceeds fund projects with environmental benefits, such as renewable energy."))
add(new("green-hills-integrity-aee3ca", "INTEGRITY RTOS", "platform", "A real-time operating system from Green Hills Software, used in safety-critical embedded systems such as avionics."))
add(new("greet-guests-86aeac", "Greeting guests", "skill", "Welcoming visitors or customers when they arrive in a friendly, professional way."))
add(new("greeting-guests-a54694", "Greeting guests", "skill", "Welcoming visitors or customers when they arrive in a friendly, professional way."))
add(unsure("grid-packaging-technology-2b2402", "I cannot tell from memory what this refers to."))
add(unsure("grid-packaging-techology-bbd0ac", "A misspelling of a term I cannot identify from memory."))
add(new("grieving-process-a6611f", "Grieving process", "knowledge", "The emotional and psychological process of coming to terms with a significant loss."))
add(new("groove-welding-59e86f", "Groove welding", "skill", "Joining two pieces of metal by filling a groove cut or formed between them with weld metal."))
add(new("groovy-9c53c0", "Groovy", "programming-language", "A dynamic programming language for the Java Virtual Machine, with syntax close to Java's, used for scripting and build files.", ["Apache Groovy"], lang="programming"))
add(new("groundskeeping-and-yard-care-daea4b", "Groundskeeping and yard care", "skill", "Maintaining outdoor grounds by mowing, trimming, planting, watering and clearing debris."))
add(new("group-decision-making-a1501b", "Group decision-making", "method", "A process in which a group weighs the options together and reaches a decision.", relations=[R("related", "od1b6mmloc")]))
add(new("group-work-f4a6b6", "Group work", "skill", "Working with other people in a group toward a shared task or goal."))
add(new("grunt-js-e6d2c0", "Grunt.js", "tool", "A JavaScript task runner that automates repetitive build tasks, such as minifying, compiling and testing files, from a configuration file."))
add(new("gruntjs-b7fc9d", "Grunt.js", "tool", "A JavaScript task runner that automates repetitive build tasks, such as minifying, compiling and testing files, from a configuration file."))
add(new("gsuite-f16c65", "Google Workspace", "platform", "Google's suite of cloud productivity and collaboration apps, including Gmail, Drive, Docs and Meet, formerly called G Suite.", ["G Suite"]))
add(no("gui-designer-828d3b", "A job role; the skill it points to is GUI or user interface design."))
add(no("gui-editor-fa140e", "A generic kind of software tool, not a specific skill or product."))
add(unsure("guidewire-core-a69de9", "A Guidewire product-area name that I cannot define reliably from memory."))
add(unsure("guidewire-data-411bdb", "A Guidewire product-area name that I cannot define reliably from memory."))
add(unsure("guidewire-digital-d3174a", "A Guidewire product-area name that I cannot define reliably from memory."))
add(new("gujarati-language-da811a", "Gujarati", "human-language", "An Indo-Aryan language spoken mainly in the Indian state of Gujarat.", lang="human"))
add(new("gulp-js-2d6566", "Gulp.js", "tool", "A JavaScript toolkit and task runner that automates build tasks such as compiling, bundling and minifying files."))
add(unsure("guttae-47fcb0", "Latin for drops, used in several medical senses, and nothing here shows which skill is meant."))
add(new("gymnastics-1df871", "Gymnastics", "skill", "The sport of performing exercises that demand strength, flexibility and balance, such as floor routines, vault and beam."))

slugs = [s for s, _ in A]
assert len(slugs) == len(set(slugs)), "duplicate slug"
reqs = {f[:-5] for f in os.listdir(REQ) if f.endswith(".json")}
missing, extra = reqs - set(slugs), set(slugs) - reqs
print("requests", len(reqs), "answers", len(slugs), "missing", sorted(missing), "extra", sorted(extra))
if missing or extra:
    sys.exit(1)
os.makedirs(OUT, exist_ok=True)
for s, d in A:
    with open(os.path.join(OUT, s + ".json"), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
from collections import Counter
print(Counter(d["decision"] for _, d in A))
