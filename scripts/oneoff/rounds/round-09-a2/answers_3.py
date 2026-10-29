from lib_resp import *

EXPECTED = ["Lao", "Lingala", "Lingo", "Lisp", "Livescript", "Logo", "Lua", "Luxembourgish", "M Programming Language", "Macedonian",
 "Macromedia Flex Markup Language", "Malagasy", "Malayalam", "Maltese", "Mandarin", "MATLAB", "Media Center Markup Language",
 "Mongolian", "Mql4 (metaquotes Language 4)", "Mumps", "Nim", "Norwegian", "Oberon", "Ocaml", "Openedge Abl", "Oriya (odia)",
 "Oz", "Pari/gp", "Pascal", "Pashto", "Perl", "Persian (farsi)", "PHP", "Pl/i", "Pl/sql", "Polish", "Portuguese", "Postscript",
 "Powershell", "Prolog", "Punjabi", "Purescript", "Q#", "Quechua", "R", "Racket", "Romanian", "Ruby", "Russian", "Rust"]

human("Lao", "Lao", "A Kra-Dai language, the official language of Laos.")
variant_of("Lingala", "Lingala")
prog("Lingo", "Lingo", "The scripting language of Macromedia Director, later Adobe Director, used to build multimedia and games.")
prog("Lisp", "Lisp",
     "A family of programming languages originating in 1958, built on parenthesized prefix notation and linked-list data.")
prog("Livescript", "LiveScript",
     "A functional-style programming language that compiles to JavaScript, descended from CoffeeScript.")
prog("Logo", "Logo",
     "An educational programming language known for turtle graphics, developed in the 1960s by Wally Feurzeig, Seymour Papert and others.")
prog("Lua", "Lua", "A lightweight, embeddable scripting language created at PUC-Rio in Brazil.")
human("Luxembourgish", "Luxembourgish", "A West Germanic language, a national language of Luxembourg.", variants=["Lëtzebuergesch"])
unsure("M Programming Language",
       "M is an alternate name for MUMPS and also the name of the Power Query formula language, and nothing here says which is meant.")
human("Macedonian", "Macedonian", "A South Slavic language, the official language of North Macedonia.")
variant_of("Macromedia Flex Markup Language", "MXML", "MXML is the XML-based markup language from Macromedia for Flex, which this label spells out.")
human("Malagasy", "Malagasy", "An Austronesian language, the national language of Madagascar.")
human("Malayalam", "Malayalam", "A Dravidian language spoken mainly in the Indian state of Kerala.")
human("Maltese", "Maltese", "A Semitic language with many Romance loanwords, the national language of Malta.")
human("Mandarin", "Mandarin",
      "The group of Chinese varieties spoken across northern and southwestern China, whose standard form is the official language of China.",
      variants=["Mandarin Chinese"])
prog("MATLAB", "MATLAB",
     "A proprietary programming language and numeric computing environment from MathWorks, built around matrix operations.")
variant_of("Media Center Markup Language", "Media Center Markup Language")
human("Mongolian", "Mongolian", "A Mongolic language, the official language of Mongolia.")
prog("Mql4 (metaquotes Language 4)", "MQL4",
     "A C-like programming language for writing indicators, scripts and automated trading programs on the MetaTrader 4 trading platform.",
     variants=["MetaQuotes Language 4"])
prog("Mumps", "MUMPS",
     "A programming language with a built-in hierarchical database, developed at Massachusetts General Hospital in the 1960s and used in healthcare systems.",
     variants=["Massachusetts General Hospital Utility Multi-Programming System"])
prog("Nim", "Nim", "A statically typed, compiled programming language with a Python-like syntax.")
human("Norwegian", "Norwegian",
      "A North Germanic language, the official language of Norway, written in the Bokmål and Nynorsk standards.")
prog("Oberon", "Oberon",
     "A programming language designed by Niklaus Wirth in the late 1980s as a successor to Modula-2.")
prog("Ocaml", "OCaml",
     "A general-purpose functional programming language of the ML family with an object system, developed at Inria.",
     variants=["Objective Caml"])
prog("Openedge Abl", "OpenEdge ABL",
     "Progress Software's high-level, business-oriented programming language for the OpenEdge platform, formerly known as Progress 4GL.",
     variants=["Progress 4GL", "OpenEdge Advanced Business Language"])
human("Oriya (odia)", "Odia", "An Indo-Aryan language spoken mainly in the Indian state of Odisha.", variants=["Oriya"])
prog("Oz", "Oz",
     "A multiparadigm programming language supporting functional, logic, constraint and concurrent programming, implemented by the Mozart Programming System.")
new("Pari/gp", "PARI/GP", "tool",
    "A computer algebra system for fast computations in number theory, with its own scripting language called GP.",
    verbs=("use",), lang=None,
    note="PARI/GP is a computer algebra system; its scripting language is called GP, so the product is a tool, not itself a language.",
    reason="A named software system with no matching entry among the nearest.")
prog("Pascal", "Pascal",
     "A structured, imperative programming language designed by Niklaus Wirth around 1970 and widely used for teaching programming.")
human("Pashto", "Pashto", "An Eastern Iranian language spoken mainly in Afghanistan and Pakistan.")
prog("Perl", "Perl", "A high-level, general-purpose scripting language known for text processing and regular expressions.")
human("Persian (farsi)", "Persian",
      "An Iranian language, the official language of Iran, closely related to Dari and Tajik.",
      variants=["Farsi"], rels=[("related", "Dari")])
variant_of("PHP", "PHP")
prog("Pl/i", "PL/I",
     "A multi-purpose programming language developed by IBM in the 1960s for scientific, business and systems programming.")
prog("Pl/sql", "PL/SQL",
     "Oracle's procedural extension of SQL, used to write stored procedures, functions and triggers in Oracle Database.",
     variants=["Procedural Language/SQL"], rels=[("related", "SQL")])
human("Polish", "Polish", "A West Slavic language, the official language of Poland.")
variant_of("Portuguese", "Portuguese")
prog("Postscript", "PostScript",
     "A stack-based page description language and programming language from Adobe, used to describe printed pages and graphics.")
prog("Powershell", "PowerShell",
     "A Microsoft command-line shell and scripting language built on .NET, used for task automation and configuration management.")
variant_of("Prolog", "Prolog")
human("Punjabi", "Punjabi", "An Indo-Aryan language spoken in the Punjab region of India and Pakistan.", variants=["Panjabi"])
prog("Purescript", "PureScript", "A strongly typed, purely functional programming language that compiles to JavaScript.")
prog("Q#", "Q#", "A Microsoft programming language for expressing quantum algorithms.")
variant_of("Quechua", "Quechua")
prog("R", "R", "A programming language and software environment for statistical computing and graphics.")
prog("Racket", "Racket",
     "A general-purpose programming language in the Scheme and Lisp family, designed to support creating new languages.")
variant_of("Romanian", "Romanian")
prog("Ruby", "Ruby",
     "A dynamic, object-oriented scripting language created by Yukihiro Matsumoto and known for its readable syntax.")
human("Russian", "Russian", "An East Slavic language, the official language of Russia.")
prog("Rust", "Rust",
     "A systems programming language focused on memory safety, concurrency and performance, without a garbage collector.")

finish(EXPECTED)
print("slice 3 ok", len(WRITTEN))
