"""Scratch script: builds work/responses/*.json from hand-written decisions. Not part of the repo."""
import glob
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(ROOT, "requests")
OUT = os.path.join(ROOT, "responses")
os.makedirs(OUT, exist_ok=True)

GK = "general-knowledge"
D = {}  # slug -> response


def nas(slug, reason):
    D[slug] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(slug, reason):
    D[slug] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def new(slug, name, kind, definition, reason, variants=(), rel=(), cert=False, scope=None, lang=None, note=""):
    entry = {
        "preferred_name": name,
        "kind": kind,
        "definition": definition,
        "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": tgt, "basis": GK} for t, tgt in rel],
        "verbs": [],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note,
    }
    if cert:
        entry["certification_scope"] = {"value": scope, "basis": GK}
    D[slug] = {"decision": "new", "variant_of": None, "reason": reason, "entry": entry}


# ---------------------------------------------------------------- H
new("housing-credit-ceritified-professional-11c67e", "Housing Credit Certified Professional", "credential",
    "A certification for professionals who manage compliance with the rules of the Low-Income Housing Tax Credit programme.",
    "A housing-industry compliance certification; the legacy spelling has a typo.",
    rel=[("related", "dcmviql9mp")], cert=True, scope="single-issuer")

new("hp-alm-22656f", "HP Application Lifecycle Management", "tool",
    "Software, first from HP and later from Micro Focus and OpenText, for managing requirements, test cases and defects across a software project.",
    "HP ALM is a known test and requirements management product.")

unsure("html-components-2ebe8d", "Could mean reusable HTML interface components or the old Internet Explorer HTML Components (.htc) feature; the tag alone does not say which.")

unsure("html-generation-7cdd6e", "Could mean producing HTML from templates or code, or generating pages with AI; the tag alone does not say which.")

new("html5shiv-6824c8", "html5shiv", "library",
    "A small JavaScript library that lets old versions of Internet Explorer recognise and style HTML5 elements.",
    "A well-known JavaScript compatibility library.",
    variants=["HTML5 Shiv"], rel=[("related", "twhbebct5l")])

unsure("htmlcontrols-deda6e", "Looks like the ASP.NET HtmlControls namespace, but could be any set of HTML interface controls; I cannot tell which.")

new("hubspot-crm-95c332", "HubSpot CRM", "platform",
    "HubSpot's customer relationship management software for tracking contacts, companies, deals and sales activity.",
    "A named CRM product from HubSpot.")

new("human-capital-management-integration-c10a7c", "Human capital management integration", "skill",
    "Connecting human capital management software, which holds HR and payroll data, with other business systems so that data flows between them.",
    "A recognised integration skill in HR systems work.")

nas("human-development-report-c1d5d9", "The name of the United Nations Development Programme's annual publication, not a skill.")

new("human-factors-5a5312", "Human factors", "knowledge",
    "The study of how people interact with machines, systems and environments, used to make them safer, easier to use and more effective.",
    "A recognised field of study and practice.",
    variants=["Human factors and ergonomics"])

new("human-factors-engineering-e03394", "Human factors engineering", "skill",
    "Applying knowledge of human abilities and limits to design equipment, interfaces and tasks that are safe, usable and effective.",
    "A recognised engineering discipline and practice.")

new("human-machine-interface-bac8be", "Human-machine interface", "knowledge",
    "The screens, controls and displays through which an operator monitors and controls a machine or industrial process.",
    "A standard industrial and engineering term; the legacy tag has a stray space.",
    variants=["HMI"])

new("human-musculoskeletal-systems-168c7c", "Human musculoskeletal system", "knowledge",
    "The bones, muscles, joints and connective tissue that support the human body and let it move.",
    "A body of anatomical knowledge asked for in health and fitness work.")

unsure("human-performance-evaluation-7725bb", "Could mean employee performance appraisal or testing how well operators perform in a human-factors study; the tag alone does not say which.")

nas("human-physical-appearance-726c0c", "A description of how a person looks, not a skill.")

unsure("human-rights-issues-066e61", "A topic area; I cannot tell whether it stands for knowledge of human rights or something else.")

new("human-rights-laws-09af16", "Human rights law", "knowledge",
    "The national and international laws that protect people's basic rights and freedoms.",
    "A recognised field of law.")

unsure("human-rights-policies-fb362c", "Could mean drafting organisational policies or knowing government policy; the tag alone does not say which.")

nas("human-trafficking-issue-38b75e", "A crime and social problem, not a skill.")

unsure("humidity-therapy-0a33cf", "I am not sure which treatment or practice this names.")

new("hungarian-language-ced834", "Hungarian", "human-language",
    "A Uralic language, the official language of Hungary.",
    "Hungarian is a human language.",
    variants=["Magyar"], lang="human")

new("hup-language-44e20a", "Hup", "human-language",
    "An Amazonian language spoken by the Hupda people along the border of Brazil and Colombia.",
    "Hup is a human language.", lang="human")

new("hybrid-mobile-app-893116", "Hybrid mobile app development", "skill",
    "Building mobile apps with web technologies such as HTML, CSS and JavaScript inside a native container, so one code base runs on several platforms.",
    "The tag names the product; the skill is building hybrid apps.")

nas("hydration-bdfb04", "A generic word for taking in or adding water, with no skill meaning on its own.")

new("hydrological-modelling-78bfea", "Hydrological modelling", "method",
    "Using mathematical models to simulate how water moves through catchments, rivers and aquifers.",
    "A standard technique in hydrology.",
    variants=["Hydrological modeling", "Hydrologic modeling", "Hydrologic modelling"])

new("hyperbaric-welding-95a8d6", "Hyperbaric welding", "skill",
    "Welding carried out at raised pressure, usually inside a sealed dry chamber around underwater structures such as pipelines.",
    "A recognised specialist welding skill.")

new("hypercompact-stellar-systems-astrophysic-c03c1b", "Hypercompact stellar systems", "knowledge",
    "Dense clusters of stars predicted to stay bound to a supermassive black hole that has been flung out of its host galaxy.",
    "A topic in astrophysics.")

nas("hyperkinetic-disorder-508293", "A medical condition, the ICD name for a form of attention-deficit disorder, not a skill.")

nas("hypertherm-2f4d5b", "A company that makes plasma cutting equipment, not a skill.")

# ---------------------------------------------------------------- I
new("i2c-2a4613", "I2C", "standard",
    "A two-wire serial bus protocol, created by Philips, that lets chips on a circuit board talk to each other.",
    "A widely used hardware communication protocol.",
    variants=["Inter-Integrated Circuit"])

new("iad-0f2585", "iAd", "platform",
    "Apple's mobile advertising platform, which served ads inside iOS apps until it was shut down in 2016.",
    "Read as iAd, Apple's advertising platform; same concept as the other iAd tag.")

new("iad-apple-s-advertising-platform-f7aed4", "iAd", "platform",
    "Apple's mobile advertising platform, which served ads inside iOS apps until it was shut down in 2016.",
    "Apple's advertising platform iAd.")

new("iam-level-ii-certification-db8308", "IAM Level II certification", "credential",
    "A Level II requirement in the US Department of Defense 8570 framework for information assurance management staff, met by holding an approved certification.",
    "A level of the DoD 8570 scheme, like the existing IAM Level I entry.",
    rel=[("related", "xzgr4torrj")], cert=True, scope="many-issuers")
new("iam-level-iii-certification-ed2cad", "IAM Level III certification", "credential",
    "A Level III requirement in the US Department of Defense 8570 framework for information assurance management staff, met by holding an approved certification.",
    "A level of the DoD 8570 scheme, like the existing IAM Level I entry.",
    rel=[("related", "xzgr4torrj")], cert=True, scope="many-issuers")

new("iar-embedded-workbench-a69ec7", "IAR Embedded Workbench", "tool",
    "An integrated development environment from IAR Systems, with a C and C++ compiler and debugger, for writing embedded software for microcontrollers.",
    "A named embedded development tool.")

for lvl, slug in (("I", "iat-level-i-certification-6cdfd6"), ("II", "iat-level-ii-certification-545569"), ("III", "iat-level-iii-certification-bdedd2")):
    new(slug, f"IAT Level {lvl} certification", "credential",
        f"A Level {lvl} requirement in the US Department of Defense 8570 framework for information assurance technical staff, met by holding an approved certification.",
        "A level of the DoD 8570 scheme, a sibling of the existing IAM Level I entry.",
        rel=[("related", "xzgr4torrj")], cert=True, scope="many-issuers")

new("ibeacon-cb4123", "iBeacon", "platform",
    "Apple's Bluetooth Low Energy technology in which a small transmitter broadcasts an identifier that nearby phones can detect, used for indoor location and proximity.",
    "A named Apple technology.")

new("ibm-bluemix-3e3c40", "IBM Bluemix", "platform",
    "IBM's cloud platform for building and running applications, renamed IBM Cloud in 2017.",
    "A named IBM cloud platform.")

new("ibm-bpm-379e0a", "IBM Business Process Manager", "platform",
    "IBM software for modelling, running and monitoring business processes, later succeeded by IBM Business Automation Workflow.",
    "IBM BPM is IBM Business Process Manager.")

new("ibm-cl-supersession-e56805", "IBM CL/SuperSession", "tool",
    "Mainframe software that manages a terminal user's sessions with several network applications at once.",
    "A mainframe session-management product; my knowledge of its details is thin.")

new("ibm-data-studio-a9ea67", "IBM Data Studio", "tool",
    "An Eclipse-based IBM tool for administering and developing Db2 databases.",
    "A named IBM database tool.")

new("ibm-eservers-0890b2", "IBM eServer", "platform",
    "IBM's server brand of the early 2000s, covering the xSeries, pSeries, iSeries and zSeries hardware lines.",
    "A named IBM hardware brand.")

new("ibm-informix-7687a3", "IBM Informix", "platform",
    "A relational database management system that IBM bought in 2001 and that is now developed and sold by HCL.",
    "A named database product.",
    variants=["Informix", "HCL Informix"])

new("ibm-officevision-9aa6bb", "IBM OfficeVision", "tool",
    "IBM's office software for mainframes, offering email, calendars and document handling.",
    "A named IBM product from the mainframe era.")

new("ibm-power10-microprocessors-12fc70", "IBM POWER10", "platform",
    "IBM's tenth-generation POWER microprocessor family for servers, released in 2021.",
    "A named processor generation, separate from POWER8.",
    variants=["POWER10"], rel=[("related", "k6ns4jdo7n")])
new("ibm-power7-microprocessors-10077b", "IBM POWER7", "platform",
    "IBM's seventh-generation POWER microprocessor family for servers, released in 2010.",
    "A named processor generation, separate from POWER8.",
    variants=["POWER7"], rel=[("related", "k6ns4jdo7n")])
new("ibm-power9-microprocessors-c93a9a", "IBM POWER9", "platform",
    "IBM's ninth-generation POWER microprocessor family for servers, released in 2017.",
    "A named processor generation, separate from POWER8.",
    variants=["POWER9"], rel=[("related", "k6ns4jdo7n")])

new("ibm-qradar-siem-software-00d9e7", "IBM QRadar", "tool",
    "Security information and event management (SIEM) software that collects and analyses log and network data to detect threats.",
    "A named SIEM product.",
    variants=["QRadar"])

new("ibm-rad-29d141", "IBM Rational Application Developer", "tool",
    "An Eclipse-based IBM development environment for building Java and web applications, aimed at deployment on IBM WebSphere.",
    "RAD in an IBM context is Rational Application Developer.",
    variants=["Rational Application Developer"])

new("ibm-was-6b35e8", "IBM WebSphere Application Server", "platform",
    "IBM's Java application server, which runs and manages enterprise web applications.",
    "WAS in an IBM context is WebSphere Application Server.",
    variants=["WebSphere Application Server"])

unsure("icap-4-550b04", "I do not recognise ICAP/4; it is not a term I can define with confidence.")

new("icd-coding-be235e", "ICD coding", "skill",
    "Assigning International Classification of Diseases codes to diagnoses and procedures in medical records for billing and statistics.",
    "A standard medical coding skill.")

unsure("ice-validation-e249a3", "Could be Windows Installer ICE validation or something else; the tag alone does not say which.")

new("ich-guidelines-f9c648", "ICH guidelines", "standard",
    "Technical guidelines from the International Council for Harmonisation that set common expectations for the quality, safety and efficacy of medicines and for how clinical trials are run.",
    "A well-known set of pharmaceutical guidelines.")

unsure("icheck-f1fbd9", "Several unrelated products and tools could be called Icheck; I cannot tell which is meant.")

new("icmpv6-3c9de2", "ICMPv6", "standard",
    "The Internet Control Message Protocol for IPv6, used for error messages, diagnostics and neighbour discovery.",
    "A named internet protocol.",
    variants=["Internet Control Message Protocol version 6"])

new("ida-pro-8f76e7", "IDA Pro", "tool",
    "An interactive disassembler and debugger from Hex-Rays for reverse engineering compiled programs.",
    "A named reverse-engineering tool.",
    variants=["Interactive Disassembler"])

nas("idea-networks-of-biomedical-research-exc-518cb5", "A US National Institutes of Health funding programme, not a skill.")

new("ideation-1c8928", "Ideation", "skill",
    "Coming up with and developing new ideas, for example for products, designs or campaigns.",
    "A recognised creative and product skill.")

new("identity-management-6567a7", "Identity management", "skill",
    "Creating, maintaining and removing the digital identities of people and systems and controlling what access those identities have.",
    "A recognised IT security discipline.")

unsure("identity-verification-services-47ea44", "Could mean the skill of verifying identities or vendor services that do it; the tag alone does not say which.")

new("identityiq-26d568", "SailPoint IdentityIQ", "platform",
    "SailPoint's identity governance software for managing user access, access reviews and account provisioning across an organisation's systems.",
    "IdentityIQ is a named SailPoint product.",
    variants=["IdentityIQ"])

new("ids-infolease-asset-finance-technology-ed9138", "IDS InfoLease", "tool",
    "Software for managing leases and other asset-finance contracts.",
    "A named asset-finance software product; my knowledge of its details is limited.")

new("ieee-1394-interface-44608f", "IEEE 1394", "standard",
    "An IEEE standard for a high-speed serial bus connecting devices such as cameras and disk drives, sold by Apple as FireWire.",
    "A named hardware interface standard.",
    variants=["FireWire", "i.LINK"])

new("ieee-1547-678f40", "IEEE 1547", "standard",
    "An IEEE standard setting technical requirements for connecting distributed energy resources, such as solar inverters and batteries, to the electric power grid.",
    "A named IEEE standard.")

new("ifs-erp-d55c2f", "IFS Applications", "platform",
    "Enterprise resource planning software from the Swedish company IFS, whose current product line is branded IFS Cloud.",
    "IFS ERP is IFS's enterprise resource planning product.")

new("igbo-language-f49965", "Igbo", "human-language",
    "A Niger-Congo language spoken mainly by the Igbo people of southeastern Nigeria.",
    "Igbo is a human language.", lang="human")

new("iiba-agile-analysis-certification-900b4d", "IIBA Agile Analysis Certification", "credential",
    "A certification from the International Institute of Business Analysis for business analysts who work in agile settings.",
    "A certification from the IIBA.",
    variants=["IIBA-AAC"], cert=True, scope="single-issuer")

unsure("iis-logs-bf42c9", "Names the log files of Microsoft IIS; unclear whether it is meant as a skill, such as log analysis, or just a data source.")

new("iis-manager-b1b19c", "IIS Manager", "tool",
    "The graphical console in Windows for configuring Microsoft Internet Information Services web sites and application pools.",
    "A named Microsoft administration tool.")

new("imac-g4-7169a2", "iMac G4", "platform",
    "Apple's all-in-one desktop computer with a flat display on an adjustable arm, sold from 2002 to 2004.",
    "A named Apple computer model.")
new("imac-g5-ca9869", "iMac G5", "platform",
    "Apple's all-in-one desktop computer with a PowerPC G5 processor, sold from 2004 to 2006.",
    "A named Apple computer model.")

new("image-and-video-compression-7cf26e", "Image and video compression", "knowledge",
    "Reducing the storage and bandwidth that pictures and video need by encoding them with formats and codecs such as JPEG and H.264.",
    "A recognised technical field.")

new("image-generation-e4eb52", "Image generation", "skill",
    "Creating new images from text prompts or other inputs with generative AI models.",
    "Most likely the generative AI sense; DALL-E is a related tool.",
    rel=[("related", "pudsxgof73")])

new("ip-address-management-54b877", "IP address management", "skill",
    "Planning, tracking and administering a network's IP address space and the DHCP and DNS records tied to it.",
    "A standard networking task.",
    variants=["IPAM"])

unsure("iplant-web-server-709ffa", "I cannot tell what the iPlant web server is; it may relate to the iPlant Collaborative but I am not sure.")

new("ipma-certified-project-management-associ-673909", "IPMA Certified Project Management Associate", "credential",
    "The entry-level of the four IPMA project management certification levels, known as Level D.",
    "An IPMA certification level, below the existing Level B entry.",
    variants=["IPMA Level D"], rel=[("related", "sbn1jb6svt")], cert=True, scope="many-issuers")

new("ipython-571ae8", "IPython", "tool",
    "An enhanced interactive Python shell, which also provides the kernel behind Jupyter notebooks.",
    "A named Python tool, not the same as Python itself.",
    rel=[("related", "pk7cebmtg6")])

new("iso-10012-a10f1c", "ISO 10012", "standard",
    "An ISO standard with requirements for managing measurement processes and the equipment used to measure.",
    "A named ISO standard.")
new("iso-10993-6f53d0", "ISO 10993", "standard",
    "A series of ISO standards for evaluating whether medical devices are biologically safe to use on or in the body.",
    "A named ISO standard series.")
new("iso-14000-standard-b6eb85", "ISO 14000", "standard",
    "A family of ISO standards on environmental management, of which ISO 14001 sets the requirements for an environmental management system.",
    "A named ISO standard family.")
new("iso-14971-79a59e", "ISO 14971", "standard",
    "An ISO standard describing how manufacturers identify, evaluate and control the risks of medical devices.",
    "A named ISO standard.")
new("iso-15189-9d3aaf", "ISO 15189", "standard",
    "An ISO standard setting quality and competence requirements for medical laboratories.",
    "A named ISO standard.")
new("iso-19011-ef0236", "ISO 19011", "standard",
    "An ISO standard giving guidance on auditing management systems, including how to plan audits and what auditors need to be competent in.",
    "A named ISO standard.")
new("iso-26262-eb69ca", "ISO 26262", "standard",
    "An ISO standard for the functional safety of electrical and electronic systems in road vehicles.",
    "A named ISO standard.")
new("iso-31000-2654d3", "ISO 31000", "standard",
    "An ISO standard giving principles and guidelines for managing risk in any organisation.",
    "A named ISO standard.")
new("iso-50001-3091bc", "ISO 50001", "standard",
    "An ISO standard with requirements for an energy management system that helps an organisation use energy more efficiently.",
    "A named ISO standard.")
new("iso-8583-798bb3", "ISO 8583", "standard",
    "An ISO standard defining the format of messages exchanged between systems that process payment-card transactions.",
    "A named ISO standard.")
new("iso-9000-f294d4", "ISO 9000", "standard",
    "A family of ISO standards on quality management, which sets out the vocabulary and principles behind ISO 9001.",
    "A named ISO standard family.",
    rel=[("related", "jqn7upjsc9")])
new("iso-iec-27000-series-3dd424", "ISO/IEC 27000 series", "standard",
    "A family of ISO/IEC standards on information security management, including ISO/IEC 27001 for management systems and ISO/IEC 27002 for controls.",
    "A named standards family; the other 27001 Series tag is the same concept.")
new("iso-iec-27001-40e00c", "ISO/IEC 27001", "standard",
    "An ISO/IEC standard that sets requirements for an information security management system, against which organisations can be certified.",
    "A named ISO/IEC standard.",
    variants=["ISO 27001"])
new("iso-iec-27001-series-f3f1d9", "ISO/IEC 27000 series", "standard",
    "A family of ISO/IEC standards on information security management, including ISO/IEC 27001 for management systems and ISO/IEC 27002 for controls.",
    "Read as the ISO/IEC 27000 family; same concept as the other 27000 series tag.")

new("iss-eclss-65dce8", "ISS Environmental Control and Life Support System", "knowledge",
    "The equipment on the International Space Station that supplies breathable air and water, controls temperature and humidity, and handles waste.",
    "ECLSS on the ISS is its life support system.")

new("it-security-architecture-545c28", "IT security architecture", "skill",
    "Designing the structure of controls, systems and policies that protect an organisation's IT environment.",
    "A recognised security design skill.")
new("it-security-documentation-711095", "IT security documentation", "skill",
    "Writing and maintaining the policies, procedures and records that describe an organisation's IT security controls.",
    "A plausible documentation skill in IT security work.")

new("itil-expert-certification-a249dc", "ITIL Expert", "credential",
    "A top-level ITIL version 3 qualification earned by collecting credits from intermediate ITIL modules.",
    "An ITIL qualification level.", cert=True, scope="single-issuer")
new("itil-foundation-certification-ef703d", "ITIL Foundation", "credential",
    "The entry-level ITIL qualification, covering the basic concepts and terms of ITIL service management.",
    "An ITIL qualification level.", cert=True, scope="single-issuer")
new("itil-practitioner-certification-76bf06", "ITIL Practitioner", "credential",
    "An ITIL qualification on adopting and adapting ITIL guidance in an organisation, including through continual service improvement.",
    "An ITIL qualification level.", cert=True, scope="single-issuer")

# ---------------------------------------------------------------- write
slugs = {os.path.basename(f)[:-5] for f in glob.glob(os.path.join(REQ, "*.json"))}
missing = slugs - set(D)
extra = set(D) - slugs
assert not missing and not extra, (missing, extra)
for slug, resp in D.items():
    with open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8") as fh:
        json.dump(resp, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
from collections import Counter
print(Counter(r["decision"] for r in D.values()), len(D))
