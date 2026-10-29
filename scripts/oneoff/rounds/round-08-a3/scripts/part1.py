from lib import *

A = {}
A["ag-Grid"] = N("AG Grid", "library",
    "A JavaScript data-grid component for web applications that displays, sorts, filters and edits large tables of data.",
    "A named JavaScript grid library; the official spelling is AG Grid.")

aas = [
 ("Accounting Technology", "accounting technology"),
 ("Aerospace Technology", "aerospace technology"),
 ("Animation and CGI Motion", "animation and computer-generated (CGI) motion"),
 ("Automotive Technology", "automotive technology"),
 ("Aviation Maintenance", "aviation maintenance"),
 ("Baking and Pastry Arts", "baking and pastry arts"),
 ("Broadcasting Technology", "broadcasting technology"),
 ("Building Inspection Technology", "building inspection technology"),
 ("Chemical Technology", "chemical technology"),
 ("Civil Engineering Technology", "civil engineering technology"),
 ("Construction Technology", "construction technology"),
 ("Criminal Justice", "criminal justice"),
 ("Culinary Arts", "culinary arts"),
 ("Cybersecurity", "cybersecurity"),
 ("Dental Hygiene", "dental hygiene"),
 ("Diagnostic Medical Sonography", "diagnostic medical sonography", [("related", "tcp74hpyqr")]),
 ("Digital Media Production", "digital media production"),
 ("Electromechanical Technology", "electromechanical technology"),
 ("Emergency Medical Services", "emergency medical services"),
 ("Fashion Design", "fashion design"),
 ("Fire Science", "fire science"),
 ("Forensic Science", "forensic science"),
 ("Graphic Communications", "graphic communications"),
 ("Health Information Technology", "health information technology"),
 ("Human Resources Management", "human resources management"),
 ("Information Technology", "information technology"),
 ("Logistics and Supply Chain Management", "logistics and supply chain management"),
 ("Mechanical Engineering Technology", "mechanical engineering technology"),
 ("Medical Laboratory Technology", "medical laboratory technology"),
]
for t in aas:
    field, phrase = t[0], t[1]
    rels = t[2] if len(t) > 2 else ()
    A["Associate of Applied Science in " + field] = AAS(field, phrase, rels)

A["eClinicalWorks (ECW)"] = N("eClinicalWorks", "tool",
    "Software for electronic health records and medical practice management, made by eClinicalWorks.",
    "A named healthcare software product.")
A["eSports Management"] = N("Esports management", "skill",
    "Running the business and operations of esports teams, players, tournaments or organizations.",
    "A management skill within the esports industry.")
A["eSports Marketing"] = N("Esports marketing", "skill",
    "Promoting esports teams, events and games, or marketing other products to esports audiences, for example through sponsorship and content.",
    "A marketing skill within the esports industry.")
A["iOffice"] = N("iOFFICE", "tool",
    "Workplace management software for planning office space, desks, moves and facility services.",
    "A named workplace management software product.")
A["iOS Stack"] = U("Not a defined product or standard term; it could mean the layers of iOS or an iOS development toolset.")
A["iReport Designer"] = N("iReport Designer", "tool",
    "A graphical report designer for JasperReports, made by Jaspersoft.",
    "A named report-design tool.", variants=["Jaspersoft iReport"])
A["mdSelect"] = U("Probably the select component of AngularJS Material, but other libraries use a similar name and I cannot tell which is meant.")
A["nAnt (Software)"] = N("NAnt", "tool",
    "A free build tool for .NET projects, modelled on Apache Ant, that runs build steps described in XML files.",
    "A named .NET build tool.")
A["ngAnimate"] = N("ngAnimate", "library",
    "An AngularJS module that lets CSS transitions, CSS animations or JavaScript run when page elements enter, leave or move.",
    "A named AngularJS module.", variants=["angular-animate"])
A["ngHide"] = U("A built-in AngularJS directive, a feature of a framework rather than a product, and no allowed kind fits it cleanly.")
A["ngRepeat"] = U("A built-in AngularJS directive, a feature of a framework rather than a product, and no allowed kind fits it cleanly.")
A["Visual Odometry"] = N("Visual odometry", "method",
    "A computer-vision technique that estimates how a camera or robot has moved by analysing a sequence of images.",
    "A named computer-vision technique.")
A["Visual Storytelling"] = N("Visual storytelling", "skill",
    "Telling a story or making a point mainly through images, video, layout and design rather than text.",
    "A communication skill.", rels=[("related", "l6oh8z1sgb")])
A["Vitalize!"] = U("I cannot tell what Vitalize! refers to.")
A["Vocabularies"] = NS("A generic word, not a defined skill.")
A["Vocational Rehabilitation Counseling"] = N("Vocational rehabilitation counseling", "skill",
    "Counseling people with disabilities or injuries to help them choose, prepare for, find and keep suitable work.",
    "A recognised counseling specialty.", variants=["Vocational rehabilitation counselling"])
A["Voice Message"] = NS("A product feature, not a skill.")
A["Voice UI Design"] = N("Voice UI design", "skill",
    "Designing interfaces that people use by speaking, such as voice assistants and phone menus.",
    "A specialty of user interface design.", variants=["Voice user interface design"],
    rels=[("broader", "xrhig81x22")])
A["Voucher"] = NS("A generic word for a document or payment token, not a skill.")
A["Vue.js"] = N("Vue.js", "framework",
    "A JavaScript framework for building user interfaces and single-page web applications.",
    "A named JavaScript framework.", variants=["Vue", "VueJS"], rels=[("related", "f0mg2qvhta")])
