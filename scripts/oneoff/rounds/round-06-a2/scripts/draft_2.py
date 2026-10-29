import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draft_lib import *

no(50, "LanguageLine Solutions", "A company, not a skill.")
no(51, "Laryngopharyngeal Reflux", "A medical condition, not a skill.")
new(52, "Laser Engineering", "Laser engineering", "knowledge",
    "The engineering of lasers and laser-based systems, including their design, building and application.")
unsure(53, "Laser", "Could mean laser equipment, laser physics or laser cutting and nothing here says which.")
new(54, "Laser Levels", "Laser level", "tool",
    "A tool that projects a level or plumb line of laser light so that surfaces and fixtures can be aligned on a building site.",
    verbs=["use", "calibrate"])
new(55, "Laser Printing", "Laser printing", "knowledge",
    "Printing in which a laser draws an image onto a charged drum that picks up toner and transfers it to paper.",
    relations=[("related", "zotkhvqj89")])
new(56, "Latin American And Latino Studies", "Latin American and Latino studies", "knowledge",
    "The interdisciplinary academic study of the history, cultures, politics and societies of Latin America and of Latino communities, especially in the United States.")
new(57, "Law Enforcement Practices", "Law enforcement practices", "knowledge",
    "The methods, procedures and rules that police and other law enforcement officers follow in their work.",
    relations=[("related", "i3hhtsx5w7")])
new(58, "Lawa (Language)", "Lawa", "human-language",
    "An Austroasiatic language of the Palaungic branch spoken by the Lawa people of northern Thailand.")
new(59, "Lawful Interception", "Lawful interception", "knowledge",
    "The legally authorised interception of telephone and data communications by network operators for law enforcement and security agencies.",
    variants=["Lawful intercept"])
unsure(60, "Layering", "Means different things in hair cutting, painting, textiles and finance and nothing here says which.")
unsure(61, "Lcs", "An abbreviation with many possible meanings, such as longest common subsequence, and nothing here says which.")
new(62, "LDRA Testbed", "LDRA Testbed", "tool",
    "A software verification tool from LDRA that performs static and dynamic analysis and measures test coverage, mainly for safety-critical code.",
    verbs=["analyze", "test"])
new(63, "Leadership Certificates", "Leadership certificate", "credential",
    "A certificate awarded by a university, professional body or training provider for completing a course in leadership.",
    cert=True, scope="many-issuers",
    reason="A generic kind of certificate that many different bodies award.")
new(64, "Lean Principles", "Lean principles", "method",
    "A set of principles, drawn from the Toyota Production System, for delivering value to customers while removing waste.",
    variants=["Lean thinking"])
new(65, "Learner Analysis", "Learner analysis", "skill",
    "Studying the characteristics, prior knowledge and needs of the people who will take a course so that instruction can be fitted to them.")
new(66, "Learner Experience Design (LXD)", "Learner experience design", "skill",
    "Designing learning experiences around the needs, motivations and context of learners, combining instructional design with user experience design.")
new(67, "Learning Agility", "Learning agility", "skill",
    "The capacity to learn quickly from experience and apply it in unfamiliar situations.")
no(68, "Learning Curve", "A general concept or figure of speech about how fast learning happens, not a skill.")
new(69, "LEED Accredited Professional (AP)", "LEED Accredited Professional", "credential",
    "A professional credential from the Green Building Certification Institute showing advanced knowledge of the LEED green building rating system.",
    variants=["LEED AP"], cert=True, scope="single-issuer")
new(70, "LEED Green Associate", "LEED Green Associate", "credential",
    "An entry-level professional credential from the Green Building Certification Institute showing basic knowledge of green building and the LEED rating system.",
    cert=True, scope="single-issuer")
no(71, "Left Ventricular Myocardial Hypertrophy", "A medical condition, not a skill.")
new(72, "Legal Nurse Consultant Certified", "Legal Nurse Consultant Certified", "credential",
    "A certification for registered nurses who pass an exam in legal nurse consulting, awarded by the American Legal Nurse Consultant Certification Board.",
    variants=["LNCC"], cert=True, scope="single-issuer")
no(73, "Legal Support", "A generic function label that names no specific skill.")
new(74, "Lego Digital Designer", "LEGO Digital Designer", "tool",
    "Free LEGO software for designing virtual models with digital bricks on a computer.",
    verbs=["design", "build"])
no(75, "Leisure And Recreation", "An industry or sector, not a skill.")
new(76, "Leisure Education", "Leisure education", "knowledge",
    "Teaching people the attitudes, knowledge and skills they need to choose and enjoy leisure activities.")
new(77, "LESS", "LESS", "style-language",
    "A CSS preprocessor language that adds variables, nesting, mixins and functions to style sheets and compiles to plain CSS.",
    variants=["Leaner Style Sheets"], verbs=["write", "compile"])
new(78, "Less.js", "Less.js", "library",
    "The JavaScript implementation of the Less compiler, which turns Less style sheets into CSS in the browser or in Node.js.",
    verbs=["compile"])
new(79, "LetterForms", "Letterforms", "knowledge",
    "The shapes of written or typeset letters, and the study and drawing of those shapes in lettering and type design.")
no(80, "Levee", "A physical structure, not a skill.")
no(81, "Level 3 Communications", "A company, not a skill.")
new(82, "Levelator", "Levelator", "tool",
    "A free desktop program that automatically evens out loudness differences in spoken-word audio recordings.",
    verbs=["use"])
no(83, "Leverage", "A generic word with many meanings, not a specific skill.")
unsure(84, "Lexmark Service Manager", "Appears to be a Lexmark software product, but I do not know what it does.")
unsure(85, "Liberator", "A common product and brand name with many unrelated uses, and nothing here says which.")
new(86, "Librarianship", "Librarianship", "knowledge",
    "The profession and discipline of organising, managing and providing access to library collections and information services.")
unsure(87, "Library Services (Library Law)", "Unclear whether this means running library services or the law that governs libraries.")
new(88, "LIBSVM", "LIBSVM", "library",
    "An open-source library for training support vector machines for classification and regression.",
    verbs=["train"])
new(89, "Licensed Insurance Producer", "Licensed insurance producer", "credential",
    "A licence, issued by a US state, that allows a person to sell insurance products in that state.",
    cert=True, scope="many-issuers")
new(90, "Licensed Practical Nurse", "Licensed Practical Nurse", "credential",
    "A US state licence for nurses who provide basic nursing care under the direction of registered nurses and physicians.",
    variants=["LPN"], cert=True, scope="many-issuers")
new(91, "Licensed Professional Engineer", "Licensed Professional Engineer", "credential",
    "A US state licence that allows an engineer to approve and take legal responsibility for engineering work.",
    cert=True, scope="many-issuers")
new(92, "Licensed Vocational Nurses", "Licensed Practical Nurse", "credential",
    "A US state licence for nurses who provide basic nursing care under the direction of registered nurses and physicians, titled Licensed Vocational Nurse in California and Texas.",
    variants=["Licensed Vocational Nurse", "LVN"], cert=True, scope="many-issuers",
    reason="LVN is the title used instead of LPN in California and Texas for the same licence level.")
new(93, "Lidar", "LiDAR", "method",
    "A remote sensing method that measures distances by timing reflected laser pulses, used to build detailed maps and 3D models.",
    variants=["Light detection and ranging"], verbs=["process", "analyze"])
new(94, "Life Skills", "Life skills", "skill",
    "Practical personal abilities, such as budgeting, cooking, time management and communication, needed to manage everyday life.")
no(95, "Life Technologies", "A company, not a skill.")
new(96, "Lightcast (Software)", "Lightcast", "platform",
    "A labor market analytics platform that provides job posting, skills and workforce data.")
new(97, "LightGBM", "LightGBM", "library",
    "A gradient boosting library for training fast decision-tree models on large datasets.",
    variants=["Light Gradient Boosting Machine"], verbs=["train", "tune"])
new(98, "Lighting Design", "Lighting design", "skill",
    "Planning the type, placement and control of light for buildings, stages, films or other spaces.")
unsure(99, "Lightspeed", "Names several unrelated products and companies, and nothing here says which.")
