from lib_answers import *

A = {}
A["printed-circuit-boards-design-3451cf"] = new("Printed circuit board design", "skill",
    "Laying out the components and copper connections of a printed circuit board from an electronic schematic.",
    variants=["PCB design"])
A["prisoner-s-rights-4dac43"] = new("Prisoners' rights", "knowledge",
    "The legal rights of people held in prisons and jails, such as protection from cruel treatment and access to the courts.")
A["privacy-impact-assessments-5c3edf"] = new("Privacy impact assessment", "method",
    "A structured process for finding and reducing the privacy risks of a project, system or policy that handles personal information.")
A["private-banking-af37fc"] = new("Private banking", "knowledge",
    "Banking, lending and investment services tailored to wealthy individuals and families.")
A["private-company-limited-by-shares-ff80f8"] = nas("A legal form of company, not a skill.")
A["privileged-access-management-e0eb76"] = new("Privileged access management", "skill",
    "Controlling, securing and monitoring accounts with elevated permissions, such as administrator and root accounts.")
A["pro-active-774b97"] = nas("A general adjective for a way of behaving, not a defined skill.")
A["problem-reports-bfc794"] = nas("A kind of document with no fixed meaning across fields, not a skill.")
A["problem-solving-531c2f"] = new("Problem solving", "skill",
    "Working out what is causing a problem and finding and carrying out a way to resolve it.",
    variants=["Problem-solving"], rels=[("related", "u9lvovjv7p")])
A["process-analysis-business-16ad21"] = variant("b2n6djrqyw",
    "Process analysis in a business setting is analysing business processes, the same concept as Business process analysis.")
A["process-analysis-computing-7fc26e"] = unsure("Unclear whether this means analysing running software processes or modelling software development processes.")
A["process-group-921cdb"] = unsure("Could mean a project-management process group, an operating-system process group or something else; I cannot tell.")
A["process-hazard-anlysis-04e6c7"] = new("Process hazard analysis", "method",
    "A structured review of an industrial or chemical process to identify its hazards and judge whether its safeguards are adequate.",
    variants=["Process hazards analysis"],
    reason="A misspelling of Process hazard analysis, a recognised safety method.")
A["process-improvements-1d4762"] = new("Process improvement", "skill",
    "Finding and putting in place changes that make a work process faster, cheaper, safer or more reliable.")
A["process-improvements-business-3d9462"] = new("Process improvement", "skill",
    "Finding and putting in place changes that make a work process faster, cheaper, safer or more reliable.",
    reason="Same concept as the untagged Process improvements tag, so answered with the same name.")
A["process-improvements-computing-fd1377"] = unsure("Could mean software process improvement or improving IT processes in general; I cannot tell which.")
A["process-management-business-26dc7c"] = new("Process management", "skill",
    "Planning, monitoring and improving how the steps of a business or manufacturing process are carried out.")
A["process-management-computing-3ed802"] = new("Process management (operating systems)", "knowledge",
    "The part of an operating system that creates, schedules, switches between and ends the running programs on a computer.",
    reason="Process management in computing is the operating-system function, a different concept from managing business processes.")
A["process-piping-43839a"] = new("Process piping", "skill",
    "Designing, fabricating, installing or inspecting piping that carries fluids in industrial plants such as refineries and chemical works.")
A["process-state-91fe04"] = new("Process state", "knowledge",
    "The condition of an operating-system process at a given moment, such as new, ready, running, waiting or terminated.")
A["processing-industry-a04054"] = nas("An industry sector, not a skill.")
A["processing-js-d4eacf"] = new("Processing.js", "library",
    "A JavaScript port of the Processing visual programming language that runs Processing sketches in web browsers.")
A["procore-9b0d3b"] = new("Procore", "platform",
    "Cloud-based construction management software for running projects, drawings, documents, budgets and field work in one place.")
A["prodigy-online-service-4ae0d3"] = nas("A former online service (a company product), not a skill.")
A["product-analysis-726c52"] = new("Product analysis", "skill",
    "Examining a product's features, quality, performance or market fit to judge how well it meets needs.")
A["product-analytics-1fd03c"] = new("Product analytics", "skill",
    "Analysing how people use a digital product, such as which features they use and where they drop out, to guide product decisions.")
A["product-benchmarking-e6b273"] = new("Product benchmarking", "method",
    "Comparing a product's features, price or performance with competing products to see where it stands and how to improve it.")
A["product-catalogue-management-b5ab5f"] = new("Product catalogue management", "skill",
    "Creating, organising and keeping up to date the descriptions, prices and images of the products a business sells.",
    variants=["Product catalog management"])
A["product-leadership-37fae6"] = new("Product leadership", "skill",
    "Guiding a product's vision, strategy and development and leading the people responsible for it.")
A["product-quality-assurance-f31047"] = new("Product quality assurance", "skill",
    "Planning and carrying out checks across design, production and testing so that a product meets its quality requirements.")
A["product-requirement-documents-f5aeff"] = new("Product requirements documentation", "skill",
    "Writing product requirements documents that set out what a product should do, for whom and why, so design and engineering can build it.",
    variants=["Product requirements document"])
A["product-strategies-975724"] = new("Product strategy", "skill",
    "Deciding what a product should achieve, for whom, and how it will succeed in its market over time.",
    rels=[("related", "pb9jup7p6r")])
A["production-aid-53cc57"] = nas("A job title or role, not a skill.")
A["production-equipment-controls-c81fd7"] = unsure("Could mean operating, maintaining or designing the control systems of production machinery; the phrase is too vague to define.")
A["production-preparation-542851"] = unsure("The meaning varies (manufacturing set-up, kitchen prep, media production), so I cannot tell what is meant.")
A["production-readiness-1bf2e5"] = unsure("Could be software production readiness reviews or manufacturing readiness; I cannot tell which.")
A["production-technique-8dbcc5"] = nas("A generic phrase with no fixed meaning, not a skill.")
A["professional-bookkeeping-service-519801"] = nas("Names a service business; the skill would be bookkeeping.")
A["professional-bridal-consultanting-9b4bc8"] = new("Bridal consulting", "skill",
    "Advising engaged couples, especially brides, on choosing wedding gowns and accessories or on planning the wedding.",
    reason="A misspelling of professional bridal consulting, a recognised service skill.")
A["professional-engineer-bf47be"] = variant("sk7bf8j7qf",
    "Professional Engineer is the title and licence that Licensed Professional Engineer describes.")
A["professional-hair-care-4adc92"] = nas("Generic phrase for hair products and services; the skill would be hairdressing or hair styling.")
A["professional-negligence-in-english-law-1e978e"] = new("Professional negligence in English law", "knowledge",
    "The area of English law about claims against professionals, such as solicitors and surveyors, who fail to meet the standard of care expected of them.")
A["professional-rescuer-cpr-a69b91"] = new("CPR for the Professional Rescuer", "credential",
    "A cardiopulmonary resuscitation certification, from American Red Cross courses, for people who respond to emergencies as part of their job, such as lifeguards and first responders.",
    cert=True, scope="single-issuer")
A["professional-studies-53c7a9"] = nas("A general name for academic programmes, not a skill.")
A["professionalism-3a6092"] = new("Professionalism", "skill",
    "Behaving in line with the standards of conduct, reliability and courtesy expected in a workplace.")
A["program-evaluations-f0c73e"] = new("Program evaluation", "skill",
    "Systematically gathering and analysing evidence to judge how well a programme works and whether it meets its goals.",
    rels=[("related", "nna0x6ic9d")])
A["program-optimization-0dacba"] = new("Program optimization", "skill",
    "Changing a computer program so that it runs faster or uses less memory or other resources while doing the same job.")
A["programmatic-media-buying-87dea7"] = new("Programmatic media buying", "skill",
    "Buying digital advertising space automatically through software and real-time auctions rather than by negotiating with each publisher.",
    variants=["Programmatic buying"], rels=[("broader", "qhvqe6edu5")])
A["programmer-s-hierarchical-interactive-gr-4da3cd"] = new("Programmer's Hierarchical Interactive Graphics System", "standard",
    "An ISO and ANSI standard from the 1980s for a programming interface for three-dimensional computer graphics.",
    variants=["PHIGS"])
A["programming-languages-1ab37b"] = nas("A category word for the whole group of programming languages, not one language or skill.")

if __name__ == "__main__":
    write(A)
