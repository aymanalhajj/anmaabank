# -*- coding: utf-8 -*-

from six import python_2_unicode_compatible
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _

# from .managers import CurrencyManager




class ExchangeRate(models.Model):
	# exchange_rate_id = models.AutoField(primary_key=True)
	# name = models.CharField(max_length=100,choices=[("$", "دولار"), ("2", "سعودي"), ("3", "اماراتي")],)
    region = models.CharField(max_length = 200, verbose_name=_('المحافظة'),default = "عدن")
    sale_dolar = models.IntegerField(_(' سعر البيع للدولار'), null=True,)
    buy_dolar = models.IntegerField(_(' سعر الشراء للدولار'), null=True,)
    buy_emarat = models.IntegerField(_(' سعر الشراء اماراتي'), null=True,)
    sale_emarat = models.IntegerField(_(' سعر البيع اماراتي'), null=True,)
    buy_ksa = models.IntegerField(_(' سعر الشراء سعودي'), null=True,)
    sale_ksa = models.IntegerField(_(' سعر البيع سعودي'), null=True,)
    

    class Meta:
        db_table = ""
        managed = True
        verbose_name = _("اسعار الصرف")
        verbose_name_plural = _("اسعار الصرف")

    # city = models.CharField(max_length=100,choices=CITY_CHOICES,)

	# basetable_id = models.ForeignKey(City, on_delete=models.CASCADE)
	
