from lib_answers import *

A = {}
A["progressive-care-certified-nurse-728841"] = new("Progressive Care Certified Nurse", "credential",
    "A nursing certification from the AACN Certification Corporation for nurses who care for acutely ill adult patients in progressive care settings.",
    variants=["PCCN"], cert=True, scope="single-issuer")
A["project-management-associate-certificati-4c9436"] = unsure("Could mean IPMA Level D, PMI's CAPM or another entry-level credential; I cannot tell which one is meant.")
A["project-management-certification-854f21"] = new("Project management certification", "credential",
    "Any professional credential that attests to a person's project-management knowledge or skill, such as the PMP or PRINCE2 certifications.",
    rels=[("related", "z83cabeb9c")], cert=True, scope="many-issuers")
A["project-management-institute-1b83c0"] = nas("An organisation (PMI), not a skill.")
A["project-management-office-0d7a26"] = nas("An organisational unit, not a skill.")
A["project-management-support-certificates-0b733b"] = unsure("Unclear which certificates are meant; it could be any project-management or project-support certificate.")
A["project-resources-169209"] = nas("A generic phrase for the people, money and materials of a project, not a skill.")
A["project-scoping-5f7978"] = new("Project scoping", "skill",
    "Defining what a project will and will not deliver, including its goals, deliverables, boundaries and constraints.",
    rels=[("part_of", "z83cabeb9c")])
A["project-stakeholder-e4451d"] = nas("A role (a person or group with an interest in a project), not a skill.")
A["project-status-reports-a4d845"] = new("Project status reporting", "skill",
    "Summarising a project's progress, risks and next steps for stakeholders in regular reports.")
A["project-zero-e73a81"] = nas("A project or team name (such as Google Project Zero), not a skill.")
A["prolog-ba4d6e"] = new("Prolog", "programming-language",
    "A logic programming language in which programs are written as facts and rules and run by answering queries.",
    lang="programming")
A["prometheus-b39947"] = new("Prometheus", "tool",
    "An open-source monitoring system that collects time-series metrics and supports querying and alerting, hosted by the Cloud Native Computing Foundation.")
A["proofreading-df621a"] = new("Proofreading", "skill",
    "Reading written text to find and correct errors in spelling, grammar, punctuation and formatting before it is published.")
A["property-administrator-certification-5ad840"] = unsure("Could be a real-property or a government-property administrator credential from different bodies; I cannot tell which.")
A["property-information-ca8911"] = nas("A generic phrase for data about property, not a skill.")
A["prophylaxis-ca0805"] = unsure("The meaning depends on the field (preventive medicine, dental cleaning), so I cannot tell what skill is meant.")
A["proportion-f545d6"] = nas("A general word with many meanings (ratio, design principle), not a skill by itself.")
A["proposal-business-a719f2"] = nas("A kind of document, not a skill; the skills are proposal writing and management.")
A["proposal-development-3ed128"] = new("Proposal development", "skill",
    "Writing and assembling proposals to win contracts, grants or business, from first outline to final submission.")
A["proposal-management-ed5bc2"] = new("Proposal management", "skill",
    "Planning, organising and overseeing the team, schedule and reviews that produce a bid or proposal.")
A["proposal-strategy-b6a5e2"] = new("Proposal strategy", "skill",
    "Deciding the approach, win themes and positioning that a bid or proposal will use to persuade the buyer.")
A["prosecutor-s-management-information-syst-289dc3"] = new("Prosecutor's management information system", "tool",
    "Software that a prosecutor's office uses to manage its caseload, such as cases, defendants, hearings and outcomes.")
A["prosthetic-devices-7a2cfe"] = new("Prosthetic devices", "knowledge",
    "Artificial replacements for missing body parts, such as limbs, and how they are fitted and maintained.",
    rels=[("broader", "i7hneu52i6")])
A["protein-characterization-84a1a7"] = new("Protein characterization", "skill",
    "Working out a protein's identity, size, structure, purity and properties with methods such as electrophoresis and mass spectrometry.")
A["protein-protein-interaction-d0eb26"] = new("Protein-protein interaction", "knowledge",
    "The physical contacts between proteins that carry out biological functions, and the methods used to detect and study them.")
A["protein-structure-prediction-631e7f"] = new("Protein structure prediction", "method",
    "Predicting a protein's three-dimensional shape from its amino-acid sequence, for example with AlphaFold.")
A["protocol-oriented-programming-f671dd"] = new("Protocol-oriented programming", "method",
    "A programming approach, popularised by Swift, that builds behaviour from protocols and their extensions instead of from class inheritance.",
    rels=[("contrast", "i0vpvmxbz0")])
A["prototype-js-284ded"] = new("Prototype JavaScript Framework", "framework",
    "A JavaScript framework that extends the browser's built-in objects with helpers for working with the page, Ajax requests and class-like inheritance.",
    variants=["Prototype.js", "Prototypejs"])
A["prototypejs-be2716"] = new("Prototype JavaScript Framework", "framework",
    "A JavaScript framework that extends the browser's built-in objects with helpers for working with the page, Ajax requests and class-like inheritance.",
    variants=["Prototype.js", "Prototypejs"],
    reason="Same framework as the Prototype.js tag, so answered with the same name.")
A["protractor-c2dfdb"] = new("Protractor", "framework",
    "An end-to-end test framework for Angular and AngularJS web apps that drives a real browser through Selenium WebDriver.")
A["provisioning-tools-04973e"] = unsure("A generic category that could mean infrastructure provisioning or user-account provisioning tools; I cannot tell which.")
A["psychiatric-mental-health-nurse-practiti-b64b0a"] = new("Psychiatric-Mental Health Nurse Practitioner", "credential",
    "A nurse practitioner credential for providing psychiatric and mental health care to patients across the lifespan.",
    variants=["PMHNP"], cert=True, scope="many-issuers")
A["psycholocial-counseling-f41ac4"] = unsure("A misspelling that could mean psychological or psychosocial counselling, and I cannot tell which.")
A["psychosocial-66867e"] = nas("An adjective, not a skill by itself.")
A["public-history-c4714c"] = new("Public history", "knowledge",
    "The practice of presenting history to general audiences, in places such as museums, archives, historic sites and the media.")
A["public-key-cryptography-64aece"] = new("Public-key cryptography", "knowledge",
    "Cryptography in which each user has a public key that anyone can use to encrypt or verify and a private key kept secret to decrypt or sign.",
    variants=["Public key cryptography", "Asymmetric cryptography"])
A["public-key-cryptography-standards-pkcs-35ebdf"] = new("Public-Key Cryptography Standards", "standard",
    "A set of numbered specifications, first published by RSA Laboratories, that define formats and interfaces for public-key cryptography, such as PKCS #1 for RSA.",
    variants=["PKCS"])
A["public-policies-2c3f7f"] = new("Public policy", "knowledge",
    "The laws, rules and government actions that address public problems, and the study of how they are made and what effects they have.")
A["pugjs-f0ec45"] = new("Pug", "library",
    "A template engine for Node.js and browsers that compiles indentation-based templates into HTML.",
    variants=["Pug.js"])
A["pulses-6fad12"] = nas("A general word (legumes, electrical pulses) with no skill meaning by itself.")
A["pumps-95f918"] = nas("Names a type of equipment, not a skill.")
A["punctuation-68fc7b"] = new("Punctuation", "skill",
    "Using punctuation marks correctly so that written text is clear.")
A["puphpet-ecef85"] = new("PuPHPet", "tool",
    "A web-based tool that generates Vagrant and Puppet configuration for setting up PHP development environments.",
    rels=[("related", "n9dorj1s29")])
A["puppet-configuration-management-tool-e79346"] = new("Puppet", "tool",
    "A configuration-management tool in which the desired state of servers is described in a declarative language and then enforced automatically.")
A["puppeteer-8b962c"] = new("Puppeteer", "library",
    "A Node.js library from the Chrome team that controls Chrome or Chromium through code, often for browser testing and automation.")
A["purifed-protein-derivative-ppd-6abcb3"] = nas("Names a substance used in the tuberculin skin test, not a skill.")
A["putty-88d402"] = new("PuTTY", "tool",
    "A free terminal program, first made for Windows, that connects to remote machines over SSH, Telnet and serial lines.")
A["pymongo-dbc83b"] = new("PyMongo", "library",
    "The official Python driver for working with MongoDB databases.",
    rels=[("related", "pk7cebmtg6")])
A["pytables-e9dbd6"] = new("PyTables", "library",
    "A Python library for managing large hierarchical datasets, built on the HDF5 file format and NumPy.")

if __name__ == "__main__":
    write(A)
