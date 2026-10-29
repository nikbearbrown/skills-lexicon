import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draft_lib import *

new(0, "Kachin (Language)", "Kachin", "human-language",
    "A Tibeto-Burman language spoken by the Kachin people of northern Myanmar and neighbouring parts of China and India.",
    variants=["Jingpho"])
new(1, "Kahoot!", "Kahoot!", "platform",
    "A game-based learning platform where a host sets quizzes that players answer live on their own devices.",
    variants=["Kahoot"], verbs=["create", "host"])
new(2, "Kairosdb", "KairosDB", "platform",
    "A scalable time-series database, originally built on Apache Cassandra, for storing and querying metrics data.",
    verbs=["query", "deploy"])
new(3, "Kalenjin (Language)", "Kalenjin", "human-language",
    "A Nilotic language, or cluster of closely related languages, spoken by the Kalenjin people of Kenya.")
new(4, "Katalon Studio", "Katalon Studio", "tool",
    "A test automation tool for web, API, mobile and desktop applications.",
    verbs=["automate"])
unsure(5, "Kayan (Language)", "Two unrelated languages are called Kayan (one in Borneo, one in Myanmar) and nothing here says which is meant.")
no(6, "Keen Worker", "An adjective and a job noun, not a skill.")
new(7, "Kenna Security", "Kenna Security", "platform",
    "A risk-based vulnerability management platform, now part of Cisco, that ranks vulnerabilities by how likely they are to be exploited.",
    variants=["Cisco Vulnerability Management"])
new(8, "Kenya Certificate Of Primary Education", "Kenya Certificate of Primary Education", "credential",
    "A certificate awarded by the Kenya National Examinations Council to pupils who sit the national examination at the end of primary school.",
    variants=["KCPE"], cert=True, scope="single-issuer")
new(9, "Kenya Certificate Of Secondary Education", "Kenya Certificate of Secondary Education", "credential",
    "A certificate awarded by the Kenya National Examinations Council to students who sit the national examination at the end of secondary school.",
    variants=["KCSE"], cert=True, scope="single-issuer")
new(10, "Keras", "Keras", "library",
    "A high-level Python library for building and training neural networks.",
    verbs=["build", "train"])
new(11, "Keyhole Markup Languages", "Keyhole Markup Language", "markup-language",
    "An XML-based markup language for describing geographic features, placemarks and map views, used by Google Earth and other mapping software.",
    variants=["KML"])
new(12, "Khmer (Language)", "Khmer", "human-language",
    "The Austroasiatic language of Cambodia, written in the Khmer script.")
variant(13, "Kikuyu (Language)", "o410b5qw7m", "Kikuyu and Gikuyu are two spellings of the same Bantu language of central Kenya.")
new(14, "Kinesitherapy", "Kinesitherapy", "skill",
    "Treating disease or injury through guided movement and exercise.",
    variants=["Kinesiotherapy"])
new(15, "Kinetics (Typography)", "Kinetic typography", "skill",
    "Animating text in motion graphics and video so that its movement and timing carry meaning.",
    reason="The parenthesis points to typography, so the term appears to mean kinetic typography.")
new(16, "Knockout.js", "Knockout.js", "library",
    "A JavaScript library that binds page elements to data models with declarative bindings, following the model-view-viewmodel pattern.")
new(17, "Know Your Third Party (KY3P)", "Know Your Third Party (KY3P)", "platform",
    "A third-party risk management platform in which firms collect and share due-diligence information on their suppliers and vendors.",
    reason="KY3P is a named third-party risk platform, though I am not certain of its owner or details.")
no(18, "Knowledge Engineer", "A job title, not a skill.")
no(19, "Knuckle Joint (Hand)", "A part of the body, not a skill.")
unsure(20, "Kol (Language)", "Several unrelated languages are called Kol and nothing here says which one is meant.")
unsure(21, "Koma (Language)", "Several unrelated languages in Africa are called Koma and nothing here says which one is meant.")
no(22, "Konkani Muslims", "An ethnic and religious community, not a skill.")
new(23, "Korwa (Language)", "Korwa", "human-language",
    "An Austroasiatic language of the Munda branch spoken by the Korwa people of central-eastern India.")
new(24, "Kpi Reporting", "KPI reporting", "skill",
    "Collecting key performance indicator data and presenting it in regular reports or dashboards.",
    verbs=["produce", "present"])
new(25, "Kurdish (Language)", "Kurdish", "human-language",
    "A group of Northwestern Iranian languages and dialects spoken by Kurds in Turkey, Iraq, Iran and Syria.")
new(26, "Kurukh (Language)", "Kurukh", "human-language",
    "A Dravidian language spoken by the Oraon people of eastern India and neighbouring parts of Nepal and Bangladesh.",
    variants=["Kurux"])
unsure(27, "Kwa (Language)", "Kwa is mainly the name of a Niger-Congo language family, and nothing here says whether one language or the family is meant.")
new(28, "Kyoto Protocol", "Kyoto Protocol", "standard",
    "An international treaty adopted in 1997 that set binding targets for industrialised countries to cut greenhouse gas emissions.",
    reason="A named international climate agreement that postings ask people to know or comply with.")
new(29, "Kyriba (Treasury Management Software)", "Kyriba", "platform",
    "A cloud platform that corporate finance teams use for treasury, cash and risk management.")
no(30, "Lab Tests", "A generic plural noun naming the tests, not a specific skill.")
new(31, "Label Edge Router (MPLS Networking)", "Label edge router", "tool",
    "A router at the edge of an MPLS network that adds labels to packets entering the network and removes them as packets leave.")
new(32, "Label Printer", "Label printer", "tool",
    "A printer designed to print text, barcodes and images onto adhesive labels or label stock.",
    verbs=["operate", "maintain"])
new(33, "Labor Market Trends", "Labor market trends", "knowledge",
    "Understanding of how employment, wages and the supply and demand for workers are changing over time.",
    variants=["Labour market trends"])
new(34, "Labour Economics", "Labour economics", "knowledge",
    "The branch of economics that studies labour markets, wages, employment and unemployment.",
    variants=["Labor economics"])
new(35, "Labour Laws", "Labour law", "knowledge",
    "The body of law governing the relationship between employers, employees and trade unions.",
    variants=["Labor law", "Labor laws"])
new(36, "Ladino (Language)", "Ladino", "human-language",
    "The Romance language descended from medieval Spanish that is spoken by Sephardic Jewish communities.",
    variants=["Judeo-Spanish"])
unsure(37, "Lamination (Flooring)", "Could mean making laminate flooring or fitting it, and nothing here says which.")
new(38, "Land-Atmosphere Interactions", "Land-atmosphere interactions", "knowledge",
    "The study of how the land surface and the atmosphere exchange energy, water, carbon and momentum.")
new(39, "Landing Page Optimization", "Landing page optimization", "skill",
    "Improving the design and content of web landing pages, often through testing, to raise the share of visitors who convert.",
    variants=["Landing page optimisation"], verbs=["test", "improve"])
no(40, "Landman", "A job title in the oil and gas industry, not a skill.")
new(41, "Lando (Software)", "Lando", "tool",
    "A command-line tool, built on Docker, for creating and running local development environments.")
new(42, "Landscape Painting", "Landscape painting", "skill",
    "Painting natural scenery such as hills, fields, water and sky.")
new(43, "Landscaping and Yard Care", "Landscaping and yard care", "skill",
    "Designing, planting and maintaining gardens, lawns and other outdoor spaces around buildings.",
    relations=[("related", "wcem2h6zih")])
new(44, "Lango (Language)", "Lango", "human-language",
    "A Nilotic language spoken by the Lango people of northern Uganda.")
no(45, "Language", "A generic word that names no particular language or skill.")
unsure(46, "Language Design", "Could mean designing programming languages or constructed human languages, and nothing here says which.")
new(47, "Language Interpretation and Translation", "Language interpretation and translation", "skill",
    "Converting spoken (interpretation) or written (translation) content from one language into another.",
    note="The legacy class says Language, but this is a skill of working between languages, not a language itself.",
    verbs=["interpret", "translate"])
unsure(48, "Language Study", "Too vague to say whether it means learning languages, linguistics or something else.")
new(49, "Language Teaching", "Language teaching", "skill",
    "Teaching learners to understand, speak, read and write a language, usually one that is not their first.",
    note="The legacy class says Language, but this is the skill of teaching a language, not a language itself.",
    verbs=["teach"])
