from dh import *

new("veeva-5a3123", "Veeva", "platform",
    "A suite of cloud software for the life-sciences industry, covering customer relationship management, content and quality management and clinical operations, made by Veeva Systems.")

new("vehicle-inspection-18b616", "Vehicle inspection", "skill",
    "Checking a vehicle's condition, such as its brakes, tires, lights and fluids, for safety and legal compliance.",
    verbs=["perform"])

new("vehicle-maintenance-f99d06", "Vehicle maintenance", "skill",
    "Servicing and repairing vehicles on a regular schedule to keep them safe and working.")

new("vendavo-software-79c622", "Vendavo", "platform",
    "Business-to-business pricing and margin management software used to set, optimise and control prices.")

new("vendor-payments-618527", "Vendor payments", "skill",
    "Processing and issuing payments to suppliers for goods and services received.")

new("ventilator-management-2e580e", "Ventilator management", "skill",
    "Setting up, monitoring and adjusting mechanical ventilators that support or replace a patient's breathing.")

new("verbal-and-physical-intervention-9ce959", "Verbal and physical intervention", "skill",
    "Using de-escalation through words and, as a last resort, safe physical holds to manage a person in crisis or at risk of harm.")

ns("veritas-softwares-676e97", "A software company name, not a skill.")
un("vertical-reflex-therapy-081431", "I do not know with confidence what this therapy is, so I will not define it.")

new("vestibular-rehabilitation-28f5da", "Vestibular rehabilitation", "skill",
    "Exercise-based therapy that helps people with inner-ear or balance disorders reduce dizziness and improve balance.",
    relations=[("broader", "dpym5atjbx")])

un("vhd-87c15f", "A bare abbreviation that could be a virtual hard disk format, a veterinary degree or a disease; cannot tell which.")
ns("vibration-theory-of-olfaction-73bc1d", "A scientific hypothesis about how smell works, not a skill.")
ns("vibrators-6530a3", "A generic or ambiguous product word, not a skill.")

new("video-ads-7e3605", "Video advertising", "skill",
    "Creating and running advertisements delivered as video, for example on YouTube, social media and connected TV.")

new("video-assisted-thoracoscopic-surgeries-abdb49", "Video-assisted thoracoscopic surgery", "skill",
    "Minimally invasive chest surgery performed through small incisions using a camera and long instruments.",
    relations=[("broader", "gyc8aazwuc")])

new("video-js-f90aa4", "Video.js", "library",
    "An open-source JavaScript library and player for playing HTML5 video in web pages.")

new("video-marketing-2c0eaa", "Video marketing", "skill",
    "Using video content to promote a product, service or brand and to engage an audience.")

new("video-remote-interpreting-vri-8034ef", "Video remote interpreting", "skill",
    "Interpreting between spoken or signed languages over a live video link instead of in person.",
    variants=["VRI"])

new("videoconferencing-6a073c", "Videoconferencing", "skill",
    "Holding meetings between people in different places by live video and audio, using software or room systems.",
    variants=["Video conferencing"],
    relations=[("related", "ms1ijh6bgm")])

new("virtual-design-and-construction-vdc-cd54d0", "Virtual design and construction", "method",
    "Using connected digital models of a building's design, schedule and cost to plan and manage a construction project before it is built.",
    relations=[("related", "t79xst2o2u")])

un("virtual-earth-3a2315", "Probably the Microsoft mapping product now called Bing Maps, but it could also be a generic phrase; cannot tell.")

new("virtual-health-5d8529", "Virtual health", "knowledge",
    "Delivering health care at a distance through video, phone, messaging and remote monitoring.")

new("virtual-lan-d166ee", "Virtual LAN", "knowledge",
    "A way of dividing one physical network into separate logical networks so that devices are grouped regardless of where they are connected, standardised as IEEE 802.1Q.",
    variants=["VLAN"])

ns("virtual-office-cf20b8", "A generic phrase for remote working or shared office services, not a defined skill.")

new("virtual-private-networks-3a7822", "Virtual private network", "knowledge",
    "A technology that creates an encrypted connection over a public network so users or sites can reach a private network securely.",
    variants=["VPN", "VPNs"])

new("virtual-production-9857c7", "Virtual production", "method",
    "Filmmaking that combines live action with real-time computer graphics, often shot in front of LED walls driven by a game engine.",
    relations=[("broader", "r4rp67mbb0")])

new("virtual-reality-8df0bd", "Virtual reality", "knowledge",
    "Computer technology that places a user inside a simulated three-dimensional environment, usually through a headset.",
    relations=[("related", "sfte4xs6zx")])

un("virtual-reality-scene-generators-b07428", "A descriptive phrase rather than a named tool or established field; cannot tell what is meant.")
un("virtual-rf-environment-195182", "I do not recognise this as an established tool or field; cannot tell what is meant.")
ns("virtual-team-b22f83", "A generic term for a team that works remotely, not a skill.")
un("virtuoso-ebab2c", "An ordinary word that is also the name of at least two software products (OpenLink Virtuoso and Cadence Virtuoso); cannot tell which.")

new("virus-culture-e63971", "Virus culture", "method",
    "Growing viruses in living host cells, such as cultured cell lines, to isolate, identify or study them.",
    relations=[("related", "rqqx99ehke")])

ns("visas-3e1950", "A generic word for immigration or travel documents, not a skill.")

new("visi-cad-cam-software-e51f60", "VISI", "tool",
    "A CAD/CAM software package for designing and machining plastic injection moulds, press tools and dies.")

new("visicalc-ef71b2", "VisiCalc", "tool",
    "An early spreadsheet program for personal computers, first released in 1979.")

new("visier-analytics-software-d038a5", "Visier", "platform",
    "A cloud people-analytics platform for analysing workforce data such as headcount, turnover and hiring.")

ns("vision-quest-bddd15", "A ritual, film title or organisation name, not a skill.")

new("vision-rehabilitation-b8efc0", "Vision rehabilitation", "skill",
    "Training and therapy that help people with vision loss use their remaining sight and other abilities to manage everyday tasks.",
    relations=[("broader", "dpym5atjbx")])

new("vissim-mathematical-modeling-ecd076", "VisSim", "tool",
    "A visual block-diagram program for modelling and simulating dynamic systems.",
    reason="The block-diagram modelling program, not the PTV traffic simulator of similar name.")

ns("visual-assets-dcc575", "A generic phrase for images and graphics, not a skill.")
ns("visual-impairment-due-to-intracranial-pr-b327dc", "A clinical sign or symptom, not a skill.")

new("visual-impairment-education-ce58ae", "Visual impairment education", "knowledge",
    "The specialist teaching of students who are blind or have low vision, adapting materials and methods to their needs.")

un("visual-modeler-0df6ae", "Could be Microsoft's older UML modelling tool or another modelling product; cannot tell which.")

new("vmware-aria-automation-e2ebca", "VMware Aria Automation", "platform",
    "A VMware platform for automating the deployment and management of cloud infrastructure and applications, formerly called vRealize Automation.",
    variants=["vRealize Automation"])

new("vmware-aria-automation-orchestrator-85f6e4", "VMware Aria Automation Orchestrator", "platform",
    "A VMware workflow automation engine that builds and runs automated workflows for IT tasks, formerly called vRealize Orchestrator.",
    variants=["vRealize Orchestrator"])

new("vmware-aria-operations-aabf9d", "VMware Aria Operations", "platform",
    "A VMware platform for monitoring the performance, capacity and health of IT infrastructure and applications, formerly called vRealize Operations.",
    variants=["vRealize Operations"])

new("vmware-aria-operations-for-logs-34ed32", "VMware Aria Operations for Logs", "platform",
    "A VMware service for collecting, searching and analysing log data from IT systems, formerly called vRealize Log Insight.",
    variants=["vRealize Log Insight"])

new("vmware-aria-suite-9ff5d6", "VMware Aria Suite", "platform",
    "A bundle of VMware cloud management products for automation, operations, logging and cost management, formerly called vRealize Suite.",
    variants=["vRealize Suite"])

new("vmware-vrealize-orchestrator-582b27", "VMware Aria Automation Orchestrator", "platform",
    "A VMware workflow automation engine that builds and runs automated workflows for IT tasks, formerly called vRealize Orchestrator.",
    variants=["vRealize Orchestrator"])

new("vpython-6c7b01", "VPython", "library",
    "A Python module for creating simple 3D visualisations and animations, widely used for teaching physics.",
    relations=[("related", "pk7cebmtg6")])

print(len(DONE), "written")
