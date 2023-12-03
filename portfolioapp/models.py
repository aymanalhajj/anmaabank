from django.db import models
from django.utils.translation import gettext_lazy as _
from distutils.command.upload import upload
import numbers
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
import datetime
from tinymce.models import HTMLField
from django.shortcuts import reverse
# Create your models here.
# from navbarapp.models import Navbars,SecondaryNavbars,ColumnNavbars


class Category(models.Model):
    name = models.CharField(
        max_length=250, verbose_name=_("اسم القسم")
    )

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = _("اقسام معرض الأعمال  ")
        verbose_name_plural = _("قسم معرض الأعمال")


class Portfolio(models.Model):
    # navbar = models.ForeignKey(Navbars, 
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")
    # column_navbar = models.ForeignKey(ColumnNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=False, verbose_name=_("القسم")
    )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("(إختياري) تم الأنشاء بواسطة "))
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )
    Client = models.CharField(
        max_length=250, default=" ", blank=True, null=True, verbose_name=_("اسم العميل   (إختياري)"))

    PhoneNo_one = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("رقم  التلفون الأول   (إختياري)"))
    PhoneNo_two = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("رقم  التلفون الثاني   (إختياري)"))
    PhoneNo_whatsapp = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("رقم  التلفون واتس أب   (إختياري)"))
    PhoneNo_landline = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("رقم  الثابت (إختياري)"))
    Url_ForProject = models.URLField(
        blank=True, null=True, verbose_name=_("رابط للخدمة ان وجد"))
    detial_ar = HTMLField(
        max_length=100000, null=True,  blank=True, verbose_name=_("التفاصيل"))
    titel = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("عنوان العمل"))
   # image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.titel

    class Meta:
        managed = True
        verbose_name = _("معرض الأعمال")
        verbose_name_plural = _("معرض الأعمال الشركة معا كتابة التفاصيل")


class ImagesPortfolio(models.Model):
    image = models.ImageField(
        # upload_to=portfolio_file_name,

        upload_to="Image/ImagesPortfolio/%Y/%m/%d/",
         verbose_name=_("إختيار صورة"), null=True,
    )

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
    )
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.SET_NULL, null=True, verbose_name=_("المعرض"))

    class Meta:
        verbose_name = _("صور معرض اعمال الشركة  ")
        verbose_name_plural = _("صور اعمال الشركة مع التفاصيل  ")

    def __str__(self):
        return "this image {0}  {1} for portfolio    {2}   ".format(
            self.id,  self.image, self.portfolio.titel
        )


class ImagesPortfolioNoDetils(models.Model):
    titel = models.CharField(
        max_length=250, default=" ", null=True, verbose_name=_("عنوان الصورة"))
    # image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    image = models.ImageField(
        # upload_to=portfolio_file_name,
        upload_to="Image/ImagesPortfolioNoDetils/%Y/%m/%d/",
        verbose_name=_("إختيار صورة"), null=True,

    )

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
    )
    # portfolioNoDetils = models.ForeignKey(
    # PortfolioNoDetils, on_delete=models.SET_NULL, null=True, verbose_name=" المعرض")

    class Meta:
        verbose_name = _("معرض الصور")
        verbose_name_plural = _("معرض الصور")

    def __str__(self):
        return " {0}    {1}   ".format(
            self.id, self.titel
        )
