from django.shortcuts import render
from django.shortcuts import render
from .models import *
static_content= {
    "ar":
    {
        "lang":"ar",
        "switch_lang":"en",
        "switch_language":"English",
        "search_here":"ابحث هنا",
        "search":"بحث",
        "service_points":"نقاط الخدمة",
        "use_the_map":"استخدم الخريطة لمعرفة أقرب صراف اليك أو فرع بنك إنما ",
        "inma_service_point_address":"عنوان نقاط خدمة بنك إنماء",
        "inma_service_point_addresses":"عناوين نقاط خدمة بنك إنماء",
        "contact_numbers":"أرقام التواصل",
        "work_time":"أوقات الدوام",
        "hour":"ساعة",
        "inma_service_point":"نقطة خدمة بنك إنماء",
        "inma_service_points":"نقاط خدمة بنك إنماء",
        "language":"العربية",
        "ask_or_request_for_service":"للإستفسار او طلب الخدمة يرجى تعبئة الحقول معا رسالة توضح طلبك",
        "send":"ارسال",
        "loan_app":"تقديم طلب تمويل",
        "loan_app_msg":"لتقديم طلب تمويل انقر على الزر التالي",
        "currency":"العملة",
        "services":"الخدمات",
        "applications":"التطبيقات",
        "section":"القسم",
        "policies":"السياسات",
        "purchase":"شراء",
        "sell":"بيع",
        "currency_rate":"أسعار العملات",
        "currency_rate_msg":"سعر صرف العملات الأجنبية مقابل الريال اليمني",
        "direction":"rtl",
        "main":"الرئيسية",
        "request_open_account":"طلب فتح حساب",
        "apply_for_account":"تقديم طلب فتح حساب",
        "register":"انشاء حساب",
        "login":"تسجيل الدخول",
        "company_services":"خدمات الشركات",
        "organization_services":"خدمات المنظمات",
        "service_title2":"باقة فريدة من الخدمات البنكية المتطورة",
        "individual_services":"خدمات الأفراد",
        "pages_and_sections":"اقسام وصفحات",
        "service_title3":"تحويل .. سهولة .. ابتكار",
        "bank_applications":"تطبيقات البنك",
        "about":"عن البنك",
        "copy_rights":"جميع الحقوق محفوظة © لـ بنك الإنماء للتمويل الأصغر الإسلامي 2023",
        "privacy_policy":"سياسة الخصوصية",
        "free_number":"الرقم المجاني ",
        "mail_box":"صندوق البريد ",
        "email_address":"البريد الإلكتروني",
        "fax":"فاكس",
        "put_your_email_address":"ادخل ايميلك في الأسفل",
        "put_your_email_address_msg":". واحصل على اخر الأخبار في الصرافه  والعروض التمويلية المقدمة منا اول بأول في صندوق الوارد الخاص بك.   .",
        "stay_in_touch":"ابق على إطلاع بآخر أخبار البنك",
        "subscribe":"إشتراك",
        "board":"مجلس الإدارة",
        "our_service_points":"نقاط تواجدنا",
        "account_points":"نقاط حساب",
        "inma_faori":"الإنماء فوري",
        "inma_jawal":"الإنماء جوال",
        "yearly_reports":"تقارير سنوية",
        "financial_reports":"تقارير مالية",
        "download_report":"تنزيل التقرير",
        "issue_date":"تاريخ الإصدار",
        "bank_news":"اخبار البنك",
        "events":"الفعاليات",
        "blog":"المدونة",
        "news_center":"المركز الإعلامي",
        "contact_us":"تواصل معنا",
        "phone_1":"هاتف 1 ",
        "phone_2":"هاتف 2 ",
        "agencies":"التوكيلات",
        "pages":"الصفحات",
        "reports":"التقارير",
        "money_washing":"مكافحة غسل الأموال",
        "service_points_in_region":"تعرف على نقاط الخدمة في منطقتك",
        "our_services_always_with_you":"خدماتنا دوماً معك",
        "more_details":"عرض تفاصيل أكثر",
        "download_app_now": "حمل التطبيق الأن علــــى ",
        "app_features": "مميزات التطبيق",
        "site_features": "مميزات الموقع",
        "system_features": "مميزات النظام",
        "visit_site": "أو قم بزيارة الموقع",
        "install_system": "أو قم بتحميل النظام",
        "from_here": "من هنا",
        "employement":"التوظيف",
        "training_courses":"الدورات التدريبية",
        "name":"الاسم",
        "education":"المؤهلات العلمية",
        "lang_skills":"مهارات اللغة",
        "computer_skills":"مهارات الحاسب",
        "experiences":"الخبرات",
        "work_domains":"مجالات العمل",
        "bank_known":"معرفين من البنك",
        "general_info":"بيانات عامة",
        "upload_cv":"رفع ملف السيرة",
        "institute_name":"اسم المعهد",
        "education_level":"المستوى التعليمي",
        "speciality":"التخصص",
        "grade":"المعدل",
        "from_date":"من تاريخ",
        "to_date":"إلى تاريخ",
        "course_name":"الدورة",
        "country":"البلد",
        "from_dtae":"من تاريخ",
        "to_date":"الى تاريخ",
        "add":"إضافة",
        "next":"التالي",
        "previous":"السابق",
        "basic_info":"البيانات الأساسية",
        "cv":"السيرة الذاتية",
        "save":"حفظ",
        "add_language":"إضافة لغة",
        "the_language":"اللغة",
        "reading":"القراءه",
        "writing":"الكتابة",
        "speaking":"محادثة",
        "add_computer_skills":"إضافة مهارات حاسوب",
        "number":"رقم",
        "skill_level":"مستوى المهارة",
        "skill_name":"اسم المهارة",
        "place_name":"اسم المحل/الجهة",
        "work_owner_name":"اسم صاحب العمل",
        "work_address":"عنوان العمل",
        "work_phone":"تلفون العمل",
        "last_salary":"الراتب في النهاية",
        "first_salary":"الراتب في البداية",
        "last_job":"المسمى الوظيفي في النهاية",
        "first_job":"المسمى الوظيفي في البداية",
        "tasks":"المهام",
        "work_hours":"عدد ساعات العمل",
        "leave_reason":"سبب ترك العمل",
        "job_title":"اسم العمل",
        "add_work_domains":"اضافة مجالات العمل",
        "work_domain":"مجال العمل",
        "add_reference":"اضافة مرجع",
        "telephone":"التلفون",
        "work":"العمل",
        "general_info":"معلومات عامة",
        "update":"تعديل",
        "relation_type":"صلة القرابة",
        "cv_file":"ملف السيرة الذاتية",
        "upload_file":"رفع الملف",
        "add_cv_file":"اضافة ملف السيرة الذاتية",
        "create_account":"انشاء حساب جديد",
        "alinma_bank":"بنك الإنماء",
        "new_user":"مستخدم جديد؟ ",
        "client_data":"بيانات العميل",
        "project_data":"بيانات المشروع",
        "loan_app_detail":"تفاصيل طلب التمويل",
        "submit_loan_app":"إرسال الطلب",
        "fill_account_data":"تعبئة بيانات متطلبات الحساب",
        "birth_info":"بيانات  الميلاد",
        "personal_info":"بيانات شخصية",
        "livig_address":"عنوان السكن الاقامة الميلاد",
        "id_info":"بيانات الهوية الشخصية",
        "video_library":"مكتبة الفيديوهات",
        

    }
    ,
    "en":
    {
        "video_library":"Video Library",
        "id_info":"Personal Identity Information",
        "birth_info":"Birth Information",
        "personal_info":"Personal Information",
        "livig_address":"Living Address",
        "fill_account_data":"Fill the Information",
        "apply_for_account":"Apply For new Account",
        "submit_loan_app":"Apply",
        "client_data":"Client Data",
        "project_data":"Project Data",
        "loan_app_detail":"Loan App Details",
        "new_user":"New User?",
        "create_account":"Create New Account",
        "alinma_bank":"AL-Inma Bank",
        "upload_file":"Upload File",
        "add_cv_file":"Add C.V File",
        "cv_file":"C.V File",
        "update":"Update",
        "general_info":"General Information",
        "relation_type":"Relation Type",
        "work":"Work",
        "telephone":"Telephone",
        "add_reference":"Add Reference",
        "add_work_domains":"Add Work Domains",
        "work_domain":"Work Domain",

        "job_title":"Job Title",
        "work_hours":"Work Hours",
        "leave_reason":"Leave Reason",
        "last_salary":"Last Salary",
        "last_salary":"Last Salary",
        "first_salary":"First Salary",
        "last_job":"Last Job",
        "first_job":"First Job",
        "tasks":"Tasks",
        "place_name":"Place Name",
        "work_owner_name":"Work Owner Name",
        "work_address":"Work Address",
        "work_phone":"Work Telephone",
        "number":"Number",
        "number":"Number",
        "skill_level":"Skill Level",
        "skill_name":"Skill Name",
        "add_computer_skills":"Add Computer Skills",
        "add_language":"Add Language",
        "the_language":"The Language",
        "reading":"Reading",
        "writing":"Writing",
        "speaking":"Speaking",
        "save":"Save",
        "cv":"C.V Information",
        "employement":"Employement",
        "education":"Education",
        "lang_skills":"Language Skills",
        "computer_skills":"Computer Skills",
        "experiences":"Experiences",
        "work_domains":"Work Domains",
        "bank_known":"References in Bank",
        "general_info":"General Information",
        "upload_cv":"Upload cv",                       
        "basic_info":"Basic information",
        "training_courses":"Training Courses",
        "name":"name",
        "institute_name":"Institute Name",
        
        "education_level":"Education Level",
        "speciality":"Speciality",
        "grade":"Grade",
        "from_date":"from date",
        "to_date":"to date",

        

        "course_name":"course name",
        "country":"country",
        "from_dtae":"from dtae",
        "to_date":"to date",
        "add":"Add",
        "next":"Next",
        "previous":"Previous",
        "lang":"en",
        "switch_lang":"ar",
        "switch_language":"العربية",
        "search_here":"Search Here",
        "search":"Search",
        "service_points":"Service Points",
        "inma_service_point":"AL-Inma Service Point",
        "use_the_map":"Use the Map to Know the Nearest Branch or ATM to You.",
        "inma_service_point_address":"AL-Inma Service Point Address",
        "inma_service_point_addresses":"AL-Inma Service Point Addresses",
        "contact_numbers":"Contact Numbers",
        "work_time":"Work Times",
        "hour":"Hour",
        "inma_service_points":"AL-Inma Service Points",
        "language":"English",
        "ask_or_request_for_service":"To Ask or Request for Service Fill the Following Fields.",
        "send":"Submit",
        "loan_app":"Apply for Loan",
        "loan_app_msg":"To Apply for New Loan App Click The Next Button",
        "direction":"ltr",
        "services":"Services",
        "applications":"Applications",
        "section":"Section",
        "policies":"Policies",
        "currency":"Currency",
        "purchase":"Purchase",
        "sell":"Sell",
        "currency_rate":"Currency Rate",
        "currency_rate_msg":"foreign currencies exchange rates against the Yemeni Riyal",
        "main":"Home",
        "request_open_account":"Request Open Account",
        "register":"Register",
        "login":"Login",
        "company_services":"Company Services",
        "organization_services":"Organization Services",
        "service_title2":"Collection of Sophisticated Banking Services",
        "individual_services":"Individual Services",
        "pages_and_sections":"Pages and Sections",
        "service_title3":"Transfer .. Easy .. Invent",
        "bank_applications":"Bank Applications",
        "about":"About",
        "copy_rights":"All right received © to AL-inma Islamic Microfinance Bank 2023",
        "privacy_policy":"Privacy Policy",
        "free_number":"Free Number",
        "mail_box":"Mail Box",
        "email_address":"Email Address",
        "fax":"Fax",
        "put_your_email_address":"put your email down",
        "put_your_email_address_msg":"receive last news from us.",
        "stay_in_touch":"keep in touch with last news",
        "subscribe":"subscribe",
        "board":"board",
        "our_service_points":"Our Service Points",
        "account_points":"Account Points",
        "inma_faori":"Alinma Furi",
        "inma_jawal":"Alinma Jawal",
        "yearly_reports":"Yearly Reports",
        "financial_reports":"Financial Reports",
        "download_report":"Download Report",
        "issue_date":"Issue Date",
        "bank_news":"Bank News",
        "events":"Events",
        "blog":"Blog",
        "news_center":"Knowledge Center",
        "contact_us":"Contact Us",
        "phone_1":"Phone 1 ",
        "phone_2":"Phone 2 ",
        "agencies":"Agents",
        "pages":"Pages",
        "reports":"Reports",
        "money_washing":"Anti money laundering",
        "service_points_in_region":"Service Points at Your Region",
        "our_services_always_with_you":"Our Services Always with You",
        "more_details":"More Details",
        "download_app_now": "Download App Now",
        "app_features": "App Features",
        "site_features": "Site Features",
        "system_features": "System Features",
        "visit_site": "Visit the Site",
        "install_system": "Install the System",
        "from_here": "From Here",
    }
}
def SettingModelQuerySet():
    queryset = SettingModel.objects.filter(
        is_deleted=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except SettingModel.DoesNotExist:
        print(" OurVision DoesNotExist ")
    return queryset
