-- ======================================================
-- MEDICAL FACILITIES SEED (Properly Split & Translated)
-- Exact Coordinates Preserved
-- ======================================================
INSERT INTO medical_facilities (name_en, name_mm, phone, address_en, address_mm, type, location) VALUES
(
    'Yangon General Hospital', 'ရန်ကုန်ပြည်သူ့ဆေးရုံကြီး', '01256112', 
    'Bogyoke Aung San Road, Latha Township', 'ဗိုလ်ချုပ်အောင်ဆန်းလမ်း, လသာ မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.150555 16.779103)')
),
(
    'New Yangon General Hospital (500 Bedded)', 'ရန်ကုန်အထူးကုဆေးရုံကြီး (ခုတင် ၅၀၀)', '012301618', 
    'Min Ye Kyaw Swar Road, Lanmadaw Township', 'မင်းရဲကျော်စွာလမ်း, လမ်းမတော် မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.143796 16.78358)')
),
(
    'North Okkalapa General & Teaching Hospital', 'မြောက်ဥက္ကလာပ အထွေထွေရောဂါကုနှင့်သင်ကြားရေးဆေးရုံကြီး', '09420038487', 
    'May Darwi Road , Yangon, North Okkalapa Township', 'မေဓါဝီလမ်းကြီး , မြောက်ဥက္ကလာပ မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.156762 16.901176)')
),
(
    'Thingangyun Model General Hospital', 'သင်္ဃန်းကျွန်းစံပြဆေးရုံကြီး', '01579890', 
    'Kyaik Kasan Road, Thingangyun Township', 'ကျိုက်က္ကစံလမ်း၊ သင်္ဃန်းကျွန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.190661 16.834452)')
),
(
    'Yangon West General Hospital', 'ရန်ကုန်အနောက်ပိုင်းဆေးရုံကြီး', '01222860', 
    'Lower Kyimyindaing Road, Ahlone Township', 'အောက်ကြည့်မြင်တိုင်လမ်း, အလုံ မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.125742 16.795935)')
),
(
    'Insein General Hospital', 'အင်းစိန်ပြည်သူ့ဆေးရုံကြီး', '01640132', 
    'Min Gyi St, Yangon ', 'မင်းကြီးလမ်း, ရန်ကုန် ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.105268 16.892209)')
),
(
    'Yangon Children''s Hospital', 'ရန်ကုန်ကလေးဆေးရုံကြီး', '01222807', 
    '2 Pyidaungzu Yeiktha Road', 'ပြည်ထောင်စုရိပ်သာလမ်း၊ အမှတ် ၂', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.136417 16.788333)')
),
(
    'Central Women''s Hospital', 'ဗဟိုအမျိုးသမီးဆေးရုံကြီး (မီးဖွားဆောင်)', '01222811', 
    '59 Min Ye Kyaw Zwa Road, Lanmadaw , Yangon', '၅၉ မင်းရဲကျော်ဇောလမ်း, လမ်းမတော် , ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.141786 16.781522)')
),
(
    'Eye, Ear, Nose and Throat (EENT) Hospital', 'နား၊ နှာခေါင်း၊ လည်ပင်း အထူးကုဆေးရုံကြီး', '01544000', 
    'No. 355, Banyar Dala Road, Tamwe Gyi (Ka/Kha-Nge) Ward, Tamwe Township', 'အမှတ် ၃၅၅၊ ဗညားဒလလမ်း၊ တာမွေကြီး (က/ခ-ငယ်) ရပ်ကွက်၊ တာမွေမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.172694 16.808127)')
),
(
    'Yangon Orthopaedic Hospital', 'ရန်ကုန်အရိုးရောဂါကုဆေးရုံကြီး', '01527086', 
    'No. 132, Hanthawaddy Road, Thayet Taw (North) Ward, Kyimyindaing Township', 'အမှတ်(၁၃၂)၊ဟံသာ၀တီလမ်း၊သရက်တော(မြောက်)ရပ်ကွက်၊ ကြည့်မြင်တိုင်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.122865 16.819072)')
),
(
    'Mingaladon General Hospital', 'မင်္ဂလာဒုံ အထွေထွေရောဂါကုဆေးရုံကြီး', '01635299', 
    'Pyay Road, near Kyaik Kalot Pagoda, Pyidawtha Ward, Mingaladon Township', 'ပြည်လမ်း၊ ကျိုက်ကလော့ဘုရားအနီး၊ ပြည်တော်သာရပ်ကွက်၊ မင်္ဂလာဒုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.129945 16.952406)')
),
(
    'Yway Tha Gyi Mental Health Hospital', 'စိတ်ကျန်းမာရေးဆေးရုံကြီး (ရွာသာကြီး)', '09967778817', 
    '164, No (7) Main Road, Ywar Thar Gyi Ward, East Dagon Township, Yangon', '၁၆၄၊ အမှတ် (၇) လမ်းမကြီး, ရွာသာကြီးရပ်ကွက်, အရှေ့ဒဂုံ မြို့နယ်, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.261833 16.962639)')
),
(
    'South Dagon Public Hospital', 'တောင်ဒဂုံ ပြည်သူ့ဆေးရုံကြီး', '01590074', 
    'Pale Yadanar Road, Ward No. 26, South Dagon Township', 'ပုလဲရတနာလမ်း၊ အမှတ် (၂၆) ရပ်ကွက်၊ ဒဂုံမြို့သစ်(တောင်ပိုင်း)မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.220597 16.851405)')
),
(
    'Hlaingthaya Public Hospital', 'လှိုင်သာယာ ပြည်သူ့ဆေးရုံကြီး', '01640814', 
    'Corner of Hlaing River Road & Kyan Sit Thar St, Hlaingtharyar Township', 'Corner of လှိုင် River လမ်း & Kyan Sit Thar လမ်း, လှိုင်tharyar မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.06472 16.875286)')
),
(
    'Bedded 100 Tharkayta Hospital', 'အထူးကုဆေးရုံ သာကေတ', '01450791', 
    'Shukhinthar Rd, Yangon', 'ရှုခင်းသာလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.217528 16.805681)')
),
(
    'Yankin Children''s Hospital', 'ရန်ကင်းကလေးဆေးရုံကြီး', '018550684', 
    'Thitsar Road, Yankin Township, Yangon', 'သစ္စာလမ်း၊ ရန်ကင်းမြို့နယ်, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.160258 16.83524)')
),
(
    'North Dagon Public Hospital', 'ပြည်သူ့ဆေးရုံ (ဒဂုံမြို့သစ်မြောက်ပိုင်း)', '01584071', 
    'Near the 7/8 Street intersection, Yarzaa Dirit Road, Thingangyun Township.', '၇/၈ လမ်းဆုံအနီး၊, ရာဇာဓိရစ်လမ်း သင်္ဃန်းကျွန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.199005 16.891669)')
),
(
    'East Dagon Public Hospital', 'ဒဂုံမြို့သစ်အရှေ့ပိုင်း ပြည်သူ့ဆေးရုံကြီး', '01585195', 
    'Yarzadirit Road၊ No. (122) Ward, Dagon Myothit (Eastern) Township', 'ရာဇာဓိရစ်လမ်း၊ အမှတ် (၁၂၂) ရပ်ကွက်၊ ဒဂုံမြို့သစ်(အရှေ့ပိုင်း)မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.236756 16.919474)')
),
(
    'ZeeKwek Eyewear & Eye Hospital South Okkalapa Branch', 'ဇီးကွက် မျက်မှန်နှင့် မျက်စိဆေးရုံ (တောင်ဥက္ကလာပခွဲ)', '09887633336', 
    'No. 806 Than Thu Mar Rd, Yangon', ' အမှတ် ၈၀၆၊ သံသုမာလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.193702 16.849193)')
),
(
    'Wai Bar Gi Specialty Hospital Infectious Diseases', 'ဝေဘာဂီ အထူးကုဆေးရုံ ကူးစက်', '01690118', 
    'May Darwi Road, Corner of Dhama Thukha Street, Wai Bar Gi Ward (8), North Okkalapa', 'မေဒါဝီလမ်း၊ ဓမ္မသုခလမ်းထောင့် ဝေဘာဂီရပ်ကွက် (၈)၊ မြောက်ဥက္ကလာပ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.156618 16.920606)')
),
(
    'Ma Har Myaing Hospital', 'မဟာမြိုင်ဆေးရုံ', '01537918', 
    'No.308 Pyay Rd, စမ်းချောင်းမြို့နယ်', 'အမှတ် ၃၀၈၊ ပြည်လမ်း, စမ်းချောင်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.136446 16.808184)')
),
(
    'Bahan Township Public Health Department', 'ဗဟန်းမြို့နယ် ပြည်သူ့ကျန်းမာရေးဦးစီးဌာန', '01554081', 
    '32 Bogyoke Museum St, Bo Cho Ward (2), Bahan Township', '၃၂ ဗိုလ်ချုပ်ပြတိုက်လမ်း၊ဗိုလ်ချိုရပ်ကွက်(၂)၊ဗဟန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.164169 16.805946)')
),
(
    'Yangon Traditional Medicine Hospital', 'တိုင်းရင်းဆေးရုံကြီး ရန်ကုန်', '01544168', 
    '182, Thazin St, Ngar Htat Gyi Pagoda St,Bahan, Yangon', '182, သဇင်လမ်း၊ ငါးထပ်ကြီးဘုရားလမ်း,ဗဟန်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.164005 16.806784)')
),
(
    'Victoria Hospital', 'ဝိတိုရိယဆေးရုံ', '019666141', 
    'No.68, Taw Win Road, Mayangone Township', 'အမှတ် ၆၈၊ တော်ဝင်လမ်း၊ မရမ်းကုန်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.130168 16.877547)')
),
(
    'Asia Royal Hospital', 'အာရှတော်ဝင်ဆေးရုံ', '012304999', 
    'No.14, Baho Road, Sanchaung Township', 'No.14, ဗဟိုလမ်း, စမ်းချောင်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.131461 16.798075)')
),
(
    'Pun Hlaing Hospital', 'ပန်းလှိုင်ဆေးရုံ', '09772889922', 
    'Pun Hlaing Estate Avenue, Hlaing TharYar Township, Yangon', 'ပန်းလှိုင်အိမ်ယာ၊ လှိုင်သာယာမြို့နယ်၊ ရန်ကုန်မြို့', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.088866 16.840898)')
),
(
    'Parami Hospital', 'ပါရမီအထွေထွေရောဂါကုဆေးရုံ', '01657232', 
    'No-60, G-1,  Parami Road, Mayangone', 'အမှတ်-၆၀၊ G-1၊ ပါရမီလမ်း၊ မရမ်းကုန်းမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.155802 16.849928)')
),
(
    'Pinlon Hospital', 'ပင်လုံဆေးရုံ', '013581329', 
    'No.9, Saya San Road', ', အမှတ် ၉၊ ဆရာစံလမ်း', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.208745 16.860846)')
),
(
    'Grand Hantha Hospital', 'ဂရန်းဟံသာဆေးရုံ', '012317600', 
    'No (3), Corner of Nar Nat Taw Street and Kyee Myin Daing, Kan Nar Road, Yangon', 'အမှတ် (၃), နာနတ်တောလမ်းနှင့်ကြည့်မြင်တိုင်လမ်းထောင့်, ကမ်းနားလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.123294 16.821373)')
),
(
    'Kan Thar Yar Hospital', 'ကံသာယာဆေးရုံ', '01505284', 
    '87 Pyay Rd, Yangon', '၈၇ ပြည်လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.137153 16.842162)')
),
(
    'Sakura Hospital', 'ဆာကူရာဆေးရုံ', '017512668', 
    'No.23, Shin Saw Pu Road, Sanchaung Township', 'အမှတ် ၂၃၊ ရှင်စောပုလမ်း, စမ်းချောင်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.130535 16.79631)')
),
(
    'SSC Hospital', 'ရွှေဂုံတိုင်အထူးကုဆေးရုံ', '01541457', 
    'No.7, Shwe Gon Daing St, Bahan Township', 'အမှတ် ၇၊ ရွှေဂုံတိုင်လမ်း, ဗဟန်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.165681 16.8109)')
),
(
    'Jivitadana Sangha Hospital', 'ဇီဝိတဒါန သံဃာ့ဆေးရုံကြီး', '01557733', 
    'Kaba Aye Pagoda Road, Bahan Township', 'ကမ္ဘာအေးဘုရားလမ်း, ဗဟန်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.156345 16.803049)')
),
(
    'Okkala Hospital', 'ဥက္ကလာဆေးရုံ', '014706622', 
    'No.137/D, Thudhamma Road, South Okkalapa', 'အမှတ် ၁၃၇/D၊ သုဓမ္မလမ်း, တောင်ဥက္ကလာပ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.155001 16.884979)')
),
(
    'Ar Yu Hospital', 'အာယုအင်တာနေရှင်နယ်ဆေးရုံ', '019376200', 
    'R57G+59R, 400 Kyaik Ka San Rd, Yangon', 'R57G+59R, ၄၀၀ ကျိုက်ကစံလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.175777 16.813033)')
),
(
    'Sabal Specialist Clinic', 'စံပယ်အထူးကုဆေးခန်း', '09677756737', 
    '90 Hledan Street, Yangon', '၉၀ လှည်းတန်း လမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.143683 16.776809)')
),
(
    'Marlar Myaing Specialist Clinic', 'မာလာမြိုင် အထူးကုဆေးခန်း', '09765111729', 
    'No.6, Marlar Myaing 4th St,16th Ward,Hlaing Township, Yangon', 'အမှတ် ၆၊ မာလာမြိုင် ၄ လမ်း,၁၆ ရပ်ကွက်,လှိုင် မြို့နယ်, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.120922 16.856918)')
),
(
    'Shwe Taw Win Hospital', 'ရွှေတော်ဝင်ဆေးရုံ', '09799992342', 
    '10/B U Wisara Road, Yangon', '၁၀/ဘီ၊ ဦးဝိစာရလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.172762 16.878087)')
),
(
    'No. (2) Military Hospital (500 Bedded)', 'အမှတ်(၂) တပ်မ​တော်ဆေးရုံ (ကုတင်၅၀၀)', '', 
    'Zay Street, Yangon Dagon Township', 'ဇေ လမ်း, ရန်ကုန် ဒဂုံ မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.152483 16.78954)')
),
(
    'Shin Par Gu Hospital', 'သျှင်ပါကူဆေးရုံ', '01548779', 
    '71, 73 Banyar Dala Rd, Yangon', '၇၁၊ ၇၃ ဗညားဒလ လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.171726 16.806627)')
),
(
    'Aung Yadana Hospital', 'အောင်ရတနာဆေးရုံ', '09880443355', 
    'No. 5/24, Thirigon Estate, Waizayantar Road, 16 2 Block, Yangon', 'အမှတ် ၅/၂၄, သီရိဂုဏ်အိမ်ရာ , ဝေဇယန္တာလမ်း, ၁၆-၂ ဘလောက်, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.179402 16.832502)')
),
(
    'THUKHAGABAR HOSPITAL', 'သုခကမ္ဘာ ဆေးရုံ', '01500100', 
    ' San Yeik Nyein, 6th Street, Yangon', ' စံရိပ်ငြိမ်း၊ ၆ လမ်း လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.130616 16.833271)')
),
(
    'National Rehabilitation Hospital', 'အမျိုးသားပြန်လည်သန်စွမ်းရေးဆေးရုံ', '01660898', 
    'Min Dhama Road , Kyaik Waing Pagoda Road ထောင့်Ward (3), Mayangone Township', 'မင်းဓမ္မ လမ်း , ကျိုက်ဝိုင်းဘုရား လမ်း ထောင့်ရပ်ကွက် (၃), မရမ်းကုန်း မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.131649 16.865726)')
),
(
    'KWEKABAW Hospital', 'ကွယ်ကဘောဆေးရုံ', '09253132574', 
    'အမှတ် 144၊ မင်းကြီးလမ်း၊ ရွာမ (အရှေ့) ရပ်ကွက်၊ အင်းစိန်မြို့နယ်', 'အမှတ် ၁၄၄၊ မင်းကြီးလမ်း၊ ရွာမ (အရှေ့) ရပ်ကွက်၊ အင်းစိန်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.105007 16.89466)')
),
(
    'Bahosi Hospital', 'ဗဟိုစည်ဆေးရုံ', '012300631', 
    'B 1/6-31/36-37/38, Bahosi Housing Complex, Wardan Street, Yangon', 'B ၁/၆-၃၁/၃၆-၃၇/၃၈, ဗဟိုစည်အိမ်ရာအစုအဝေး, ဝါးတန်းလမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.14089 16.779212)')
),
(
    'Aung Chan Tha Specialist Clinic', 'အောင်ချမ်းသာအထူးကုဆေးခန်း', '09753113161', 
    'Aung Chan Thar, Yangon ', 'အောင်ချမ်းသာ, ရန်ကုန် ', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.120257 16.977764)')
),
(
    'Taw Win 24Hr Clinic', 'တော်ဝင် ၂၄နာရီ ဆေးခန်း', '09774411358', 
    'No.111 Ground floor, Baho Rd, Yangon ', 'အမှတ် ၁၁၁၊ မြေညီထပ်, ဗဟို လမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.125334 16.825712)')
),
(
    'Thukha Specialist Clinic', 'သုခအထူးကုဆေးခန်း', '0973017408', 
    'No. 83, 84 Insein Rd, Yangon', 'အမှတ် ၈၃၊၈၄ အင်းစိန် လမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.126452 16.840414)')
),
(
    'KBC Hospital', 'ကေဘီစီ ဆေးရုံ', '01644943', 
    'Seminary Hill, Insein Rd, Yangon', 'Seminary Hill, အင်းစိန် လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.114277 16.881959)')
),
(
    'Kandawlay Clinic', 'ကန်တော်လေးဆေးခန်း', '01246531', 
    'Yangon', 'ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.163074 16.790248)')
),
(
    'Yuzana Clinic', 'ယုဇနဆေးခန်း', '01526074', 
    'No 45, Hlaing Bu Tar Yon St, Yangon', 'အမှတ် ၄၅၊ လှိုင်ဘူတာရုံလမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.121843 16.836922)')
),
(
    'Shwe Baho Hospital', 'ရွှေဗဟိုဆေးရုံကြီး', '09263683904', 
    '26 Tha Mein Ba Yan Rd, Yangon', '၂၆ သမိန်ဗရမ်း လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.177181 16.809975)')
),
(
    'Myittar Hospital', 'မေတ္တာဆေးရုံ', '09262840600', 
    'Myittar Rd, Yangon', 'မေတ္တာ လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.186613 16.845674)')
),
(
    'Aye Meitta Clinic', 'အေးမေတ္တာဆေးခန်း', '09450289543', 
    'Dhama Yarzar St, Yangon', 'ဓမ္မရာဇာ လမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.18345 16.846074)')
),
(
    'Shwe Pyi Thar Specialist Clinic', 'ရွှေပြည်သာအထူးကုဆေးခန်း', '0973033027', 
    'No. 732 4th St, Yangon', 'အမှတ် ၇၃၂ ၄လမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.11291 16.861818)')
),
(
    'Sanpya Specialist Clinic', 'စံပြအထူးကုဆေးခန်း', '09780981106', 
    'Tha Mein Ba Yan, Yangon', 'သမိန်ဗရမ်း, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.174445 16.812384)')
),
(
    'Moe Myittar Hospital', 'မိုးမေတ္တာ ဆေးရုံ', '01523564', 
    'No.30 Aung Myay Thar Si 1 lane 1 Ward Kamayut Township, Yangon', 'အမှတ် ၃၀၊ အောင်မြေသာစည်လမ်းသွယ် ၁ ရပ်ကွက် ကမာရွတ် မြို့နယ်, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.127909 16.833999)')
),
(
    'Academy Hospital', 'အကယ်ဒမီ ဆေးရုံ', '01212890', 
    'No. 335 Lower Kyeemyindaing Rd, Yangon', 'အမှတ် ၃၃၅ အောက်ကြည့်မြင်တိုင်လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.127952 16.790417)')
),
(
    'Moe Thee Hospital', 'မိုးသီး ဆေးရုံ', '095000948', 
    '238/239 Yamonnar Rd, Yangon ', '၂၃၈/၂၃၉ ယမုံနာ လမ်း, ရန်ကုန် ', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.191577 16.779589)')
),
(
    'Samitivej International Clinic', 'ဆစ်မီတဝေ့ အင်တာနေရှင်နယ် ဆေးခန်း', '09424274301', 
    '9E/2 Kabaraye Pagoda Road, Mayangone Township, Yangon', '9E/2 ကမ္ဘာအေးဘုရားလမ်း, မရမ်းကုန်း မြို့နယ်, ရန်ကုန်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.14497412876264 16.867563002675407)')
),
(
    'Moe Kaung Treasure Maternal and Child Hospital', 'မိုးကောင်းရတနာ မိခင်နှင့်ကလေးဆေးရုံ', '09696908881', 
    'No.15, Street Moe Kaung Rd', 'အမှတ် 15, မိုးကောင်း လမ်း', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.16885039712693 16.830697989164584)')
),
(
    'Rose Hill Hospital', 'နှင်းဆီကုန်းဆေးရုံ', '01558401', 
    '20/A Kabar Aye Pagoda Rd, Yangon', '20/A ကမ္ဘာအေးဘုရား လမ်း, ရန်ကုန်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.15605561349271 16.809619847548785)')
);