from lib import *

A = {}
A["Wi-Fi 6"] = N("Wi-Fi 6", "standard",
    "The Wi-Fi Alliance name for the IEEE 802.11ax wireless networking standard.",
    "A named wireless standard.", variants=["802.11ax", "IEEE 802.11ax"])
A["WIA"] = U("An abbreviation with several meanings (for example Workforce Investment Act, Windows Image Acquisition) and nothing shows which one is meant.")
A["Wicklander-Zulawski Certification"] = N("Wicklander-Zulawski certification", "credential",
    "A certification awarded by Wicklander-Zulawski & Associates to people who complete its training in investigative interviewing and interrogation.",
    "A certification from one training company.", cert=True, scope="single-issuer")
A["Wide Area Networks"] = N("Wide area network", "knowledge",
    "A computer network that links sites across a large geographic area, such as cities or countries.",
    "A networking topic.", rels=[("broader", "fnhev4v1dn"), ("related", "oj9fkwcd4e")])
A["WiFi Architecture"] = N("Wi-Fi architecture", "knowledge",
    "The design of Wi-Fi wireless networks, including how access points, controllers, clients and channels are arranged to give coverage and capacity.",
    "A wireless networking topic.")
A["Wifi Direct"] = N("Wi-Fi Direct", "standard",
    "A Wi-Fi Alliance specification that lets devices connect to each other directly over Wi-Fi without a router or access point.",
    "A named wireless specification.")
A["WiFi Security"] = N("Wi-Fi security", "knowledge",
    "Protecting wireless networks and their users, for example with encryption protocols such as WPA2 and WPA3, authentication and access control.",
    "A wireless security topic.", rels=[("broader", "norpz7ekiw")])
A["WiFi Test Engineering"] = N("Wi-Fi test engineering", "skill",
    "Testing Wi-Fi devices and networks for conformance, interoperability and performance.",
    "A test-engineering specialty.")
A["WiFi Test Tools"] = NS("A generic category of tools, not one named tool or a skill.")
A["Wilderness EMT"] = N("Wilderness EMT", "credential",
    "Emergency medical technician training combined with wilderness medicine, for treating patients far from hospital care, awarded as a course certificate by various outdoor and medical training providers.",
    "A course certificate offered by many training providers.",
    variants=["WEMT", "Wilderness Emergency Medical Technician"], cert=True, scope="many-issuers")
A["Wilderness First Responder"] = N("Wilderness First Responder", "credential",
    "A wilderness medicine certification, taught by several training providers, for people who give emergency care in remote places where help is hours away.",
    "A course certification offered by many training providers.",
    variants=["WFR"], cert=True, scope="many-issuers")
A["Wilderness Medical Emergency"] = U("It names a kind of event; it could stand for wilderness medicine training or response, and I cannot tell which.")
A["Wildlife Habitat"] = NS("An environment, not a skill.")
A["Wildlife Observation"] = N("Wildlife observation", "skill",
    "Watching and recording wild animals, their behaviour and their numbers in the field.",
    "A field-biology skill.")
A["Will And Testament Preparation"] = N("Will and testament preparation", "skill",
    "Drafting a will, the legal document that states how a person's property is to be distributed after death.",
    "A legal-document skill.", variants=["Will preparation", "Will drafting"])
A["Wind Chill"] = NS("A weather measure, not a skill.")
A["Wind Turbine"] = NS("A piece of equipment, not a skill.")
A["Windows Aero"] = NS("A visual theme of Windows Vista and 7, a user-interface feature and not a skill.")
A["Windows Intune"] = N("Microsoft Intune", "tool",
    "Microsoft's cloud service for managing and securing devices and apps, first released as Windows Intune.",
    "A named Microsoft product, which this tag names by its earlier name.", variants=["Intune"])
A["Windows Meeting Space"] = N("Windows Meeting Space", "tool",
    "A Windows Vista feature for sharing programs and documents with other people over a network during a meeting.",
    "A named Windows feature.")
A["Windows Performance Analyzer"] = N("Windows Performance Analyzer", "tool",
    "A Microsoft tool for viewing and analysing event traces to find performance problems in Windows and its software.",
    "A named Microsoft tool.")
A["Windows Performance Recorder"] = N("Windows Performance Recorder", "tool",
    "A Microsoft tool for recording event traces of how Windows and its software perform, for later analysis.",
    "A named Microsoft tool.")
A["Windows Performance Toolkit"] = N("Windows Performance Toolkit", "tool",
    "A set of Microsoft tools for recording and analysing event traces to diagnose performance problems on Windows.",
    "A named Microsoft toolset.")
A["Windows Security"] = U("Could be the built-in Windows Security app or the practice of securing Windows systems; I cannot tell which is meant.")
A["Windows Server 2004"] = U("There is no classic Windows Server 2004 (only a 2020 release called version 2004), so the tag may be a typo for another version.")
A["Windows Software"] = NS("A generic phrase for any software that runs on Windows, not a skill.")
A["Windows Software Trace Preprocessor"] = N("Windows software trace preprocessor", "tool",
    "A Microsoft preprocessor, part of the Windows Driver Kit, that adds event-tracing code to software such as drivers.",
    "A named Microsoft development tool.")
A["Windows Support"] = N("Windows support", "skill",
    "Helping users with problems on computers that run Microsoft Windows.",
    "A technical-support skill.")
A["Windows System Administration"] = N("Windows systems administration", "skill",
    "Configuring and operating computers and servers that run Microsoft Windows.",
    "A system-administration skill.")
A["Windows Vista"] = N("Windows Vista", "platform",
    "The Microsoft operating system for personal computers released in 2007.",
    "A named operating system.")
A["Windows Vista Startup Process"] = N("Windows Vista startup process", "knowledge",
    "How Windows Vista boots, using the Windows Boot Manager and the boot configuration data store in place of NTLDR and boot.ini.",
    "A narrow operating-system topic.")
A["Windows XP Media Center Edition"] = N("Windows XP Media Center Edition", "platform",
    "A version of Windows XP, first released in 2002, with extra features for recording and playing TV, music, photos and video on a home computer.",
    "A named operating-system edition.")
A["Windows XP Professional X64 Edition"] = N("Windows XP Professional x64 Edition", "platform",
    "The 64-bit version of Windows XP Professional for x86-64 processors, released in 2005.",
    "A named operating-system edition.")
A["Windscreen Wiper"] = NS("A vehicle part, not a skill.")
A["Wine Education"] = N("Wine education", "knowledge",
    "Teaching and learning about wine, including grape varieties, regions, production and tasting.",
    "A field of knowledge.", rels=[("related", "s7mn3f7m94")])
A["Winemaking"] = N("Winemaking", "skill",
    "Producing wine, from handling grapes and fermenting the juice to ageing and bottling it.",
    "A production skill.", variants=["Wine making"])
A["Winjs"] = N("WinJS", "library",
    "A Microsoft JavaScript library of user-interface controls and helpers for building Windows and web apps.",
    "A named JavaScript library.", variants=["Windows Library for JavaScript"])
A["Wireless And Planning And Coordination Wing"] = NS("A government organisation, not a skill.")
A["Wireless Technologies"] = N("Wireless technologies", "knowledge",
    "Technologies that carry data or signals without cables, such as Wi-Fi, Bluetooth, cellular and radio.",
    "A broad technical field.")
A["Wkwebview"] = N("WKWebView", "library",
    "An Apple WebKit class for showing web content inside iOS and macOS apps.",
    "A named Apple API class.")
A["WLG"] = U("An abbreviation with several possible meanings (it is also an airport code) and nothing shows which one is meant.")
A["Women'S Health And Cancer Rights Act (WHCRA)"] = N("Women's Health and Cancer Rights Act", "standard",
    "A 1998 US federal law requiring group health plans that cover mastectomy to also cover breast reconstruction and related care.",
    "A named US law.", variants=["WHCRA"])
A["Women’s Studies"] = N("Women's studies", "knowledge",
    "The interdisciplinary academic study of women's lives, history and roles in society, and of gender.",
    "An academic field.")
A["Word Embedding"] = N("Word embedding", "method",
    "A natural-language-processing technique that represents words as lists of numbers so that words with similar meanings lie close together.",
    "A named machine-learning technique.", variants=["Word embeddings"])
A["Word Formation"] = N("Word formation", "knowledge",
    "The ways new words are made in a language, such as adding prefixes and suffixes, joining words and shortening them.",
    "A topic in linguistics.")
A["Word Processor"] = N("Word processing", "skill",
    "Creating, editing and formatting documents with word-processing software.",
    "The skill behind the word processor tag.")
A["Word Vba"] = N("Word VBA", "skill",
    "Writing Visual Basic for Applications code to automate tasks and extend Microsoft Word.",
    "VBA programming for Word.", lang=None)
A["Word2vec"] = N("word2vec", "method",
    "A family of shallow neural-network models, introduced at Google in 2013, that learn word embeddings from large amounts of text.",
    "A named machine-learning technique.")
A["Workers' Compensation Claims"] = N("Workers' compensation claims", "skill",
    "Handling claims for benefits that employees make after a work-related injury or illness, from filing and investigating to settling them.",
    "An insurance and HR skill.")
A["Workflow Automation"] = N("Workflow automation", "skill",
    "Using software to carry out the steps of a business process automatically, passing work between people and systems.",
    "A business-process skill.", rels=[("related", "ubxuka0jkc")])
