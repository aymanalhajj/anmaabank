from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.shortcuts import reverse
from django.core.exceptions import ValidationError

from country_regions.models import Country
from branches.models import validate_hostname
from django.utils import timezone
# from navbarapp.models import Navbars,SecondaryNavbars,ColumnNavbars


class CategoriesServices(models.Model):

    name = models.CharField(max_length=20, null=True,verbose_name="اسم نوع الخدمة", unique=True)
    name_en = models.CharField(max_length=20, null=True,verbose_name="Service Type Name", unique=True)
    description = models.CharField(max_length=100, verbose_name=_("وصف مختصر جملة واحده فقط"), null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, blank=True, editable=False,related_name="created_by_category_services",
            null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    is_deleted = models.BooleanField(default=False,
        help_text=_("سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  "),
        verbose_name=_("محذوف ")
    )
    is_hidden = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  "),
        verbose_name=_("مخفي ")
    )
    date_update = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name=_("تاريخ التعديل "))
    date_added = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name=_("تاريخ الأضافة "))
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #                                null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name=_("تاريخ الأنشاء "))

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='category_services_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='category_services_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='category_services_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )

    # sort_no = models.IntegerField(
    #     null=True, editable=True, blank=True, verbose_name="رقم الترتيب ",
    #     help_text=" اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد"
    # )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        # if self.sort_no is None:
        #     self.sort_no = self.id
        # else:
        # self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # def hard_delete(self):
    #     super(SoftDeleteModel, self).delete()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = _("نوع الخدمة")
        verbose_name_plural = _("نوع الخدمة")


class Services(models.Model):
    titel = models.CharField(
        max_length=100, verbose_name=_("العنوان")
    )
    titel_en = models.CharField(max_length=100, verbose_name="Service Title")
    
    category_services = models.ForeignKey(
        CategoriesServices,
        null=True,
        related_name="category_services",
        on_delete=models.SET_NULL,
        # blank=True,
        verbose_name=_("نوع الخدمة"),
        help_text=_("مثال : خدمات الشركات او خدمات الأفراد او خدمات المنظمات")
    )
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")

    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )
    # type_services = models.CharField(
    #     max_length=100,
    #     choices=(
    #             ("1", 'خدمات الأفراد'),
    #             ("2", 'خدمات المنظمات'),
    #             ("3", 'خدمات الشركات'),
    #         # ("4", 'تطبيقات البنك'),

    #         # ("5", 'التمويل الأصغر '),
    #         # ("6", 'الاقسام'),
    #         # ("none", ''),
    #         # ("none", ''),
    #         # ("none", ''),
    #         # ("none", ''),
    #         # ("none", ''),
    #         # ("none", ''),
    #         # ("none", ''),

    #     ),
    #     # default="الرئيسية",
    #     null=True,
    #     verbose_name="نوع الخدمة",
    #     # blank=True
    # )

    short_detial = models.CharField(
        max_length=100, null=True, verbose_name=_("وصف مختصر جملة واحده فقط")
    )
    detial_ar = HTMLField(
        max_length=100000, default=" ", null=True, verbose_name=_("التفاصيل"))

    name_action = models.CharField(
        max_length=250, verbose_name=_("اسم الحدث (النقرة)"),
        null=True,
        blank=True,

        help_text=_("عنوان البوتون المراد النقر  فيها مثال : احجز الان او استفسر اكثر")
    )
    
    booking_link = models.URLField(
        null=True, blank=True,
        verbose_name=_("رابط الحجز او استفسار عن الخدمة (اختياري)")
    )
    phone_whatsapp = models.CharField(
        max_length=20,
        null=True, blank=True,
        help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp  with out +",
        verbose_name=_("رقم تلفون الواتساب للحجز او استفسار عن الخدمة (اختياري)")
    )
    phone = PhoneNumberField(
        null=True, blank=True,
        verbose_name=_("رقم تلفون اتصال للحجز او استفسار عن الخدمة (اختياري)")
    )

    image = models.ImageField(
        upload_to="Image/Service/%Y/%m/%d/", verbose_name=_(" إختيار صورة"), null=True,
    )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    # : marshal(question, questionlist_fields)}

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('service-single',  kwargs={'id': self.pk})

    # def get_absolute_url(self):
        # return reverse('name-of-some-view', kwargs={'para': 'meters'})
    def __str__(self):
        return self.titel

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   related_name="created_by_services",
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )
    is_hidden = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  "),
        verbose_name=_("مخفي ")
    )
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #                                null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name=_("تاريخ الأنشاء "))

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='services_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='services_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='services_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )

    # sort_no = models.IntegerField(
    #     null=True, editable=True, blank=True, verbose_name="رقم الترتيب ",
    #     help_text=" اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد"
    # )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        # if self.sort_no is None:
        #     self.sort_no = self.id
        # else:
        # self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # def hard_delete(self):
    #     super(SoftDeleteModel, self).delete()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    class Meta:
        managed = True
        verbose_name = _("الخدمة")
        verbose_name_plural =_( "الخدمات")


desketop = 'desketop'
mobile = 'mobile'
website = 'website'

TYPE_CHOICES = (
    (desketop, 'تطبيق سطح المكتب'),
    (mobile, 'تطبيق جوال'),
    (website, 'موقع الكتروني ')
)


class ImagesServices(models.Model):
    image = models.ImageField(
        # upload_to=portfolio_file_name,

        upload_to="Image/ImagesServices/%Y/%m/%d/",
        verbose_name=_(" إختيار صورة"), null=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
    )
    date_update = models.DateTimeField(
        auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
    )
    service = models.ForeignKey(
        Services, on_delete=models.SET_NULL, null=True, verbose_name=_(" الخدمة"))

    class Meta:
        verbose_name = _("صور خدمات البنك  ")
        verbose_name_plural = _("صور خدمات البنك")

    def __str__(self):
        return "this image {0}  {1} for service    {2}   ".format(
            self.id,  self.image, self.service.titel
        )


class BankApplications(models.Model):
    titel = models.CharField(
        max_length=50, verbose_name=_("اسم التطبيق")
    )
    titel_en = models.CharField(
        max_length=50, verbose_name=_("اسم التطبيق انجليزي")
    )
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")

    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )
    detial_ar = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("اسم التطبيق")
    )
    detial_en = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("اسم التطبيق انجليزي")
    )
    # detial_ar = HTMLField(
    #  null=True,blank=True, verbose_name="تفاصيل التطبيق")
    logo_image = models.ImageField(
        upload_to="Image/BankApplications/Logo/%Y/%m/%d/",
        verbose_name=_(" ايقون شعار التطبيق صورة مصغر "), null=True,
    )
    screen_image = models.ImageField(
        upload_to="Image/BankApplications/Screen/%Y/%m/%d/",
        verbose_name=_(" صورة شاشة التطبيق"), null=True,
    )
    barcode_image = models.ImageField(
        upload_to="Image/BankApplications/Barcode/%Y/%m/%d/",
        verbose_name=_(" صورة باركود تحميل التطبيق"), null=True,
    )
    # balance = MoneyField(max_digits=14, blank=True,
    #  null=True, decimal_places=2, default_currency=usd,
    #  verbose_name="سعر الخدمة يبتداء من"
    #  )

    created_by = models.ForeignKey(User,
                                   blank=True,
                                   editable=False,
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة ")
                                   )
    # price_net_amount = models.DecimalField(max_digits=9, decimal_places=2, default="5",
    #                                        verbose_name="سعر الخدمة يبتداء من")
    type_choice = models.CharField(
        max_length=8,
        choices=TYPE_CHOICES,
        # default=usd,
        null=True,
        verbose_name=_("نوع التطبيق"),
        # blank=True
    )

    # price = models.DecimalField(
    #     max_digits=9, decimal_places=2, default="5",
    #     verbose_name="سعر الخدمة يبتداء من")
    google_play = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name=_("رابط تطبيق على جوجل ابلاي "),
        help_text="https://play.google.com",
        validators=[validate_hostname('google.com', 'play.google.com')]
    )
    app_store = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name=_("رابط تطبيق على اب استور "),
        help_text="https://apps.apple.com",
        validators=[validate_hostname('apps.apple.com', 'apple.com')]
    )
    desketop = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name=_("رابط تطبيق تحميل desketop"),
        help_text="https://play.google.com",
        validators=[validate_hostname('google.com', 'play.google.com')]
    )
    website = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name=_("رابط website"),
        help_text="http://alinmabank.com",
        # validators=[validate_hostname('play.google.com/', 'play.google.com')]
    )
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.titel
    is_deleted = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا التطبيق من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  "),
        verbose_name=_("محذوف ")
    )
    is_hidden = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  "),
        verbose_name=_("مخفي ")
    )
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #                                null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name=_("تاريخ الأنشاء "))

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='bank_applications_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='bank_applications_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='bank_applications_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )

    # sort_no = models.IntegerField(
    #     null=True, editable=True, blank=True, verbose_name="رقم الترتيب ",
    #     help_text=" اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد"
    # )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        # if self.sort_no is None:
        #     self.sort_no = self.id
        # else:
        # self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # def hard_delete(self):
    #     super(SoftDeleteModel, self).delete()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def clean(self):
        """
        In here you can validate the two fields
        raise ValidationError if you see anything goes wrong. 
        for example if you want to make sure that field1 != field2
        """
        type_choice = self.type_choice
        google_play = self.google_play
        app_store = self.app_store
        website_url = self.website
        desketop_url = self.desketop
        errors = {}
        if type_choice == mobile:
            if (google_play is None or google_play is '') and (app_store is None or app_store is ''):
                errors["google_play"] = "الرجاء ادخال رابط التطبيق على Google Play"
                errors["app_store"] = "الرجاء ادخال رابط التطبيق على app Store"

            # if :
        elif type_choice == website:
            if website_url is None or website_url is '':
                errors["website"] = "الرجاء ادخال رابط الموقع  الالكتروني"
        elif type_choice == desketop:
            if desketop_url is None or desketop_url is '':
                errors["desketop"] = "الرجاء ادخال رابط تحميل تطبيق سطح المكتب "
            # if app_store is None or app_store is '':
            #     errors["app_store"]= "الرجاء ادخال رابط التطبيق على app Store"
        # return self.cleaned_data
        if errors:
            raise ValidationError(errors)

    class Meta:
        managed = True
        verbose_name = _("تطبيقات البنك")
        verbose_name_plural = _("تطبيقات البنك")

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('application-single',  kwargs={'id': self.pk})


class FutureApplications(models.Model):

    name = models.CharField(
        null=True, max_length=30, verbose_name=_("اسم الميزة")
    )
    name_en = models.CharField(
        null=True, max_length=30, verbose_name=_("اسم الميزة انجليزي")
    )
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
    )
    date_update = models.DateTimeField(
        auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
    )
    applications = models.ForeignKey(
        BankApplications, on_delete=models.SET_NULL, related_name="future_applications",
        null=True, verbose_name=_("التطبيق"))

    class Meta:
        verbose_name = _("مميزات التطبيق")
        verbose_name_plural = _("مميزات التطبيق")

    def __str__(self):
        return self.name


class ServiceRequests(models.Model):

    # contry =
    # Phone_Number = models.CharField(
    #     max_length=250, null=True,
    #     verbose_name="رقم التلفون",

    # )
    country = models.ForeignKey(
        Country,
        null=True,
        related_name="countr_ServiceRequests",
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
        verbose_name=_("رقم التلفون ")
    )
    emile = models.EmailField(
        null=True, blank=True,
        verbose_name=_("  البريد الألكتروني"),

    )
    name = models.CharField(
        max_length=250, null=True,
        verbose_name=_("إسمك")
    )
    service_application = models.ForeignKey(
        BankApplications,
        null=True,
        related_name="service_application_requests",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name=_("خدمات التطبيقات")
    )
    service = models.ForeignKey(Services, blank=True,
                                related_name="service_requests",

                                null=True, on_delete=models.SET_NULL, verbose_name=_(" الخدمة"))
    cookie = HTMLField(
        max_length=100000, default=" ", null=True, blank=True)
    Message = HTMLField(
        max_length=1000, null=True, verbose_name=_("الرساله"))
    # image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.Message

    class Meta:
        managed = True
        verbose_name = _(" حجوزات الخدمات ")
        verbose_name_plural = _("حجوزات الخدمات  ")
