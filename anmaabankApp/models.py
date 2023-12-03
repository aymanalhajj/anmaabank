from distutils.command.upload import upload
import numbers
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
import datetime
from tinymce.models import HTMLField
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

# from djmoney.models.fields import MoneyField

# Create your models here.


class Statistics(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name=_("الرقم")
    )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))

    titel = models.CharField(
        max_length=20, null=True, verbose_name=_("العنوان"))

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.titel

    class Meta:
        managed = True
        verbose_name = _("نقاط تواجدنا")
        verbose_name_plural = _("نقاط تواجدنا")

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('index-section',  kwargs={'tag': "counts"})


# class OurVision(models.Model):
#     # titel = models.CharField(
#     # max_length=250, verbose_name=_("العنوان")
#     # )
#     created_by = models.ForeignKey(User, blank=True, editable=False,
#                                    null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))

#     detial_ar = HTMLField(
#         max_length=100000, default=" ", null=True, blank=True, verbose_name="تفاصيل رؤية الشركة")

#     # image = models.ImageField(
#     # upload_to="Image/About/%Y/%m/%d/", blank=True, verbose_name=_(" إختيار صورة"), null=True,
#     # verbose_name=_(" إختيار صورة")
#     # )
#     Date_Update = models.DateTimeField(
#         auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

#     def __str__(self):
#         return self.detial_ar

#     class Meta:
#         managed = True
#         verbose_name = "رؤيتنا"
#         verbose_name_plural = "رؤيتنا"


class IpInfo(models.Model):
    status = models.CharField(
        max_length=50, null=True, verbose_name="status", blank=True, editable=False
    )
    cookie = HTMLField(
        max_length=100000, default=" ", null=True, blank=True, editable=False)
    COOKIES = HTMLField(
        max_length=100000, default=" ", null=True, blank=True, editable=False)
    ip = models.CharField(
        max_length=50,  verbose_name=" Ip", null=True, blank=True, editable=False
    )
    country = models.CharField(
        max_length=50,  null=True, verbose_name=" الدولة", blank=True, editable=False
    )
    screen = models.CharField(
        max_length=50,  null=True, verbose_name=" الشاشة ", blank=True, editable=False
    )
    countryCode = models.CharField(
        max_length=50,  null=True, verbose_name=" رمز الدولة", blank=True, editable=False
    )
    timezone = models.CharField(
        max_length=50,  null=True, verbose_name="timezone", blank=True, editable=False
    )
    city = models.CharField(
        max_length=50, null=True,  verbose_name=" المدينة ", blank=True, editable=False
    )
    regionCode = models.CharField(
        max_length=100,  null=True, verbose_name=" رمز المنطقة ", blank=True, editable=False
    )

    regionName = models.CharField(
        max_length=100,  null=True, verbose_name=" اسم المنطقة ", blank=True, editable=False
    )

    isp = models.CharField(
        max_length=100, null=True,  verbose_name=" مزود خدمة الإنترنت ISP  Internet service provider ", blank=True, editable=False
    )

    org = models.CharField(
        max_length=200, null=True, verbose_name=" منظمة org ", blank=True, editable=False
    )

    asn = models.CharField(
        max_length=200, null=True, default="", verbose_name=" أرقام النظام الذاتي Autonomous System Numbers ", blank=True, editable=False
    )
    zip = models.CharField(
        max_length=20, null=True, default="", verbose_name=" أرقام النظام الذاتي Autonomous System Numbers ", blank=True, editable=False
    )
    latitude = models.FloatField(
        verbose_name=" latitude خط العرض", null=True, blank=True, editable=False)
    longitude = models.FloatField(
        verbose_name=" longitude خط الطول", null=True, blank=True, editable=False)
    #    https://www.google.com/maps?q=24.197611,120.780512
    url_google_map_location = models.URLField(
        # max_length=20,
        null=True, default="https://www.google.com/maps?q=15.3538569,44.2058841",
        verbose_name=" رابط الموقع النقريبي للمستخدم على خرائط جوجل ", blank=True, editable=False
    )
    security_is_bogon = models.BooleanField(
        null=True, default=False, verbose_name=" security is bogon ", blank=True, editable=False
    )

    security_is_cloud_provider = models.BooleanField(
        null=True, default=False, verbose_name="الأمن هو مزود السحابة security is cloud provider ", blank=True, editable=False
    )

    security_is_tor_exit = models.BooleanField(
        null=True, default=False, verbose_name="security is tor exit", blank=True, editable=False
    )

    security_is_tor = models.BooleanField(
        null=True, default=False, verbose_name="  security is tor", blank=True, editable=False
    )

    security_is_proxy = models.BooleanField(
        null=True, default=False, verbose_name=" security_is_proxy ", blank=True, editable=False
    )

    security_is_abuser = models.BooleanField(
        null=True, default=False, verbose_name=" security_is_abuser امان الشبكة مسيء", blank=True, editable=False
    )
    security_is_anonymous = models.BooleanField(
        null=True, default=False, verbose_name="الشبكة مجهولة ", blank=True, editable=False
    )

    security_is_attacker = models.BooleanField(
        null=True, default=False, verbose_name=" مهاجم", blank=True, editable=False
    )

    security_is_threat = models.BooleanField(
        null=True, default=False, verbose_name="تهديد ", blank=True, editable=False
    )

    IMEI_device = models.CharField(
        max_length=30, verbose_name=" معرف الجهاز", null=True, blank=True, editable=False
    )

    Date_Update = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name=_("تاريخ التعديل "), editable=False)
    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_("تاريخ الأضافة "), editable=False)
    # netowrkinfo = models.ForeignKey(
    #     NetowrkInfo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        managed = True
        verbose_name = _("معلومات IP")
        verbose_name_plural = _("معلومات IP")


class RequestHederInfo(models.Model):
    datajson = models.JSONField()
    cookie = HTMLField(
        max_length=100000, default=" ", null=True, )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    latitude = models.FloatField(
        default=0.0, null=True, verbose_name=" latitude خط العرض")
    longitude = models.FloatField(
        verbose_name=" longitude خط الطول", default=0.0, null=True)
    cookie = HTMLField(
        max_length=100000, default=" ", null=True, )
    ip_info = models.ForeignKey(IpInfo, blank=True, editable=False,
                                null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('Date_Update',)
        managed = True
        verbose_name = _("معلومات ريكوست الهيدر")
        verbose_name_plural = _("معلومات ريكوست الهيدر")


class RequestMetaAndGet(models.Model):
    datajson = models.JSONField()
    datajsonGet = models.JSONField(null=True, blank=True,)
    cookie = HTMLField(
        max_length=100000, default=" ", null=True, )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    # latitude = models.FloatField(
    # default=0.0, null=True, verbose_name=" latitude خط العرض")
    # longitude = models.FloatField(
    # verbose_name=" longitude خط الطول", default=0.0, null=True)
    CONTENT_LENGTH = HTMLField(
        max_length=100000, default=" ", null=True, )
    CONTENT_TYPE = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_ACCEPT = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_ACCEPT_ENCODING = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_ACCEPT_LANGUAGE = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_HOST = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_REFERER = HTMLField(
        max_length=100000, default=" ", null=True, )
    HTTP_USER_AGENT = HTMLField(
        max_length=100000, default=" ", null=True, )
    QUERY_STRING = HTMLField(
        max_length=100000, default=" ", null=True, verbose_name="QUERY_STRING ")
    REMOTE_ADDR = HTMLField(
        max_length=100000, default=" ", null=True, )
    REMOTE_HOST = HTMLField(
        max_length=100000, default=" ", null=True, )
    REMOTE_USER = HTMLField(
        max_length=100000, default=" ", null=True, )
    REQUEST_METHOD = HTMLField(
        max_length=100000, default=" ", null=True, )
    SERVER_NAME = HTMLField(
        max_length=100000, default=" ", null=True, )
    SERVER_PORT = HTMLField(
        max_length=100000, default=" ", null=True, )
    GET = HTMLField(
        max_length=100000, default=" ", null=True, )
    encoding = HTMLField(
        max_length=100000, default=" ", null=True, )
    COOKIES = HTMLField(
        max_length=100000, default=" ", null=True, )
    PATH = HTMLField(
        max_length=100000, default=" ", null=True, )
    ip_info = models.ForeignKey(IpInfo, blank=True, editable=False,
                                null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('Date_Update',)
        managed = True
        verbose_name = _("معلومات ريكوست الميتا")
        verbose_name_plural = _("معلومات ريكوست الميتا")

# IYE = 'IYE'
# FXX = 'FXX'
# QBA = 'QBA'
# AIRLINE_CHOICES = (
#     (IYE, '	الخطوط الجوية اليمنية'),
#     (FXX, ' طيران السعيدة	'),
#     (QBA, '	طيران الملكة بلقيس ')
#     (QBA, 'أخرى')

# )


# class PortfolioNoDetils(models.Model):
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, blank=False, null=False, verbose_name="القسم  "
#     )
#     created_by = models.ForeignKey(User, blank=True, editable=False,
#                                    null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة")
#     # Locations = models.ManyToManyField(
#     #     Location_Country,
#     #     #through='LocationContry',
#     #    # through_fields=('favorite', 'user'),
#     # )

#     titel = models.CharField(
#         max_length=250, default=" ", null=True, verbose_name="عنوان العمل  ")
#     #image = models.ManyToManyField()
#     Date_Update = models.DateTimeField(
#         auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

#     def __str__(self):
#         return self.titel

#     class Meta:
#         managed = True
#         verbose_name = "معرض الأعمال"
#         verbose_name_plural = "معرض الأعمال الشركة بدون كتابة تفاصيل"


# def portfolio_file_name(instance, filename):
    # return 'Image/'.join(['portfolio', instance.user.username, filename])

# FXX = 'FXX'
