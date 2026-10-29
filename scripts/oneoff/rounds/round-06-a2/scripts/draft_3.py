import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draft_lib import *

new(100, "Lighttools", "LightTools", "tool",
    "Software for designing and analysing illumination optics such as lamps, light guides and displays.",
    verbs=["simulate", "design"])
unsure(101, "Limited License Bachelor Of Social Work", "Appears to be a state-specific social work licence tier, but I am not sure which state issues it or what it allows.")
no(102, "Limited User", "A type of computer account, not a skill.")
unsure(103, "LINA", "A short name with several unrelated meanings, and nothing here says which.")
no(104, "Linefeed", "A text control character, not a skill.")
no(105, "Lineman", "A job title, not a skill.")
new(106, "Lingala", "Lingala", "human-language",
    "A Bantu language spoken along the Congo River and widely used as a lingua franca in the Democratic Republic of the Congo and the Republic of the Congo.")
no(107, "Lingenfelter Performance Engineering", "A company, not a skill.")
new(108, "Linguistic Morphology", "Linguistic morphology", "knowledge",
    "The study of the internal structure of words and how they are formed from smaller meaningful parts.")
new(109, "LinkedIn", "LinkedIn", "platform",
    "A professional social networking platform used for networking, recruiting, job search and marketing.",
    verbs=["use", "post"])
new(110, "Linkedin Api", "LinkedIn API", "tool",
    "A set of web interfaces that lets applications access LinkedIn features and data, such as sign-in, sharing and marketing.",
    verbs=["integrate", "call"])
new(111, "Liquid Template", "Liquid template language", "programming-language",
    "An open-source template language, created by Shopify, that uses objects, tags and filters to build dynamic web pages.",
    verbs=["write"])
new(112, "Liquidity Forecastings", "Liquidity forecasting", "skill",
    "Estimating a business's future cash inflows, outflows and available funds to see whether it can meet its obligations.",
    relations=[("broader", "ygv0c1sw96")])
new(113, "Listwise Deletion", "Listwise deletion", "method",
    "A way of handling missing data in which any record with a missing value in the analysed variables is removed entirely.",
    variants=["Complete case analysis"])
unsure(114, "Live Steaming", "Probably the hobby of running live-steam model locomotives, but nothing here confirms it.")
new(115, "LiveData", "LiveData", "library",
    "An Android Jetpack class that holds observable data and notifies observers only while their lifecycle is active.",
    verbs=["observe"])
new(116, "Livestream", "Livestreaming", "skill",
    "Broadcasting live video and audio over the internet to an audience in real time.",
    variants=["Live streaming"], verbs=["produce", "host"])
no(117, "Living Hinge", "A physical design feature of a part, not a skill.")
new(118, "Load Securement", "Load securement", "skill",
    "Fastening and restraining cargo on a vehicle so that it cannot shift or fall during transport.",
    verbs=["secure", "inspect"])
new(119, "Loan Administration", "Loan administration", "skill",
    "Managing a loan after it is made, including recording payments, tracking terms and handling lender and borrower paperwork.")
new(120, "Loan Agreements", "Loan agreements", "knowledge",
    "Knowledge of the contracts that set out the terms on which a lender provides money to a borrower.",
    verbs=["draft", "review"])
new(121, "Loan Structuring", "Loan structuring", "skill",
    "Designing the terms of a loan, such as amount, rate, term, security and covenants, to fit the borrower and lender.")
new(122, "Loan Syndication", "Loan syndication", "skill",
    "Arranging for a large loan to be provided by a group of lenders who share the risk.")
unsure(123, "Local Class", "Probably a programming language feature rather than a skill, and the language is not given.")
unsure(124, "Local Exchange Trading Systems", "An economic arrangement rather than an obvious skill, and nothing here shows what is asked of the person.")
new(125, "Localdb", "SQL Server Express LocalDB", "platform",
    "A lightweight version of the SQL Server Express database engine for developers that starts on demand and needs no server setup.",
    variants=["LocalDB"], verbs=["query"])
unsure(126, "Locks", "A generic plural noun with many meanings, such as locksmithing, canals or database locking.")
new(127, "Log Management", "Log management", "skill",
    "Collecting, storing, searching and analysing the log files that systems and applications produce.",
    verbs=["monitor", "analyze"])
new(128, "Logic Diagrams", "Logic diagrams", "method",
    "Diagrams that show how logic gates and other elements combine to produce outputs, used to design and troubleshoot digital circuits.",
    verbs=["read", "draw"])
new(129, "Logistic Engineering", "Logistics engineering", "knowledge",
    "The engineering discipline of designing and improving how materials, equipment and information are moved and supported across a supply chain or over a system's life.",
    variants=["Logistic engineering"])
new(130, "Logistics Planning", "Logistics planning", "skill",
    "Planning how goods, equipment and people are stored and moved so they arrive where and when needed.")
new(131, "Logo Design", "Logo design", "skill",
    "Creating the symbol or wordmark that identifies a brand.")
no(132, "Long Press", "A touchscreen gesture, not a skill.")
new(133, "Long Short-Term Memory (LSTM)", "Long short-term memory", "method",
    "A type of recurrent neural network with gated memory cells that can learn dependencies across long sequences.",
    variants=["LSTM"], verbs=["train"])
unsure(134, "Long-Term Armor Strategy", "I do not know what this term refers to.")
new(135, "Lookup Table", "Lookup table", "knowledge",
    "A table of precomputed values indexed by an input, used to replace repeated calculation with a quick lookup.")
new(136, "Loss Prevention Certified", "Loss Prevention Certified", "credential",
    "A certification from the Loss Prevention Foundation for retail loss prevention professionals.",
    cert=True, scope="single-issuer")
new(137, "Low-Code Development Platform (LCDP)", "Low-code development platform", "platform",
    "A software platform for building applications mainly through visual modelling and configuration instead of hand-written code.",
    variants=["Low-code platform", "LCDP"],
    reason="A category of platforms for building applications with little hand-written code.")
new(138, "Low Risk Neonatal Nursing", "Low risk neonatal nursing", "skill",
    "Nursing care of healthy newborns and those with minor health problems, usually in a normal newborn nursery.")
new(139, "Low Voltage Transistor Transistor Logic", "Low Voltage Transistor-Transistor Logic", "standard",
    "A digital logic signalling standard that uses transistor-transistor logic levels at a lower supply voltage, typically 3.3 volts.",
    variants=["LVTTL"])
no(140, "Lower Extremity", "A part of the body, not a skill.")
no(141, "Lower Riser Package", "A piece of subsea drilling equipment, not a skill.")
unsure(142, "LRC", "A short abbreviation with several unrelated meanings, and nothing here says which.")
new(143, "Luigi", "Luigi", "library",
    "A Python library from Spotify for building and scheduling pipelines of batch jobs that depend on one another.",
    verbs=["build", "schedule"])
unsure(144, "Lule (Language)", "More than one language is called Lule and nothing here says which is meant.")
no(145, "Luminous Paint", "A material, not a skill.")
new(146, "Lumion (3D Rendering Software)", "Lumion", "tool",
    "3D rendering software that architects and designers use to turn building models into images, videos and walkthroughs.",
    verbs=["render"])
no(147, "Lymph", "A body fluid, not a skill.")
new(148, "Lymphedema Certification", "Lymphedema certification", "credential",
    "A certification showing training in assessing and treating lymphedema, awarded by various training bodies and certifying boards.",
    cert=True, scope="many-issuers",
    reason="A generic kind of certification awarded by more than one body.")
new(149, "Lymphedema Management", "Lymphedema management", "skill",
    "Assessing and treating lymphedema with techniques such as manual lymph drainage, compression and exercise.")
