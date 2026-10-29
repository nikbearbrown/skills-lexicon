from common import *
A = {}
A["Sign In Enterprise (Software)"] = unsure("May be a visitor-management product, but I cannot confirm what it is.")
A["Signaling (Crane Rigging)"] = new("Crane signaling", "skill",
    "Guiding a crane operator during a lift with standard hand signals or radio calls.",
    variants=["Crane signalling"])
A["Signalling Connection Control Part (SCCP)"] = new("Signalling Connection Control Part", "standard",
    "A layer of the SS7 telephone signalling protocol stack that adds addressing and connection-oriented and connectionless services on top of the message transfer part.")
SS7 = dict(name="Signalling System No. 7", kind="standard",
    definition="A set of ITU-T telephone signalling protocols used to set up and route calls and provide services across public telephone networks.",
    variants=["SS7", "Signalling System 7", "Signaling System 7"])
A["Signalling System 7 (SS7)"] = new(SS7["name"], SS7["kind"], SS7["definition"], variants=SS7["variants"])
A["Signalling System No. 7"] = new(SS7["name"], SS7["kind"], SS7["definition"], variants=SS7["variants"])
A["Signalling Systems"] = unsure("Could mean telephone, railway or other signalling; the name alone does not say which.")
A["Sil-Lum (Shaolin) Kung Fu"] = new("Shaolin kung fu", "skill",
    "A family of Chinese martial arts associated with the Shaolin Temple; Sil Lum is the Cantonese rendering of Shaolin.",
    variants=["Sil Lum kung fu"])
A["Silesian (Language)"] = new("Silesian", "human-language",
    "A West Slavic language spoken in Upper Silesia, mainly in southern Poland.",
    lang="human")
A["SilkTesting"] = new("Silk Test", "tool",
    "A tool for automating functional and regression tests of software applications, originally developed by Segue Software.",
    variants=["SilkTest"], relations=[R("related", "ss273uzint")])
A["Simple Form"] = unsure("Could be the Rails simple_form gem or a plain description of a form; no context.")
A["Simple Interrupted Stitch"] = new("Simple interrupted suture", "skill",
    "A basic suturing technique in which each stitch is placed and knotted separately to close a wound.",
    variants=["Simple interrupted stitch"])
A["Simple Mail Transfer Protocols"] = new("Simple Mail Transfer Protocol", "standard",
    "The internet protocol used to send email from mail clients to servers and between mail servers.",
    variants=["SMTP"])
A["Simple Public-Key Infrastructure"] = new("Simple Public Key Infrastructure", "standard",
    "An IETF proposal for authorisation certificates that bind permissions to public keys instead of names, described in RFC 2693.",
    variants=["SPKI"])
A["SimpleLegal (Legal Operations Software)"] = new("SimpleLegal", "platform",
    "Software for corporate legal departments to manage matters, outside counsel invoices and legal spend.")
A["Simplex"] = unsure("Could mean the simplex method, simplex communication, a company or a geometric shape; no context.")
A["Simplified Disaster Recovery"] = unsure("Not a standard term; I cannot tell if it names a method, a product or a loose phrase.")
A["Simputer"] = new("Simputer", "tool",
    "A low-cost handheld computer designed in India in the early 2000s for people with little access to computers, using icons and speech output.")
A["Simultaneous Engineering Wikipedia"] = new("Concurrent engineering", "method",
    "An approach in which design, manufacturing and other product-development stages are carried out in parallel instead of one after another.",
    variants=["Simultaneous engineering"])
A["Single In-Line Memory Module (SIMM)"] = new("Single In-Line Memory Module", "tool",
    "An older type of computer memory module with contacts on both sides of one edge that are electrically the same.",
    variants=["SIMM"])
A["Single Nucleotide Polymorphism Database[1] (DbSNP)"] = new("dbSNP", "platform",
    "A public database run by the US National Center for Biotechnology Information that catalogues single nucleotide polymorphisms and other short genetic variations.",
    variants=["Single Nucleotide Polymorphism Database"])
A["Single Sign-On"] = new("Single sign-on", "method",
    "An authentication approach that lets a user sign in once to reach several separate applications.",
    variants=["SSO"])
A["Site Reliability Engineering"] = new("Site reliability engineering", "skill",
    "Applying software engineering to running large systems so that they stay reliable, scalable and efficient.",
    variants=["SRE"], relations=[R("related", "qmravcc671")])
A["Six Sigma Black Belt Certification"] = new("Six Sigma Black Belt", "credential",
    "A certification for people who lead Six Sigma process-improvement projects, higher than the Green Belt.",
    cert=True, scope="many-issuers")
A["Six Sigma Green Belt Certification"] = new("Six Sigma Green Belt", "credential",
    "A certification for people who take part in or lead smaller Six Sigma process-improvement projects, below the Black Belt.",
    cert=True, scope="many-issuers")
A["Skill"] = na("A generic word, not a particular skill.")
A["Skinning"] = unsure("Could mean animal skinning, 3D character skinning or interface skinning; no context.")
A["Skiptrace"] = new("Skip tracing", "skill",
    "Locating a person who has moved or disappeared, such as a debtor, by searching records and databases.",
    variants=["Skip trace"])
A["Slam Life Assessment Method (Engineering Test)"] = unsure("I do not recognise this method.")
A["Sluce Gates"] = new("Sluice gate", "tool",
    "A movable barrier that controls the flow of water in a channel, dam or canal.",
    variants=["Sluice gates"])
A["Sluice"] = unsure("Could mean a sluice gate, a water channel or a gold-mining sluice box.")
A["Slurm"] = new("Slurm Workload Manager", "tool",
    "An open-source job scheduler and resource manager for Linux computing clusters.",
    verbs=["administer"])
A["Smart Buildings"] = new("Smart buildings", "knowledge",
    "Buildings that use networked sensors, controls and software to automate and tune systems such as heating, lighting, security and energy use.")
A["Smart Lighting"] = new("Smart lighting", "knowledge",
    "Lighting that can be controlled automatically or remotely, for example by sensors, schedules or an app.")
A["Smart Meter Systems"] = new("Smart meter systems", "knowledge",
    "Electronic utility meters and the communications and software that send a customer's usage readings to the supplier.",
    relations=[R("related", "i5gs33auro")])
A["Smart Pigs"] = new("Smart pig", "tool",
    "An instrumented device sent through a pipeline to inspect it for corrosion, cracks and dents.")
A["SmartBidNet"] = new("SmartBidNet", "platform",
    "Online software for construction companies to invite subcontractors to bid and to manage bid documents and responses.")
A["Smartbook"] = unsure("Could be an adaptive learning product or a type of laptop; no context.")
A["Smartphone Operation"] = new("Smartphone operation", "skill",
    "Using a smartphone's apps, settings and features for tasks such as calls, messaging and navigation.")
A["Smartstream (Software)"] = unsure("The name could refer to a financial-software vendor or to other products; I cannot confirm which.")
A["SmartTest"] = unsure("I cannot tell which product this names; several tools use the name.")
A["Smds"] = unsure("Ambiguous acronym; it could be a telecom data service or something else.")
A["Smoothing"] = unsure("Used in statistics, sanding, graphics and cosmetics with different meanings; no context.")
A["Snort (Intrusion Detection System)"] = new("Snort", "tool",
    "An open-source network intrusion detection and prevention system that inspects traffic against rules.",
    relations=[R("broader", "uuer0jxuof")])
A["Snow (Software)"] = new("Snow Software", "platform",
    "A software asset management platform, from the company Snow Software, for tracking software licences and usage.")
A["Snowplow"] = unsure("Could be the Snowplow event-data platform or the snow-clearing vehicle; no context.")
A["Snubbing"] = new("Hydraulic snubbing", "method",
    "An oil-well service technique in which a hydraulic unit pushes pipe into, or pulls it out of, a well that is under pressure.")
A["Social and Behavior Change Communication"] = new("Social and behavior change communication", "method",
    "A public-health communication approach that uses strategic messaging and community engagement to change both individual behaviours and the social norms around them.",
    variants=["SBCC", "Social and behaviour change communication"],
    relations=[R("related", "jctieiwib0")])
A["Social Determinants Of Health"] = new("Social determinants of health", "knowledge",
    "The non-medical conditions in which people live and work, such as income, housing and education, that shape their health.",
    variants=["SDOH"])
A["Social-Emotional Learning"] = new("Social-emotional learning", "method",
    "An educational approach that teaches skills such as self-awareness, self-management, empathy, relationship skills and responsible decision-making.",
    variants=["SEL", "Social and emotional learning"])
A["Social Impact Bond"] = new("Social impact bond", "knowledge",
    "A pay-for-success contract in which private investors fund a social programme and are repaid by government only if agreed outcomes are met.")

if __name__ == "__main__":
    write(slice_terms(100, 150), A)
