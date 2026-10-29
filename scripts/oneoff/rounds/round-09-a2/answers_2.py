from lib_resp import *

EXPECTED = ["Dzongkha (bhutanese)", "Eiffel", "Elm", "English", "Erlang", "F*", "F#", "Fantom", "Filipino", "Finnish", "Forth",
 "Fortran", "French", "Fula (fulani)", "German", "Go", "Google Dart", "Greek", "Groovy", "Hack", "Haitian Creole",
 "Hardware Description Language", "Haskell", "Hausa", "Hawaiian", "Haxe", "Hebrew", "Hindi", "Hmong", "Hokkien Dialects",
 "Hungarian", "Indonesian", "Italian", "J#", "Japanese", "Java", "Javascript", "Jscript", "Julia",
 "Just-another Hardware Description Language (jhdl)", "Kannada", "Kazakh", "Keyhole Markup Languages", "Kinyarwanda",
 "Kirundi", "Korean", "Kotlin", "Kyrgyz", "Labview", "Ladder Logic"]

human("Dzongkha (bhutanese)", "Dzongkha", "A Sino-Tibetan language, the national language of Bhutan.")
prog("Eiffel", "Eiffel",
     "An object-oriented programming language designed by Bertrand Meyer and built around design by contract.")
prog("Elm", "Elm", "A functional programming language that compiles to JavaScript, used to build web front ends.")
variant_of("English", "English")
prog("Erlang", "Erlang",
     "A functional programming language, originally developed at Ericsson, designed for concurrent, fault-tolerant systems.")
prog("F*", "F*",
     "A proof-oriented, ML-family functional programming language for writing and verifying programs, developed by Microsoft Research and Inria.")
variant_of("F#", "F#")
prog("Fantom", "Fantom",
     "A general-purpose, object-oriented programming language that targets the Java Virtual Machine, .NET and JavaScript.")
human("Filipino", "Filipino", "The standardized form of Tagalog and the national language of the Philippines.",
      variants=["Tagalog"])
human("Finnish", "Finnish", "A Uralic language, the main language of Finland.")
variant_of("Forth", "Forth")
prog("Fortran", "Fortran",
     "One of the oldest high-level programming languages, created at IBM in the 1950s and still widely used for numerical and scientific computing.")
variant_of("French", "French")
human("Fula (fulani)", "Fula",
      "A Niger-Congo language spoken by the Fulani people as a chain of dialects across West and Central Africa.",
      variants=["Fulani", "Fulfulde"])
human("German", "German", "A West Germanic language spoken mainly in Germany, Austria and Switzerland.", variants=["Deutsch"])
prog("Go", "Go",
     "A statically typed, compiled programming language designed at Google, known for simple syntax and built-in concurrency.",
     variants=["Golang"])
variant_of("Google Dart", "Dart", "Google Dart is the Dart programming language, which Google develops.")
human("Greek", "Greek", "An Indo-European language forming its own Hellenic branch, spoken mainly in Greece and Cyprus.")
variant_of("Groovy", "Groovy")
prog("Hack", "Hack",
     "A programming language for the HipHop Virtual Machine, developed at Facebook as a statically typed dialect of PHP.",
     rels=[("related", "PHP")])
human("Haitian Creole", "Haitian Creole", "A French-based creole language, one of the two official languages of Haiti.",
      variants=["Kreyòl Ayisyen", "Haitian Kreyol"])
variant_of("Hardware Description Language", "Hardware description language")
prog("Haskell", "Haskell",
     "A purely functional programming language with lazy evaluation and a strong static type system.")
human("Hausa", "Hausa",
      "A Chadic language of the Afroasiatic family, spoken mainly in northern Nigeria and Niger and used as a lingua franca in West Africa.")
variant_of("Hawaiian", "Hawaiian")
prog("Haxe", "Haxe",
     "A high-level, cross-platform programming language and compiler that can produce code for targets such as JavaScript, C++ and the JVM.")
human("Hebrew", "Hebrew", "A Semitic language and the main official language of Israel.")
human("Hindi", "Hindi", "An Indo-Aryan language written in the Devanagari script and an official language of India.")
human("Hmong", "Hmong",
      "A group of related Hmong-Mien languages spoken by the Hmong people in China, Southeast Asia and diaspora communities.")
variant_of("Hokkien Dialects", "Hokkien", "The existing Hokkien entry already covers the Hokkien dialects and lists this label as a variant.")
variant_of("Hungarian", "Hungarian")
human("Indonesian", "Indonesian", "A standardized form of Malay, the national language of Indonesia.", variants=["Bahasa Indonesia"])
human("Italian", "Italian", "A Romance language spoken mainly in Italy and Switzerland.")
prog("J#", "J#",
     "A Microsoft programming language with Java-language syntax for the .NET Framework, now discontinued.")
human("Japanese", "Japanese", "The language of Japan, written with kanji and kana.")
variant_of("Java", "Java")
variant_of("Javascript", "JavaScript")
variant_of("Jscript", "JScript")
prog("Julia", "Julia", "A high-level, dynamic programming language designed for fast numerical and scientific computing.")
variant_of("Just-another Hardware Description Language (jhdl)", "JHDL")
human("Kannada", "Kannada", "A Dravidian language spoken mainly in the Indian state of Karnataka.")
human("Kazakh", "Kazakh", "A Turkic language, the official language of Kazakhstan.")
variant_of("Keyhole Markup Languages", "Keyhole Markup Language")
human("Kinyarwanda", "Kinyarwanda", "A Bantu language, the national language of Rwanda.")
human("Kirundi", "Kirundi", "A Bantu language, the national language of Burundi.", variants=["Rundi"])
human("Korean", "Korean", "The language of Korea, written in the Hangul script and spoken in North and South Korea.")
prog("Kotlin", "Kotlin",
     "A statically typed programming language from JetBrains that runs on the Java Virtual Machine and is widely used for Android apps.")
human("Kyrgyz", "Kyrgyz", "A Turkic language, the official language of Kyrgyzstan.", variants=["Kirghiz"])
new("Labview", "LabVIEW", "tool",
    "National Instruments' graphical programming environment, in which programs are built by wiring together icons, used for test, measurement and control.",
    verbs=("develop",), lang=None,
    note="LabVIEW is a development environment; the graphical language it uses is called G, not LabVIEW.",
    reason="A named software environment with no matching entry among the nearest.")
prog("Ladder Logic", "Ladder logic",
     "A graphical programming language for programmable logic controllers, resembling electrical relay-logic diagrams.",
     variants=["Ladder diagram"])

finish(EXPECTED)
print("slice 2 ok", len(WRITTEN))
