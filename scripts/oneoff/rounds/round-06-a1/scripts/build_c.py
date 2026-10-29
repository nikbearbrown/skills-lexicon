import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from h import *

A = {}

A[100] = ("International General Certificate Of Secondary Education", new(
    "International General Certificate of Secondary Education", "credential",
    "An internationally aimed secondary-school qualification, taken at about age 16 and awarded by several exam boards such as Cambridge and Pearson Edexcel, comparable to the GCSE.",
    variants=["IGCSE"], rel=[("related", "h1v8wztmne")], cert=True, scope="many-issuers"))

A[101] = ("International Standard Book Number", new(
    "International Standard Book Number", "standard",
    "A unique number that identifies a particular edition of a book or similar publication, defined by the ISO 2108 standard.",
    variants=["ISBN"]))

A[102] = ("International Tourism", ns("An industry or sector, not a skill."))

A[103] = ("Internet Communications", unsure("Could mean communicating online (close to Digital communications) or internet communication technology."))

A[104] = ("Internet Control Message Protocol", new(
    "Internet Control Message Protocol", "standard",
    "A network-layer protocol, defined in RFC 792, that IP devices use to send error messages and operational information, such as the echo requests used by ping.",
    variants=["ICMP"], rel=[("related", "ff2sy7qrjo")]))

A[105] = ("Internet Message Access Protocols", new(
    "Internet Message Access Protocol", "standard",
    "An email protocol that lets a mail client read and manage messages that stay stored on the mail server.",
    variants=["IMAP"]))

A[106] = ("Internet Protocolss", new(
    "Internet protocol suite", "standard",
    "The set of communication protocols, such as IP, TCP and UDP, that computers use to exchange data over the internet and similar networks.",
    variants=["TCP/IP", "Internet protocols"], rel=[("broader", "fnhev4v1dn")]))

A[107] = ("Internet Resource Locator", unsure("Probably a garbled expansion of URL (Uniform Resource Locator), but that is not certain."))

A[108] = ("Interpret Drawings", new(
    "Reading technical drawings", "skill",
    "Reading technical drawings such as blueprints and schematics to understand the shapes, dimensions and instructions they show.",
    variants=["Blueprint reading"], rel=[("related", "fbmyyojcj3")]))

A[109] = ("Interpret Law", new(
    "Interpreting law", "skill",
    "Working out what statutes, regulations and court decisions mean and how they apply to a particular situation."))

A[110] = ("Interpreting Contracts In English Laws", new(
    "Interpreting contracts under English law", "skill",
    "Working out what the terms of a contract mean and how they apply under the law of England and Wales."))

A[111] = ("InterQual Criteria", new(
    "InterQual", "tool",
    "A set of evidence-based clinical criteria, sold as software, that hospitals and insurers use in utilization review to judge whether admissions and levels of care are medically necessary.",
    variants=["InterQual criteria"]))

A[112] = ("Intervertebral Disk Disease", ns("A medical condition, not a skill."))
A[113] = ("Intoxication", ns("A medical condition or symptom, not a skill."))

A[114] = ("Intradermal", new(
    "Intradermal injection", "skill",
    "Injecting a small amount of a substance into the layer of skin just under the surface, as in a tuberculin skin test."))

A[115] = ("Intraoperative Neurophysiological Monitoring", new(
    "Intraoperative neurophysiological monitoring", "skill",
    "Using electrical tests such as EEG, evoked potentials and EMG during surgery to monitor the nervous system and warn the surgeon of possible injury.",
    variants=["IONM", "Intraoperative neuromonitoring", "Intraoperative neurophysiologic monitoring"],
    rel=[("related", "rfizzr2lin"), ("related", "ycridfb6ao")]))

A[116] = ("Intraoral Cameras", new(
    "Intraoral cameras", "tool",
    "Small pen-shaped cameras that dentists use to take enlarged pictures of the inside of a patient's mouth.",
    variants=["Intraoral camera"]))

A[117] = ("Intravenous Hydration", new(
    "Intravenous hydration", "skill",
    "Giving fluids directly into a vein through an IV line to treat or prevent dehydration.",
    variants=["IV hydration"]))

A[118] = ("Intravenous (IV) Fusions", new(
    "Intravenous infusion", "skill",
    "Giving fluids, medicines or nutrients into a vein through an IV line, using a drip or a pump.",
    variants=["IV infusion", "IV infusions"],
    reason="Almost certainly a typo for 'Intravenous (IV) infusions'."))

A[119] = ("Inventory Management Software", new(
    "Inventory management software", "tool",
    "Software for tracking stock levels, orders, sales and deliveries so that a business knows what it has and where."))

A[120] = ("Investigating Drug Trafficking", new(
    "Investigating drug trafficking", "skill",
    "Investigating the making, transport and sale of illegal drugs, including surveillance, informants, evidence gathering and tracing money."))

A[121] = ("Investigative Interviewing", new(
    "Investigative interviewing", "skill",
    "Questioning witnesses, victims and suspects in a structured, non-coercive way to get accurate and complete accounts for an investigation."))

A[122] = ("Investigator'S Brochure", new(
    "Investigator's brochure", "skill",
    "Writing and maintaining the investigator's brochure, the document used in clinical trials that summarises the clinical and non-clinical data on the study drug for the people running the trial."))

A[123] = ("Investment Certificate", unsure("Could be a financial product or a qualification from a body such as the CISI, and no single credential can be named."))

A[124] = ("InVision", new(
    "InVision", "platform",
    "A web-based digital product design platform for prototyping screens, collaborating on them and handing them off to developers, which was discontinued at the end of 2024."))

A[125] = ("Invoice Processing", new(
    "Invoice processing", "skill",
    "Receiving, checking, recording and paying supplier invoices as part of accounts payable."))

A[126] = ("Io.js", new(
    "Io.js", "platform",
    "A fork of the Node.js JavaScript runtime, started in 2014 and merged back into Node.js in 2015."))

A[127] = ("Ionic2", new(
    "Ionic 2", "framework",
    "The second major version of the Ionic framework for building mobile apps with web technologies, rebuilt on Angular to replace the AngularJS-based first version."))

A[128] = ("Irb", unsure("Could be Institutional Review Board, Ruby's interactive shell irb, or something else; nothing here shows which."))

A[129] = ("Ironmq", new(
    "IronMQ", "tool",
    "A hosted message-queue service from Iron.io for passing messages between the parts of an application."))

A[130] = ("IronPython", new(
    "IronPython", "tool",
    "An implementation of the Python language for the .NET platform.",
    rel=[("related", "pk7cebmtg6"), ("related", "rtrc1foglt")]))

A[131] = ("Irrigation (Agriculture)", new(
    "Irrigation (agriculture)", "skill",
    "Supplying water to crops or land through channels, sprinklers or drip lines, and operating and maintaining the equipment that does so."))

A[132] = ("Irrigation (Health)", new(
    "Irrigation (health)", "skill",
    "Flushing a wound, body cavity, eye, ear or catheter with a stream of sterile fluid to clean it or clear it out."))

A[133] = ("ISO/IEC 27001 Series", vo("b9atybxdgh", "'27001 series' is a common loose name for the ISO/IEC 27000 family."))

A[134] = ("Iso/iec", ns("A prefix shared by many standards, not a standard by itself."))

A[135] = ("Issue Management", unsure("Means tracking and resolving project issues in some roles and managing public-policy issues in communications roles."))

A[136] = ("Issue Tracking Systems", new(
    "Issue tracking systems", "tool",
    "Software for recording, assigning and following issues such as software bugs, tasks and support requests until they are resolved.",
    variants=["Issue tracker", "Issue tracking software"],
    rel=[("related", "ve6il0e4wg")]))

A[137] = ("Italics", ns("A text-formatting option, not a skill."))

A[138] = ("Iteratee", unsure("Means different things in functional programming (Haskell, Scala) and in JavaScript utility libraries; nothing here shows which."))

A[139] = ("Ito'S Lemma", new(
    "Itô's lemma", "knowledge",
    "A result in stochastic calculus that gives the change in a function of a random process such as Brownian motion, used in finance to price derivatives.",
    variants=["Ito's lemma", "Itô's formula"]))

A[140] = ("Ivalua (Spend Management Software)", new(
    "Ivalua", "platform",
    "A cloud spend-management platform for procurement, covering sourcing, contracts, supplier management and purchasing."))

A[141] = ("Jacorb", new(
    "JacORB", "library",
    "An open-source Java implementation of the CORBA object request broker."))

A[142] = ("JAD", unsure("Could be Joint Application Development workshops or the JAD Java decompiler; nothing here shows which."))

A[143] = ("JAFAN", new(
    "JAFAN", "standard",
    "A series of Joint Air Force-Army-Navy publications on security policy for US Department of Defense special access programs, best known for JAFAN 6/3 on protecting such information in information systems."))

A[144] = ("Jamf Certification", new(
    "Jamf certification", "credential",
    "Certifications awarded by Jamf, the Apple device management software company, showing skill in managing Apple devices with Jamf products.",
    cert=True, scope="single-issuer"))

A[145] = ("Janssen Biotech", ns("A company, not a skill."))

A[146] = ("Janus", unsure("Could be the Janus WebRTC server, JanusGraph or something else; nothing here shows which."))

A[147] = ("JAR (Java ARchive)", new(
    "Java Archive", "standard",
    "A file format, based on ZIP, that packages compiled Java classes, resources and metadata into one compressed file.",
    variants=["JAR"]))

A[148] = ("Jargon", ns("A generic word, not a skill."))

A[149] = ("Jasmine", new(
    "Jasmine", "framework",
    "A behaviour-driven development framework for testing JavaScript code."))

write_all(A)
