from lib_resp import *

EXPECTED = ["Ada 95", "Adapter Scripting Language", "Afrikaans", "Albanian", "Algebraic Logic Functional", "Algol", "Alice",
 "Amharic", "Apex", "Arabic", "Armenian", "Assamese", "Assembly Language", "Awk", "Azerbaijani", "Ballerina", "Bash", "Basic",
 "Beanshell", "Bemba", "Bislama", "Blitzmax", "Boo", "Bosnian", "Burmese", "C++", "C", "C#", "Castilian Spanish", "Cebuano",
 "CFML(coldfusion Markup Language)", "Chichewa (nyanja)", "Chinese", "Clist", "Clojure", "Cobol", "Coffeescript", "Coldfusion",
 "Common Lisp", "Component Pascal", "Crystal", "Cython", "Czech", "D", "Danish", "Dart", "Dcl (digital Command Language)",
 "Delphi", "Dutch", "Dylan"]

prog("Ada 95", "Ada 95",
     "The 1995 revision of the Ada programming language (ISO/IEC 8652:1995), which added object-oriented features to Ada 83.")
unsure("Adapter Scripting Language", "I do not know what a language called Adapter Scripting Language is, so I cannot define it.")
human("Afrikaans", "Afrikaans", "A West Germanic language that developed from Dutch, spoken mainly in South Africa and Namibia.")
human("Albanian", "Albanian", "An Indo-European language forming its own branch, spoken mainly in Albania, Kosovo and North Macedonia.")
variant_of("Algebraic Logic Functional", "Algebraic Logic Functional")
prog("Algol", "ALGOL",
     "A family of imperative programming languages first designed in 1958, whose ALGOL 60 and ALGOL 68 versions influenced many later languages.")
unsure("Alice", "Alice names both an educational 3D programming environment from Carnegie Mellon and a Standard ML dialect (Alice ML), and nothing here says which is meant.")
human("Amharic", "Amharic", "A Semitic language spoken mainly in Ethiopia, where it is the working language of the federal government.")
prog("Apex", "Apex",
     "A strongly typed, object-oriented programming language for writing business logic on the Salesforce platform.")
human("Arabic", "Arabic", "A Semitic language spoken across the Middle East and North Africa, with a standard written form used in formal settings.")
human("Armenian", "Armenian", "An Indo-European language forming its own branch, spoken mainly in Armenia and by Armenian communities abroad.")
human("Assamese", "Assamese", "An Indo-Aryan language spoken mainly in the Indian state of Assam.")
prog("Assembly Language", "Assembly language",
     "A family of low-level programming languages in which each statement corresponds closely to a machine instruction of a particular processor.")
prog("Awk", "AWK",
     "A scripting language for processing text line by line with pattern-action rules, named after its creators Aho, Weinberger and Kernighan.")
human("Azerbaijani", "Azerbaijani", "A Turkic language spoken mainly in Azerbaijan and northwestern Iran.", variants=["Azeri"])
prog("Ballerina", "Ballerina",
     "An open-source programming language for writing cloud-native integration and network-service programs, created by WSO2.")
prog("Bash", "Bash",
     "The GNU Project's Unix shell and its scripting language, the default shell on many Linux systems.",
     variants=["Bourne-Again Shell"])
prog("Basic", "BASIC",
     "A family of high-level programming languages first designed in 1964 at Dartmouth College to be easy for beginners.")
prog("Beanshell", "BeanShell",
     "A lightweight scripting language for the Java platform that interprets Java syntax with extra scripting features.")
variant_of("Bemba", "Bemba")
human("Bislama", "Bislama", "An English-based creole language and one of the national languages of Vanuatu.")
prog("Blitzmax", "BlitzMax",
     "A BASIC-derived, object-oriented programming language aimed at game development, created by Blitz Research.")
prog("Boo", "Boo",
     "An object-oriented, statically typed programming language for the .NET common language infrastructure, with a Python-inspired syntax.")
human("Bosnian", "Bosnian",
      "A South Slavic language, one of the official languages of Bosnia and Herzegovina, closely related to Croatian and Serbian.")
human("Burmese", "Burmese", "A Sino-Tibetan language, the official language of Myanmar.")
variant_of("C++", "C++")
prog("C", "C",
     "A general-purpose procedural programming language created by Dennis Ritchie at Bell Labs in the early 1970s.")
variant_of("C#", "C#")
variant_of("Castilian Spanish", "Castilian Spanish")
human("Cebuano", "Cebuano", "An Austronesian language spoken mainly in Cebu, the central Philippines and parts of Mindanao.")
prog("CFML(coldfusion Markup Language)", "CFML",
     "A tag-based scripting language, run by servers such as Adobe ColdFusion and Lucee, for building dynamic web applications.",
     variants=["ColdFusion Markup Language"])
human("Chichewa (nyanja)", "Chichewa", "A Bantu language spoken mainly in Malawi and also known as Nyanja, notably in Zambia.",
      variants=["Nyanja"])
variant_of("Chinese", "Chinese")
prog("Clist", "CLIST",
     "A scripting language for writing command procedures under IBM's TSO on z/OS and earlier MVS mainframe systems.")
prog("Clojure", "Clojure",
     "A dynamic, functional Lisp dialect that runs mainly on the Java Virtual Machine, created by Rich Hickey.")
prog("Cobol", "COBOL",
     "A business-oriented programming language dating from 1959, still used in banking, insurance and government mainframe systems.")
prog("Coffeescript", "CoffeeScript", "A programming language with concise syntax that compiles to JavaScript.")
new("Coldfusion", "Adobe ColdFusion", "platform",
    "A commercial web application server and development platform, now from Adobe, that runs applications written in CFML.",
    variants=["ColdFusion"], verbs=("develop",), lang=None,
    note="ColdFusion is an application server and platform; the language it runs is CFML, not ColdFusion itself.",
    reason="ColdFusion is a product that runs CFML, not itself a language; no entry among the nearest.")
prog("Common Lisp", "Common Lisp",
     "A standardized, multi-paradigm dialect of Lisp specified in ANSI standard X3.226-1994.")
prog("Component Pascal", "Component Pascal",
     "A programming language in the Pascal and Oberon tradition, a refinement of Oberon-2 designed by Oberon microsystems.")
prog("Crystal", "Crystal", "A statically typed, compiled programming language with a Ruby-inspired syntax.")
prog("Cython", "Cython",
     "A programming language that is a superset of Python and is compiled to C to build fast Python extension modules.",
     rels=[("related", "Python")])
variant_of("Czech", "Czech")
prog("D", "D",
     "A general-purpose systems programming language with C-like syntax, created by Walter Bright.")
human("Danish", "Danish", "A North Germanic language, the official language of Denmark.")
variant_of("Dart", "Dart")
prog("Dcl (digital Command Language)", "Digital Command Language",
     "The command language of the OpenVMS operating system and its predecessors from Digital Equipment Corporation, used interactively and for command procedures.")
prog("Delphi", "Delphi",
     "An object-oriented dialect of Pascal (Object Pascal) and the development environment built around it, originally from Borland and now from Embarcadero.")
human("Dutch", "Dutch", "A West Germanic language spoken mainly in the Netherlands, Belgium and Suriname.", variants=["Nederlands"])
prog("Dylan", "Dylan",
     "A multi-paradigm, object-oriented programming language derived from Scheme and influenced by Common Lisp, developed in the 1990s by Apple and partners.")

finish(EXPECTED)
print("slice 1 ok", len(WRITTEN))
