from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

import country_regions.models as models

from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin


class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'name_ar',

        'name_ascii',
        'created_at',
        'geoname_id',
        'alternate_names',
        'code2',
        "edit_at",
        'code3',
        'continent',
        'tld',
        'phone',
    )
    search_fields = ('name',        'name_ar',
                     )
    # prepopulated_fields = {'slug': ['name']}


class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'name_ar',
        'get_display_name',
        'get_display_name_ar',
        'name_ascii',
        'created_at',
        'geoname_id',
        "edit_at",
        'alternate_names',
        'display_name',
        'display_name_ar',

        'geoname_code',
        'country',


    )
    raw_id_fields = ('country',


                     )
    search_fields = ('name',
                     #  'created_at',
                     'name_ar',
                     )
    # prepopulated_fields = {'slug': ['name']}


class DirectorateAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'name_ar',
        'name_ascii',
        'created_at',
        'geoname_id',
        "edit_at",
        'alternate_names',
        'display_name',
        'display_name_ar',
        'geoname_code',

        'region',
        'get_display_name',
        'get_display_name_ar',
    )
    raw_id_fields = ('region',


                     )
    search_fields = ('name',
                     #  'created_at',
                     'name_ar',
                     )
    # prepopulated_fields = {'slug': ['name']}


class IsolationAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'name_ar',

        'name_ascii',
        'created_at',
        'geoname_id',
        "edit_at",
        'alternate_names',
        'display_name',
        'display_name_ar',

        'geoname_code',
        'directorate',
        'get_display_name',
        'get_display_name_ar'
    )
    raw_id_fields = ('directorate',


                     )
    search_fields = ('name',
                     #  'created_at',
                     'name_ar',
                     )
    # prepopulated_fields = {'slug': ['name']}


def _register(model, admin_class):
    admin.site.register(model, admin_class)
    # erp_admin_site.register(model, admin_class)


_register(models.Country, CountryAdmin)
_register(models.Region, RegionAdmin)
_register(models.Directorate, DirectorateAdmin)
_register(models.Isolation, IsolationAdmin)
