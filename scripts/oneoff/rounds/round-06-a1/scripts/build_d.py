import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from h import *

A = {}

A[150] = ("Java API For XML-Based RPC", new(
    "JAX-RPC", "library",
    "A Java API for building and calling web services that use XML-based remote procedure calls, later replaced by JAX-WS."))

A[151] = ("Javascript Build", unsure("Unclear whether it means JavaScript build tools, a build process or a particular build."))

A[152] = ("Javascript Engine", new(
    "JavaScript engine", "tool",
    "A program that parses, compiles and runs JavaScript code, such as V8 in Chrome and Node.js, SpiderMonkey in Firefox and JavaScriptCore in Safari.",
    rel=[("related", "h60l8olauw")]))

A[153] = ("JavaScript Pagination Plugin", ns("A generic description of a plugin, not a named product or skill."))

A[154] = ("Javascriptcore", new(
    "JavaScriptCore", "tool",
    "The JavaScript engine of the WebKit browser engine, used in Safari and available to macOS and iOS apps.",
    rel=[("related", "h60l8olauw")]))

A[155] = ("Javax.comm", new(
    "Java Communications API", "library",
    "A Java API, in the javax.comm package, for reading and writing serial and parallel ports.",
    variants=["javax.comm"]))

A[156] = ("Jax Ws", new(
    "JAX-WS", "library",
    "The Java API for XML Web Services, which uses annotations to build and call SOAP web services.",
    variants=["Java API for XML Web Services"]))

A[157] = ("JCAHO Standards", new(
    "Joint Commission standards", "standard",
    "Accreditation standards for US hospitals and other health-care organisations, set by The Joint Commission (formerly JCAHO) to judge quality and patient safety.",
    variants=["Joint Commission standards"]))

A[158] = ("JD Edwards CNC", new(
    "JD Edwards CNC", "skill",
    "Administering the technical environment of Oracle's JD Edwards EnterpriseOne ERP software, known as Configurable Network Computing, including installing, configuring, upgrading and tuning it.",
    variants=["JD Edwards Configurable Network Computing"]))

A[159] = ("Jdbctemplate", new(
    "JdbcTemplate", "library",
    "A class in the Spring Framework that simplifies database access with JDBC by handling connections, statements and exceptions."))

A[160] = ("JDesktop Network Components", new(
    "JDesktop Network Components", "library",
    "A Sun Microsystems SwingLabs project of components for building data-oriented Java Swing desktop applications.",
    variants=["JDNC"]))

A[161] = ("Jdoql", new(
    "JDOQL", "programming-language",
    "The object query language of Java Data Objects (JDO), used to retrieve persistent Java objects with filter expressions written in Java-like syntax.",
    lang="programming"))

A[162] = ("JED", unsure("Could be several unrelated things, such as the Joomla Extensions Directory or the JED text editor; nothing here shows which."))

A[163] = ("Jersey (Java Framework)", new(
    "Jersey", "framework",
    "An open-source Java framework, the reference implementation of JAX-RS, for building RESTful web services."))

A[164] = ("Jetbrains", ns("A company, not a skill."))

A[165] = ("Jiba Language (Jukunoid Languages)", new(
    "Jiba", "human-language",
    "A Jukunoid language spoken in Nigeria.",
    variants=["Jiba language"], lang="human"))

A[166] = ("Jigsaw (Jigsaw Puzzles)", ns("A hobby and toy, not a skill."))
A[167] = ("Jigsaw Puzzles", ns("A hobby and toy, not a skill."))

A[168] = ("Jigsaw Talent Management", unsure("Probably a software product or company, but I do not know it well enough to define it."))

A[169] = ("Jive (Software)", new(
    "Jive Software", "platform",
    "Enterprise collaboration software that gives an organisation an internal social network for sharing content and discussion."))

A[170] = ("Jmock", new(
    "jMock", "library",
    "A Java library for testing with mock objects, which lets a test state the calls it expects an object to receive."))

A[171] = ("Jmockit", new(
    "JMockit", "library",
    "A Java library for mocking objects, including static methods and constructors, in unit tests."))

A[172] = ("Job Satisfaction", ns("A feeling or workplace outcome, not a skill."))

A[173] = ("Job Scheduling (Batch Processing)", new(
    "Job scheduling", "skill",
    "Setting up, running and monitoring automated jobs, such as nightly batch runs, with a scheduler.",
    variants=["Batch job scheduling"]))

A[174] = ("Joint Clearance And Access Verification Systems", new(
    "Joint Clearance and Access Verification System", "tool",
    "The application in the US Department of Defense's Joint Personnel Adjudication System that security managers use to verify and record personnel security clearances and access.",
    variants=["JCAVS"]))

A[175] = ("Jointjs", new(
    "JointJS", "library",
    "A JavaScript library for building interactive diagrams and visual editors in the browser."))

A[176] = ("Joomla", new(
    "Joomla", "platform",
    "An open-source content management system, written in PHP, for building and managing websites."))

A[177] = ("JPA2", new(
    "Java Persistence API 2.0", "library",
    "The second version of the Java Persistence API, released as part of Java EE 6, for mapping Java objects to relational database tables; it added the Criteria API for building queries in code.",
    variants=["JPA 2.0", "JPA 2"]))

A[178] = ("JPEG", new(
    "JPEG", "standard",
    "A widely used standard for compressing photographs, from the Joint Photographic Experts Group, that makes small image files by discarding some detail.",
    variants=["JPG"]))

A[179] = ("Jsapi", unsure("Could be the Java Speech API, the Google or ArcGIS JavaScript APIs, or something else; nothing here shows which."))

A[180] = ("Jscript", new(
    "JScript", "programming-language",
    "Microsoft's implementation of the ECMAScript language, used in Internet Explorer and Windows Script Host.",
    lang="programming", rel=[("related", "h60l8olauw")]))

A[181] = ("Jscript.net", new(
    "JScript .NET", "programming-language",
    "A version of Microsoft's JScript language that compiles to .NET code and adds features such as typed variables and classes.",
    lang="programming"))

A[182] = ("Jsf 2", new(
    "JavaServer Faces 2.0", "framework",
    "The second major version of JavaServer Faces, the Java framework for building web user interfaces from components, released as part of Java EE 6 with Facelets as its standard view technology.",
    variants=["JSF 2.0", "JSF 2"]))

A[183] = ("Jsfiddle", new(
    "JSFiddle", "tool",
    "An online editor for writing, running and sharing snippets of HTML, CSS and JavaScript."))

A[184] = ("Jsgrid", new(
    "jsGrid", "library",
    "A lightweight jQuery plugin for showing and editing data in a table-like grid with sorting, filtering and paging."))

A[185] = ("JSON Web Token (JWT)", new(
    "JSON Web Token", "standard",
    "A compact, URL-safe token format, defined in RFC 7519, for passing claims between parties as a signed or encrypted JSON object, commonly used for authentication.",
    variants=["JWT"]))

A[186] = ("Jsperf", new(
    "jsPerf", "tool",
    "A website for creating and sharing JavaScript performance tests that run in the visitor's browser."))

A[187] = ("Jsrender", new(
    "JsRender", "library",
    "A JavaScript template library that renders HTML from templates and data."))

A[188] = ("Jsunit", new(
    "JsUnit", "framework",
    "An early unit-testing framework for JavaScript, modelled on JUnit."))

A[189] = ("JTrac - Open Source And Customizable Issue-Tracking In Java", new(
    "JTrac", "tool",
    "An open-source, customizable issue-tracking web application written in Java."))

A[190] = ("Juris Doctor", new(
    "Juris Doctor", "credential",
    "The professional law degree awarded in the United States and some other countries after law school, and a usual requirement to sit the bar exam in the US.",
    variants=["J.D."], cert=True, scope="many-issuers"))

A[191] = ("Jury", ns("A generic word, not a skill."))

A[192] = ("Jury Instructions", new(
    "Jury instructions", "skill",
    "Drafting and reviewing jury instructions, the statements of law that a judge gives jurors before they decide a case."))

A[193] = ("Jury Management", new(
    "Jury management", "skill",
    "Summoning, qualifying and scheduling the people called for jury service, and looking after them while they serve."))

A[194] = ("Just-Another Hardware Description Language (JHDL)", new(
    "JHDL", "modeling-language",
    "A hardware description language, developed at Brigham Young University, in which circuits are described with Java classes.",
    variants=["Just-Another Hardware Description Language"], lang="programming", rel=[("broader", "qsaoj0vnxc")]))

A[195] = ("Just In Time", unsure("Could be just-in-time manufacturing and inventory, JIT compilation, or just the ordinary phrase."))

A[196] = ("Juvenile Court", ns("A type of court, not a skill."))
A[197] = ("Juvenile Delinquency", ns("A social phenomenon, not a skill."))

A[198] = ("Juvenile Rehabilitation", new(
    "Juvenile rehabilitation", "skill",
    "Working with young people who have committed offences to change their behaviour and return to society, through counselling, education and supervised programmes."))

A[199] = ("K Means", new(
    "k-means clustering", "method",
    "An unsupervised machine-learning method that splits data into k groups by repeatedly assigning each point to the nearest of k centres and recalculating each centre as the mean of its group.",
    variants=["k-means", "k-means algorithm"]))

write_all(A)
