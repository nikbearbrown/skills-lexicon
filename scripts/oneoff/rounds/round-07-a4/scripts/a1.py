from common import *
A = {}
A["Scope Statement"] = new("Scope statement", "skill",
    "Writing the document that sets out a project's objectives, deliverables, boundaries and exclusions.",
    variants=["Project scope statement"])
A["Screen Designs"] = new("Screen design", "skill",
    "Designing the layout, content and visual appearance of individual screens in an app, website or device interface.",
    relations=[R("related", "sixghka9vw")])
A["Screen Reader"] = new("Screen reader", "tool",
    "Assistive software that reads on-screen text and interface elements aloud, or sends them to a braille display, for blind and low-vision users.")
A["Screenshots"] = na("A generic noun for a captured image of a screen, not a distinct skill.")
A["Screw Conveyor"] = new("Screw conveyor", "tool",
    "A conveyor that moves bulk material along a trough or tube with a rotating helical screw.",
    variants=["Auger conveyor"], relations=[R("related", "lgdf0oiq2g")])
A["Script Writing"] = new("Script writing", "skill",
    "Writing the dialogue, action and structure of a script for film, television, theatre, radio or video.",
    variants=["Scriptwriting"])
A["Sd Card"] = new("SD card", "tool",
    "A small removable flash-memory card in the Secure Digital format, used to store data in cameras, phones and other devices.",
    variants=["Secure Digital card"])
A["Sdn"] = unsure("Abbreviation with several meanings (for example software-defined networking) and no context to choose between them.")
A["Seafood"] = na("A generic food word, not a skill.")
A["Seal (Mechanical)"] = new("Mechanical seal", "tool",
    "A device that stops fluid leaking along a rotating shaft where it passes through the casing of a pump, mixer or similar machine.")
A["Seamanship"] = new("Seamanship", "skill",
    "The skill of handling, navigating and maintaining a boat or ship safely at sea.")
A["Seat Guests"] = new("Seating guests", "skill",
    "Showing arriving guests to their tables or seats in a restaurant, event or venue.",
    relations=[R("related", "nnpo33gfsf")])
A["Secondary Source"] = unsure("A research term for a type of document; it is not clear it names a skill rather than a kind of material.")
A["Secretion"] = na("A biological process (release of substances by cells or glands), not a skill.")
A["Section Drawings"] = new("Section drawings", "skill",
    "Preparing or reading drawings that show a building or object as if cut through along a plane, to reveal its internal construction.",
    variants=["Section drawing"], relations=[R("broader", "fbmyyojcj3")])
A["Secure Coding Best Practices"] = new("Secure coding", "skill",
    "Writing software in ways that avoid common security flaws, such as injection, unsafe input handling and memory errors.",
    variants=["Secure coding practices"])
A["Secure Shell"] = new("Secure Shell", "standard",
    "A network protocol for encrypted remote login and command execution between computers.",
    variants=["SSH"])
A["Secured Transactions (Contract Law)"] = new("Secured transactions", "knowledge",
    "The area of commercial law that governs loans and credit backed by collateral in personal property, such as Article 9 of the US Uniform Commercial Code.")
A["Security Certified Network Architecture"] = new("Security Certified Network Architect", "credential",
    "A certification from the Security Certified Program for designing secure network architectures.",
    variants=["SCNA"], cert=True, scope="single-issuer")
A["Security Information And Event Management"] = new("Security information and event management", "tool",
    "Software that gathers and correlates security logs and events from across an organisation so that threats can be detected, investigated and reported.",
    variants=["SIEM"], verbs=["monitor", "configure"])
A["Security Level Management"] = unsure("Not a standard term; it could mean access-control clearance levels or alert severity levels, and the name alone does not say which.")
A["Security Liaison Officer"] = na("A job title, not a skill.")
A["Security Managing"] = new("Security management", "skill",
    "Planning and overseeing the measures, people and procedures that protect an organisation's people, property and information.")
A["Security Onion (Intrusion Detection System)"] = new("Security Onion", "platform",
    "A free Linux distribution for network security monitoring, intrusion detection, log management and threat hunting.",
    relations=[R("related", "uuer0jxuof")])
A["Security Operations"] = new("Security operations", "skill",
    "Running the monitoring, detection and response work that keeps an organisation's systems and data secure.",
    variants=["SecOps"])
A["Security Operations (SecOps)"] = new("Security operations", "skill",
    "Running the monitoring, detection and response work that keeps an organisation's systems and data secure.",
    variants=["SecOps"])
A["Security Vision"] = unsure("Could be a vendor product or a vision-related phrase; the name alone does not say which.")
A["Seeder"] = new("Seeder", "tool",
    "A farm machine that sows seeds into the soil at a set depth and spacing.")
A["Seesaw (Educational Software)"] = new("Seesaw (software)", "platform",
    "A classroom app where students build digital portfolios of their work and teachers share it with families.")
A["Segment (Software)"] = new("Segment (software)", "platform",
    "A customer data platform, owned by Twilio, that collects event data from websites and apps and sends it to other tools.",
    variants=["Twilio Segment"])
A["Seim (Language)"] = unsure("I do not know for certain which language this names; it may be a small language of Papua New Guinea.")
A["Selection Rule"] = unsure("Used in several fields (for example quantum mechanics and data processing) with different meanings, and no context is given.")
A["Selenium"] = new("Selenium", "framework",
    "An open-source suite for automating web browsers, mainly used to write automated tests for web applications.",
    verbs=["automate"])
A["Self- Confident"] = new("Self-confidence", "ability",
    "Trust in one's own abilities and judgment, shown by acting and speaking without undue doubt.",
    variants=["Self-confident"])
A["Self Confident"] = new("Self-confidence", "ability",
    "Trust in one's own abilities and judgment, shown by acting and speaking without undue doubt.",
    variants=["Self-confident"])
A["Self-Discharger"] = unsure("Unclear whether this means a battery that loses charge by itself or a patient who leaves care; neither is a recognised skill term.")
A["Self-Harm"] = na("A behaviour or clinical symptom, not a skill.")
A["Self-started"] = new("Self-starter", "ability",
    "Taking the initiative to begin and carry out work without being told or closely supervised.",
    variants=["Self starter"])
A["Seliwanoff'S Tests"] = new("Seliwanoff's test", "method",
    "A chemical test using resorcinol and hydrochloric acid that tells ketose sugars, such as fructose, from aldose sugars.",
    variants=["Seliwanoff test"], relations=[R("related", "wck3opdy5d")])
A["Semicolon"] = na("A punctuation mark, not a skill.")
A["Senior Certified Welding Inspector"] = new("Senior Certified Welding Inspector", "credential",
    "An American Welding Society certification for experienced welding inspectors, ranking above the Certified Welding Inspector.",
    variants=["SCWI"], cert=True, scope="single-issuer")
A["Sequel Pro"] = new("Sequel Pro", "tool",
    "A free Mac application for managing MySQL and MariaDB databases through a graphical interface.")
A["Sequelize.js"] = new("Sequelize", "library",
    "A JavaScript object-relational mapper for Node.js that works with databases such as PostgreSQL, MySQL, MariaDB, SQLite and SQL Server.")
A["Serial ATA"] = new("Serial ATA", "standard",
    "A computer bus interface standard for connecting storage drives such as hard disks and solid-state drives to a motherboard.",
    variants=["SATA"])
A["Serial Line Internet Protocolss"] = new("Serial Line Internet Protocol", "standard",
    "A simple protocol that carries IP packets over serial lines such as dial-up modem links, described in RFC 1055.",
    variants=["SLIP"], relations=[R("related", "npe8caepoo")])
FIN = "A FINRA qualification exam and registration for "
A["Series 22 Direct Participation (Limited Partnerships) License"] = new("Series 22 Direct Participation Programs Limited Representative", "credential",
    FIN + "representatives who sell direct participation programs, such as limited partnerships.",
    variants=["Series 22"], cert=True, scope="single-issuer")
A["Series 24 General Securities Principal License"] = new("Series 24 General Securities Principal", "credential",
    FIN + "principals who supervise a broker-dealer's general securities business.",
    variants=["Series 24"], cert=True, scope="single-issuer")
A["Series 26 Investment Company And Variable Contracts Products Principal License"] = new("Series 26 Investment Company and Variable Contracts Products Principal", "credential",
    FIN + "principals who supervise the sale of mutual funds and variable annuities.",
    variants=["Series 26"], cert=True, scope="single-issuer")
A["Series 27 Financial And Operations Principal License"] = new("Series 27 Financial and Operations Principal", "credential",
    FIN + "principals who supervise a broker-dealer's financial reporting and operations.",
    variants=["Series 27"], cert=True, scope="single-issuer")
A["Series 3 National Exchange License"] = new("Series 3 National Commodity Futures", "credential",
    "A qualification exam, administered through FINRA for the National Futures Association, for people who sell futures and options on futures.",
    variants=["Series 3"], cert=True, scope="single-issuer")

if __name__ == "__main__":
    write(slice_terms(0, 50), A)
