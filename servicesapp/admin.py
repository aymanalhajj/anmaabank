# vim: set fileencoding=utf-8 :
from django.contrib import admin

import servicesapp.models as models
import datetime

from navbarapp.admin import SecondaryNavbarserviceackAdmin, SecondaryNavbarsBankApplicationsStackAdmin


class ImagesPortfolioAdmin(admin.StackedInline):
    model = models.ImagesServices
    extra = 1


class FutureBankApplicationsAdmin(admin.StackedInline):
    model = models.FutureApplications
    # extra = 1


class ServicesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if not change:
            obj.created_by = request.user
        else:
            obj.deleted_by = request.user
            obj.deleted_at = datetime.datetime.now()

        super().save_model(request, obj, form, change)
    inlines = [ImagesPortfolioAdmin]
    exclude = ('Date_Added', 'Date_Update', 'created_by', 'name_action',
               'booking_link',
               'phone_whatsapp',
               'phone',)
    readonly_fields = ('Date_Added', 'Date_Update', "created_by", 'name_action',
                       'booking_link',
                       'phone_whatsapp',
                       'phone',)

    # else :
    #  return ("add" in request.path)
    # return request.user.is_superuser
    list_display = (
        'id',
        'titel',
        'titel_en',
        'short_detial',
        # 'detial_ar',
        'image_ar',
        'created_by',

        'Date_Update',
        'Date_Added',
    )
    list_filter = (
        'created_by',
        'Date_Update',
        'Date_Added',
        # 'id',
        # 'titel',
        # 'short_detial',
        # 'detial_ar',
        # 'image',
        # 'name_action',
        # 'booking_link',
        # 'phone_whatsapp',
        # 'phone',
    )


class CategoriesServicesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if not change:
            obj.created_by = request.user
        else:
            obj.deleted_by = request.user
            obj.deleted_at = datetime.datetime.now()

        super().save_model(request, obj, form, change)
    list_display = ('id', 'name','name_en', 'description', 'date_added', 'date_update')
    list_filter = ('date_added', 'date_update',
                   'is_deleted',
                   'is_hidden',

                   'deleted_at',
                   'deleted_by',
                   'created_by',
                   'edited_by',
                   'created_at',
                   'edited_at',
                   )
    search_fields = (
        "id",
        "name",
        "description",
        "date_added",
        "date_update",
    )


class ImagesServicesAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'date_added', 'date_update', 'service')
    list_filter = ('date_added', 'date_update', 'service',

                   #    'short_note',
                   )


class BankApplicationsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if not change:
            obj.created_by = request.user
        else:
            obj.deleted_by = request.user
            obj.deleted_at = datetime.datetime.now()

        super().save_model(request, obj, form, change)
    inlines = [FutureBankApplicationsAdmin]
    list_display = (
        'id',
        'titel',
        # 'detial_ar',
        'logo_image',
        'screen_image',
        'barcode_image',
        'type_choice',
        'google_play',
        'app_store',
        'desketop',
        'website',
        'Date_Update',
        'Date_Added',
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
        'is_deleted',
        'deleted_at',
        'deleted_by',
        'created_by',
        'edited_by',
        'created_at',
        'edited_at',
        # 'id',
        # 'titel',
        # 'detial_ar',
        # 'logo_image',
        # 'screen_image',
        # 'barcode_image',
        'type_choice',
        # 'google_play',
        # 'app_store',
        # 'desketop',
        # 'website',
        # 'short_note',
    )
    search_fields = (
        "id",
        "titel",
        "detial_ar",
        "created_by",
        "screen_image",
        "barcode_image",

        "Date_Update",
        "Date_Added",
    )

    date_hierarchy = 'created_at'


# class FutureApplicationsAdmin(admin.ModelAdmin):

#     list_display = (
#         'id',
#         'name',
#         'date_added',
#         'date_update',
#         'applications',
#     )
#     list_filter = ('date_added', 'date_update', 'applications', 'id', 'name')
#     search_fields = ('name',)


class ServiceRequestsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if SettingModel.objects.all().count() > 0 :
        return ("add" in request.path or "change" in request.path)
    list_display = (
        'id',
        'country',
        'phone_whatsapp',
        'Phone_Number',
        'emile',
        'name',
        'service_application',
        'service',
        'cookie',
        'Message',
        'Date_Update',
        'Date_Added',
    )
    list_filter = (
        'country',
        'service_application',
        'service',
        'Date_Update',
        'Date_Added',
        'id',
        'phone_whatsapp',
        'Phone_Number',
        'emile',
        'name',
        'cookie',
        'Message',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.CategoriesServices, CategoriesServicesAdmin)

_register(models.Services, ServicesAdmin)
_register(models.ImagesServices, ImagesServicesAdmin)
_register(models.BankApplications, BankApplicationsAdmin)
# _register(models.FutureApplications, FutureApplicationsAdmin)
_register(models.ServiceRequests, ServiceRequestsAdmin)
