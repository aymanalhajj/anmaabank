from django.db import models
from django.utils.translation import gettext_lazy as _
from jopapp.models import Register

from django.utils.translation import gettext_lazy as _
# Create your models here.

class ActivityType(models.Model):
    name = models.CharField(max_length = 100,unique = True, null= False, verbose_name = _("اسم نوع النشاط"))
    description = models.CharField(max_length = 100, null = True, blank = True, verbose_name = _("وصف مختصر لنوع النشاط"))
    
    def __str__(self):
        return self.name

    class Meta:
        managed             = True
        verbose_name        = _("نوع النشاط")
        verbose_name_plural = _("نوع النشاط")


class GuaranteeType(models.Model):
    name = models.CharField(max_length = 100,unique = True, null= False, verbose_name = _("اسم نوع الضمانه"))
    description = models.CharField(max_length = 100, null = True, blank = True, verbose_name = _("وصف مختصر لنوع الضمانة"))
    
    def __str__(self):
        return self.name

    class Meta:
        managed             = True
        verbose_name        = _("نوع  الضمانة")
        verbose_name_plural = _("نوع الضمانات")

class LoanApplication(models.Model):
    client_name =           models.CharField(max_length = 200,                                  verbose_name=_("client name"))#verbose_name=_("اسم العميل"))
    mobile_number =         models.CharField(max_length = 200,                                  verbose_name=_("رقم الجوال"))
    city_name =             models.CharField(max_length = 200,                                  verbose_name=_("المدينة"))
    street_name =           models.CharField(max_length = 200,                                  verbose_name=_("الحي/الشارع"))
    nearest_known_place =   models.CharField(max_length = 200,                                  verbose_name=_("أقرب معلم بارز"))
    project_created_at =    models.DateField(null=True, blank=True,                             verbose_name=_("عمر المشروع(تاريخ التأسيس)"))
    current_capital =       models.IntegerField(max_length = 200,                               verbose_name=_("رأس مال المشروع حالياً"))
    loan_purpose =          models.CharField(max_length = 200,                                  verbose_name=_("غرض التمويل"))
    required_amount =       models.IntegerField(max_length = 200,                               verbose_name=_("مبلغ التمويل المطلوب"))
    loan_months =           models.IntegerField(max_length = 200,                               verbose_name=_("مدة التمويل بالأشهر"))
    monthly_installment =   models.IntegerField(max_length = 200,                               verbose_name=_("القسط الشهري"))
    activity_type =         models.ForeignKey(ActivityType, on_delete = models.DO_NOTHING,      verbose_name=_("نوع النشاط"))
    guarantee_type =        models.ForeignKey(GuaranteeType, on_delete = models.DO_NOTHING,     verbose_name=_("نوع الضمانة"))
    user = models.ForeignKey(Register, on_delete=models.SET_NULL,null=True, blank=True,         verbose_name=_('المستخدم'))
    class Meta:
        managed             = True
        verbose_name        = _("طلب التمويل")
        verbose_name_plural = _("طلبات التمويل")