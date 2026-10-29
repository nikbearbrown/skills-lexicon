import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from h import *

A = {}

A[50] = ("Information Leak Prevention", new(
    "Information leak prevention", "skill",
    "Stopping sensitive information from leaving an organisation without permission, using policies, training and technical controls such as data loss prevention software."))

A[51] = ("Information Source", ns("A generic phrase, not a skill."))

A[52] = ("Information Technology Audit", new(
    "Information technology audit", "skill",
    "Examining an organisation's IT systems, controls and processes to judge whether they protect assets, keep data accurate and follow policy and regulation.",
    variants=["IT audit", "Information systems audit"],
    rel=[("related", "ogfx5yxebl")],
    verbs=["conduct"]))

A[53] = ("InFusion Enterprise Control System", new(
    "InFusion Enterprise Control System", "platform",
    "An industrial control and operations software product from Invensys, later part of Schneider Electric."))

A[54] = ("Ingenuity", new(
    "Ingenuity", "ability",
    "The quality of being clever and inventive, especially in finding new ways to solve problems."))

A[55] = ("Ingredient Functionality", new(
    "Ingredient functionality", "knowledge",
    "The role an ingredient plays in a food or other formulation, such as binding, thickening, emulsifying, sweetening or preserving."))

A[56] = ("Ingres", new(
    "Ingres", "tool",
    "A relational database management system that began as a University of California, Berkeley research project and was later developed commercially by Ingres Corporation and then Actian.",
    verbs=["administer"]))

A[57] = ("Innerhtml", unsure("A single JavaScript DOM property; it is unclear whether it is a skill or which kind it would be."))

A[58] = ("Innodb", new(
    "InnoDB", "tool",
    "A storage engine for the MySQL database server that supports transactions, row-level locking and foreign keys."))

A[59] = ("Inorder", ns("A fragment, probably the phrase 'in order' or part of 'in-order traversal', not a skill by itself."))
A[60] = ("Inova Health Systems", ns("A company, not a skill."))

A[61] = ("Inpatient Obstetric Nursing", new(
    "Inpatient obstetric nursing", "skill",
    "Caring for women in hospital during pregnancy complications, labour, delivery and the days after birth."))

A[62] = ("Inside Sales Management", new(
    "Inside sales management", "skill",
    "Leading a team that sells to customers by phone, email and online rather than face to face, including coaching staff and meeting sales targets."))

A[63] = ("Instagram", new(
    "Instagram", "platform",
    "A social media platform, owned by Meta, for sharing photos and short videos."))

_iga = dict(kind="skill", definition="Creating, targeting and managing paid ads on Instagram through Meta's advertising tools.")
A[64] = ("Instagram Ads", new("Instagram advertising", _iga["kind"], _iga["definition"], variants=["Instagram ads"]))
A[65] = ("Instagram Advertising", new(
    "Instagram advertising", _iga["kind"], _iga["definition"], variants=["Instagram ads"],
    rel=[("broader", "a19c10mi46"), ("related", "lvlyhbur7j")]))

A[66] = ("Instagram Content", new(
    "Instagram content creation", "skill",
    "Planning and making posts, stories, reels and captions for an Instagram account."))

A[67] = ("Instagram Marketing", new(
    "Instagram marketing", "skill",
    "Promoting a brand or product on Instagram through content, community engagement, influencer partnerships and ads.",
    rel=[("broader", "dv5vi280tf")]))

A[68] = ("Instagram Stories", new(
    "Instagram Stories", "tool",
    "A feature of Instagram for posting photos and short videos that disappear after 24 hours."))

A[69] = ("Institute/Intercultural Global Studies", ns("A garbled organisation or department name, not a skill."))
A[70] = ("Institute Of Chartered Accountants Of Pakistan", ns("The name of a professional body, not a skill or credential."))
A[71] = ("Institutional Knowledge", ns("A general phrase for what an organisation's people know, not a skill or field."))

A[72] = ("Instructure Canvas (Educational Software)", new(
    "Canvas LMS", "platform",
    "Instructure's cloud-based learning management system that schools and universities use to deliver courses, assignments and grades.",
    variants=["Instructure Canvas"]))

A[73] = ("Instrument Rating", new(
    "Instrument rating", "credential",
    "A pilot qualification, added to a pilot licence or certificate, that allows flying by reference to cockpit instruments in cloud and poor visibility under instrument flight rules.",
    cert=True, scope="many-issuers"))

A[74] = ("Insurance Captives", new(
    "Captive insurance", "knowledge",
    "Insurance provided by a company that is owned by the business or group it insures, set up to cover that group's own risks.",
    variants=["Captive insurance company"]))

A[75] = ("Intacct", new(
    "Sage Intacct", "platform",
    "Cloud-based accounting and financial management software, originally from Intacct Corporation and now owned by Sage."))

A[76] = ("Intarsia", unsure("Names both a knitting colour technique and a wood-inlay craft, and nothing here shows which is meant."))

A[77] = ("Integrative Biology", new(
    "Integrative biology", "knowledge",
    "The study of living things that combines methods and ideas from several levels of biology, from molecules and cells to whole organisms and ecosystems."))

A[78] = ("Intel Viiv", new(
    "Intel Viiv", "platform",
    "Intel's brand, launched in 2006, for home-entertainment PCs built around specified Intel processors and chipsets."))

A[79] = ("Intellectual", ns("An adjective, not a skill."))

A[80] = ("Intellectual Properties", new(
    "Intellectual property", "knowledge",
    "The legal rights over creations of the mind, such as patents, copyrights, trademarks and trade secrets."))

A[81] = ("Intelligent Automation", new(
    "Intelligent automation", "method",
    "Combining robotic process automation with artificial intelligence, such as machine learning and language processing, to automate whole business processes."))

A[82] = ("Intended Nationally Determined Contributions", new(
    "Intended Nationally Determined Contributions", "knowledge",
    "The national climate action plans that countries submitted ahead of the 2015 Paris climate conference, which became Nationally Determined Contributions once adopted under the Paris Agreement.",
    variants=["INDC"]))

A[83] = ("Intenet Communications", unsure("Probably a misspelling of 'Internet communications', which could mean online communication (close to Digital communications) or internet technology."))

A[84] = ("Intensive Outpatient Therapy", new(
    "Intensive outpatient therapy", "method",
    "A structured mental-health or substance-use treatment programme in which patients attend therapy for several hours on several days a week while living at home.",
    variants=["Intensive outpatient program"]))

A[85] = ("Interactive Design", new(
    "Interactive design", "skill",
    "Designing digital products and media, such as websites, apps and installations, that respond to what people do, including how they navigate, choose and get feedback.",
    rel=[("related", "xrhig81x22")]))

_story = "Writing and designing stories that readers or players can shape through their choices, as in interactive fiction, branching narratives and narrative games."
A[86] = ("Interactive Stories", new("Interactive storytelling", "skill", _story))
A[87] = ("Interactive Storytelling", new("Interactive storytelling", "skill", _story))

_iwc = "Building web pages and page elements, such as forms, quizzes, calculators, animations and games, that respond to what the visitor does."
A[88] = ("Interactive Web Content", new("Interactive web content", "skill", _iwc))

A[89] = ("Interactive Web Design", new(
    "Interactive web design", "skill",
    "Designing websites whose layout and elements respond to what visitors do, such as menus, forms, animation and live updates.",
    rel=[("related", "xrhig81x22")]))

A[90] = ("Interactive Web Development", new(
    "Interactive web development", "skill",
    "Writing the code that makes web pages respond to visitors' actions, usually with JavaScript.",
    rel=[("broader", "qg4095ukub")]))

A[91] = ("Interactive Web Pages", new("Interactive web content", "skill", _iwc))

A[92] = ("Interceptor", unsure("Could be a software design pattern, a vehicle or a military system; nothing here shows which."))
A[93] = ("Interconnection", ns("A generic word with unrelated meanings in networking, power and other fields."))
A[94] = ("Intercooler", unsure("Could be the Intercooler.js web library or an engine part; nothing here shows which."))

A[95] = ("Interdisciplinary Collaboration", new(
    "Interdisciplinary collaboration", "skill",
    "Working effectively with people from other professions or fields, such as nurses and physicians or engineers and designers, toward a shared goal."))

A[96] = ("Internal Investigations", new(
    "Internal investigations", "skill",
    "Investigating suspected misconduct or rule-breaking inside an organisation, such as fraud, harassment or policy breaches, to establish the facts and recommend action.",
    rel=[("related", "jrbj7k9am7")]))

A[97] = ("International Board Certified Lactation Consultant", new(
    "International Board Certified Lactation Consultant", "credential",
    "A certification for lactation consultants, awarded by the International Board of Lactation Consultant Examiners.",
    variants=["IBCLC"], cert=True, scope="single-issuer"))

A[98] = ("International Board of Heart Rhythm Examiners (IBHRE) Certification", new(
    "IBHRE certification", "credential",
    "Certifications in heart rhythm management, such as the Certified Cardiac Device Specialist and Certified Electrophysiology Specialist, awarded by the International Board of Heart Rhythm Examiners.",
    variants=["IBHRE", "International Board of Heart Rhythm Examiners certification"], cert=True, scope="single-issuer"))

A[99] = ("International Computer Drivering License", vo("wy0q8xbf4z", "A misspelling of International Computer Driving Licence."))

write_all(A)
