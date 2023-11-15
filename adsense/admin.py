from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Adsence)
# admin.site.register(ViewAdcence)
# admin.site.register(AdsenceFooter)
# admin.site.register(ViewAdsenceHeader)
# admin.site.register(ViewAdsenceFooter)
# admin.site.register(PressAdsenceFooter)
# admin.site.register(PressAdsenceHeder)


class AdsenceHederAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'Date_Finish_Posted',

        'Tital_AR',
        'Tital_EN',
        "Description_AR",
        'Description_EN',
        'image',
        "Date_Update",
        'Date_Added',




    )
    list_display_links = (
        'id',
        'Date_Finish_Posted',

        'Tital_AR',
        'Tital_EN',
        "Description_AR",
        'Description_EN',
        'image',
        "Date_Update",
        'Date_Added',


    )
    list_editable = ()
    list_filter = (
        # 'id',

        # 'Tital_AR',
        # 'Tital_EN',
        # # "Description_AR",
        # # 'Description_EN',
        # 'image',
        "Date_Update",
        'Date_Added',
        'Date_Finish_Posted',
    )

    search_fields = (
        'id',

        'Tital_AR',
        'Tital_EN',
        "Description_AR",
        'Description_EN',
        'image',
        "Date_Update",
        'Date_Added',
        'Date_Finish_Posted',
    )

    class Meta:
        model = AdsenceHeder


admin.site.register(AdsenceHeder, AdsenceHederAdmin)
