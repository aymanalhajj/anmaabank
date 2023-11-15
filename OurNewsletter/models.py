from django.db import models
from country_regions.models import Country,Region,Directorate,Isolation
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    # Phone_Number = models.CharField(
    #     max_length=250, null=True,
    #     verbose_name="رقم التلفون او البريد الألكتروني",

    # )
    country = models.ForeignKey(
        Country,
        null=True,
        # related_name="countr_Contact",
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="الدولة"
    )
    phone_whatsapp = models.CharField(
        max_length=20,
        null=True, blank=True,
        # help_text="https://api.whatsapp.com/send/?phone=phone_number_whatsapp",
        verbose_name="رقم تلفون الواتساب"
    )
    Phone_Number = PhoneNumberField(
        null=True, 
        verbose_name="رقم التلفون "
    )
    # emile = models.EmailField(
    #     max_length=250, null=True,blank=True
    #     verbose_name=" البريد الألكتروني",

    # )
    name = models.CharField(
        max_length=250, null=True,
        verbose_name="إسمك"
    )
    # service = models.ForeignKey(Service, blank=True, editable=False,
    #    null=True, on_delete=models.SET_NULL, verbose_name=" الخدمة")

    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )
    emile = models.EmailField(
        null=True, blank=True,
        verbose_name="  البريد الألكتروني",

    )
    # subject = models.CharField(
    #     max_length=250, blank=True, null=True, verbose_name="العنوان")
    Message = models.TextField(
        max_length=1000, null=True, verbose_name="الرساله")
    #image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")

    def __str__(self):
        return self.Message
    
    class Meta:
        managed = True
        verbose_name = "اتصل بناء "
        verbose_name_plural = "اتصل بناء"


class OurNewsletter(models.Model):
    # Phone_Number = models.CharField(
    #     max_length=250, null=True,
    #     verbose_name="رقم التلفون او البريد الألكتروني",

    # )
    emile = models.EmailField(
        # max_length=5000,
        #  null=True, blank=True,
        #   max_length=250,
        null=True,
        unique=True,
        verbose_name="البريد الألكتروني",
        error_messages={
            "required":
                "Please enter correct emile. "
                "."
            ,
            "unique": "البريد الألكتروني موجود من سابق",
        }
        # verbose_name=" البريد الألكتروني",

    )
    # name = models.CharField(
    #     max_length=250, null=True,
    #     verbose_name="إسمك"
    # )
    # service = models.ForeignKey(Service, blank=True, editable=False,
    #    null=True, on_delete=models.SET_NULL, verbose_name=" الخدمة")

    # Locations = models.ManyToManyField(
    #     Location_Country,
    #     #through='LocationContry',
    #    # through_fields=('favorite', 'user'),
    # )

    # subject = models.CharField(
    #     max_length=250, blank=True, null=True, verbose_name="العنوان")
    # Message = models.TextField(
    #     max_length=1000, null=True, verbose_name="الرساله")
    #image = models.ManyToManyField()
    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")

    def __str__(self):
        return self.emile

    class Meta:
        managed = True
        verbose_name = "مشتركين في اخر الاخبار"
        verbose_name_plural = "مشتركين في اخر الاخبار"

