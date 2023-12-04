from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from navbarapp.models import Navbars, ColumnNavbars
from django.shortcuts import reverse


class Partners(models.Model):
    # navbar = models.ForeignKey(Navbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")
    # column_navbar = models.ForeignKey(ColumnNavbars,
    #    null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")
    # users = models.OneToOneField('Users')
    full_name = models.CharField(max_length=30,  null=True,)
    full_name_en = models.CharField(max_length=30,  null=True,)
    
    # last_name = models.CharField(max_length=60,blank=True,)
    # ci = models.CharField(max_length=9)
    # birth_date = models.DateField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True,
                             verbose_name=_("رقم التلفون ان وجد"))
    city = models.CharField(max_length=20, blank=True, default="")
    image = models.ImageField(
        upload_to="Image/Partners/%Y/%m/%d/", verbose_name=_("صورة الشعار "), null=True,
    )

    is_hidden = models.BooleanField(
        default=False,
        help_text=_(" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده"),
        verbose_name=_("مخفي")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name=_("محذوف ")
    )
    # is_hidden = models.BooleanField(default=False, verbose_name=_("مخفي"))
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name=_("رقم الترتيب (يرتب بالموقع حسب الرقم)")
    )
    # is_hidden = models.BooleanField(default=False, verbose_name=_("مخفي"))
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name=_("تاريخ الأضافة")
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name=_("تاريخ التعديل")
    )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name=_("تم الأنشاء بواسطة "))

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("تاريخ التعديل "))
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("تاريخ الأضافة "))
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_("تاريخ الحذف ")
                                      )
    deleted_by = models.ForeignKey(User, related_name='Partners_deleted_by',

                                   verbose_name=_(" تم الحذف  بواسطة "),
                                   editable=False,

                                   null=True, on_delete=models.SET_NULL,)
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
                                  related_name='Partners_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    # is_hidden = models.BooleanField(default=False, verbose_name=_("مخفي"))
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name=_("رقم الترتيب (يرتب بالموقع حسب الرقم)")
    )
    short_note = models.CharField(
        max_length=200,
        null=True,
        default=" ",
        blank=True,
        help_text=_(" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً"),

        verbose_name=_("ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)"))

    class Meta:
        db_table = ""
        managed = True
        verbose_name = _("الشركاء")
        verbose_name_plural = _("الشركاء")

    def save(self, *args, **kwargs):
        if self.sort_no is None:
            self.sort_no = self.id
        else:
            self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
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
        return reverse('index',  kwargs={})
