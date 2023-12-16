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
    template = "admin/edit_inline/tabular.html"

    def get_changeform_initial_data(self, request):
        return {'facebook': 'https://www.facebook.com/alinmabankye/',
                'instagram': 'https://www.instagram.com/alinmabankye/',
                'twitter': 'https://www.twitter.com/alinmabankye/',
                'linkedin': 'https://www.linkedin.com/alinmabankye/',
                'youtube': 'https://youtube.com/alinmabankye/',
                'facebook': 'https://www.facebook.com/alinmabankye/',
                "emile": "info@alinmabank.com",
                "whatsapp": "+96702344804",

                "phone_1": "+96702344804",
                "free_phone_numbar": "+9678000060",
                # "phone_1":"+96702344804",
                # "phone_1":"+96702344804",
                }

    def has_add_permission(self, request):

        if SettingModel.objects.all().count() > 0:
            return ("change")
        else:
            #  return ("add" in request.path)
            return ("add")
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
        'name_website_short',
        "name_website",
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
        'is_hidden_sectio_page_all',
        'is_hidden_sectio_page_in_home_only',
        'is_hidden_ourmission',
        'is_hidden_bank_applications',
        'is_hidden_adsence_header',
        'is_hidden_last_news',
        'is_hidden_footer',
        'is_hidden_logo_ainmation',
        'is_hidden_images_portfolio_no_detils',
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
    # list_filter = (
    #     'Date_Update',
    #     'Date_Added',
    #     'is_hidden_branche',
    #     'is_hidden_contact',
    #     'is_hidden_about',
    #     'is_hidden_button_action',
    #     'is_hidden_client',
    #     'is_hidden_galary',
    #     'is_hidden_teams',
    #     'is_hidden_partner',
    #     'is_hidden_ournewsletter',
    #     'is_hidden_imagesportfolionodetils',
    #     'is_hidden_ourmarch',
    #     'is_hidden_sectio_page_all',
    #     'is_hidden_sectio_page_in_home_only',
    #     'is_hidden_ourmission',
    #     'is_hidden_bank_applications',
    #     'is_hidden_adsence_header',
    #     'is_hidden_last_news',
    #     'is_hidden_footer',
    #     'is_hidden_logo_ainmation',
    #     'is_hidden_images_portfolio_no_detils',
    #     'is_hidden_services',
    #     'is_deleted',
    #     'deleted_at',
    #     'deleted_by',
    #     'created_by',
    #     'edited_by',
    #     'created_at',
    #     'edited_at',
    #     'id',
    #     'footer',
    #     'name_website_short',
    #     "name_website",
    #     'facebook',
    #     'telegram',
    #     'twitter',
    #     'instagram',
    #     'linkedin',
    #     'youtube',
    #     'whatsapp',
    #     'phone_1',
    #     'phone_2',
    #     'fax',
    #     'free_phone_numbar',
    #     'emile',
    #     'mail_box',
    #     'short_note',
    # )

    date_hierarchy = 'created_at'
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (

                    'footer',
                    'footer_en',
                    'short_note',

                ),
            },
        ),
        (
            "تحكم بعرض واخفاء الاقسام",
            {
                "classes": ("wide",),
                "fields": (
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
                    'is_hidden_sectio_page_all',
                    'is_hidden_sectio_page_in_home_only',
                    'is_hidden_ourmission',
                    'is_hidden_bank_applications',
                    'is_hidden_adsence_header',
                    'is_hidden_last_news',
                    'is_hidden_footer',
                    'is_hidden_logo_ainmation',
                    'is_hidden_images_portfolio_no_detils',
                    'is_hidden_services',
                ),
            },
        ),
        (
            "روابط ورقام اتصل بنا",
            {
                "classes": ("wide",),
                "fields": (
                    'name_website_short',
                    "name_website",
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
                ),
            },
        ),











    )
    show_full_result_count = False

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             'fax',
    #     'free_phone_numbar',
    #     'emile',
    #     'mail_box'),
    #     }),
    # )
    save_on_top = True


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(SettingModel, SettingModelAdmin)
