-- ======================================================
-- 1. INITIAL ADMIN ACCOUNT SEED
-- ======================================================
-- Placeholder bcrypt hash for: 'AdminPassword123' (Replace during real auth implementation)
INSERT INTO users (full_name, phone, email, password_hash, role)
VALUES (
    'System Administrator', 
    '09987654321', 
    'admin@ema.local', 
    '$2b$12$YB5T/hBhDDHcsKPJhowyD.bcBhFuk7ThnNC0lVKPZl2EhkAqRwy/u', 
    'ADMIN'
);

-- ======================================================
-- 2. EMERGENCY CATEGORIES SEED
-- ======================================================
-- IDs will be generated sequentially (1 to 10) due to IDENTITY column
INSERT INTO emergency_categories (name_en, name_mm, priority) VALUES
('Stroke', 'လေဖြတ်ခြင်း', 1),
('Heart Attack', 'နှလုံးဖောက်ခြင်း', 1),
('Seizure', 'တက်ခြင်း', 2),
('Fainting', 'မေ့လဲခြင်း', 3),
('Severe Bleeding', 'သွေးထွက်လွန်ခြင်း', 1),
('Severe Allergy', 'ပြင်းထန်သော ဓာတ်မတည့်မှု', 1),
('Snake Bite', 'မြွေကိုက်ခြင်း', 2),
('Burn', 'မီးလောင်ဒဏ်ရာ', 2),
('Choking', 'အသက်ရှူလမ်းကြောင်းပိတ်ခြင်း', 1),
('Fracture', 'အရိုးကျိုးခြင်း', 2);

-- ======================================================
-- 3. FIRST AID STEPS SEED
-- ======================================================

-- ======================================================
-- CATEGORY 1: STROKE (လေဖြတ်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(1, 1, 'Check the Face. Ask the person to smile. Check if one side of the face droops.', 
       'မျက်နှာကို စစ်ဆေးပါ။ လူနာကို ပြုံးခိုင်းကြည့်ပါ။ မျက်နှာတစ်ခြမ်း တွဲကျနေခြင်း ရှိ၊ မရှိ ကြည့်ပါ။'),
(1, 2, 'Check the Arms. Ask the person to raise both arms. Check if one arm drifts downward or feels weak.', 
       'လက်မောင်းကို စစ်ဆေးပါ။ လူနာကို လက်နှစ်ဖက်လုံး မြှောက်ခိုင်းကြည့်ပါ။ လက်တစ်ဖက်က အောက်သို့ ပြန်ကျသွားခြင်း သို့မဟုတ် အားမရှိဘဲ ဖြစ်နေခြင်း ရှိ၊ မရှိ စစ်ဆေးပါ။'),
(1, 3, 'Check the Speech. Ask the person to repeat a simple sentence. Check if their speech is slurred, strange, or hard to understand.', 
       'စကားပြောခြင်းကို စစ်ဆေးပါ။ လူနာကို ရိုးရှင်းသော စကားစုတစ်ခု ထပ်ခါတလဲလဲ ပြောခိုင်းကြည့်ပါ။ စကားသံ ဗလုံးဗထွေးဖြစ်နေခြင်း သို့မဟုတ် ပြောရခက်ခဲနေခြင်း ရှိ၊ မရှိ စစ်ဆေးပါ။'),
(1, 4, 'Call emergency services immediately. If the person shows any of these signs, call for help right away, even if the symptoms go away.', 
       'အရေးပေါ်အဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။ အထက်ပါ လက္ခဏာတစ်ခုခု ပြလာပါက (လက္ခဏာများ ပြန်ကောင်းသွားလျှင်ပင်) ကယ်ဆယ်ရေးအဖွဲ့ထံ ချက်ချင်း အကူအညီတောင်းပါ။'),
(1, 5, 'Note the time. Keep track of exactly when the first symptoms started. This is critical info for the hospital staff.', 
       'အချိန်ကို မှတ်သားထားပါ။ လက္ခဏာများ စတင်ပြသခဲ့သည့် အချိန်ကို အတိအကျ မှတ်ထားပါ။ ၎င်းသည် ဆေးရုံရောက်လျှင် အလွန်အရေးကြီးသော အချက်အလက် ဖြစ်သည်။'),
(1, 6, 'Stay with the person. Keep them calm, comfortable, and resting safely. Do not give them any food, drink, or aspirin.', 
       'လူနာနှင့်အတူ ရှိနေပေးပါ။ လူနာကို စိတ်ငြိမ်ငြိမ်ထားရန်၊ သက်သောင့်သက်သာ နားနားနေနေ နေရန် ကူညီပေးပါ။ အစားအစာ၊ ရေ သို့မဟုတ် အက်စပရင် (Aspirin) ဆေးပြားများ လုံးဝမတိုက်ပါနှင့်။');

-- ======================================================
-- CATEGORY 2: HEART ATTACK (နှလုံးဖောက်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(2, 1, 'Recognize the signs. Look for chest pain, pressure, squeezing, or discomfort. Pain may spread to the jaw, neck, back, or arms. Watch for shortness of breath, sweating, or dizziness.', 
       'ရောဂါလက္ခဏာများကို ခွဲခြားပါ။ ရင်ဘတ်အောင့်ခြင်း၊ အောင့်သကဲ့သို့ ဖိညှစ်ထားသလို ခံစားရခြင်းကို သတိပြုပါ။ ထိုနာကျင်မှုသည် မေးရိုး၊ လည်ပင်း၊ ကျောပြင် သို့မဟုတ် လက်မောင်းများဆီသို့ ပျံ့နှံ့သွားနိုင်သည်။ အသက်ရှူမဝခြင်း၊ ချွေးစေးများထွက်ခြင်း သို့မဟုတ် မူးဝေခြင်းများကို စောင့်ကြည့်ပါ။'),
(2, 2, 'Call emergency services immediately. Do not wait to see if the symptoms pass. Act right away.', 
       'အရေးပေါ်အဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။ ရောဂါလက္ခဏာများ သက်သာသွားမလားဟု စောင့်မနေပါနှင့်။ ချက်ချင်း အရေးယူ ဆောင်ရွက်ပါ။'),
(2, 3, 'Rest and calm the person. Have the person sit down in a comfortable position (a semi-sitting position with knees bent is usually best). Loosen tight clothing around their neck.', 
       'လူနာကို အနားယူစေပြီး စိတ်ငြိမ်အောင် ထားပါ။ လူနာကို သက်သောင့်သက်သာဖြစ်မည့် အနေအထား (ဒူးကွေးပြီး တစ်ဝက်ထိုင် အနေအထားက အကောင်းဆုံးဖြစ်သည်) ဖြင့် ထိုင်ခိုင်းပါ။ လည်ပင်းတစ်ဝိုက်ရှိ ကျပ်နေသောအဝတ်အစားများကို လျှော့ပေးပါ။'),
(2, 4, 'Offer Aspirin if appropriate. If the person is conscious, not allergic to aspirin, and has no history of severe bleeding, give them one adult aspirin (325 mg) or 2 to 4 low-dose aspirins (81 mg each). Tell them to chew it, not swallow it whole.', 
       'အခြေအနေအလိုက် အက်စပရင် (Aspirin) ဆေးပြား တိုက်ကျွေးပါ။ လူနာသည် သတိရနေပြီး၊ ဆေးနှင့် ဓာတ်မတည့်ခြင်းမရှိ၊ သွေးထွက်လွန်ဖူးသည့် ရာဇဝင်မရှိပါက လူကြီးသောက် အက်စပရင် ၁ ပြား (325 mg) သို့မဟုတ် အနိမ့်စား (81 mg) ကို ၃ ပြားမှ ၄ ပြားအထိ တိုက်နိုင်ပါသည်။ မျိုမချခိုင်းဘဲ ဝါးစားခိုင်းပါ။'),
(2, 5, 'Monitor closely. Be ready to perform CPR immediately if the person becomes unconscious and stops breathing normally.', 
       'အနီးကပ် စောင့်ကြည့်ပါ။ လူနာသည် သတိလစ်သွားပြီး ပုံမှန်အတိုင်း အသက်မရှူတော့ပါက ချက်ချင်း နှလုံးနှိုးစက် သို့မဟုတ် CPR ပြုလုပ်ရန် အသင့်ပြင်ထားပါ။');

-- ======================================================
-- CATEGORY 3: SEIZURE (တက်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(3, 1, 'Protect from injury. Move nearby sharp or hard objects out of the way. Place something soft (like a folded jacket) under their head.', 
       'ဒဏ်ရာမရအောင် ကာကွယ်ပါ။ လူနာအနီးနားရှိ ထက်မြက်သော သို့မဟုတ် မာကျောသောပစ္စည်းများကို ဖယ်ရှားပါ။ လူနာ၏ခေါင်းအောက်တွင် ခေါက်ထားသောအင်္ကျီကဲ့သို့ ပျော့ပျောင်းသောအရာတစ်ခုခု ခုပေးပါ။'),
(3, 2, 'Do not restrain. Never try to hold the person down or stop their movements. Let the seizure run its course.', 
       'လူနာကို အတင်းချုပ်မထားပါနှင့်။ လူနာကို အောက်သို့ဖိချုပ်ထားခြင်း သို့မဟုတ် ၎င်း၏လှုပ်ရှားမှုများကို အတင်းအဓမ္မရပ်တန့်စေရန် လုံးဝမပြုလုပ်ပါနှင့်။ တက်ခြင်းဝေဒနာ သဘာဝအတိုင်း ပြီးဆုံးသည်အထိ လွှတ်ထားပေးပါ။'),
(3, 3, 'Do not put anything in their mouth. Contrary to popular myths, a person cannot swallow their tongue. Forcing an object between their teeth can cause severe dental or airway injury.', 
       'ပါးစပ်ထဲသို့ မည်သည့်အရာမှ မထည့်ပါနှင့်။ လူနာ၏သွားများကြားထဲသို့ ပစ္စည်းများအတင်းထိုးထည့်ခြင်းမျိုး လုံးဝမပြုလုပ်ပါနှင့်။ သွားနှင့် အသက်ရှူလမ်းကြောင်းကို ပြင်းထန်စွာ ထိခိုက်ဒဏ်ရာရစေနိုင်ပါသည်။'),
(3, 4, 'Time the seizure. Note the exact time the seizure started and how long it lasts.', 
       'တက်သည့်အချိန်ကို မှတ်သားပါ။ တက်ခြင်းစတင်သည့် အချိန်နှင့် မည်မျှကြာအောင် တက်နေသည်ကို သေချာမှတ်သားထားပါ။'),
(3, 5, 'Roll them onto their side. As soon as the jerking movements stop and it is safe to do so, gently turn the person into the recovery position (on their side) to keep their airway clear of saliva or vomit.', 
       'လူနာကို ဘေးစောင်းအနေအထား ပြောင်းပေးပါ။ လူနာတုန်ခါလှုပ်ရှားမှုများ ရပ်တန့်သွားပြီး ဘေးကင်းပြီဆိုသည်နှင့် တံတွေး သို့မဟုတ် အန်ဖတ်များကြောင့် အသက်ရှူလမ်းကြောင်း မပိတ်စေရန် လူနာကို ဘေးစောင်းအနေအထား (Recovery Position) သို့ ညင်သာစွာ ပြောင်းပေးပါ။'),
(3, 6, 'Call emergency services if required. Call for help immediately if the seizure lasts longer than 5 minutes, if they are injured, if they have back-to-back seizures, or if it is their first known seizure.', 
       'လိုအပ်ပါက အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပါ။ တက်သည့်အချိန် ၅ မိနစ်ထက်ကျော်လွန်ပါက၊ လူနာတွင် ဒဏ်ရာရသွားပါက၊ တစ်ကြိမ်ပြီးတစ်ကြိမ် ဆက်တိုက်တက်နေပါက သို့မဟုတ် ၎င်းသည် လူနာ၏ပထမဆုံးအကြိမ် တက်ဖူးခြင်းဖြစ်ပါက ကယ်ဆယ်ရေးအဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။');

-- ======================================================
-- CATEGORY 4: FAINTING (မေ့လဲခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(4, 1, 'Check responsiveness and breathing. Ensure the person is breathing normally. If they do not wake up quickly or stop breathing, transition immediately to CPR protocol and call emergency services.', 
       'သတိရှိမရှိနှင့် အသက်ရှူခြင်းကို စစ်ဆေးပါ။ လူနာ ပုံမှန်အတိုင်း အသက်ရှူနေခြင်း ရှိ၊ မရှိ သေချာပါစေ။ အကယ်၍ လူနာသည် လျင်မြန်စွာ ပြန်လည်သတိမရလာပါက သို့မဟုတ် အသက်ရှူရပ်သွားပါက ချက်ချင်း အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပြီး CPR နှလုံးနှိုးခြင်းလုပ်ငန်းစဉ်ကို စတင်ပါ။'),
(4, 2, 'Position the person safely. Keep the person lying flat on their back. If possible and there are no signs of injury, elevate their legs about 12 inches to help restore blood flow to the heart and brain.', 
       'လူနာကို ဘေးကင်းသောအနေအထားဖြင့် ထားပါ။ လူနာကို ပက်လက်လှန်အနေအထားဖြင့် ပြားပြားလေး သိပ်ထားပါ။ အကယ်၍ ထိခိုက်ဒဏ်ရာရထားသည့် လက္ခဏာမရှိပါက ခြေထောက်ကို ၁ ပေခန့် (၁၂ လက်မ) မြှင့်ထားပေးပါ။'),
(4, 3, 'Loosen tight clothing. Undo tight collars, ties, belts, or waistbands to ease breathing and circulation.', 
       'ကျပ်နေသောအဝတ်အစားများကို လျှော့ပေးပါ။ အသက်ရှူရလွယ်ကူစေရန်နှင့် သွေးလှည့်ပတ်မှုကောင်းစေရန် ကျပ်နေသော ကော်လာများ၊ ကရဗတ်များ၊ ขါးပတ်များနှင့် ဘောင်းဘီခါးပတ်များကို ဖြေလျှော့ပေးပါ။'),
(4, 4, 'Ensure fresh air. Keep crowds back and open windows if indoors. Do not let them get up too quickly once they regain consciousness.', 
       'လေကောင်းလေသန့်ရရှိပါစေ။ လူနာဘေးတွင် လူစုလူဝေးမဖြစ်အောင် ဖယ်ရှားပေးပါ၊ အခန်းတွင်းဖြစ်ပါက ပြတင်းပေါက်များကို ဖွင့်ပေးပါ။ လူနာ သတိပြန်ရလာပါကလည်း ချက်ချင်း အတင်းထခိုင်းခြင်းမျိုး မပြုလုပ်ပါနှင့်။'),
(4, 5, 'Do not splash water. Never slap the person''s face, splash cold water on them, or give them anything to eat or drink until they are fully awake and alert.', 
       'ရေဖြန်းခြင်း၊ အတင်းလှုပ်နှိုးခြင်း မပြုလုပ်ပါနှင့်။ လူနာ၏မျက်နှာကို ရိုက်ပုတ်ခြင်း၊ ရေအေးဖြင့်ပက်ခြင်း သို့မဟုတ် လူနာလုံးဝသတိပြန်မရမချင်း မည်သည့်အစားအစာနှင့် ရေကိုမျှ တိုက်ကျွေးခြင်းမပြုပါနှင့်။'),
(4, 6, 'Call emergency services if needed. Call for help if the person remains unconscious for more than 1 minute, if they fell and suffered an injury, or if they have a history of heart conditions.', 
       'လိုအပ်ပါက အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပါ။ လူနာသည် ၁ မိနစ်ထက်ကျော်လွန်သည်အထိ သတိမရဘဲဖြစ်နေပါက၊ လဲကျစဉ် ထိခိုက်ဒဏ်ရာရသွားပါက သို့မဟုတ် နှလုံးရောဂါအခံရှိသည့် ရာဇဝင်ရှိပါက ချက်ချင်း အကူအညီတောင်းပါ။');

-- ======================================================
-- CATEGORY 5: SEVERE BLEEDING (သွေးထွက်လွန်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(5, 1, 'Apply direct pressure. Place a clean dressing directly over the wound and press firmly with both hands.', 
       'ဒဏ်ရာကို တိုက်ရိုက် ဖိထားပါ။ သန့်ရှင်းသော ပတ်တီး (သို့မဟုတ် သန့်ရှင်းသောအဝတ်၊ လက်အိတ်စွပ်ထားသောလက်) ကို ဒဏ်ရာပေါ် တိုက်ရိုက်တင်ပြီး လက်နှစ်ဖက်လုံးဖြင့် ခပ်ပြင်းပြင်း ဖိထားပေးပါ။'),
(5, 2, 'Maintain constant pressure. Do not lift the dressing to check if bleeding has stopped. If blood seeps through, place another cloth right on top and keep pressing.', 
       'မလွှတ်တမ်း ဆက်တိုက် ဖိထားပါ။ သွေးတိတ်၊ မတိတ် စစ်ဆေးရန် ပတ်တီးကို မကြွပါနှင့်။ ကြွလိုက်ပါက သွေးခဲများကို ပျက်စီးစေပြီး သွေးပြန်ထွက်လာစေနိုင်သည်။ သွေးစိုရွှဲထွက်လာပါက ပထမအဝတ်ပေါ်ကနေ နောက်ထပ်အဝတ်တစ်ထပ် ထပ်ဆင့်ပြီး ဆက်ဖိထားပါ။'),
(5, 3, 'Secure with a bandage. Once bleeding is under control, wrap a bandage firmly over the dressing to hold it in place. Do not wrap too tightly to cut off circulation completely.', 
       'ပတ်တီးဖြင့် စည်းပါ။ သွေးထွက်ခြင်း ထိန်းချုပ်နိုင်ပြီဆိုပါက ဒဏ်ရာပေါ်ကအဝတ် မြဲနေစေရန် ပတ်တီးဖြင့် သေချာပတ်နှောင်ပါ။ သွေးလှည့်ပတ်မှု လုံးဝမပိတ်သွားစေရန် အလွန်အမင်း တင်းကျပ်စွာ စည်းခြင်းမျိုးတော့ မပြုလုပ်ရပါ။'),
(5, 4, 'Call emergency services. Call for help immediately if the bleeding is heavy, pulsing, or does not stop after several minutes of continuous direct pressure.', 
       'အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပါ။ သွေးထွက်လွန်နေပါက၊ သွေးက ပန်းထွက်နေပါက သို့မဟုတ် မိနစ်အနည်းငယ်ကြာ ဆက်တိုက်ဖိထားသော်လည်း သွေးမတိတ်ပါက ကယ်ဆယ်ရေးအဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။'),
(5, 5, 'Minimize shock. Help the person lie down flat. Keep them warm with a blanket and reassure them to keep their heart rate down.', 
       'ရှော့ခ် (Shock) မရအောင် ကာကွယ်ပါ။ လူနာကို ပက်လက်ပြားပြား လှဲအိပ်စေပါ။ စောင်ခြုံပေးပြီး ခန္ဓာကိုယ်ကို နွေးထွေးအောင်ထားကာ လူနာစိတ်ငြိမ်စေရန် အားပေးစကားပြောပါ။');

-- ======================================================
-- CATEGORY 6: SEVERE ALLERGY / ANAPHYLAXIS (ပြင်းထန်သော ဓာတ်မတည့်မှု)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(6, 1, 'Recognize anaphylaxis. Look for critical warning signs: trouble breathing or swallowing, swelling of the face/throat, widespread hives, dizziness, or a rapid pulse.', 
       'ပြင်းထန်ဓာတ်မတည့်မှုကို ခွဲခြားပါ။ အန္တရာယ်ရှိသော လက္ခဏာရပ်များကို သတိပြုပါ - အသက်ရှူရခက်ခြင်း သို့မဟုတ် မျိုချရခက်ခြင်း၊ မျက်နှာ/လည်ချောင်း ရောင်ရမ်းလာခြင်း၊ တစ်ကိုယ်လုံး အင်ပြင်များထွက်ခြင်း၊ မူးဝေခြင်း သို့မဟုတ် သွေးခုန်နှုန်း အလွန်မြန်ခြင်း။'),
(6, 2, 'Call emergency services immediately. Anaphylaxis is a life-threatening medical emergency. Do not wait to see if symptoms improve.', 
       'အရေးပေါ်အဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။ ပြင်းထန်စွာ ဓာတ်မတည့်ခြင်းသည် အသက်အန္တရာယ်ရှိသော အရေးပေါ်အခြေအနေဖြစ်သည်။ လက္ခဏာများ သက်သာလာမလားဟု စောင့်မနေပါနှင့်။'),
(6, 3, 'Use an Epinephrine Auto-Injector (EpiPen). If available, press it firmly against the outer thigh (through clothing if necessary) and hold it in place for 3 seconds.', 
       'အပီနက်ဖရင် (Epinephrine) ဆေးထိုးပြွန်ကို သုံးပါ။ လူနာတွင် အရေးပေါ်သုံး ဆေးထိုးပြွန် (EpiPen) အသင့်ပါလာပါက ချက်ချင်းထိုးပေးပါ။ ပေါင်အပြင်ဘက်ကြွက်သားပေါ်သို့ တည့်တည့်ဖိစိုက်ပြီး ၃ စက္ကန့်ခန့် ဖိထားပါ။'),
(6, 4, 'Position for breathing and shock. Have the person sit up if they have trouble breathing. If they feel dizzy or faint, lay them flat on their back and elevate their legs.', 
       'အသက်ရှူရလွယ်ကူမည့် အနေအထား ထားပါ။ လူနာ အသက်ရှူရခက်ခဲနေပါက မတ်မတ်ထိုင်ခိုင်းပါ။ အကယ်၍ လူနာ မူးဝေခြင်း သို့မဟုတ် မေ့လဲချင်သလို ဖြစ်နေပါက ပက်လက်လှန်သိပ်ပြီး ခြေထောက်ကို မြှင့်ထားပေးပါ။'),
(6, 5, 'Prepare a second dose if needed. If emergency services take longer than 5 to 10 minutes to arrive and symptoms worsen, administer a second dose if another auto-injector is available.', 
       'လိုအပ်ပါက ဒုတိယတစ်ကြိမ် ထပ်ထိုးပါ။ အကယ်၍ အရေးပေါ်အဖွဲ့ ရောက်လာရန် ၅ မိနစ်မှ ၁၀ မိနစ်ထက် ပိုကြာနေပြီး၊ လက္ခဏာများ သက်သာမလာဘဲ ပိုဆိုးလာပါက အပိုပါလာသော ဆေးထိုးပြွန်ဖြင့် ဒုတိယတစ်ကြိမ် ထပ်မံထိုးနှံပေးပါ။');

-- ======================================================
-- CATEGORY 7: SNAKE BITE (မြွေကိုက်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(7, 1, 'Keep the person calm and still. Minimizing physical movement slows down the heart rate, directly delaying the spread of venom.', 
       'လူနာကို ငြိမ်ငြိမ်ထားပြီး စိတ်သက်သာရာရစေပါ။ ခန္ဓာကိုယ်လှုပ်ရှားမှုနှင့် ထိတ်လန့်မှုကို လျှော့ချခြင်းက သွေးခုန်နှုန်းကို နှေးစေပြီး မြွေဆိပ်ပျံ့နှံ့မှုကို တိုက်ရိုက်နှောင့်နှေးစေပါသည်။'),
(7, 2, 'Immobilize the bitten limb. Keep the affected arm or leg still and positioned at or slightly below the level of the heart. Use a splint or sling if available.', 
       'ကိုက်ခံရသည့် ခြေလက်ကို လုံးဝမလှုပ်ရှားစေပါနှင့်။ ကိုက်ခံရသော လက် သို့မဟုတ် ခြေထောက်ကို ငြိမ်ငြိမ်ထားပြီး နှလုံးအောက် အနေအထားတွင် ထားပါ။ မလှုပ်ရှားနိုင်စေရန် ကျပ်စည်း သို့မဟုတ် သိုင်းကြိုးတစ်ခုခုသုံး၍ ထိန်းထားပါ။'),
(7, 3, 'Remove tight items. Instantly take off any rings, watches, jewelry, or tight clothing near the bite area, as severe swelling is likely to occur rapidly.', 
       'ကျပ်နေသောအရာများကို ချွတ်ပစ်ပါ။ ဒဏ်ရာပတ်ဝန်းကျင်တွင် အလွန်အမင်း ရောင်ရမ်းလာနိုင်သဖြင့် ကိုက်ခံရသည့်နေရာအနီးရှိ လက်စွပ်၊ နာရီ၊ လက်ကောက် သို့မဟုတ် ကျပ်နေသောအဝတ်အစားများကို ချက်ချင်းချွတ်ပစ်ပါ။'),
(7, 4, 'Clean the wound gently. Wash the bite area gently with clean water and soap if available. Do not flush it aggressively or scrub the skin.', 
       'ဒဏ်ရာကို ညင်သာစွာ ဆေးကြောပါ။ ရေသန့်သန့်နှင့် ဆပ်ပြာရှိပါက ဒဏ်ရာပတ်ဝန်းကျင်ကို ညင်သာစွာ ဆေးကြောပေးပါ။ ဒဏ်ရာကို ပြင်းပြင်းထန်ထန် ပွတ်တိုက်ခြင်းမျိုး လုံးဝမပြုလုပ်ရပါ။'),
(7, 5, 'Apply a clean bandage. Cover the wound with a clean, dry dressing. Do NOT cut the wound, suck the venom, apply ice, or use a tight tourniquet.', 
       'သန့်ရှင်းသောအဝတ်ဖြင့် အုပ်ထားပါ။ ဒဏ်ရာကို ခြောက်သွေ့သန့်ရှင်းသောအဝတ် သို့မဟုတ် ပတ်တီးဖြင့် အုပ်ထားပါ။ မြွေဆိပ်စုပ်ထုတ်ရန် ဒဏ်ရာကို ဓားဖြင့်လှီးခြင်း၊ ပါးစပ်ဖြင့်စုပ်ခြင်း၊ ရေခဲကပ်ခြင်း သို့မဟုတ် ကြိုးဖြင့် တင်းကျပ်စွာ တုပ်နှောင်ခြင်းမျိုး လုံးဝမပြုလုပ်ရပါ။'),
(7, 6, 'Transport immediately. Get the person to the nearest hospital that stocks antivenom. Try to safely note the snake''s appearance or take a photo from a safe distance.', 
       'မြွေဆိပ်ဖြေဆေးရှိသော ဆေးရုံသို့ ချက်ချင်းပို့ဆောင်ပါ။ မြွေဆိပ်ဖြေဆေး (Antivenom) အသင့်ရှိသော အနီးဆုံးဆေးရုံသို့ လူနာကို အမြန်ဆုံး ပို့ဆောင်ပါ။ ဖြစ်နိုင်ပါက မြွေ၏ပုံသဏ္ဍာန်ကို ဘေးကင်းရာမှ မှတ်သားခြင်း သို့မဟုတ် ဓာတ်ပုံရိုက်ယူထားပါ။');

-- ======================================================
-- CATEGORY 8: BURN (မီးလောင်ဒဏ်ရာ)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(8, 1, 'Stop the burning process. Move the person away from the heat source. Smother flames with a blanket or water.', 
       'မီးလောင်မှုကို ချက်ချင်းရပ်တန့်ပါ။ လူနာကို အပူရှိန်ရှိရာနေရာမှ အမြန်ဆုံး ဖယ်ရှားပါ။ မီးတောက်များကို စောင်ဖြင့်အုပ်၍ဖြစ်စေ၊ ရေဖြင့်ဖြစ်စေ ငြှိမ်းသတ်ပါ။'),
(8, 2, 'Cool the burn immediately. Run cool or lukewarm clean water over the burn for at least 10 to 20 minutes. Do NOT use ice or ice-cold water.', 
       'ဒဏ်ရာကို ချက်ချင်း အအေးခံပါ။ မီးလောင်ထားသောနေရာကို အနည်းဆုံး ၁၀ မိနစ်မှ မိနစ် ၂၀ ခန့် ရေအေးအေး (သို့မဟုတ်) ရေသာမန် စီးဆင်းနေသောရေအောက်တွင် ထားပေးပါ။ ရေခဲ (သို့မဟုတ်) ရေခဲရေ လုံးဝမသုံးရပါ။'),
(8, 3, 'Remove constricting items. Gently slide off rings, bracelets, or tight clothing before swelling starts. Do not peel away clothing stuck directly to the burn.', 
       'ကျပ်နေသောအရာများကို ညင်သာစွာချွတ်ပါ။ ဒဏ်ရာနေရာ မရောင်ရမ်းလာမီ လက်စွပ်၊ လက်ကောက် သို့မဟုတ် ကျပ်နေသောအဝတ်အစားများကို ညင်သာစွာ ချွတ်ပါ။ အရေပြားတွင် အရည်ပျော်ပြီး ကပ်နေသောအဝတ်အစားများကို အတင်းခွာမပစ်ပါနှင့်။'),
(8, 4, 'Protect blisters and cover loosely. Never pop or puncture any blisters. Apply a clean, sterile, non-stick dressing or loose plastic wrap over the cooled burn. Do NOT apply toothpaste or butter.', 
       'အရည်ကြည်ဖုများကို မဖောက်ပါနှင့် ပတ်တီးကို ခပ်ပွပွ စည်းပေးပါ။ အရည်ကြည်ဖုများကို လုံးဝဖောက်ခြင်းမပြုရပါ။ အအေးခံပြီးပါက သန့်ရှင်းသော ပတ်တီး (သို့မဟုတ်) ပလတ်စတစ်စသန့်သန့်ဖြင့် ဒဏ်ရာပေါ်တွင် ခပ်ပွပွ အုပ်ပေးပါ။ သွားတိုက်ဆေး၊ ထောပတ်၊ ဆီ စသည်တို့ လုံးဝမသုတ်ရပါ။'),
(8, 5, 'Seek medical care for severe burns. Call emergency services if the burn covers a large area, involves the face, hands, feet, or if the skin looks charred, white, or leathery.', 
       'ပြင်းထန်ပါက ဆေးကုသမှု ချက်ချင်းခံယူပါ။ မီးလောင်ဒဏ်ရာ အတိုင်းအတာကြီးမားပါက၊ မျက်နှာ၊ လက်၊ ခြေတို့တွင် လောင်ကျွမ်းပါက သို့မဟုတ် အရေပြားမှာ မည်းတူးသွားခြင်း၊ ဖြူဖျော့ပြီး ကြမ်းတမ်းသွားခြင်းဖြစ်ပါက အရေးပေါ်အဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။');

-- ======================================================
-- CATEGORY 9: CHOKING (အသက်ရှူလမ်းကြောင်းပိတ်ခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(9, 1, 'Verify if the person is choking. Ask "Are you choking?" Look for the universal sign of choking (hands clutched to the throat), inability to speak, cough, or breathe.', 
       'အသက်ရှူလမ်းကြောင်း ပိတ်မပိတ် စိစစ်ပါ။ "သီးနေတာလား" ဟု မေးမြန်းပါ။ လည်ပင်းကို လက်နှစ်ဖက်ဖြင့် ဆုပ်ကိုင်ထားခြင်း၊ စကားမပြောနိုင်ခြင်း၊ ချောင်းမဆိုးနိုင်ခြင်း သို့မဟုတ် အသက်မရှူနိုင်ခြင်း စသည့် လက္ခဏာများကို စောင့်ကြည့်ပါ။'),
(9, 2, 'Encourage coughing. If the person can cough forcefully or speak, encourage them to keep coughing to clear the object naturally. Do not interfere.', 
       'ချောင်းဆိုးရန် အားပေးပါ။ လူနာသည် အားရပါးရ ချောင်းဆိုးနိုင်ခြင်း သို့မဟုတ် စကားပြောနိုင်ခြင်း ရှိပါက အသက်ရှူလမ်းကြောင်းပိတ်ဆို့မှုကို သဘာဝအတိုင်း ထွက်လာစေရန် ဆက်တိုက်ချောင်းဆိုးခိုင်းပါ။ ဝင်ရောက်မနှောင့်ယှက်ပါနှင့်။'),
(9, 3, 'Give 5 back blows. If the airway is severely blocked and they cannot speak/cough, lean them forward and give 5 firm blows between the shoulder blades with the heel of your hand.', 
       'ကျောကုန်းကို ၅ ကြိမ် ထုပုတ်ပေးပါ။ အသက်ရှူလမ်းကြောင်း လုံးဝပိတ်နေပါက လူနာကို ရှေ့သို့အနည်းငယ်ကိုင်းစေပြီး ကျောကုန်းအလယ် (ဗဟို) ကို လက်ဖနောင့်ဖြင့် ၅ ကြိမ် ခပ်ပြင်းပြင်း ထုပုတ်ပေးပါ။'),
(9, 4, 'Give 5 abdominal thrusts (Heimlich Maneuver). If the object is still stuck, stand behind the person, wrap your arms around their waist, make a fist just above the navel, and thrust inward and upward 5 times.', 
       'ဝမ်းဗိုက်ကို ၅ ကြိမ် ဆောင့်တွန်းပေးပါ။ အဝတ်/အရာဝတ္ထု ညပ်နေဆဲဖြစ်ပါက လူနာ၏နောက်ကနေ သိုင်းဖက်ပြီး ချက်အထက်နားတွင် လက်သီးဆုပ်ထားကာ အထဲသို့နှင့် အပေါ်သို့ ၅ ကြိမ် ဆောင့်တွန်းပေးပါ။ (Heimlich Maneuver)'),
(9, 5, 'Call emergency services and alternate. If the obstruction persists, call for help immediately. Continue alternating 5 back blows and 5 abdominal thrusts until the object is freed or the person loses consciousness.', 
       'အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပြီး လုပ်ငန်းစဉ်ကို အလှည့်ကျ ဆက်လုပ်ပါ။ ပိတ်ဆို့နေဆဲဖြစ်ပါက ကယ်ဆယ်ရေးအဖွဲ့ထံ ချက်ချင်းဖုန်းခေါ်ဆိုပါ။ ပစ္စည်းထွက်မလာမချင်း သို့မဟုတ် လူနာသတိမလစ်မချင်း ကျောပုတ် ၅ ကြိမ်၊ ဝမ်းဗိုက်ဆောင့် ၅ ကြိမ်ကို တလှည့်စီ ဆက်တိုက်ပြုလုပ်ပေးပါ။'),
(9, 6, 'Begin CPR if they become unconscious. Lower the person gently to the floor. Call emergency services if not already done, and begin chest compressions immediately. Look inside the mouth during rescue breaths.', 
       'လူနာ သတိလစ်သွားပါက ချက်ချင်း CPR စတင်ပါ။ လူနာကို ကြမ်းပြင်ပေါ် ညင်သာစွာ လှဲချပါ။ အရေးပေါ်အဖွဲ့ထံ ဖုန်းမခေါ်ရသေးပါက ခေါ်ဆိုပြီး ချက်ချင်း ရင်ဘတ်ဖိနှိပ်ခြင်း (CPR) စတင်ပါ။ လေမှုတ်သွင်းချိန်တွင် ပါးစပ်ထဲ၌ ညပ်နေသောအရာ မြင်ရ၊ မမြင်ရ ကြည့်ရှုဖယ်ရှားပါ။');

-- ======================================================
-- CATEGORY 10: FRACTURE (အရိုးကျိုးခြင်း)
-- ======================================================
INSERT INTO first_aid_steps (category_id, step_number, instruction_en, instruction_mm) VALUES
(10, 1, 'Control severe bleeding first. If the fracture involves an open wound with heavy bleeding, apply direct pressure around the bone to stop blood loss using a clean cloth.', 
       'ပြင်းထန်စွာ သွေးထွက်ခြင်းကို အရင်ထိန်းချုပ်ပါ။ အရိုးကျိုးသည့်နေရာတွင် အရေပြားပေါက်ပြဲပြီး သွေးထွက်လွန်နေပါက သန့်ရှင်းသောအဝတ်ဖြင့် သွေးတိတ်စေရန် အရိုးဘေးပတ်လည်ကို တိုက်ရိုက်ခပ်ပြင်းပြင်း ဖိထားပေးပါ။'),
(10, 2, 'Do not move the injured area. Keep the injured limb as still as possible. Never attempt to straighten a deformed bone or push a bone back into place.', 
       'ဒဏ်ရာရထားသောနေရာကို လုံးဝမရွှေ့ပါနှင့်။ ထိခိုက်ထားသော ခြေလက်ကို တတ်နိုင်သမျှ ငြိမ်ငြိမ်ထားပါ။ ကောက်ကွေးသွားသော အရိုးကို အတင်းပြန်ဆန့်ခြင်း သို့မဟုတ် ပြူးထွက်နေသောအရိုးကို နေရာပြန်သွင်းရန် လုံးဝမကြိုးစားပါနှင့်။'),
(10, 3, 'Immobilize and splint the area. Apply a splint (using rolled newspapers, boards, or folded cardboard) above and below the injured joint to keep it rigid. Secure with cloth straps, but do not tie too tightly.', 
       'ကျပ်စည်းပြီး ငြိမ်အောင်ထားပါ။ လှုပ်ရှားမှုမရှိစေရန် ဒဏ်ရာရထားသော အဆစ်၏ အပေါ်နှင့်အောက်တွင် ကျပ်ပြား (လိပ်ထားသော သတင်းစာ၊ သစ်သားပြား သို့မဟုတ် ကတ်ထူပြား) ခံပြီး အဝတ်စဖြင့် စည်းနှောင်ပါ။ သွေးလှည့်ပတ်မှု မပိတ်စေရန် အလွန်တင်းကျပ်စွာ မစည်းရပါ။'),
(10, 4, 'Apply cold packs to reduce swelling. Wrap ice or a cold pack in a cloth and apply it to the injured area for up to 20 minutes. Do not apply ice directly to the bare skin.', 
       'ရောင်ရမ်းမှုကျစေရန် ရေခဲကပ်ပေးပါ။ ရေခဲ သို့မဟုတ် ရေခဲထုပ်ကို အဝတ်ဖြင့်ပတ်ပြီး ဒဏ်ရာရထားသောနေရာပေါ်တွင် မိနစ် ၂၀ ခန့် ကပ်ပေးပါ။ ရေခဲကို အရေပြားပေါ် တိုက်ရိုက်တင်၍ မကပ်ရပါ။'),
(10, 5, 'Elevate the limb if possible and call for help. If it does not cause further pain, elevate the injured limb above heart level to reduce swelling. Call emergency services or safely transport to the hospital.', 
       'ခြေလက်ကို မြှင့်ထားပြီး အကူအညီတောင်းပါ။ နာကျင်မှု ပိုမဆိုးစေပါက ရောင်ရမ်းမှုကျစေရန် ဒဏ်ရာရထားသော ခြေလက်ကို နှလုံးအထက် မြှင့်ထားပေးပါ။ အရေးပေါ်အဖွဲ့ထံ ဖုန်းခေါ်ဆိုပါ (သို့မဟုတ်) ဆေးရုံသို့ စနစ်တကျ ပို့ဆောင်ပါ။');

-- Final Verification Query across ALL 10 categories
SELECT category_id, COUNT(*) 
FROM first_aid_steps 
GROUP BY category_id
ORDER BY category_id;

-- ======================================================
-- 4. EMERGENCY CONTACTS SEED (Sample Static Records for Development)
-- ======================================================
-- Point Coordinates: SRID 4326 (Longitude, Latitude) - Yangon Core Area
INSERT INTO emergency_contacts (name_en, name_mm, phone, type, location) VALUES
(
    'Yangon Rescue Team', 'ရန်ကုန်တိုင်း ကယ်ဆယ်ရေးအဖွဲ့', '091111111', 'RESCUE_TEAM', 
    ST_GeographyFromText('SRID=4326;POINT(96.1561 16.8052)')
),
(
    'Myanmar Red Cross', 'မြန်မာနိုင်ငံ ကြက်ခြေနီအသင်း', '092222222', 'RED_CROSS', 
    ST_GeographyFromText('SRID=4326;POINT(96.1292 16.7931)')
),
(
    'Yangon Ambulance Service', 'ရန်ကုန် အရေးပေါ်လူနာတင်ယာဉ်ဝန်ဆောင်မှု', '192', 'AMBULANCE', 
    ST_GeographyFromText('SRID=4326;POINT(96.1743 16.7794)')
),
(
    'Fire Services Department', 'မီးသတ်ဦးစီးဌာန', '191', 'FIRE_DEPARTMENT', 
    ST_GeographyFromText('SRID=4326;POINT(96.1610 16.7820)')
);

-- ======================================================
-- 5. MEDICAL FACILITIES SEED (Sample Static Records for Development)
-- ======================================================
INSERT INTO medical_facilities (name_en, name_mm, phone, address_en, address_mm, type, location) VALUES
(
    'Yangon General Hospital', 'ရန်ကုန်ပြည်သူ့ဆေးရုံကြီး', '01256112', 
    'Bogyoke Aung San Road, Latha Township', 'ဗိုလ်ချုပ်အောင်ဆန်းလမ်း၊ လသာမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1517 16.7792)')
),
(
    'New Yangon General Hospital', 'ရန်ကုန်ဆေးရုံသစ်ကြီး (ဂျပန်ဆေးရုံ)', '01371131', 
    'Ziwaka Road, Dagon Township', 'ဇီဝကလမ်း၊ ဒဂုံမြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1452 16.7865)')
),
(
    'Insein General Hospital', 'အင်းစိန်ပြည်သူ့ဆေးရုံကြီး', '01640037', 
    'Mingaladon Road, Insein Township', 'မင်္ဂလာဒုံလမ်း၊ အင်းစိန်မြို့နယ်', 'HOSPITAL', 
    ST_GeographyFromText('SRID=4326;POINT(96.1112 16.8882)')
),
(
    'ABC Clinic', 'ABC အထွေထွေရောဂါကုဆေးခန်း', '094444444', 
    'Hledan Road, Kamayut Township', 'လှည်းတန်းလမ်း၊ ကမာရွတ်မြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1278 16.8256)')
),
(
    'DEF Clinic', 'DEF မိသားစုဆေးခန်း', '095555555', 
    'Parami Road, Yankin Township', 'ပါရမီလမ်း၊ ရန်ကင်းမြို့နယ်', 'CLINIC', 
    ST_GeographyFromText('SRID=4326;POINT(96.1652 16.8411)')
);

-- Verification counts to ensure seed success
SELECT 'users' AS table_name, COUNT(*) FROM users
UNION ALL
SELECT 'emergency_categories', COUNT(*) FROM emergency_categories
UNION ALL
SELECT 'first_aid_steps', COUNT(*) FROM first_aid_steps
UNION ALL
SELECT 'emergency_contacts', COUNT(*) FROM emergency_contacts
UNION ALL
SELECT 'medical_facilities', COUNT(*) FROM medical_facilities;