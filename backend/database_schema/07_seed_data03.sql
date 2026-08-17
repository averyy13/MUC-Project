-- ======================================================
-- MEDICAL FACILITIES SEED (Fully Translated address_mm)
-- ======================================================
INSERT INTO medical_facilities (name_en, name_mm, phone, address_en, address_mm, type, location) VALUES
(
    'Yangon General Hospital', 'ရန်ကုန်ပြည်သူ့ဆေးရုံကြီး', '01256112', 
    'Bogyoke Aung San Road, Latha Township', 'ဗိုလ်ချုပ်အောင်ဆန်းလမ်း၊ လသာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1534 16.7797)')
),
(
    'Yangon Specialty Hospital (500 Bedded)', 'ရန်ကုန်အထူးကုဆေးရုံ (ကုတင် ၅၀၀)', '01222868', 
    'Min Ye Kyaw Swar Road, Lanmadaw Township', 'မင်းရဲကျော်စွာလမ်း၊လမ်းမတော်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1408 16.7844)')
),
(
    'North Okkalapa General Hospital', 'မြောက်ဥက္ကလာပ အထွေထွေရောဂါကုဆေးရုံကြီး', '019699623', 
    'Khanthamar Road, North Okkalapa Township', 'ခန္ဓာမာလမ်း၊ မြောက်ဥက္ကလာပမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1408 16.9056)')
),
(
    'Thingangyun San Pya General Hospital', 'သင်္ဃန်းကျွန်းစံပြဆေးရုံကြီး', '01570597', 
    'Pyidaungsu Road, Thingangyun Township', 'ပြည်ထောင်စုလမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2058 16.8202)')
),
(
    'Yangon West General Hospital', 'ရန်ကုန်အနောက်ပိုင်းဆေးရုံကြီး', '01222872', 
    'Lower Kyimyindaing Road, Ahlone Township', 'အောက်ကြည့်မြင်တိုင်လမ်း၊ အလုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1248 16.7905)')
),
(
    'Insein General Hospital', 'အင်းစိန်ပြည်သူ့ဆေးရုံကြီး', '01640032', 
    'Mingalardon Road, Insein Township', 'မင်္ဂလာဒုံလမ်း၊ အင်းစိန်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1114 16.8893)')
),
(
    'Yangon Children''s Hospital', 'ရန်ကုန်ကလေးဆေးရုံကြီး', '01222807', 
    'Pyay Road, Dagon Township', 'ပြည်လမ်း၊ ဒဂုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1362 16.7932)')
),
(
    'Central Women''s Hospital', 'ဗဟိုအမျိုးသမီးဆေးရုံကြီး (မီးဖွားဆောင်)', '01222811', 
    'Corner of Pyay Road & Ahlone Road, Dagon', 'ပြည်လမ်းနှင့် အလုံလမ်းထောင့်၊ ဒဂုံ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1365 16.7892)')
),
(
    'Eye, Ear, Nose and Throat (EENT) Hospital', 'မျက်စိ၊ နား၊ နှာခေါင်း၊ လည်ပင်း အထူးကုဆေးရုံကြီး', '01384420', 
    'Alan Pya Pagoda Road, Dagon Township', 'အလံပြဘုရားလမ်း၊ ဒဂုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1583 16.7861)')
),
(
    'Yangon Orthopaedic Hospital', 'ရန်ကုန်အရိုးရောဂါကုဆေးရုံကြီး', '01524155', 
    'Kyimyindaing Road, Kyimyindaing Township', 'ကြည့်မြင်တိုင်လမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1175 16.7942)')
),
(
    'Mingaladon General Hospital (500 Bedded)', 'မင်္ဂလာဒုံ အထွေထွေရောဂါကုဆေးရုံကြီး (ကုတင် ၅၀၀)', '01635327', 
    'Pyay Road, Mingalardon Township', 'ပြည်လမ်း၊ မင်္ဂလာဒုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1042 16.9831)')
),
(
    'Yway Tha Gyi Mental Health Hospital', 'ဆန်ပြပြဇာတ်ရုံအနီး စိတ်ကျန်းမာရေးဆေးရုံကြီး (ရွာသာကြီး)', '01584067', 
    'East Dagon Township, Yangon', 'ဒဂုံမြို့သစ်အရှေ့ပိုင်းမြို့နယ်၊ ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2625 16.8845)')
),
(
    'South Dagon Public Hospital', 'တောင်ဒဂုံ ပြည်သူ့ဆေးရုံကြီး', '01589133', 
    'University Road, South Dagon Township', 'တက္ကသိုလ်လမ်း၊ ဒဂုံမြို့သစ်တောင်ပိုင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2238 16.8291)')
),
(
    'Hlaingthaya Public Hospital', 'လှိုင်သာယာ ပြည်သူ့ဆေးရုံကြီး', '01684307', 
    'Yangon-Pathein Highway Road, Hlaingthaya', 'ရန်ကုန်-ပုသိမ် အဝေးပြေးလမ်း၊ လှိုင်သာယာ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.0611 16.8654)')
),
(
    'Bedded 100 Tharkayta Hospital', 'သာကေတ အထူးကုဆေးရုံ', '01556402', 
    'Ayeyarwun Road, Thaketa Township', 'ဧရာဝဏ်လမ်း၊ သာကေတမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2163 16.7981)')
),
(
    'Hematology and Children''s Oncology Hospital', 'သွေးကင်ဆာနှင့် ကလေးကင်ဆာအထူးကုဆေးရုံကြီး', '01581452', 
    '27th Ward, North Dagon Township', '၂၇ရပ်ကွက်၊ ဒဂုံမြို့သစ်မြောက်ပိုင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1895 16.8722)')
),
(
    'North Dagon Public Hospital', 'ဒဂုံမြို့သစ်မြောက်ပိုင်း ပြည်သူ့ဆေးရုံကြီး', '01580219', 
    'Panglong Road, North Dagon Township', 'ပင်လုံလမ်း၊ ဒဂုံမြို့သစ်မြောက်ပိုင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1942 16.8524)')
),
(
    'East Dagon Public Hospital', 'ဒဂုံမြို့သစ်အရှေ့ပိုင်း ပြည်သူ့ဆေးရုံကြီး', '01585122', 
    'Minye Kyawswa Road, East Dagon', 'မင်းရဲကျော်စွာလမ်း၊ ဒဂုံမြို့သစ်အရှေ့ပိုင်း', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2415 16.8912)')
),
(
    'Yangon Dermatology Hospital', 'ရန်ကုန်အရေပြားရောဂါကုဆေးရုံကြီး', '01662453', 
    'Kaba Aye Pagoda Road, Mayangone Township', 'ကမ္ဘာအေးဘုရားလမ်း၊ မရမ်းကုန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1548 16.8451)')
),
(
    'Kaba Aye Infectious Disease Hospital', 'ကမ္ဘာအေး ကူးစက်ရောဂါကုဆေးရုံကြီး', '01660122', 
    'Kaba Aye Pagoda Road, Mayangone Township', 'ကမ္ဘာအေးဘုရားလမ်း၊ မရမ်းကုန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1562 16.8511)')
),
(
    'Sanchaung Township Public Hospital', 'စမ်းချောင်းမြို့နယ် ပြည်သူ့ဆေးရုံ', '01535402', 
    'Pyay Road, Sanchaung Township', 'ပြည်လမ်း၊ စမ်းချောင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1314 16.8112)')
),
(
    'Bahan Township Public Hospital', 'ဗဟန်းမြို့နယ် ပြည်သူ့ဆေးရုံ', '01549521', 
    'Pyay Road, Sanchaung Township', 'ပြည်လမ်း၊ စမ်းချောင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1512 16.8045)')
),
(
    'Kamayut Township Public Hospital', 'ကမာရွတ်မြို့နယ် ပြည်သူ့ဆေးရုံ', '01525203', 
    'Hledan Road, Kamayut Township', 'လှည်းတန်းလမ်း၊ ကမာရွတ်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1284 16.8241)')
),
(
    'Victoria Hospital', 'ဝိတိုရိယဆေးရုံ', '09666141', 
    'No.68, Taw Win Road, Mayangone Township', 'အမှတ်၆၈၊ တော်ဝင်လမ်း၊ မရမ်းကုန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1181 16.8553)')
),
(
    'Asia Royal Hospital', 'အာရှတော်ဝင်ဆေးရုံ', '012304999', 
    'No.14, Baho Road, Sanchaung Township', 'အမှတ်၁၄၊ ဗဟိုလမ်း၊ စမ်းချောင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1265 16.8553)')
),
(
    'Pun Hlaing Hospital', 'ပန်းလှိုင်ဆေးရုံ', '09772889922', 
    'Pun Hlaing Ave, Hlaing Tharyar Township', 'ပန်းလှိုင်အိမ်ရာ၊ လှိုင်သာယာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.0624 16.8621)')
),
(
    'Parami Hospital', 'ပါရမီအထွေထွေရောဂါကုဆေးရုံ', '01657232', 
    'No-60, G-1, New Parami Road, Mayangone', 'အမှတ်-၆၀၊ ဂ-၁၊ ပါရမီ(သစ်)လမ်း၊ မရမ်းကုန်း', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1345 16.8504)')
),
(
    'Pinlon Hospital', 'ပင်လုံဆေးရုံ', '013581616', 
    'No.9, Saya San Road, Dagon Seikkan Township', 'အမှတ်၉၊ ဆရာစံလမ်း၊ ဒဂုံဆိပ်ကမ်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.2201 16.8285)')
),
(
    'Grand Hantha Hospital', 'ဂရန်းဟံသာဆေးရုံ', '012317600', 
    'No.3, Corner of Nar Nat Taw St & Kyee Myin Daing Rd, Kamayut', 'အမှတ်၃၊ နာနတ်တောလမ်းနှင့် ကြည့်မြင်တိုင်လမ်းထောင့်၊ ကမာရွတ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1147 16.8123)')
),
(
    'Kantha Yar International Hospital', 'ကံသာယာအင်တာနေရှင်နယ်ဆေးရုံ', '01400083', 
    'No.87, Kan Yeik Tha Road, Mingalar Taung Nyunt', 'အမှတ်၈၇၊ ကန်ရိပ်သာလမ်း၊ မင်္ဂလာတောင်ညွန့်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1685 16.7925)')
),
(
    'Sakura Hospital', 'ဆာကူရာဆေးရုံ', '01512668', 
    'No.23, Shin Saw Pu Road, Sanchaung Township', 'အမှတ်၂၃၊ ရှင်စောပုလမ်း၊ စမ်းချောင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1287 16.8014)')
),
(
    'SSC Hospital', 'ရွှေဂုံတိုင်အထူးကုဆေးရုံ', '01544116', 
    'No.7, Shwe Gon Daing Gyi St, Bahan Township', 'အမှတ်၇၊ ရွှေဂုံတိုင်ကြီးလမ်း၊ ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1554 16.8062)')
),
(
    'Bahan General Hospital', 'ဇီဝိတဒါန သံဃာ့ဆေးရုံကြီး', '01543169', 
    'Kaba Aye Pagoda Road, Bahan Township', 'ကမ္ဘာအေးဘုရားလမ်း၊ ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1594 16.8105)')
),
(
    'Okkala Hospital', 'အိုက္ကလာဆေးရုံ', '014706622', 
    'No.137/D, Thudhamma Road, North Okkalapa', 'အမှတ်၁၃၇/D၊ သုဓမ္မာလမ်း၊ မြောက်ဥက္ကလာပ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1705 16.9022)')
),
(
    'Ar Yu Hospital', 'အာယုအင်တာနေရှင်နယ်ဆေးရုံ', '019376200', 
    'No.400, U Wisara Road, Bahan Township', 'အမှတ်၄၀၀၊ ဦးဝိစာရလမ်း၊ ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1432 16.8145)')
),
(
    'Sabal Hospital', 'စံပယ်အထူးကုဆေးရုံ', '01504332', 
    'No.56, Insein Road, Kamayut Township', 'အမှတ်၅၆၊ အင်းစိန်လမ်း၊ ကမာရွတ်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1215 16.8324)')
),
(
    'Marlar Myaing Hospital', 'မာလာမြိုင်ဆေးရုံ', '01507114', 
    'No.24, Marlar Myaing St, 16 Ward, Hlaing', 'အမှတ်၂၄၊ မာလာမြိုင်လမ်း၊ ၁၆ရပ်ကွက်၊ လှိုင်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1192 16.8485)')
),
(
    'Taw Win Hospital', 'တော်ဝင်ဆေးရုံ', '01534347', 
    'No.33, University Avenue Road, Bahan Township', 'အမှတ်၃၃၊ တက္ကသိုလ်ရိပ်သာလမ်း၊ ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1482 16.8251)')
),
(
    'Myat Taw Win Hospital', 'မြတ်တော်ဝင်ဆေးရုံ', '01211470', 
    'No.308, Ahlone Road, Ahlone Township', 'အမှတ်၃၀၈၊ အလုံလမ်း၊ အလုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1264 16.7885)')
),
(
    'Shin Par Gu Hospital', 'ရှင်ပါဂူဆေးရုံ', '01537755', 
    'No.462, Pyay Road, Kamayut Township', 'အမှတ်၄၆၂၊ ပြည်လမ်း၊ ကမာရွတ်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1662 16.8095)')
),
(
    'Aung Yadana Hospital', 'အောင်ရတနာဆေးရုံ', '018561140', 
    'No.553, Waizayandar Road, South Okkalapa', 'အမှတ်၅၅၃၊ ဝေဇယန္တာလမ်း၊ တောင်ဥက္ကလာပ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1854 16.8412)')
),
(
    'Famous Hospital', 'ကမ္ဘာကျော်ဆေးရုံ', '012301144', 
    'No.86, Hnin Si Gone Road, Ahlone Township', 'အမှတ်၈၆၊ နှင်းဆီကုန်းလမ်း၊ အလုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1212 16.7914)')
),
(
    'Min Dhama Hospital', 'မင်းဓမ္မအထူးကုဆေးရုံ', '01657930', 
    'No.24, Min Dhama Road, Mayangone Township', 'အမှတ်၂၄၊ မင်းဓမ္မလမ်း၊ မရမ်းကုန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1235 16.8812)')
),
(
    'SAM Hospital', 'စင်ကာပူ-မြန်မာ အထူးကုဆေးရုံ', '01542283', 
    'No.234, Kaba Aye Pagoda Road, Bahan Township', 'အမှတ်၂၃၄၊ ကမ္ဘာအေးဘုရားလမ်း၊ ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1581 16.8122)')
),
(
    'Bahosi Hospital', 'ဗဟိုစည်ဆေးရုံ', '012302171', 
    'Bogyoke Aung San Road, Lanmadaw Township', 'ဗိုလ်ချုပ်အောင်ဆန်းလမ်း၊လမ်းမတော်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1374 16.7811)')
),
(
    'Aung Chan Tha Specialist Clinic', 'အောင်ချမ်းသာအထူးကုဆေးခန်း', '09420011223', 
    'Thudhamma Road, (G) Ward, North Okkalapa Township', 'သုဓမ္မာလမ်း၊ (ဂ)ရပ်ကွက်၊ မြောက်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1682 16.9025)')
),
(
    'Sein Ge Har Specialist Clinic', 'စိန်ဂေဟာအထူးကုဆေးခန်း', '09250011334', 
    'Thudhamma Road, (2) Ward, North Okkalapa Township', 'သုဓမ္မာလမ်း၊ (၂)ရပ်ကွက်၊ မြောက်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1695 16.9081)')
),
(
    'Saw Maha Specialist Clinic', 'စောမဟာအထူးကုဆေးခန်း', '01642115', 
    'Insein Road, Ywama West Ward, Insein Township', 'အင်းစိန်လမ်း၊ ရွာမအနောက်ရပ်ကွက်၊ အင်းစိန်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1152 16.8921)')
),
(
    'Great Wall Specialist Clinic', 'ဂရိတ်ဝေါအထူးကုဆေးခန်း', '09777123456', 
    'Pauk Taw Wa Junction, Insein Township', 'ပေါက်တောဝလမ်းဆုံ၊ အင်းစိန်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1185 16.8854)')
),
(
    'Myat Mon Specialist Clinic', 'မြတ်မွန်အထူးကုဆေးခန်း', '01377889', 
    'Pyay Road, Dagon Township', 'ပြည်လမ်း၊ ဒဂုံမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1385 16.7912)')
),
(
    'Taw Win Specialist Clinic', 'တော်ဝင်အထူးကုဆေးခန်း', '095012345', 
    'Ahlone Road, Dagon Township', 'အလုံလမ်း၊ ဒဂုံမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1352 16.7885)')
),
(
    'Thukha Meitta Specialist Clinic', 'သုခမေတ္တာအထူးကုဆေးခန်း', '01507223', 
    'Insein Road, (16) Ward, Hlaing Township', 'အင်းစိန်လမ်း၊ (၁၆)ရပ်ကွက်၊ လှိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1205 16.8492)')
),
(
    'Shwe Lin Yone Clinic', 'ရွှေလင်းယုန်ဆေးခန်း', '09450099887', 
    'Thamaing (2) Street, Hlaing Township', 'သမိုင်း(၂)လမ်း၊ လှိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1189 16.8581)')
),
(
    'Lanmadaw Specialist Clinic', 'လမ်းမတော်အထူးကုဆေးခန်း', '01221144', 
    'Anawrahta Road, Lanmadaw Township', 'Anawrahta လမ်း၊လမ်းမတော်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1412 16.7785)')
),
(
    'Shwe Pyi Thu Specialist Clinic', 'ရွှေပြည်သူအထူးကုဆေးခန်း', '09970112233', 
    'Maha Bandula Road, Lanmadaw Township', 'မဟာဗန္ဓုလလမ်း၊လမ်းမတော်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1435 16.7762)')
),
(
    'Pinlon Specialist Clinic', 'ပင်လုံအထူးကုဆေးခန်း', '09421055667', 
    'Panglong Road, (35) Ward, North Dagon Township', 'ပင်လုံလမ်း၊ (၃၅)ရပ်ကွက်၊ ဒဂုံမြို့သစ်မြောက်ပိုင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1942 16.8542)')
),
(
    'Thathana Alinn Specialist Clinic', 'သာသနာ့အလင်းအထူးကုဆေးခန်း', '09260114455', 
    'Bohmu Ba Htoo Road, North Dagon Township', 'ဗိုလ်မှူးဗထူးလမ်း၊ ဒဂုံမြို့သစ်မြောက်ပိုင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1915 16.8621)')
),
(
    'Yangon General Hospital - YGH', 'ရန်ကုန် အထွေထွေရောဂါကု ဆေးရုံကြီး', '01256112', 
    'Bogyoke Aung San Road, Latha Township', 'ဗိုလ်ချုပ်အောင်ဆန်းလမ်း၊ လသာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1505 16.7788)')
),
(
    'Dental Hospital - Latha', 'အမှတ် (၁) သွားဘက်ဆိုင်ရာ ဆေးရုံကြီး', '01221546', 
    'Min Ye Kyaw Swar Road, Latha Township', 'မင်းရဲကျော်စွာလမ်း၊ လသာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1478 16.7812)')
),
(
    'Eindra Specialist Clinic', 'အိန္ဒြာအထူးကုဆေးခန်း', '09450033221', 
    'Anawrahta Road, Latha Township', 'Anawrahta လမ်း၊ လသာမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.152 16.7765)')
),
(
    'Yangon Children Hospital', 'ရန်ကုန် ကလေးဆေးရုံကြီး - မင်္ဂလာတောင်ညွန့်', '01222811', 
    'Pyidaungsu Yeiktha Road, Mingalar Taung Nyunt Township', 'ပြည်ထောင်စုရိပ်သာလမ်း၊ မင်္ဂလာတောင်ညွန့်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1622 16.7831)')
),
(
    'Natmauk Specialist Clinic', 'နတ်မောက်အထူးကုဆေးခန်း', '09254112233', 
    'Natmauk Road, Mingalar Taung Nyunt Township', 'နတ်မောက်လမ်း၊ မင်္ဂလာတောင်ညွန့်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1635 16.791)')
),
(
    'Kandawgyi Specialist Clinic', 'ကန်တော်ကြီးအထူးကုဆေးခန်း', '01391122', 
    'Kandawgyi Circular Road, Mingalar Taung Nyunt Township', 'ကန်တော်ကြီးပတ်လမ်း၊ မင်္ဂလာတောင်ညွန့်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.164 16.7875)')
),
(
    'Yuzana Clinic', 'ယုဇနဆေးခန်း', '09421008899', 
    'Yuzana Garden City, Dagon Seikkan Township', 'ယုဇနဥယျာဉ်မြို့တော်၊ ဒဂုံဆိပ်ကမ်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.248 16.828)')
),
(
    'Maha Thukha Clinic', 'မဟာသုခဆေးခန်း', '09790112244', 
    'Creek Street, Ward 9, Dagon Seikkan Township', 'ချောင်းလမ်း၊ ၉ရပ်ကွက်၊ ဒဂုံဆိပ်ကမ်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.243 16.8205)')
),
(
    'Teza Clinic', 'တေဇဆေးခန်း', '09250044556', 
    'Yadanar Main Road, Dagon Seikkan Township', 'ရတနာလမ်းမကြီး၊ ဒဂုံဆိပ်ကမ်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.24 16.8235)')
),
(
    'Victoria Hospital Branch - Hlaingthaya', 'ဝိတိုရိယ အထူးကုဆေးရုံ', '01685511', 
    'Yangon-Pathein Road, Hlaingthaya Township', 'ရန်ကုန်-ပုသိမ်လမ်း၊ လှိုင်သာယာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.062 16.855)')
),
(
    'Nawaday Specialist Clinic', 'နဝဒေးအထူးကုဆေးခန်း', '09450113322', 
    'Nawaday Housing, Hlaingthaya Township', 'နဝဒေးအိမ်ရာ၊ လှိုင်သာယာမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.055 16.859)')
),
(
    'Magway Specialist Clinic', 'မကွေးအထူးကုဆေးခန်း', '09260118877', 
    'Bogyoke Road, Ward 5, Hlaingthaya Township', 'ဗိုလ်ချုပ်လမ်း၊ ၅ရပ်ကွက်၊ လှိုင်သာယာမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.065 16.851)')
),
(
    'Shwe Bahosi Specialist Clinic - Thaketa', 'ရွှေဗဟိုအထူးကုဆေးခန်း', '01551122', 
    'Ayeyarwun Road, Thaketa Township', 'ဧရာဝဏ်လမ်း၊ သာကေတမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.206 16.793)')
),
(
    'Meitta San Clinic', 'မေတ္တာစမ်းဆေးခန်း', '09420077889', 
    'Shwe Thaung Yan Road, Thaketa Township', 'ရွှေသောင်ယံလမ်း၊ သာကေတမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.203 16.7895)')
),
(
    'Sanda Specialist Clinic', 'စန္ဒာအထူးကုဆေးခန်း', '09770114455', 
    'Yushu Street, Thaketa Township', 'ယုရှုလမ်း၊ သာကေတမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.21 16.796)')
),
(
    'Sein Gay Sar Clinic - South Dagon', 'စိန်ဂေဟာဆေးခန်း', '09450066778', 
    'No. 2 Main Road, South Dagon Township', 'အမှတ်(၂)လမ်းမကြီး၊ ဒဂုံမြို့သစ်တောင်ပိုင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.217 16.8811)')
),
(
    'Ayeyarwaddy Clinic', 'ဧရာဝတီဆေးခန်း', '09250114433', 
    'Pinlon Main Road, South Dagon Township', 'ပင်လုံလမ်းမကြီး၊ ဒဂုံမြို့သစ်တောင်ပိုင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.22 16.8165)')
),
(
    'Aye Meitta Clinic', 'အေးမေတ္တာဆေးခန်း', '09970115566', 
    'Ward 56, South Dagon Township', '၅၆ရပ်ကွက်၊ ဒဂုံမြို့သစ်တောင်ပိုင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.212 16.805)')
),
(
    'Specialist Hospital Mingalardon', 'အထူးကုဆေးရုံကြီး - မင်္ဂလာဒုံ', '01637100', 
    'Pyay Road, Mingalardon Township', 'ပြည်လမ်း၊ မင်္ဂလာဒုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.14 16.925)')
),
(
    'Zaykabar Clinic', 'ဇေကမ္ဘာဆေးခန်း', '01620112', 
    'Zaykabar Compound, Mingalardon Township', 'ဇေကမ္ဘာဝင်း၊ မင်္ဂလာဒုံမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.15 16.94)')
),
(
    'Shwe Pyi Thar Specialist Clinic', 'ရွှေပြည်သာအထူးကုဆေးခန်း', '09420011998', 
    'Mingalardon Garden, Mingalardon Township', 'မင်္ဂလာဒုံဥယျာဉ်၊ မင်္ဂလာဒုံမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.145 16.931)')
),
(
    'Teaching Hospital - Kyimyindaing', 'အမှတ် (၂) စာသင်ဆေးရုံကြီး', '01512211', 
    'Lower Kyimyindaing Road, Kyimyindaing Township', 'အောက်ကြည့်မြင်တိုင်လမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.114 16.7925)')
),
(
    'Sabai Clinic - Kyimyindaing', 'စံပယ်ဆေးခန်း', '09450118833', 
    'Pan Htein Tan Street, Kyimyindaing Township', 'ပန်းထိမ်တန်းလမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.117 16.788)')
),
(
    'Thiri Mingalar Clinic', 'သီရိမင်္ဂလာဆေးခန်း', '09260113344', 
    'Thiri Mingalar Street, Kyimyindaing Township', 'သီရိမင်္ဂလာလမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1155 16.788)')
),
(
    'Oscar General Hospital', 'အော်စကာ အထူးကုဆေးရုံ', '01577889', 
    'Lay Daungkan Road, Thingangyun Township', 'လေးထောင့်ကန်လမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1935 16.82)')
),
(
    'Sanpya Specialist Clinic', 'စံပြအထူးကုဆေးခန်း', '09421002211', 
    'Yadanar Road, Thingangyun Township', 'ရတနာလမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.196 16.8225)')
),
(
    'Thukha Meitta Private Hospital', 'သုခမေတ္တာဆေးရုံ', '01564433', 
    'Aung Zeya Road, Thingangyun Township', 'အောင်ဇေယျလမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.191 16.817)')
),
(
    'Maydhawi Specialist Clinic', 'မေဓါဝီ အထူးကုဆေးခန်း', '01570112', 
    'Maydhawi Road, South Okkalapa Township', 'မေဓာဝီလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.173 16.836)')
),
(
    'Yadanar Specialist Clinic', 'ရတနာအထူးကုဆေးခန်း', '09450088990', 
    'Thanthumar Road, South Okkalapa Township', 'သံသုမာလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.177 16.84)')
),
(
    'Jivaka Clinic - South Okkalapa', 'ဇီဝကဆေးခန်း', '09250117766', 
    'Ward 7, South Okkalapa Township', '၇ရပ်ကွက်၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1745 16.834)')
),
(
    'Academy Private Hospital', 'အကယ်ဒမီပုဂ္ဂလိကဆေးရုံ', '01552233', 
    'Kyauk Myaung Street, Tamwe Township', 'ကျောက်မြောင်းလမ်း၊ တာမွေမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1735 16.8062)')
),
(
    'Shwe Yaung Chanthar Clinic', 'ရွှေရောင်ချမ်းသာဆေးခန်း', '0955012345', 
    'Insein Road, Hlaing Township', 'အင်းစိန်လမ်း၊ လှိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1234 16.8401)')
),
(
    'City Care Specialist Clinic', 'စီးတီးကဲရ်အထူးကုဆေးခန်း', '0942001122', 
    'Thanthumar Road, South Okkalapa Township', 'သံသုမာလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.184 16.845)')
),
(
    'Khit Thit Polyclinic', 'ခေတ်သစ်အထွေထွေရောဂါကုဆေးခန်း', '0979888111', 
    'Banyar Dala Road, Mingalar Taung Nyunt', 'ဗညားဒလလမ်း၊ မင်္ဂလာတောင်ညွန့်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.165 16.7922)')
),
(
    'Golden Star Women and Children Clinic', 'ရွှေကြယ် မိခင်နှင့်ကလေးဆေးခန်း', '0995544332', 
    'Waizayandar Road, South Okkalapa Township', 'ဝေဇယန္တာလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.182 16.8395)')
),
(
    'Aung Myitta General Clinic', 'အောင်မေတ္တာအထွေထွေဆေးခန်း', '0926008899', 
    'Bogyoke Road, Pazundaung Township', 'ဗိုလ်ချုပ်လမ်း၊ ပုဇွန်တောင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.172 16.7795)')
),
(
    'Family Health Center', 'မိသားစုကျန်းမာရေးစောင့်ရှောက်မှုဆေးခန်း', '01377888', 
    'Maha Bandula Road, Botahtaung Township', 'မဟာဗန္ဓုလလမ်း၊ ဗိုလ်တထောင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1685 16.776)')
),
(
    'Pinlon Specialist Clinic', 'ပင်လုံအထူးကုဆေးခန်း', '0950112233', 
    'Myittar Road, South Okkalapa Township', 'မေတ္တာလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1802 16.8375)')
),
(
    'Yankin Children Hospital', 'ရန်ကင်းကလေးဆေးရုံကြီး', '01556011', 
    'Min Ye Kyaw Swar Road, Yankin Township', 'မင်းရဲကျော်စွာလမ်း၊ ရန်ကင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.16 16.832)')
),
(
    'Worker''s Hospital - Tamwe', 'အလုပ်သမားဆေးရုံကြီး', '01551122', 
    'Kyaikkasan Road, Tamwe Township', 'ကျိုက္ကဆံလမ်း၊ တာမွေမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.175 16.808)')
),
(
    'San Pya Clinic - Yankin', 'စံပြဆေးခန်း', '0945009988', 
    'Moe Kaung Road, Yankin Township', 'မိုးကောင်းလမ်း၊ ရန်ကင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1625 16.8315)')
),
(
    'Thukha Waddy Specialist Clinic', 'သုခဝတီအထူးကုဆေးခန်း', '0925008877', 
    'Insein Road, Hlaing Township', 'အင်းစိန်လမ်း၊ လှိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.126 16.842)')
),
(
    'Shwe La Min Hospital - North Okkalapa', 'ရွှေလမင်းဆေးရုံကြီး', '019692233', 
    'Thudhamma Road, North Okkalapa Township', 'သုဓမ္မာလမ်း၊ မြောက်ဥက္ကလာပမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1435 16.908)')
),
(
    'Mingalar Clinic', 'မင်္ဂလာဆေးခန်း', '0945112244', 
    'U Wisara Road, Dagon Township', 'ဦးဝိစာရလမ်း၊ ဒဂုံမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.141 16.792)')
),
(
    'Myat Mon Private Hospital', 'မြတ်မွန်ပုဂ္ဂလိကဆေးရုံ', '01650011', 
    'Parami Road, South Okkalapa Township', 'ပါရမီလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.178 16.848)')
),
(
    'East Yangon General Hospital - Botahtaung', 'ရန်ကုန်အရှေ့ပိုင်းဆေးရုံကြီး', '01292111', 
    'Merchant Road, Botahtaung Township', 'ကုန်သည်လမ်း၊ ဗိုလ်တထောင်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.171 16.7725)')
),
(
    'Great Wall Specialist Clinic', 'ဂရိတ်ဝေါအထူးကုဆေးခန်း', '09977885522', 
    'Hledan Road, Kamayut Township', 'လှည်းတန်းလမ်း၊ ကမာရွတ်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.127 16.826)')
),
(
    'Metta Clinic', 'မေတ္တာဆေးခန်း', '0943001122', 
    'Lower Kyimyindaing Road, Kyimyindaing Township', 'အောက်ကြည့်မြင်တိုင်လမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.115 16.793)')
),
(
    'Sanda Clinic - Tamwe', 'စန္ဒာဆေးခန်း', '0926004455', 
    'Banyar Dala Road, Tamwe Township', 'ဗညားဒလလမ်း၊ တာမွေမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.172 16.804)')
),
(
    'Sithu Specialist Clinic', 'စည်သူအထူးကုဆေးခန်း', '0979008899', 
    'Shwe Gon Daing Road, Bahan Township', 'ရွှေဂုံတိုင်လမ်း၊ ဗဟန်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.155 16.808)')
),
(
    'Zabu Thiri Clinic', 'ဇမ္ဗူသီရိဆေးခန်း', '0942006677', 
    'Aung Zeya Road, Yankin Township', 'အောင်ဇေယျလမ်း၊ ရန်ကင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.164 16.833)')
),
(
    'Kyi Myin Daing Orthopedic Hospital', 'ကြည့်မြင်တိုင် အရိုးဆေးရုံ', '01222444', 
    'Kyimyindaing Road, Kyimyindaing Township', 'ကြည့်မြင်တိုင်လမ်း၊ ကြည့်မြင်တိုင်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1165 16.795)')
),
(
    'San Chaung Specialist Clinic', 'စမ်းချောင်းအထူးကုဆေးခန်း', '0945110033', 
    'Kyuntaw Road, Sanchaung Township', 'ကျွန်းတောလမ်း၊ စမ်းချောင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.13 16.805)')
),
(
    'Nadi Clinic', 'နဒီဆေးခန်း', '09252009988', 
    'Insein Road, Hlaing Township', 'အင်းစိန်လမ်း၊ လှိုင်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.124 16.843)')
),
(
    'Ayerwaddy Clinic', 'ဧရာဝတီဆေးခန်း', '0942008877', 
    'Pyay Road, Mayangone Township', 'ပြည်လမ်း၊ မရမ်းကုန်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.138 16.86)')
),
(
    'Hlaing Tharyar Model Clinic', 'လှိုင်သာယာစံပြဆေးခန်း', '0950115566', 
    'Yangon-Pathein Road, Hlaingthaya Township', 'ရန်ကုန်-ပုသိမ်လမ်း၊ လှိုင်သာယာမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.065 16.868)')
),
(
    'Thiri Clinic', 'သီရိဆေးခန်း', '0944002233', 
    'Myittar Road, South Okkalapa Township', 'မေတ္တာလမ်း၊ တောင်ဥက္ကလာပမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.181 16.838)')
),
(
    'Waso Clinic', 'ဝါဆိုဆေးခန်း', '0926117788', 
    'Thanthumar Road, Thingangyun Township', 'သံသုမာလမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.208 16.818)')
),
(
    'Myat Shin Specialist Clinic', 'မြတ်ရှင်အထူးကုဆေးခန်း', '0977882211', 
    'Ayeyarwun Road, Thaketa Township', 'ဧရာဝဏ်လမ်း၊ သာကေတမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.218 16.797)')
);