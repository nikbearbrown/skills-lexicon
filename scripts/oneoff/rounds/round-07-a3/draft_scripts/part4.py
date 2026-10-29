import sys
sys.path.insert(0, "/home/user/rounds/round-07/a3/skills-lexicon/work/draft_scripts")
from lib import new, no, unsure, variant

new(150, "SAP", "SAP", "platform",
    "The enterprise software from SAP, especially its ERP systems, used to run finance, logistics, manufacturing and human resources processes.",
    reason="In skill lists this almost always means SAP's enterprise software rather than the company.")

new(151, "Sap Bo", "SAP BusinessObjects", "platform",
    "SAP's business intelligence software suite, originally from BusinessObjects, for reporting, analysis and dashboards.",
    variants=["SAP BO"])

unsure(152, "Sap Connector", "Several different SAP connectors exist (SAP .NET Connector, JCo, Cloud Connector, vendor connectors), and there are no quotes to say which.")

new(153, "SAP Crystal Reports", "SAP Crystal Reports", "tool",
    "A report-design tool, owned by SAP, for creating formatted reports from databases and other data sources.",
    variants=["Crystal Reports"])

new(154, "Sap Fiori", "SAP Fiori", "framework",
    "SAP's design system and user-interface technology that gives its software a consistent, role-based interface on browsers and mobile devices.")

new(155, "SAP GUIing", "SAP GUI", "tool",
    "SAP's desktop client program for logging in to and working with SAP systems.",
    reason="A gerund form of SAP GUI, SAP's desktop client.")

new(156, "SAP IoT", "SAP IoT", "platform",
    "SAP's cloud services for connecting devices and machines, collecting their data and using it in business processes.")

new(157, "SAP IS Retail", "SAP IS-Retail", "platform",
    "SAP's industry solution for retailers, which adds merchandise, assortment and store functions to SAP ERP.")

new(158, "Sap Lumira", "SAP Lumira", "tool",
    "A self-service tool from SAP for exploring data and building charts and dashboards.",
    variants=["SAP BusinessObjects Lumira"])

new(159, "SAP Meterial Management", "SAP Materials Management", "tool",
    "The SAP ERP module that handles procurement, inventory and invoice checking for materials.",
    variants=["SAP MM"],
    reason="A misspelling of SAP Materials Management.")

new(160, "SAP NetWeaver Process Integration", "SAP NetWeaver Process Integration", "platform",
    "SAP middleware for connecting SAP and non-SAP systems and passing messages between them.",
    variants=["SAP PI"], relations=[("related", "zhx1j34swl")])

new(161, "SAP Quality ManageMent", "SAP Quality Management", "tool",
    "The SAP ERP module for planning and recording quality inspections, quality notifications and certificates for materials and production.",
    variants=["SAP QM"])

new(162, "SAP S 4HANA", "SAP S/4HANA", "platform",
    "SAP's enterprise resource planning suite built to run on the SAP HANA in-memory database.",
    variants=["S/4HANA", "SAP S4HANA"])

new(163, "SAP Sovereign Cloud", "SAP Sovereign Cloud", "platform",
    "SAP's cloud offering designed to keep customer data and operations under the legal and operational control of a particular country or region.")

new(164, "SAP Technology Consultanting", "SAP technology consulting", "skill",
    "Advising organisations on the technical side of SAP systems, such as installation, integration, performance and cloud platforms.",
    reason="A misspelling of SAP technology consulting.")

unsure(165, "SAP Transport Management Systems", "Could mean the SAP Transport Management System for moving changes between systems or SAP Transportation Management for logistics, and there are no quotes to decide.")

unsure(166, "SAPGovernance Risk And Compliance Analytics Software", "Looks like SAP Governance, Risk and Compliance, but the analytics wording may name a narrower product.")

no(167, "Saphenous Vein", "A part of the body, not a skill.")

new(168, "Saraiki (Language)", "Saraiki", "human-language",
    "An Indo-Aryan language spoken mainly in the south of Punjab province in Pakistan.",
    variants=["Seraiki", "Siraiki"], lang="human")

new(169, "SAS/Base", "Base SAS", "programming-language",
    "The core of the SAS system, providing the SAS programming language with its DATA step, procedures and macro facility for data management and analysis.",
    lang="programming")

new(170, "SAS Macros", "SAS macro language", "programming-language",
    "The text-substitution language in SAS that generates and controls SAS code through macro variables and macros.",
    variants=["SAS macro"], lang="programming")

new(171, "SASS", "Sass", "style-language",
    "A stylesheet language that extends CSS with variables, nesting and mixins and is compiled into ordinary CSS.",
    lang="programming")

new(172, "Savon", "Savon", "library",
    "A Ruby library for calling SOAP web services.")

new(173, "Scaffold Building", "Scaffold building", "skill",
    "Erecting and taking down the temporary frameworks of tubes, boards and fittings that give workers safe access to high structures.")

new(174, "Scala.js", "Scala.js", "tool",
    "A compiler that turns Scala code into JavaScript so that Scala programs can run in browsers and on Node.js.",
    variants=["ScalaJS"], relations=[("related", "ztt7xizgr8")])

new(175, "Scalding", "Scalding", "library",
    "A Scala library, originally from Twitter, for writing Hadoop MapReduce data-processing jobs concisely.",
    relations=[("related", "ztt7xizgr8")])

new(176, "Scanvec Amiable FlexiSign", "FlexiSIGN", "tool",
    "Sign-making and large-format print design software, from Scanvec Amiable, used to design signs and drive cutters and printers.")

new(177, "Scara", "SCARA robot", "knowledge",
    "A type of industrial robot arm, short for Selective Compliance Assembly Robot Arm, that moves in a horizontal plane and is rigid vertically, used for assembly and pick-and-place work.")

new(178, "Schema Markup", "Schema markup", "standard",
    "Code added to a web page, using the schema.org vocabulary, that tells search engines what the page's content means.",
    variants=["Schema.org markup"])

new(179, "Schematic Diagrams", "Schematic diagrams", "skill",
    "Reading and drawing diagrams that show the parts of a circuit or system and how they connect, using standard symbols.")

new(180, "Scholarship Of Teaching And Learning (SoTL)", "Scholarship of teaching and learning", "knowledge",
    "The systematic study of teaching and student learning, with the findings made public so that others can build on them.",
    variants=["SoTL"])

new(181, "School Bus Endorsement", "School bus endorsement", "credential",
    "A commercial driver's licence endorsement, issued by a US state, that permits driving a school bus.",
    variants=["CDL school bus endorsement"], relations=[("related", "sli7qqx1gw")],
    cert=True, scope="many-issuers")

new(182, "School Counseling", "School counseling", "skill",
    "Helping students with their academic, personal, social and career development as a counsellor in a school.")

new(183, "Schoology", "Schoology", "platform",
    "A learning management system, now owned by PowerSchool, that schools use for assignments, grading and communication among teachers, students and parents.")

new(184, "Scientific Computating", "Scientific computing", "skill",
    "Using computational methods and software to simulate, analyse and solve problems in science and engineering.",
    reason="A misspelling of scientific computing.")

unsure(185, "Scientific Literatures", "Names a body of publications, and it is unclear whether reading, searching or writing it is the skill meant.")

new(186, "Scientific Modelling", "Scientific modelling", "method",
    "Building simplified mathematical or computational representations of natural systems to explain or predict their behaviour.")

unsure(187, "ScientificPython", "Could mean Konrad Hinsen's ScientificPython package or the general scientific Python stack, and there are no quotes to decide.")

new(188, "Scikit Learn", "scikit-learn", "library",
    "An open-source Python library of machine-learning algorithms for classification, regression, clustering and data preparation.",
    variants=["sklearn"])

new(189, "Scikit-learn (Machine Learning Library)", "scikit-learn", "library",
    "An open-source Python library of machine-learning algorithms for classification, regression, clustering and data preparation.",
    variants=["sklearn"])

new(190, "Scissor Lift Certification", "Scissor lift certification", "credential",
    "A certificate showing that a person has been trained to operate scissor lifts, aerial work platforms that raise straight up on a folding frame.",
    relations=[("broader", "umpb7it897")], cert=True, scope="many-issuers")

no(191, "Scoliosis", "A medical condition, not a skill.")

no(192, "Scooping", "A generic word for an everyday action, not a skill.")

no(193, "Scope Creep", "Names a project problem to be managed, not a skill.")

unsure(194, "SCYBER", "Not recognised: the name could be a cybersecurity credential or programme, but nothing known confirms it.")

unsure(195, "SITE Design", "Could mean civil or landscape site design, website design or a named programme, and there are no quotes to decide.")

unsure(196, "SPFPC", "An unrecognised acronym, and nothing known says what it stands for.")

new(197, "SQL-92", "SQL-92", "standard",
    "The 1992 revision of the SQL standard, which defined entry, intermediate and full levels of the database query language.",
    variants=["SQL92", "SQL2"], relations=[("broader", "f69xny35zm")])

new(198, "SQL Server Integration Services", "SQL Server Integration Services", "tool",
    "Microsoft's tool in SQL Server for building data integration and extract, transform and load workflows.",
    variants=["SSIS"], relations=[("related", "ynlpt6x7jh")])

new(199, "SQL Tuning", "SQL tuning", "skill",
    "Improving the speed and resource use of SQL queries, for example by rewriting them and adjusting indexes and statistics.",
    variants=["SQL performance tuning"])
