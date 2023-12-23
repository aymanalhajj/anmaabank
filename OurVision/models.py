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
    titel = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم"),
        null=True,
    )
    detial_ar = models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل رؤية الشركة"))

    titel_en = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم بالانجليزي"),
        null=True,
    )
    detial_en =  models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل رؤية الشركة بالانجليزي"))

    image = models.ImageField(
        upload_to="Image/OurVision/%Y/%m/%d/", verbose_name=_(" إختيار صورة"), null=True,
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
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

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


class OurStartup(models.Model):
    title = models.CharField(
        max_length=250, verbose_name=_("عنوان النشأة"),
        null=True,
    )
    detail_ar = models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل النشأة"))

    title_en = models.CharField(
        max_length=250, verbose_name=_("عنوان النشأة بالانجليزي"),
        null=True,
    )
    detail_en =  models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل النشأة بالانجليزي"))

    image = models.ImageField(
        upload_to="Image/OurVision/%Y/%m/%d/", verbose_name=_(" إختيار صورة"), null=True,
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
                                   related_name='OurStartup_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='OurStartup_created_by',
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
                                  related_name='OurStartup_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.detail_ar

    class Meta:
        managed = True
        verbose_name = _("نشـأة البنك")
        verbose_name_plural = _("نشـأة البنك")


class Objectives(models.Model):
    titel = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم"),
        null=True,
    )
    detial_ar =  models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل بالعربي"))
    
    titel_en = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم انجليزي"),
        null=True,
    )
    detial_en = models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل بالانجليزي"))

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
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
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
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_("اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
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


class Values(models.Model):
    title = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم"),
        null=True,
    )
    detail_ar =  models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل بالعربي"))
    
    title_en = models.CharField(
        max_length=250, verbose_name=_("عنوان القسم انجليزي"),
        null=True,
    )
    detail_en = models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("تفاصيل بالانجليزي"))

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
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,
                                   related_name='values_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='values_created_by',
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
                                  related_name='values_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=_("اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),
        verbose_name=_("ملاحظة قصيرة")
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.detail_ar

    class Meta:
        managed = True
        verbose_name = _("القيم")
        verbose_name_plural = _("القيم")


class About(models.Model):
    titel = models.CharField(
        max_length=250, verbose_name=_("العنوان")
    )
    titel_en = models.CharField(
        max_length=250, verbose_name=_("العنوان بالانجليزي")
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
    
    detial_en = HTMLField(
        max_length=100000, default=" ", null=True,  verbose_name=_("التفاصيل بالانجليزي"))
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
    title = models.CharField(
        max_length=250, verbose_name=_("العنوان"),
        null=True,
    )
    detail_ar =  models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("التفاصيل بالعربي"))
    
    title_en = models.CharField(
        max_length=250, verbose_name=_("العنوان انجليزي"),
        null=True,
    )
    detail_en = models.TextField(
        default=" ", null=True, blank=True, verbose_name=_("التفاصيل بالانجليزي"))

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
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return str(self.detail_ar)

    class Meta:
        managed = True
        verbose_name = _("الرسالة")
        verbose_name_plural = _("الرسالة")
