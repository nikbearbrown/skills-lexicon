import sys
sys.path.insert(0, "/home/user/rounds/round-07/a3/skills-lexicon/work/draft_scripts")
from lib import new, no, unsure, variant

new(0, "Raytracing", "Ray tracing", "method",
    "A rendering technique that makes images by following the paths of light rays through a scene and calculating how they bounce off and pass through surfaces.")

new(1, "Reactivex", "ReactiveX", "library",
    "A family of libraries, such as RxJava and RxJS, for writing asynchronous and event-driven programs by composing streams of events called observables.",
    variants=["Reactive Extensions"])

new(2, "Read To Children", "Reading to children", "skill",
    "Reading books and stories aloud to children, for example to build their listening, language and interest in reading.")

no(3, "Readonly", "A keyword or access setting in programming languages and systems, not a skill.")

new(4, "ReadyAPI", "ReadyAPI", "tool",
    "A SmartBear suite of tools for testing and monitoring APIs, covering functional, security and load testing.")

new(5, "Real Estate Broker License", "Real estate broker license", "credential",
    "A licence, issued by a US state or similar authority, that lets a person act as a real estate broker and handle property sales or lettings for others.",
    cert=True, scope="many-issuers")

new(6, "Real Estate Contracts", "Real estate contracts", "knowledge",
    "The agreements, such as purchase, sale and lease contracts, used to transfer or let property, and the rules on how they are written and enforced.")

new(7, "Real Estate Market Analysis", "Real estate market analysis", "skill",
    "Studying prices, supply, demand and trends in a property market to judge the value of properties and the prospects of an area.")

new(8, "Real Estate Owned (REO)", "Real estate owned", "knowledge",
    "Property that a lender owns after it fails to sell at a foreclosure auction, and the work of managing and reselling it.",
    variants=["REO"])

new(9, "Real Estate Salesperson License", "Real estate salesperson license", "credential",
    "A licence, issued by a US state or similar authority, that lets a person sell and lease property for a licensed real estate broker.",
    cert=True, scope="many-issuers")

new(10, "Real Estates", "Real estate", "knowledge",
    "Land and the buildings on it, and the field of buying, selling, leasing, valuing and managing them.")

new(11, "Real Property Administrator", "Real Property Administrator", "credential",
    "A professional designation from BOMI International for people who manage commercial property, earned by completing its coursework and exams.",
    cert=True, scope="single-issuer")

new(12, "Real Time Payments", "Real-time payments", "knowledge",
    "Payment systems that clear and settle transfers between bank accounts within seconds, at any hour, such as the RTP network and FedNow.")

new(13, "Receptive And Expressive Language", "Receptive and expressive language", "knowledge",
    "The two sides of language ability studied in speech-language pathology: understanding what others say or write, and putting thoughts into words.",
    lang=None,
    note="It names two aspects of language ability, not a language itself.",
    reason="A clinical topic about language ability, so a knowledge entry, not a language.")

no(14, "Reciprocity", "A generic word with several unrelated senses, naming no specific skill.")

new(15, "Recruiment Consultancy", "Recruitment consulting", "skill",
    "Advising employers on hiring and finding, screening and placing candidates for them.",
    reason="A misspelling of recruitment consultancy, which is a skill.")

new(16, "Red Hat Certification Programs", "Red Hat certification", "credential",
    "The exams and certifications that Red Hat awards for skills in Linux, automation, containers and its other software, such as RHCSA, RHCE and RHCA.",
    cert=True, scope="single-issuer")

new(17, "Red Hat Certified Engineer", "Red Hat Certified Engineer", "credential",
    "A Red Hat certification, above Red Hat Certified System Administrator, for engineers who automate and manage Red Hat Enterprise Linux systems.",
    variants=["RHCE"], cert=True, scope="single-issuer")

new(18, "Red Teaming", "Red teaming", "method",
    "Playing the part of an adversary to test how well an organisation, system or AI model withstands attack or misuse.")

new(19, "Reduction (Complexity)", "Reduction (complexity)", "method",
    "A way of converting one problem into another so that a solution to the second gives a solution to the first, used in complexity theory to compare how hard problems are.")

new(20, "Reference Range", "Reference range", "knowledge",
    "The range of values for a laboratory test that is expected in healthy people, used to judge whether a result is normal.")

unsure(21, "Reference Work", "Could mean library reference services or consulting reference books, and there are no quotes to decide.")

no(22, "Refinement", "A generic word with many senses (backlog refinement, design refinement) and no single skill.")

no(23, "Refinery", "An industrial facility or industry, not a skill.")

unsure(24, "Reflux", "Could be the chemistry technique of boiling under a condenser or the medical symptom, and there are no quotes to decide.")

new(25, "Refrigerated Transport", "Refrigerated transport", "skill",
    "Moving perishable or temperature-sensitive goods in vehicles or containers that keep them cold.")

new(26, "Refrigeration", "Refrigeration", "knowledge",
    "The technology and practice of removing heat to keep a space or product colder than its surroundings, as in cold rooms, freezers and chillers.")

new(27, "Refrigeration Compressors|", "Refrigeration compressors", "knowledge",
    "The machines that compress refrigerant gas in a refrigeration system so that it can circulate and carry heat away.")

new(28, "Refugee Issues", "Refugee issues", "knowledge",
    "Understanding the legal, social and humanitarian circumstances of people forced to flee their countries, and the services that support them.")

new(29, "Registered Art Therapist", "Registered Art Therapist", "credential",
    "A credential from the Art Therapy Credentials Board for art therapists who have met its education and supervised-practice requirements.",
    relations=[("related", "syt4e7l62v")], cert=True, scope="single-issuer")

new(30, "Registered Cardiac Electrophysiology Specialist", "Registered Cardiac Electrophysiology Specialist", "credential",
    "A credential from Cardiovascular Credentialing International for specialists who assist with electrophysiology studies and heart rhythm procedures.",
    variants=["RCES"], cert=True, scope="single-issuer")

new(31, "Registered Cardiac Sonographer", "Registered Cardiac Sonographer", "credential",
    "A credential from Cardiovascular Credentialing International for sonographers who perform ultrasound examinations of the heart.",
    cert=True, scope="single-issuer")

new(32, "Registered Cardiovascular Invasive Specialist", "Registered Cardiovascular Invasive Specialist", "credential",
    "A credential from Cardiovascular Credentialing International for specialists who assist with invasive procedures in a cardiac catheterisation laboratory.",
    variants=["RCIS"], cert=True, scope="single-issuer")

new(33, "Registered Clinical Exercise Physiologist", "Registered Clinical Exercise Physiologist", "credential",
    "A credential for exercise physiologists who plan and supervise exercise programmes for people with chronic disease or disability.",
    variants=["RCEP"], cert=True, scope="single-issuer")

new(34, "Registered Communications Distribution Designer", "Registered Communications Distribution Designer", "credential",
    "A BICSI credential for designers of telecommunications and data cabling distribution systems in buildings.",
    variants=["RCDD"], cert=True, scope="single-issuer")

new(35, "Registered Diagnostic Cardiac Sonographer", "Registered Diagnostic Cardiac Sonographer", "credential",
    "A credential from the American Registry for Diagnostic Medical Sonography for sonographers who perform ultrasound examinations of the heart.",
    variants=["RDCS"], cert=True, scope="single-issuer")

new(36, "Registered Diagnostic Medical Sonographer", "Registered Diagnostic Medical Sonographer", "credential",
    "A credential from the American Registry for Diagnostic Medical Sonography for sonographers who perform diagnostic ultrasound examinations.",
    variants=["RDMS"], cert=True, scope="single-issuer")

new(37, "Registered Dietitian", "Registered Dietitian", "credential",
    "A credential awarded by the Commission on Dietetic Registration to dietitians in the United States who have completed an accredited degree, supervised practice and an exam.",
    variants=["Registered Dietitian Nutritionist", "RDN"], cert=True, scope="single-issuer")

new(38, "Registered Education Savings Planning", "Registered Education Savings Plan", "knowledge",
    "A Canadian government-registered savings account, with grants, for a child's education after high school, and the planning of contributions to it.",
    variants=["RESP"])

new(39, "Registered Health Information Administrator", "Registered Health Information Administrator", "credential",
    "A credential from AHIMA for health information managers who oversee patient records, health data and privacy.",
    variants=["RHIA"], cert=True, scope="single-issuer")

new(40, "Registered Health Information Technician", "Registered Health Information Technician", "credential",
    "A credential from AHIMA for technicians who code, maintain and check the quality of patient health records.",
    variants=["RHIT"], cert=True, scope="single-issuer")

new(41, "Registered Phlebology Sonographer", "Registered Phlebology Sonographer", "credential",
    "A credential from the American Registry for Diagnostic Medical Sonography for sonographers who perform ultrasound examinations of the veins.",
    variants=["RPhS"], cert=True, scope="single-issuer")

new(42, "Registered Poetry Therapist", "Registered Poetry Therapist", "credential",
    "A credential for practitioners trained in using poetry and other literature as a form of therapy.",
    cert=True, scope="single-issuer")

new(43, "Registered Respiratory Therapist", "Registered Respiratory Therapist", "credential",
    "A credential from the National Board for Respiratory Care for respiratory therapists who pass its advanced-level exams.",
    cert=True, scope="single-issuer")

no(44, "Registered User", "A generic term for someone with an account on a system, not a skill.")

new(45, "Registered Vascular Specialist", "Registered Vascular Specialist", "credential",
    "A credential from Cardiovascular Credentialing International for specialists who perform vascular ultrasound and other vascular testing.",
    variants=["RVS"], cert=True, scope="single-issuer")

new(46, "Registered Vascular Technologist", "Registered Vascular Technologist", "credential",
    "A credential from the American Registry for Diagnostic Medical Sonography for technologists who perform vascular ultrasound examinations.",
    variants=["RVT"], cert=True, scope="single-issuer")

new(47, "Regulatory CMC", "Regulatory CMC", "skill",
    "Preparing and managing the chemistry, manufacturing and controls information that regulators require in applications for drugs and biological products.",
    variants=["Regulatory chemistry, manufacturing and controls"])

no(48, "Regulatory Frameworks", "A generic phrase for any set of rules, naming no specific framework or field.")

unsure(49, "Rehabilitation And Healthy Aging", "Two combined topics, and it is unclear which skill is meant.")
