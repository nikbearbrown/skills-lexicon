from common import *
A = {}
FIN = "A FINRA qualification exam and registration for "
A["Series 31 Futures : Managed Funds License"] = new("Series 31 Futures Managed Funds", "credential",
    "A qualification exam, administered through FINRA for the National Futures Association, for people who sell managed futures funds.",
    variants=["Series 31"], cert=True, scope="single-issuer")
A["Series 4 Registered Options Principal License"] = new("Series 4 Registered Options Principal", "credential",
    FIN + "principals who supervise a firm's options business.",
    variants=["Series 4"], cert=True, scope="single-issuer")
A["Series 52 Municipal Securities Representative License"] = new("Series 52 Municipal Securities Representative", "credential",
    "A qualification exam, written by the Municipal Securities Rulemaking Board and administered by FINRA, for representatives who sell municipal securities.",
    variants=["Series 52"], cert=True, scope="single-issuer")
A["Series 53 Municipal Securities Principal License"] = new("Series 53 Municipal Securities Principal", "credential",
    "A qualification exam, written by the Municipal Securities Rulemaking Board and administered by FINRA, for principals who supervise a firm's municipal securities business.",
    variants=["Series 53"], cert=True, scope="single-issuer")
A["Series 55 Equity Trader : Limited Representative License"] = new("Series 55 Equity Trader Limited Representative", "credential",
    FIN + "traders of equity securities at broker-dealers.",
    variants=["Series 55"], cert=True, scope="single-issuer")
A["Series 56 Proprietary Trader Qualification License"] = new("Series 56 Proprietary Trader", "credential",
    FIN + "traders who trade a firm's own capital in securities.",
    variants=["Series 56"], cert=True, scope="single-issuer")
A["Series 6 Investment Company And Variable Contracts License (Mutual Funds/Variable Annuities)"] = new("Series 6 Investment Company and Variable Contracts Products Representative", "credential",
    FIN + "representatives who sell mutual funds and variable annuities.",
    variants=["Series 6"], cert=True, scope="single-issuer")
A["Series 63 Uniform Securities Agent State Law License"] = new("Series 63 Uniform Securities Agent State Law", "credential",
    "A state securities-law exam, written by the North American Securities Administrators Association, that most states require of people who sell securities.",
    variants=["Series 63"], cert=True, scope="many-issuers")
A["Series 65 Uniform Registered Investment Adviser Law License (RIA)"] = new("Series 65 Uniform Investment Adviser Law", "credential",
    "A state securities-law exam, written by the North American Securities Administrators Association, for people who give investment advice for a fee.",
    variants=["Series 65"], cert=True, scope="many-issuers")
A["Series 66 Uniform Investment Adviser : Combined State Laws License (Combined 63 And 65)"] = new("Series 66 Uniform Combined State Law", "credential",
    "A state securities-law exam that combines the state-law content of the Series 63 and Series 65 exams, for people who work as both securities agents and investment adviser representatives.",
    variants=["Series 66"], cert=True, scope="many-issuers")
A["Series 7 General Securities Representative License (Stockbroker)"] = new("Series 7 General Securities Representative", "credential",
    FIN + "representatives who sell most types of securities, such as stocks, bonds and mutual funds.",
    variants=["Series 7"], cert=True, scope="single-issuer")
A["Series 79 Investment Banking License"] = new("Series 79 Investment Banking Representative", "credential",
    FIN + "investment bankers who advise on securities offerings and mergers and acquisitions.",
    variants=["Series 79"], cert=True, scope="single-issuer")
A["Series 86 Research Analyst : Securities Analysis"] = new("Series 86 Research Analyst (Analysis)", "credential",
    "The securities-analysis part of FINRA's research analyst qualification exams, covering valuation and financial analysis.",
    variants=["Series 86"], cert=True, scope="single-issuer")
A["Series 9 General Securities Sales Supervisor License : Options"] = new("Series 9 General Securities Sales Supervisor (Options Module)", "credential",
    FIN + "general securities sales supervisors, covering the supervision of options sales.",
    variants=["Series 9"], cert=True, scope="single-issuer")
A["Series 99 Operations Professional"] = new("Series 99 Operations Professional", "credential",
    FIN + "operations staff at broker-dealers.",
    variants=["Series 99"], cert=True, scope="single-issuer")
A["Service Delivery"] = unsure("A broad business term used in IT, health care and consulting with different meanings; the name alone does not fix one.")
A["Service Desk"] = new("Service desk", "skill",
    "Giving users first-line support for IT problems and requests, and logging, resolving or escalating each case.")
A["Service Development Studio"] = unsure("I cannot tell which product or vendor this names.")
A["Service Excellence - Health Care"] = unsure("Could be a training programme, a quality standard or a general aim; the name alone does not say which.")
A["Service Level Requirement"] = new("Service level requirement", "skill",
    "Defining and recording what a customer needs from a service, such as availability and response time, as the basis for a service level agreement.")
A["Service-Orientation"] = new("Service orientation", "skill",
    "Looking out for chances to be useful to other people and acting on them.")
A["Service Provisioning Markup Languages"] = new("Service Provisioning Markup Language", "markup-language",
    "An OASIS XML-based standard for exchanging user, resource and service provisioning information between systems.",
    variants=["SPML"], lang="programming")
A["Service Quality"] = unsure("A broad management and telecoms term with different meanings (customer service quality, quality of service); the name alone does not fix one.")
A["Servicenow"] = new("ServiceNow", "platform",
    "A cloud platform for IT service management and for automating business workflows.",
    verbs=["administer", "configure"])
A["ServiceNow Discovery"] = new("ServiceNow Discovery", "tool",
    "A ServiceNow product that scans a network to find devices and applications and records them in the configuration management database.")
A["Servient Estate"] = na("A property-law term for land burdened by an easement, not a skill or field.")
A["Servsafe Alcohol"] = new("ServSafe Alcohol", "credential",
    "A responsible-alcohol-service certification from the National Restaurant Association's ServSafe program.",
    cert=True, scope="single-issuer")
A["Setenv"] = unsure("Probably the name of a shell command or script (csh setenv, Tomcat setenv.sh), not clearly a skill.")
A["Setup Deployment"] = unsure("Vague phrase that could mean installer projects, software rollout or something else.")
A["Sex Therapy"] = new("Sex therapy", "skill",
    "Counselling or psychotherapy that helps individuals and couples with sexual difficulties and concerns.")
A["Sha256"] = new("SHA-256", "standard",
    "A cryptographic hash function from the SHA-2 family, specified in NIST FIPS 180-4, that produces a 256-bit digest.")
A["Sha512"] = new("SHA-512", "standard",
    "A cryptographic hash function from the SHA-2 family, specified in NIST FIPS 180-4, that produces a 512-bit digest.")
A["Shake"] = unsure("Could be the SHAKE hash functions, a drink or a motion; no context.")
A["Shama (Language)"] = unsure("I do not know for certain which language this names.")
A["Shan (Language)"] = new("Shan", "human-language",
    "A Tai language spoken by the Shan people, mainly in Shan State, Myanmar.",
    lang="human")
A["Sharable Content Object Reference Model"] = new("Sharable Content Object Reference Model", "standard",
    "A set of technical standards for packaging e-learning content and tracking learners so that courses work across learning management systems.",
    variants=["SCORM"])
A["Shared Vision Planning"] = new("Shared Vision Planning", "method",
    "A collaborative water-resources planning approach that combines traditional planning, stakeholder participation and shared computer models.")
A["Shareholder"] = na("A person or company that owns shares, not a skill.")
A["Shareholder Value"] = na("A finance concept, not a skill.")
A["Sharp Zaurus"] = new("Sharp Zaurus", "tool",
    "A line of handheld personal digital assistants made by Sharp, many of which run Linux.")
A["Shepard'S Citations"] = new("Shepard's Citations", "tool",
    "A LexisNexis legal research service that lists later cases and authorities citing a given case, showing whether it is still good law.",
    verbs=["shepardize"])
A["Shilajit"] = na("A natural substance used in Ayurvedic medicine, not a skill.")
A["Ship Handling"] = new("Ship handling", "skill",
    "Controlling a ship's movement, especially manoeuvring it in confined water and when berthing.",
    variants=["Shiphandling"])
A["Shipping and Receiving"] = new("Shipping and receiving", "skill",
    "Preparing and dispatching outgoing goods and checking, recording and storing incoming goods.",
    relations=[R("related", "lpcilh3rqk")])
A["Shortening"] = na("A generic word (a baking fat, among other senses), not a skill.")
A["Shoulder Surgeries"] = new("Shoulder surgery", "skill",
    "Performing or assisting with operations on the shoulder joint, such as rotator cuff repair and joint replacement.")
A["Shower Installation"] = new("Shower installation", "skill",
    "Fitting a shower, including its enclosure, valves and drainage, in a bathroom.")
A["Shrink Wrap"] = new("Shrink wrapping", "skill",
    "Packaging items in plastic film that is shrunk tight around them with heat.")
A["Shuttle Car Operating"] = new("Shuttle car operation", "skill",
    "Driving a shuttle car, the low electric haulage vehicle that carries cut coal or ore from the mining machine to the conveyor in an underground mine.")
A["Siege"] = unsure("Could be the HTTP load-testing tool, a game or the military term; no context.")

if __name__ == "__main__":
    write(slice_terms(50, 100), A)
