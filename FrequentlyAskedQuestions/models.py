from django.db import models
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField
# from tinymce import models as tinymce_models
# Create your models here.


class FrequentlyAskedQuestions(models.Model):
    question = models.CharField(
        max_length=250, verbose_name="السؤال"
    )

    answer = HTMLField(
        max_length=100000, default=" ", null=True, verbose_name="الأجابة")
    # image = models.ImageField(
    # upload_to="Image/Teams/%Y/%m/%d/", blank=True, verbose_name=" إختيار صورة", null=True,
    # )
    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")
    # content = HTMLField(blank=True, null=True, verbose_name="المحتوى كود")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    deleted_at = models.DateTimeField(  null=True, 
                                        blank=True, 
                                        editable=False,
                                        verbose_name="تاريخ الحذف "
    )
    deleted_by = models.ForeignKey(User, blank=True, related_name='frequently_deleted_by',
                                        verbose_name=" تم الحذف  بواسطة ", 
                                        editable=False, 
                                   null=True, on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")
    edited_at = models.DateTimeField(   null=True,  
                                        editable=False,
                                        blank=True, 
                                        auto_now=True, 
                                        verbose_name="تاريخ اخر تعديل "
    )
    edited_by = models.ForeignKey(  User, 
                                    blank=True,
                                    editable=False,
                                    verbose_name=" تم التعديل  بواسطة ", 
                                    related_name='frequently_edited_by',
                                    null=True, 
                                    on_delete=models.SET_NULL,
    )
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

        verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

    def __str__(self):
        return self.question
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
        verbose_name = "أسئلة شائعه عنا"
        verbose_name_plural = "أسئلة شائعه عنا"
