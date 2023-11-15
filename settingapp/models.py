from django.db import models
from distutils.command.upload import upload
import numbers
from django.db import models
from django.contrib.auth.models import User, Group
import datetime
from tinymce.models import HTMLField
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
# from teams.models import validate_hostname
from .cache import del_cached_active_theme

from urllib.parse import urlparse
from django.core.exceptions import ValidationError
from functools import wraps
# from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


class SettingModelQuerySet(models.QuerySet):
    def get_active(self):
        objs_active_qs = self.filter(is_deleted=False)
        objs_active_ls = list(objs_active_qs)
        objs_active_count = len(objs_active_ls)

        if objs_active_count == 0:
            obj = self.all().first()
            if obj:
                obj.set_active()
            else:
                obj = self.create()

        elif objs_active_count == 1:
            obj = objs_active_ls[0]

        elif objs_active_count > 1:
            obj = objs_active_ls[-1]
            obj.set_active()

        return obj


def validate_hostname(*hostnames):
    hostnames = set(hostnames)

    @wraps(validate_hostname)
    def validator(value):
        try:
            result = urlparse(value)
            if result.hostname not in hostnames:
                raise ValidationError(
                    f'هذا الرابط  {result.hostname} غير مسموح')
        except ValueError:
            raise ValidationError('invalid url')
    return validator


class SettingModel(models.Model):

    # detial_ar = HTMLField(
    #     max_length=10000000,
    #     default=" ", null=True, blank=True, verbose_name="تفاصيل رؤية الشركة")
    footer = models.CharField(
        #     max_length=10000000,
        max_length=300,
        null=True,
        default=" جميع الحقوق محفوظة © لـ بنك الإنماء للتمويل الأصغر الإسلامي 2023",
    )
    name_website_short = models.CharField(
        max_length=20,
        null=True, blank=True,
        default="بنك الإنماء",

        verbose_name="اسم website مختصر",
        # help_text="https://youtube.com",
        # validators=[validate_hostname('youtube.com', 'www.youtube.com')]
    )
    name_website = models.CharField(
        # max_length=10000000,
        max_length=50,
        null=True, blank=True,
        default=" بنك الإنماء للتمويل الأصغر الإسلامي ",

        verbose_name="اسم website",
        # help_text="https://youtube.com",
        # validators=[validate_hostname('youtube.com', 'www.youtube.com')]
    )
    facebook = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        # default="",

        verbose_name="رابط حساب الفيسبوك إن وجد ",
        help_text="https://facebook.com",
        validators=[validate_hostname('facebook.com', 'www.facebook.com')]
    )

    telegram = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="رابط تلجرام إن وجد ",
        help_text="https://t.me/",
        validators=[validate_hostname(
            't.me', 'www.t.me', 'telegram.com', 'www.telegram.com')]
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
    whatsapp = PhoneNumberField(
        max_length=20,
        null=True, blank=True,
        help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name="رقم تلفون الواتساب"
    )
    phone_1 = PhoneNumberField(
        # max_length=250,
        null=True,
        blank=True,
        # default="",

        verbose_name="هاتف 1"
    )
    phone_2 = PhoneNumberField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="هاتف 2"
    )
    fax = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="فاكس"
    )
    free_phone_numbar = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="الرقم المجاني"
    )

    emile = models.EmailField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="البريد الإلكتروني"
    )
    mail_box = models.PositiveSmallIntegerField(
        # max_length=250,
        null=True,
        blank=True,
        verbose_name="الصندوق البريدي"
    )

    # twitter = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name="رابط حساب تويتر"
    # )
    # instagram = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name="رابط حساب انستجرام "
    # )
    # linkedin = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name="رابط حساب لنكدإن "
    # )
    # facebook_url = models.URLField(
    #     # max_length=10000000,
    #      default=" ", null=True, blank=True, verbose_name="رابط صفحة  الفيسبوك")
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")

    # is_hidden_adsenceHeder = models.BooleanField(
    #     default=False,
    #     help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
    #     verbose_name="اخفاء قسم الاعلانات المتحركة في اعلا الصفحه"
    # )
    is_hidden_branche = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الفروع"
    )
    is_hidden_contact = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم اتصل بنا"
    )
    is_hidden_about = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم نبذه عنا"
    )
    is_hidden_button_action = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء action  "
    )
    is_hidden_client = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم  العملاء"
    )
    is_hidden_galary = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم معرض الصور"
    )
    is_hidden_teams = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم فريق العمل"
    )
    is_hidden_partner = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم شركائنا"
    )
    is_hidden_ournewsletter = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم اشترك باخر الاخبار"
    )
    is_hidden_imagesportfolionodetils = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم معرض الــصــور"
    )
    is_hidden_ourmarch = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم مسيرتنــــا"
    )
    is_hidden_sectio_page_all = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الاقسام والصفحات"
    )
    is_hidden_sectio_page_in_home_only = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الاقسام والصفحات من الشاشة الرئسية فقط"
    )
    is_hidden_ourmission = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم مهمتنــــا"
    )

    is_hidden_bank_applications = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم تطبيقات البنك"
    )
    is_hidden_adsence_header = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الاعلانات المتحركة في اعلا الصفحه"
    )
    is_hidden_last_news = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم اخر الاخبار في الشاشة الرئيسية "
    )
    is_hidden_footer = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء  اسفل الصفحة 'footer' بشكل كامل  "
    )
    is_hidden_faq = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الأسئلة الشائعة"
    )
    is_hidden_currencies = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء اسعار العملات "
    )
    is_hidden_logo_ainmation = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم الشعار اعلا اسفل الصفحة "
    )
    is_hidden_images_portfolio_no_detils = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم معرض الصور "
    )
    is_hidden_services = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
        verbose_name="اخفاء قسم خدمات "
    )
    # is_hidden_services_person = models.BooleanField(
    #     default=False,
    #     help_text=" سيتم اخفاء هذا القسم  من العرض بالموقع بحال تم تحديده",
    #     verbose_name="اخفاء قسم خدمات الافراد"
    # )

    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name="محذوف "
    )
    # created_by = models.ForeignKey(User, blank=True, editable=False,
    #                                null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")
    deleted_at = models.DateTimeField(null=True,
                                      blank=True,
                                      editable=False,
                                      verbose_name="تاريخ الحذف "
                                      )
    # created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")

    deleted_by = models.ForeignKey(User, blank=True,
                                   verbose_name=" تم الحذف  بواسطة ",
                                   editable=False,
                                   related_name='setting_model_deleted_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='setting_model_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="تم الأنشاء بواسطة ")
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=" تم التعديل  بواسطة ",
                                  related_name='setting_model_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name="تاريخ الأنشاء ")
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name="تاريخ اخر تعديل "
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
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",
        verbose_name="ملاحظة قصيرة"
    )
    objects = SettingModelQuerySet.as_manager()

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
        return "الاعــــدادات"

    class Meta:
        managed = True
        verbose_name = "الاعــــدادات"
        verbose_name_plural = "الاعـــدادات"


@receiver(post_save, sender=SettingModel)
def post_save_handler(sender, instance, **kwargs):
    del_cached_active_theme()
    if instance.is_deleted == False:
        SettingModel.objects.exclude(pk=instance.pk).update(is_deleted=True)
    SettingModel.objects.get_active()
