from django.db import models
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Clients(models.Model):
    # users = models.OneToOneField('Users')
    full_name = models.CharField(max_length=30, blank=True, null=True,)
    # last_name = models.CharField(max_length=60,blank=True,)
    # ci = models.CharField(max_length=9)
    # birth_date = models.DateField(null=True, blank=True)
    phone = PhoneNumberField(blank=True,
                             
                             null=True, verbose_name="رقم التلفون ان وجد")
    # city = models.CharField(max_length=20, blank=True, default="")
    image = models.ImageField(
        upload_to="Image/Clients/%Y/%m/%d/", blank=True, verbose_name="صورة الشعار ", null=True,
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
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name="تاريخ التعديل"
    )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    deleted_at = models.DateTimeField(  null=True, 
                                        blank=True, 
                                        editable=False,
                                        verbose_name="تاريخ الحذف "
    )
    deleted_by = models.ForeignKey(User, related_name='clients_deleted_by',
    
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
                                    related_name='clients_edited_by',
                                    null=True, 
                                    on_delete=models.SET_NULL,
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )
    short_note = models.CharField(
        max_length=1000,
        null=True,
        default=" ",
        blank=True,
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

        verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

    class Meta:
        db_table = ""
        managed = True
        verbose_name = " العملاء "
        verbose_name_plural = "العملاء"

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
