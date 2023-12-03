from django.db import models
from django.utils.translation import gettext_lazy as _
from distutils.command.upload import upload
import numbers
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
import datetime
from tinymce.models import HTMLField
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse
# from navbarapp.models import Navbars,SecondaryNavbars,ColumnNavbars


class OurVision(models.Model):
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")
    # column_navbar = models.ForeignKey(ColumnNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")

    titel = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم"),
        null=True,
    )
    detial_ar = HTMLField(
        # max_length=10000000,
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل رؤية الشركة"))

    image = models.ImageField(
        upload_to="Image/OurVision/%Y/%m/%d/", verbose_name=_(" إختيار صورة"), null=True,
        # verbose_name=_(" إختيار صورة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    is_hidden = models.BooleanField(
        default=False,
        help_text=_(" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده"),
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
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
                                   related_name='OurVision_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='OurVision_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='OurVision_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
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
    # name_action = models.CharField(
    #     max_length=250, verbose_name="اسم الحدث (النقرة)",
    #     null=True, blank=True,
    #     help_text="عنوان البوتون المراد النقر  فيها مثال : اقراء المزيد"
    # )
    # booking_link = models.URLField(
    #     # max_length=250,
    #     null=True, blank=True,

    #     verbose_name="رابط الحجز او استفسار عن الخدمة (اختياري)"
    # )
    # phone_whatsapp = models.CharField(
    #     max_length=20,
    #     null=True, blank=True,
    #     help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp  with out +",
    #     verbose_name="رقم تلفون الواتساب للحجز او استفسار عن الخدمة (اختياري)"
    # )
    # phone = PhoneNumberField(
    #     # max_length=250,
    #     null=True, blank=True,

    #     verbose_name="رقم تلفون اتصال للحجز او استفسار عن الخدمة (اختياري)"
    # )

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
        return self.detial_ar

    class Meta:
        managed = True
        verbose_name = _("رؤيتنــــا")
        verbose_name_plural = _("رؤيتنــــا")


class Objectives(models.Model):
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")
    # column_navbar = models.ForeignKey(ColumnNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")

    titel = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم"),
        null=True,
    )
    detial_ar = HTMLField(
        # max_length=10000000,
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل"))

    image = models.ImageField(
        upload_to="Image/OurVision/%Y/%m/%d/", verbose_name=_("إختيار صورة"), null=True,
        # verbose_name=_(" إختيار صورة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده",
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
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
                                   related_name='Objectivesn_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='Objectives_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='Objectives_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
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
        help_text=_("اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )
    # name_action = models.CharField(
    #     max_length=250, verbose_name="اسم الحدث (النقرة)",
    #     null=True, blank=True,
    #     help_text="عنوان البوتون المراد النقر  فيها مثال : اقراء المزيد"
    # )
    # booking_link = models.URLField(
    #     # max_length=250,
    #     null=True, blank=True,

    #     verbose_name="رابط الحجز او استفسار عن الخدمة (اختياري)"
    # )
    # phone_whatsapp = models.CharField(
    #     max_length=20,
    #     null=True, blank=True,
    #     help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp  with out +",
    #     verbose_name="رقم تلفون الواتساب للحجز او استفسار عن الخدمة (اختياري)"
    # )
    # phone = PhoneNumberField(
    #     # max_length=250,
    #     null=True, blank=True,

    #     verbose_name="رقم تلفون اتصال للحجز او استفسار عن الخدمة (اختياري)"
    # )

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
        return self.detial_ar

    class Meta:
        managed = True
        verbose_name = _("الـــغـــايــات")
        verbose_name_plural = _("الـــغـــايــات")

# class Objective(models.Model):

#     name  = models.CharField(
#          null=True,max_length=100, verbose_name="اسم الغاية"
#     )
#     date_added = models.DateTimeField(
#         auto_now_add=True, null=True, verbose_name=_("تاريخ الأضافة")
#     )
#     date_update = models.DateTimeField(
#         auto_now=True, null=True, verbose_name=_("تاريخ التعديل")
#     )
#     objective = models.ForeignKey(
#         Objectives, on_delete=models.SET_NULL,related_name="future_applications" ,
#         null=True, verbose_name="الغايات")


#     class Meta:
#         verbose_name = "مميزات التطبيق"
#         verbose_name_plural = "مميزات التطبيق"

#     def __str__(self):
#         return self.name


class About(models.Model):
    titel = models.CharField(
        max_length=250, verbose_name=_("العنوان")
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )
    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده",
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name=_("تاريخ الأنشاء "))

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='About_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='Abouton_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='About_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
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
    detial_ar = HTMLField(
        max_length=100000, default=" ", null=True,  verbose_name=_("التفاصيل"))
    image = models.ImageField(
        upload_to="Image/About/%Y/%m/%d/",  verbose_name=_(" إختيار صورة"), null=True,
        # verbose_name=_(" إختيار صورة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))

    def __str__(self):
        return self.titel

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
        return self.detial_ar

    class Meta:
        managed = True
        verbose_name = _("عنا")
        verbose_name_plural = _("عنا")


class MassegeAbout(models.Model):
    titel = models.CharField(
        max_length=250, verbose_name=_("العنوان")
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

    detial_ar = HTMLField(
        null=True,  verbose_name=_("التفاصيل"))
    image = models.ImageField(
        upload_to="Image/About/%Y/%m/%d/",  verbose_name=_(" إختيار صورة"), null=True,
        # verbose_name=_(" إختيار صورة")
    )
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name=_("تاريخ الأنشاء "))

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='MassegeAbout_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='MassegeAbout_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='MassegeAbout_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
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
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده",
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )

    def __str__(self):
        return self.titel

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
        return self.detial_ar

    class Meta:
        managed = True
        verbose_name = _("الرسالة")
        verbose_name_plural = _("الرسالة")
