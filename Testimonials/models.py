from django.db import models
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField

# Create your models here.


from django.db import models
# importing validationerror
from django.core.exceptions import ValidationError

# creating a validator function


def validate_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


def validate_facebook(value):
    if "facebook.com" in value:
        return value
    else:
        raise ValidationError("هذا الحقل يقبل رابط بموقع فيسبوك فقط ")


def validate_instagram(value):
    if "instagram.com" in value:
        return value
    else:
        raise ValidationError("هذا الحقل يقبل رابط بموقع انستجرام فقط ")


def default_error_messages_instagram():
    default_error_messages = {
        'invalid': _('“%(value)s”  رابط انستجرام  فقط '),
    }
    return default_error_messages


def validate_twitter(value):
    if "twitter.com" in value:
        return value
    else:
        raise ValidationError("هذا الحقل يقبل رابط بموقع تويتر فقط ")


def default_error_messages_twitter():
    default_error_messages = {
        'invalid': _('“%(value)s”  رابط تويتر  فقط '),
    }
    return default_error_messages


def validate_linkedin(value):
    if "linkedin.com" in value:
        return value
    else:
        raise ValidationError("هذا الحقل يقبل رابط بموقع لينكد ان فقط ")


def default_error_messages_linkedin():
    default_error_messages = {
        'invalid': _('“%(value)s”  رابط لينكد فقط '),
    }

    return default_error_messages


class Testimonials(models.Model):
    full_name = models.CharField(
        help_text=" سيتم عرضها بالموقع مثال '  ابراهيم شاهر'    ",
        # error_messages={
        #     "":"اختيار من 1 الى 5",
        #     "unique":"The Geeks Field you entered is not unique.",
        #     'invalid_choice': _(u'Value %r is not a valid choice.'),
        #     'null': _(u'This field cannot be null.'),
        #     'blank': _(u'This field cannot be blank.'),
        # },
        max_length=250, verbose_name="الأسم الكامل (سيتم عرضها بالموقع)"
    )
    adjective = models.CharField(
        help_text=" سيتم عرضها بالموقع مثال 'الرئيس التنفيذي لشركة رواد'    ",
        # error_messages="اختيار من 1 الى 5",

        max_length=250, null=True, default=" ", verbose_name=" الصفة او المهنة "
    )
    evaluation_number = models.PositiveIntegerField(
        # max_length=5,
        null=True, default=5,
        help_text="(سيتم عرضها بالموقع على هيئة نجوم)",
        error_messages={
            "invalid_choice": "اختيار من 1 الى 5",
            # "unique": "The  Field you entered is not unique.",
            # 'invalid_choice': _(u'Value  is not a valid choice.'),
            # 'null': _(u'This field cannot be null.'),
            # 'blank': _(u'This field cannot be blank.'),
        },
        verbose_name=" رقم تقييم العميل للشركة   "
    )
    detial_ar = HTMLField(
        default="", null=True, verbose_name="الشهادة او التوصيات او الرأْي (سيتم عرضها بالموقع)")
    # content = HTMLField(blank=True, null=True, verbose_name="")

    # image = models.ImageField(
    #     upload_to="Image/Testimonials/%Y/%m/%d/", blank=True, verbose_name=" إختيار صورة", null=True,
    # )
    # content = HTMLField(blank=True, null=True, verbose_name="المحتوى كود")

    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده",
        verbose_name="مخفي"
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ",
        verbose_name="محذوف "
    )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")
    facebook = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        validators=[validate_facebook],
        verbose_name="رابط حساب الفيسبوك (إن وجد - اختياري - لن يتم عرضه في الموقع ) "
    )

    twitter = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        validators=[validate_twitter],
        error_messages={
            'invalid': '  رابط تويتر  فقط ',
        },
        # error_messages=default_error_messages_twitter,
        help_text="(إن وجد - اختياري - لن يتم عرضه في الموقع )",
        verbose_name="رابط حساب تويتر "
    )
    instagram = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        # error_messages=default_error_messages_instagra
        help_text="(إن وجد - اختياري - لن يتم عرضه في الموقع )",

        validators=[validate_instagram],
        error_messages={
            'invalid': '  رابط انستجرا م  فقط ',
        },
        # error_messages=default_error_messages_instagram,
        verbose_name="رابط حساب انستجرام "
    )
    linkedin = models.URLField(
        # max_length=250,
        null=True,
        blank=True,
        error_messages={
            'invalid': '  رابط لنكدإن  فقط ',
        },
        validators=[validate_linkedin],
        # error_messages=default_error_messages_linkedin,
        help_text="(إن وجد - اختياري - لن يتم عرضه في الموقع )",

        verbose_name="رابط حساب لنكدإن "
    )
    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

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
                                  related_name='Testimonials_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    deleted_by = models.ForeignKey(User, blank=True, related_name='Testimonials_deleted_by',
                                   verbose_name=" تم الحذف  بواسطة ",
                                   editable=False,
                                   null=True, on_delete=models.SET_NULL,)

    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب ",
        help_text="(  اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد)"
    )
    short_note = models.CharField(
        max_length=200,
        null=True,
        default=" ",
        blank=True,
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

        verbose_name="ملاحظة قصيرة (إن وجد - لن يتم عرضه في الموقع )")

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
        verbose_name = "آراء العملاء"
        verbose_name_plural = "آراء العملاء"
