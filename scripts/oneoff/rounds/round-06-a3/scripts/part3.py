import sys
sys.path.insert(0, "/home/user/rounds/round-06/a3/skills-lexicon/work/scripts")
from h import *

N("microsoft-certified-azure-solutions-arch-2d502d", "Microsoft Certified: Azure Solutions Architect Expert", "credential",
  "A Microsoft certification for architects who design cloud and hybrid solutions on Azure, covering compute, storage, networking and security.",
  cert=True, scope="single-issuer",
  reason="The tag is an older or shortened name for Microsoft's Azure Solutions Architect certification.")

N("microsoft-certified-systems-administrato-877786", "Microsoft Certified Systems Administrator", "credential",
  "A Microsoft certification for professionals who manage Windows server environments and networks.",
  cert=True, scope="single-issuer")

N("microsoft-cognitive-services-6ce83f", "Azure Cognitive Services", "platform",
  "A set of Microsoft cloud APIs for adding vision, speech, language and decision-making features to applications.",
  variants=["Azure AI services"])

N("microsoft-digital-image-suite-e3e5d8", "Microsoft Digital Image Suite", "tool",
  "Microsoft consumer software for editing, organising and sharing digital photos.")

U("microsoft-digital-images-c7b01d", "It is not clear whether it means Microsoft Digital Image Suite or Pro software or something else.")

U("microsoft-digital-imaging-da1a94", "It is not clear whether it names a Microsoft product or the general field of digital imaging.")

N("microsoft-dynamics-365-field-service-828f4c", "Dynamics 365 Field Service", "tool",
  "A Microsoft Dynamics 365 application for scheduling and dispatching technicians and managing field work orders.",
  variants=["Microsoft Dynamics 365 Field Service"])

N("microsoft-dynamics-365-field-service-cer-1964a5", "Microsoft Dynamics 365 Field Service certification", "credential",
  "A Microsoft certification that shows skill in configuring and implementing Dynamics 365 Field Service.",
  cert=True, scope="single-issuer")

N("microsoft-flow-ec2df4", "Power Automate", "tool",
  "Microsoft's cloud service for building automated workflows between apps and services, first released as Microsoft Flow.",
  variants=["Microsoft Power Automate"])

N("microsoft-forms-752a5a", "Microsoft Forms", "tool",
  "A Microsoft 365 app for creating surveys, quizzes and polls and collecting the responses.")

N("microsoft-groupme-38293e", "GroupMe", "tool",
  "A group text-messaging app owned by Microsoft.",
  variants=["Microsoft GroupMe"])

N("microsoft-language-interface-pack-6ad001", "Microsoft Language Interface Pack", "tool",
  "A downloadable Microsoft add-on that translates much of the Windows or Office interface into another language.",
  note="The legacy class says Language, but this is a software translation pack, not a language.")

N("microsoft-lists-502a37", "Microsoft Lists", "tool",
  "A Microsoft 365 app for tracking information and work in customisable lists.")

N("microsoft-lync-232698", "Microsoft Lync", "tool",
  "Microsoft's business instant-messaging, presence and conferencing software, later renamed Skype for Business.")

U("microsoft-mail-387adb", "It could mean the early LAN-based Microsoft Mail system or a general Microsoft email product, and nothing here says which.")

U("microsoft-office-password-protection-de0058", "It names a single Office feature and it is unclear whether it counts as a distinct skill.")

N("microsoft-paint-cda342", "Microsoft Paint", "tool",
  "A basic raster graphics editor included with Windows.",
  variants=["MS Paint"])

N("microsoft-power-fx-7d6406", "Power Fx", "programming-language",
  "A low-code formula language from Microsoft, modelled on Excel formulas, used in Power Apps and the Power Platform.",
  variants=["Microsoft Power Fx"], lang="programming")

NS("microsoft-softwares-7426d5", "It is a generic phrase for Microsoft software, not one skill or product.")

N("microsoft-teams-live-events-c0f627", "Microsoft Teams live events", "tool",
  "A Microsoft Teams feature for broadcasting meetings and presentations to large online audiences.")

N("microsoft-teams-voice-d2e4bd", "Microsoft Teams Phone", "tool",
  "The calling features of Microsoft Teams, which let users place and receive phone calls through Teams.",
  reason="Teams Voice appears to be the common name for the Teams telephony features, which Microsoft calls Teams Phone.")

N("microsoft-transaction-server-9fd4e1", "Microsoft Transaction Server", "platform",
  "A Microsoft runtime from the 1990s for running and managing transactions and components in Windows server applications, later merged into COM+.")

N("microsoft-visio-f8f699", "Microsoft Visio", "tool",
  "A Microsoft application for drawing diagrams such as flowcharts, floor plans and network maps.",
  variants=["Visio"])

N("microsoft-windows-10-b19e14", "Windows 10", "platform",
  "The Microsoft operating system for personal computers released in 2015.",
  variants=["Microsoft Windows 10"])

N("microsoft-windows-7-287f2e", "Windows 7", "platform",
  "The Microsoft operating system for personal computers released in 2009.",
  variants=["Microsoft Windows 7"])

N("microsoft-windows-8-2e566b", "Windows 8", "platform",
  "The Microsoft operating system for personal computers released in 2012, known for its tile-based Start screen.",
  variants=["Microsoft Windows 8"])

N("microsoft-works-37d1c0", "Microsoft Works", "tool",
  "A low-cost Microsoft productivity suite that combined a word processor, spreadsheet and database.")

N("microstation-201103", "MicroStation", "tool",
  "A computer-aided design application from Bentley Systems for 2D and 3D design and drafting, used mainly in infrastructure and architecture.")

N("microstrategy-desktops-3d0669", "MicroStrategy Desktop", "tool",
  "The desktop application of MicroStrategy's business intelligence software, used to build reports and dashboards.")

N("microstrategy-intelligence-servers-6a476e", "MicroStrategy Intelligence Server", "platform",
  "The server component of MicroStrategy's business intelligence software that runs queries, caches results and serves reports to users.")

N("microstrategy-metrics-b606ca", "MicroStrategy metrics", "knowledge",
  "In MicroStrategy, the objects that define business calculations, such as total revenue, which reports and dashboards display.")

U("microstrategy-object-management-514e79", "It may mean the MicroStrategy Object Manager tool or the general practice of managing MicroStrategy objects, and nothing here says which.")

N("microstrategy-office-1e6dc5", "MicroStrategy Office", "tool",
  "A MicroStrategy add-in that lets users run and analyse MicroStrategy reports inside Microsoft Excel, PowerPoint and Word.")

N("microstrategy-olap-services-f97acb", "MicroStrategy OLAP Services", "tool",
  "A MicroStrategy extension that lets users slice and filter report results held in memory without re-querying the database.")

N("microstrategy-report-services-b0c452", "MicroStrategy Report Services", "tool",
  "A MicroStrategy component for building formatted, multi-section documents and dashboards from several reports.")

U("microstrategy-reporting-suite-6b3b97", "I cannot tell which MicroStrategy product bundle, if any, this names.")

N("microstrategy-software-development-kit-3e571d", "MicroStrategy Software Development Kit", "tool",
  "A set of programming interfaces and tools for customising and extending MicroStrategy applications.",
  variants=["MicroStrategy SDK"])

N("microstrategy-transaction-services-eecb92", "MicroStrategy Transaction Services", "tool",
  "A MicroStrategy feature that lets users write data back to a database from reports and documents.")

N("microstrategy-visual-insight-8b9edd", "MicroStrategy Visual Insight", "tool",
  "A MicroStrategy interface for building interactive data visualisations and dashboards.")

N("microstrategy-web-c27ef0", "MicroStrategy Web", "tool",
  "The web interface of MicroStrategy's business intelligence software, used to run reports and build dashboards in a browser.")

NS("migraine-16f386", "It names a medical condition, not a skill.")

NS("milestones-e7bdef", "It is a generic word, not a skill.")

NS("military-aid-f7a8de", "It is a generic phrase for assistance, not a skill.")

U("military-medication-68368e", "It is unclear whether it means military medicine or handling medication in a military setting.")

NS("military-services-4e7253", "It is a generic phrase for armed forces branches, not a skill.")

N("military-standards-and-specifications-964858", "Military standards and specifications", "standard",
  "US Department of Defense documents, such as MIL-STD and MIL-SPEC, that set technical, quality and process requirements for defence products.")

NS("military-trainings-117ebe", "It is a generic phrase for training in the armed forces, not one skill.")

N("mill-test-report-85e27e", "Mill test report", "knowledge",
  "A document from a metal mill that certifies the chemical and mechanical properties of a batch of material supplied with it.",
  variants=["Mill test certificate"])

NS("millennials-f2892a", "It names a generation, not a skill.")

N("millimeter-waves-0c65ad", "Millimeter waves", "knowledge",
  "Radio waves with wavelengths of about 1 to 10 millimetres (30 to 300 GHz), used in 5G, radar and imaging.",
  variants=["mmWave", "Millimetre waves"])
