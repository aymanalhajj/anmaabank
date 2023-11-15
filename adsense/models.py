from django.db import models
from anmaabankApp.models import *
from servicesapp.models import Services, BankApplications
# Create your models here.


class AdsenceHeder(models.Model):
    Tital_AR = models.CharField(
        max_length=300,     null=True,
        blank=True, verbose_name="العنوان بالعربي"
    )
    Tital_EN = models.CharField(
        max_length=300,     null=True,
        blank=True,  verbose_name="العنوان بالانجليزي"
    )

    Description_AR = models.CharField(
        max_length=1000,     null=True,
        blank=True,  verbose_name=" الوصف بالعربي "
    )
    Description_EN = models.CharField(
        null=True,
        blank=True,  max_length=1000, verbose_name=" الوصف بالانجليزي "
    )
    image = models.ImageField(
        null=True,
        # blank=True,

        upload_to="Image/Adsence/AdsenceHeder/%Y/%m/%d/%H/%M/%S",
        verbose_name="صورة الاعلان"
    )

    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name="تاريخ الأضافة ")
    Date_Finish_Posted = models.DateTimeField(
        null=True, blank=True,
        verbose_name="تاريخ أنتهاء النشر ")

    Price = models.FloatField(
        default=0.0,
    )
    service = models.ForeignKey(
        Services,
        null=True,
        related_name="service_ads_header",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="الخدمات"
    )
    service_application = models.ForeignKey(
        BankApplications,
        null=True,
        related_name="service_application_ads_header",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="خدمات التطبيقات"
    )
    # daily_flight_schedule = models.ForeignKey(
    #     DailyFlightSchedule,
    #     null=True,
    #     related_name="comercialActivieAdsenceHeder",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="النشاط التجاري"
    # )
    url_ads = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="الرابط"
    )

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "الأعلان في الصفحة الرئيسية "
        verbose_name_plural = "صور إعلان متحرك في الصفحة الرئيسية "
        # verbose_name_plural = "الأعلانات في الاسف "


class AdsenceFooter(models.Model):
    Tital_AR = models.CharField(
        max_length=300,     null=True,
        blank=True,  verbose_name="العنوان بالعربي"
    )
    Tital_EN = models.CharField(
        max_length=300,     null=True,
        blank=True,  verbose_name="العنوان بالانجليزي"
    )

    Description_AR = models.CharField(
        max_length=1000, null=True, verbose_name="  الوصف عربي"
    )
    Description_EN = models.CharField(
        max_length=1000,     null=True,
        blank=True,
        verbose_name="  الوصف انجليزي"
    )
    image = models.ImageField(
        # blank=True,
        null=True,
        upload_to="Image/Adsence/AdsenceHeder/%Y/%m/%d/%H/%M/%S",
        verbose_name="صورة الاعلان"
    )

    service = models.ForeignKey(
        Services,
        null=True,
        related_name="services_footer",
        on_delete=models.SET_NULL,
        # blank=True,
        verbose_name="الخدمات"
    )
    service_application = models.ForeignKey(
        BankApplications,
        null=True,
        related_name="service_application_ads_footer",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="خدمات التطبيقات"
    )

    # type_comercial_activies_primary = models.ForeignKey(
    #     Airline,
    #     null=True,
    #     related_name="AirlineAdsenceFooter",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="نوع النشاط التجاري الاساسي"
    # )
    # daily_flight_schedule = models.ForeignKey(
    #     DailyFlightSchedule,
    #     null=True,
    #     related_name="comercialActivieAdsenceFooter",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="النشاط التجاري"
    # )
    url_ads = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="الرابط"
    )

    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name="تاريخ الأضافة ")
    Date_Finish_Posted = models.DateTimeField(
        null=True, blank=True,
        verbose_name="تاريخ أنتهاء النشر ")

    Price = models.FloatField(
        default=0.0,
    )

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "الأعلان في الاسف "
        verbose_name_plural = "الأعلانات في الاسف "


class Adsence(models.Model):
    Tital_AR = models.CharField(
        max_length=300,     null=True,
        blank=True,  verbose_name="العنوان بالعربي"
    )
    Tital_EN = models.CharField(
        max_length=300,     null=True,
        blank=True,  verbose_name="العنوان بالانجليزي"
    )

    Description_AR = models.CharField(
        max_length=1000, null=True, verbose_name="  الوصف عربي"
    )
    Description_EN = models.CharField(
        max_length=1000,     null=True,
        blank=True,
        verbose_name="  الوصف انجليزي"
    )

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )

    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل ")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الأضافة ")
    # Date_Finish_Posted = models.DateTimeField(
    #     null = True, blank=True,auto_now=True,
    #     verbose_name="تاريخ أنتهاء النشر ")
    image = models.ImageField(
        upload_to="Image/Adsence/%Y/%m/%d/%H/%M/%S",
    )
    Price = models.FloatField(
        default=0.0,
    )
    service = models.ForeignKey(
        Services,
        null=True,
        related_name="serviceAdsence",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="المنتج"
    )
    # daily_flight_schedule = models.ForeignKey(
    #     DailyFlightSchedule,
    #     null=True,
    #     related_name="comercialActivieAdsence",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name="النشاط التجاري"
    # )
    url_ads = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="الرابط"
    )

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "الأعلانات "
        verbose_name_plural = " الأعلانات "


class ViewAdcence(models.Model):
    IMEI_device = models.CharField(
        max_length=30, null=True, verbose_name="رقم معرف الجوال"
    )

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الاضافة")
    adsence = models.ForeignKey(
        Adsence, on_delete=models.SET_NULL, null=True, verbose_name="الاعلانات"
    )
    user = models.ForeignKey(RequestHederInfo,
                             related_name="userViewAdcence",
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)

    # device = models.ForeignKey(Device,
    #  on_delete=models.SET_NULL,
    #  related_name="device_login",

    #  blank=True, null=True)
    ipInfo = models.ForeignKey(
        IpInfo, on_delete=models.SET_NULL,
        related_name="ipInfoViewAdcence",

        blank=True, null=True)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "مشاهدات الاعلانات"
        verbose_name_plural = "مشاهدات الاعلانات"


class ViewAdsenceFooter(models.Model):

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الاضافة")
    adsencefooter = models.ForeignKey(
        AdsenceFooter, on_delete=models.SET_NULL,
        null=True, verbose_name="الاعلانات في الأسفل"
    )
    user = models.ForeignKey(RequestHederInfo,
                             related_name="userViewAdsenceFooter",
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)

    # device = models.ForeignKey(Device,
    #  on_delete=models.SET_NULL,
    #  related_name="device_login",

    #  blank=True, null=True)
    ipInfo = models.ForeignKey(
        IpInfo, on_delete=models.SET_NULL,
        related_name="ipInfoViewAdsenceFooter",

        blank=True, null=True)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "مشاهدات الاعلانات في الاسفل"
        verbose_name_plural = "مشاهدات الاعلانات في الاسفل"


class PressAdsenceFooter(models.Model):

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الاضافة")
    adsencefooter = models.ForeignKey(
        AdsenceFooter, on_delete=models.SET_NULL,
        null=True, verbose_name="الاعلانات في الأسفل"
    )

    # device = models.ForeignKey(Device,
    #  on_delete=models.SET_NULL,
    #  related_name="device_login",

    #  blank=True, null=True)
    ipInfo = models.ForeignKey(
        IpInfo, on_delete=models.SET_NULL,
        related_name="ipInfoPressAdsenceFooter",

        blank=True, null=True)

    url_ads = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="الرابط"
    )

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "الضغط على الاعلانات في الاسفل"
        verbose_name_plural = "الضغط على الاعلانات في الاسفل"


class ViewAdsenceHeader(models.Model):

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الاضافة")
    viewAdsenceHeader = models.ForeignKey(
        AdsenceHeder, on_delete=models.SET_NULL,
        null=True, verbose_name="الاعلانات في الاعلى"
    )

    # device = models.ForeignKey(Device,
    #  on_delete=models.SET_NULL,
    #  related_name="device_login",

    #  blank=True, null=True)

    ipInfo = models.ForeignKey(
        IpInfo, on_delete=models.SET_NULL,
        related_name="ipInfoViewAdsenceHeader",

        blank=True, null=True)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "مشاهدات الاعلانات في الأعلى"
        verbose_name_plural = "مشاهدات الاعلانات في الاعلى"


class PressAdsenceHeder(models.Model):

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, verbose_name="تاريخ التعديل")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, verbose_name="تاريخ الاضافة")
    adsenceheder = models.ForeignKey(
        AdsenceHeder, on_delete=models.SET_NULL,
        null=True, verbose_name="الاعلانات في الاعلى"
    )

    # users = models.ForeignKey(Users,
    #                           related_name="user_id",

    # device = models.ForeignKey(Device,
    #  on_delete=models.SET_NULL,
    #  related_name="device_login",

    #  blank=True, null=True)
    ipInfo = models.ForeignKey(
        IpInfo, on_delete=models.SET_NULL,
        related_name="ipInfoPressAdsenceHeder",

        blank=True, null=True)

    url_ads = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="الرابط"
    )

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "الضغط على الاعلانات في الاعلى"
        verbose_name_plural = "الضغط على الاعلانات في الاعلى"
