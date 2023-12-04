from country_regions.models import Region
from django.db import models
from django.utils.translation import gettext_lazy as _
# import shapely
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# from teams.models import validate_hostname
# from erp_system.utils import *
# from staff.models import Staff
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

# from common.utils import TYPEUSER, GENDERCHOICE, INDCHOICES, EVENT_STATUS, COUNTRIES, INDCHOICES, LEAD_SOURCE, CURRENCY_CODES, LEAD_STATUS, STAGES, STATUS_CHOICE, PRIORITY_CHOICE, CASE_TYPE
# from common.models import Tags, Org, Users, Contact, Address


class Address(models.Model):

    address_line = models.CharField(
        verbose_name=_("العنوان"), max_length=255, null=True,
    )
    street = models.CharField(
        _("الشارع"), max_length=55, blank=True, default="")
    # city = models.CharField(_("City"), max_length=255, blank=True, default="")
    region = models.ForeignKey(
        Region, verbose_name=_(
            "المدينة"), on_delete=models.DO_NOTHING, null=True,)
    # state = models.CharField(
    #     _("State"), max_length=255, blank=True, default="")
    postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True, default=""
    )
    # country = models.CharField(
    # max_length=3, choices=COUNTRIES, blank=True, default="")
    map_location = models.URLField(
        verbose_name=_("رابط الموقع على خرائط جوجل"), help_text="https://www.google.com/maps/@15.3616384,44.2073088,13z?entry=ttu",
        blank=True, null=True)
    lat = models.FloatField(
        verbose_name=_(" خط العرض"), null=True)
    long = models.FloatField(
        verbose_name=_(" خط الطول"),  null=True)
    # def clean(self):

    # type_choice = self.type_choice
    # google_play = self.google_play
    # app_store = self.app_store
    # website_url = self.website
    # desketop_url = self.desketop
    # errors={}

    #     lon = self.long
    #     lat = self.lat
    #     lon %= 360
    # # Put the longitude in the range of [-180,180):
    #     if lon >= 180:
    #         lon -= 360
    # lon_lat_point = shapely.geometry.Point(lon, lat)
    # lon_lat_bounds = shapely.geometry.Polygon.from_bounds(
    #     xmin=-180.0, ymin=-90.0, xmax=180.0, ymax=90.0
    # )
    # return lon_lat_bounds.intersects(lon_lat_point)
    # would not provide any corrected values

    # if lon_lat_bounds.intersects(lon_lat_point):
    #     return
    # else:
    #     errors["lat"]= "ادخل خط عرض صحيح"
    #     errors["long"]= "ادخل خط طول صحيح"

    # return lon, lat
    # if type_choice == mobile:
    #     if google_play is None or google_play is '':
    #         errors["google_play"]= "الرجاء ادخال رابط التطبيق على Google Play"
    #     if app_store is None or app_store is '':
    #         errors["app_store"]= "الرجاء ادخال رابط التطبيق على app Store"
    # elif type_choice == website:
    #     if website_url is None or website_url is '':
    #         errors["website"]= "الرجاء ادخال رابط الموقع  الالكتروني"
    # elif type_choice == desketop:
    #     if desketop_url is None or desketop_url is '':
    #         errors["desketop"]= "الرجاء ادخال رابط تحميل تطبيق سطح المكتب "
    # if app_store is None or app_store is '':
    #     errors["app_store"]= "الرجاء ادخال رابط التطبيق على app Store"
    # return self.cleaned_data
    # if errors:
    #     raise ValidationError(errors)
    def __str__(self):
        return self.address_line if self.address_line else ""

    class Meta:
        managed = True
        verbose_name = _("عنوان فروع")
        verbose_name_plural = _("عناوين الفروع")

    def get_complete_address(self):
        address = ""
        if self.address_line:
            address += self.address_line
        if self.street:
            if address:
                address += ", " + self.street
            else:
                address += self.street
        # if self.city:
        #     if address:
        #         address += ", " + self.city
        #     else:
        #         address += self.city
        if self.state:
            if address:
                address += ", " + self.state
            else:
                address += self.state
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode
        if self.country:
            if address:
                address += ", " + self.get_country_display()
            else:
                address += self.get_country_display()
        return address


CATEGORU = (
    ("فرع", _("فرع")),
    ("صراف آلي", _("صراف آلي")),
    ("وكيل", _("وكيل")),
    # ("اخرى", _("اخرى")),

)
CATEGORU_HORSE = (
    ("24", _("24 ساعة")),
    ("فترتين", _("فترتين")),
    ("فترة واحده", _("فترة واحده")),
    # ("اخرى", _("اخرى")),

)


class SerchModel(models.Model):
    search = models.CharField(verbose_name=_(
        "ابحث هنا"), blank=True, help_text="اسم الفرع او اسم الشارع او اسم نقطة الخدمة", null=True, max_length=64,)
    category = models.CharField(verbose_name=_(
        "نوع نقطة الخدمة"), blank=True, null=True, max_length=100, choices=CATEGORU,)
    region = models.ForeignKey(
        Region, verbose_name=_(
            "region - المدينة"), blank=True,  on_delete=models.DO_NOTHING, null=True,)


class Branches(models.Model):
    # client_id = models.AutoField(primary_key=True)
    # org = models.ForeignKey(
    #     Org, null=True, on_delete=models.SET_NULL, blank=True
    # )
    name = models.CharField(verbose_name=_(
        "اسم الفرع"), null=True, max_length=64,)
    name_en = models.CharField(verbose_name=_(
        "اسم الفرع بالانجليزي"), null=True, max_length=64,)
    address1 = models.ForeignKey(
        Address, null=True, on_delete=models.SET_NULL, verbose_name=_(" العنوان 1"), related_name="branches_address1"
    )
    
    # address2 = models.ForeignKey(
    #     Address, null=True, on_delete=models.SET_NULL,verbose_name= _(" العنوان 2"), blank=True,related_name="branches_address2"
    # )

    # website = models.URLField(
    #     verbose_name=_("رابط موقع الويب"), max_length=255, blank=True, null=True)
    # description = models.TextField(verbose_name=_(
    #     "وصف"), blank=True, null=True)
    # facebook = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name=_("رابط حساب الفيسبوك إن وجد "),
    #     help_text="https://facebook.com",
    #     validators=[validate_hostname('facebook.com', 'www.facebook.com')]
    # )
    # youtube = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name=_("رابط قناة اليوتيوب "),
    #     help_text="https://youtube.com",
    #     validators=[validate_hostname('youtube.com', 'www.youtube.com',

    #                                   )]
    # )
    # twitter = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name=_("رابط حساب تويتر او منصة اكس إن وجد "),
    #     help_text="https://twitter.com",
    #     validators=[validate_hostname('twitter.com', 'www.twitter.com',
    #                                   'x.com', 'www.x.com'
    #                                   )]
    # )
    # instagram = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name=_("رابط حساب انستجرام إن وجد "),
    #     help_text="https://instagram.com",
    #     validators=[validate_hostname('instagram.com', 'www.instagram.com',

    #                                   )]
    # )
    # linkedin = models.URLField(
    #     # max_length=250,
    #     null=True,
    #     blank=True,
    #     verbose_name=_("رابط حساب لنكدإن  إن وجد "),
    #     help_text="https://linkedin.com",
    #     validators=[validate_hostname('linkedin.com', 'www.linkedin.com',

    #                                   )]
    # )
    # account_name = models.CharField(
    # verbose_name=_("account name"), max_length=255, null=True, blank=True)

    # secondary_country_code = models.CharField(verbose_name=_("password"),max_length=100)
    # notes = models.CharField(verbose_name=_("password"),max_length=100)

    # city = models.CharField(verbose_name=_("password"),max_length=100)
    # timezone = models.CharField(verbose_name=_(
    # "timezone"), blank=True, null=True, max_length=100)

    # starting_balance = models.CharField(
    # verbose_name=_("starting balance"), blank=True, null=True, max_length=100)
    # phone1 = PhoneNumberField(verbose_name=_(
    #     "رقم التلفون "), null=True,)
    phone = PhoneNumberField("رقم التلفون  ", null=True,)
    HORSE = models.CharField(verbose_name=_(
        "اوقات الدوام"),  null=True, max_length=100, choices=CATEGORU_HORSE,)
    from_hourse_firest = models.TimeField(
        blank=True, null=True, verbose_name=_(
            "اوقات الدوام"),)
    to_hourse_firest = models.TimeField(blank=True, null=True, verbose_name=_(
        "اوقات الدوام"),)
    from_hourse_scond = models.TimeField(
        blank=True, null=True, verbose_name=_(
            "اوقات الدوام"),)
    to_hourse_scond = models.TimeField(blank=True, null=True, verbose_name=_(
        "اوقات الدوام"),)

    # is_offline = models.BooleanField()
    # group_price_id = models.CharField(
    #     verbose_name=_("Group Price"), blank=True, null=True, max_length=100)
    # password = models.CharField(verbose_name=_("password"),_("password"),_("password"),max_length=100)

    # credit_limit = models.CharField(verbose_name=_("password"), max_length=100)
    # credit_period = models.CharField(
    # verbose_name=_("Credit Period"), blank=True, null=True, max_length=100)

    # bn1_label = models.CharField(verbose_name=_("password"), max_length=100)
    # state = models.CharField(verbose_name=_(
    # "state"), blank=True, null=True, max_length=100)
    # secondary_address1 = models.CharField(
    #     _("secondary address 1"), blank=True, null=True, max_length=100)
    # name = models.CharField(verbose_name=_("name"), max_length=100)
    # email = models.EmailField(max_length=100, blank=True, null=True,)
    # number_employees = models.IntegerField(
    #     blank=True, verbose_name=_("عدد الموظفين"), null=True,)
    created_at = models.DateTimeField(
        null=True, editable=False, blank=True, verbose_name=_("تاريخ الأنشاء "))
    edited_at = models.DateTimeField(null=True,
                                     editable=False,
                                     blank=True,
                                     verbose_name=_("تاريخ اخر تعديل ")
                                     )
    created_by = models.ForeignKey(User, blank=True, editable=False, related_name='branches_model_created_by',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_("تم الأنشاء بواسطة "))
    edited_by = models.ForeignKey(User,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_(" تم التعديل  بواسطة "),
                                  related_name='branches_model_edited_by',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  )
    # secondary_city = models.CharField(
    # verbose_name=_("secondary city"), blank=True, null=True, max_length=100)
    # secondary_state = models.CharField(
    # verbose_name=_("Secondary state"), blank=True, null=True, max_length=100)
    # default_currency_code = models.CharField(
    # _("default currency code"), blank=True, null=True, max_length=100)
    # bn1 = models.CharField(verbose_name=_(
    # "bn1"), blank=True, null=True, max_length=100)
    # address2 = models.CharField(verbose_name=_(
    # "address 2"), blank=True, null=True, max_length=100)
    # address1 = models.CharField(verbose_name=_(
    # "address 1"), blank=True, null=True, max_length=100)
    # bn2 = models.CharField(verbose_name=_("bn2"), max_length=100)
    # last_name = models.CharField(verbose_name=_(
    # "last name"), blank=True, null=True, max_length=100)
    # follow_up_status = models.CharField(
    #     verbose_name=_("follow up status"), blank=True, null=True, max_length=100)
    # country_code = models.CharField(verbose_name=_("password"),max_length=100)
    # postal_code = models.CharField(verbose_name=_("password"),max_length=100)
    category = models.CharField(verbose_name=_(
        "نوع نقطة الخدمة"),  null=True, max_length=100, choices=CATEGORU,)

    # avatar = models.ImageField(blank=True, null=True, upload_to='images/')
    ACCOUNT_STATUS_CHOICE = (("open", "Open"), ("close", "Close"))
    # name = models.CharField(verbose_name=_(
    #     "Name of Account"), max_length=64, blank=True, null=True,)
    # email = models.EmailField(blank=True, null=True,)
    # industry = models.CharField(
    #     verbose_name=_("Industry Type"), max_length=255, choices=INDCHOICES, blank=True, null=True
    # )
    # type = models.CharField(
    #     verbose_name=_("Users Type"), max_length=255, choices=TYPEUSER, blank=True, null=True
    # )

    def __str__(self):
        return "{0}".format(self.id)

    class Meta:
        managed = True
        verbose_name = _("الفروع و نقاط الخدمة")
        verbose_name_plural = _("نقاط الخدمة ,الفرع")
# class Supplier(BaseModel):
#     secondary_country_code = models.CharField(max_length=100)
#     active_secondary_address = models.BooleanField()
#     # notes = models.CharField(max_length=100)
#     # city = models.CharField(max_length=100)
#     # phone2 = models.CharField(max_length=100)
#     # secondary_name = models.CharField(max_length=100)
#     # phone1 = models.CharField(max_length=100)
#     is_offline = models.BooleanField()
#     language_code = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     staff_id = models.ForeignKey(
#         Staff, on_delete=models.DO_NOTHING, null=True, blank=True)
#     secondary_address2 = models.CharField(max_length=100)
#     bn1_label = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     secondary_address1 = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     secondary_postal_code = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     business_name = models.CharField(max_length=100)
#     secondary_city = models.CharField(max_length=100)
#     secondary_state = models.CharField(max_length=100)
#     default_currency_code = models.CharField(max_length=100)
#     bn1 = models.CharField(max_length=100)
#     address2 = models.CharField(max_length=100)
#     address1 = models.CharField(max_length=100)
#     bn2 = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     follow_up_status = models.CharField(max_length=100)
#     country_code = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=100)
#     bn2_label = models.CharField(max_length=100)
#     supplier_number = models.CharField(max_length=100)
