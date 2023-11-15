from django.db import models
from django.db import models
from django.contrib.auth.models import User, Group
import datetime
from tinymce.models import HTMLField
from django.shortcuts import reverse

# from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
CATEGORU = (
    ("اخبار البنك", _("اخبار البنك")),
    ("الفعاليات", _("الفعاليات")),
    ("المدونة", _("المدونة"))
    # ("اخرى", _("اخرى")),

)
CATEGORU_Policies = (
    ("سياسة خصوصية", _("سياسة خصوصية")),
    ("مكافحة غسل الأموال", _("مكافحة غسل الأموال")),
    ("اخرى", _("اخرى"))
    # ("اخرى", _("اخرى")),

)
# Create your models here.


class CategoryBlog(models.Model):
    name = models.CharField(
        max_length=250, verbose_name="عنوان القسم  "
    )
    # logo = models.ImageField(
    #     upload_to="Image/CategoryBlog/%Y/%m/%d/", blank=True,
    #     verbose_name="", null=True,
    # )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL,
                                   verbose_name="تم الأنشاء بواسطة ")
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name_plural = " قسم المقالات و آخر الأخبار  "
        verbose_name = " قسم المقالات و آخر الأخبار  "


class Blogs(models.Model):
    titel = models.CharField(
        max_length=70, verbose_name="عنوان الخبر او المقالة"
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

    image = models.ImageField(
        upload_to="Image/Blog/%Y/%m/%d/",
        verbose_name=" إختيار صورة المدونة", null=True,
    )
    # balance = MoneyField(max_digits=14, blank=True,
    #  null=True, decimal_places=2, default_currency=usd,
    #  verbose_name="سعر الخدمة يبتداء من"
    #  )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    # airline = models.CharField(
    #     max_length=3,
    #     choices=CURRENCY_CHOICES,
    #     default=usd,
    #     null=True,
    #     verbose_name="شركة طيران",
    #     blank=True
    # )
    # airline = models.ForeignKey(
    #     Airline, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="الصنف",

    # )
    category = models.CharField(verbose_name=_(
        "نوع المقال"), null=True, max_length=100, choices=CATEGORU,)
    category_blog = models.ForeignKey(
        CategoryBlog, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="الصنف",
        related_name="category_blog"

    )
    date_post = models.DateField(default=datetime.datetime.now,
                                 # auto_now_add=True,
                                 blank=True, null=True, verbose_name="تاريخ النشر ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    detial_ar = HTMLField(
        # blank=True,
        null=True,
        # max_length=1000000000,
        # default="",
        verbose_name="المقال او المحتوى"
    )

    def __str__(self):
        return self.titel

    # def get_absolute_url(self):
        # return reverse('last-news')

    class Meta:
        managed = True
        verbose_name = "  المقالات و آخر الأخبار  "
        verbose_name_plural = "  المقالات و آخر الأخبار  "

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('last-news-detiel',  kwargs={'id': self.pk})


class ImagesBlogs(models.Model):
    image = models.ImageField(
        # upload_to=portfolio_file_name,

        upload_to="Image/ImagesBlogs/%Y/%m/%d/",
        blank=True, verbose_name=" إختيار صورة", null=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاريخ الأضافة"
    )
    date_update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاريخ التعديل"
    )
    blog = models.ForeignKey(
        Blogs, on_delete=models.SET_NULL, null=True, verbose_name=" المقال")

    class Meta:
        verbose_name = "صور المدونة البنك  "
        verbose_name_plural = "صور المدونة البنك"

    def __str__(self):
        return "this image {0}  {1} for blog    {2}   ".format(
            self.id,  self.image, self.blog.titel
        )


class Policies(models.Model):
    titel = models.CharField(
        max_length=70, verbose_name="عنوان السياسة "
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

    detial_ar = HTMLField(
        # blank=True,
        null=True,
        max_length=1000000000,
        default="",
        verbose_name="تفاصيل"
    )
    image = models.ImageField(
        upload_to="Image/Blog/%Y/%m/%d/",
        verbose_name=" إختيار صورة السياسة", null=True,
    )
    # balance = MoneyField(max_digits=14, blank=True,
    #  null=True, decimal_places=2, default_currency=usd,
    #  verbose_name="سعر الخدمة يبتداء من"
    #  )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    # airline = models.CharField(
    #     max_length=3,
    #     choices=CURRENCY_CHOICES,
    #     default=usd,
    #     null=True,
    #     verbose_name="شركة طيران",
    #     blank=True
    # )
    # airline = models.ForeignKey(
    #     Airline, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="الصنف",

    # )
    category = models.CharField(verbose_name=_(
        "نوع السياسة"), null=True, max_length=100, choices=CATEGORU_Policies,)
    # category_blog = models.ForeignKey(
    #     CategoryBlog, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="الصنف",
    #     related_name="category_blog"

    # )
    date_post = models.DateField(default=datetime.datetime.now,
                                 # auto_now_add=True,
                                 blank=True, null=True, verbose_name="تاريخ النشر ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")

    def __str__(self):
        return self.titel

    # def get_absolute_url(self):
        # return reverse('last-news')

    class Meta:
        managed = True
        verbose_name = " السياسات "
        verbose_name_plural = "  السياسات "

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('Policies',  kwargs={'id': self.pk})
