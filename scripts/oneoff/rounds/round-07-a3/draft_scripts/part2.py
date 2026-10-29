import sys
sys.path.insert(0, "/home/user/rounds/round-07/a3/skills-lexicon/work/draft_scripts")
from lib import new, no, unsure, variant

new(50, "Rehabilitations", "Rehabilitation", "knowledge",
    "Treatment and training that help a person recover or regain abilities and independence lost through injury, illness, disability or addiction.")

new(51, "Reinforced Masonry Building", "Reinforced masonry", "knowledge",
    "Masonry construction in which steel bars or mesh are embedded in mortar or grout so that walls resist tension, bending and earthquake loads.")

new(52, "Relational Database Management System (RDMS)", "Relational database management system", "knowledge",
    "Software that stores data in tables of rows and columns linked by keys and is queried with SQL, such as PostgreSQL, MySQL and Oracle Database.",
    variants=["RDBMS"], relations=[("contrast", "pmy0yp0e50")])

variant(53, "Release of Information (ROI)", "s3rphwj2ud",
        "Release of information is the handling of requests to disclose patient records, the same concept as Medical records release; it is not a credential, so the legacy certification list is probably mistaken.")

no(54, "Religious Belief", "A personal characteristic, not a skill.")

new(55, "Reltio (Master Data Management Software)", "Reltio", "platform",
    "A cloud master data management platform that unifies and manages customer, product and other business data from many sources.")

unsure(56, "RemoteAccess", "Could be the general idea of remote access or a software package named RemoteAccess, and there are no quotes to decide.")

new(57, "Renal Nutrition", "Renal nutrition", "knowledge",
    "The study and practice of dietary care for people with kidney disease, including limits on protein, potassium, phosphorus, sodium and fluid.")

new(58, "Renewable Energy", "Renewable energy", "knowledge",
    "Energy from sources that are naturally replenished, such as sunlight, wind, water and geothermal heat, and the technology used to harness it.")

new(59, "Renewable Sales", "Renewable energy sales", "skill",
    "Selling renewable energy products or services, such as solar systems or clean power contracts.",
    reason="Most likely selling renewable energy products or services.")

no(60, "Rental Business", "A type of business or industry, not a skill.")

unsure(61, "Replacement Window", "Names a product, and it is unclear whether installing, selling or specifying it is meant.")

new(62, "Reportng", "Reporting", "skill",
    "Gathering information and presenting it in regular or one-off reports for others to use.",
    reason="A misspelling of reporting, which is a skill.")

new(63, "Representational State Transfer", "Representational State Transfer", "method",
    "An architectural style for web services in which resources are identified by URLs and handled with standard HTTP methods.",
    variants=["REST", "RESTful"])

new(64, "Reproductive Health Care", "Reproductive health care", "knowledge",
    "Care that supports sexual and reproductive health, such as contraception, pregnancy care, fertility care and screening.")

new(65, "Requirejs", "RequireJS", "library",
    "A JavaScript file and module loader that implements the Asynchronous Module Definition format for browsers and Node.js.")

new(66, "Research Electronic Data Capture (REDCap)", "REDCap", "tool",
    "A web application, developed at Vanderbilt University, for building and managing online surveys and research databases.",
    variants=["Research Electronic Data Capture"], relations=[("broader", "zt8mhiw2a3")])

new(67, "Research Methodology", "Research methodology", "knowledge",
    "The principles and methods for designing and carrying out research, including how data is collected and analysed.")

unsure(68, "Research Papers", "Names a document type, and it is unclear whether writing, reading or reviewing them is meant.")

unsure(69, "Research Quality Framework", "Several unrelated frameworks share this name, and there are no quotes to decide.")

no(70, "Research Sources", "A generic phrase for the places information comes from, not a skill.")

new(71, "Resharper", "ReSharper", "tool",
    "A JetBrains extension for Microsoft Visual Studio that adds code analysis, quick fixes and refactoring for .NET developers.",
    relations=[("related", "dbxqhrpv38")])

new(72, "Residential Construction", "Residential construction", "knowledge",
    "Building homes and apartment buildings, as distinct from commercial or industrial construction.")

new(73, "Resilience", "Resilience", "ability",
    "The capacity to keep functioning and recover after setbacks, stress or hardship.")

new(74, "Resilience Planning", "Resilience planning", "skill",
    "Planning how an organisation, community or system will keep working through shocks such as disasters, outages or climate events, and recover afterwards.",
    relations=[("related", "eecearu52w")])

new(75, "Resolve Guest Concerns", "Resolving guest concerns", "skill",
    "Dealing with a guest's complaints or problems, especially in hotels and restaurants, so that they are put right.")

unsure(76, "Resolver", "Several unrelated meanings (DNS resolver, GraphQL resolver, a person who settles problems), and there are no quotes to decide.")

new(77, "Resolving Guest Concerns", "Resolving guest concerns", "skill",
    "Dealing with a guest's complaints or problems, especially in hotels and restaurants, so that they are put right.")

unsure(78, "Resonance", "A physics term with several unrelated meanings (acoustic, electrical, magnetic), and it is unclear which skill is meant.")

new(79, "Resorcerer", "Resorcerer", "tool",
    "A resource editor for classic Macintosh software, used to view and edit the resources stored in application and system files.")

new(80, "Resource Mobilization", "Resource mobilization", "skill",
    "Raising and bringing together the funds, people and materials an organisation or programme needs, especially in non-profit and development work.")

new(81, "Responsibility Assignment Matrix", "Responsibility assignment matrix", "method",
    "A table that maps the tasks of a project to the people or roles responsible for them, often using codes such as responsible, accountable, consulted and informed.")

new(82, "Responsive Teaching", "Responsive teaching", "skill",
    "Adjusting instruction as a lesson happens, in response to what students say, do and need.")

new(83, "Rest Security", "REST API security", "skill",
    "Protecting RESTful web services, for example with authentication, authorisation, encryption and input validation.",
    reason="Most likely the security of REST APIs.")

new(84, "Restaurant Management", "Restaurant management", "skill",
    "Running a restaurant's daily operations, including staff, service, purchasing, food safety and finances.",
    relations=[("related", "t1845bgn6q")])

new(85, "Restorative Justice", "Restorative justice", "method",
    "An approach to wrongdoing that focuses on repairing the harm done, by bringing together victims, offenders and the community, rather than only punishing.")

no(86, "Restructuring", "A generic word with several unrelated senses (financial, organisational), naming no single skill.")

new(87, "Results-orientated", "Results-oriented", "ability",
    "A tendency to focus on achieving measurable outcomes and to judge work by what it produces.",
    relations=[("related", "g32rgj6uc5")])

new(88, "Rethinkdb", "RethinkDB", "tool",
    "An open-source distributed document database that can push changes in query results to applications as the data changes.")

new(89, "Retirement Administration", "Retirement administration", "skill",
    "Running retirement plans for employers or members, including enrolment, contributions, benefit calculations and record-keeping.")

unsure(90, "Retrospective Reviews", "Could mean agile retrospectives, retrospective chart reviews or other reviews, and there are no quotes to decide.")

new(91, "Return-to-Work Management", "Return-to-work management", "skill",
    "Helping injured or ill employees get back to work through planned, modified or gradual duties, usually alongside insurers and health providers.")

new(92, "Revise Legal Documents", "Revising legal documents", "skill",
    "Editing legal documents such as contracts and agreements to correct errors and update their terms.",
    relations=[("related", "veknequ9pu")])

new(93, "Revision Control Softwares", "Version control", "method",
    "Recording changes to files over time in a system, such as Git or Subversion, so that earlier versions can be recovered and several people can work on the same files.",
    variants=["Revision control", "Source control"])

new(94, "Revision Controls", "Version control", "method",
    "Recording changes to files over time in a system, such as Git or Subversion, so that earlier versions can be recovered and several people can work on the same files.",
    variants=["Revision control", "Source control"])

no(95, "Revolving Door", "A generic phrase for a type of door or a staffing pattern, not a skill.")

new(96, "Rhino", "Rhinoceros 3D", "tool",
    "Computer-aided design software from Robert McNeel & Associates for modelling free-form 3D curves and surfaces, widely used in architecture and product design.",
    variants=["Rhino 3D"],
    reason="Most likely the Rhino 3D modelling software, though Mozilla Rhino also exists.")

new(97, "Ribosomal Intergenic Spacer Analysis", "Ribosomal intergenic spacer analysis", "method",
    "A DNA fingerprinting technique that compares the length of the spacer between two ribosomal RNA genes to profile the bacteria in a sample.")

unsure(98, "Ridge/LASSO Regressions", "Combines two separate methods, ridge and lasso regression, so a person should decide whether to split or merge them.")

new(99, "Rigging (3D Modeling)", "Rigging (computer animation)", "skill",
    "Building the skeleton, joints and controls that let a 3D model be posed and animated.")
