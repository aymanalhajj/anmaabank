from django.db import models
from django.utils.translation import gettext_lazy as _
# from navbarapp.models import ColumnNavbars as columnna

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.shortcuts import reverse
#

VIEW_CHOICES = (
    ("الرئيسية", 'الصفحة الرئيسية'),
    ("منفصل", 'صفحة منفصل'),
    # (sar, 'ريال سعودي')
)
STYLE_CHOICES = (
    ("V", ' افقي'),
    ("H", ' عمودي'),
    # (sar, 'ريال سعودي')
)
NOMBAR_CHOICES = (
    ("1", '1'),
    ("2", '2'),
    ("3", '3'),
    ("4", '4'),

    # (sar, 'ريال سعودي')
)


class SectionPage(models.Model):
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")

    # column_navbar = models.ForeignKey(ColumnNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("(إختياري) تم الأنشاء بواسطة "))

    titel = models.CharField(
        max_length=250, null=True, verbose_name=_("عنوان القسم  "))
    short_titel = models.CharField(
        max_length=250, null=True, default="",  blank=True, verbose_name=_("جملة قصيرة اسفل العنوان"))

    detial_ar = HTMLField(
        null=True,  blank=True, verbose_name=_("تفاصيل"),
        default="",
    )

   # image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    image = models.ImageField(
        # upload_to=portfolio_file_name,

        upload_to="Image/SectionPage/%Y/%m/%d/",
        verbose_name=_(" إختيار صورة"), null=True,
    )
    view = models.CharField(
        max_length=100,
        choices=VIEW_CHOICES,
        # default="الرئيسية",
        null=True,
        verbose_name=_("صفحة عرض القسم"),
        # blank=True
    )
    # style = models.CharField(
    #     max_length=100,
    #     choices=STYLE_CHOICES,
    #     default="V",
    #     null=True,
    #     verbose_name="عملة الخدمة يبتداء من",

    #     # blank=True
    # )
    number_rows = models.CharField(
        null=True,
        choices=NOMBAR_CHOICES,

        # default="4",
        verbose_name=_("عدد الصفوف"),
        max_length=100,
        help_text=_("عدد الصفوف العناصر في عرض الشاشة"),

        # blank=True

    )
    # is_display_image_item = models.BooleanField(
    #     default=False,
    #     help_text="في حال تحديد هذا العنصر ولم تتوفر صور سيتم عرض صور الشعار ",
    #     verbose_name="عرضه صور عناصر القسم اجباري"
    # )

    is_hidden = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده"),
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #    null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    deleted_by = models.ForeignKey(User,
                                   related_name='SectionPage_deleted_by',

                                   blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   null=True,
                                   editable=False,
                                   on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(
        null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     auto_now=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='SectionPage_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='SectionPage_created_by',
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name=_("رقم الترتيب "),
        help_text=_(" اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد")
    )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    # def __str__(self):
    #     return str(self.titel)

    class Meta:
        managed = True
        verbose_name = _("الاقسام والصفحات")
        verbose_name_plural = _("الاقسام والصفحات")

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

    def get_absolute_url(self):
        # return reverse_lazy('service-single', kwargs={'pk': self.pk})
        return reverse('section-singl',  kwargs={'id': self.pk})


class SectionPageProperty(models.Model):
    titel = models.CharField(
        max_length=250, null=True, verbose_name=_("عنوان الغاية"))
    image = models.ImageField(
        # upload_to=portfolio_file_name,

        upload_to="Image/SectionPage/%Y/%m/%d/",
        blank=True, verbose_name=_(" إختيار صورة"), null=True,
    )
    detial_ar = HTMLField(
        null=True,  blank=True, verbose_name=_("التفاصيل"))

    Date_Added = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
    )
    our_advantage = models.ForeignKey(

        SectionPage, on_delete=models.SET_NULL, null=True, related_name="our_dvantages_property",
        verbose_name=_("القسم"))

    is_hidden = models.BooleanField(
        default=False,
        help_text=_("سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده"),
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #    null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    deleted_by = models.ForeignKey(User,
                                   related_name='SectionPageProperty_deleted_by',

                                   blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   null=True,
                                   editable=False,
                                   on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(
        null=True,    auto_now_add=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     auto_now=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='SectionPageProperty_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='SectionPageProperty_created_by',
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name=_("رقم الترتيب "),
        help_text=_("اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد")
    )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    # def __str__(self):
    #     return self.titel

    class Meta:
        managed = True
        verbose_name = _("محتوى فرعي للقسم")
        verbose_name_plural = _("محتوى فرعي للقسم")

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
