# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ExchangeRate

@admin.register(ExchangeRate)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('region','sale_dolar','buy_dolar','buy_emarat','sale_emarat','buy_ksa','sale_ksa')
    list_filter = ('region',)
    search_fields = ('region',)


# admin.site.register(ExchangeRate)
