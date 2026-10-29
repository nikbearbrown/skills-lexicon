import sys
sys.path.insert(0, "work/scripts")
from lib import *

A = {}

A["nsxml-11e40d"] = unsure(
    "Possibly the Cocoa NSXML classes, but the bare term is too unclear to define.")

A["nuance-pdf-converter-7cf695"] = new(
    "Nuance PDF Converter is a named software product.",
    "Nuance PDF Converter", "tool",
    "Nuance software for creating, converting and editing PDF files.")

A["nuclear-weapon-eb8ed3"] = nas(
    "A type of object, not a skill.")

A["nucleo-9dd733"] = new(
    "In skill lists Nucleo most likely names the STMicroelectronics STM32 Nucleo boards.",
    "STM32 Nucleo", "tool",
    "A family of low-cost microcontroller development boards from STMicroelectronics built around STM32 chips.",
    variants=["Nucleo"])

A["numbers-spreadsheet-e0a205"] = new(
    "Numbers is Apple's spreadsheet app; the name is disambiguated because numbers is an everyday word.",
    "Apple Numbers", "tool",
    "Apple's spreadsheet application for macOS, iOS and iPadOS.")

A["numpy-148fb3"] = new(
    "NumPy is a named Python library.",
    "NumPy", "library",
    "A Python library for fast numerical computing built around N-dimensional arrays.")

A["nuodb-267ad2"] = new(
    "NuoDB is a named database product.",
    "NuoDB", "platform",
    "A distributed SQL relational database designed to run in the cloud.")

A["nurse-licensure-a6ef59"] = new(
    "Nurse licences are issued by many state and national boards under a common standard.",
    "Nurse licensure", "credential",
    "A licence, issued by a state or national nursing board, that legally permits a person to practise as a nurse.",
    cert=True, scope="many-issuers")

A["nurse-midwife-b887a3"] = new(
    "Treated as the nurse-midwife credential, like the nurse practitioner credentials already in the dictionary.",
    "Certified Nurse-Midwife", "credential",
    "A credential for advanced practice nurses trained in midwifery, awarded by the American Midwifery Certification Board.",
    variants=["Nurse Midwife", "CNM"], cert=True, scope="single-issuer")

A["nurse-practitioner-670237"] = new(
    "Nurse practitioner is an advanced practice credential, like the specialty versions already in the dictionary.",
    "Nurse Practitioner", "credential",
    "An advanced practice nursing credential for registered nurses with graduate education who are licensed by a state and certified in a population focus.",
    cert=True, scope="many-issuers")

A["nutanix-ahv-fdb1cf"] = new(
    "Nutanix AHV is a named hypervisor.",
    "Nutanix AHV", "tool",
    "Nutanix's built-in hypervisor, based on KVM, that runs virtual machines on Nutanix clusters.")

A["nutanix-calm-7a4be4"] = new(
    "Nutanix Calm is a named Nutanix product.",
    "Nutanix Calm", "tool",
    "Nutanix's application automation and orchestration tool for provisioning and managing applications across clouds.")

A["nutanix-f6644b"] = new(
    "In skill lists Nutanix names the Nutanix infrastructure platform.",
    "Nutanix", "platform",
    "A hyperconverged infrastructure platform that combines compute, storage and virtualisation on clustered servers.")

A["nutanix-prism-aeaabe"] = new(
    "Nutanix Prism is a named Nutanix product.",
    "Nutanix Prism", "tool",
    "Nutanix's web-based console for monitoring and managing Nutanix clusters.")

A["nutraceuticals-eb0f61"] = new(
    "Nutraceuticals are a defined product area with its own knowledge.",
    "Nutraceuticals", "knowledge",
    "Food-derived products, such as supplements and fortified foods, that are sold for health benefits beyond basic nutrition.")

A["nutrition-care-plans-420192"] = new(
    "Writing nutrition care plans is a recognised dietetic skill.",
    "Nutrition care planning", "skill",
    "Writing individual plans that set a patient's nutrition goals, interventions and follow-up.",
    variants=["Nutrition care plans"])

A["nutrition-consulting-c0e9e2"] = new(
    "Advising people on diet is a recognised skill.",
    "Nutrition consulting", "skill",
    "Advising individuals or organisations on diet and eating habits to meet health or performance goals.")

A["nutrition-diagnosis-9ca68b"] = new(
    "Nutrition diagnosis is a named step of the Nutrition Care Process.",
    "Nutrition diagnosis", "skill",
    "The step of the Nutrition Care Process in which a dietitian identifies and names a nutrition problem that they are responsible for treating.")

A["nutrition-intervention-3dc758"] = new(
    "Nutrition intervention is a named step of the Nutrition Care Process.",
    "Nutrition intervention", "skill",
    "The step of the Nutrition Care Process in which planned actions are taken to address an identified nutrition problem.")

A["nutritional-assessment-5f562b"] = new(
    "Nutritional assessment is a recognised clinical skill.",
    "Nutritional assessment", "skill",
    "Evaluating a person's nutritional status from diet history, body measurements, clinical signs and laboratory results.")

A["nutritional-screening-3b2e80"] = new(
    "Nutritional screening is a recognised clinical skill.",
    "Nutritional screening", "skill",
    "Quickly identifying people who are malnourished or at nutritional risk, using a short validated screening tool.")

A["nuxt-js-5b094c"] = new(
    "Nuxt is a named web framework.",
    "Nuxt", "framework",
    "A framework built on Vue.js for building server-rendered and static web applications.",
    variants=["Nuxt.js"])

A["nw-js-9ee71c"] = new(
    "NW.js is a named desktop app framework.",
    "NW.js", "framework",
    "A framework for building desktop applications with HTML, CSS and JavaScript on top of Node.js and Chromium.",
    variants=["node-webkit"])

A["obd-ii-b8b8d0"] = new(
    "OBD-II is a named vehicle diagnostics standard.",
    "OBD-II", "standard",
    "A standard for on-board vehicle diagnostics that gives access to a car's engine and emissions data through a standard connector and fault codes.",
    variants=["OBD2", "On-Board Diagnostics II"])

A["obiee-answers-e53764"] = new(
    "OBIEE Answers is the ad hoc query part of Oracle's BI suite.",
    "Oracle BI Answers", "tool",
    "The ad hoc query and analysis component of Oracle Business Intelligence Enterprise Edition, used to build reports from a business model.")

A["object-oriented-data-model-for-database--50c3ad"] = new(
    "The object-oriented data model is a named data modelling approach.",
    "Object-oriented data model", "knowledge",
    "A way of modelling data in which information is represented as objects that have attributes and behaviour and can be related to one another.")

A["object-oriented-programming-9585e3"] = new(
    "Object-oriented programming is a standard programming paradigm, distinct from object-oriented design.",
    "Object-oriented programming", "method",
    "A programming paradigm that organises code into objects that combine data and the behaviour that works on it.",
    variants=["OOP"], relations=[R("related", "y098fizl5l")])

A["obsolescence-bfbd4e"] = nas(
    "A generic word; the skill would be obsolescence management.")

A["occupational-health-and-safety-administr-697960"] = nas(
    "Names a government agency (OSHA), not a skill.")

A["occupational-health-and-safety-technolog-f4990c"] = new(
    "OHST is a safety credential awarded by the Board of Certified Safety Professionals.",
    "Occupational Health and Safety Technologist", "credential",
    "A safety credential for technicians who support occupational health and safety work, awarded by the Board of Certified Safety Professionals (BCSP).",
    variants=["OHST"], cert=True, scope="single-issuer")

A["occupational-injury-226169"] = nas(
    "An event or condition, not a skill.")

A["oclc-connexion-aa4fff"] = new(
    "OCLC Connexion is a named library cataloguing product.",
    "OCLC Connexion", "tool",
    "OCLC's cataloguing service and client software for creating and editing library catalogue records.")

A["ocular-pathology-f1e9f7"] = new(
    "Ocular pathology is a recognised medical specialty area.",
    "Ocular pathology", "knowledge",
    "The branch of pathology that studies diseases of the eye and the tissues around it.")

A["ocunit-a149d5"] = new(
    "OCUnit is a named Objective-C unit testing framework.",
    "OCUnit", "framework",
    "A unit testing framework for Objective-C that was bundled with Apple's Xcode before XCTest replaced it.")

A["odas-98e83e"] = unsure(
    "ODAS could stand for several things and nothing here says which.")

A["odor-controls-3c7963"] = new(
    "Odor control is a recognised engineering topic.",
    "Odor control", "knowledge",
    "Methods and equipment, such as scrubbers and biofilters, for removing or neutralising unpleasant odours in plants such as wastewater and industrial facilities.",
    variants=["Odor controls", "Odour control"])

A["office-and-productivity-software-8416b1"] = new(
    "A category of software, treated like other software categories in the dictionary.",
    "Office and productivity software", "tool",
    "Software for everyday office work, such as word processing, spreadsheets, presentations and email.")

A["office-assistant-d50570"] = nas(
    "A job title, not a skill.")

A["office-complex-a911bc"] = nas(
    "A type of place, not a skill.")

A["office365-ec67bb"] = new(
    "Office 365 is the former name of Microsoft 365.",
    "Microsoft 365", "platform",
    "Microsoft's subscription suite of productivity apps and cloud services, including Word, Excel, Outlook and Teams.",
    variants=["Office 365"])

A["official-statistics-04c154"] = new(
    "Official statistics is a recognised field in statistics.",
    "Official statistics", "knowledge",
    "Statistics produced and published by government statistical agencies about a country's population, economy and society.",
    relations=[R("related", "ecoz6ylymx")])

A["offshore-installation-manager-oim-c2f4f2"] = nas(
    "A job title, not a skill.")

A["offshore-water-survival-c3edcd"] = unsure(
    "May mean offshore sea-survival training or a certificate for it, and I cannot tell which.")

A["ohm-s-law-a36203"] = new(
    "Ohm's law is a basic physics and electronics law.",
    "Ohm's law", "knowledge",
    "The law that the current through a conductor is proportional to the voltage across it, written V = I × R.")

A["oil-pipelines-086363"] = new(
    "Oil pipelines are an engineering and operations domain.",
    "Oil pipelines", "knowledge",
    "The pipeline systems that carry crude oil and refined products, and the engineering, operation and regulation of them.")

A["oil-refinery-13df62"] = unsure(
    "Names a type of facility; it may mean refinery operations knowledge, and a person should decide.")

A["oils-chemical-7f51e5"] = nas(
    "A class of substances, not a skill.")

A["ojose-scienfic-engine-3c613a"] = unsure(
    "I do not recognise OJOSE and the label gives no further clue.")

A["olit-7af61a"] = unsure(
    "I cannot tell with confidence what Olit refers to.")

A["omniorb-003e79"] = new(
    "omniORB is a named CORBA implementation.",
    "omniORB", "library",
    "An open-source CORBA object request broker for C++ and Python.")

if __name__ == "__main__":
    write(A)
