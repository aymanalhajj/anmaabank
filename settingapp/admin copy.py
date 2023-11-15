# vim: set fileencoding=utf-8 :
from django.contrib import admin

import settingapp.models as models

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from .models import *
import datetime
# Register your models here.

class AdminUserPermissionMixin:
    # def has_view_permission(self, request, obj=None):
    #     return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_module_permission(self, request):
        return request.user.is_superuser

class SettingModelAdmin(admin.ModelAdmin):
    list_per_page = 1

    def has_add_permission(self, request):

        if SettingModel.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return False
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

            # return request.user.is_superuser
    # def has_view_permission(self, request, obj=None):
    #     return request.user.is_superuser

    # def has_add_permission(self, request):
    #     return request.user.is_superuser

    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if not change:
            obj.created_by = request.user
        else:
            obj.deleted_by = request.user
            obj.deleted_at = datetime.datetime.now()

        super().save_model(request, obj, form, change)
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        'id',
        'footer',
        'youtube_url',
        'facebook',
        'telegram',
        'twitter',
        'instagram',
        'linkedin',
        'youtube',
        'whatsapp',
        'phone_1',
        'phone_2',
        'fax',
        'free_phone_numbar',
        'emile',
        'mail_box',
        'Date_Update',
        'Date_Added',
        'is_hidden_adsence_header',
        'is_hidden_branche',
        'is_hidden_contact',
        'is_hidden_about',
        'is_hidden_button_action',
        'is_hidden_client',
        'is_hidden_galary',
        'is_hidden_teams',
        'is_hidden_partner',
        'is_hidden_ournewsletter',
        'is_hidden_imagesportfolionodetils',
        'is_hidden_ourmarch',
        'is_hidden_bank_applications',
        'is_hidden_services',
        'is_deleted',
        'deleted_at',
        'deleted_by',
        'created_by',
        'edited_by',
        'created_at',
        'edited_at',
        'short_note',
    )
    list_filter = (
        'Date_Update',
        'Date_Added',
        'is_hidden_adsence_header',
        'is_hidden_branche',
        'is_hidden_contact',
        'is_hidden_about',
        'is_hidden_button_action',
        'is_hidden_client',
        'is_hidden_galary',
        'is_hidden_teams',
        'is_hidden_partner',
        'is_hidden_ournewsletter',
        'is_hidden_imagesportfolionodetils',
        'is_hidden_ourmarch',
        'is_hidden_bank_applications',
        'is_hidden_services',
        'is_deleted',
        'deleted_at',
        'deleted_by',
        'created_by',
        'edited_by',
        'created_at',
        'edited_at',
        'id',
        'footer',
        'youtube_url',
        'facebook',
        'telegram',
        'twitter',
        'instagram',
        'linkedin',
        'youtube',
        'whatsapp',
        'phone_1',
        'phone_2',
        'fax',
        'free_phone_numbar',
        'emile',
        'mail_box',
        'short_note',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(SettingModel, SettingModelAdmin)
