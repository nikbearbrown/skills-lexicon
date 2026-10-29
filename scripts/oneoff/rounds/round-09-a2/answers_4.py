from lib_resp import *

EXPECTED = ["Samoan", "Sas", "Scala", "Scheme", "Scratch", "Serbo-croatian", "Sesotho", "Shell", "Shona", "Simula", "Sindhi",
 "Sinhala", "Siswati (swazi)", "Slovak", "Smalltalk", "Somali", "Sotho", "Spanish", "Sql", "Sundanese", "Swahili", "Swedish",
 "Swift", "Tagalog (filipino)", "Tajik", "Tatar", "Tcl", "Telugu", "Thai", "Tigrinya", "Tswana", "Turkish", "Turkmen",
 "Typescript", "Uighur", "Ukrainian", "Unified Modeling Languages", "Urdu", "Uzbek", "Vb.net", "Vba", "Verilog", "Vhdl",
 "Vietnamese", "Walloon", "XBRL", "XML", "XUL", "Zulu"]
# the 50th is Zulu; "Sas" etc. above make 49 + one more below
EXPECTED = EXPECTED

human("Samoan", "Samoan", "A Polynesian language, an official language of Samoa.")
prog("Sas", "SAS",
     "The programming language of the SAS software suite, used for data management, statistical analysis and reporting.")
variant_of("Scala", "Scala")
prog("Scheme", "Scheme", "A minimalist dialect of Lisp with lexical scoping and first-class continuations.")
prog("Scratch", "Scratch", "A block-based visual programming language developed at the MIT Media Lab for teaching children to code.")
human("Serbo-croatian", "Serbo-Croatian",
      "A South Slavic language whose standardized forms include Bosnian, Croatian, Montenegrin and Serbian.")
human("Sesotho", "Sesotho",
      "A Bantu language, the national language of Lesotho and one of the official languages of South Africa.",
      variants=["Southern Sotho"])
prog("Shell", "Shell scripting",
     "The scripting languages of Unix command-line shells such as sh and Bash, used to automate sequences of commands.",
     variants=["Shell script"])
human("Shona", "Shona", "A Bantu language spoken mainly in Zimbabwe.", variants=["chiShona"])
prog("Simula", "Simula",
     "An early object-oriented programming language developed in the 1960s by Ole-Johan Dahl and Kristen Nygaard that introduced classes and objects.")
human("Sindhi", "Sindhi", "An Indo-Aryan language spoken in the Sindh province of Pakistan and parts of India.")
human("Sinhala", "Sinhala", "An Indo-Aryan language, the main language of Sri Lanka.", variants=["Sinhalese"])
variant_of("Siswati (swazi)", "Swati", "siSwati and Swazi are names for the Swati language, and the existing entry lists both.")
human("Slovak", "Slovak", "A West Slavic language, the official language of Slovakia.")
prog("Smalltalk", "Smalltalk", "A pure object-oriented programming language and environment developed at Xerox PARC in the 1970s.")
human("Somali", "Somali", "A Cushitic language, the official language of Somalia.")
human("Sotho", "Sesotho",
      "A Bantu language, the national language of Lesotho and one of the official languages of South Africa.",
      reason="Taken to mean Sesotho (Southern Sotho), the same concept as the Sesotho tag; Northern Sotho is usually named Sepedi.")
human("Spanish", "Spanish", "A Romance language spoken in Spain, Latin America and many other countries.", variants=["Español"])
variant_of("Sql", "SQL")
human("Sundanese", "Sundanese", "An Austronesian language spoken by the Sundanese people in West Java, Indonesia.")
human("Swahili", "Swahili", "A Bantu language widely used as a lingua franca in East Africa.", variants=["Kiswahili"])
human("Swedish", "Swedish", "A North Germanic language, the main language of Sweden and an official language of Finland.")
variant_of("Swift", "Swift", "The tag is explicitly the Swift programming language, which the existing Swift entry covers.")
human("Tagalog (filipino)", "Filipino", "The standardized form of Tagalog and the national language of the Philippines.",
      variants=["Tagalog"],
      reason="Tagalog and Filipino are used as one tag here; same concept as the Filipino tag, so the same name is given.")
human("Tajik", "Tajik", "A variety of Persian, the official language of Tajikistan.")
human("Tatar", "Tatar", "A Turkic language spoken mainly in Tatarstan and other parts of Russia.")
prog("Tcl", "Tcl", "A dynamic scripting language, short for Tool Command Language, created by John Ousterhout.",
     variants=["Tool Command Language"])
human("Telugu", "Telugu", "A Dravidian language spoken mainly in the Indian states of Andhra Pradesh and Telangana.")
human("Thai", "Thai", "A Kra-Dai language, the official language of Thailand.")
human("Tigrinya", "Tigrinya", "A Semitic language spoken in Eritrea and the Tigray region of Ethiopia.")
human("Tswana", "Tswana", "A Bantu language, the national language of Botswana and one of the official languages of South Africa.",
      variants=["Setswana"])
variant_of("Turkish", "Turkish")
human("Turkmen", "Turkmen", "A Turkic language, the official language of Turkmenistan.")
variant_of("Typescript", "TypeScript")
human("Uighur", "Uyghur", "A Turkic language spoken mainly by the Uyghur people in Xinjiang, China.", variants=["Uighur"])
human("Ukrainian", "Ukrainian", "An East Slavic language, the official language of Ukraine.")
unsure("Unified Modeling Languages",
       "This is almost certainly the same concept as the existing UML entry (id va052jqj8q), which is not among the nearest entries I was shown, so I cannot name it as variant_of; a person should merge it.")
human("Urdu", "Urdu", "An Indo-Aryan language, the national language of Pakistan and one of the official languages of India.")
human("Uzbek", "Uzbek", "A Turkic language, the official language of Uzbekistan.")
prog("Vb.net", "Visual Basic .NET", "Microsoft's object-oriented version of the Visual Basic language for the .NET platform.",
     variants=["VB.NET"])
prog("Vba", "Visual Basic for Applications",
     "The Visual Basic-based scripting language built into Microsoft Office applications, used to automate tasks.",
     variants=["VBA"])
new("Verilog", "Verilog", "modeling-language",
    "A hardware description language used to model, simulate and design digital electronic circuits.",
    verbs=("write",), lang="programming", rels=[("related", "SystemVerilog")],
    reason="A hardware description language with no matching entry among the nearest.")
new("Vhdl", "VHDL", "modeling-language",
    "A hardware description language, standardized by the IEEE, used to model and design digital circuits; the name abbreviates VHSIC Hardware Description Language.",
    variants=["VHSIC Hardware Description Language"], verbs=("write",), lang="programming",
    reason="A hardware description language with no matching entry among the nearest.")
human("Vietnamese", "Vietnamese", "An Austroasiatic language, the official language of Vietnam.")
human("Walloon", "Walloon", "A Romance language spoken in Wallonia, the French-speaking part of Belgium.")
variant_of("XBRL", "XBRL")
variant_of("XML", "XML")
variant_of("XUL", "XUL")
human("Zulu", "Zulu", "A Bantu language spoken mainly in South Africa, one of its official languages.", variants=["isiZulu"])

finish(EXPECTED)
print("slice 4 ok", len(WRITTEN))
