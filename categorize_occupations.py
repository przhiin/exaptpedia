import json
import re

# Your data - Fixed the data structure (removed extra brackets)
data = [
  {
    "name": "A. PONNUCHAMY",
    "occupation": "President, Tamil Social and Cultural Association",
    "phone": "39652663",
    "email": "ponnu@batelco.com.bh"
  },
  {
    "name": " A.H.NIZAM ",
    "occupation": "Founder & Managing Director,Inco Designs W.L.L",
    "phone": "33277991",
    "email": "info@incodesigns.com"
  },
  {
    "name": "A.M.GANI",
    "occupation": "Director, Green Electrofit W.L.L",
    "phone": "33322762",
    "email": "amgani5@gmail.com"
  },
  {
    "name": "A.P.FAISAL",
    "occupation": " Sales Manager, Mooza Toys,Vice President, KMCC Bahrain",
    "phone": "39841984",
    "email": "apfaisal666@gmail.com"
  },
  {
    "name": "ABBAS ZAKIYUDDIN",
    "occupation": "Manager, A. A. Kothambawala Co.",
    "phone": "36452152",
    "email": "abbas@kothambawala.com"
  },
  {
    "name": "ABDUL BASHAT (BASHEER)",
    "occupation": "Managing Director, Royal Glass Co. W.L.L; Diamond Line Aluminium Powder Coating Factory W.L.L.; New Real Glasses Co. W.L.L",
    "phone": "38382747",
    "email": "diamondaluminium2013@gmail.com"
  },
  {
    "name": "ABDUL GHAFFAR BUTT",
    "occupation": "Businessman, Haa Meem Tailoring",
    "phone": "33045183",
    "email": "buttabdulghaffar@gmail.com"
  },
  {
    "name": "DR. ABDUL GAFFAR SHAIKH AHMED",
    "occupation": "Senior Consultant, Orthopedic & Trauma Surgeon",
    "phone": "39611278",
    "email": "abgaf.saheb@gmail.com"
  },
  {
    "name": "ABDUL RAHMAN KUNNUMMAL",
    "occupation": "Managing Director, Aseel Supermarkets W.L.L",
    "phone": "39678075",
    "email": "aseelrahman@gmail.com"
  },
  {
    "name": "ABDUL RASHID RANA",
    "occupation": "Chairman, Crystal Trading W.L.L.; Vice President, Bahrain Pakistan Friendship Society",
    "phone": "39679229",
    "email": "ranarashid73@hotmail.com"
  },
  {
    "name": "ABDUL JAVAD PASHA",
    "occupation": "Core Committee Member, Indian Community Relief Fund",
    "phone": "39337866",
    "email": "javad222013@hotmail.com"
  },
  {
    "name": "ABDUL HANNAN",
    "occupation": "Managing Director, Ad Mart Trading W.L.L.",
    "phone": "33510522",
    "email": "admarttrading@gmail.com"
  },
  {
    "name": "ABDUL MANSHEER",
    "occupation": "Vice President, Muharraq Malayali Samajam",
    "phone": "34135124",
    "email": "mansheerk@gmail.com"
  },
  {
    "name": "ABDUL SAHEER",
    "occupation": "",
    "phone": "33197315",
    "email": "abdulsaheer123@gmail.com"
  },
  {
    "name": "ABDUL RAHIMAN",
    "occupation": "Branch Manager, Bahrain Express Travel & Tours W.L.L.",
    "phone": "37733583",
    "email": "salam.elegancehometrading@gmail.com"
  },
  {
    "name": "ABDUL SALAM A.P.",
    "occupation": "General Manager, Elegance Home",
    "phone": "37733583",
    "email": "salam.elegancehometrading@gmail.com"
  },
  {
    "name": "DR. ABRAHAM GEORGE",
    "occupation": "Orthopaedic Surgeon, Al Hilal Hospital, Adliya",
    "phone": "39842024",
    "email": "ageorge79@gmail.com"
  },
  {
    "name": "ABRAHAM JOHN",
    "occupation": "",
    "phone": "37111695",
    "email": ""
  },
  {
    "name": "ACHU ARUN RAJ",
    "occupation": "Branding Head, OPPO Bahrain; Creative Director, Branding Designer Filmmaker and Actor",
    "phone": "36104315",
    "email": "raj4arun@gmail.com"
  },
  {
    "name": "ADNAN MUSTAFA",
    "occupation": "Director, Pushcord Technology W.L.L.; Moda Vestir Boutique W.L.L.",
    "phone": "36074003",
    "email": "adnan@cordis.us"
  },
  {
    "name": "AINUL HOQUE",
    "occupation": "Managing Director, Adnan Gate Contracting W.L.L; Ayefsha Real Estate S.P.C; Member of Board, Linnas Medical Center; Vice Chairman, Linnas Travels & Tourism; Managing Partner, Al Shafi Rent A Car; Kite Trading Co. W.L.L",
    "phone": "33243392",
    "email": "ainul.bh@gmail.com"
  },
  {
    "name": "AKSHAY KHANDELWAL",
    "occupation": "Chief Executive Officer, Nuetel Communications BSC",
    "phone": "33106767",
    "email": "akshay.khandelwal@nue-tel.com"
  },
  {
    "name": "AJAY KUMAR CHETTUVETTY",
    "occupation": "Chartered Accountant",
    "phone": "39800143",
    "email": "ajikumar35@gmail.com"
  },
  {
    "name": "AJAY KUMAR CHETTUVETTY",
    "occupation": "Chartered Accountant",
    "phone": "39980232",
    "email": "ajaykckn@gmail.com"
  },
  {
    "name": "AJAYAKRISHNAN. V",
    "occupation": "Former Director Board Member, The Indian School; Director, Exxon Facilities Co. W.L.L.",
    "phone": "38287840",
    "email": "ajayakrishnanmvk@gmail.com"
  },
  {
    "name": "AJIKUMAR BALABHADRAN",
    "occupation": "General Manager, Zarwan Fiberglass Factory W.L.L. Bahrain",
    "phone": "39125578",
    "email": "ajuno3@hotmail.com"
  },
  {
    "name": "AJAY KUMAR V N",
    "occupation": "Football, Cricket, Hockey Secretary, The Indian Club",
    "phone": "39613858",
    "email": "ajithprasad06@gmail.com"
  },
  {
    "name": "AJITH PRASAD. K",
    "occupation": "Machinist, Bahrain Airport Services",
    "phone": "39613858",
    "email": "ajithprasad06@gmail.com"
  },
  {
    "name": "ALI GOKASLAN",
    "occupation": "Manager and Partner, Al Naeem Al Aali Restaurant Co.WLL.",
    "phone": "39622231",
    "email": "alnaeemali@gmail.com"
  },
  {
    "name": "ALISHBA FAISAL",
    "occupation": "Director, 786 Marketing & Event W.L.L.; Right Way W.L.L",
    "phone": "37226082",
    "email": "alishba@786marketingevent.co"
  },
  {
    "name": "ALWYN D'SOUZA",
    "occupation": "Sports Secretary, Karnataka Social Club",
    "phone": "36999564",
    "email": "alwynjeni@gmail.com"
  },
  {
    "name": "DR. AMARJIT KAUR SANDHU",
    "occupation": "Medical Consultant & Associate Professor, Arabian Gulf University; Al-Kindi Hospital & Salmaniya Medical Complex",
    "phone": "39808874",
    "email": "sandhuak@gmail.com"
  },
  {
    "name": "DR. AMENA EBRAHIM MALIK",
    "occupation": "Consultant Advisor to the CEO, National Health Regulatory Authority",
    "phone": "",
    "email": "amena.malik@nhra.bh"
  },
  {
    "name": "AMENA SALTANAT SHAHRUKH LALI",
    "occupation": "Founder & CEO, Fitness 365 Dance workout and Wellness Studio; Founder & Director, Shahzaib's Clubhouse",
    "phone": "39571334",
    "email": "Info@fitness365bahrain.com"
  },
  {
    "name": "AMER MAHMOOD KHALID",
    "occupation": "Financial Controller, Nestle Waters",
    "phone": "39980525",
    "email": "aamiraca@gmail.com"
  },
  {
    "name": "AMIT JAISWAL",
    "occupation": "Project Director/ Owner, Watercolor Interiors Middle East W.L.L.",
    "phone": "36557788",
    "email": "projects@watercolorme.com"
  },
  {
    "name": "AMIT KUMAR",
    "occupation": "Chief Executive Officer, State Bank of India, Retail Branch Bahrain",
    "phone": "33032792",
    "email": "ceo.rbbh@statebank.com"
  },
  {
    "name": "AMIT MEHTA",
    "occupation": "Social Worker",
    "phone": "36885333",
    "email": ""
  },
  {
    "name": "AMRITA CHATTERJEE",
    "occupation": "Public Relations & Marketing Consultant (Independent)",
    "phone": "36209719",
    "email": "amrita.s.chatterjee@gmail.com"
  },
  {
    "name": "ANAND KUMAR",
    "occupation": "Production Manager, Aztec Services W.L.L.",
    "phone": "33435365",
    "email": "akumar@aztec-gulf.com"
  },
  {
    "name": "ANAND LOBO",
    "occupation": "President, Karnataka Social Club; Founder Member, Kudlothsava",
    "phone": "34345000",
    "email": "loboanand@yahoo.com"
  },
  {
    "name": "ANAND SUBRAMANIAM",
    "occupation": "Group Chief Investment & Financial Officer, Bahrain National Holding Co. B.S.C.",
    "phone": "17587330",
    "email": "anand.subramaniam@bnhgroup.com"
  },
  {
    "name": "ANIL KUMAR R",
    "occupation": "General Secretary, The Indian Club",
    "phone": "39623936",
    "email": "akumarrajan@gmail.com"
  },
  {
    "name": "ANISH DAS ROY",
    "occupation": "Managing Partner, Millennial HR",
    "phone": "39629197",
    "email": "anish@mc2hr.com"
  },
  {
    "name": "ANISH VARGHESE",
    "occupation": "Proprietor, V Star Embroidery and Tailoring",
    "phone": "39899300",
    "email": "vstarembah16@gmail.com"
  },
  {
    "name": "ANISUR RAHMAN",
    "occupation": "Managing Director, ARM Group",
    "phone": "33226658",
    "email": "anisur@armtrading.net"
  },
  {
    "name": "ANITA KURUVILLA",
    "occupation": "Managing Director, MTM Trading Company W.L.L.",
    "phone": "39137753",
    "email": "mtmclts@batelco.com.bhm"
  },
  {
    "name": "ANJALI SHAH",
    "occupation": "Managing Director, Mayball Solutions W.L.L.",
    "phone": "33351538",
    "email": "anjali@mayballsolutions.com"
  },
  {
    "name": "ANJU SIVADASS",
    "occupation": "Founder, Smart Kid's Education Support W.L.L.",
    "phone": "33006543",
    "email": "mails.anjusivadass@gmail.com"
  },
  {
    "name": "ANOOP KRISHNAN",
    "occupation": "Operations Manager, Wellflow Gulf Trading W.L.L.",
    "phone": "36313242",
    "email": "a.krishnan@outlook.com"
  },
  {
    "name": "ANSILLA V. RAJAN",
    "occupation": "Managing Director, Perform Better Fitness",
    "phone": "39268852",
    "email": "ansillar@gmail.com"
  },
  {
    "name": "ANSON P. ISAAC",
    "occupation": "Secretary, St. Peter's Jacobite Syrian Orthodox Church",
    "phone": "39312185",
    "email": "stpeters@batelco.com.bh"
  },
  {
    "name": "ANUP ASHOK VELHAL",
    "occupation": "General Secretary, Maharashtra Cultural Society",
    "phone": "39460115",
    "email": "anup.vehlal@yahoo.com"
  },
  {
    "name": "ARSALAN MOHAMMAD ANWAR",
    "occupation": "CEO and Founder, Arsalan Anwar Consulting W.L.L.; Director, AMZ Accounting W.L.L.; Green Grid Co. W.L.L.",
    "phone": "39839312",
    "email": "arsalan.anwar5@gmail.com"
  },
  {
    "name": "ARJUN BURMAN",
    "occupation": "General Manger - Finance, Nasser Saeed Al Hajri Corporation W.L.L. & Gulf Asia Contracting Company W.L.L.",
    "phone": "37205206",
    "email": "arjun.burman@gulfasiallc.com"
  },
  {
    "name": "ARUN K. JOSE",
    "occupation": "Indoor Games Secretary, The Indian Club",
    "phone": "39539946",
    "email": "kjosearun@gmail.com"
  },
  {
    "name": "ARULDAS KALARICKAL THOMAS",
    "occupation": "General Manager, iPoint; UniData; Business International Xerox",
    "phone": "39863008",
    "email": "aruldas.thomas@gmail.com"
  },
  {
    "name": "ARUN GOVIND",
    "occupation": "CEO, ARHC Consultants LLP",
    "phone": "36499739",
    "email": "arg@arg.io"
  },
  {
    "name": "DR. ARUN RAJ",
    "occupation": "Alternative medicine practitioner, Sherry Group; Sherry Wellness and Alternative Center",
    "phone": "66762007",
    "email": "arunrajknply@gmail.com"
  },
  {
    "name": "ARUNACHALAM T.",
    "occupation": "Badminton Secretary, The Indian Club",
    "phone": "35007544",
    "email": "arun_cad_3@hotmail.com"
  },
  {
    "name": "ASAINAR KALATHINGAL",
    "occupation": "General Secretary, Kerala Muslim Cultural Centre",
    "phone": "33452334",
    "email": "asainar2000@gmail.com"
  },
  {
    "name": "DR. ASHA PRADEEP",
    "occupation": "Specialist Radiologist, Aster Clinic",
    "phone": "38220570",
    "email": "deepash273@gmail.com"
  },
  {
    "name": "ASHESH MUKHOPADHYAY",
    "occupation": "Director, Gulf Business Machines",
    "phone": "",
    "email": "ashesh_mukhopadhyay@yahoo.com"
  },
  {
    "name": "ASHRAF KAKKANDI",
    "occupation": "Managing Director, Riya Travel & Tours BPC",
    "phone": "39416767",
    "email": "md@riyatravelbh.com"
  },
  {
    "name": "ATAMJEET SINGH BAWA",
    "occupation": "Paper Artist; Principal, Paper Modeller",
    "phone": "34602328",
    "email": "hi@papermodel.guru"
  },
  {
    "name": "DR. ATHULYA UNNIKRISHNAN",
    "occupation": "Alternative Medical Practitioner, Middle East Medical Center; Santhigiri Ayurvedic Center",
    "phone": "34104951",
    "email": "athulyausa@gmail.com"
  },
  {
    "name": "ATTIQ UR REHMAN",
    "occupation": "Principal, Pakistan School",
    "phone": "33749697",
    "email": "atrqureshi345@yahoo.com"
  },
  {
    "name": "DR. ATUL DESHMUKH",
    "occupation": "Sr. Economist, Ministry of Housing & Urban Planning",
    "phone": "66601514",
    "email": "atulvd@housing.gov.bh"
  },
  {
    "name": "ATUL P. SHINDE",
    "occupation": "Senior Manager, Awal Gulf Manufacturing Co.",
    "phone": "",
    "email": "atulss2004@gmail.com"
  },
  {
    "name": "AYESHA ADNAN",
    "occupation": "CEO, Alaroob Trends & Styles",
    "phone": "33982611",
    "email": "ashooadnan@gmail.com"
  },
  {
    "name": "DR. BABU RAMACHANDRAN",
    "occupation": "Medical Doctor/Head, Amwaj Medical and Wellness Centre & Antismoking Clinic; American Mission Hospital",
    "phone": "39430708",
    "email": "drbabuamh@gmail.com"
  },
  {
    "name": "BAIJU KRISHNAN",
    "occupation": "Sales & Technical Support Engineer, Khayber Fire & Security Systems W.L.L.",
    "phone": "39976946",
    "email": "baijukrishnan72@gmail.com"
  },
  {
    "name": "DR. BENROY BENTAL DAISY",
    "occupation": "Specialist Dermatologist, American Mission Hospital",
    "phone": "39501831",
    "email": "bdbenroy@yahoo.com"
  },
  {
    "name": "BERNARD DE VILLELE",
    "occupation": "General Manager, The Ritz-Carlton, Bahrain",
    "phone": "17580000",
    "email": "bernard.devillele@ritzcarlton.com"
  },
  {
    "name": "BHAGWAN L. ASARPOTA",
    "occupation": "Secretary, Thattai Hindu Community",
    "phone": "39691500",
    "email": "bhagwan@haridasp.com"
  },
  {
    "name": "BIJOY KAMBRATH",
    "occupation": "Assistant Treasurer, The Indian Club",
    "phone": "39025573",
    "email": "crpbijoy@gmail.com"
  },
  {
    "name": "BIJU JACOB",
    "occupation": "Director - Digital Business NEC",
    "phone": "13311221",
    "email": "biju.jacob@nec.bh"
  },
  {
    "name": "BIPLAB SAHA",
    "occupation": "Vice President, Bengal Cultural Society, Bahrain",
    "phone": "35617336",
    "email": "biplabsaha778@gmail.com"
  },
  {
    "name": "BIRTHE VAN DER HEIJDEN",
    "occupation": "Founder, OneHeartBahrain; CEO, OneHeartEarth, Manama & Ras Al Khaimah (UAE)",
    "phone": "33872346",
    "email": "birthe@oneheartbahrain.com"
  },
  {
    "name": "BOBAN IDICULLA",
    "occupation": "Director, The Daily Tribune",
    "phone": "39456914",
    "email": "bobkon82@gmail.com"
  },
  {
    "name": "BRIAN JOSEPH",
    "occupation": "General Manager, Monroe Hotel Bahrain",
    "phone": "38788600",
    "email": "gm@monroehotelbh.com"
  },
  {
    "name": "C.M.JUNITH",
    "occupation": "CEO, Sport Hub W.L.L.; Head of Operations, Gulf Badminton Academy",
    "phone": "66359777",
    "email": "junithcm@gmail.com"
  },
  {
    "name": "CALVIN FERNANDO",
    "occupation": "Country Manager, Binzagr",
    "phone": "35573153",
    "email": "calvin.fernando@binzagr.com.sa"
  },
  {
    "name": "CASSIUS CAMILO PEREIRA",
    "occupation": "President, The Indian Club",
    "phone": "39660475",
    "email": "cassius.929@hotmail.com"
  },
  {
    "name": "ÇETIN YURTTAŞER",
    "occupation": "Director, Kuwait-Turkish Participation Bank Inc. Bahrain Wholesale Branch",
    "phone": "39473771",
    "email": "Cetin.Yurttaser@kuveytturk.com"
  },
  {
    "name": "CHANDRAMOHANAN P.V.",
    "occupation": "Managing Director, ME Trade Company W.L.L.",
    "phone": "39941043",
    "email": "md@metradebh.com"
  },
  {
    "name": "CHEMBAN JALAL",
    "occupation": "Managing Director, Euro Steel General Trading W.L.L.",
    "phone": "39574557",
    "email": "chembanjalal@gmail.com"
  },
  {
    "name": "CHERIAN VARGHESE",
    "occupation": "CEO & Founder, VIN Technology Systems W.L.L.",
    "phone": "34688877",
    "email": "cherian@vin-systems.com"
  },
  {
    "name": "DR. CHITRA SINHA",
    "occupation": "Author and Academic",
    "phone": "37762112",
    "email": "sinhachitra@gmail.com"
  },
  {
    "name": "CINSON CHACKO PULIKOTTIL",
    "occupation": "Senior Civil Engineer, Ayman Yousif Engineer",
    "phone": "36255292",
    "email": "cinsonchacko@gmail.com"
  },
  {
    "name": "CLARENCE D'SOUZA",
    "occupation": "Former Secretary, Karnataka Social Club",
    "phone": "38854693",
    "email": "clarencedsouza19@gmail.com"
  },
  {
    "name": "CLAUDE WIJESINGHE",
    "occupation": "Executive Housekeeper, Wyndham Garden",
    "phone": "66398010",
    "email": "claude.wijesinghe@wyndhamgardenmanama.com"
  },
  {
    "name": "CLETUS RODRIGUES",
    "occupation": "Vice President, Karnataka Social Club",
    "phone": "39635321",
    "email": "clitey43@gmail.com"
  },
  {
    "name": "CLIVE BRITTO",
    "occupation": "Asst. General Secretary, Karnataka Social Club",
    "phone": "36811874",
    "email": "clive_britto@yahoo.com"
  },
  {
    "name": "CONALD VEIGAS",
    "occupation": "Internal Auditor, Karnataka Social Club",
    "phone": "36434275",
    "email": "conaldveigas@gmail.com"
  },
  {
    "name": "D.V.SIVAKUMAR",
    "occupation": "Supervisor, M.O.Interior",
    "phone": "39895971",
    "email": "dvsivakumar9724@gmail.com"
  },
  {
    "name": "DEBANIK PAUL",
    "occupation": "Convener, Bengal Cultural Society, Bahrain",
    "phone": "39161206",
    "email": "debanikp@yahoo.com"
  },
  {
    "name": "DEVAL MEHTA",
    "occupation": "Social Worker",
    "phone": "36885333",
    "email": ""
  },
  {
    "name": "DEEPAK YASHWANT GHANEKAR",
    "occupation": "Project Director, Gulf House Engineering",
    "phone": "39382607",
    "email": "deeprag5355@gmail.com"
  },
  {
    "name": "DR. DEVPAL PATIL",
    "occupation": "Consultant Gen & Laparoscopic Surgery, Ibn Al Nafees Hospital",
    "phone": "39672008",
    "email": "devpalpatil1@gmail.com"
  },
  {
    "name": "ADV. DHANASHREE HRISHIKESH DUNAKHE",
    "occupation": "Freelance legal counselor, Astrologer, Teacher",
    "phone": "39295469",
    "email": "dhanashreehdunakhe@gmail.com"
  },
  {
    "name": "DIL AFSAR",
    "occupation": "Director, IConstruct Co. W.L.L.",
    "phone": "39453686",
    "email": "iconstruct.co@gmail.com"
  },
  {
    "name": "DILAWAR KHAN",
    "occupation": "Managing Director, Superb Events",
    "phone": "38098999",
    "email": "tents.superb@gmail.com"
  },
  {
    "name": "REV. DILEEP DAVIDSON MARK",
    "occupation": "Vicar, The Bahrain Malayalee CSI Parish",
    "phone": "38077979",
    "email": "dileepdavidson@gmail.com"
  },
  {
    "name": "DILIP KUMAR VAYA",
    "occupation": "Social Worker",
    "phone": "39872494",
    "email": ""
  },
  {
    "name": "DR. DIVYA DEV",
    "occupation": "General Physician, Middle East Medical Center",
    "phone": "38702426",
    "email": "divyad87@gmail.com"
  },
  {
    "name": "DOMINIC MANUEL",
    "occupation": "General Secretary, Bengal Cultural Society, Bahrain",
    "phone": "33261206",
    "email": "dominic.lochlan@gmail.com"
  },
  {
    "name": "ADV. DOMINY EAPEN",
    "occupation": "General Manager, Riyada Solution; Legal Consultant for Indian expatriates",
    "phone": "39148491",
    "email": "advdominic7@gmail.com"
  },
  {
    "name": "DR. DONNEL DON BOSCO",
    "occupation": "Senior Emergency Physician, King Hamad American Mission Hospital",
    "phone": "38745208",
    "email": "dr.donbosco86.bh@gmail.com"
  },
  {
    "name": "DUSHAN KANCHANA GODAGE",
    "occupation": "Finance and Human Resources Manager, Faalyat W.L.L.",
    "phone": "39215980",
    "email": "dushan@faalyat.com"
  },
  {
    "name": "DURGADAS PANJIKAYIL",
    "occupation": "Showroom In-Charge, Bahrain Gas",
    "phone": "39267759",
    "email": "durgadasp@hotmail.com"
  },
  {
    "name": "EDATHODY BHASKARAN",
    "occupation": "Director, Adler Westpoint Co. W.L.L.",
    "phone": "39230363",
    "email": "sales@adlerwestpoint.com"
  },
  {
    "name": "EKTA MEHTA",
    "occupation": "Member, Indian Ladies Association",
    "phone": "66998133",
    "email": "ekta_bm@yahoo.com"
  },
  {
    "name": "ELIAS",
    "occupation": "Managing Director, Matha Middle East Advertising; Marvel - Gift and Promotion",
    "phone": "35650829",
    "email": "mathawll@gmail.com"
  },
  {
    "name": "EYAD ABDELMAJEED ABU TALEB",
    "occupation": "Legal Advisor, Kanoo",
    "phone": "36288870",
    "email": "eyadabutaleb2020@gmail.com"
  },
  {
    "name": "FAHAD SADEQ",
    "occupation": "CEO, Group Financial & Development Director, Suha Investments",
    "phone": "17722211",
    "email": "info@suhainvestments.com"
  },
  {
    "name": "FAHAD TARIQ",
    "occupation": "Marketing Specialist/ Home Remittance & NRP Banking, United Bank Limited",
    "phone": "66366705",
    "email": "fahad_tariq@ublint.com"
  },
  {
    "name": "FAIZEL REHMAN",
    "occupation": "Director, Maxstar Uniforms; Pulito Laundry",
    "phone": "38267447",
    "email": "maxstaruniforms@gmail.com"
  },
  {
    "name": "FATHIMA SAHLA",
    "occupation": "Accounting Assistant, Al Amir Custom Clearing",
    "phone": "33065360",
    "email": "fathimasahlaa.99@gmail.com"
  },
  {
    "name": "FAYYAZ AHMAD CHAUDHARY",
    "occupation": "General Manager, Super Fire & Safety Services W.L.L",
    "phone": "39044901",
    "email": "fayyaz@superfiresafety.com"
  },
  {
    "name": "FAZALULHAQ",
    "occupation": "General Manager, Outlook WLL",
    "phone": "39710151",
    "email": "fazalpm@gmail.com"
  },
  {
    "name": "FRANCIS KAITHARATH",
    "occupation": "Chairman & MD, IMAC Bahrain Media City W.L.L.",
    "phone": "39834729",
    "email": "franisha@hotmail.com"
  },
  {
    "name": "GANAPATHY NARAYANAN",
    "occupation": "Treasury Manager, Bahrain National Holding Company B.S.C.",
    "phone": "39848590",
    "email": "gananara@gmail.com"
  },
  {
    "name": "GEORGE E. CHERIAN",
    "occupation": "Managing Director, Maximum Effort Co. W.L.L.",
    "phone": "36366500",
    "email": "georgecher@gmail.com"
  },
  {
    "name": "GEORGE ISSA",
    "occupation": "Executive Assistant Manager, Golden Tulip Bahrain Hotel - Louvre Hotels Group",
    "phone": "39995140",
    "email": "eam@goldentulipbahrain.com"
  },
  {
    "name": "GEORGEKUTTY THOMAS",
    "occupation": "General Manager, Heavy Equipment Parts & TBLE Division, Y.K. Almoayyed & Sons",
    "phone": "36440888",
    "email": "george@almoayyed.com"
  },
  {
    "name": "GERARD M. FERNANDES",
    "occupation": "Director, One Vision For Consultancy W.L.L.",
    "phone": "17231302",
    "email": "gerard@1visionconsultancy.com"
  },
  {
    "name": "GIRISH BABU (GB)",
    "occupation": "Executive Director, Heat Master W.L.L., Alko Industries W.L.L., Fab Master W.L.L.",
    "phone": "33526667",
    "email": "gb@heatmasterint.com"
  },
  {
    "name": "GOPAKUMAR P.R.",
    "occupation": "Assistant General Secretary, The Indian Club",
    "phone": "39279570",
    "email": "gops789@hotmail.com"
  },
  {
    "name": "GOPINATHAN PRADEEP KUMAR",
    "occupation": "Chairman, Delta Electrical Items W.L.L.",
    "phone": "39135389",
    "email": "sales@deltaelectricals.com"
  },
  {
    "name": "GOVIND C. JOSHI",
    "occupation": "Service / Proposals Manager, Arab Shipbuilding and Repair Yard Co. (ASRY), Hidd",
    "phone": "36287318",
    "email": "govindc@asry.net"
  },
  {
    "name": "GURCHARAN SINGH",
    "occupation": "Senior General Manager, M/S Ebrahim Khalil Kanoo",
    "phone": "39466403",
    "email": "sihry57@hotmail.com"
  },
  {
    "name": "GURMAIL SINGH",
    "occupation": "President, Sikh Community Center Gurdwara",
    "phone": "39208388",
    "email": "gurmailsingh.msceb@gmail.com"
  },
  {
    "name": "DR. GURPREET KAUR",
    "occupation": "Former Sec. Activities, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "HABEEB RAHMAN",
    "occupation": "Director, Chief Executive Officer, Shifa Al Jazeera Hospital & Medical centres; President, Kerala Muslim Cultural Centre",
    "phone": "39000035",
    "email": "habeebak2002@gmail.com"
  },
  {
    "name": "HAMZA MOHAMMED",
    "occupation": "President, Indian Islahi Centre",
    "phone": "33307835",
    "email": "hamzapappurath@gmail.com"
  },
  {
    "name": "HANSUL GANI",
    "occupation": "Classical Dance Teacher & Choreographer",
    "phone": "33381762",
    "email": "hansulgani@gmail.com"
  },
  {
    "name": "HARSH VIRENDRA BHATIA",
    "occupation": "Managing Director, Oilfield & Technical Supplies Centre W.L.L.",
    "phone": "36455400",
    "email": "harsh@otsc.bh"
  },
  {
    "name": "HEMENDRA SWAROOP",
    "occupation": "Chief Operating Officer, The New India Assurance Co. Ltd., Appointed Representative: The International Agencies Co. Ltd.",
    "phone": "39660494",
    "email": "coo@newindiabahrain.com"
  },
  {
    "name": "HERMAN D'SOUZA",
    "occupation": "Asst. Treasurer, Karnataka Social Club",
    "phone": "36627415",
    "email": "po_dsouza@hotmail.com"
  },
  {
    "name": "HESHAN MINDIKA",
    "occupation": "Managing Director, Gulf Wind Travel & Tours W.L.L.",
    "phone": "39464765",
    "email": "sales@gulfwindtravel.com"
  },
  {
    "name": "HETAL BHASKAR",
    "occupation": "Secretary, Shree Gujarati Samaj",
    "phone": "39879751",
    "email": "hetalbhaskar@gmail.com"
  },
  {
    "name": "HILDA ELIZABETH LOBO",
    "occupation": "Former Membership Secretary, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "HITESH SIKKA",
    "occupation": "Managing Director, Yellow Paint International Media Services W.L.L.",
    "phone": "38883904",
    "email": "sales@yellowpaintmedia.com"
  },
  {
    "name": "IMRAN JAMIL",
    "occupation": "Project Manager, BFG International",
    "phone": "36111467",
    "email": "imranjamil75@gmail.com"
  },
  {
    "name": "INDIKA SANJEEWA",
    "occupation": "Head of Billing and Debt Collection, AJM Kooheji Bsc Closed",
    "phone": "39947489",
    "email": "indika@ajmkooheji.com"
  },
  {
    "name": "DR. IQBAL WARDHAWALA",
    "occupation": "Chief Resident, Emergency Department, Government Hospitals, SMC- Bahrain",
    "phone": "36923640",
    "email": "driqbalw@gmail.com"
  },
  {
    "name": "PASTOR ISAAC INAYAT",
    "occupation": "Pastor and Chairman of Urdu Language Congregation, National Evangelical Church",
    "phone": "36361244",
    "email": "isaacinayat@yahoo.com"
  },
  {
    "name": "ISHTIAQ ASHFAQ BUTT",
    "occupation": "Director, Fiddah Décor & Maintenance W.L.L.",
    "phone": "39461379",
    "email": "fiddahdecor70@hotmail.com"
  },
  {
    "name": "IVAN VAS",
    "occupation": "Tennis Secretary, The Indian Club",
    "phone": "39562444",
    "email": "anuvas2005@gmail.com"
  },
  {
    "name": "JAGADEESH P.",
    "occupation": "Shift Charge Engineer, Al Ezzel Power Station",
    "phone": "36600246",
    "email": "pjnskruti@gmail.com"
  },
  {
    "name": "JANAKA DESHAPRIYA PERERA",
    "occupation": "Chief Accountant, Lari Group, Khalil Ali Akbar Lari Group",
    "phone": "36894000",
    "email": "janaka@larigroup.com.bh"
  },
  {
    "name": "JASHIM UDDIN",
    "occupation": "Managing Director, Al Khunaizi Fish W.L.L, TSM Contracting & Clearing W.L.L",
    "phone": "33392958",
    "email": "Jashim69503@gmail.com"
  },
  {
    "name": "JASSEELA M.A.",
    "occupation": "Author, Freelance Counselor and Yoga Trainer",
    "phone": "32081101",
    "email": "bankhouse55@gmail.com"
  },
  {
    "name": "JATIN KARIA",
    "occupation": "Senior Partner, Grant Thornton Bahrain",
    "phone": "17500188",
    "email": "jatin.karia@bh.gt.com"
  },
  {
    "name": "JAYA MENON",
    "occupation": "Novelist & Cine Artist",
    "phone": "37735579",
    "email": "pragjaya@gmail.com"
  },
  {
    "name": "JAYAFAR MAIDANEE",
    "occupation": "Hon. Vice Chairman, The Indian School; Tennis Secretary, The Indian Club",
    "phone": "39716600",
    "email": "vicechairman@indianschool.bh"
  },
  {
    "name": "Jayaprakash",
    "occupation": "Chairman Sir, Tennis Secretary, The Indian Club",
    "phone": "39562444",
    "email": "anuvas2005@gmail.com"
  },
  {
    "name": "JEEBEN VARGHESE KURIAN",
    "occupation": "Director, Al Namal & VKL Group of Companies",
    "phone": "66766646",
    "email": "jeeben@al-namal.com"
  },
  {
    "name": "JEENA NIAZ",
    "occupation": "Artist (Painter)",
    "phone": "33240047",
    "email": "artofjeena@gmail.com"
  },
  {
    "name": "FR. JOHNS JOHNSON",
    "occupation": "Vicar, St. Peter's Jacobite Syrian Orthodox Church",
    "phone": "39840243",
    "email": "frjohnsjohnson@gmail.com"
  },
  {
    "name": "DR. JOHN PANACKEL",
    "occupation": "Chairman and Managing Director, Pravasi Guidance Centre W.L.L.",
    "phone": "39963855",
    "email": "john.panackel@gmail.com"
  },
  {
    "name": "JOJO MATHEWS",
    "occupation": "Salesman, Amfa Holding Company",
    "phone": "39269656",
    "email": "jojomathews27@gmail.com"
  },
  {
    "name": "JOSEPH ANDRADE",
    "occupation": "Administrative Member, Karnataka Social Club",
    "phone": "39063953",
    "email": "samariajoe@yahoo.co.uk"
  },
  {
    "name": "JOSEPH GEORGE",
    "occupation": "Real Estate Administrator, Dawani Properties",
    "phone": "39412270",
    "email": "josegeo09@yahoo.com"
  },
  {
    "name": "JOSEPH JOY",
    "occupation": "Vice President, The Indian Club",
    "phone": "39802800",
    "email": "joejoys@yahoo.com"
  },
  {
    "name": "JUSTEN JOHN",
    "occupation": "School Principal, Pakistan Urdu School",
    "phone": "36114565",
    "email": "justenjohn@hotmail.com"
  },
  {
    "name": "JYOTHISH PANICKER",
    "occupation": "Sales Manager, Global Office Supply Co. W.L.L.",
    "phone": "39091901",
    "email": "jyothishbhn@gmail.com"
  },
  {
    "name": "DR. JYOTSNA PANDIT",
    "occupation": "General Dentist, Al Jishi Specialist Dental Centre",
    "phone": "34202300",
    "email": "drjyotsna@aljishidental.com"
  },
  {
    "name": "DR. K.G. BABURAJAN",
    "occupation": "Chairman & Managing Director, BKG Holding W.L.L.",
    "phone": "17250333",
    "email": "bkgh@batelco.com.bh"
  },
  {
    "name": "K.G. DEVRAJ",
    "occupation": "Director, Kivi Management Consultancy W.L.L.",
    "phone": "39884222",
    "email": "devrajkg@hotmail.com"
  },
  {
    "name": "K.R. NAIR",
    "occupation": "Managing Director, Pegasus Trading & Construction Co. W.L.L; Partner, DELTROY Pvt. Ltd., Singapore",
    "phone": "39652009",
    "email": "krnooranad@gmail.com"
  },
  {
    "name": "K. GOPINATH MENON",
    "occupation": "Principal and Chapter Convener (Bahrain Chapter), The New Indian School W.L.L",
    "phone": "33871700",
    "email": "gopinathmenon@hotmail.com"
  },
  {
    "name": "KAMAL PERERA",
    "occupation": "Restaurant Manager, Alo & Eggstop",
    "phone": "33051779",
    "email": "kamalpereradp@gmail.com"
  },
  {
    "name": "KAMAL UDDIN AHMED",
    "occupation": "Director, Washington Suit W.L.L., Bangladesh Travels W.L.L., Miros Air Cargo Service W.L.L.",
    "phone": "36368934",
    "email": "kamalahmedlsr@gmail.com"
  },
  {
    "name": "KANJIRAKATTU MATHEW CHERIAN",
    "occupation": "Managing Director, Technoline Trading and Services W.L.L.",
    "phone": "39427425",
    "email": "kmcherian@gmail.com"
  },
  {
    "name": "KASIM PADATHAKAYIL",
    "occupation": "General Secretary, Gulf Malayalee Federation (GMF), Bahrain; Media Coordinator, Bahrain Kerala Social Forum (BKSF)",
    "phone": "33403533",
    "email": "kasim76@live.com"
  },
  {
    "name": "KALPANA D. PATIL",
    "occupation": "ICRF Regional Forum member, BAPS Ladies wing member - PR Team",
    "phone": "39650314",
    "email": "devkalp.patil@gmail.com"
  },
  {
    "name": "KATTUM THAZHA MOIDEEN",
    "occupation": "Sales and Project Technical Support, B.F.G. Commercial Services",
    "phone": "39270887",
    "email": "moideen@bfgcommercial.net"
  },
  {
    "name": "KIRAN ABHIJIT MANGLE",
    "occupation": "Former Hon. President, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "KIRAN UPADHYAYA",
    "occupation": "Engineer/Businessman",
    "phone": "33457671",
    "email": "dhyapaa@gmail.com"
  },
  {
    "name": "KISHOR P. GAIKWAD",
    "occupation": "CEO, SKG Publicity & Advertising Co. W.L.L",
    "phone": "39517565",
    "email": "kishor@skgadvertisingwll.com"
  },
  {
    "name": "KRISHAN KISHORE MATHUR",
    "occupation": "CEO/Executive Director, Ahmed Mohammed Amin Alkhaja & Sons Group",
    "phone": "39609570",
    "email": "kkishoremathur@gmail.com"
  },
  {
    "name": "KRISHNAPRIYA SUBIN",
    "occupation": "Managing Director, Design Track Prints W.L.L.",
    "phone": "33352368",
    "email": "priyasubin.bh@gmail.com"
  },
  {
    "name": "KRISHNA KUMAR D.",
    "occupation": "Chairman, Sree Narayana Cultural Society",
    "phone": "39605002",
    "email": "chairman@sncsbahrain.com"
  },
  {
    "name": "KRITHIVASAN KRISHNAMOORTHY",
    "occupation": "Managing Director, Jay Kay Consultants W.L.L.",
    "phone": "39616508",
    "email": "k.krithivasan@gmail.com"
  },
  {
    "name": "KRUPA SAGAR",
    "occupation": "Head of Business Development, Al Majarah Jewellers",
    "phone": "17214324",
    "email": "krupa@almajarahgold.com"
  },
  {
    "name": "LAKSHMIDHA ARUN",
    "occupation": "Freelancer, Fashion Designer, Stylist and Artist; Faculty, Artstationonline",
    "phone": "34367579",
    "email": "meetlakshmi82@gmail.com"
  },
  {
    "name": "LATA UNNIKRISHNAN",
    "occupation": "Director, The Daily Tribune",
    "phone": "36458393",
    "email": "director@newsofbahrain.com"
  },
  {
    "name": "LINA STAHL",
    "occupation": "Owner, A Box Forward Charity",
    "phone": "",
    "email": ""
  },
  {
    "name": "LOLAKSHI RAJARAM",
    "occupation": "Served as Ladies Co-ordinator, Kannada Sangha; Served as General Secretary, Entertainment Secretary, Ladies Co-ordinator, Bahrain Billawas",
    "phone": "33006657",
    "email": ""
  },
  {
    "name": "M. ASGHAR AFRIDI",
    "occupation": "Managing Director, Rich House Real Estate W.L.L.",
    "phone": "36804044",
    "email": "info@richhouserealestate.com"
  },
  {
    "name": "M. MUTHUVEL",
    "occupation": "Marketing Manager, Al Fateh Industrial Suppliers; General Secretary, Bharathi Association",
    "phone": "39911531",
    "email": "rajeebalans@gmail.com"
  },
  {
    "name": "M. SREEJITH KRISHNAN",
    "occupation": "Legal Advisor, Hassan Al Muharraqi Law Firm",
    "phone": "33364112",
    "email": "advsreejithkrishnan@gmail.com"
  },
  {
    "name": "M.C. MANOHARAN",
    "occupation": "Policeman (Airport), Ministry of Interior",
    "phone": "39284004",
    "email": "manoharan.sheeja@gmail.com"
  },
  {
    "name": "MD TOFAZZAL HOSSEN MUKUL",
    "occupation": "General Manager, Alfa Express Goods",
    "phone": "34540500",
    "email": "alfaxprs@gmail.com"
  },
  {
    "name": "MAHMOOD RAFIQUE CHAUDHRY",
    "occupation": "Founder/Editor-in-Chief, The24X7 News; Owner/Managing Director/CEO, Two Way Communication Co. W.L.L.",
    "phone": "32007700",
    "email": "the24x7newsbahrain@gmail.com"
  },
  {
    "name": "MADHAVAN KALLATH",
    "occupation": "Managing Partner, Kallath and Company W.L.L.",
    "phone": "39953988",
    "email": "madhavan@kallathandco.com"
  },
  {
    "name": "MANI LAKSHMANAMOORTHHY",
    "occupation": "Partner, Bahrain, MCA",
    "phone": "35358705",
    "email": "mani.l@mcagulf.com"
  },
  {
    "name": "MANOJ KESAVAN",
    "occupation": "Chief Operating Officer, Arabian Neon W.L.L.",
    "phone": "36364470",
    "email": "manojek@arabianneon.com"
  },
  {
    "name": "MANOSH KORA",
    "occupation": "Vice President 2024 / Secretary 2025, St. Peter's Jacobite Syrian Orthodox Church",
    "phone": "33043810",
    "email": "manoshkorah4@gmail.com"
  },
  {
    "name": "MELVIN DANTIS",
    "occupation": "Internal Auditor, Karnataka Social Club",
    "phone": "33882372",
    "email": "melvin@magnalit.com"
  },
  {
    "name": "MEENA DILIP KUMAR",
    "occupation": "Social Worker & Former Secretary, Indian Ladies Association",
    "phone": "33302887",
    "email": ""
  },
  {
    "name": "MOHD MOKBUL AHMED",
    "occupation": "General Manager, Ayedh Alkaabi Aluminium & Iron W.L.L.",
    "phone": "34445352",
    "email": "alkabiworks@gmail.com"
  },
  {
    "name": "MIAN BILAL AHMAD",
    "occupation": "CEO, Hamco Logistics Company (WLL)",
    "phone": "17750999",
    "email": "bahrain@hamcologistics.com"
  },
  {
    "name": "MOHD. SALAH UDDIN",
    "occupation": "Managing Director, Quba Excavation & Contracting Co. W.L.L; Director, Al Arafa Contracting",
    "phone": "33984432",
    "email": "salahuddin20@gmail.com"
  },
  {
    "name": "MOHAMMAD ANWAR HUSSAIN",
    "occupation": "Senior Auditor, A.N. For Auditing & Accounting",
    "phone": "39880285",
    "email": "m.anwar@an-auditor-tax.com"
  },
  {
    "name": "MOHAMMAD MANSOOR",
    "occupation": "Founder & CEO, Saara Group",
    "phone": "35117777",
    "email": "mansoor@saara.bh"
  },
  {
    "name": "MOHAMMAD SHABBIR",
    "occupation": "Managing Director, Dar Al Karam Trading & Contracting; Board Member, Pakistan Club & Pakistan Youth Society",
    "phone": "36414549",
    "email": "msm5577@gmail.com"
  },
  {
    "name": "MOHAMMED BASHAR MIAH",
    "occupation": "Managing Director, Kiwi Restaurant W.L.L",
    "phone": "33121249",
    "email": "bashar_6910@yahoo.com"
  },
  {
    "name": "MOHAMMED ASHFAQ BUTT",
    "occupation": "Director, Fiddah Décor & Maintenance W.L.L.",
    "phone": "39461379",
    "email": "fiddahdecor70@hotmail.com"
  },
  {
    "name": "MOHAMMED FAISAL IKRAM",
    "occupation": "Director, Wajda Group - Wajda Information Technology Services Co. W.L.L.",
    "phone": "33345615",
    "email": "faisal.ikram@wajdagroup.co"
  },
  {
    "name": "MOHAMMED JAHANGIR",
    "occupation": "Managing Director, Alumex Aluminum & Steel W.L.L.",
    "phone": "33023738",
    "email": "alumexaluminum@gmail.com"
  },
  {
    "name": "MOHAMMED JOYNUL ABDIN",
    "occupation": "Managing Director, Linnas World Furniture W.L.L; Chairman, Golden Salmabad Aluminium W.L.L.",
    "phone": "33552655",
    "email": "asmjoynul@gmail.com"
  },
  {
    "name": "MOHI UDDIN",
    "occupation": "Managing Director, Al Baraka Star Contracting",
    "phone": "66662353",
    "email": "albarakastar22@gmail.com"
  },
  {
    "name": "MOHAMMED ROSHAN",
    "occupation": "Marketing Manager, Al Jazira Group",
    "phone": "36478948",
    "email": "roshan@aljaziragroup.com"
  },
  {
    "name": "MONI ODIKANDATHIL",
    "occupation": "Senior NCO, Ministry of Interior",
    "phone": "39668326",
    "email": "moni66mathew@gmail.com"
  },
  {
    "name": "MONOJIT RAKHIT",
    "occupation": "Treasurer, Bengal Cultural Society, Bahrain",
    "phone": "33520231",
    "email": "monojit.34@gmail.com"
  },
  {
    "name": "MUHAMMAD ARSHAD",
    "occupation": "Country Manager, World Zone Logistics W.L.L.",
    "phone": "",
    "email": "arshad@worldzoneglobal.com"
  },
  {
    "name": "MUHAMMAD ASIM BAIG",
    "occupation": "CEO, Meridian Quality Management",
    "phone": "00966-507879405",
    "email": "ceo@meqmp.com"
  },
  {
    "name": "MUHAMMAD AZAM",
    "occupation": "Journalist",
    "phone": "36553848",
    "email": "azamqudrat@gmail.com"
  },
  {
    "name": "MUHAMMAD HANIF MALIK",
    "occupation": "Chairman, Layyah Overseas Forum",
    "phone": "36299389",
    "email": "hanif7644@yahoo.com"
  },
  {
    "name": "MUHAMMAD MAJID HANIF",
    "occupation": "Director, Techzology Consultancy W.L.L.",
    "phone": "32197779",
    "email": "info@techzology.com"
  },
  {
    "name": "MUHAMMAD HAYATULLAH",
    "occupation": "Managing Director, Tren Tren Restaurant & Grill",
    "phone": "33192911",
    "email": "muhammadmhd31@gmail.com"
  },
  {
    "name": "MUHAMMAD SHAHBAZ",
    "occupation": "Owner, Gourmet Burger, Burger Express, Burger Zoom, Burger time, Grill and Thrill, Gourmet Supermarket",
    "phone": "36020031",
    "email": ""
  },
  {
    "name": "MUHAMMED JUNAID",
    "occupation": "CEO, Wadima Business Solutions W.L.L; Wadima Travel and Tourism W.L.L.",
    "phone": "39025069",
    "email": "munawaradc@gmail.com"
  },
  {
    "name": "MUKESH TOLARAM NARSINGDAS GANDHI KAVALANI",
    "occupation": "Managing Director, Kavalani & Sons W.L.L.",
    "phone": "39450796",
    "email": "mukeshkavalani@gmail.com"
  },
  {
    "name": "MURALI KRISHNA G.",
    "occupation": "Community Service, Cultural and Language Enthusiast, Member - Telugu Kala Samithi",
    "phone": "39163266",
    "email": "gmkrishna22@yahoo.com"
  },
  {
    "name": "PROF. MUSTAFA AYTEKIN",
    "occupation": "Head of Promotion Committee, College of Engineering, University of Bahrain",
    "phone": "36936675",
    "email": "maytekin1@gmail.com"
  },
  {
    "name": "MUSTAFA DÖKMETAŞ",
    "occupation": "General Manager, Turkish Airlines in Bahrain",
    "phone": "",
    "email": "mdokmetas@thy.com"
  },
  {
    "name": "MYTHRAYEE HARISH",
    "occupation": "Mural Artist",
    "phone": "36365452",
    "email": ""
  },
  {
    "name": "N.K. MATHEW",
    "occupation": "General Manager, Box Makers W.L.L.",
    "phone": "39897958",
    "email": "enkayboxmaker@ymail.com"
  },
  {
    "name": "NADEEM IKRAM",
    "occupation": "Director of Finance, The Ritz-Carlton, Bahrain",
    "phone": "17580000",
    "email": "nadeem.ikram@ritzcarlton.com"
  },
  {
    "name": "NAJEEB KADALAYI",
    "occupation": "Chairman & Managing Director, K City Business Center W.L.L.",
    "phone": "37762255",
    "email": "info@kcitybahrain.com"
  },
  {
    "name": "NANDAKUMAR V.P.",
    "occupation": "Maintenance Manager, Bahrain Services and Maintenance Company -BSC ©",
    "phone": "39285406",
    "email": "nandakumarvp13@gmail.com.bh"
  },
  {
    "name": "NANJU REYES FRANCISCO",
    "occupation": "Content Writer/Editor/English Trainer, INTERMID TRAINING CENTER",
    "phone": "36947863",
    "email": "nanjufrancisco@gmail.com"
  },
  {
    "name": "NAZIA BARI",
    "occupation": "Director, Pushcord Technology W.L.L; Moda Vestir Boutique W.L.L.",
    "phone": "33196180",
    "email": "nazia@modavetire.com"
  },
  {
    "name": "DR. NAZMA ADIL HABIB",
    "occupation": "Specialist Gynecologist",
    "phone": "35519600",
    "email": "najmanaju@898@gmail.com"
  },
  {
    "name": "NILANJAN CHAKRABORTY",
    "occupation": "Convener, Bengal Cultural Society, Bahrain",
    "phone": "39064696",
    "email": "nilanjangr8@gmail.com"
  },
  {
    "name": "NILESH EKNATH KAPSE",
    "occupation": "Vice President, Maharashtra Cultural Society",
    "phone": "38987979",
    "email": "nekapse@gmail.com"
  },
  {
    "name": "NIREESH KUMAR",
    "occupation": "Plant Manager, Nass Contracting",
    "phone": "33214792",
    "email": "nireeshk@gmail.com"
  },
  {
    "name": "NIRMALA JOSEPH",
    "occupation": "Contract Specialist, Department of Defence, United States Government",
    "phone": "33665950",
    "email": "senoraa.nims@gmail.com"
  },
  {
    "name": "NIROSHAN SAMARASINGHA",
    "occupation": "Managing Partner / Director - Business Development, Bravo Group",
    "phone": "36334115",
    "email": "directorbusinessdevelopment@bravo-consultancy.com"
  },
  {
    "name": "NISHA SHARMA KOTWANI",
    "occupation": "Chartered Accountant / Compliance Head",
    "phone": "39095789",
    "email": "nishakotwani@gmail.com"
  },
  {
    "name": "NISHA RANGARAJAN",
    "occupation": "Hon. President, The Indian Fine Arts Society",
    "phone": "39617094",
    "email": "nishrang@gmail.com"
  },
  {
    "name": "NIVEDITA DUTTA",
    "occupation": "President, Bahrain Assamese Society",
    "phone": "39850372",
    "email": "ndutta8@gmail.com"
  },
  {
    "name": "NOMULA MURLI",
    "occupation": "IT Services; Welfare Convenor, Telugu Kala Samithi; Executive Member, ICRF",
    "phone": "39833395",
    "email": "nmurli@gmail.com"
  },
  {
    "name": "NOEL FERNANDES",
    "occupation": "President, Young Goan's Sports Club",
    "phone": "33778199",
    "email": "noelfern66@gmail.com"
  },
  {
    "name": "NOORUDHEEN",
    "occupation": "Secretary, Indian Islahi Centre",
    "phone": "33498517",
    "email": "noorudheenmusafir@gmail.com"
  },
  {
    "name": "P. GOPAKUMAR",
    "occupation": "Manager, Siam Printing and Publishing SCC",
    "phone": "39467749",
    "email": "pgopakumar@hotmail.com"
  },
  {
    "name": "P. UNNIKRISHNAN",
    "occupation": "Chairman, The Daily Tribune",
    "phone": "38444692",
    "email": "chairman@newsofbahrain.com"
  },
  {
    "name": "P.V. RADHAKRISHNA PILLAI",
    "occupation": "President, The Bahrain Keraleeya Samajam",
    "phone": "39691590",
    "email": "radhakrishnapillaipv@gmail.com"
  },
  {
    "name": "PADMAKUMAR MENON",
    "occupation": "Sr. Surveyor Motor Claims, The New India Assurance Co. Ltd.",
    "phone": "36793200",
    "email": "pappanmenon@gmail.com"
  },
  {
    "name": "PAMBAVASAN NAIR",
    "occupation": "Managing Director, Amad Group of Companies",
    "phone": "34305555",
    "email": "pambavasan@amadbaeed.com"
  },
  {
    "name": "PANKAJ NALLUR",
    "occupation": "Administration Manager, BDO; General Secretary, Indian Community Relief Fund (ICRF)",
    "phone": "39653007",
    "email": "pankaj.nallur@gmail.com"
  },
  {
    "name": "PAPIA GUHA",
    "occupation": "Active Member, Indian Community Relief Fund; Cancer Care Group",
    "phone": "39247486",
    "email": "papiamithu@hotmail.com"
  },
  {
    "name": "PAVITHRAN K. V.",
    "occupation": "Senior Secretary, RCS-PD",
    "phone": "39021796",
    "email": "pavikv@hotmail.com"
  },
  {
    "name": "PRADEEP KUMAR SHETTY",
    "occupation": "Director of IT, Gulf University & Alhekma International School",
    "phone": "39147114",
    "email": "pradeep@gulfuniversity.edu.bh"
  },
  {
    "name": "PRADEEP PURAVANKARA",
    "occupation": "Executive Editor, News of Bahrain (DT) / 4 PM News; Vice Chairman & Deputy Managing Director, Pravasi Guidance Center W.L.L.",
    "phone": "36458398",
    "email": "pradeeppuravankara@gmail.com"
  },
  {
    "name": "DR. PRAFUL VAIDYA FRCSI",
    "occupation": "Sr. Consultant General and Laparoscopic Surgeon",
    "phone": "39659909",
    "email": "plvaidya@batelco.com.bh"
  },
  {
    "name": "PRAKASH VATAKARA",
    "occupation": "Country Manager, Philip Morris Division; Malayalam Film Actor",
    "phone": "66372663",
    "email": "pragjaya@gmail.com"
  },
  {
    "name": "PRAMIL PEIRIS",
    "occupation": "Managing Director, Aquatic Home W.L.L.",
    "phone": "33467751",
    "email": "aquatichome.bh@gmail.com"
  },
  {
    "name": "PRASEETHA BALASUBRAMANIAM",
    "occupation": "Visual Artist",
    "phone": "39755991",
    "email": "praseethaullas@gmail.com"
  },
  {
    "name": "PRASHANT ASHOK JAGTAP",
    "occupation": "Corporate Sales (Brand In-charge), Abdullateef Khalid Al Aujan Food Stuff Est. W.L.L.",
    "phone": "66605952",
    "email": "prashant.a@alaujan.com.bh"
  },
  {
    "name": "PRASHANT RENGHE",
    "occupation": "Service / Division Manager, Prudent Solutions W.L.L. Um Al Hassam",
    "phone": "39913055",
    "email": "pacificrenghe@gmail.com"
  },
  {
    "name": "PRATHAP KUMAR GOPINATHAN",
    "occupation": "Director, Delta Electrical Items W.L.L.",
    "phone": "34646277",
    "email": "prathap@deltaelectricals.com"
  },
  {
    "name": "PRAVEEN NAIR",
    "occupation": "Social Worker; Former President, Kerala Social and Cultural Association",
    "phone": "36462046",
    "email": "pgpnair2007@yahoo.com"
  },
  {
    "name": "PRINCE NARAYANAN RAVI",
    "occupation": "Managing Partner, GSPU Chartered Accountants",
    "phone": "33160433",
    "email": "princegspu@gmail.com"
  },
  {
    "name": "PRINCE S. NATARAJAN",
    "occupation": "Hon. Chairman, The Indian School, Bahrain; Senior IT Project Administrator, GPIC",
    "phone": "36711195",
    "email": "princesn@indianschool.bh"
  },
  {
    "name": "PRIYA SHANKAR",
    "occupation": "Cluster Director of Marketing, InterContinental Hotels - Bahrain and Al Ahsa",
    "phone": "32239588",
    "email": "priya.shankar@ihg.com"
  },
  {
    "name": "PRIYANTHA NANAYAKKARA",
    "occupation": "Chartered Architect/ Senior Project Manager, Sanad Engineering",
    "phone": "33143331",
    "email": "priyantha_1@hotmail.com"
  },
  {
    "name": "QAMAR UL HASSAN",
    "occupation": "General Manager, Mohd Gharib Architects & Engineers",
    "phone": "39431815",
    "email": "qamarh63@gmail.com"
  },
  {
    "name": "QUSHEM MOHAMMAD SOFI SARWAR",
    "occupation": "Managing Director, Rich Interior Works W.L.L.",
    "phone": "33617547",
    "email": "qushem@richinteriorworks.com"
  },
  {
    "name": "R. SETHU VENKATESWARAN",
    "occupation": "Chairman, Innosoft Solutions Bahrain WLL; Managing Director, Bright Bridge Consultants Co WLL Bahrain",
    "phone": "39421691",
    "email": "sethu.chitra@gmail.com"
  },
  {
    "name": "R. SRINIVASAN",
    "occupation": "Director & CEO, Almoayyed International Group",
    "phone": "36075000",
    "email": "srinivasan@almoayyedintl.com"
  },
  {
    "name": "RADHIKA ANIL KUMAR",
    "occupation": "Teacher, Bahrain",
    "phone": "33445440",
    "email": "phroditeradh@gmail.com"
  },
  {
    "name": " RAFEEK ABBAS",
    "occupation": " Social Worker",
    "phone": "33202833",
    "email": "rafeek.met@gmail.com"
  },
  {
    "name": "RAGHUNADHABABU VADLAMUDI",
    "occupation": " RAGHUNADHABABU VADLAMUDI",
    "phone": "36053125",
    "email": "raghunadhababu.vadlamudi@ewa.bh"
  },
  {
    "name": "RAISON VARGHESE",
    "occupation": "Assistant Entertainment Secretary, The Indian Club",
    "phone": "39952725",
    "email": "raison1982@gmail.com"
  },
  {
    "name": "RAJEEB CHOWDHURY",
    "occupation": "Chief of Planning, Marketing & Customer Service - ME and Rest of the world, NAQEL Express; Founder, Biz Excel W.L.L.",
    "phone": "36062244",
    "email": "c.rajeeb@naqel.com.sa"
  },
  {
    "name": "RAJEEVAN C.K.",
    "occupation": "Member, ICRF; Founder, HOPE Bahrain",
    "phone": "33099976",
    "email": "rajivckp@yahoo.com"
  },
  {
    "name": "RAJESH B SHETTY",
    "occupation": "Operations Manager - Inspection and Certification, Alhoty Analytical Services; President, Patla Foundation (Bahrain & Saudi)",
    "phone": "38902807",
    "email": "rajeshbshetty28@gmail.com"
  },
  {
    "name": "RAJESH NAMBIAR",
    "occupation": "President, Kerala Social and Cultural Association",
    "phone": "37776719",
    "email": "rajrejiroshrohi@gmail.com"
  },
  {
    "name": "RAJKUMAR BHASKARA",
    "occupation": "Businessman, Aarya Interior Décor Co. W.L.L.",
    "phone": "39688395",
    "email": "rkumarbh90@gmail.com"
  },
  {
    "name": "RAJKUMAR V. WAGHNANI",
    "occupation": "Managing Director, RCL Rajkumar Consultancy Co. W.L.L.",
    "phone": "39654658",
    "email": "rajkumar@rclbh.com"
  },
  {
    "name": "DR. RAJSHRI GACHKAL",
    "occupation": "Head of Dermatology Department, Al Kindi Specialist Hospital, Zinj",
    "phone": "34065427",
    "email": "drrajshrigachkal@yahoo.com"
  },
  {
    "name": "RAKESH SHARMA",
    "occupation": "Managing Director, Palace Electronics",
    "phone": "39450463",
    "email": "palace.electronics@gmail.com"
  },
  {
    "name": "RAMANPREET PRAVEEN",
    "occupation": "Psychologist, Writer, Director (Freelancer)",
    "phone": "66685335",
    "email": "preetypraveen19@gmail.com"
  },
  {
    "name": "RAMAZAN METE ALAK",
    "occupation": "Director - Business Development and Sales, Bahrain Institute for Pearls & Gemstones (DANAT)",
    "phone": "38414155",
    "email": "ramazanmete.alak@danat.bh"
  },
  {
    "name": "RANA SHAHID",
    "occupation": "Businessman- Food, Hospitality and Trading, Transit Café Lounge",
    "phone": "33115579",
    "email": "ranashahid913@gmail.com"
  },
  {
    "name": "DR. RANJITH MENON",
    "occupation": "Consultant Nephrologist, Middle East Hospital",
    "phone": "33057566",
    "email": "drranjith@mehospital.com"
  },
  {
    "name": "DR. RASHMI DHANUKA",
    "occupation": "General Physician, Middle East Medical Center",
    "phone": "33035640",
    "email": "rashmidhanukadr@yahoo.com"
  },
  {
    "name": "RATHAN BHAT",
    "occupation": "Asst. Entertainment Secretary, Karnataka Social Club",
    "phone": "66654872",
    "email": "rathankbayar@gmail.com"
  },
  {
    "name": "RATHIN NATH K R",
    "occupation": "Operations Manager, Acon Travels and Tours W.L.L.",
    "phone": "38255019",
    "email": "operation-mgr@acon-travels.com"
  },
  {
    "name": "RAVI PAREKH",
    "occupation": "Managing Director, New Jumbo Jewellers",
    "phone": "17211665",
    "email": "ravi@jumbogold.com"
  },
  {
    "name": "RAZAK MUZHIKKAL",
    "occupation": "Managing Director, Muzhikkal Alzayani Construction Co. W.L.L. & Mcgrow Alzayani Rent A Car W.L.L.",
    "phone": "39605707",
    "email": "razakmuzhikkal@gmail.com"
  },
  {
    "name": "RENGANATHAN RAMESH",
    "occupation": "Managing Director, Santy Excavation and Construction Co. W.L.L.",
    "phone": "66960061",
    "email": "ramesh@santyconstruction.com"
  },
  {
    "name": "RICHA MAYURA",
    "occupation": "Visual Artist, Designer and Art Educator",
    "phone": "34056855",
    "email": "richahuesntones@gmail.com"
  },
  {
    "name": "RISMY SURANGA",
    "occupation": "Assistant Manager-Project, Fine Foods",
    "phone": "32174176",
    "email": "risuranga04@gmail.com"
  },
  {
    "name": "RIYAS THARIPPAYIL",
    "occupation": "Entrepreneur, P.O.Box 54653, Manama",
    "phone": "39177666",
    "email": "riyasbangkok@yahoo.com"
  },
  {
    "name": "ROLAND VARELLA",
    "occupation": "General Secretary, Young Goan's Sports Club",
    "phone": "36355164",
    "email": "roland.varella@yahoo.com"
  },
  {
    "name": "ROSHAN ARAVIND",
    "occupation": "Chief Distribution Officer (Insurance Business), Al Hilal Life & Al Hilal Takaful",
    "phone": "36919205",
    "email": "roshanaravind@outlook.com"
  },
  {
    "name": "ROSHAN TENNAKOON",
    "occupation": "Technical Services Director, Gulf Hotel Groups",
    "phone": "36552999",
    "email": "roshan.tennakoon@gulfhotelsgroup.com"
  },
  {
    "name": "ROY C ANTONY",
    "occupation": "Marine A/C section Incharge, Ministry of Interior, Segaya",
    "phone": "39681102",
    "email": "antonycroy@yahoo.com"
  },
  {
    "name": "ROYSTAN FERNANDES",
    "occupation": "Entertainment Secretary, Karnataka Social Club",
    "phone": "38103231",
    "email": "royarva@gmail.com"
  },
  {
    "name": "RREMA NAIR",
    "occupation": "Former Hon. Secretary Entertainment, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "S. LAKSHMI NARASIMHAN",
    "occupation": "General Manager & Director, Bahrain India International Exchange Co. (BIIECO)",
    "phone": "39403909",
    "email": "lakshmi@biieco.com"
  },
  {
    "name": "S. SANKARANARAYANAN",
    "occupation": "Director - Commercial & Operations, Alliance Maritime Company W.L.L.",
    "phone": "32334466",
    "email": "shankaran@alliancemaritime.net"
  },
  {
    "name": "S.VIVEKANADAN",
    "occupation": "Secretary, Tamil Social and Cultural Association",
    "phone": "39971555",
    "email": "anand@alriyadhgroup.com"
  },
  {
    "name": "DR. SAGAR ADKAR",
    "occupation": "Consultant Gastroenterologist, BDF Hospital",
    "phone": "34231528",
    "email": "sagar.adkar@bdfmedical.org"
  },
  {
    "name": "SAIKAT DEY",
    "occupation": "Admin Secretary, Bengal Cultural Society, Bahrain",
    "phone": "34437415",
    "email": "saikatdey1981@gmail.com"
  },
  {
    "name": "SAIKAT SARKAR",
    "occupation": "Chief, Electricity and Water Authority (EWA-MEWA), Bahrain; President, Bengal Cultural Society",
    "phone": "36410205",
    "email": "netsaikat2k1@yahoo.co.in"
  },
  {
    "name": "SAIRA RANJ",
    "occupation": "Marketing Head, Europcar Oman & Bahrain; Founder, Createit - Bahrain",
    "phone": "39124300",
    "email": "saira.ranj@europcaroman.net"
  },
  {
    "name": "DR. SAJI ABRAHAM CHIRATHALATTU",
    "occupation": "Consultant Orthodontist CEO & Medical Director, Dr Saji Abraham Dental Specialists and Orthodontics.W.L.L.",
    "phone": "39755217",
    "email": "drsajiortho@gmail.com"
  },
  {
    "name": "SAJI ANTONY",
    "occupation": "Honorary General Secretary, The Indian School, Bahrain",
    "phone": "39691959",
    "email": "antonysaji@gmail.com"
  },
  {
    "name": "SAJID BUTT",
    "occupation": "Sajid Butt Information Technology Co. W.L.L.",
    "phone": "33306786",
    "email": "globalsales@sbitwll.com"
  },
  {
    "name": "SAJIN HENTRY",
    "occupation": "Managing Director, Syskode Technologies",
    "phone": "37513751",
    "email": "sajinhentry@syskode.com"
  },
  {
    "name": "SAKHARIAH P PUNATHIL",
    "occupation": "Chairman, Westhome Property Management W.L.L.",
    "phone": "33163333",
    "email": "sakhariah@westhomeproperty.com"
  },
  {
    "name": "SAMEER ASIF BUTT",
    "occupation": "Director, Digital Players Media; Managing Editor, Bizbahrain",
    "phone": "33836777",
    "email": "sameer@bizbahrain.com"
  },
  {
    "name": "SAMI UR REHMAN AZIZ",
    "occupation": "Chairman, Board of Management, Pakistan School; General Secretary, Pakistan Club",
    "phone": "39143498",
    "email": "samirehman334@gmail.com"
  },
  {
    "name": "DR. SAMY GOUDA",
    "occupation": "Consultant of Neurosurgery & Spine Surgery, Middle East Hospital",
    "phone": "39000377",
    "email": ""
  },
  {
    "name": "SANDRA D'COSTA",
    "occupation": "Treasurer, Karnataka Social Club",
    "phone": "39537742",
    "email": "sananchi3@yahoo.com"
  },
  {
    "name": "SANKARA SUBBU NANDAKUMAR",
    "occupation": "Entertainment Secretary, The Indian Club",
    "phone": "36433552",
    "email": "nanda.kumar75@yahoo.com"
  },
  {
    "name": "SANGEETHA RAM PRASAD",
    "occupation": "Carnatic Music Vocalist, Music Teacher, Sahaja Yoga Meditation Practitioner (With all sessions being free of charges)",
    "phone": "39231481",
    "email": "sangrp@gmail.com"
  },
  {
    "name": "SANJEEV DANIEL",
    "occupation": "Investor, Carzone Promotions; Former Secretary, St. Peter's Jacobite Syrian Orthodox Church",
    "phone": "34120380",
    "email": "danielkollam@gmail.com"
  },
  {
    "name": "SANTHOSH ANDREWS ISAAC",
    "occupation": "",
    "phone": "36770771",
    "email": "saisaac017@gmail.com"
  },
  {
    "name": "SARADA AJITH",
    "occupation": "Former President, Indian Ladies Association",
    "phone": "38872702",
    "email": "saruajith@hotmail.com"
  },
  {
    "name": "SARMISTHA DEY",
    "occupation": "Former Hon. General Secretary, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "SATHEESH NARAYANAN NAIR",
    "occupation": "General Secretary, Kerala Social and Cultural Association (KSCA)",
    "phone": "33368466",
    "email": "stnpvk@gmail.com"
  },
  {
    "name": "SATHISH MUDALAYIL",
    "occupation": "Architect-Director, Simandpro-Atcon Bahrain Co. W.L.L.",
    "phone": "36646609",
    "email": "sathish.simandpro@atconbahrain.com"
  },
  {
    "name": "SAVITHA RAGHAVAN",
    "occupation": "Senior Lecturer- Banking Centre, Bahrain Institute of Banking and Finance (BIBF)",
    "phone": "39108050",
    "email": "savitha@bibf.com"
  },
  {
    "name": "SEBAHAT ISIK",
    "occupation": "Managing Director, Founder, YSM Consultancy W.L.L; Senator, World Business Angels Investment Forum in Bahrain",
    "phone": "39605349",
    "email": "info@ysm-consultancy.com"
  },
  {
    "name": "SEEMA ASHISH ATHAVALE",
    "occupation": "Senior Associate-Gemologist, DANAT",
    "phone": "33656748",
    "email": "athavaleseemaa@gmail.com"
  },
  {
    "name": "SEVI MATHUNNY",
    "occupation": "Former President, Kerala Catholic Association; Former Board Member, Syro Malabar Society; Former Culture Secretary of Coordination, Indian Association",
    "phone": "38382676",
    "email": "mmsevi@gmail.com"
  },
  {
    "name": "SHAHID AHMED",
    "occupation": "Managing Director, IES Alliance for Management of Industrial Projects W.L.L",
    "phone": "66677727",
    "email": "sirshahidahmed1@gmail.com"
  },
  {
    "name": "SHAHMEEN ISLAM",
    "occupation": "Architect/Philanthropist; President, Pakistani Women's Association",
    "phone": "",
    "email": "pwabahrain11@gmail.com"
  },
  {
    "name": "SHAILESH R. SHAH",
    "occupation": "Chartered Accountant; Former President, Vice President, Secretary, Gujarati Samaj",
    "phone": "39624285",
    "email": ""
  },
  {
    "name": "SHAILESH PILLEWAR",
    "occupation": "Subject Matter Expert Human Capital Management, Dr. Ambedkar International Mission Bahrain (AIM)",
    "phone": "36401025",
    "email": "snpillewar@yahoo.com"
  },
  {
    "name": "SHAJI KARTHIKEYAN",
    "occupation": "Sales and Marketing Manager, National Constructions",
    "phone": "38377372",
    "email": "sales@ncbahrain.com"
  },
  {
    "name": "C.A. SHARMILA SHET",
    "occupation": "Manager, Internal Audit and Risk Advisory, Protiviti",
    "phone": "36797832",
    "email": "shet.sharmila@gmail.com"
  },
  {
    "name": "SHAWN ABRAHAM GEORGE",
    "occupation": "Business Development Manager, Gratia Advertising",
    "phone": "38324071",
    "email": "info@gratiaad.com"
  },
  {
    "name": "SHEEJA NATRAJ",
    "occupation": "Managing Director, Zawia 3 Supermarket",
    "phone": "39789866",
    "email": "sheeja.natraj@gmail.com"
  },
  {
    "name": "SHEETAL SHAH",
    "occupation": "Former Hon. Treasurer, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "DR. SHEMILY P. JOHN",
    "occupation": "Assistant Professor, Head of General Studies Unit, University College of Bahrain",
    "phone": "33381808",
    "email": "shemily.john@gmail.com"
  },
  {
    "name": "SHILPA YASHODHAN ABHYANKAR",
    "occupation": "Art of livings Happiness Program Teacher; Meditation Teacher; Yoga Teacher; Yoga Instructor at Ritz Carlton",
    "phone": "39047298",
    "email": "shilpa306@gmail.com"
  },
  {
    "name": "SHIPRA DHIR PASSI",
    "occupation": "Entrepreneur and Humanitarian",
    "phone": "39475574",
    "email": "shipradhir@gmail.com"
  },
  {
    "name": "DR. SHREYAS LAXMAN PALAV",
    "occupation": "Head of Ophthalmology Department, Shifa Al Jazeera Hospital Manama",
    "phone": "36297561",
    "email": "drpalav@gmail.com"
  },
  {
    "name": "SHYAM SUNDER",
    "occupation": "Group Head Corporate Banking, Ahli United Bank B.S.C.",
    "phone": "",
    "email": "shyam.sunder@ahliunited.com"
  },
  {
    "name": "SIVA YELLAPU",
    "occupation": "Power Generations Engineer, Alezzel Operations & Maintenance (Engie Group)",
    "phone": "33332778",
    "email": "ysivak@gmail.com"
  },
  {
    "name": "SIVAKUMAR KOLLEROTH",
    "occupation": "Project Manager, Albayynat Construction Co.",
    "phone": "34646440",
    "email": "sivak67@gmail.com"
  },
  {
    "name": "SMITHA JENSEN",
    "occupation": "President; Former Hon. Sec. Operations, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "SOMAN BABY",
    "occupation": "Chairman, Veritas Media and Advertising",
    "phone": "39629123",
    "email": "somanwmc@gmail.com"
  },
  {
    "name": "SOMASHREE SARKAR",
    "occupation": "Executive Member, Bengal Cultural Society, Bahrain",
    "phone": "37736619",
    "email": "tupshis@gmail.com"
  },
  {
    "name": "SREEJA SREEDHARAN",
    "occupation": "HR & Admin, DHI International W.L.L Bahrain",
    "phone": "39293112",
    "email": "sreeja.sunu@gmail.com"
  },
  {
    "name": "SREEKANTH SIVAN",
    "occupation": "Gen. Secretary, Sree Narayana Cultural Society",
    "phone": "38099465",
    "email": ""
  },
  {
    "name": "SREEKUMAR K.L.",
    "occupation": "General Manager, Project Delivery Center Division, Yokogawa Saudi Arabia Company",
    "phone": "33941200",
    "email": "klsree@hotmail.com"
  },
  {
    "name": "SREENIVAS KRISHNAMOORTHY",
    "occupation": "Industry Manager, Bureau Veritas",
    "phone": "39034717",
    "email": "sreenivas.krishnamoorthy@bureauveritas.com"
  },
  {
    "name": "SRINIVASAN RATHINAM",
    "occupation": "Managing Director, Maxworth Consulting W.L.L.",
    "phone": "39468234",
    "email": "ssrinivasanrathinam@maxworthconsulting.me"
  },
  {
    "name": "SUAY DOĞANAY",
    "occupation": "International Violinist/Violin Artist",
    "phone": "32063108",
    "email": "suaydoganay@gmail.com"
  },
  {
    "name": "SUBAIR KANNUR",
    "occupation": "Member, Non Resident Indians (Keralites) Commission, Govt. of Kerala; Member, Lok Kerala Sabha; Patron, Bahrain Parathiba",
    "phone": "39682974",
    "email": "subeerkannur@gmail.com"
  },
  {
    "name": "SUBAS SAHOO",
    "occupation": "CEO, Ayrus Infotech (A division of AYRUS Group)",
    "phone": "33098893",
    "email": "thechammu@gmail.com"
  },
  {
    "name": "SUBHASIS GUPTA",
    "occupation": "Managing Director, Enas International Co. W.L.L.; Freight & Logistics Global",
    "phone": "36110847",
    "email": "subhasis@enasinternational.org"
  },
  {
    "name": "SUBIN KANJIRAPARAMBIL UNNIKRISHNAN",
    "occupation": "General Manager, Design Track Prints W.L.L.",
    "phone": "33393983",
    "email": "subindt.bh@gmail.com"
  },
  {
    "name": "SUCHITA DEY",
    "occupation": "Festival Secretary, Bengal Cultural Society, Bahrain",
    "phone": "33234150",
    "email": "suchitakardey@gmail.com"
  },
  {
    "name": "SUDEEP JOSEPH",
    "occupation": "Managing Partner, Al Bandar Cars W.L.L; Director, M&S Associates, Auditors and Tax Consultants; Al Nada Training Centre",
    "phone": "36414289",
    "email": "sudeepjoseph@gmail.com"
  },
  {
    "name": "SUDEEP SUDHIR DESHPANDE",
    "occupation": "Founder, Concept House Co. W.L.L.",
    "phone": "33368809",
    "email": "sudeepforart@gmail.com"
  },
  {
    "name": "SUDHEER THIRUNILATH",
    "occupation": "Director, Humanitarian Aid, Middle East Region at World NRI Council; Country Head, Pravasi Legal Cell; Executive Secretary to HE.Sh.Khalid Bin Hamad Rezq Al-Khalifa",
    "phone": "39461746",
    "email": "sudheer@worldnricouncil.org"
  },
  {
    "name": "SUDIN ABRAHAM",
    "occupation": "General Manager, Mercury Marketing W.L.L.",
    "phone": "39960171",
    "email": "sudin.abraham@gmail.com"
  },
  {
    "name": "SUJESH GEORGE",
    "occupation": "Treasurer, St. Peter's Jacobite Syrian Orthodox Church",
    "phone": "39967524",
    "email": "sujeshgeorge767@gmail.com"
  },
  {
    "name": "SULTANAGODA MANAGE LIONEL",
    "occupation": "Electrical Engineer - Sanitary Engineering, Ministry of Works",
    "phone": "39057488",
    "email": "sult@works.gov.bh"
  },
  {
    "name": "DR. SUNANDO ROY",
    "occupation": "Advisor, Central Bank of Bahrain",
    "phone": "39927138",
    "email": "sunandoroy@gmail.com"
  },
  {
    "name": "SUNDEEP CHOPRA",
    "occupation": "Founder and President, Punjabi's United in Bahrain (PUB)",
    "phone": "36149888",
    "email": "sundeep7@gmail.com"
  },
  {
    "name": "FR. SUNIL KURIAN BABY",
    "occupation": "Vicar, St. Mary's Indian Orthodox Cathedral",
    "phone": "39445358",
    "email": ""
  },
  {
    "name": "SUNISH SUSEELAN",
    "occupation": "Former Chairman, Sree Narayana Cultural Society",
    "phone": "36674139",
    "email": "sncsbahrain@hotmail.com"
  },
  {
    "name": "SUNIL GEORGE D'SOUZA",
    "occupation": "Former President, Karnataka Social Club",
    "phone": "39889358",
    "email": "dsouzasunil71@gmail.com"
  },
  {
    "name": "SURAJ HAMEED",
    "occupation": "Managing Director, Techno Fire Systems & Safety Co. W.L.L.",
    "phone": "38381562",
    "email": "suraj@technofiresafe.com"
  },
  {
    "name": "SURENDRA SHETTY",
    "occupation": "Managing Director, S.S.K. Trading",
    "phone": "33771999",
    "email": "sales@ssktrdg.com"
  },
  {
    "name": "SURESH BALAKRISHNAN",
    "occupation": "Quality Inspector, Arab Shipbuilding & Repair Yard Co. (ASRY)",
    "phone": "34077368",
    "email": "balakrishnansuresh00@gmail.com"
  },
  {
    "name": "SURESH DESIKAN",
    "occupation": "General Manager - Finance, Global Industrial Resources W.L.L.",
    "phone": "39068323",
    "email": "desikansuresh2@gmail.com"
  },
  {
    "name": "SURESH T. VAIDYANATHAN",
    "occupation": "Former Managing Director of a Banking Business Advisory Firm specialized in Risk Management and Compliance",
    "phone": "39629264",
    "email": "suresh60bahrain@gmail.com"
  },
  {
    "name": "SUSHIL MULJIMAL",
    "occupation": "Chairman, Thattai Hindu Community",
    "phone": "39989907",
    "email": "sushil@vmbros.com"
  },
  {
    "name": "SUSHMA GUPTA",
    "occupation": "Entrepreneur, Shining Rays Co.",
    "phone": "33052258",
    "email": "sushma.anilk@gmail.com"
  },
  {
    "name": "SYED HANEEF",
    "occupation": "Founder, Lights of Kindness (Social Assistance Drive) Segaya",
    "phone": "36221399",
    "email": "mhsyed@yahoo.com"
  },
  {
    "name": "TARAL PAREKH",
    "occupation": "Senior Director, STC Bahrain; Partner, Kailash Parbat Restaurant",
    "phone": "33011158",
    "email": "taral9000@hotmail.com"
  },
  {
    "name": "TARIQ MEHMOOD",
    "occupation": "Relationship Manager Global Remittance Business, FIGTS, Habib Bank Limited",
    "phone": "33987307",
    "email": "tariq.mehmood15@hbl.com"
  },
  {
    "name": "TAYYAR UFUK ERSOY",
    "occupation": "Senior Sales Manager, Al Areen Palace & Spa by Accor",
    "phone": "",
    "email": "ufuk.ersoy@accor.com"
  },
  {
    "name": "TEJBIR SINGH",
    "occupation": "Architect",
    "phone": "39291632",
    "email": "tejbirsingh25@gmail.com"
  },
  {
    "name": "DR. TEJENDER KAUR SARNA",
    "occupation": "Dietician, Lifestyle Nutritionist and Meal Planner, GHK Rite Diet; Former Hon. Vice President, Indian Ladies Association",
    "phone": "39157282",
    "email": "tejenderkaursarna@gmail.com"
  },
  {
    "name": "DR. THAJUDEEN H. MUSTHAFA",
    "occupation": "General and Family Physician; Medical Director, Middle East Medical Center",
    "phone": "33908656",
    "email": "drthaj@gmail.com"
  },
  {
    "name": "THANUJA JAYARAM",
    "occupation": "Has been associated with Financial Resources Directorate for 20 years, Ministry of Works, Kingdom of Bahrain",
    "phone": "36310050",
    "email": ""
  },
  {
    "name": "THARANGA MADUSHANKA W.K.",
    "occupation": "Senior Mechanical Engineer & Project Manager, Ministry of Works",
    "phone": "66904699",
    "email": "TharangaM@works.gov.bh"
  },
  {
    "name": "THOMAS PHILIP",
    "occupation": "Sales Manager, Abu Khalil Building Materials W.L.L",
    "phone": "39384959",
    "email": "bijuthomasphilip98@gmail.com"
  },
  {
    "name": "THOMAS V.K. (ADV.)",
    "occupation": "Managing Partner/Legal Consultant, Thomas & Associates W.L.L; Corporate Services, Associated with Al Ansari & Partners Attorneys & Legal Consultants; Vice-Chairman - ICRF; Board Member - Bahrain India Society",
    "phone": "39442560",
    "email": "thomasvk@thomasvk.com"
  },
  {
    "name": "THUSARA DILHAN GALLAGE",
    "occupation": "President, Sri Lankan Welfare Society",
    "phone": "33055911",
    "email": "thusara.arabian.pool@gmail.com"
  },
  {
    "name": "TILOTTAMA S. SHAH",
    "occupation": "Former Teacher, The Indian School",
    "phone": "38400925",
    "email": "shahtilo@gmail.com"
  },
  {
    "name": "TONY NELLICKEN",
    "occupation": "Executive Director, Global Remote Bahrain W.L.L.",
    "phone": "17811757",
    "email": "tony@global-remote.net"
  },
  {
    "name": "UDAYA ERANGA",
    "occupation": "Marketing Manager, Lanka Bravo Consultancy W.L.L.",
    "phone": "34227887",
    "email": "marketing@bravo-consultancy.com"
  },
  {
    "name": "UJJAL KUMAR MUKHERJEE",
    "occupation": "CEO, Al Jazira Group",
    "phone": "17720700",
    "email": "ujjal@aljaziragroup.com.bh"
  },
  {
    "name": "ULHAS KARNAVAR",
    "occupation": "Former Secretary, The Indian Club",
    "phone": "66629976",
    "email": "ulhasskarnavar@gmail.com"
  },
  {
    "name": "UMESH SONARIKAR",
    "occupation": "President, Maharashtra Cultural Society Kingdom of Bahrain",
    "phone": "33331866",
    "email": "mcs.bahrain@gmail.com"
  },
  {
    "name": "USMAN TIP TOP",
    "occupation": "Proprietor, Tip Top Boutique; Vice President, KMCC Bahrain",
    "phone": "39823200",
    "email": "usman.tiptop@gmail.com"
  },
  {
    "name": "V. KRISHNA KUMAR",
    "occupation": "Operations Manager, Park Regis Lotus Hotel - Bahrain",
    "phone": "36375777",
    "email": "om@parkregislotushotel.com"
  },
  {
    "name": "V.R. PALANISWAMY",
    "occupation": "Principal, The Indian School, Bahrain; Chairman, CBSE Gulf Sahodaya (2023-2024)",
    "phone": "36375777",
    "email": "om@parkregislotushotel.com"
  },
  {
    "name": "V.R. SAJEEVAN",
    "occupation": "Financial Management Analyst, COMUSNAVCENT COMPTROLLER Department, U S Navy; Former General Secretary, Sree Narayana Cultural Society, Bahrain",
    "phone": "36711192",
    "email": "principal@indianschool.bh"
  },
  {
    "name": "V.S. THAKUR",
    "occupation": "General Manager, Speedex Global Cargo Express",
    "phone": "36111701",
    "email": "thakurs57@yahoo.com"
  },
  {
    "name": "VARGHESE KARAKKAL",
    "occupation": "General Secretary, The Bahrain Keraleeya Samajam",
    "phone": "39617620",
    "email": "bksamajam@gmail.com"
  },
  {
    "name": "VARGHESE KURIAN",
    "occupation": "Chairman & Managing Director, VKL & Al Namal Group of Companies",
    "phone": "39699904",
    "email": "vk@vklholdings.com"
  },
  {
    "name": "VIJAY KUMAR (MUKHIYA)",
    "occupation": "Vedic Sanatan Dharma Shastri; Hindu Community Priest, Shree Krushna (Shrinathji) Hindu Temple, Manama",
    "phone": "39275838",
    "email": "shastrivijaykumar60@gmail.com"
  },
  {
    "name": "VIJAY NAIK",
    "occupation": "Senior Consultant, LIC International",
    "phone": "39084973",
    "email": "vijaynaik_lic@hotmail.com"
  },
  {
    "name": "VILAS V. DESHMUKH",
    "occupation": "Sales & Marketing Manager, Mohammed Jalal and Sons Technology W.L.L.",
    "phone": "36974820",
    "email": "vilas_deshmukh@jalal.com"
  },
  {
    "name": "VINAY SEQUEIRA",
    "occupation": "General Secretary, Karnataka Social Club",
    "phone": "33244300",
    "email": "vinsequeri@gmail.com"
  },
  {
    "name": "VINEESH M.P.",
    "occupation": "Financial Controller, Falcon Electrical W.L.L.",
    "phone": "39603989",
    "email": "vini143@gmail.com"
  },
  {
    "name": "VINOD A PATRIC",
    "occupation": "General Manager, Leisure, House of Travel",
    "phone": "36066022",
    "email": "v.patric@hot.bh"
  },
  {
    "name": "VINOD DAS. M.",
    "occupation": "Director, Steelmark Mideast W.L.L.",
    "phone": "17223470",
    "email": "info@steelmarkgroup.com"
  },
  {
    "name": "VINOD EARATH",
    "occupation": "General Manager, Esquire Property Consultancy Co. W.L.L.",
    "phone": "39991014",
    "email": "vinod@esquirebh.com"
  },
  {
    "name": "VINOD KUMAR",
    "occupation": "Director, Veva Publicity & Advertising W.L.L.",
    "phone": "39034346",
    "email": "vevapublicity.vk@gmail.com"
  },
  {
    "name": "VINOD NARAYANAN",
    "occupation": "Cambridge IGCSE Coordinator, Al Noor International School Kingdom of Bahrain",
    "phone": "33434380",
    "email": "vinodnsair@gmail.com"
  },
  {
    "name": "VINOD SASTHAVU ASARI",
    "occupation": "Vice-Principal, The Indian School",
    "phone": "33660126",
    "email": "vpms@indianschool.bh"
  },
  {
    "name": "WAQAR UL HAQ AHMED",
    "occupation": "Chairman, HFMC W.L.L. Group; Founder, Intellectuals Professional Organization, Bahrain; Director, Falcon Real Estate, Pakistan",
    "phone": "32203400",
    "email": "waqar.haqq@gmail.com"
  },
  {
    "name": "WILSON MATHEW",
    "occupation": "Director, Al Saad Power Projects; Manager, Pearl India Trading Company W.L.L.",
    "phone": "39660586",
    "email": "wilson@alsaadprojects.com"
  },
  {
    "name": "WINSENT THOMAS",
    "occupation": "",
    "phone": "39894859",
    "email": "pearlindia2009@yahoo.com"
  },
  {
    "name": "YOGESH BHATIA",
    "occupation": "Group chairman, Falcon Trading Company W.L.L.; Bhatia Technical Services Company W.L.L.; Slingtek W.L.L.; Naraina Holding Company W.L.L.",
    "phone": "17737077",
    "email": "yogeshb@batelco.com.bh"
  },
  {
    "name": "YOGESH PATIL",
    "occupation": "Partner/Director, BostonBrooks Advisory W.L.L.",
    "phone": "38870973",
    "email": "ypatil@bostonbrooks.com"
  },
  {
    "name": "ZAFAR IQBAL MALIK",
    "occupation": "Coordinator/Counsellor, Alnada Training Centre",
    "phone": "",
    "email": "awan.zafar71@outlook.com"
  },
  {
    "name": "ZAHID SHEIKH",
    "occupation": "Executive Director, MSS Hotels & Restaurants W.L.L.; Gulf MSS for Trading & Services",
    "phone": "36764750",
    "email": "mzahidsheikh@gmail.com"
  },
  {
    "name": "ZAMINI CHARAK",
    "occupation": "Former Hon. Sec. Public Relations, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "DR. MANOJ KUMAR CG",
    "occupation": "Occupational Medicine Specialist, Royal Bahrain Hospital",
    "phone": "33050525",
    "email": "manojplr@gmail.com"
  },
  {
    "name": "FAISAL MADAPPALLY",
    "occupation": "IT Technician, Ministry of Interior",
    "phone": "33394919",
    "email": "faisalmadappalli@gmail.com"
  },
  {
    "name": "K.T. SALIM",
    "occupation": "Social Worker; General Secretary, Cancer Care Group; ICRF - Active Member",
    "phone": "33750999",
    "email": "salimktaj@gmail.com"
  },
  {
    "name": "DR. ROSHNI RAJAN",
    "occupation": "Dental Surgeon, Kings Dental Center",
    "phone": "66304029",
    "email": "doctor.roshnirajan@gmail.com"
  },
  {
    "name": "SURESH BABU",
    "occupation": "President, Samskruthi Bahrain",
    "phone": "39237596",
    "email": "samskruthibahrain@gmail.com"
  },
  {
    "name": "KAIHEKUSHAN OMAR KAZI",
    "occupation": "Hon. Secretary Activities, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "K.T. MOHAMMED ALI",
    "occupation": "Managing Director, Dar Al Shifa Medical Centre",
    "phone": "36403999",
    "email": "ktmali@daralshifa.com.bh"
  },
  {
    "name": "SALMANUL FARIS",
    "occupation": "President, OICC Palakkad District Committee; Secretary, Palakkad Arts and Cultural Theatre; Vice Chairman, IYC International; Academic Council Memberr, Priyadarshini Publication; General Secretary, Mannarkad Association",
    "phone": "39143967",
    "email": ""
  },
  {
    "name": "FOUSIYA SULTHANA",
    "occupation": "Hon. Vice President, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "TESSY CHERIAN",
    "occupation": "Hon. Treasurer, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "VANI SREEDHAR",
    "occupation": "Hon. General Secretary, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "SHILPA NAIK",
    "occupation": "Hon. Secretary Public Relations, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "SUNANDA GAIKWAD",
    "occupation": "Hon. Secretary Entertainment, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "VIJAY LAKSHMI",
    "occupation": "Hon. Secretary Membership, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "ANU SAMPATH",
    "occupation": "Hon. Secretary Operations, Indian Ladies Association",
    "phone": "33560046",
    "email": "ilabahrain@gmail.com"
  },
  {
    "name": "DILEEF PM",
    "occupation": "Social Worker; Member, Cancer Care Group",
    "phone": "33782226",
    "email": "deepadileef@hotmail.com"
  },
  {
    "name": "DEEPA DILEEF",
    "occupation": "Social Worker; Member, Cancer Care Group",
    "phone": "33521211",
    "email": "deepadileef@hotmail.com"
  },
  {
    "name": "MOHAMMED RAFEEK",
    "occupation": "Joint Secretary, PGF; Ex Advisory Board Member, MMS; Ex Vice President, IYCC",
    "phone": "33896640",
    "email": "rafeekmohammed333@gmail.com"
  },
  {
    "name": "AHMED SHAMEER",
    "occupation": "General Manager, Dar Al Shifa Medical Centre",
    "phone": "33002636",
    "email": "shameerpcb@daralshifa.com.bh"
  },
  {
    "name": "RASHEEDA MOHAMMED ALI",
    "occupation": "HR Director, Dar Al Shifa Medical Centre",
    "phone": "36444520",
    "email": "rasheeda@daralshifa.com.bh"
  },
  {
    "name": "CLIFFORD CORREIA",
    "occupation": "Action Committee Member, Migrant Worker Society",
    "phone": "39876070",
    "email": "cliffordcorreia@gmail.com"
  },
  {
    "name": "MOHAMMED RAJUL",
    "occupation": "Head of Marketing and Business Development, Dar Al Shifa Medical Centre",
    "phone": "36708252",
    "email": "rajul@daralshifa.com.bh"
  },
  {
    "name": "RAMEEN MOHAMMED ALI",
    "occupation": "Chief Finance Officer, Dar Al Shifa Medical Centre",
    "phone": "36554343",
    "email": "rameen@daralshifa.com.bh"
  },
  {
    "name": "DR. RIFAT AKTER",
    "occupation": "Medical Director, Dar Al Shifa Medical Centre",
    "phone": "34007917",
    "email": "dr.rifat@daralshifa.com.bh"
  },
  {
    "name": "DR. BASHEER AHAMED",
    "occupation": "Medical Director, Dar Al Shifa Medical Centre",
    "phone": "39289936",
    "email": "dr.basheer@daralshifa.com.bh"
  },
  {
    "name": "DR. SUJAI SUKUMARAN",
    "occupation": "Head of Dental Department, Dar Al Shifa Medical Centre",
    "phone": "38803849",
    "email": "dr.sujai@daralshifa.com.bh"
  },
  {
    "name": "DR. ASHFAQ HUSSAIN",
    "occupation": "Head of Dental Department, Dar Al Shifa Medical Centre",
    "phone": "33226919",
    "email": "dr.ashfaq@daralshifa.com.bh"
  },
  {
    "name": "DR. PRINCE PAPPACHAN",
    "occupation": "General Dentist, IMA Medical Center, Tubli",
    "phone": "39441063",
    "email": "drprinceacl2@gmail.com"
  },
  {
    "name": "ANEESH SREEDHARAN",
    "occupation": "General Secretary, ICRF (Indian Community Relief Fund)",
    "phone": "39401394",
    "email": "aneeshas2002@gmail.com"
  },
  {
    "name": "ANVER NILAMBUR",
    "occupation": "President, Canoly Nilambur Bahrain Koottayma",
    "phone": "36617657",
    "email": ""
  },
  {
    "name": "DR. SALAM MAMPATTU MOOLA",
    "occupation": "President, Manama Central Market Association",
    "phone": "33748156",
    "email": ""
  },
  {
    "name": "DEEPAK THANAL",
    "occupation": "Artist and Social Worker",
    "phone": "38431384",
    "email": "deepakthanal7@gmail.com"
  },
  {
    "name": "LATHEEF MARAKKATTU",
    "occupation": "General Manager (Commercial), Al Sayyad Transport Est; Treasurer, MCMA Bahrain",
    "phone": "33614955",
    "email": "latheef.marakkat@gmail.com"
  },
  {
    "name": "GIBI JOHN VARGHESE",
    "occupation": "President, United Nurses Association - Bahrain Chapter",
    "phone": "39043910",
    "email": "gibij92@gmail.com"
  },
  {
    "name": "ANAS RAHIM",
    "occupation": "President, Muharaq Malayali Samajam; Vice President, IYCC Bahrain; Voice of Alleppey",
    "phone": "33874100",
    "email": "anasrahimkylm@gmail.com"
  },
  {
    "name": "DR. SREEDEVI SREERAMA RAJAN",
    "occupation": "Ex-President, Bahrain Kerala Physio Forum; Member - Working Committee, Pravasi Legal Cell",
    "phone": "33130821",
    "email": "sreedevi.physio@gmail.com"
  },
  {
    "name": "MURALIKRISHNAN KUNHIRAMAN",
    "occupation": "Convener, ICRF Spectra; General Secretary, Kerala Engineers Forum",
    "phone": "34117864",
    "email": "muralimayyil@gmail.com"
  },
  {
    "name": "RAMSHAD AYILAKKAD",
    "occupation": "President, OICC Malappuram District Committee; General Secretary, Indian Youth Congress International",
    "phone": "32224314",
    "email": "ramshadtk89@gmail.com"
  },
  {
    "name": "JACOB THEKKUTHODE",
    "occupation": "President, Seven Arts Cultural Forum",
    "phone": "37750755",
    "email": "jacobtk260@gmail.com"
  },
  {
    "name": "KATHU SACHINDEV",
    "occupation": "Excom Member, Karunya Welfare Forum - Bahrain Chapter",
    "phone": "36302047",
    "email": "kathu.sachindev@gmail.com"
  },
  {
    "name": "SHIBIN THOMAS ABRAHAM",
    "occupation": "President, Indian Youth Cultural Congress (IYCC Bahrain)",
    "phone": "35510845",
    "email": "shibinchemmarikkad@gmail.com"
  },
  {
    "name": "SUNIL BABU",
    "occupation": "President, Padav Family Community; Secretary, Ernakulam Jilla Pravasi; Chief Coordinator, Maithri Bahrain; Bahrain Coordinator, Ernakulam Pravasi Expravasi Global Association",
    "phone": "33532669",
    "email": "sunilbabu3353@gmail.com"
  },
  {
    "name": "BABU MAHE",
    "occupation": "President, Samsa Samskarika Samithi",
    "phone": "33744317",
    "email": "baburajanmahe@gmail.com"
  },
  {
    "name": "MANIKKUTTAN KTM",
    "occupation": "Social Worker",
    "phone": "38899576",
    "email": "manikuttanktm@gmail.com"
  },
  {
    "name": "BASHEER AMBALAYI",
    "occupation": "President, Gulf Malayali Federation - GCC",
    "phone": "33982363",
    "email": "gulfsat@hotmail.com"
  },
  {
    "name": "NISAR KOLLAM",
    "occupation": "Founder President & Central Committee Member, Kollam Pravasi Association; Executive Committee Member, HOPE, MAITHRI, CIGI",
    "phone": "33057631",
    "email": "nizarnmk2011@gmail.com"
  },
  {
    "name": "LATHEEF AYANCHERY",
    "occupation": "Former President, Pravasi Guidance Forum; OICC Bahrain National Committee Treasurer",
    "phone": "39605806",
    "email": ""
  },
  {
    "name": "HARMINDER KAUR GABA",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "38415171",
    "email": "harmindergaba3@gmail.com"
  },
  {
    "name": "ARTI AGARWAL",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "39895971",
    "email": "artiagarwal.70@gmail.com"
  },
  {
    "name": "ALTHEA D'SOUZA REEVES",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "39895971",
    "email": ""
  },
  {
    "name": "BRAINY TOMAR",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "36100189",
    "email": "brainy.tomar@gmail.com"
  },
  {
    "name": "RAJI MURALI",
    "occupation": "Social Worker, ICRF Bahrain; President, Angels Toastmasters Club; Program Director, Dr. APJ Abdul Kalam International Foundation",
    "phone": "39895971",
    "email": "rajimuraliem@gmail.com"
  },
  {
    "name": "SWAPNA GOWLI",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "33328865",
    "email": "gowlisj@gmail.com"
  },
  {
    "name": "ANU JOSE",
    "occupation": "Joint Coordinator Ladies Wing & EC Member, ICRF Bahrain",
    "phone": "36836640",
    "email": "anujosep@gmail.com"
  },
  {
    "name": "DEEPSHIKHA SARAOGI",
    "occupation": "ICRF Executive Committee (ICRF LIFE Coordinator & ICRF Women's Forum), ICRF Bahrain",
    "phone": "34320957",
    "email": "deepshikhasaraogi@gmail.com"
  },
  {
    "name": "HEMLATA SINGH",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "37395593",
    "email": "drhlsingh@gmail.com"
  },
  {
    "name": "NIMMI ROSHAN",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "3989591",
    "email": ""
  },
  {
    "name": "RUCHI CHAKRABARTI",
    "occupation": "Executive Committee Member, ICRF Bahrain",
    "phone": "3989591",
    "email": "ruchitaneja2000@gmail.com"
  },
  {
    "name": "SHYAMALA CT",
    "occupation": "Social Worker, ICRF Bahrain",
    "phone": "33618726",
    "email": "shyamala2007physics@gmail.com"
  },
  {
    "name": "SANDRA PALANNA",
    "occupation": "Executive Committee Member, ICRF Bahrain; Social Worker, ICRF - Women's Forum",
    "phone": "33155462",
    "email": "sandrapalanna@gmail.com"
  }
]  # Your complete JSON data here

# Define occupation categories and their keywords with priority order
OCCUPATION_CATEGORIES = {
    'Doctor': [
        'doctor', 'dr.', 'surgeon', 'physician', 'dentist', 'medical', 'hospital',
        'consultant', 'specialist', 'clinician', 'practitioner', 'dermatologist',
        'orthopedic', 'orthopaedic', 'cardiologist', 'gynecologist', 'pediatrician', 
        'psychiatrist', 'radiologist', 'anesthesiologist', 'neurologist', 'nephrologist',
        'gastroenterologist', 'ophthalmologist', 'pathologist', 'psychologist',
        'medical director', 'health', 'clinic', 'medicine', 'dietician'
    ],
    'Manager': [
        'manager', 'managing director', 'director', 'ceo', 'chief executive officer', 
        'general manager', 'senior manager', 'head of', 'country manager', 'operations manager',
        'sales manager', 'marketing manager', 'project manager', 'branch manager',
        'finance manager', 'hr manager', 'admin manager', 'technical manager',
        'president', 'chairman', 'principal', 'executive director', 'group head',
        'chief', 'head', 'lead', 'supervisor', 'coordinator', 'controller'
    ],
    'Entrepreneur': [
        'entrepreneur', 'businessman', 'businesswoman', 'proprietor', 'owner',
        'founder', 'self-employed', 'startup', 'venture', 'enterprise',
        'managing director', 'ceo', 'director', 'partner', 'investor',
        'freelancer', 'consultant', 'contractor', 'business', 'trading',
        'company', 'w.l.l', 'co.', 'est.', 'group'
    ],
    'Social Worker': [
        'social worker', 'community service', 'welfare', 'humanitarian', 'charity',
        'relief fund', 'founder', 'president', 'secretary', 'treasurer', 'coordinator',
        'convener', 'member', 'volunteer', 'activist', 'philanthropist',
        'association', 'society', 'club', 'forum', 'center', 'centre',
        'cultural', 'welfare', 'help', 'support', 'care'
    ]
}

def categorize_occupation(occupation_text):
    """
    Categorize occupation based on keywords in the occupation text
    Returns the category name or empty string if no match found
    """
    if not occupation_text or occupation_text.strip() == "":
        return ""
    
    occupation_lower = occupation_text.lower()
    
    # Check each category in priority order
    for category, keywords in OCCUPATION_CATEGORIES.items():
        for keyword in keywords:
            # Use word boundaries to avoid partial matches
            if re.search(r'\b' + re.escape(keyword) + r'\b', occupation_lower):
                return category
    
    return ""

# Process the data and add occupation_category field
categorized_data = []

for person in data:
    # Create a copy of the person dictionary
    person_with_category = person.copy()
    
    # Get the occupation text
    occupation_text = person.get('occupation', '')
    
    # Categorize the occupation
    occupation_category = categorize_occupation(occupation_text)
    
    # Add the new field
    person_with_category['occupation_category'] = occupation_category
    
    categorized_data.append(person_with_category)

# Create the new JSON file
output_filename = "categorized_members.json"

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(categorized_data, f, indent=2, ensure_ascii=False)

print(f"✅ Categorized data saved to {output_filename}")

# Print some statistics
categories_count = {}
for person in categorized_data:
    category = person['occupation_category']
    categories_count[category] = categories_count.get(category, 0) + 1

print("\n📊 Category Statistics:")
for category, count in sorted(categories_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {category if category else 'Uncategorized'}: {count}")

# Show some examples
print("\n👥 Sample Categorized Entries:")
for i, person in enumerate(categorized_data[:10]):
    print(f"  {i+1}. {person['name']} -> {person['occupation_category']}")