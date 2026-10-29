"""Build work/responses/*.json for batch 002 from hand-written answers. Run: python3 -I work/build_responses.py"""
import glob
import json
import os
from pathlib import Path

ROOT = Path("/home/user/agent1/skills-lexicon")
GK = "general-knowledge"
A = {}   # term -> response dict


def new(term, name, kind, definition, variants=(), relations=(), verbs=(), cert=False, lang=None,
        note="", reason="A skill, tool or concept I can define from general knowledge."):
    A[term] = {
        "decision": "new", "variant_of": None, "reason": reason,
        "entry": {
            "preferred_name": name, "kind": kind, "definition": definition, "definition_basis": GK,
            "variants": [{"label": v, "basis": GK} for v in variants],
            "relations": [{"type": t, "target": i, "basis": GK} for t, i in relations],
            "verbs": [{"verb": v, "basis": GK} for v in verbs],
            "certification": {"value": cert, "basis": GK},
            "language_type": {"value": lang, "basis": GK},
            "annotation_note": note,
        },
    }


def nas(term, reason):
    A[term] = {"decision": "not_a_skill", "variant_of": None, "reason": reason, "entry": None}


def unsure(term, reason):
    A[term] = {"decision": "unsure", "variant_of": None, "reason": reason, "entry": None}


def variant(term, target, reason):
    A[term] = {"decision": "variant_of", "variant_of": target, "reason": reason, "entry": None}


# ---------------------------------------------------------------- 0-9
new("1Password", "1Password", "tool",
    "A commercial password manager that stores logins and other secrets in encrypted vaults.",
    verbs=["use", "administer"])
new("360 Campaigns", "360 campaigns", "skill",
    "Planning marketing campaigns that carry one message across many channels, such as TV, digital, print and in-store.",
    variants=["360-degree campaigns"], verbs=["plan", "run"])
new("3D Modeling Softwares", "3D modeling software", "tool",
    "Software used to build three-dimensional models of objects or scenes, for example for design, animation or games.",
    variants=["3D modelling software"], verbs=["use"])
unsure("3D Production", "Could mean 3D animation or CGI production or 3D printing production; the tag alone does not say which.")
new("3D Touch", "3D Touch", "knowledge",
    "A pressure-sensitive touchscreen feature on some Apple iPhones that responds differently to light and firm presses.")
new("3DMark (Computer Benchmarking )", "3DMark", "tool",
    "A benchmark program that measures the graphics and processing performance of computers.",
    verbs=["run"])
new("4D Modelling (Construction)", "4D modeling (construction)", "method",
    "Linking a three-dimensional building model to the construction schedule so the building work can be viewed step by step over time.",
    variants=["4D BIM"], verbs=["create"])
new("50% Tissue Culture Infective Dose (TCID50)", "50% tissue culture infectious dose (TCID50)", "method",
    "The amount of virus that infects half of the inoculated cell cultures, used as a unit to measure virus infectivity in the laboratory.",
    variants=["TCID50"], verbs=["perform"])
nas("AAA Video Games", "Names a market category of video games by budget, not a skill, tool or method.")
unsure("Abacus", "Could be the counting frame, a person's abacus calculation skill, or a software product with this name; the tag does not say.")

# ---------------------------------------------------------------- 10-19
new("ABC Javascript Renderer", "ABC JavaScript Renderer", "library",
    "A JavaScript library that draws music written in ABC notation as sheet music in a web page.",
    relations=[("related", "h60l8olauw")])
new("ABEC Scale", "ABEC scale", "knowledge",
    "A rating scale from the Annular Bearing Engineers' Committee that grades the manufacturing tolerances of precision ball bearings.",
    variants=["ABEC rating"])
unsure("Abeel Java Toolkit", "The name suggests a Java library by someone named Abeel, but I cannot say what it contains.")
unsure("Ablation", "Has several unrelated senses (machine-learning ablation studies, medical ablation, laser ablation); the tag does not say which.")
variant("ABMLI Certified", "u3ojnio176", "ABMLI is the American Board of Medical Laboratory Immunology, the same certification as the nearest entry.")
new("ABMM Certified", "American Board of Medical Microbiology certification", "credential",
    "Certification by the American Board of Medical Microbiology in medical microbiology.",
    variants=["ABMM certification", "ABMM"], cert=True)
unsure("ACA Insturctor Certificate", "ACA stands for several organisations (for example American Canoe Association, American Counseling Association); the tag does not say which.")
new("Academic English", "Academic English", "skill",
    "The register of English used for scholarly reading, writing and speaking, such as essays and research papers.",
    relations=[("broader", "tsdlbd9gt0")])
unsure("Academic History", "Could mean the discipline of history or a person's educational record; the tag does not say which.")
nas("Academic Papers", "Names a kind of document, not a skill; the skill would be academic writing or research publishing.")

# ---------------------------------------------------------------- 20-29
new("Academic Record-Keeping", "Academic record-keeping", "skill",
    "Maintaining accurate student records such as enrolment, grades and transcripts for a school or university.",
    verbs=["maintain"])
unsure("ACCEL/Exchange", "Appears to be the name of a payment or ATM network rather than a skill, but I cannot confirm what it is.")
new("Accelerated Failure Time Models", "Accelerated failure time models", "method",
    "A class of survival-analysis regression models in which the covariates act multiplicatively on the time until an event occurs.",
    variants=["accelerated failure time model", "AFT model"], verbs=["fit"])
new("Accelerated Mobile Pages", "Accelerated Mobile Pages", "framework",
    "An open-source HTML framework, started by Google, for building web pages that load quickly on mobile devices.")
new("Acceptance and Commitment Therapy (ACT)", "Acceptance and Commitment Therapy", "method",
    "A form of psychotherapy that helps people accept difficult thoughts and feelings and commit to actions that fit their values.",
    verbs=["deliver"])
new("Access Point Name", "Access point name", "knowledge",
    "The name of a gateway between a mobile network and another network such as the internet, which a device uses to set up a data connection.",
    verbs=["configure"])
new("Accessioning", "Accessioning", "skill",
    "Formally logging a received specimen or item and giving it a unique identifying number.",
    verbs=["perform"])
unsure("Accordion", "Could be the musical instrument (playing it is a skill) or the user-interface component; the tag does not say which.")
new("Accountancy And Passenger Ticket Issuing System (APTIS)", "Accountancy and Passenger Ticket Issuing System", "tool",
    "A computerised system for issuing passenger tickets and accounting for the sales.",
    variants=["APTIS"], verbs=["operate"])
new("Accounting Cycle", "Accounting cycle", "method",
    "The sequence of steps an accountant follows from recording a business's transactions to preparing financial statements and closing the books.")

# ---------------------------------------------------------------- 30-39
unsure("Accounting Record Management System", "A generic phrase that could name a particular product or just the practice of managing accounting records; the tag does not say which.")
new("Accounting Softwares", "Accounting software", "tool",
    "Software for recording financial transactions and producing ledgers, invoices and financial reports.",
    verbs=["use"])
new("Accounts Receivable Management", "Accounts receivable management", "skill",
    "Tracking invoices and collecting the money that customers owe a business.",
    verbs=["manage"])
unsure("Accounts Receivable Management Solutions",
       "Probably software or services for the same practice as 'Accounts Receivable Management' in this batch, which is not in nearest; a person should merge or reject.")
new("Accumulated Benefit Obligation", "Accumulated benefit obligation", "knowledge",
    "The present value of pension benefits earned to date, measured on current pay levels without assuming future pay rises.")
nas("Achievement-driven", "A personality-trait adjective, not a skill, tool or method.")
nas("Achievement-oriented", "A personality-trait adjective, not a skill, tool or method.")
new("ACL Analytics (Audit Command Language)", "ACL Analytics", "tool",
    "Data analysis software that auditors and finance teams use to test large data sets, scripted with a command language called ACLScript.",
    verbs=["use"], cert=False, lang=None,
    note="ACL Analytics is the software product and its scripting language is ACLScript, so I treated the tag as a tool, not a language.")
nas("Action Button", "A user-interface or hardware button, not a skill.")
new("Action for Climate Empowerment (ACE)", "Action for Climate Empowerment", "knowledge",
    "The UN climate process's term for work on climate education, training, public awareness, public participation and access to information.")

# ---------------------------------------------------------------- 40-49
new("Activated Sludge", "Activated sludge", "method",
    "A wastewater treatment process in which air and a mixed community of microorganisms break down the organic matter in sewage.",
    verbs=["operate"])
new("Active Hdl", "Active-HDL", "tool",
    "An integrated design and simulation environment from Aldec for FPGA and digital-logic designs written in hardware description languages such as VHDL and Verilog.",
    verbs=["simulate"])
new("Active Pharmaceutical Ingredients", "Active pharmaceutical ingredient", "knowledge",
    "The component of a medicine that produces its intended therapeutic effect.",
    variants=["active pharmaceutical ingredients"])
new("Activepivot", "ActivePivot", "tool",
    "An in-memory analytics engine from ActiveViam for real-time aggregation and multidimensional analysis of large data sets.")
new("ActivePython", "ActivePython", "tool",
    "A commercially supported distribution of the Python programming language from ActiveState.",
    relations=[("related", "pk7cebmtg6")])
new("Activities Of Daily Living (ADLs)", "Activities of daily living", "knowledge",
    "The basic self-care tasks of everyday life, such as bathing, dressing, eating and moving about, that carers help with and clinicians use to assess independence.",
    verbs=["assist"])
new("Activity Director Certified", "Activity Director Certified", "credential",
    "A certification for people who plan and run activity programs for residents of long-term care and similar facilities.",
    cert=True)
new("Actuarial Exams", "Actuarial exams", "knowledge",
    "The series of professional examinations set by actuarial societies such as the Society of Actuaries and the Casualty Actuarial Society, which candidates pass on the way to actuarial credentials.",
    variants=["actuarial exam"], cert=False,
    note="The exams are tests set by actuarial societies; the credentials (ASA, FSA, ACAS, FCAS) are awarded after passing them.")
new("Acunetix", "Acunetix", "tool",
    "A web application security scanner that tests websites for vulnerabilities such as SQL injection and cross-site scripting.",
    verbs=["scan"])
new("Acute Care Nurse Practitioner", "Acute Care Nurse Practitioner", "credential",
    "A nurse practitioner credential for providing advanced care to patients with acute, critical or complex illnesses.",
    relations=[("related", "u0nv7nrdlk")], cert=True)

# ---------------------------------------------------------------- 50-59
nas("Acute Liver Failure", "A medical condition, not a skill, tool or method.")
new("AD Model Builder (ADMB)", "AD Model Builder", "tool",
    "Open-source software for fitting complex nonlinear statistical models using automatic differentiation.",
    variants=["ADMB"], verbs=["fit"])
new("Adaboost", "AdaBoost", "method",
    "A machine-learning algorithm that combines many weak classifiers into one strong classifier by reweighting the training examples at each round.",
    variants=["Adaptive Boosting"], verbs=["apply"])
new("Adaptabilities", "Adaptability", "ability",
    "The capacity to adjust to new conditions, tasks or environments.")
unsure("Adaptable Databse Systems", "Unclear whether this is a product, a research topic or a generic phrase, and 'Databse' is a misspelling.")
unsure("Adapter Scripting Language", "I do not know what this language is or which product it belongs to.")
new("Adaptive Equipments", "Adaptive equipment", "tool",
    "Devices and tools designed or modified to help people with disabilities or injuries do everyday tasks.")
new("Adaptive Insights", "Adaptive Insights", "tool",
    "Cloud-based business planning, budgeting and forecasting software that Workday acquired in 2018.",
    variants=["Workday Adaptive Planning"], verbs=["use"])
unsure("Adaptive Insights (Software)",
       "Appears to be the same product as 'Adaptive Insights' in this batch, which is not in nearest, so I cannot mark it variant_of; a person should merge.")
new("Adaptive Leadership", "Adaptive leadership", "method",
    "A leadership approach, developed from the work of Ronald Heifetz and Marty Linsky, that focuses on helping groups adapt to difficult challenges.")

# ---------------------------------------------------------------- 60-69
new("ADDIE Instructional Design Model", "ADDIE model", "method",
    "An instructional design process with five phases: analysis, design, development, implementation and evaluation.",
    variants=["ADDIE"], verbs=["apply"])
new("Adjudication Process", "Adjudication process", "method",
    "The formal process of reviewing a claim, application or dispute and deciding the outcome under set rules.")
unsure("Administered Payroll", "The phrase is odd; it may mean payroll administration, but I cannot be sure of the intended concept.")
nas("Administrative Law Review", "Appears to be the name of a law journal, not a skill.")
new("Administrative Laws", "Administrative law", "knowledge",
    "The body of law governing how government agencies make rules and decisions and how those actions can be challenged.",
    variants=["administrative laws"])
nas("Administrative Skills", "A generic umbrella label, not one specific skill.")
unsure("Admissions Operation", "Could mean school or college admissions or hospital patient admissions; the tag does not say which.")
new("Adobe Analytics", "Adobe Analytics", "tool",
    "Adobe's product for measuring and analysing customer behaviour on websites and apps.",
    verbs=["analyze"])
new("Adobe Experience Platform Launch", "Adobe Experience Platform Launch", "tool",
    "Adobe's tag management system for deploying and managing marketing and analytics tags on websites and apps.",
    variants=["Adobe Launch"], verbs=["configure"])
new("Adobe PhotoDeluxe", "Adobe PhotoDeluxe", "tool",
    "A discontinued consumer photo-editing program from Adobe, aimed at home users rather than professionals.",
    verbs=["use"])

# ---------------------------------------------------------------- 70-79
unsure("ADP/SIS Auto-Cage System (For Brokerage Firms)", "I do not know this brokerage back-office system well enough to define it.")
new("AI Copywriting", "AI copywriting", "skill",
    "Writing marketing and advertising copy with the help of generative AI tools.",
    verbs=["write"])
new("AKTA (Chromatography Technology)", "ÄKTA", "tool",
    "A family of liquid chromatography systems, now sold by Cytiva, used mainly to purify proteins and other biomolecules.",
    variants=["AKTA"], verbs=["operate"])
unsure("AMAP", "AMAP could stand for several credentials or terms, and I cannot tell which one this is.")
unsure("AMAX Cerfitications", "I cannot tell what AMAX refers to or whether any credential with that name exists; 'Cerfitications' is a misspelling.")
new("(American Society For Quality) ASQ Certified", "ASQ certification", "credential",
    "A professional certification awarded by the American Society for Quality, in fields such as quality engineering, auditing and Six Sigma.",
    variants=["American Society for Quality certification", "ASQ certified"], cert=True)
new("AMPScript", "AMPscript", "programming-language",
    "Salesforce Marketing Cloud's scripting language for personalizing the content of emails, landing pages and other messages.",
    lang="programming", verbs=["write"])
new("AMX Programming", "AMX programming", "skill",
    "Writing control programs for AMX audio-visual control systems, typically in the NetLinx language.",
    verbs=["program"])
unsure("ANS SureRemote Service", "I do not know what this service is or which company offers it.")
new("APache EXtenSion Tool (APXS)", "apxs", "tool",
    "A command-line tool of the Apache HTTP Server for building and installing extension modules as dynamic shared objects.",
    variants=["APXS"], verbs=["use"])

# ---------------------------------------------------------------- 80-89
unsure("APN-Series Radar", "Possibly a military or aviation radar designation, but I cannot say what it is.")
unsure("ARGO BankPro", "I cannot confirm what this banking software is or who makes it.")
new("ARP4754", "ARP4754", "knowledge",
    "An SAE International recommended practice with guidelines for developing civil aircraft and their systems, including requirements and development assurance.",
    variants=["ARP4754A", "SAE ARP4754"])
new("ASC 340", "ASC 340", "knowledge",
    "The FASB Accounting Standards Codification topic on other assets and deferred costs, such as capitalised costs of obtaining and fulfilling customer contracts.")
new("ASP.NET Core MVC", "ASP.NET Core MVC", "framework",
    "A Microsoft web framework for building web apps and APIs with the model-view-controller pattern on ASP.NET Core.",
    verbs=["build"])
new("ASP.NET Identity", "ASP.NET Identity", "library",
    "Microsoft's membership system for adding user accounts, sign-in and role-based authorization to ASP.NET applications.",
    verbs=["implement"])
new("ASP.NET Razor", "ASP.NET Razor", "markup-language",
    "A markup syntax from Microsoft for embedding C# or Visual Basic code in HTML to generate web pages on the server.",
    lang="other", verbs=["write"])
new("ASP.NET Web API", "ASP.NET Web API", "framework",
    "A Microsoft framework for building HTTP-based web services and APIs on .NET.",
    verbs=["build"])
new("AVEVA PI (Software)", "AVEVA PI System", "tool",
    "A data infrastructure for collecting, storing and analysing real-time industrial process data, originally from OSIsoft and now sold by AVEVA.",
    variants=["OSIsoft PI", "PI System"], verbs=["use"])
new("AWS CloudFormation", "AWS CloudFormation", "tool",
    "An Amazon Web Services service that provisions and manages cloud resources from templates written in JSON or YAML.",
    variants=["CloudFormation"], relations=[("broader", "lpsnz8mgp5")], verbs=["write", "deploy"])

# ---------------------------------------------------------------- 90-99
new("AWS CloudHSM", "AWS CloudHSM", "tool",
    "An Amazon Web Services service that provides dedicated hardware security modules in the cloud for generating and storing cryptographic keys.",
    variants=["CloudHSM"])
new("AWS CloudTrail", "AWS CloudTrail", "tool",
    "An Amazon Web Services service that records actions taken in an AWS account, such as API calls, for auditing and security analysis.",
    variants=["CloudTrail"])
new("AWS CodeBuild", "AWS CodeBuild", "tool",
    "An Amazon Web Services service that compiles source code, runs tests and produces build artifacts.",
    variants=["CodeBuild"])
new("AWS CodeCommit", "AWS CodeCommit", "tool",
    "An Amazon Web Services service that hosts private Git repositories.",
    variants=["CodeCommit"])
new("AWS Internet of Things (IoT)", "AWS IoT", "tool",
    "Amazon Web Services' set of services for connecting Internet of Things devices to the cloud and managing the data they send.")
new("AWS Networking", "AWS networking", "skill",
    "Designing and operating network connectivity on Amazon Web Services, using services such as Virtual Private Cloud, Route 53 and Direct Connect.",
    relations=[("broader", "fnhev4v1dn")])
new("AWS Outposts", "AWS Outposts", "tool",
    "An Amazon Web Services offering that installs AWS-managed infrastructure and services in a customer's own data center or facility.")
new("AWS SageMaker", "Amazon SageMaker", "tool",
    "An Amazon Web Services service for building, training and deploying machine-learning models.",
    variants=["SageMaker"], verbs=["train", "deploy"])
new("AWS Serverless", "AWS serverless", "skill",
    "Building and running applications on Amazon Web Services with managed, event-driven services such as AWS Lambda, without provisioning or managing servers.")
new(".NET Development", ".NET development", "skill",
    "Building software applications on Microsoft's .NET platform, using languages such as C#.",
    verbs=["develop"])


def main():
    files = sorted(glob.glob(str(ROOT / "work" / "requests" / "*.json")))
    out_dir = ROOT / "work" / "responses"
    out_dir.mkdir(exist_ok=True)
    terms = {}
    for f in files:
        req = json.loads(Path(f).read_text("utf-8"))
        terms[req["term"]] = (f, req)
    missing = set(terms) - set(A)
    extra = set(A) - set(terms)
    assert not missing, f"no answer for: {sorted(missing)}"
    assert not extra, f"answer without request: {sorted(extra)}"
    for term, resp in A.items():
        f, req = terms[term]
        near = {n["id"] for n in req["nearest"]}
        if resp["decision"] == "variant_of":
            assert resp["variant_of"] in near, (term, "variant_of not in nearest")
        if resp["entry"]:
            for r in resp["entry"]["relations"]:
                assert r["target"] in near, (term, r["target"], "relation target not in nearest")
            assert len(resp["entry"]["annotation_note"]) <= 135, term
        (out_dir / os.path.basename(f)).write_text(json.dumps(resp, indent=1, ensure_ascii=False) + "\n", "utf-8")
    from collections import Counter
    print(len(A), "responses written", dict(Counter(r["decision"] for r in A.values())))


main()
