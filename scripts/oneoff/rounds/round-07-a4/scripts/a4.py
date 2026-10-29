from common import *
A = {}
A["Social Media Analytics"] = new("Social media analytics", "skill",
    "Collecting and analysing data from social media accounts and conversations to measure performance and audience behaviour.")
A["Social Media Content"] = unsure("A noun for the material itself; it may mean creating, curating or managing it.")
A["Social Media Content Creation"] = new("Social media content creation", "skill",
    "Planning and making posts, images, video and captions for an organisation's or person's social media accounts.",
    relations=[R("related", "ipfsxmf9ys")])
A["Social Media Content Management"] = new("Social media content management", "skill",
    "Planning, scheduling, publishing and reviewing the content on social media accounts.",
    relations=[R("related", "ttp0mxfqt6")])
A["Social Media Management"] = new("Social media management", "skill",
    "Running social media accounts for a person or organisation, including planning and publishing posts, replying to followers and reporting on results.",
    relations=[R("related", "ttp0mxfqt6")])
A["Social Media Optimization"] = new("Social media optimization", "skill",
    "Using social media activity and content to raise the visibility of a brand or website and bring traffic to it.")
A["Social Media Profiles"] = na("A noun for accounts on social platforms, not a skill.")
A["Social Media Sharing"] = na("An everyday action of users, not a skill.")
A["Social Media Trends"] = unsure("A changing subject rather than a stable skill, though some postings ask for awareness of it.")
A["Social Network Advertising"] = new("Social media advertising", "skill",
    "Planning, buying and running paid advertisements on social media platforms.",
    variants=["Social network advertising"], relations=[R("broader", "a19c10mi46")])
A["Social Perception"] = unsure("Could be the psychology concept or the O*NET skill Social Perceptiveness; I am not sure they are the same.")
A["Social Sustainability"] = new("Social sustainability", "knowledge",
    "The part of sustainability concerned with the wellbeing, equity and rights of the people and communities affected by an organisation or project.")
A["Sociology of Education"] = new("Sociology of education", "knowledge",
    "The study of how schooling and education relate to social structures, inequality and social change.",
    relations=[R("related", "p0xczo9z6e")])
A["Socket 478"] = new("Socket 478", "tool",
    "A 478-pin CPU socket made by Intel for later Pentium 4 and Celeron processors.")
A["Socket 5"] = new("Socket 5", "tool",
    "A 320-pin CPU socket used by Intel for its Pentium processors from 75 to 133 MHz.")
A["Sockjs"] = new("SockJS", "library",
    "A JavaScript library that gives browsers a WebSocket-like object and falls back to other transports when WebSockets are unavailable.")
A["Softrax (Software)"] = new("Softrax", "platform",
    "Software for revenue recognition, billing and contract management, aimed at software and subscription companies.")
A["Software As A Services"] = variant("rm0k01pcl6", "A plural misspelling of Software as a service.")
A["Software-Defined Networking Wide Area Network (SD-WAN)"] = new("Software-defined WAN", "knowledge",
    "A way of running a wide area network in which software centrally controls how traffic is routed across links such as broadband, MPLS and cellular.",
    variants=["SD-WAN", "Software-defined wide area network"])
A["Software Interfaces"] = unsure("Could mean APIs, user interfaces or hardware-software interfaces; no context.")
A["Software Quality Assurance (SQA)"] = new("Software quality assurance", "skill",
    "Planning and carrying out the processes and checks that make sure software meets its quality requirements.")
A["Software Quality Management (Software Quality)"] = new("Software quality management", "skill",
    "Planning, controlling and improving the quality of software across its development, through standards, reviews and testing.")
A["Software Reliability Testing"] = new("Software reliability testing", "skill",
    "Testing software to measure how long and how often it runs without failure under expected use.",
    relations=[R("broader", "ss273uzint")])
A["Software Sensor"] = unsure("Possibly a soft or virtual sensor in process control, or a monitoring probe in software; no context.")
A["Software Testing Life Cycle"] = new("Software testing life cycle", "method",
    "The sequence of phases in software testing, from analysing requirements and planning through designing and running tests to closing the cycle.",
    variants=["STLC"], relations=[R("related", "ss273uzint")])
A["Sogdian (Language)"] = new("Sogdian", "human-language",
    "An extinct Eastern Iranian language that served as a trade language along the Silk Road.",
    lang="human")
A["Soil Fertility Treatment"] = new("Soil fertility treatment", "skill",
    "Improving the nutrient content and condition of soil, for example with fertilisers, lime or organic matter.")
A["Solar Panel"] = new("Solar panel", "tool",
    "A panel of photovoltaic cells that converts sunlight into electricity.")
A["Solar Power Plants In The Mojave Desert"] = na("The title of an article about particular places, not a skill.")
A["Solar Street Light"] = new("Solar street light", "tool",
    "A street lamp powered by a solar panel and battery that switches on automatically at dusk.")
A["Sonicstage"] = new("SonicStage", "tool",
    "Sony's music management software for ripping CDs, organising a library and transferring tracks to Sony portable players.")
A["Sonicwall"] = new("SonicWall", "tool",
    "A line of network security appliances and software, chiefly firewalls, from the vendor SonicWall.")
A["Sony ACID"] = new("ACID Pro", "tool",
    "A loop-based music-making software line first released by Sonic Foundry and later owned by Sony and then Magix.",
    variants=["Sony ACID Pro"])
A["Soot Blower"] = new("Soot blower", "tool",
    "A device in a boiler that cleans soot and ash off heat-transfer surfaces with jets of steam or air.",
    variants=["Sootblower"])
A["Sorce Intranets"] = unsure("I cannot tell what this names; it may be a misspelling.")
A["Source Insight"] = new("Source Insight", "tool",
    "A source code editor and browser for large programs, from SI Software, that analyses code to show symbols and call relationships.")
A["Source Server"] = unsure("Could be Microsoft's debugger source server, a game server or a generic phrase; no context.")
A["SourceGear Vault (Revision Control System)"] = new("SourceGear Vault", "tool",
    "A centralised version control system from SourceGear.")
A["Sourcing (Recruitment)"] = new("Candidate sourcing", "skill",
    "Finding and approaching potential candidates for job openings, including people who are not actively applying.",
    variants=["Talent sourcing"])
A["Sovereign Cloud (Data Security Framework)"] = new("Sovereign cloud", "knowledge",
    "Cloud computing arranged so that data, operations and control stay within the legal jurisdiction of a particular country or region.")
A["SpaCy (NLP Software)"] = new("spaCy", "library",
    "An open-source Python library for natural language processing tasks such as tokenisation, part-of-speech tagging and named-entity recognition.")
A["Spartan"] = unsure("Could be an FPGA family, a CSS framework, a sports name or a race; no context.")
A["Spatial Net"] = unsure("I cannot tell what this names.")
A["Special Education"] = new("Special education", "knowledge",
    "The teaching of students whose learning needs arise from disabilities or other exceptionalities, using adapted methods and supports.")
A["Special Education Law"] = new("Special education law", "knowledge",
    "The body of law, such as the US Individuals with Disabilities Education Act, that sets the rights and services owed to students with disabilities.",
    relations=[R("related", "a4cpgp9pfi")])
A["Special Hazards Suppression Systems"] = new("Special hazards suppression systems", "knowledge",
    "Fire suppression systems that use gas, foam or other agents to protect high-value or high-risk areas, such as data centres and flammable-liquid stores.")
A["Special Use Airspace"] = new("Special use airspace", "knowledge",
    "Airspace in which flight activity is restricted or the activities of other users are limited, such as restricted, prohibited and military operations areas.")
A["Specialist in Blood Banking (SBB-ASCP)"] = new("Specialist in Blood Banking", "credential",
    "A certification from the ASCP Board of Certification for laboratory professionals who specialise in blood banking and transfusion medicine.",
    variants=["SBB(ASCP)"], cert=True, scope="single-issuer")
A["Specialized Skill"] = na("A generic phrase, not a named certification, despite the legacy certification list.")
A["Specimen Processing"] = new("Specimen processing", "skill",
    "Receiving, labelling and preparing clinical specimens so they are ready for laboratory testing.")

if __name__ == "__main__":
    write(slice_terms(150, 200), A)
