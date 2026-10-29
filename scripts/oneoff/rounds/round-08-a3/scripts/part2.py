from lib import *
import copy
from part1 import A as A1

A = {}
A["Vuejs"] = copy.deepcopy(A1["Vue.js"])
A["Vuejs"]["entry"]["relations"] = []   # Nuxt is not in this request's nearest list
A["Vulkan Graphics API"] = N("Vulkan", "library",
    "A low-overhead, cross-platform graphics and compute API from the Khronos Group.",
    "A named graphics API.", variants=["Vulkan API"], rels=[("broader", "dp6y03hiq5")])
A["Vulnerability Assessment"] = N("Vulnerability assessment", "skill",
    "Finding, classifying and ranking security weaknesses in systems, networks or applications so they can be fixed.",
    "A security skill.", variants=["Vulnerability assessments"], verbs=["conduct", "perform"])
A["Wagdi (Language)"] = N("Wagdi", "human-language",
    "An Indo-Aryan language spoken in the Vagad region of southern Rajasthan, India, and nearby areas.",
    "A human language.", lang="human")
A["Wage and Hour Laws"] = N("Wage and hour laws", "knowledge",
    "The laws that set minimum wages, overtime pay, working hours and related record-keeping rules for employees.",
    "A body of employment law.", variants=["Wage and hour law"], rels=[("broader", "k7zdlmxxst")])
A["Wage System"] = NS("A general economic term for how pay is structured, not a skill.")
A["Wainscot Panelling"] = N("Wainscot panelling", "skill",
    "Fitting decorative panels, usually of wood, to the lower part of interior walls.",
    "A building-trade skill.", variants=["Wainscot paneling"])
A["Wardrobing"] = U("The word means retail return fraud in one sense and costume or wardrobe work in another, and I cannot tell which is meant.")
A["Warehouse Automation"] = N("Warehouse automation", "knowledge",
    "Using machinery and software, such as conveyors, robots and automated storage systems, to move and store goods in a warehouse with less manual handling.",
    "A field of logistics technology.")
A["Warfarin"] = NS("A drug, not a skill.")
A["Warning Signs"] = NS("A generic phrase for signs or symptoms, not a defined skill.")
A["Wasapi"] = N("WASAPI", "library",
    "The Windows Audio Session API, a Microsoft Windows interface that lets applications play and record audio streams.",
    "A named Windows API.", variants=["Windows Audio Session API"])
A["Waste Characterisation"] = N("Waste characterisation", "skill",
    "Determining the physical, chemical and sometimes radiological properties of waste so that it can be classified, handled and disposed of correctly.",
    "A waste-management skill.", variants=["Waste characterization"])
A["Waste Minimisation"] = N("Waste minimisation", "method",
    "Reducing the amount of waste a process or organization produces, preferably at the source.",
    "A waste-management approach.", variants=["Waste minimization"])
A["Watchkeeping"] = N("Watchkeeping", "skill",
    "Standing a watch aboard a ship, monitoring navigation, machinery and safety while on duty.",
    "A seafaring skill.")
A["watchOS"] = N("watchOS", "platform",
    "Apple's operating system for the Apple Watch.",
    "A named operating system.", rels=[("related", "yuymi2lr97")])
A["Watcom SQL"] = N("Watcom SQL", "tool",
    "A relational database management system from Watcom that was later developed as Sybase SQL Anywhere.",
    "A named database product.")
A["Water Based Pipe Coating"] = N("Water-based pipe coating", "skill",
    "Applying water-based (waterborne) coatings to pipes as a protective layer.",
    "A coating trade skill, defined from the meaning of the words.")
A["Water Content"] = NS("A measured property of a material, not a skill.")
A["Water Coolers"] = NS("An appliance, not a skill.")
A["Water Quality Modelling"] = N("Water quality modelling", "method",
    "Using mathematical models to simulate and predict the quality of water in rivers, lakes, reservoirs or supply networks.",
    "A modelling method.", variants=["Water quality modeling"], rels=[("related", "v4z52o4053")])
A["Watercrafts"] = NS("Boats and similar vessels, an object and not a skill.")
A["Wave (Band)"] = NS("The name of a music band, not a skill.")
A["Waveguide"] = N("Waveguide", "knowledge",
    "A structure, such as a hollow metal pipe or an optical fibre, that guides electromagnetic or light waves along a path.",
    "A topic in radio-frequency and photonics engineering.", variants=["Waveguides"], rels=[("related", "awv8d1to01")])
A["Waziri (Language)"] = U("I believe Waziri is a dialect of Pashto, but I am not sure whether it counts as a language of its own.")
A["Weapon Of Mass Destruction (WMDS)"] = NS("A category of weapon, not a skill.")
A["Web Crawlers"] = N("Web crawling", "skill",
    "Building or running programs that automatically follow links and fetch web pages, for example to index sites or collect data.",
    "The skill behind web crawlers.", variants=["Web crawler"])
A["Web Help"] = U("Could mean the WebHelp documentation format, help content on a website, or web support; I cannot tell which.")
A["Web Navigation"] = U("Could mean designing site navigation or the plain ability to browse the web; I cannot tell which.")
A["Web Programming Certificates"] = N("Web programming certificate", "credential",
    "A certificate awarded for completing a course of study in web programming.",
    "A course certificate awarded by many institutions.", rels=[("related", "qg4095ukub")],
    cert=True, scope="many-issuers")
A["Web Technologies Certificates"] = N("Web technologies certificate", "credential",
    "A certificate awarded for completing a course of study in web technologies.",
    "A course certificate awarded by many institutions.", cert=True, scope="many-issuers")
A["Web Traffics"] = NS("A measure of site visits, not a skill.")
A["WebCT"] = N("WebCT", "tool",
    "A commercial learning management system for running online courses, later acquired by Blackboard.",
    "A named learning management system.")
A["WebCTRL"] = N("WebCTRL", "tool",
    "A web-based building automation system from Automated Logic for monitoring and controlling building equipment such as heating and cooling.",
    "A named building automation product.")
A["Webdriver"] = N("WebDriver", "standard",
    "A W3C standard interface for controlling a web browser from a program, which Selenium's WebDriver implements.",
    "A named browser-automation standard.")
A["Webdriverjs"] = N("WebDriverJS", "library",
    "The JavaScript bindings for Selenium WebDriver, used to automate web browsers from Node.js.",
    "A named Selenium library.", variants=["selenium-webdriver"])
A["Website Filtering"] = N("Web filtering", "method",
    "Blocking or allowing access to websites according to rules such as category, reputation or policy.",
    "A network security technique.")
A["Website Optimization"] = N("Website optimization", "skill",
    "Improving a website's speed, search visibility, usability or conversion rate.",
    "A web skill with several senses; the definition covers the common ones.",
    variants=["Website optimisation"], rels=[("related", "ikmthn4x72")])
A["Website Wireframe"] = N("Website wireframing", "skill",
    "Sketching the basic layout and structure of web pages, without final visual design, before they are built.",
    "The skill of making website wireframes.", variants=["Website wireframes"], verbs=["create"])
A["Webui"] = NS("A user-interface element or generic term, not a skill.")
A["WebVR"] = N("WebVR", "library",
    "A JavaScript API that let web pages show virtual reality content on headsets, since replaced by WebXR.",
    "A named web API.")
A["Weed Controls"] = N("Weed control", "skill",
    "Managing or removing unwanted plants in crops, lawns and other land by mechanical, chemical, cultural or biological means.",
    "An agriculture and grounds-keeping skill.")
A["Weekly Markets In Munich"] = NS("A place-based event, not a skill.")
A["Weighmaster Certification"] = U("A weighmaster credential exists in some US states, but I am not sure which body awards it or whether there is one issuer or many.")
A["Welding Symbols"] = N("Welding symbols", "knowledge",
    "The standardised symbols on engineering drawings that show the type, size, location and process of each weld.",
    "A body of drafting and welding knowledge.", verbs=["read", "interpret"])
A["Welfare"] = NS("A generic word, not a skill.")
A["Whatsapp"] = N("WhatsApp", "tool",
    "A mobile messaging and voice and video calling app owned by Meta.",
    "A named application.")
A["White Hat"] = U("It names a role or stance (ethical hacker, white-hat SEO) rather than a defined skill, and I cannot tell which is meant.")
A["Whitespace"] = U("Could be the esoteric programming language, the design concept of empty space, or the character class; I cannot tell which is meant.")
A["WhiteStar"] = U("I cannot tell what WhiteStar refers to.")
