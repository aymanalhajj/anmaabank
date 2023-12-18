from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from country_regions.models import Country, Region, Directorate, Isolation
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from SendEmile.views import *
from tinymce.models import HTMLField
from django.shortcuts import reverse
import os
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe


CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)
SELECT_specialization = (


    ("Architectural Management", "Architectural Management"),

    ("Advertising Management", "Advertising Management"),
    ("Asset Management", "Asset Management"),
    ("Audit Management", "Audit Management"),
    ("Aviation Management", "Aviation Management"),
    ("Agriculture Management", "Agriculture Management"),
    ("Air Transport Management", "Air Transport Management"),


    ("Banking Management", "Banking Management"),
    ("BPO Management", "BPO Management"),
    ("Business Marketing", "Business Marketing"),
    ("Business Administration", "Business Administration"),
    ("Bio-Technology Management", "Bio-Technology Management"),

    (
        "Corporate Social Responsibility",
        "Corporate Social Responsibility",
    ),

    (
        "Customer Relationship Management",
        "Customer Relationship Management",
    ),
    # ('Customer Relationship Management', 'Customer Relationship Management'),
    ('Customer Care Management', 'Customer Care Management'),
    ('Call center Management', 'Call center Management'),
    ('Clinical Pharmacology', 'Clinical Pharmacology'),
    ('Clinical Research', 'Clinical Research'),
    ('Co-operative Management', 'Co-operative Management'),
    # ('Corporate Social Responsibility', 'Corporate Social Responsibility'),
    ('Cost and Management Accounting', 'Cost and Management Accounting'),
    ('Corporate and Finance Management', 'Corporate and Finance Management'),
    ('Consumer Management', 'Consumer Management'),
    ('Corporate Law', 'Corporate Law'),
    ('Corporate Training', 'Corporate Training'),
    ('Cyber Law Management', 'Cyber Law Management'),
    ('Civil Management', 'Civil Management'),
    ('Communication Management', 'Communication Management'),
    ('Construction Management', 'Construction Management'),
    ('Chartered Finance Management', 'Chartered Finance Management'),

    ('Data Management', 'Data Management'),
    ('Dairy Management', 'Dairy Management'),

    ('Equity Research Management', 'Equity Research Management'),
    ('Equality Research Management', 'Equality Research Management'),
    ('Export Management', 'Export Management'),
    ('Entrepreneurship Management', 'Entrepreneurship Management'),
    ('E-Business System ', 'E-Business System'),
    ('E-commerce', 'E-commerce'),
    ('Environmental Management', 'Environmental Management'),
    ('Event Management', 'Event Management'),
    ('Entrepreneur Management', 'Entrepreneur Management'),
    ('Energy Management', 'Energy Management'),


    ('Foreign Exchange Management', 'Foreign Exchange Management'),
    ('Finance Management', 'Finance Management'),
    ('Foreign Trade ', 'Foreign Trade'),
    ('Family Business Management', 'Family Business Management'),

    ('General Management', 'General Management'),

    ('Hospital Administration', 'Hospital Administration'),
    ('Health Care Management', 'Health Care Management'),
    ('Holistic Management', 'Holistic Management'),
    ('Hospital Management', 'Hospital Management'),
    ('Hotel Management', 'Hotel Management'),
    ('Hospitality Management', 'Hospitality Management'),
    ('Hardware Management', 'Hardware Management'),
    ('Human Resource Management', 'Human Resource Management'),
    ('Interior Management', 'Interior Management'),
    ('Information Management', 'Information Management'),
    ('Investment Analysis Management', 'Investment Analysis Management'),
    ('Investment Management', 'Investment Management'),
    ('International Finance Management', 'International Finance Management'),
    ('International Management', 'International Management'),
    ('International Trade', 'International Trade'),
    ('Industrial Marketing', 'Industrial Marketing'),
    ('International Marketing', 'International Marketing'),
    ('Information Technology', 'Information Technology'),
    ('Infrastructure Management', 'Infrastructure Management'),
    ('Industrial Management', 'Industrial Management'),
    ('Intellectual Property Rights', 'Intellectual Property Rights'),



    ('Logistics Management', 'Logistics Management'),
    ('Labour Law Management', 'Labour Law Management'),
    ('Library Management', 'Library Management'),


    ('Mass Communication', 'Mass Communication'),
    ('Media Management', 'Media Management'),
    ('Marketing Management', 'Marketing Management'),
    ('Mutual Fund Management', 'Mutual Fund Management'),
    ('Marketing Research', 'Marketing Research'),
    ('Market Risk Management', 'Market Risk Management'),
    ('Material Management', 'Material Management'),
    ('Marketing Finance Management', 'Marketing Finance Management'),
    ('Management Control Systems', 'Management Control Systems'),
    ('Maintenance Management', 'Maintenance Management'),

    ('Networking Management', 'Networking Management'),

    ('Operation Management', 'Operation Management'),
    ('Petroleum Management', 'Petroleum Management'),
    ('Production Management', 'Production Management'),
    ('Project Management', 'Project Management'),
    ('Packaging Management', 'Packaging Management'),
    ('Purchasing Management', 'Purchasing Management'),
    ('Personal Management', 'Personal Management'),
    ('Public Administration', 'Public Administration'),
    ('Purchase Management', 'Purchase Management'),
    ('Portfolio Management', 'Portfolio Management'),
    ('Public Relationship Management', 'Public Relationship Management'),
    ('Product Management', 'Product Management'),
    ('Personal Finance Management', 'Personal Finance Management'),
    ('Pharmacology Management', 'Pharmacology Management'),
    ('Pathology Lab Management', 'Pathology Lab Management'),


    ('Risk and Insurance Management', 'Risk and Insurance Management'),
    ('Retail Management', 'Retail Management'),
    ('Rural Marketing', 'Rural Marketing'),
    ('Rural Management', 'Rural Management'),
    ('Risk Management', 'Risk Management'),


    ('Stock Management', 'Stock Management'),
    ('Sales Management', 'Sales Management'),
    ('Sevices Marketing', 'Sevices Marketing'),
    ('Social Media Marketing', 'Social Media Marketing'),
    ('Supply chain Management', 'Supply chain Management'),
    ('Software Project Management', 'Software Project Management'),
    ('SAP Consultancy Management', 'SAP Consultancy Management'),
    ('Software Management', 'Software Management'),
    ('School Management', 'School Management'),
    ('Shipping Management', 'Shipping Management'),
    ('Safety Management', 'Safety Management'),



    ('Telecom Management', 'Telecom Management'),
    ('Taxation Management', 'Taxation Management'),
    ('Takeover and Acquisition Management',
     'Takeover and Acquisition Management'),
    ('Treasury Management', 'Treasury Management'),
    ('Travel and Tourism Management', 'Travel and Tourism Management'),
    ('Transport Management', 'Transport Management'),
    ('Total Quality Management', 'Total Quality Management'),
    ('Total Safety Management', 'Total Safety Management'),
    ('Total Quality Management', 'Total Quality Management'),
    ('Ware House Management', 'Ware House Management'),
    ('othar', 'تخصص أخر'),

)
lang = (
    ('Abkhaz', 'Abkhaz'),
    ('Afrikaans', 'Afrikaans'),
    ('Albanian', 'Albanian'),
    ('Amharic', 'Amharic'),
    ('Arabic', 'Arabic'),
    ('Assamese', 'Assamese'),
    ('Basque', 'Basque'),
    ('Belarusian', 'Belarusian'),
    ('Bengali', 'Bengali'),
    ('Berber', 'Berber'),
    ('Bhojpuri', 'Bhojpuri'),
    ('Bosnian', 'Bosnian'),
    ('Bulgarian', 'Bulgarian'),
    ('Cantonese Chinese', 'Cantonese Chinese'),
    ('Catalan', 'Catalan'),
    ('Chinese', 'Chinese'),
    ('Croatian', 'Croatian'),
    ('Czech', 'Czech'),
    ('Danish', 'Danish'),
    ('Dutch', 'Dutch'),
    ('English', 'English'),
    ('Estonian', 'Estonian'),
    ('Faroese', 'Faroese'),
    ('Fijian', 'Fijian'),
    ('Finnish', 'Finnish'),
    ('French', 'French'),
    ('Frisian', 'Frisian'),
    ('Filipino', 'Filipino'),
    ('Fula', 'Fula'),
    ('Gaelic', 'Gaelic'),
    ('Gan', 'Gan'),
    ('Georgian', 'Georgian'),
    ('German', 'German'),
    ('Greek', 'Greek'),
    ('Gujarati', 'Gujarati'),
    ('Haitian Creole', 'Haitian Creole'),
    ('Hakka', 'Hakka'),
    ('Hausa', 'Hausa'),
    ('Hawaiian', 'Hawaiian'),
    ('Hebrew', 'Hebrew'),
    ('Hindi', 'Hindi'),
    ('Hmong', 'Hmong'),
    ('Hungarian', 'Hungarian'),
    ('Ibibio', 'Ibibio'),
    ('Icelandic', 'Icelandic'),
    ('Igbo', 'Igbo'),
    ('Inuinnaqtun', 'Inuinnaqtun'),
    ('Inuktitut', 'Inuktitut'),
    ('Irish', 'Irish'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Javanese', 'Javanese'),
    ('Kannada', 'Kannada'),
    ('Kashmiri', 'Kashmiri'),
    ('Khmer', 'Khmer'),
    ('Kazakh', 'Kazakh'),
    ('Korean', 'Korean'),
    ('Kurdish', 'Kurdish'),
    ('Kyrgyz', 'Kyrgyz'),
    ('Lao', 'Lao'),
    ('Lugandan', 'Lugandan'),
    ('Malagasy', 'Malagasy'),
    ('Malay (or Maysian)', 'Malay (or Maysian)'),
    ('Moldovian', 'Moldovian'),
    ('Oriya', 'Oriya'),
    ('Russian', 'Russian'),
    ('Romanian', 'Romanian'),
    ('Somali', 'Somali'),
    ('Spanish', 'Spanish'),
    ('Slovene', 'Slovene'),
    ('Slovak', 'Slovak'),
    ('Turkish', 'Turkish'),
    ('Ukrainian', 'Ukrainian'),
    ('Xiang', 'Xiang'),
    ('Vietnamese', 'Vietnamese'),
    ('Xhosa', 'Xhosa'),
    ('Zhuang', 'Zhuang'),

    ('othar', 'لغة أخرى'),

)


SELECT_COUNTRY = {
    ('اليمن', 'اليمن'),
    ('مصر', 'مصر'),
    ('قطر', 'قطر'),
    ('الامارات', 'الامارات'),
    ('السعودية', 'السعودية'),


    ('سوريا', 'سوريا'),
    ('السودان', 'السودان'),
    ('الاردن', 'الاردن'),
    ('العراق', 'العراق'),
    ('كوريا', 'كوريا'),
    ('روسيا', 'روسيا'),

    ('امريكا', 'امريكا'),
    ('ماليزيا', 'ماليزيا'),
    ('بريطانيا', 'بريطانيا'),
    ('بريطانيا', 'بريطانيا'),
    ('فرنسا', 'فرنسا'),


}
SELECT_CITY = (
    ('صنعاء', 'صنعاء'),
    ('عدن', 'عدن'),
    ('تعز', 'تعز'),
    ('إب', 'إب'),
    ('الحديدة', 'الحديدة'),
    ('حجة', 'حجة'),
    ('عمران', 'عمران'),
    ('ريمة', 'ريمة'),
    ('البيضاء', 'البيضاء'),
    ('المحويت', 'المحويت'),
    ('المهرة', 'المهرة'),
    ('الجوف', 'الجوف'),
    ('شبوة', 'شبوة'),
    ('حضرموت - المكلا', 'حضرموت - المكلا')
)
SELECT_SKILLS = (
    ('ممتاز', 'ممتاز'),
    ('جيد جدا', 'جيد جدا'),
    ('جيد', 'جيد'),
    ('ضعيف', 'ضعيف')
)

SELECT_MARIDE = (
    ('عازب', 'عازب'),
    ('متزوج', 'متزوج'),
    ('مطلق', 'مطلق'),
)
SELECT_GERDER = (
    ('ذكر', 'ذكر'),
    ('أنثى', 'أنثى')
)
SELECT_NOW_US = (
    ('عن طريق موظف لديكم', 'عن طريق موظف لديكم'),
    ('الاعلان بفروع المصرف', 'الاعلان بفروع المصرف'),
    ('الاعلان عبر الموقع', 'الاعلان عبر الموقع'),
    ('صفحة توظيف بالفيس بوك', 'صفحة توظيف بالفيس بوك'),
    ('عن طريق ملصق اعلاني', 'عن طريق ملصق اعلاني'),
    ('مكتب توظيف', 'مكتب توظيف'),
    ('اخرى', 'اخرى')


)
CHECK_ANSER = (
    ('نعم', 'نعم'),
    ('لا', 'لا')
)


def file_size(value):  # add this to some file where you can import it from
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            'حجم الملف كبير جداً - الحد الاقصى والمسموح لك بالحفظ هي 10 ميجا.')


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'الملف غير مسموح لك حفظه الرجاء ادخال صيغة مدعومه فقط - نوع الملف pdf او png او jpg او doc او docx ')


class Register(models.Model):
    """ Customize default User model """

    username = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_('اسم المستخدم'))
    full_name = models.CharField(
        max_length=500, verbose_name=_('الاسم الكامل'))
    email = models.EmailField(
        unique=False, verbose_name=_('البريد الإلكتروني'))
    password = models.CharField(max_length=200, verbose_name=_('كلمة السر'))
    confirmpassword = models.CharField(
        max_length=200, verbose_name=_('تأكيد كلمة السر'))
    gender = models.CharField(
        choices=SELECT_GERDER, max_length=10, default='ather', verbose_name=_('الجنس'))
    governorate = models.ForeignKey(
        Region,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_('المحافظة')
    )
    # governorate = models.CharField(
    #     choices=SELECT_CITY, max_length=200, verbose_name=_('المحافظة'))
    city = models.CharField(max_length=200, verbose_name=_('المدينة'))
    address = models.CharField(max_length=200, verbose_name=_('العنوان'))
    village = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_('القرية/الحي'))
    idnumber = models.IntegerField(unique=False, verbose_name=_('رقم البطاقة'))
    Release_date = models.CharField(
        max_length=200, verbose_name=_('تاريخ الإصدار'))
    place_issue = models.CharField(
        max_length=200, verbose_name=_('مكان الإصدار'))
    date_birth = models.CharField(
        max_length=200, verbose_name=_('تاريخ الميلاد'))
    place_birth = models.CharField(
        max_length=200, verbose_name=_('محل الميلاد'))
    marital_status = models.CharField(
        choices=SELECT_MARIDE, max_length=200, verbose_name=_('الحالة الاجتماعية'))
    number_childer = models.IntegerField(
        blank=True, null=True, verbose_name=_('عدد من تعولهم'))
    current_address = models.CharField(
        max_length=200, verbose_name=_('العنوان الحالي'))
    permanent_address = models.CharField(
        max_length=300, verbose_name=_('عنوان السكن الدائم'))
    mobile_number = models.IntegerField(
        unique=False, verbose_name=_('رقم الموبايل'))
    number_whatsapp = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_('رقم الواتساب'))
    link_facebook = models.URLField(
        max_length=400, blank=True, null=True, verbose_name=_('صفحتك على الفيسبوك'))
    link_twiter = models.URLField(
        max_length=400, blank=True, null=True, verbose_name=_('صفحتك على منصة x تويتر سابقاً'))
    link_instigrem = models.URLField(
        max_length=500, blank=True, null=True, verbose_name=_('صفحتك على الإنستجرام'))
    created_at = models.DateTimeField(
        auto_now_add=timezone.now, verbose_name=_('تاريخ الإنشاء'))
    cv_uploaded_file = models.FileField(

        upload_to="Image/cv/%Y/%m/%d/%H/%M/%S",
        validators=[file_size, validate_file_extension],
        verbose_name=_(
            'ملف السيرة الذاتية / pdf or png or jpg or doc or docx  '),
        help_text=_(" نوع الملف pdf او png او jpg او doc او docx فقط والحجم لا يزيد 10 ميجا  ")
    )

    def cv_dispaly(self):
        if self.cv_uploaded_file:
            extension = os.path.splitext(self.cv_uploaded_file.name)
            if extension[1] == '.pdf':
                return mark_safe(f"<object width=100% height=300px data={self.cv_uploaded_file.url}  type=application/pdf></object>")
            elif extension == '.doc':
                return mark_safe(f"<object width=100% height=300px data={self.cv_uploaded_file.url}  type=application/pdf></object>")
            elif extension[1] == 'png' or extension[1] == '.jpg':
                return mark_safe(f'<image width=300px height=300px src={self.cv_uploaded_file.url}></image>')
            else:
                return mark_safe(f'<image width=300px height=300px src={self.cv_uploaded_file.url}></image>')

        else:
            return mark_safe(f"<span>  لايوجد شهادة </span>")

    def cv_dispalys(self):
        if self.cv_uploaded_file != None:
            extension = os.path.splitext(self.cv_uploaded_file.name)
            print("extension")
            print(extension[1])

            if extension[1] == '.pdf':
                return "<object width=100% height=300px data="+self.cv_uploaded_file.url+"  type=application/pdf></object>"
            elif extension == '.doc':
                return "<object width=100% height=300px data="+self.cv_uploaded_file.url+"  type=application/pdf></object>"
            elif extension[1] == 'png' or extension[1] == '.jpg':
                return '<image width=300px height=300px src='+self.cv_uploaded_file.url+'></image>'
            else:
                return '<image width=300px height=300px src='+self.cv_uploaded_file.url+'></image>'

        else:
            return "<span>  لايوجد cv </span>"

    session = models.OneToOneField(
        Session, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('الجلسة'))

    # username = None
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['mobile_number']

    class Meta:
        managed = True
        verbose_name = _(" الحسابات  ")
        verbose_name_plural = _(" الحسابات  ")

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('home-jop-manage-admin-ad'  # args=[self.pk,
                       #          #  self.month,
                       #          #  self.published.day,
                       #          #  self.slug
                       #          ]
                       ,  kwargs={"id": self.pk, "": "/"}

                       )

    def save(self, *args, **kwargs):
        if self.id == None:
            SignUpValidete.objects.create(email=self.email,
                                          user=self.id
                                          )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


def getUrl(request):
    if request is None:
        raise Exception("request is None")
    # print("url_name")
    # print(request.build_absolute_uri())
    return request.build_absolute_uri()


class SignUpValidete(models.Model):
    code = models.BigIntegerField(unique=False)
    email = models.EmailField()
    created_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    quality_score = models.FloatField()
    is_valid_format = models.BooleanField(null=True, blank=True)
    is_free_email = models.BooleanField(null=True, blank=True)
    is_disposable_email = models.BooleanField(null=True, blank=True)
    is_role_email = models.BooleanField(null=True, blank=True)
    is_catchall_email = models.BooleanField(null=True, blank=True)
    is_mx_found = models.BooleanField(null=True, blank=True)
    is_smtp_valid = models.BooleanField(null=True, blank=True)
    create_at = models.DateField(
        auto_now_add=timezone.now, verbose_name=_('تاريخ الإنشاء:'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="SignUpValideteRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))

    objects = UserManager()

    class Meta:
        managed = True
        verbose_name = _(" التحقق من الايميل  ")
        verbose_name_plural = _(" التحقق من الايميل  ")

    # longitude = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()

        # Convert the date and time to an integer using the timestamp() method
        timestamp = int(now.timestamp())

        # Print the integer value
        print(timestamp)
        self.code = str(timestamp)
        self.quality_score = 0.8

        # if self.sort_no is None:
        # self.sort_no = self.id
        # else:
        # self.code = self.sort_no
        super().save(*args, **kwargs)
        subject = 'Your Subject'
        template_name = 'jop/email_template.html'
        context = {"switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
            'verification_link': 'https://alinmabank.com/passswordrest/'+self.code}
        html_message = render_to_string(
            'jop/email_template.html', {'context': context})
        recipient_list = [self.email]
    #     send_email(     "This is an important message.",
    #                     "This is an important message.",
    #                     html_content=html_message,
    #                     is_html_content=True,
    #                     # to="ialzoriqi@gmail.com",
    #                     to_list=[recipient_list]
    # )
        # sendEmile()
        send_email("This is an important message. Code email validation.",
                   "Code email validation. "+'verification_link' +
                   '  https://alinmabank.com/verification/'+self.code,
                   # html_content=html_message,
                   is_html_content=False,
                   to=self.email
                   # to_list=recipient_list
                   )


class Jobs(models.Model):
    # id=models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100, blank=True,
                            verbose_name=_('اسم المجال'))
    type = models.CharField(max_length=100, blank=True,
                            verbose_name=_('نوع المجال'))
    description = HTMLField(null=True, verbose_name=_('الوصف'))
    # job_type = models.CharField(
    #     max_length=30, choices=CHOICES, verbose_name=_(' النوع '), default='Full Time', null=True)
    created_at = models.DateTimeField(
        null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    # created_at = models.DateTimeField(
    # null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name=_("تاريخ التعديل")
    )
    edite_at = models.DateTimeField(
        null=True,    auto_now=True, editable=False, blank=True, verbose_name=_("تاريخ التعديل "))
    # order_num = models.PositiveIntegerField(
    #     blank=True, null=True, verbose_name=_('رقم الطلب'))
    # image = models.ImageField(upload_to="Image/Jobs/%Y/%m/%d/%H/%M/%S",
    #                           verbose_name=_('صورة المجال'))
    task = HTMLField(
        null=True, verbose_name=_('مهام الوظيفة'))
    # task1 = HTMLField(blank=True,
    #                   null=True, verbose_name=_('المهمة 1'))
    # task2 = HTMLField(blank=True,
    #                   null=True, verbose_name=_('المهمة 2'))
    # task3 = HTMLField(blank=True,
    #                   null=True, verbose_name=_('المهمة 3'))
    conditions = HTMLField(null=True, verbose_name=_('شروط الوظيفة'))
    # conditions1 = HTMLField(blank=True, null=True, verbose_name=_('الشروط 1'))
    # conditions2 = HTMLField(blank=True, null=True, verbose_name=_('الشروط 2'))
    # conditions3 = HTMLField(blank=True, null=True, verbose_name=_('الشروط 3'))

    class Meta:
        managed = True
        verbose_name = _(" الوظيفة  ")
        verbose_name_plural = _("الوظائف  ")

    # longitude = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('job-singles',  kwargs={"id": self.pk})


class SerchJobsModel(models.Model):
    search = models.CharField(verbose_name=_(
        "ابحث هنا"), blank=True, help_text=_("عنوان الوظيفة  او التخصص او اسم المقدم للوظيفة"), null=True, max_length=64,)
    # category = models.CharField(verbose_name=_(
    # "نوع نقطة الخدمة"), blank=True, null=True, max_length=100, choices=CATEGORU,)
    job = models.ForeignKey(
        Jobs, verbose_name=_("الوظيفة"), blank=True,  on_delete=models.DO_NOTHING, null=True,)

    specialization = models.CharField(
        max_length=100,  blank=True, choices=SELECT_specialization, verbose_name=_('التخصص:'))
    gender = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=SELECT_GERDER,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("الجنس")
    )
    all_data = models.BooleanField(
        # max_length=20,
        # null=True,
        # blank=True,
        default=False,
        # choices=SELECT_GERDER
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("بيانات  شبه مكتملة")
    )


class loginModel(models.Model):
    # emile = models.EmailField(verbose_name=_(
    #     "البريد الالكتروني"), blank=True,
    #     #   help_text="اسم الفرع او اسم الشارع او اسم نقطة الخدمة",
    #       null=True,
    #     max_length=64,)
    email = models.EmailField(
        unique=False, verbose_name=_('البريد الإلكتروني'))
    password = models.CharField(max_length=200, verbose_name=_('كلمة السر'))
    confirmpassword = models.CharField(
        max_length=200, verbose_name=_('تأكيد كلمة السر'))
    re_member_me = models.BooleanField(
        # max_length=200,
        # null=False,
        # blank=False,
        default=True,
        verbose_name=_('تذكرني'))
    right_privecy = models.BooleanField(
        # max_length=200,
        # null=False,
        # blank=False,
        default=True,

        # default=True,
        verbose_name=_('الموافقة على سياسة الخصوصية'))
    # models.CharField(
    #     max_length=20,
    #     null=True,
    #     choices=SELECT_GERDER
    #     # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
    #     verbose_name="الجنس"
    # )
    # category = models.CharField(verbose_name=_(
    # "نوع نقطة الخدمة"), blank=True, null=True, max_length=100, choices=CATEGORU,)
    # job = models.ForeignKey(
    # Jobs, verbose_name=_(
    # "الوظيفة"), blank=True,  on_delete=models.DO_NOTHING, null=True,)

    # specialization = models.CharField(
    #     max_length=100,  blank=True, choices=SELECT_specialization, verbose_name=_('التخصص:'))


class oreder_Jobs(models.Model):
    oreder_message = models.TextField(verbose_name=_('رسالة الطلب'),
                                      help_text=_("يجب أن لا تقل رسالة طلب العمل عن 1250 حرف ")
                                      )
    how_to_now_job = models.CharField(
        max_length=300, choices=SELECT_NOW_US, verbose_name=_('كيف عرفت عنا'))
    created_at = models.DateTimeField(
        null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    # created_at = models.DateTimeField(
    # null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name=_("تاريخ التعديل")
    )
    edite_at = models.DateTimeField(
        null=True,    auto_now=True, editable=False, blank=True, verbose_name=_("تاريخ التعديل "))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             null=True, blank=True, verbose_name=_('المستخدم'),
                             related_name="oreder_Jobs_user"
                             )
    job = models.ForeignKey(Jobs, on_delete=models.SET_NULL,
                            null=True, blank=True, verbose_name=_('الوظيفة'))

    class Meta:
        managed = True
        verbose_name = _(" طلب تقديم للوظيفة  ")
        verbose_name_plural = _(" طلبات التقديم للوظائف  ")

    # longitude = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.id)


class Education(models.Model):
    id = models.IntegerField(
        auto_created=True, primary_key=True, verbose_name=_("الرقم"))
    name_educational_institution = models.CharField(
        max_length=100, verbose_name=_('اسم المؤسسة التعليمية:'))
    country = models.ForeignKey(
        Country,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_('البلد')
    )    # country = models.CharField(
    #     max_length=100, blank=True, choices=SELECT_COUNTRY, verbose_name=_('البلد:'))
    sducation_level = models.CharField(max_length=100,
                                       choices=[('primary', "ابتدئي"), ("general secondary", "ثنوية عامة"),
                                                ("diploma", "دبلوم"),
                                                ("higher_diploma", "دبلوم عالي"),
                                                ("bachelor", "بكالوريوس"),
                                                ("master", "ماجستير"),
                                                ("doctor", "دكتورة"),
                                                # ("widow", "بروفيسور")   ,
                                                ],

                                       verbose_name=_('المستوى التعليمي:'))
    specialization = models.CharField(
        max_length=100, choices=SELECT_specialization, verbose_name=_('التخصص:'))
    othar_specialization = models.CharField(
        max_length=100, null=True, blank=True,
        help_text=_("يتم تعبئة هذا الحقل في حال لم يتوفر التخصص في القائمة السابقة"),
        verbose_name=_('تخصص أخر :'))

    rate = models.CharField(max_length=100, verbose_name=_('المعدل:'))
    From_Date = models.DateField(verbose_name=_('من تاريخ:'))
    To_date = models.DateField(verbose_name=_('إلى تاريخ:'))
    uploaded_image = models.FileField(

        validators=[validate_file_extension, file_size],
        upload_to="Image/certificate/%Y/%m/%d/%H/%M/%S",
        blank=True, null=True,
        # verbose_name=_('  الشهادة'),
        verbose_name=_(
            'الشهادة/ pdf or png or jpg or doc or docx  '),
        help_text=_(" نوع الملف pdf او png او jpg او doc او docx فقط والحجم لا يزيد 10 ميجا  ")
    )

    def cv_dispaly(self):
        if self.uploaded_image != None:
            extension = os.path.splitext(self.uploaded_image.name)
            if extension[1] == '.pdf':
                return "<object width=100% height=300px data="+self.uploaded_image.url+"  type=application/pdf></object>"
            elif extension == '.doc':
                return "<object width=100% height=300px data="+self.uploaded_image.url+"  type=application/pdf></object>"
            elif extension[1] == 'png' or extension[1] == '.jpg':
                return '<image width=300px height=300px src='+self.uploaded_image.url+'></image>'
            else:
                return '<image width=300px height=300px src='+self.uploaded_image.url+'></image>'

        else:
            return "<span>  لايوجد شهادة </span>"
    create_at = models.DateField(
        auto_now_add=timezone.now, verbose_name=_('تاريخ الإنشاء:'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="EducationRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    # objects = UserManager()

    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _(" المؤهل ")
        verbose_name_plural = _("الموهلات ")


class LanguageSkill(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name_language = models.CharField(max_length=100,

                                     choices=lang,
                                     verbose_name=_('اللغة'))
    otharـname_language = models.CharField(max_length=100,
                                           help_text=_("يتم تعبئة هذا الحقل في حال لم يتوفر اللغة في القائمة السابقة"),
                                           verbose_name=_('اللغة أخر :'),
                                           null=True,
                                           blank=True
                                           )

    reading = models.CharField(
        max_length=100, choices=SELECT_SKILLS, verbose_name=_('مهارة القراءة'))
    writing = models.CharField(
        max_length=100, choices=SELECT_SKILLS, verbose_name=_('مهارة الكتابة'))
    conversation = models.CharField(
        max_length=100, choices=SELECT_SKILLS, verbose_name=_('مهارة الحديث'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="LanguageSkillRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _("مهاراة اللغة ")
        verbose_name_plural =_( "مهارات اللغة ")


class ComputerSkill(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('المهارة'))
    level = models.CharField(
        max_length=100, choices=SELECT_SKILLS, verbose_name=_('مستوى المهارة'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="ComputerSkillRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name_plural = _("مهارات الحاسوب ")
        verbose_name = _("مهاراة الحاسوب ")


class TrainingCourses(models.Model):
    name_institute = models.CharField(
        max_length=100, verbose_name=_('اسم المؤسسة التعليمية'))
    name_courses = models.CharField(
        max_length=100, verbose_name=_('اسم الدورة التعليمية'))
    country = models.ForeignKey(
        Country,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_('البلد')
    )
    # country = models.CharField(
    #     max_length=100, choices=SELECT_COUNTRY, verbose_name=_('البلد'))
    From_Date = models.DateField(verbose_name=_('تاريخ البداية'))
    To_date = models.DateField(verbose_name=_('تاريخ الانتهاء'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="TrainingCoursesRegister",

                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _(" الدورات التدربية ")
        verbose_name_plural = _("الدورات التدريبية ")


class Experience(models.Model):
    name_word = models.CharField(
        max_length=100, verbose_name=_('اسم الشركة/المؤسسة'))
    From_Date = models.DateField(verbose_name=_('تاريخ البداية'))
    To_date = models.DateField(verbose_name=_('تاريخ الانتهاء'))
    name_shop = models.CharField(
        max_length=100, verbose_name=_('اسم المتجر/المكان'))
    name_owner = models.CharField(
        max_length=100, verbose_name=_('اسم صاحب المحل'))
    address = models.CharField(max_length=100, verbose_name=_('العنوان'))
    mobile = models.IntegerField(verbose_name=_('رقم الهاتف'))
    task = models.TextField(max_length=100000, verbose_name=_('المهام'))
    name_job_start = models.CharField(
        max_length=100, verbose_name=_('المسمى الوظيفة (بداية)'))
    name_job_end = models.CharField(
        max_length=100, verbose_name=_('اسم الوظيفة (نهاية)'))
    salary_start = models.CharField(
        max_length=100, verbose_name=_('الراتب (بداية)'))
    salary_end = models.CharField(
        max_length=100, verbose_name=_('الراتب (نهاية)'))
    working_hours = models.CharField(
        max_length=100, verbose_name=_('ساعات العمل'))
    resson_leaving = models.CharField(
        max_length=100, verbose_name=_('سبب مغادرة الوظيفة'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="ExperienceRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _("الخبرة ")
        verbose_name_plural = _("الخبرات  ")


class Employment(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('اسم المجال'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="EmploymentRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _(" مجال العمل  ")
        verbose_name_plural = _(" مجالات العمل  ")


class BankKonown(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('اسم الشخص'))
    relative = models.CharField(max_length=100, verbose_name=_('صلة القرابة'))
    working = models.CharField(max_length=100, verbose_name=_('جهة العمل'))
    address = models.CharField(max_length=100, verbose_name=_('العنوان'))
    mobile = models.IntegerField(verbose_name=_('رقم الهاتف'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="BankKonownRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    create_at = models.DateField(auto_now_add=now)
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _(" المعرف  ")
        verbose_name_plural = _("  المعرفين  ")


class GeneralData(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    work_bank = models.CharField(
        max_length=5, choices=CHECK_ANSER, default='لا', verbose_name=_('هل تعمل في البنك'))
    receive_email = models.CharField(
        max_length=100, verbose_name=_('هل تريد استقبال بريد إلكتروني من البنك ',))
    file_civil_service = models.CharField(
        max_length=5, choices=CHECK_ANSER, default='لا', verbose_name=_('هل لديك ملف في الخدمة المدنية'))
    spend_working = models.CharField(
        max_length=100, verbose_name=_('كيفية إنفاق راتبك'))
    purchasing_visa = models.CharField(
        max_length=5, choices=CHECK_ANSER, default='لا', verbose_name=_('هل تمتلك تأشيرة للسفر'))
    traveling = models.CharField(
        max_length=3, choices=CHECK_ANSER, default='لا', verbose_name=_('هل تسافر'))
    currently_working = models.CharField(
        max_length=250, verbose_name=_('هل تعمل حاليًا'))
    Current_working_phone = models.IntegerField(
        verbose_name=_('رقم هاتف جهة العمل الحالية'))
    Current_work_address = models.CharField(
        max_length=250, verbose_name=_('عنوان جهة العمل الحالية'))

    currently_studying = models.CharField(
        max_length=3, choices=CHECK_ANSER, default='لا', verbose_name=_('هل تدرس حاليًا'))
    work_night = models.CharField(
        max_length=3, choices=CHECK_ANSER, default='نعم', verbose_name=_('هل تعمل ليلاً'))
    start_working = models.CharField(
        max_length=250, verbose_name=_('تاريخ بدء العمل'))
    lowest_salary = models.IntegerField(
        null=True, blank=True, verbose_name=_('أدنى راتب تقبله'))
    health_problems = models.CharField(
        max_length=250, null=True, help_text=_("معا السبب ان توفر"), blank=True, verbose_name=_('مشاكل صحية'))
    hobbies = models.TextField(verbose_name=_('الهوايات'))
    person_closest = models.CharField(
        max_length=250, verbose_name=_('اسم أقرب شخص'))
    person_closest_Phone = models.CharField(
        max_length=250, verbose_name=_('رقم هاتف الشخص الأقرب'))
    relative_relation = models.CharField(
        max_length=250, verbose_name=_('علاقتك بالشخص الأقرب'))
    person_closest_address = models.CharField(
        max_length=250, verbose_name=_('عنوان الشخص الأقرب'))
    name_village_justice = models.CharField(
        max_length=250, verbose_name=_('اسم قريتك أو مدينتك'))
    village_justice_Telephon = models.IntegerField(
        verbose_name=_('رقم هاتف قائمة العدالة بقريتك أو مدينتك'))
    village_justice_address = models.CharField(
        max_length=250, verbose_name=_('عنوان قائمة العدالة بقريتك أو مدينتك'))
    manage_business = models.CharField(
        max_length=250, verbose_name=_('هل تدير عمل خاص'))
    ready_work = models.CharField(
        max_length=250, help_text=_("معا السبب ان توفر"), verbose_name=_('هل أنت جاهز للعمل'))
    government_job = models.CharField(
        max_length=250, help_text="معا السبب ان توفر", verbose_name=_('هل تفضل وظيفة حكومية'))
    source_financial_income = models.CharField(
        max_length=250, help_text=_("معا السبب ان توفر"), verbose_name=_('مصدر دخلك المالي'))
    proficient_English = models.CharField(
        max_length=250, help_text=_("معا السبب ان توفر"), verbose_name=_('مهارة اللغة الإنجليزية'))
    have_illness = models.CharField(
        max_length=250, help_text=_("معا السبب ان توفر"), verbose_name=_('هل تعاني من أمراض'))
    graduation_certificate = models.CharField(
        max_length=250, help_text=_("معا السبب ان توفر"), verbose_name=_('شهادة التخرج'))
    graduation_certificate_file = models.FileField(

        validators=[validate_file_extension, file_size],
        upload_to="Image/certificate/%Y/%m/%d/%H/%M/%S",
        blank=True, null=True,
        # verbose_name=_('  الشهادة'),
        verbose_name=_(
            'شهادة التخرج ان توفرت/ pdf or png or jpg or doc or docx  '),
        help_text=_(" نوع الملف pdf او png او jpg او doc او docx فقط والحجم لا يزيد 10 ميجا  ")
    )

    def graduation_certificate_dispaly(self):
        if self.graduation_certificate_file:
            extension = os.path.splitext(self.graduation_certificate_file.name)
            if extension[1] == '.pdf':
                return mark_safe(f"<object width=100% height=300px data={self.graduation_certificate_file.url}  type=application/pdf></object>")
            elif extension == '.doc':
                return mark_safe(f"<object width=100% height=300px data={self.graduation_certificate_file.url}  type=application/pdf></object>")
            elif extension[1] == 'png' or extension[1] == '.jpg':
                return mark_safe(f'<image width=300px height=300px src={self.graduation_certificate_file.url}></image>')
            else:
                return mark_safe(f'<image width=300px height=300px src={self.graduation_certificate_file.url}></image>')

        else:
            return mark_safe(f"<span>  لايوجد  </span>")

    def graduation_certificate_dispalyss(self):
        if self.graduation_certificate_file:
            extension = os.path.splitext(self.graduation_certificate_file.name)
            if extension[1] == '.pdf':
                return mark_safe(f"<object width=100% height=300px data={self.graduation_certificate_file.url}  type=application/pdf></object>")
            elif extension == '.doc':
                return mark_safe(f"<object width=100% height=300px data={self.graduation_certificate_file.url}  type=application/pdf></object>")
            elif extension[1] == 'png' or extension[1] == '.jpg':
                return mark_safe(f'<image width=300px height=300px src={self.graduation_certificate_file.url}></image>')
            else:
                return mark_safe(f'<image width=300px height=300px src={self.graduation_certificate_file.url}></image>')

        else:
            return mark_safe(f"<span>  لايوجد شهادة </span>")

    create_at = models.DateField(
        auto_now_add=now, verbose_name=_('تاريخ الإنشاء'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             related_name="GeneralDataRegister",
                             null=True, blank=True, verbose_name=_('المستخدم'))
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = _(" البيانات العامة  ")
        verbose_name_plural = _(" البيانات العامة  ")


class BirthData(models.Model):
    cookie = models.TextField(max_length=10000000, editable=False, null=True, blank=True)
    cookie = models.TextField(max_length=10000000, editable=False, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name=_('المستخدم'))
    objects = UserManager()
    
    country = models.ForeignKey(
        Country,null=True,on_delete=models.SET_NULL, verbose_name=_("الدولة"),help_text=_("اختار دولة"),
        # related_name="countr_RequestToOpenAccount",
        # blank=True,  
    )

    region = models.ForeignKey(
        Region,  null=True, on_delete=models.SET_NULL,
       verbose_name=_("المحافظة"),  help_text=_("اختار المحافظة"),
        # related_name="countr_RequestToOpenAccount",
    )
    directorate = models.ForeignKey(
        Directorate, null=True,on_delete=models.SET_NULL,
        blank=True,verbose_name=_("المديرية"),help_text=_("اختار المديرية"),
        # related_name="countr_RequestToOpenAccount",
        # blank=True,
    )
    isolation = models.ForeignKey( Isolation, null=True, blank=True,
        on_delete=models.SET_NULL,verbose_name=_("العزلة"),help_text=_("اختار العزلة"),
        # related_name="countr_RequestToOpenAccount",
        # blank=True,
    )

    class Meta:
        managed = True
        verbose_name = _("طلب فتح حساب - بيانات الميلاد ")
        verbose_name_plural = _("طلب فتح حساب - بيانات الميلاد ")


class AddressLocation(models.Model):
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             null=True, blank=True, verbose_name=_('المستخدم'))
    # objects = UserManager()

    objects = UserManager()
    country_address = models.ForeignKey(
        Country,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_("الدولة")
    )
    cookie = models.TextField(
        max_length=10000000, editable=False, null=True, blank=True)
    region_address = models.ForeignKey(
        Region,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("المحافظة")
    )
    directorate_address = models.ForeignKey(
        Directorate,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("المديرية")
    )
    isolation_address = models.ForeignKey(
        Isolation,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("العزلة")
    )
    street = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("الشارع")
    )
    nearest_branch = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("اقرب فرع لبنك الإنماء من محل اقامتك")
    )
    nearest_outstanding_landmark = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("اقرب معلم بارز من محل اقامتك")
    )
    accommodation_type = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("نوع السكن")
    )

    class Meta:
        managed = True
        verbose_name = _("طلب فتح حساب - بيانات العنوان ")
        verbose_name_plural = _("طلب فتح حساب - بيانات العنوان ")


class IdentificationCard (models.Model):
    cookie = models.TextField(
        max_length=10000000, default=" ", null=True, blank=True)
    # user = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('المستخدم'))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             null=True, blank=True, verbose_name=_('المستخدم'))
    # objects = UserManager()

    objects = UserManager()
    full_name = models.CharField(
        max_length=250, null=True,
        verbose_name=_("الاسم الرباعي حسب البطاقة الشخصية")
    )
    birth_date = models.DateField(
        # BirthData,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        # on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_("تاريخ الميلاد")
    )
    id_number = models.PositiveBigIntegerField(
        # BirthData,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        # on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_("رقم الهوية الشخصية")
    )
    birth_date = models.DateField(
        # BirthData,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        # on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("تاريخ الميلاد")
    )
    id_issuance_date = models.DateField(
        # BirthData,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        # on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("تاريخ اصدار الهوية")
    )
    id_expiry_date = models.DateField(
        # BirthData,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        # on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("تاريخ انتهاء الهوية")
    )
    image_front = models.ImageField(
        max_length=250, null=True,
        upload_to="Image/IdentificationCard/%Y/%m/%d/%H/%M/%S",

        verbose_name=_("صورة البطاقة الآمامية")
    )
    image_back = models.ImageField(
        max_length=250, null=True,
        upload_to="Image/IdentificationCard/%Y/%m/%d/%H/%M/%S",

        verbose_name=_("صورة البطاقة الخلفية")
    )
    gender = models.CharField(
        max_length=20,
        null=True,
        choices=SELECT_GERDER,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("الجنس")
    )
    nationality_amrican = models.BooleanField(
        # max_length=20,

        help_text=_("هل لديك الجنسية الامريكية"),
        # null=True,
        # choices=[('male', "ذكر"), ("faimle", "انثى"),],
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("هل لديك الجنسية الامريكية"),
        choices=[(False, "لا"), (True, "نعم"),],
        serialize=False,

        default=False
    )
    have_nationality = models.BooleanField(
        # max_length=20,

        # help_text="هل لديك جنسية اخرى ؟",
        # null=True,
        # choices=[('male', "ذكر"), ("faimle", "انثى"),],
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("هل لديك جنسية اخرى ؟"),
        choices=[(False, "لا"), (True, "نعم"),],
        # serialize=False,

        # default=False
    )
    nationality = models.CharField(
        max_length=200,
        null=True,
        #   blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("الجنسية")
    )
    # nationality = models.ForeignKey(
    #     Country,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     # blank=True,
    #     verbose_name="الجنسية"
    # )
    nationality_othar = models.CharField(
        max_length=200,
        null=True,
        blank=True,

        # blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("جنسية اخرى")
    )
    # nationality_othar = models.ForeignKey(
    #     Country,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     # blank=True,
    #     verbose_name="الجنسية الاخرى"
    # )
    maritalـstatus = models.CharField(
        max_length=20,
        null=True,
        choices=[('bachelor', "اعزب"), ("married", "متزوج"),
                 ("divorced", "مطلق"), ("widow", "ارمل")],
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("الحالة الاجتماعية")
    )
    educational_level = models.CharField(
        max_length=20,
        null=True,
        choices=[('primary', "ابتدئي"), ("general secondary", "ثنوية عامة"),
                 ("diploma", "دبلوم"),
                 ("higher_diploma", "دبلوم عالي"),
                 ("bachelor", "بكالوريوس"),
                 ("master", "ماجستير"),
                 ("doctor", "دكتورة"),
                 # ("widow", "بروفيسور")   ,

                 ],
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("المستوى التعلمي")
    )
    specialization = models.CharField(
        max_length=100,
        null=True,
        choices=SELECT_specialization,

        verbose_name=_("التخصص")
    )
    othar_specialization = models.CharField(
        max_length=100, null=True, blank=True,
        help_text=("يتم تعبئة هذا الحقل في حال لم يتوفر التخصص في القائمة السابقة"),
        verbose_name=_('تخصص أخر :'))
    name_language = models.CharField(max_length=100,

                                     choices=lang,
                                     verbose_name=_('اللغة'))
    otharـname_language = models.CharField(max_length=100,
                                           help_text=_("يتم تعبئة هذا الحقل في حال لم يتوفر اللغة في القائمة السابقة"),
                                           verbose_name=_('اللغة أخر :'),
                                           null=True,
                                           blank=True
                                           )

    class Meta:
        managed = True
        verbose_name = _("طلب فتح حساب - بيانات البطاقة الشخصية ")
        verbose_name_plural = _("طلب فتح حساب - بيانات البطاقة الشخصية ")

from django.utils.translation import gettext_lazy as _
class RequestToOpenAccount(models.Model):

    # contry =
    # Phone_Number = models.CharField(
    #     max_length=250, null=True,
    #     verbose_name="رقم التلفون",

    # )
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,
                             null=True, blank=True, verbose_name=_('المستخدم'))
    # objects = UserManager()

    objects = UserManager()
    # birth_data = models.ForeignKey(
    #     BirthData,
    #     null=True,
    #     # related_name="countr_RequestToOpenAccount",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="تاريخ الميلاد"
    # )
    # address_location = models.ForeignKey(
    #     AddressLocation,
    #     null=True,
    #     # related_name="countr_RequestToOpenAccount",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="تاريخ الميلاد"
    # )
    # id_card = models.ForeignKey(
    #     IdentificationCard,
    #     null=True,
    #     # related_name="countr_RequestToOpenAccount",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="بيانات الهوية الشخصية"
    # )

    country = models.ForeignKey(
        Country,
        null=True,
        # related_name="countr_RequestToOpenAccount",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("الدولة")
    )
    phone_whatsapp = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name=_("رقم تلفون الواتساب")
    )
    Phone_Number = PhoneNumberField(
        null=True,
        verbose_name=_("رقم التلفون")
    )
    emile = models.EmailField(
        null=True, blank=True,
        verbose_name=_("البريد الألكتروني"),

    )

    # service_application = models.ForeignKey(
    #     BankApplications,
    #     null=True,
    #     related_name="service_application_requests",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="خدمات التطبيقات"
    # )
    # service = models.ForeignKey(Services, blank=True,
    #                             related_name="service_requests",

    #                             null=True, on_delete=models.SET_NULL, verbose_name=" الخدمة")
    cookie = models.TextField(
       default=" ", null=True, blank=True)
    note = models.TextField(
        null=True, blank=True, verbose_name=_("ادخل ملاحظة"))
    # image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    gender = models.CharField(
        choices=SELECT_GERDER, max_length=10, default='ather', verbose_name=_('الجنس'))

    def __str__(self):
        return self.note

    class Meta:
        managed = True
        verbose_name = _("طلب فتح حساب - بيانات عامة")
        verbose_name_plural = _("طلب فتح حساب - بيانات عامة")
