from lib import *

A = {}
A["Workflow Management"] = N("Workflow management", "skill",
    "Defining, coordinating and monitoring the steps and handoffs through which work moves through an organization.",
    "A business-process skill.")
A["Workforce Optimisation"] = N("Workforce optimisation", "skill",
    "Matching staffing levels and schedules to expected demand, as in contact centres, so that a workforce is used efficiently.",
    "A workforce-planning skill.", variants=["Workforce optimization"])
A["Workforce Trends"] = N("Workforce trends", "knowledge",
    "Understanding how the size, make-up, skills and working patterns of an organization's or an industry's workers are changing over time.",
    "A labour-analysis topic.", rels=[("related", "nj7ggxlzyt")])
A["Workgroup"] = NS("A generic word, not a skill.")
A["Working With Children 0-5"] = N("Working with children aged 0-5", "skill",
    "Caring for and teaching babies, toddlers and young children from birth to five years old.",
    "An early-years care skill.")
A["Workplace Diversities"] = NS("A generic phrase, not a defined skill.")
A["Workplace Violence"] = NS("Names a hazard and not a skill.")
A["WorkPLAN"] = U("I cannot tell for certain which product or term WorkPLAN refers to.")
A["Workspace"] = NS("A generic word, not a skill.")
A["Workspace Macro"] = U("Nothing shows which application's macros are meant.")
A["Worship Ministry"] = N("Worship ministry", "knowledge",
    "The planning and leading of a church's public worship, including its music, liturgy and volunteer teams.",
    "A church ministry area.", rels=[("related", "b54kbh2h43"), ("related", "qatr9a0kcz")])
A["Wpf Controls"] = NS("User-interface elements of a framework, not a skill.")
A["Writing Outlines"] = N("Writing outlines", "skill",
    "Planning a piece of writing by listing its main points and their order before drafting it.",
    "A writing skill.")
A["Wsdl2java"] = N("WSDL2Java", "tool",
    "A command-line tool, found in Apache Axis and Apache CXF, that generates Java classes from a WSDL web-service description.",
    "A named code-generation tool.")
A["WXGTK (GTK+ Language Bindings)"] = N("wxGTK", "library",
    "The GTK port of the wxWidgets C++ toolkit, used to build cross-platform desktop applications.",
    "A named GUI toolkit port.",
    note="wxGTK is a GUI toolkit port and not a language, so the legacy language class is wrong.")
A["WxPerl"] = N("wxPerl", "library",
    "The Perl bindings for the wxWidgets GUI toolkit.",
    "A named GUI toolkit binding.")
A["WxPython"] = N("wxPython", "library",
    "The Python bindings for the wxWidgets GUI toolkit, used to build cross-platform desktop applications.",
    "A named GUI toolkit binding.")
A["Wyse Management Suite"] = N("Wyse Management Suite", "tool",
    "Dell's software for configuring, monitoring and updating Wyse thin clients and other edge devices.",
    "A named device-management product.")
A["X/PTR"] = U("I cannot tell what X/PTR refers to.")
A["X3D"] = N("X3D", "markup-language",
    "An ISO standard, XML-based format and language for describing interactive 3D scenes for the web, the successor to VRML.",
    "A named 3D scene-description language.", variants=["Extensible 3D"], lang="programming")
A["Xanadu"] = NS("A proper name (a poem's setting, a company, a hypertext project), not a skill.")
A["Xanthoproteic Reaction"] = N("Xanthoproteic reaction", "method",
    "A chemical test in which concentrated nitric acid turns proteins that contain aromatic amino acids yellow, used to detect such proteins.",
    "A named laboratory test.", variants=["Xanthoproteic test"], rels=[("broader", "fo93ho62h9")])
A["Xbox Live Vision"] = N("Xbox Live Vision", "tool",
    "A USB camera accessory for the Xbox 360 that adds video chat and image capture to games and Xbox Live.",
    "A named hardware product.")
A["Xcalibur"] = N("Xcalibur", "tool",
    "Thermo Fisher Scientific software for controlling mass spectrometers and processing their data.",
    "A named laboratory software product.")
A["Xhosa (Language)"] = N("Xhosa", "human-language",
    "A Bantu language spoken mainly in South Africa, where it is one of the official languages.",
    "A human language.", variants=["isiXhosa"], lang="human")
A["Xtradb"] = N("Percona XtraDB", "tool",
    "A storage engine for MySQL and MariaDB, made by Percona as an enhanced fork of InnoDB.",
    "A named database storage engine.")
A["Xtragrid"] = N("XtraGrid", "library",
    "The DevExpress data-grid control for Windows Forms applications.",
    "A named UI control library.", variants=["DevExpress XtraGrid"])
A["Xul"] = N("XUL", "markup-language",
    "An XML-based language from Mozilla for describing the user interface of applications such as Firefox.",
    "A named markup language.", variants=["XML User Interface Language"], rels=[("related", "php2tc9p7y")],
    lang="programming")
A["Yahoo! Messenger Protocols"] = N("Yahoo! Messenger protocols", "knowledge",
    "The proprietary network protocols that Yahoo! Messenger clients used to talk to Yahoo's servers.",
    "A narrow protocol topic.", rels=[("related", "llq5laptmx")])
A["YARA (Software)"] = N("YARA", "tool",
    "An open-source tool that identifies and classifies malware by matching files against rules that describe text or binary patterns.",
    "A named security tool.")
A["Yardi (Property Management Software)"] = N("Yardi", "tool",
    "Property management and real-estate accounting software from Yardi Systems.",
    "A named software product line.")
A["Yellow Dog Linux"] = N("Yellow Dog Linux", "platform",
    "A Linux distribution for PowerPC computers, made by Terra Soft Solutions.",
    "A named operating system.")
A["Yoruba (Language)"] = N("Yoruba", "human-language",
    "A Niger-Congo language spoken mainly in southwestern Nigeria and in Benin and Togo.",
    "A human language.", variants=["Yorùbá"], lang="human")
A["Youth Mentoring"] = N("Youth mentoring", "skill",
    "Guiding and supporting a young person over time as an adult mentor, for example with school, work and personal choices.",
    "A youth-work skill.")
A["Youth Ministry"] = N("Youth ministry", "knowledge",
    "The programmes, teaching and pastoral care a church provides for teenagers and young people.",
    "A church ministry area.", rels=[("related", "b54kbh2h43"), ("related", "qatr9a0kcz")])
A["Youtube Channels"] = NS("A generic phrase for accounts on a video site, not a skill.")
A["Yun OS"] = N("YunOS", "platform",
    "An operating system developed by Alibaba for smartphones and other connected devices.",
    "A named operating system.")
A["Z/OS"] = N("z/OS", "platform",
    "IBM's operating system for its z Systems mainframe computers.",
    "A named operating system.", variants=["IBM z/OS"])
A["Z-Wave Protocol"] = N("Z-Wave", "standard",
    "A low-power wireless protocol that smart-home devices such as sensors, locks and switches use to communicate.",
    "A named wireless protocol.")
A["Zemax"] = N("Zemax OpticStudio", "tool",
    "Software for designing and simulating optical systems such as lenses, from Zemax.",
    "A named optical design product.", variants=["OpticStudio"])
_zce = lambda: N("Zend Certified PHP Engineer", "credential",
    "A certification from Zend that shows a PHP developer has passed its exam.",
    "A certification awarded by one company.", variants=["ZCE"], cert=True, scope="single-issuer")
A["Zend Certified Engineer"] = _zce()
A["Zend PHP Certification"] = _zce()
A["Zenworks Asset Management"] = N("ZENworks Asset Management", "tool",
    "A ZENworks product, originally from Novell, for tracking an organization's software licences and hardware assets.",
    "A named IT asset management product.")
A["Zeroheight (Software)"] = N("zeroheight", "tool",
    "A web platform for documenting and sharing a design system so that designers and developers work from the same guidelines.",
    "A named design-system product.")
A["Zerto"] = N("Zerto", "tool",
    "Software for disaster recovery, backup and workload migration across virtual and cloud environments.",
    "A named data-protection product.")
A["Zetafax"] = N("Zetafax", "tool",
    "Server software for sending and receiving faxes from desktops and applications across a network.",
    "A named fax server product.")
A["Zettabyte File System"] = N("ZFS", "tool",
    "A file system and volume manager, first developed at Sun Microsystems, that combines storage pooling, snapshots and data checksums.",
    "A named file system.")
A["Zinnia"] = U("Could be the flower, a company or a handwriting-recognition library; nothing shows which is meant.")
A["Zolpidem"] = NS("A drug, not a skill.")
A["Zorba"] = U("I think this may be an XQuery processor, but the name is shared with other things and I am not sure.")
