"""Scratch: build one response per request in work/requests/ and write it to work/responses/."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQ = ROOT / "requests"
OUT = ROOT / "responses"
GK = "general-knowledge"

A = {}  # slug (file stem) -> answer dict


def stem(prefix):
    hits = [p.stem for p in REQ.glob(prefix + "*.json")]
    if len(hits) != 1:
        sys.exit(f"prefix {prefix!r} matched {hits}")
    return hits[0]


def no(prefix, reason):
    A[stem(prefix)] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(prefix, reason):
    A[stem(prefix)] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def new(prefix, name, kind, definition, reason, variants=(), relations=(), verbs=(),
        cert=False, scope=None, lang=None, cert_basis=None, note=None):
    e = {
        "preferred_name": name,
        "kind": kind,
        "definition": definition,
        "definition_basis": GK,
        "variants": [{"label": v, "basis": GK} for v in variants],
        "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
        "verbs": [{"verb": v, "basis": GK} for v in verbs],
        "certification": {"value": cert, "basis": GK},
        "language_type": {"value": lang, "basis": GK},
        "annotation_note": note or "",
    }
    if cert:
        e["certification_scope"] = {"value": scope, "basis": GK}
    A[stem(prefix)] = {"decision": "new", "variant_of": None, "reason": reason, "entry": e}


# ---------------------------------------------------------------- B

new("broadcast-programming", "Broadcast programming", "skill",
    "Selecting and scheduling the shows and other content that a television or radio station or network broadcasts.",
    "A broadcasting scheduling skill; no nearest entry is the same.")
no("broadcom", "Broadcom is a company.")
unsure("broker-s-market-analysis", "It looks like a real-estate valuation analysis, but I cannot tell it from a comparative market analysis or a financial-market analysis by a broker.")
no("browsing", "A generic word for looking through web pages or goods, not a named skill.")
new("browzwear", "Browzwear", "tool",
    "3D fashion design software for creating and simulating garments digitally before they are made.",
    "A named fashion-industry software product.")
new("brute-force", "Brute-force search", "method",
    "Solving a problem by systematically trying every possible candidate solution until one works.",
    "A general problem-solving approach; the tag could also mean the security attack, which uses the same approach.")
new("btrieve", "Btrieve", "tool",
    "A record-oriented database engine, originally from Pervasive Software, that stores and retrieves records through key indexes.",
    "A named database engine; no nearest entry is the same.",
    relations=[("related", "w9n8sme4x4")])
no("buckets", "A generic word, not a named skill.")
new("budtending", "Budtending", "skill",
    "Advising customers on and selling cannabis products in a dispensary.",
    "The activity of a budtender in a cannabis shop.")
new("bug-tracking-systems", "Bug tracking systems", "tool",
    "Software used to record, prioritise and follow software defects until they are fixed.",
    "A category of software tools, classed like Accounting software.")
new("builder-s-risk-insurance", "Builder's risk insurance", "knowledge",
    "Insurance that covers a building and its materials against damage while it is under construction or renovation.",
    "A recognised type of property insurance.")
unsure("building-control", "It can mean the building-regulations approval function (for example in the UK) or building automation controls, and the tag alone does not say which.")
new("building-crates-and-skids", "Building crates and skids", "skill",
    "Constructing wooden crates and skids to ship and support goods.",
    "A packaging and carpentry task.")
no("buildout", "A generic word for fitting out a space or expanding something, not a named skill.")
new("bullet-software", "Bullet Physics", "library",
    "An open-source physics engine library for real-time collision detection and rigid-body simulation in games, robotics and visual effects.",
    "The software called Bullet is, as far as I know, the Bullet physics engine.")
new("bulma", "Bulma", "framework",
    "An open-source CSS framework built on Flexbox that provides ready-made layout and interface components.",
    "A named CSS framework.")
no("bumpers", "A generic word for a part or guard, not a named skill.")
no("bungalow", "A type of house, not a skill.")
unsure("bunu-language", "Bunu is the name of a Hmong-Mien language in China and also of a Yoruba dialect in Nigeria, and the tag does not say which.")
new("burn-down-chart", "Burndown chart", "method",
    "A chart that plots the work remaining in a project against time, used by agile teams to track progress.",
    "A named agile reporting technique.")
no("burn-injuries", "A medical condition, not a capability.")
unsure("business-continuity-risk", "It names a type of risk; I cannot tell whether the intended skill is business continuity planning or risk management.")
new("business-excellence", "Business excellence", "method",
    "A management approach that applies quality-management principles and models such as the EFQM Excellence Model to improve an organisation's performance.",
    "A recognised quality-management approach.")
new("business-integration-softwares", "Business integration software", "tool",
    "Software that connects business applications and data sources so that they can exchange information.",
    "A category of software tools, classed like Accounting software.")
no("business-model", "A generic business concept rather than a named skill or method.")
no("business-objectives", "A generic business word, not a skill.")
new("business-process-analysis", "Business process analysis", "skill",
    "Studying how a business process works in order to find problems and ways to improve it.",
    "A recognised analysis skill; no nearest entry is the same.")
unsure("business-transaction-services", "It reads as the name of an advisory or software service line, and I do not know which concept is meant.")
new("butchering", "Butchering", "skill",
    "Cutting and trimming animal carcasses into cuts of meat for sale or cooking.",
    "A manual meat-trade skill.")
new("butterknife", "Butter Knife", "library",
    "An Android library that uses annotations to bind views, resources and event handlers to fields and methods.",
    "The Android library written as Butter Knife; the tag drops the space.")
new("bzip2", "bzip2", "tool",
    "A free compression program and file format that shrinks files using the Burrows-Wheeler transform and Huffman coding.",
    "A named compression tool.")

# ---------------------------------------------------------------- C

new("c3-js", "C3.js", "library",
    "A JavaScript library, built on D3, for making reusable charts.",
    "A named charting library; neither nearest entry is the same.")
unsure("ca-software-change-management", "Possibly a CA (now Broadcom) change-management product such as CA Harvest, but I cannot be sure of the product or of its exact name.")
new("caesarean-section", "Caesarean section", "skill",
    "Performing or assisting with the surgical delivery of a baby through an incision in the mother's abdomen and uterus.",
    "A surgical obstetric procedure; no nearest entry is the same.",
    variants=["Cesarean section", "C-section"])
new("caffe-b8020a", "Caffe", "framework",
    "A deep learning framework from Berkeley AI Research, known for speed and modularity and used mostly for image tasks.",
    "A named deep learning framework; the nearest entries are certifications and unrelated.")
new("caffe2", "Caffe2", "framework",
    "A lightweight deep learning framework from Facebook that succeeded Caffe and was later merged into PyTorch.",
    "A named deep learning framework, separate from Caffe.")
new("cairngorm", "Cairngorm", "framework",
    "An application framework for Adobe Flex that organises rich internet applications with the model-view-controller pattern.",
    "In a technology list this is the Adobe Flex framework, not the mountain range.")
new("cakewalk", "Cakewalk", "tool",
    "Digital audio workstation software for recording, editing and mixing music, formerly sold as SONAR.",
    "A named audio-production product.")
no("calculators", "A generic word for a device, not a named skill.")
unsure("calculus-removal", "It could mean removing dental calculus (scaling) or kidney stones, and the tag does not say which.")
no("call-centers", "A type of workplace, not a skill.")
new("call-connection-admission-control", "Call admission control", "method",
    "A telecommunications network mechanism that decides whether to accept a new call or connection by checking that enough resources remain to keep quality of service.",
    "A recognised network-management technique; no nearest entry is the same.")
new("callback-functions", "Callback function", "knowledge",
    "A function passed to other code as an argument so that the other code can call it later, for example when an event or task finishes.",
    "A basic programming concept, classed like B-tree as knowledge.")
new("calyx-point", "Calyx Point", "tool",
    "Mortgage loan origination software that lenders and brokers use to take applications and prepare loan files.",
    "A named mortgage software product.")
no("came-e40e60", "A fragment of an ordinary word with no skill meaning that I know.")
unsure("camera-api", "It names an interface that exists on several platforms (Android, iOS, the web), so no single product is meant.")
new("camera-calibration", "Camera calibration", "method",
    "Estimating a camera's internal parameters, lens distortion and position so that image measurements can be related to real-world geometry.",
    "A standard computer vision technique; the nearest entries are not the same.")
unsure("campaign-administration", "Too general: it could be marketing, fundraising or political campaign administration.")
new("canape", "CANape", "tool",
    "Software from Vector Informatik for measuring, calibrating and diagnosing electronic control units in vehicles.",
    "A named automotive engineering tool.")
no("canc-n-agreements", "An international climate agreement, not a capability.")
new("cancan", "CanCan", "library",
    "A Ruby on Rails authorisation library in which a single ability definition sets what each user may do.",
    "In a technology list this is the Rails gem, not the dance.")
new("canjs", "CanJS", "framework",
    "A JavaScript framework for building web applications with observable data, templates and components.",
    "A named JavaScript framework.")
no("cannabis-853e0a", "A plant and product, not a skill.")
new("cannabis-and-hemp-extraction", "Cannabis and hemp extraction", "skill",
    "Extracting cannabinoids and other compounds from cannabis or hemp plant material using solvents or CO2.",
    "A production process skill.")
new("cannabis-cultivation", "Cannabis cultivation", "skill",
    "Growing cannabis plants, including their care, harvest and curing.",
    "A cultivation skill; the nearest entries are not related.")
new("cannabis-regulations", "Cannabis regulations", "knowledge",
    "Knowledge of the laws and rules governing the growing, sale and use of cannabis, which differ by jurisdiction.",
    "A body of rules; Regulation SHO is a different regulation.")
new("canon-eos-flash-systems", "Canon EOS flash systems", "tool",
    "Canon's family of Speedlite flash units and wireless flash controls made for use with EOS cameras.",
    "A named photography equipment line.")
new("canva-software", "Canva", "platform",
    "An online graphic design platform for making presentations, social media posts and other visual content from templates.",
    "A named design product.",
    relations=[("related", "s46ycd317l")])
new("canvasjs", "CanvasJS", "library",
    "A JavaScript charting library that draws charts on an HTML5 canvas.",
    "A named charting library.")
new("capacity-management", "Capacity management", "skill",
    "Planning and monitoring resources so that capacity meets current and future demand.",
    "A recognised IT and operations skill; the nearest entries are not the same.")
new("capistrano", "Capistrano", "tool",
    "A Ruby-based tool for automating deployment and other tasks on remote servers over SSH.",
    "A named deployment tool.",
    verbs=["deploy"])
new("capital-asset-pricing-model", "Capital asset pricing model", "knowledge",
    "A finance model that relates the expected return of an asset to the risk-free rate and to the asset's sensitivity to market risk.",
    "A standard finance model. I give no CAPM variant because CAPM is also a PMI project-management credential.")
new("capture-one", "Capture One", "tool",
    "Photo-editing software from Phase One for processing RAW images and shooting with the camera connected to a computer.",
    "A named photo-editing product.")
new("capybara", "Capybara", "library",
    "A Ruby library for testing web applications by simulating how a user interacts with them.",
    "In a technology list this is the Ruby test library, not the animal.")
no("carbon-graphite", "A material, not a skill.")
unsure("cardiac-devices", "It names a class of equipment (pacemakers, defibrillators and similar); I cannot tell which skill is meant.")
new("cardiac-stress-tests", "Cardiac stress testing", "skill",
    "Conducting tests that record how the heart responds to physical exercise or to drugs that simulate exercise.",
    "A clinical procedure; no nearest entry is the same.")
new("cardiac-surgeries", "Cardiac surgery", "knowledge",
    "The surgical specialty that operates on the heart.",
    "A medical field.")
new("cardiac-valve-repair", "Cardiac valve repair", "skill",
    "Surgically reconstructing a damaged heart valve so that it works again without replacing it.",
    "A surgical procedure.")
new("cardio-pulmonary-resuscitation-cpr", "Cardiopulmonary resuscitation", "skill",
    "An emergency procedure that combines chest compressions and rescue breaths to keep blood and oxygen moving when someone's heart or breathing has stopped.",
    "The same concept as the next tag; both answered new with one name.",
    variants=["CPR"],
    relations=[("related", "gxbpx9za78")])
new("cardiopulmonary-resuscitation", "Cardiopulmonary resuscitation", "skill",
    "An emergency procedure that combines chest compressions and rescue breaths to keep blood and oxygen moving when someone's heart or breathing has stopped.",
    "The same concept as the Cardio-Pulmonary Resuscitation (CPR) tag; both answered new with one name.",
    variants=["CPR"])
new("cardiothoracic-surgeries", "Cardiothoracic surgery", "knowledge",
    "The surgical specialty that operates on organs in the chest, mainly the heart and lungs.",
    "A medical field, wider than cardiac surgery.")
new("cardiovascular-coding", "Cardiovascular coding", "skill",
    "Assigning standard diagnosis and procedure codes to heart and blood-vessel care records for billing and reporting.",
    "A medical coding specialty.")
new("cardiovasculars-physiology", "Cardiovascular physiology", "knowledge",
    "The study of how the heart and blood vessels work.",
    "A field of physiology.")
new("care-coordination", "Care coordination", "skill",
    "Organising a patient's care across providers and services so that the patient's needs are met.",
    "A healthcare skill; the nearest entries are physical abilities and not the same.")
no("career-guide", "A document or job title, not a skill.")
unsure("carew-language", "I do not know a language called Carew.")
new("carib-language", "Carib", "human-language",
    "A Cariban language spoken by the Kalina (Kari'nja) people along the coasts of northern South America.",
    "A human language; the legacy language list agrees.",
    lang="human")
new("carrot2", "Carrot2", "tool",
    "An open-source search results clustering engine that groups documents and search results into topics.",
    "A named open-source tool.")
new("ccure-security-and-event-management-syst", "C-CURE", "platform",
    "An access control and security event management system made by Software House, a Johnson Controls business.",
    "A named physical security product.")
no("cd-player", "A consumer device, not a skill.")
new("cdc-cyber-cdc-hardware", "CDC Cyber", "platform",
    "A line of mainframe and supercomputer systems made by Control Data Corporation from the 1970s.",
    "A named historical computer hardware line.")
new("cdl-class-b-license", "Class B commercial driver's license", "credential",
    "A US state-issued commercial driver's license for driving a single heavy vehicle, or one towing a light trailer.",
    "A US driving licence issued by each state under federal standards.",
    variants=["Class B CDL"],
    cert=True, scope="many-issuers")
new("cdl-class-c-license", "Class C commercial driver's license", "credential",
    "A US state-issued commercial driver's license for vehicles that fit neither Class A nor Class B but carry 16 or more passengers or hazardous materials that need placards.",
    "A US driving licence issued by each state under federal standards.",
    variants=["Class C CDL"],
    cert=True, scope="many-issuers")
unsure("cfc-refrigeration-certification", "Probably the US EPA refrigerant-handling certification, but I cannot confirm the scheme or who awards it.")
new("cih", "Certified Industrial Hygienist", "credential",
    "A professional certification for industrial hygienists, who anticipate, recognise, evaluate and control workplace health hazards.",
    "CIH most often means this credential; it can also be an abbreviation for other things such as the Chartered Institute of Housing.",
    cert=True, scope="single-issuer",
    note="The legacy lists class CIH as a skill, but it is a credential.")
new("cisco-certified-network-professional-sec", "CCNP Security", "credential",
    "A Cisco professional-level certification for engineers who design, implement and operate network security.",
    "A Cisco certification; the nearest entries are other bodies' credentials.",
    variants=["Cisco Certified Network Professional Security"],
    cert=True, scope="single-issuer")
new("ckeditor", "CKEditor", "library",
    "A JavaScript rich-text editor that lets users format content in web pages.",
    "A named editor component.")
new("cnc-programming", "CNC programming", "skill",
    "Writing the instructions, often in G-code, that direct computer numerically controlled machine tools to cut or shape parts.",
    "A machining skill; the nearest entries are different kinds of programming.")
new("cnor-certification", "Certified Perioperative Nurse (CNOR)", "credential",
    "A certification for registered nurses who work in the operating room, awarded by the Competency and Credentialing Institute.",
    "A single-body nursing certification.",
    variants=["CNOR"],
    cert=True, scope="single-issuer")
new("comit", "COMIT", "programming-language",
    "An early string-processing programming language developed at MIT in the 1950s for linguistic research and machine translation.",
    "A historical programming language; AWS CodeCommit is not related.",
    lang="programming")
new("coso-framework", "COSO framework", "standard",
    "A framework published by the Committee of Sponsoring Organizations of the Treadway Commission for designing and assessing internal control and enterprise risk management.",
    "A published control framework, classed as a standard.")
new("cpython", "CPython", "tool",
    "The reference implementation of the Python language, written in C.",
    "A specific Python implementation, not the language itself.",
    relations=[("related", "pk7cebmtg6"), ("related", "wpvzxxfp8w")])
no("cs-gas", "A chemical riot-control agent, not a skill.")
unsure("cssp-analyst", "It is a US DoD cybersecurity service provider workforce category that requires approved certifications; I cannot tell whether it counts as a credential.")
unsure("cssp-auditor", "It is a US DoD cybersecurity service provider workforce category that requires approved certifications; I cannot tell whether it counts as a credential.")
unsure("cssp-incident-responder", "It is a US DoD cybersecurity service provider workforce category that requires approved certifications; I cannot tell whether it counts as a credential.")
unsure("cssp-infrastructure-support", "It is a US DoD cybersecurity service provider workforce category that requires approved certifications; I cannot tell whether it counts as a credential.")
new("cu-seeme", "CU-SeeMe", "tool",
    "An early internet videoconferencing program developed at Cornell University.",
    "A named historical software product.")
new("curl-dfc1a3", "cURL", "tool",
    "A command-line tool and library for transferring data with URLs over protocols such as HTTP and FTP.",
    "In job lists this is almost always the cURL tool; a separate programming language also called Curl exists.")


def main():
    reqs = sorted(p.stem for p in REQ.glob("*.json"))
    missing = [r for r in reqs if r not in A]
    extra = [a for a in A if a not in reqs]
    if missing or extra:
        sys.exit(f"missing {missing}, extra {extra}")
    OUT.mkdir(exist_ok=True)
    for s, ans in A.items():
        (OUT / f"{s}.json").write_text(json.dumps(ans, indent=1, ensure_ascii=False) + "\n")
    from collections import Counter
    print(len(A), Counter(a["decision"] for a in A.values()))


main()
