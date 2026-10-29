from lib_answers import *

A = {}
A["play-therapy-0cf677"] = new("Play therapy", "skill",
    "Using play, such as toys, drawing and games, as the way children express feelings and work through problems in therapy.")
A["player-coach-b35618"] = nas("A job role (a manager who also does individual work), not a skill.")
A["plink-d8e561"] = new("PLINK", "tool",
    "A free, open-source command-line toolset for analysing genotype data, mainly in genome-wide association studies and population genetics.")
A["plumbing-fixture-d9fd6e"] = nas("Names a type of equipment, not a skill.")
A["plumbing-plans-examination-f3840e"] = new("Plumbing plans examination", "skill",
    "Reviewing plumbing plans to check that they comply with the plumbing code, typically before a building permit is issued.",
    variants=["Plumbing plan review"])
A["plywood-366f76"] = nas("A building material, not a skill.")
A["pneumatic-tube-941777"] = nas("Names a piece of equipment, not a skill.")
A["point-to-point-tunneling-protocols-f5d1f9"] = new("Point-to-Point Tunneling Protocol", "standard",
    "A network protocol, described in RFC 2637, that carries PPP traffic through a tunnel to build virtual private networks.",
    variants=["PPTP"])
A["police-accountability-80b669"] = new("Police accountability", "knowledge",
    "The laws, oversight bodies and practices, such as civilian review and use-of-force reporting, that hold police answerable for their conduct.")
A["policy-analysis-07a632"] = new("Policy analysis", "skill",
    "Evaluating public policies and their alternatives, costs and likely effects so as to advise the people who decide.")
A["policy-research-and-analysis-77a732"] = new("Policy analysis", "skill",
    "Evaluating public policies and their alternatives, costs and likely effects so as to advise the people who decide.",
    reason="Policy research and analysis is the same activity as policy analysis; answered with the same name so it can be merged.")
A["political-opportunity-1c2dbc"] = unsure("Could be the political-science idea of political opportunity structure or an everyday phrase; I cannot tell which is meant.")
A["poll-everywhere-polling-software-cc7ecc"] = new("Poll Everywhere", "tool",
    "An online audience-response service where a presenter asks questions and participants answer from their phones or browsers, with results shown live.")
A["polycom-video-conferencing-7cad88"] = new("Polycom", "tool",
    "Video and audio conferencing equipment and software from Polycom, a company that later became part of Poly.")
A["portfolio-management-professional-76fcdb"] = new("Portfolio Management Professional", "credential",
    "A Project Management Institute certification for people who manage a portfolio of projects and programs so that it supports an organisation's strategy.",
    variants=["PfMP"], cert=True, scope="single-issuer")
A["portuguese-language-dd4a75"] = new("Portuguese", "human-language",
    "A Romance language spoken in Portugal, Brazil and several other countries.", lang="human")
A["positive-airway-pressure-03f5b1"] = new("Positive airway pressure", "skill",
    "Treating breathing problems such as sleep apnea by delivering pressurised air through a mask to keep the airway open, as CPAP and BiPAP machines do.",
    variants=["Positive airway pressure therapy"])
A["positive-airway-pressure-cpab-bipap-5c6519"] = new("Positive airway pressure", "skill",
    "Treating breathing problems such as sleep apnea by delivering pressurised air through a mask to keep the airway open, as CPAP and BiPAP machines do.",
    variants=["Positive airway pressure therapy"],
    reason="The term is a misspelling of CPAP/BiPAP; same concept as the other positive airway pressure tag, so answered with the same name.")
A["positive-discipline-community-resources-019bf9"] = unsure("Seems to relate to Positive Discipline parenting and teaching materials, but the phrase does not clearly name one skill I can define.")
A["posix-ed9c90"] = new("POSIX", "standard",
    "A family of IEEE standards that define a common interface for Unix-like operating systems, covering the shell, utilities and programming interfaces.",
    variants=["Portable Operating System Interface"])
A["post-office-protocol-ace14d"] = new("Post Office Protocol", "standard",
    "An internet email protocol that lets a mail program download messages from a mail server; its current version is POP3.",
    variants=["POP3"])
A["postcss-e6bf13"] = new("PostCSS", "tool",
    "A JavaScript tool that transforms CSS through plugins, for example to add vendor prefixes or allow newer syntax.",
    rels=[("related", "x4397709dt")])
A["postman-e67b8b"] = new("Postman", "tool",
    "A desktop and cloud application for building, testing and documenting APIs by sending requests and inspecting the responses.")
A["postorder-bccab8"] = new("Postorder traversal", "method",
    "Visiting every node of a tree by processing a node's children before the node itself.",
    variants=["Post-order traversal"])
A["postpartum-period-028bc9"] = nas("A period of time after childbirth, not a skill.")
A["potential-applications-of-carbon-nanotub-34293a"] = nas("The title of a topic or article about uses of a material, not a skill or field.")
A["pothead-713004"] = nas("Slang for a heavy cannabis user (or a cable-termination fitting); either way not a skill.")
A["pouchdb-7c73ad"] = new("PouchDB", "library",
    "An open-source JavaScript database that runs in the browser or Node.js and can synchronise with CouchDB.")
A["power-flow-studies-c8aa2b"] = new("Power flow study", "skill",
    "Calculating the voltages and the real and reactive power flowing through an electrical power system under given load conditions.",
    variants=["Load flow study"])
A["power-tool-operation-3a7328"] = new("Power tool operation", "skill",
    "Using powered hand and bench tools, such as drills, saws and sanders, to cut, shape or join materials.")
A["powered-industrial-truck-pit-operation-a02b91"] = new("Powered industrial truck operation", "skill",
    "Driving forklifts and other powered industrial trucks to move and stack loads; in the United States OSHA requires employers to train and evaluate operators.")
A["pre-sales-engineering-b0d18c"] = new("Pre-sales engineering", "skill",
    "Supporting the sales process by learning a customer's needs, demonstrating the product and designing a technical solution before the sale.",
    variants=["Presales engineering"])
A["prebuild-646da4"] = unsure("Could be a build step, Gitpod-style prebuilds or an open-source project-file generator; I cannot tell which is meant.")
A["precompile-54d76f"] = nas("A build-step verb, not a skill, tool or method on its own.")
A["precompiled-1fac7a"] = nas("An adjective for code that is already compiled, not a skill.")
A["predictionio-8d7180"] = new("Apache PredictionIO", "platform",
    "An open-source machine-learning server for building and serving predictive engines, developed as an Apache Software Foundation project.",
    variants=["PredictionIO"])
A["predictive-analytics-softwares-4c25a2"] = new("Predictive analytics software", "tool",
    "Software that applies statistical and machine-learning models to existing data to forecast future outcomes.")
A["predictive-modelling-970964"] = new("Predictive modelling", "method",
    "Building statistical or machine-learning models that use known data to predict future or unknown outcomes.",
    variants=["Predictive modeling"])
A["presentation-design-ab5780"] = new("Presentation design", "skill",
    "Designing slides and other visual presentation materials so that ideas are clear and engaging.")
A["presentation-programs-51d8b6"] = new("Presentation software", "tool",
    "Software for building and showing slide-based presentations, such as PowerPoint, Keynote and Google Slides.")
A["prestodb-aa90a3"] = new("PrestoDB", "tool",
    "The open-source distributed SQL query engine first developed at Facebook, now hosted by the Linux Foundation as Presto.")
A["preventative-dental-care-952fde"] = new("Preventive dental care", "skill",
    "Helping patients avoid tooth and gum disease through examinations, cleanings, fluoride, sealants and oral-hygiene teaching.")
A["prezi-e60fb9"] = new("Prezi", "tool",
    "A cloud-based presentation tool that lays content out on a large zoomable canvas instead of separate slides.")
A["primary-source-c2269d"] = nas("A kind of source material (an original document or record), not a skill.")
A["primavera-a37994"] = new("Oracle Primavera", "tool",
    "Oracle's family of project portfolio management software, best known for Primavera P6, used to plan and schedule large projects.")
A["primer-6df452"] = nas("A common word with several unrelated meanings (PCR primer, paint primer, introductory text), not a skill by itself.")
A["primerx-pharmacy-management-software-7c2c18"] = new("PrimeRx", "tool",
    "Pharmacy management software used to handle prescriptions, billing and inventory in a pharmacy.",
    rels=[("related", "jakzhha1se")])
A["principles-for-responsible-banking-prb-729bb7"] = new("Principles for Responsible Banking", "standard",
    "A voluntary framework launched in 2019 by the UN Environment Programme Finance Initiative for banks to align their strategy and business with the UN Sustainable Development Goals and the Paris Agreement.")
A["print-design-77dac7"] = new("Print design", "skill",
    "Designing layouts and artwork for printed materials such as brochures, posters and packaging.")
A["print-shops-837b63"] = nas("A type of business, not a skill.")

if __name__ == "__main__":
    write(A)
