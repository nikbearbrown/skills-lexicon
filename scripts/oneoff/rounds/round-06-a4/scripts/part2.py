import sys
sys.path.insert(0, "work/scripts")
from lib import *

A = {}

A["nautical-charts-eac4d7"] = new(
    "Reading nautical charts is a recognised maritime knowledge area.",
    "Nautical charts", "knowledge",
    "Maps made for marine navigation that show water depths, coastlines, hazards and aids to navigation.")

A["navigation-cf03cf"] = unsure(
    "Too ambiguous: it could mean marine, air or land navigation, or website and app navigation.")

A["navigational-aid-3f1297"] = new(
    "A navigational aid is a category of equipment, treated like other tools.",
    "Navigational aid", "tool",
    "A device, marker or system, such as a buoy, beacon or radio transmitter, that helps ships or aircraft find their position and route.")

A["navisworks-bim-software-884632"] = new(
    "Navisworks is a named Autodesk product.",
    "Navisworks", "tool",
    "Autodesk software that combines design and construction models of a building project so they can be reviewed and checked for clashes.",
    variants=["Autodesk Navisworks"])

A["nccer-heo-forklift-a00d05"] = unsure(
    "Seems to be an NCCER forklift operator credential, but I cannot confirm the exact name or scheme.")

A["ncidq-certified-6fceda"] = new(
    "NCIDQ is the interior design certification awarded by CIDQ.",
    "NCIDQ Certification", "credential",
    "A certification for interior designers awarded by the Council for Interior Design Qualification (CIDQ) to those who meet its education and experience requirements and pass its exams.",
    variants=["NCIDQ"], cert=True, scope="single-issuer")

A["ndebele-language-ab98b9"] = new(
    "Ndebele is a human language, and the name covers two related languages.",
    "Ndebele", "human-language",
    "The name of two related Bantu languages: Northern Ndebele, spoken mainly in Zimbabwe, and Southern Ndebele, spoken in South Africa.",
    lang="human")

A["nedgraphics-textile-design-software-d8e1de"] = new(
    "NedGraphics is a named textile design software product.",
    "NedGraphics", "tool",
    "Computer-aided design software for textile and fashion design, such as print, weave and knit design.",
    relations=[R("related", "eakf49x3b5")])

A["needle-localization-f944fa"] = new(
    "Needle localization is a named clinical imaging procedure.",
    "Needle localization", "skill",
    "Marking the location of a lesion, usually in the breast, by placing a needle or wire under imaging guidance so a surgeon can find and remove it.",
)

A["negotiating-pricing-989b87"] = new(
    "Negotiating prices is a recognised commercial skill.",
    "Price negotiation", "skill",
    "Negotiating the price of goods or services with customers or suppliers.")

A["neonatal-intensive-care-nursing-0cd62b"] = new(
    "Neonatal intensive care nursing is a recognised nursing specialty.",
    "Neonatal intensive care nursing", "skill",
    "Nursing care for critically ill or premature newborns in a neonatal intensive care unit.")

A["nepali-language-916be2"] = new(
    "Nepali is a human language.",
    "Nepali", "human-language",
    "An Indo-Aryan language that is the official language of Nepal and is also spoken in parts of India.",
    lang="human")

A["net-profit-8bebc6"] = nas(
    "A financial figure, not a skill.")

A["net-promoter-score-df06d4"] = new(
    "Net Promoter Score is a named customer-loyalty metric and method.",
    "Net Promoter Score", "method",
    "A customer loyalty metric based on how likely customers are to recommend a company, scored from -100 to 100.")

A["net-zero-06936e"] = new(
    "Net zero is a defined sustainability concept.",
    "Net zero", "knowledge",
    "A state in which the greenhouse gases a person, company or country puts into the atmosphere are balanced by those removed.")

A["nette-cf0076"] = new(
    "Nette is a named PHP framework.",
    "Nette", "framework",
    "An open-source PHP framework for building web applications.",
    variants=["Nette Framework"])

A["network-intrusion-detection-systems-aff5c9"] = new(
    "Network intrusion detection systems are a category of security tool.",
    "Network intrusion detection system", "tool",
    "A tool that monitors network traffic for signs of attacks or policy violations and raises alerts.",
    variants=["NIDS"])

A["network-performance-433bf9"] = new(
    "Network performance is a part of the networking field.",
    "Network performance", "knowledge",
    "How fast, reliable and responsive a network is, judged by measures such as latency, throughput and packet loss.",
    relations=[R("broader", "fnhev4v1dn")])

A["network-security-administrator-0b2473"] = nas(
    "A job title, not a skill.")

A["network-topologies-a88572"] = new(
    "Network topology is a core networking concept.",
    "Network topology", "knowledge",
    "The arrangement of the nodes and links in a network, such as bus, star, ring and mesh.",
    variants=["Network topologies"], relations=[R("broader", "fnhev4v1dn")])

A["neurobiology-88ce67"] = new(
    "Neurobiology is an established science.",
    "Neurobiology", "knowledge",
    "The branch of biology that studies the nervous system and how it develops and works.")

A["neuromuscular-medicine-d37635"] = new(
    "Neuromuscular medicine is a recognised medical subspecialty.",
    "Neuromuscular medicine", "knowledge",
    "The medical subspecialty that diagnoses and treats diseases of the nerves, the muscles and the junctions between them.")

A["neuromuscular-system-and-disorders-3e6a2d"] = new(
    "Names a body of anatomy and clinical knowledge.",
    "Neuromuscular system and disorders", "knowledge",
    "How the nerves and muscles work together and the diseases that disrupt them.")

A["neurosurgeries-9d990d"] = new(
    "Plural form of neurosurgery, an established surgical specialty.",
    "Neurosurgery", "knowledge",
    "The surgical specialty that treats disorders of the brain, spinal cord and peripheral nerves.",
    variants=["Neurosurgeries"])

A["nexpose-vulnerability-scanning-software-e33b5f"] = new(
    "Nexpose is a named Rapid7 product related to, but distinct from, InsightVM.",
    "Nexpose", "tool",
    "Rapid7's vulnerability scanner, which finds and ranks security weaknesses in networks and systems.",
    relations=[R("related", "jx2hqz8q8r")])

A["next-js-694fd7"] = new(
    "Next.js is a named web framework.",
    "Next.js", "framework",
    "A React-based framework for building server-rendered and static web applications.",
    relations=[R("related", "hjzieo2ohv")])

A["nice-unix-utility-f7ffb0"] = new(
    "nice is a standard Unix command.",
    "nice (Unix utility)", "tool",
    "A Unix command that runs a program with a changed scheduling priority.")

A["nice-wfm-software-4ae172"] = new(
    "NICE's workforce management product.",
    "NICE Workforce Management", "tool",
    "Workforce management software from NICE for forecasting workload and scheduling staff in contact centres.",
    variants=["NICE WFM"])

A["night-work-1c1101"] = nas(
    "A work condition, not a skill.")

A["nightwatch-js-7ce883"] = new(
    "Nightwatch.js is a named testing framework.",
    "Nightwatch.js", "framework",
    "An end-to-end testing framework for web applications that runs on Node.js and drives browsers through WebDriver.")

A["nih-stroke-scale-nihss-c3eb29"] = new(
    "The NIH Stroke Scale is a clinical scoring scale, not a credential.",
    "NIH Stroke Scale", "method",
    "A standardised neurological examination scale that measures the severity of stroke symptoms.",
    variants=["NIHSS"],
    note="The NIH Stroke Scale is a clinical scoring scale; training certificates exist for using it but are a separate concept.")

A["nist-800-15cee0"] = new(
    "NIST's 800 series of Special Publications on information security.",
    "NIST SP 800 series", "standard",
    "NIST's 800 series of Special Publications, which give guidelines and recommendations on information security.",
    variants=["NIST 800"])

A["nist-800-37-a56c30"] = new(
    "NIST SP 800-37 is a specific NIST publication.",
    "NIST SP 800-37", "standard",
    "A NIST Special Publication that describes the Risk Management Framework for managing security and privacy risk in information systems.",
    variants=["NIST 800-37"])

A["nist-800-53-63f2a1"] = new(
    "NIST SP 800-53 is a specific NIST publication.",
    "NIST SP 800-53", "standard",
    "A NIST Special Publication that catalogues security and privacy controls for information systems and organisations.",
    variants=["NIST 800-53"])

A["nist-cybersecurity-framework-csf-e7056d"] = new(
    "The NIST CSF is a voluntary framework, not a credential.",
    "NIST Cybersecurity Framework", "framework",
    "A voluntary framework from NIST that organises cybersecurity activities into functions such as identify, protect, detect, respond and recover.",
    variants=["NIST CSF"], relations=[R("related", "norpz7ekiw")],
    note="The NIST Cybersecurity Framework is guidance published by NIST; no certification is awarded for it.")

A["nitrogen-phosphorous-detector-046ee3"] = new(
    "A named type of gas chromatography detector.",
    "Nitrogen-phosphorus detector", "tool",
    "A gas chromatography detector that responds selectively to compounds containing nitrogen or phosphorus.",
)

A["nlog-software-a5b133"] = new(
    "NLog is a named .NET logging library.",
    "NLog", "library",
    "An open-source logging library for .NET applications.")

A["nmc-guidelines-33e76e"] = unsure(
    "NMC could be the UK Nursing and Midwifery Council or India's National Medical Commission, and nothing here says which.")

A["no-child-left-behind-act-6547ca"] = new(
    "No Child Left Behind is a named US law that people are expected to know.",
    "No Child Left Behind Act", "standard",
    "A United States federal education law from the early 2000s that set testing and accountability requirements for public schools and was replaced in 2015 by the Every Student Succeeds Act.")

A["node-js-cfce80"] = new(
    "Node.js is a named runtime platform.",
    "Node.js", "platform",
    "A cross-platform JavaScript runtime built on Chrome's V8 engine that runs JavaScript outside the browser.")

A["node-oracle-8e2977"] = unsure(
    "Might be the node-oracledb driver for Node.js, but the term is too bare to be sure.")

A["node-package-manager-e4906f"] = new(
    "Node Package Manager is the spelled-out name of npm.",
    "npm", "tool",
    "The default package manager for Node.js, used to install and manage JavaScript packages.",
    variants=["Node Package Manager"])

A["non-detergents-sulfobetaines-83206e"] = nas(
    "A class of chemical reagents, not a skill.")

A["non-facility-associated-signalling-nfas-3d745e"] = new(
    "NFAS is a named ISDN signalling arrangement.",
    "Non-Facility Associated Signalling", "knowledge",
    "An ISDN primary rate interface arrangement in which a single D channel carries the signalling for several PRI trunk groups.",
    variants=["NFAS"])

A["non-fungible-tokens-nft-3f8530"] = new(
    "Non-fungible tokens are a defined blockchain concept.",
    "Non-fungible tokens", "knowledge",
    "Unique blockchain-based tokens that record ownership of a digital or physical item.",
    variants=["NFT", "Non-fungible token"])

A["nonverbal-communications-cd7eff"] = new(
    "Nonverbal communication is a recognised communication skill.",
    "Nonverbal communication", "skill",
    "Conveying and reading meaning without words, through body language, gestures, facial expression and tone.",
    variants=["Nonverbal communications"], relations=[R("broader", "gisypzf6gf")])

A["nosetests-4335fa"] = new(
    "nosetests is the test runner of the nose Python framework.",
    "nosetests", "framework",
    "The command-line test runner of nose, a Python unit testing framework that extends unittest.")

A["notion-software-4a3a2b"] = new(
    "Notion is a named workspace app; the name is disambiguated because Notion is also an everyday word.",
    "Notion (software)", "tool",
    "A workspace app for notes, documents, wikis and databases.")

A["novacare-rehabilitation-7144eb"] = nas(
    "A company, not a skill.")

A["novant-health-charlotte-orthopedic-hospi-75cf75"] = nas(
    "A hospital, not a skill.")

A["novant-health-f05f0f"] = nas(
    "A healthcare company, not a skill.")

if __name__ == "__main__":
    write(A)
