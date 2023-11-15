from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

import autoslug

# Create your models here.
APP_NAME = "country_regions"


CONTINENT_CHOICES = (
    ('OC', _('أوقيانوسيا')),
    ('EU', _('اوروبا')),
    ('AF', _('افريقيا')),
    ('NA', _('أمريكا الشمالية')),
    ('AN', _('القارة القطبية الجنوبية')),
    ('SA', _('أمريكا الجنوبية')),
    ('AS', _('اسيا')),
)


class Base(models.Model):
    """
    Base model with boilerplate for all models.
    """

    name = models.CharField(verbose_name=_('الاسم انجليزي'),
                            max_length=200, db_index=True, null=True, )
    name_ar = models.CharField(verbose_name=_('الاسم عربي'),
                               max_length=200, db_index=True, null=True, )
    name_ascii = models.CharField(max_length=200, verbose_name=_(
        'الاسم  أسكي'), blank=True, db_index=True)
    slug = autoslug.AutoSlugField(populate_from='name_ascii')
    geoname_id = models.IntegerField(
        null=True, verbose_name=_('المعرف'), blank=True, unique=True)
    alternate_names = models.TextField(
        null=True, blank=True, default='', verbose_name=_('أسماء بديلة'),)
    created_at = models.DateTimeField(
        null=True,  auto_now_add=True, verbose_name=_("تاريخ الانشاء"))
    edit_at = models.DateTimeField(
        null=True, auto_created=True, auto_now=True, verbose_name=_("تاريخ التعديل"))

    class Meta:
        abstract = True
        ordering = ['name_ar']

    def __str__(self):
        display_name_ar = getattr(self, 'display_name_ar', None)
        display_name = getattr(self, 'display_name', None)
        get_display_name_ar = getattr(self, 'get_display_name_ar', None)
        # get_display_name = getattr(self, 'get_display_name', None)

        if display_name_ar:
            return display_name_ar
        # elif get_display_name_ar:
            return get_display_name_ar
        # elif get_display_name:
        #     return get_display_name
        elif display_name:
            return display_name
        return self.name_ar


class Country(Base):
    """
    Base Country model.
    """

    code2 = models.CharField(max_length=2, null=True, blank=True, unique=True)
    code3 = models.CharField(max_length=3, null=True, blank=True, unique=True)
    continent = models.CharField(max_length=2, db_index=True,
                                 choices=CONTINENT_CHOICES, verbose_name=_("القارة"))
    tld = models.CharField(max_length=5, blank=True, db_index=True)
    phone = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name=_("مفتاح التلفون"))

    def __str__(self):
        return '%s , +%s' % (self.name_ar, self.phone)

    class Meta(Base.Meta):
        verbose_name_plural = _('الدول')
        ordering = ['phone']

    def get_display_name_ar(self):
        return '%s, %s , %s' % (self.continent, self.name_ar, self.phone)

    def get_display_name(self):
        return '%s, %s , %s' % (self.continent, self.name, self.phone)


class Region(Base):
    """
    Base Region/State model.
    """
    display_name_ar = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("اسم العرض عربي"))
    display_name = models.CharField(
        max_length=200, verbose_name=_("اسم العرض انجليزي"))
    geoname_code = models.CharField(max_length=50, null=True, blank=True,
                                    db_index=True, verbose_name=_("رمز الاسم الجغرافي"))

    country = models.ForeignKey(APP_NAME + '.Country',
                                verbose_name=_("الدولة"),
                                on_delete=models.CASCADE)

    class Meta(Base.Meta):
        unique_together = (('country', 'name'))
        verbose_name = _('المحافظة/الولاية')
        verbose_name_plural = _('المحافظة/الولاية')
        # verbose_name=""

    def get_display_name_ar(self):
        return '%s, %s' % (self.name_ar, self.country.name_ar)

    def get_display_name(self):
        return '%s, %s' % (self.name, self.country.name)


class Directorate(Base):
    """
    Base Region/State model.
    """
    display_name_ar = models.CharField(max_length=200, null=True, blank=True,)
    display_name = models.CharField(max_length=200)
    geoname_code = models.CharField(max_length=50, null=True, blank=True,
                                    db_index=True)

    region = models.ForeignKey(APP_NAME + '.Region',
                               on_delete=models.CASCADE)

    class Meta(Base.Meta):
        unique_together = (('region', 'name'))
        verbose_name = _('المديرية')
        verbose_name_plural = _('المديرية')
        # verbose_name=""

    def get_display_name(self):
        return '%s, %s, %s' % (self.name, self.region.name, self.region.country.name)

    def get_display_name_ar(self):
        return '%s, %s, %s' % (self.name_ar, self.region.name_ar, self.region.country.name_ar)


class Isolation(Base):
    """
    Base Region/State model.
    """
    display_name_ar = models.CharField(max_length=200, null=True, blank=True,)
    display_name = models.CharField(max_length=200)
    geoname_code = models.CharField(max_length=50, null=True, blank=True,
                                    db_index=True)

    directorate = models.ForeignKey(APP_NAME + '.Directorate',
                                    on_delete=models.CASCADE)

    class Meta(Base.Meta):
        unique_together = (('directorate', 'name'))
        verbose_name = _('العزلة')
        verbose_name_plural = _('العزلة')
        # verbose_name=""

    # def get_display_name(self):
        # return '%s, %s, %s, %s' % (self.name_ar, self.directorate.name_ar,self.directorate.region.name_ar,self.directorate.region.country.name_ar)
    def get_display_name_ar(self):
        return '%s, %s, %s, %s' % (self.name_ar, self.directorate.name_ar, self.directorate.region.name_ar, self.directorate.region.country.name_ar)

    def get_display_name(self):
        return '%s, %s, %s, %s' % (self.name, self.directorate.name, self.directorate.region.name, self.directorate.region.country.name)
