import sys
sys.path.insert(0, "work/scripts")
from lib import *

A = {}

A["omt-ef8e43"] = unsure(
    "OMT is a bare acronym with several possible meanings and nothing here says which.")

A["on1-software-db3e41"] = new(
    "ON1 is a named photo software product line.",
    "ON1", "tool",
    "Photo editing and organising software made by ON1, Inc., including ON1 Photo RAW.")

A["onboarding-8d49e0"] = new(
    "Onboarding is a recognised HR and customer-success activity.",
    "Onboarding", "skill",
    "Guiding new employees or new customers through their first stage of joining so they can work or use a product effectively.")

A["onclick-760c1f"] = nas(
    "An HTML and JavaScript event attribute, a feature of code rather than a skill.")

A["oncogenomics-141001"] = new(
    "Oncogenomics is an established research field.",
    "Oncogenomics", "knowledge",
    "The study of the genetic and genomic changes behind cancer and how they can guide diagnosis and treatment.")

A["oncology-certified-nurse-4f789f"] = new(
    "OCN is a named nursing certification, distinct from the advanced oncology certifications nearby.",
    "Oncology Certified Nurse", "credential",
    "A certification for registered nurses who care for people with cancer, awarded by the Oncology Nursing Certification Corporation.",
    variants=["OCN"], cert=True, scope="single-issuer")

A["oncology-sales-0b3fa4"] = new(
    "Selling oncology products is a recognised sales specialty.",
    "Oncology sales", "skill",
    "Selling cancer drugs, devices or diagnostics to oncologists, hospitals and other cancer care providers.")

A["onetrust-software-a2ac51"] = new(
    "OneTrust is a named privacy and compliance platform.",
    "OneTrust", "platform",
    "A software platform for privacy, data governance, third-party risk and compliance management.")

A["online-communication-between-school-and--aa3402"] = unsure(
    "Reads like a duty description rather than a named skill, so a person should decide.")

A["online-demostration-ae224d"] = new(
    "Online demonstration is a recognised sales and teaching skill; the tag misspells it.",
    "Online demonstration", "skill",
    "Showing a product, process or technique to an audience remotely, using screen sharing or video.")

A["online-focus-74b4e3"] = unsure(
    "The term is too vague to say whether it names a skill, such as online focus groups.")

A["online-marketing-dbaabc"] = variant(
    "dv5vi280tf",
    "Online marketing and e-marketing both mean promoting products through internet channels.")

A["online-pharmacy-57ebd0"] = nas(
    "A type of business, not a skill.")

A["online-writing-lab-08e36c"] = nas(
    "A service or website, not a skill.")

A["onshape-3d-modeling-software-fe0f24"] = new(
    "Onshape is a named cloud CAD product, an instance of 3D modeling software.",
    "Onshape", "tool",
    "A cloud-based computer-aided design system for 3D product modelling that runs in a web browser and is owned by PTC.",
    relations=[R("broader", "xaw12yw4wk")])

A["open-banking-58656b"] = new(
    "Open banking is a defined financial technology and regulatory concept.",
    "Open banking", "knowledge",
    "A system in which banks let authorised third parties access customer account data and payment services through secure APIs, with the customer's consent.")

A["open-network-computing-1a316a"] = new(
    "Open Network Computing is Sun Microsystems' set of network computing technologies.",
    "Open Network Computing", "knowledge",
    "A set of distributed computing technologies from Sun Microsystems, including ONC RPC and the Network File System.")

A["open-shortest-path-first-9edff5"] = new(
    "OSPF is a named routing protocol.",
    "Open Shortest Path First", "standard",
    "A link-state routing protocol for IP networks that finds shortest paths using Dijkstra's algorithm.",
    variants=["OSPF"])

A["open-water-b87946"] = unsure(
    "Could mean open-water swimming or diving, or a diver certification, and nothing here says which.")

A["open-web-application-security-2d6aa5"] = unsure(
    "Looks like a truncated OWASP name, and it is unclear whether it means the organisation, its guidance or web application security in general.")

A["openapi-8cfc01"] = new(
    "Openapi is the OpenAPI Specification (same concept as the next tag, answered under one name).",
    "OpenAPI Specification", "standard",
    "A language-agnostic specification for describing HTTP APIs in a machine-readable YAML or JSON format, formerly known as Swagger.",
    variants=["OpenAPI"], relations=[R("related", "xe2d2jfa1r")])

A["openapi-specification-7fb5b7"] = new(
    "OpenAPI Specification is the named standard for describing HTTP APIs.",
    "OpenAPI Specification", "standard",
    "A language-agnostic specification for describing HTTP APIs in a machine-readable YAML or JSON format, formerly known as Swagger.",
    variants=["OpenAPI"])

A["opencart-5a5546"] = new(
    "OpenCart is a named e-commerce platform.",
    "OpenCart", "platform",
    "An open-source PHP e-commerce platform for running online stores.")

A["opendaylight-36f442"] = new(
    "OpenDaylight is a named software-defined networking platform.",
    "OpenDaylight", "platform",
    "An open-source software-defined networking platform, hosted by the Linux Foundation, built around a network controller.")

A["openni-eefc9a"] = new(
    "OpenNI is a named framework for depth-sensing devices.",
    "OpenNI", "framework",
    "An open-source software framework for working with depth-sensing cameras and natural-interaction devices, such as the Microsoft Kinect.")

A["opennlp-126fa5"] = new(
    "Apache OpenNLP is a named natural language processing library.",
    "Apache OpenNLP", "library",
    "An Apache open-source machine-learning library for natural language processing tasks such as tokenisation, part-of-speech tagging and named-entity recognition.",
    variants=["OpenNLP"], relations=[R("related", "d168utcmjy")])

A["openstreetmap-fa78a3"] = new(
    "OpenStreetMap is a named mapping project and data source.",
    "OpenStreetMap", "platform",
    "A collaborative project that builds a free, editable map database of the world.")

A["opentok-0cf8ee"] = new(
    "OpenTok is a named video platform.",
    "OpenTok", "platform",
    "A WebRTC-based platform and API, originally from TokBox and now part of Vonage, for adding live video to web and mobile apps.")

A["opentsdb-9af9e1"] = new(
    "OpenTSDB is a named time series database.",
    "OpenTSDB", "platform",
    "A scalable, open-source time series database built to run on Apache HBase.")

A["operating-point-ec1722"] = unsure(
    "A technical term with different meanings in electronics, control and other fields, and nothing here says which.")

A["operating-theater-886954"] = nas(
    "A type of place, not a skill.")

A["operation-centers-c9cfe2"] = nas(
    "A type of place, not a skill.")

A["operational-risk-mitigation-ce73ce"] = new(
    "Mitigating operational risk is a recognised risk management skill.",
    "Operational risk mitigation", "skill",
    "Planning and applying controls to reduce the risk of loss from failed processes, people, systems or external events.")

A["operationalizing-ai-6670e8"] = new(
    "Operationalizing AI is a recognised practice of putting AI into production.",
    "Operationalizing AI", "skill",
    "Moving AI models from prototypes into reliable production use, including deployment, monitoring and integration into business processes.")

A["operations-administration-maintenance-an-3ae7e8"] = new(
    "OAM&P is a standard telecommunications term.",
    "Operations, administration, maintenance and provisioning", "knowledge",
    "The set of functions needed to run a telecommunications network: operating it, administering it, maintaining it and provisioning services on it.",
    variants=["OAM&P", "OAMP"])

A["operations-administration-maintenance-sa-b145d2"] = new(
    "Same concept as the previous OAMP tag (with a typo), answered under the identical name.",
    "Operations, administration, maintenance and provisioning", "knowledge",
    "The set of functions needed to run a telecommunications network: operating it, administering it, maintaining it and provisioning services on it.",
    variants=["OAM&P", "OAMP"])

A["operations-analytics-d97030"] = new(
    "Operations analytics is a recognised analytics specialty.",
    "Operations analytics", "skill",
    "Using data analysis to measure and improve how an organisation's operations, such as supply chains, production or service delivery, perform.")

A["ophthalmic-surgical-assisting-6829a6"] = new(
    "Names the work of assisting in eye surgery rather than a credential.",
    "Ophthalmic surgical assisting", "skill",
    "Assisting an ophthalmic surgeon during eye surgery by preparing the patient, handling instruments and supporting the procedure.",
    relations=[R("related", "v7d85yap3i")],
    note="The tag names the activity of assisting in eye surgery; a credential for it would be a separate concept.")

A["opsworks-6d7b98"] = new(
    "OpsWorks is a named AWS service.",
    "AWS OpsWorks", "tool",
    "An Amazon Web Services configuration management service that uses Chef and Puppet to automate how servers are configured and deployed.",
    variants=["OpsWorks"])

A["optical-fiber-0940d7"] = new(
    "Optical fibre is a basic telecommunications and photonics topic.",
    "Optical fiber", "knowledge",
    "Thin strands of glass or plastic that carry data as pulses of light.",
    variants=["Optical fibre"])

A["optical-fiber-cable-f28d40"] = new(
    "Optical fibre cable is a basic telecommunications topic.",
    "Optical fiber cable", "knowledge",
    "A cable that holds one or more optical fibers inside protective layers for carrying data as light.",
    variants=["Optical fibre cable", "Fiber optic cable"])

A["optical-power-meters-18098b"] = new(
    "An optical power meter is a standard fibre-testing instrument.",
    "Optical power meter", "tool",
    "An instrument that measures the power of an optical signal, used to test fibre-optic links.")

A["optical-waveguides-1b4491"] = new(
    "Optical waveguides are a photonics topic.",
    "Optical waveguides", "knowledge",
    "Structures that guide light along a path, such as optical fibres and channels on a photonic chip.",
    variants=["Optical waveguide"])

A["optimization-softwares-570740"] = new(
    "A category of software, treated like other software categories in the dictionary.",
    "Optimization software", "tool",
    "Software that finds the best values of decision variables under given constraints, for example by linear or integer programming.")

A["optitex-fashion-design-software-6948d7"] = new(
    "Optitex is a named fashion CAD product, comparable to the nearby Browzwear.",
    "Optitex", "tool",
    "Computer-aided design software for 2D pattern making and 3D garment simulation in fashion and apparel.",
    relations=[R("related", "eakf49x3b5")])

A["oracle-8a1681"] = unsure(
    "Oracle names a company and many products (database, ERP, cloud) and nothing here says which is meant.")

A["oracle-application-frameworks-oaf-d36b5d"] = new(
    "Oracle Application Framework is a named Oracle E-Business Suite development framework.",
    "Oracle Application Framework", "framework",
    "Oracle's Java-based framework for building and customising the web user interfaces of Oracle E-Business Suite applications.",
    variants=["OAF"])

A["osha-safety-certificates-9da050"] = new(
    "Treated as the safety training cards and certificates issued under OSHA's Outreach Training Program.",
    "OSHA safety certificate", "credential",
    "A card or certificate showing completion of occupational safety training under the United States Occupational Safety and Health Administration, such as its 10-hour and 30-hour Outreach courses.",
    variants=["OSHA safety certificates", "OSHA certificate"], cert=True, scope="single-issuer")

A["ovd-8f94f8"] = unsure(
    "OVD is a bare acronym with several possible meanings and nothing here says which.")

if __name__ == "__main__":
    write(A)
