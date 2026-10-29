from common import *

NEW(100, 'Peace Officer Certification', 'Peace officer certification', 'credential',
    'A certification, awarded by a state or local peace officer standards body, showing that a person has met the training and screening requirements to serve as a sworn peace officer.',
    'A law-enforcement credential issued by many separate bodies; agrees with the legacy certification list.',
    cert=True, scope='many-issuers')

NEW(101, 'Peachtree (Accounting Software)', 'Peachtree Accounting', 'tool',
    'Accounting software for small businesses, originally from Peachtree Software and later sold by Sage as Sage 50.',
    'A named accounting product.',
    variants=['Sage Peachtree'], rel=[('broader', 'a0cpzx7lc1')])

NEW(102, 'Pearson PowerSchool', 'PowerSchool', 'platform',
    'A cloud-based student information system for schools and districts, used for attendance, grades, scheduling and communication with families.',
    'PowerSchool was formerly owned by Pearson; the product is the same.')

NEW(103, 'Pediatric Advanced Life Support', 'Pediatric Advanced Life Support', 'credential',
    'An American Heart Association course and certification in recognising and treating seriously ill or injured infants and children.',
    'A life-support certification alongside the existing ACLS and BLS entries.',
    rel=[('related', 'uqnp4t4487'), ('related', 'skuz6acynj')], cert=True, scope='single-issuer')

NAS(104, 'Pediatric Diseases And Disorders', 'A group of diseases, not a skill.')

NEW(105, 'Pediatric Surgeries', 'Pediatric surgery', 'knowledge',
    'The surgical specialty that operates on infants, children and adolescents.',
    'A surgical specialty, like the existing surgery entries.')

NEW(106, 'Peering', 'Network peering', 'knowledge',
    'An arrangement in which two networks connect directly to exchange traffic between their own customers, usually without paying each other for transit.',
    'A networking topic.')

NEW(107, 'Pega Certified Business Architect', 'Pega Certified Business Architect', 'credential',
    'A certification from Pega Systems for business architects and analysts who capture requirements and design case lifecycles in Pega applications.',
    'A vendor certification; agrees with the legacy certification list.',
    cert=True, scope='single-issuer')

NEW(108, 'Pega Certified Decisioning Consultant', 'Pega Certified Decisioning Consultant', 'credential',
    "A certification from Pega Systems for specialists who design decision strategies and next-best-action logic in Pega's decisioning products.",
    'A vendor certification; agrees with the legacy certification list.',
    cert=True, scope='single-issuer')

NEW(109, 'Pega Certified Lead System Architect', 'Pega Certified Lead System Architect', 'credential',
    "The highest certification in Pega Systems' architect path, for architects who design large, enterprise-scale Pega applications.",
    'A vendor certification; agrees with the legacy certification list.',
    cert=True, scope='single-issuer')

NEW(110, 'Pega Certified Senior System Architect', 'Pega Certified Senior System Architect', 'credential',
    'A certification from Pega Systems, above System Architect, for developers who design and build more complex Pega applications.',
    'A vendor certification; agrees with the legacy certification list.',
    cert=True, scope='single-issuer')

NEW(111, 'Pega Certified System Architect', 'Pega Certified System Architect', 'credential',
    'A certification from Pega Systems for developers who build and configure Pega applications; the entry level of its architect path.',
    'A vendor certification; agrees with the legacy certification list.',
    cert=True, scope='single-issuer')

UNS(112, 'Pegasus',
    'Many unrelated products and projects share this name (a workflow system, a spyware, an email client, accounting software); the term does not say which.')

NEW(113, 'Pelvic Floor', 'Pelvic floor', 'knowledge',
    'The muscles and connective tissue at the base of the pelvis that support the bladder, bowel and, in women, the uterus.',
    'An anatomy topic, like the existing nervous-system entry.')

NEW(114, 'Pelvic Floor Rehabilitation', 'Pelvic floor rehabilitation', 'skill',
    'Therapy, such as exercises and biofeedback, that retrains the pelvic floor muscles to treat problems like incontinence and pelvic pain.',
    'A physiotherapy skill.')

NEW(115, 'Pelvic Health', 'Pelvic health', 'knowledge',
    'The care of the pelvic organs and muscles, including bladder, bowel and sexual function, pregnancy-related changes and pelvic pain.',
    'A health-care practice area.')

NEW(116, 'Penology', 'Penology', 'knowledge',
    'The study of punishment for crime and of the management and rehabilitation of prisoners.',
    'A recognised field within criminology.')

NAS(117, 'Performance Indicator', 'A generic measure, not a skill; developing and tracking indicators would be.')

UNS(118, 'Performance Monitor',
    'Could mean the Windows Performance Monitor tool or any performance-monitoring software or role; the term alone does not say.')

UNS(119, 'Performance Prediction',
    'Used in machine learning, computer architecture and sports analytics with different meanings; the term gives no context.')

NEW(120, 'Performanceanalytics', 'PerformanceAnalytics', 'library',
    'An R package of functions for analysing the performance and risk of financial portfolios, such as returns, drawdowns and risk-adjusted ratios.',
    'The one-word form matches the R package name; the ServiceNow product is written with a space.')

NAS(121, 'Perimeter', 'A generic word (a boundary or a length), not a skill.')

NEW(122, 'Perinatology', 'Perinatology', 'knowledge',
    'The branch of medicine that cares for mothers and babies around the time of birth, especially in high-risk pregnancies.',
    'A medical specialty.')

NEW(123, 'Perioperative', 'Perioperative care', 'knowledge',
    'The care of a patient before, during and after surgery.',
    'The adjective names the period around surgery; perioperative care is the practice area.')

NAS(124, 'Peripheral', 'A generic adjective or noun, not a skill.')

UNS(125, 'Periscope',
    'Could be the optical device, the Twitter streaming app or Periscope Data analytics; the term alone does not say.')

NEW(126, 'Periscope Data (BI Software)', 'Periscope Data', 'platform',
    'A cloud data-analytics platform that lets analysts run SQL, Python and R against company data and build dashboards.',
    'A named business-intelligence product.')

NEW(127, 'Periscope (Social Media)', 'Periscope', 'platform',
    'A live video-streaming app owned by Twitter, which Twitter shut down in 2021.',
    'A named social media app.')

NEW(128, 'Permit To Work (PTW)', 'Permit to work', 'method',
    'A formal written system that authorises specific hazardous work, such as hot work or confined-space entry, only after the hazards are checked and controls are set.',
    'A workplace safety procedure for authorising jobs.',
    note='A permit to work authorises one job and is not a credential attested to a person by an official body.')

NAS(129, 'Perpendicular', 'A generic geometry word, not a skill.')

NEW(130, 'Personal Communications Services', 'Personal Communications Service', 'knowledge',
    'A class of digital wireless telephone services in the US, operating in the 1.9 GHz band and licensed by the Federal Communications Commission from the 1990s.',
    'A named telecommunications service class.')

NAS(131, 'Personal Grooming', 'A generic personal attribute or care task, not a skill.')

NEW(132, 'Personal Income Tax', 'Personal income tax', 'knowledge',
    "The tax charged on an individual's income, such as wages, interest and investment gains.",
    'A tax topic used in preparation and advisory work.')

UNS(133, 'Personal Injury',
    'Could mean the legal practice area or a kind of injury; the term alone does not say.')

NEW(134, 'Personal Printer Data Stream', 'Personal Printer Data Stream', 'standard',
    "IBM's command set for controlling its printers, also supported by some other makers' printers in an emulation mode.",
    'A named printer command set; the kind is the least certain part.')

NAS(135, 'Personal Profiles', 'A generic résumé or social-media term, not a skill.')

NEW(136, 'Personal Protective Equipment', 'Personal protective equipment', 'tool',
    'Clothing and gear, such as gloves, masks, goggles and hard hats, worn to protect against workplace hazards.',
    'A safety equipment category, like the existing Adaptive equipment entry.',
    variants=['PPE'])

UNS(137, 'Personal Security',
    'Could mean close protection of a person or an individual\'s own information security; the term alone does not say.')

NEW(138, 'Personalization', 'Personalization', 'method',
    "Tailoring content, products or experiences to individual users based on their data or behaviour.",
    'A marketing and product-design approach.')

NEW(139, 'Pest Analysis', 'PEST analysis', 'method',
    'A framework for reviewing the political, economic, social and technological factors that affect a business.',
    'A standard business-analysis framework.')

NEW(140, 'Pet Insurance', 'Pet insurance', 'knowledge',
    'Insurance that pays all or part of the veterinary costs when a pet is ill or injured.',
    'An insurance product area, like the existing insurance entries.')

NEW(141, 'Pet Insurance Sales', 'Pet insurance sales', 'skill',
    'Selling pet insurance policies to customers.',
    'A sales skill.')

NEW(142, 'Petrography', 'Petrography', 'knowledge',
    'The branch of geology that describes and classifies rocks by their mineral content and texture, usually under a microscope.',
    'A recognised geology specialty.')

NEW(143, 'Phalcon', 'Phalcon', 'framework',
    'A PHP web framework delivered as a compiled C extension, for speed and low resource use.',
    'A named PHP framework.')

NEW(144, 'Phantomjs', 'PhantomJS', 'tool',
    'A headless web browser scripted with JavaScript, used for automated testing and page rendering, which is no longer actively developed.',
    'A named tool.')

NEW(145, 'Pharmaceutical Batch Documentation', 'Pharmaceutical batch documentation', 'skill',
    'Preparing, completing and reviewing the batch records that show how each batch of a medicine was made, tested and released.',
    'A good-manufacturing-practice documentation skill.')

NEW(146, 'Pharmacist License', 'Pharmacist license', 'credential',
    'A licence, issued by a state or national board of pharmacy, that legally permits a person to practise as a pharmacist.',
    'A professional licence, like the existing Nurse licensure entry.',
    variants=['Pharmacist licensure'], cert=True, scope='many-issuers')

NEW(147, 'Pharmacogenetics', 'Pharmacogenetics', 'knowledge',
    "The study of how a person's inherited genetic differences affect their response to drugs.",
    'A recognised scientific field.')

NEW(148, 'Pharmacoinformatics', 'Pharmacoinformatics', 'knowledge',
    'The use of computing and data analysis to study drugs, how they act in the body and how they are used.',
    'A recognised informatics field; its exact scope varies by source.')

NEW(149, 'Pharmacy Operations', 'Pharmacy operations', 'skill',
    'Running the day-to-day work of a pharmacy, such as dispensing, inventory, billing and staffing.',
    'A pharmacy management skill.')
