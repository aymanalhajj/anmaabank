from django.db import models
from jopapp.models import Register
# Create your models here.


class ActivityType(models.Model):
    name = models.CharField(max_length = 100,unique = True, null= False, verbose_name = "اسم نوع النشاط")
    description = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "وصف مختصر لنوع النشاط")
    
    def __str__(self):
        return self.name

    class Meta:
        managed             = True
        verbose_name        = "نوع النشاط"
        verbose_name_plural = "نوع النشاط"


class GuaranteeType(models.Model):
    name = models.CharField(max_length = 100,unique = True, null= False, verbose_name = "اسم نوع الضمانه")
    description = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "وصف مختصر لنوع الضمانة")
    
    def __str__(self):
        return self.name

    class Meta:
        managed             = True
        verbose_name        = "نوع  الضمانة"
        verbose_name_plural = "نوع الضمانات"

class LoanApplication(models.Model):
    client_name =           models.CharField(max_length = 200,                                  verbose_name="اسم العميل")
    mobile_number =         models.CharField(max_length = 200,                                  verbose_name="رقم الجوال")
    city_name =             models.CharField(max_length = 200,                                  verbose_name="المدينة")
    street_name =           models.CharField(max_length = 200,                                  verbose_name="الحي/الشارع")
    nearest_known_place =   models.CharField(max_length = 200,                                  verbose_name="أقرب معلم بارز")
    project_created_at =    models.DateField(null=True, blank=True,                                                 verbose_name="عمر المشروع(تاريخ التأسيس)")
    current_capital =       models.IntegerField(max_length = 200,                               verbose_name="رأس مال المشروع حالياً")
    loan_purpose =          models.CharField(max_length = 200,                                  verbose_name="غرض التمويل")
    required_amount =       models.IntegerField(max_length = 200,                               verbose_name="مبلغ التمويل المطلوب")
    loan_months =           models.IntegerField(max_length = 200,                               verbose_name="مدة التمويل بالأشهر")
    monthly_installment =   models.IntegerField(max_length = 200,                               verbose_name="القسط الشهري")
    activity_type =         models.ForeignKey(ActivityType, on_delete = models.DO_NOTHING,      verbose_name="نوع النشاط")
    guarantee_type =        models.ForeignKey(GuaranteeType, on_delete = models.DO_NOTHING,     verbose_name="نوع الضمانة")
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,null=True, blank=True, verbose_name='المستخدم')
    class Meta:
        managed             = True
        verbose_name        = "طلب التمويل"
        verbose_name_plural = "طلبات التمويل"