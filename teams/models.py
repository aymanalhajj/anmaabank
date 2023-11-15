from django.db import models
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField
from navbarapp.models import Navbars,ColumnNavbars

# Create your models here.

from django.core.exceptions import ValidationError

from urllib.parse import urlparse
from django.core.exceptions import ValidationError

from functools import wraps


def validate_hostname(*hostnames):
    hostnames = set(hostnames)

    @wraps(validate_hostname)
    def validator(value):
        try:
            result = urlparse(value)
            if result.hostname not in hostnames:
                raise ValidationError(
                    f'The hostname {result.hostname} is not allowed.')
        except ValueError:
            raise ValidationError('invalid url')
    return validator


class Teams(models.Model):
    # navbar = models.ForeignKey(Navbars, 
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    # secondary_navbar = models.ForeignKey(SecondaryNavbars, blank=True,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الثنوي")
    # column_navbar = models.ForeignKey(ColumnNavbars,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="اسم العمود")
    full_name = models.CharField(
        max_length=250, verbose_name="الأسم الكامل"
    )
    jop = models.CharField(
        null=True,
        # blank=True,
        max_length=250, verbose_name="العمل"
    )
    facebook = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط حساب الفيسبوك إن وجد ",
        help_text="https://facebook.com",
        validators=[validate_hostname('facebook.com', 'www.facebook.com')]
    )
    twitter = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط حساب تويتر او منصة اكس إن وجد ",
        help_text="https://twitter.com",
        validators=[validate_hostname('twitter.com', 'www.twitter.com',
                                      'x.com', 'www.x.com'
                                      )]
    )
    instagram = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط حساب انستجرام إن وجد ",
        help_text="https://instagram.com",
        validators=[validate_hostname('instagram.com', 'www.instagram.com',

                                      )]
    )
    linkedin = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط حساب لنكدإن  إن وجد ",
        help_text="https://linkedin.com",
        validators=[validate_hostname('linkedin.com', 'www.linkedin.com',

                                      )]
    )
    youtube = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط قناة اليوتيوب ",
        help_text="https://youtube.com",
        validators=[validate_hostname('youtube.com', 'www.youtube.com',

                                      )]
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

    detial_ar = HTMLField(
        max_length=100000, default=" ", null=True, blank=True,  verbose_name="كلمة إن وجد")
    image = models.ImageField(
        upload_to="Image/Teams/%Y/%m/%d/", blank=True, verbose_name=" إختيار صورة", null=True,
    )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name="تاريخ الحذف "
                                      )
    created_at = models.DateTimeField(
        null=True,    auto_now_add=True, editable=False, blank=True, verbose_name="تاريخ الأنشاء ")
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     auto_now=True,
                                     verbose_name="تاريخ اخر تعديل "
                                     )
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=" تم التعديل  بواسطة ",
                                  related_name='teams_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    deleted_by = models.ForeignKey(User, blank=True, related_name='teams_deleted_by',
                                   verbose_name=" تم الحذف  بواسطة ",
                                   editable=False,
                                   null=True, on_delete=models.SET_NULL,)
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده",
        verbose_name="مخفي"
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name="محذوف "
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )

    short_note = models.CharField(
        max_length=200,
        null=True,
        default=" ",
        blank=True,
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

        verbose_name="ملاحظة قصيرة إن وجد")

    def __str__(self):
        return self.full_name
 # is_hidden = models.BooleanField(default=True,
    #                                 editable=True,
    #                                 verbose_name="مخفي")

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

    class Meta:
        managed = True
        verbose_name = "فريق العمل"
        verbose_name_plural = "فريق العمل"
