import sys
sys.path.insert(0, "work/scripts")
from lib import *

A = {}

A["motor-control-firmware-8b57ba"] = new(
    "Embedded code that drives electric motors is a recognised technical area.",
    "Motor control firmware", "knowledge",
    "Embedded software that runs on a microcontroller or drive to regulate the speed, torque or position of an electric motor.")

A["motor-control-software-de727f"] = new(
    "Software for controlling and tuning electric motors is a recognised technical area.",
    "Motor control software", "knowledge",
    "Software that controls, configures or monitors electric motors and drives, including embedded control code and host-side tools.")

A["movable-type-0b8eb6"] = new(
    "Movable Type is a named content management product.",
    "Movable Type", "platform",
    "A blogging and website content management platform first released by Six Apart in 2001.")

A["moz-92d181"] = new(
    "In skill lists Moz names the Moz SEO software.",
    "Moz Pro", "tool",
    "A subscription SEO software suite from Moz for keyword research, rank tracking, site audits and link analysis.",
    variants=["Moz"])

A["mstest-0909ec"] = new(
    "MSTest is Microsoft's unit testing framework.",
    "MSTest", "framework",
    "Microsoft's unit testing framework for .NET code, used with Visual Studio.",
    relations=[R("related", "ss273uzint")])

A["mud-pump-e07c2c"] = new(
    "A mud pump is drilling-rig equipment, like other machines treated as tools.",
    "Mud pump", "tool",
    "A high-pressure pump on a drilling rig that circulates drilling fluid down the drill string and back up the borehole.")

A["mulesoft-7c688e"] = new(
    "MuleSoft is a named integration platform.",
    "MuleSoft", "platform",
    "Integration software, now owned by Salesforce, whose Anypoint Platform connects applications, data and APIs.")

A["multi-agent-systems-219759"] = new(
    "Multi-agent systems is an established field of computing.",
    "Multi-agent systems", "knowledge",
    "Systems made of several autonomous agents, such as software programs or robots, that interact to cooperate or compete in solving problems.")

A["multi-core-processors-fdeffb"] = new(
    "Multi-core processors are a hardware topic engineers are expected to know.",
    "Multi-core processors", "knowledge",
    "Processors that place two or more independent processing cores on one chip so they can run tasks in parallel.")

A["multi-core-programming-388c88"] = new(
    "Writing code for several processor cores is a recognised programming skill.",
    "Multi-core programming", "skill",
    "Writing software that divides work across the several cores of a processor so tasks run in parallel.")

A["multi-core-smp-ca7156"] = new(
    "SMP on multi-core chips is a standard computer architecture topic.",
    "Multi-core SMP", "knowledge",
    "Symmetric multiprocessing on multi-core processors, where identical cores share one memory and are scheduled by a single operating system.")

A["multi-core-software-c594f8"] = new(
    "Same concept as Multi-Core Programming, answered under the identical name.",
    "Multi-core programming", "skill",
    "Writing software that divides work across the several cores of a processor so tasks run in parallel.")

A["multi-device-design-ee19a7"] = new(
    "Designing interfaces that work across devices is a recognised design skill.",
    "Multi-device design", "skill",
    "Designing a product's interface so it works well across different devices and screen sizes, such as phones, tablets and desktops.",
    relations=[R("related", "xrhig81x22")])

A["multi-objective-design-space-exploration-1621b3"] = nas(
    "It is the title of a research project (MULTICUBE), not a skill.")

A["multi-programming-monitor-control-progra-5d7e09"] = new(
    "MP/M is a named operating system from Digital Research.",
    "MP/M", "platform",
    "A multi-user, multitasking operating system from Digital Research that extended CP/M.",
    variants=["Multi-Programming Monitor Control Program"])

A["multi-tenant-915bef"] = new(
    "Multitenancy is a standard software architecture concept.",
    "Multitenancy", "knowledge",
    "A software architecture in which one running instance of an application serves several customers, called tenants, whose data is kept separate.",
    variants=["Multi-tenancy", "Multi-tenant"])

A["multi-touch-d6b373"] = new(
    "Multi-touch is a named input technology.",
    "Multi-touch", "knowledge",
    "A touch-input technology that detects two or more simultaneous points of contact, enabling gestures such as pinch and swipe.")

A["multichannel-marketing-5dd830"] = new(
    "Multichannel marketing is an established marketing practice.",
    "Multichannel marketing", "skill",
    "Marketing to customers through several channels, such as email, social media, stores and websites, at the same time.",
    relations=[R("related", "dv5vi280tf")])

A["multicultural-education-d69a3e"] = new(
    "Multicultural education is an established field in education.",
    "Multicultural education", "knowledge",
    "An approach to teaching that reflects the histories, cultures and perspectives of diverse groups so that all students have a fair chance to learn.")

A["multidisciplinary-approach-deb508"] = nas(
    "A generic phrase for working across disciplines, not a distinct skill.")

A["mushroom-aa1465"] = nas(
    "A generic word for an organism or food, not a skill.")

A["music-instruction-ee0fab"] = new(
    "Teaching music is a recognised skill.",
    "Music instruction", "skill",
    "Teaching others to play an instrument, sing or understand music.",
    variants=["Music teaching"])

A["music-theories-0afd73"] = new(
    "Plural form of the field called music theory.",
    "Music theory", "knowledge",
    "The study of how music is built, including notation, scales, harmony, rhythm and form.")

A["mutant-605d0d"] = unsure(
    "Could be a generic word or a mutation-testing tool, and there is no context to tell.")

A["mutual-exclusion-46a9ab"] = new(
    "Mutual exclusion is a core concurrency concept.",
    "Mutual exclusion", "knowledge",
    "A requirement in concurrent programming that only one thread or process at a time may use a shared resource or critical section.")

A["mutual-fund-247875"] = new(
    "Mutual funds are a financial product area people are expected to know.",
    "Mutual funds", "knowledge",
    "Investment vehicles that pool money from many investors to buy a diversified portfolio of securities.",
    variants=["Mutual fund"])

A["myhr-software-4392f4"] = unsure(
    "Several different HR products are called MyHR and nothing here says which one is meant.")

A["nagle-s-algorithm-fceb6f"] = new(
    "Nagle's algorithm is a named TCP technique.",
    "Nagle's algorithm", "method",
    "A TCP technique that reduces the number of small packets sent by holding back small writes until earlier data has been acknowledged.")

A["naivebayes-d0492c"] = new(
    "Naive Bayes is a standard machine-learning method.",
    "Naive Bayes", "method",
    "A family of simple probabilistic classifiers that apply Bayes' theorem while assuming that features are independent of each other given the class.",
    variants=["Naive Bayes classifier"])

A["naked-short-selling-1d15aa"] = new(
    "Naked short selling is a named market practice with its own rules.",
    "Naked short selling", "knowledge",
    "Selling shares short without first borrowing them or arranging to borrow them, a practice restricted in many markets.")

A["namenode-58fbf4"] = new(
    "The NameNode is a named component of Hadoop's file system.",
    "NameNode", "tool",
    "The master server of the Hadoop Distributed File System, which keeps the file-system namespace and records where each data block is stored.")

A["nanobiotechnology-c0c96f"] = new(
    "Nanobiotechnology is an established research field.",
    "Nanobiotechnology", "knowledge",
    "The field that applies nanoscale technologies to biology and medicine, for example in drug delivery and diagnostics.")

A["nanocomposite-b5a83a"] = new(
    "Nanocomposites are a materials science topic.",
    "Nanocomposites", "knowledge",
    "Materials that combine a bulk matrix with particles or fibres smaller than about 100 nanometres to improve properties such as strength or conductivity.",
    variants=["Nanocomposite"])

A["nanolithography-a12997"] = new(
    "Nanolithography is an established fabrication field.",
    "Nanolithography", "knowledge",
    "Techniques for printing or etching patterns with features measured in nanometres, used mainly to make semiconductor chips.")

A["nasotracheal-suctioning-580447"] = new(
    "Nasotracheal suctioning is a named clinical procedure, distinct from endotracheal suctioning.",
    "Nasotracheal suctioning", "skill",
    "Clearing secretions from a patient's airway by passing a suction catheter through the nose into the throat and trachea.",
    relations=[R("related", "mkkre3uwga")])

A["national-airspace-system-nas-c69c0e"] = new(
    "The National Airspace System is a defined body of aviation knowledge.",
    "National Airspace System", "knowledge",
    "The network of United States airspace, airports, navigation facilities, rules and personnel that makes up civil and military flying.")

A["national-certified-patient-care-technici-d6fb80"] = new(
    "A named certification, awarded by a different body from the nearby Certified Patient Care Technician.",
    "National Certified Patient Care Technician", "credential",
    "A certification for patient care technicians awarded by the National Center for Competency Testing (NCCT).",
    variants=["NCPCT"], relations=[R("related", "f881v6vufj")], cert=True, scope="single-issuer")

A["national-certified-school-counselor-8b585e"] = new(
    "A named certification awarded by the National Board for Certified Counselors.",
    "National Certified School Counselor", "credential",
    "A certification for school counselors awarded by the National Board for Certified Counselors (NBCC).",
    cert=True, scope="single-issuer")

A["national-geothermal-data-systems-12bdf4"] = new(
    "The National Geothermal Data System is a named data network.",
    "National Geothermal Data System", "platform",
    "A United States Department of Energy-funded network of geothermal data sources that can be searched together.")

A["national-lifeguard-service-d9c399"] = unsure(
    "Seems to be a Canadian lifeguard certification, but I cannot confirm the issuing body or the exact scheme.")

A["national-registry-emergency-medical-tech-6d7450"] = new(
    "A named certification awarded by the National Registry of Emergency Medical Technicians.",
    "National Registry Emergency Medical Technician", "credential",
    "An emergency medical technician certification awarded by the National Registry of Emergency Medical Technicians in the United States.",
    variants=["NREMT"], cert=True, scope="single-issuer")

A["nationally-certified-school-nurse-461ccb"] = new(
    "A named certification awarded by the National Board for Certification of School Nurses.",
    "Nationally Certified School Nurse", "credential",
    "A certification for school nurses awarded by the National Board for Certification of School Nurses.",
    variants=["NCSN"], cert=True, scope="single-issuer")

A["nationwide-mortgage-licensing-system-nml-ef2b83"] = new(
    "NMLS is the licensing registry, not itself a credential.",
    "Nationwide Multistate Licensing System", "platform",
    "The online system, run by the State Regulatory Registry, through which US mortgage loan originators and other financial professionals are licensed and registered by state regulators.",
    variants=["Nationwide Mortgage Licensing System", "NMLS"],
    note="NMLS is a licensing registry; the licence recorded in it is a separate concept, so this is not a certification.")

A["native-american-studies-0d8d42"] = new(
    "Native American studies is an established academic field.",
    "Native American studies", "knowledge",
    "An interdisciplinary academic field that studies the histories, cultures, politics and societies of Native American peoples.")

A["native-sql-8e4adf"] = unsure(
    "Could mean a database's own SQL dialect or a vendor feature called Native SQL, and nothing here says which.")

A["nativescript-95a14a"] = new(
    "NativeScript is a named app framework.",
    "NativeScript", "framework",
    "An open-source framework for building native iOS and Android apps from a single JavaScript or TypeScript code base.",
    relations=[R("related", "h60l8olauw"), R("related", "y37j4kl3jo")])

A["natural-capital-a24237"] = new(
    "Natural capital is a defined concept in economics and sustainability.",
    "Natural capital", "knowledge",
    "The world's stock of natural assets, such as land, water, air and living things, that provides goods and services to people.")

A["natural-gas-pipelines-de358e"] = new(
    "Natural gas pipelines are an engineering and operations domain.",
    "Natural gas pipelines", "knowledge",
    "The pipeline systems that transport natural gas, and the engineering, operation and regulation of them.")

A["natural-language-generation-86f311"] = new(
    "Natural language generation is a subfield of natural language processing.",
    "Natural language generation", "knowledge",
    "The part of natural language processing concerned with having software produce readable human language from data or meaning.",
    relations=[R("broader", "d168utcmjy"), R("related", "ivx36sezid")],
    note="Natural language generation is a field of computing, not a language.")

A["natural-language-processing-systems-5cce22"] = new(
    "Systems built with natural language processing; related to the field but not the same concept.",
    "Natural language processing systems", "knowledge",
    "Software systems that analyse or produce human language, such as translators, chatbots and text classifiers.",
    relations=[R("related", "d168utcmjy")],
    note="This names systems built with a field of computing, not a language.")

if __name__ == "__main__":
    write(A)
