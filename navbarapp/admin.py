from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
# import autocomplete_all as admin

import navbarapp.models as models


class SecondaryNavbarSSectionPageStackAdmin(admin.StackedInline,):
    # ex = ("title","parent","our_advantages")
    readonly_fields = ("bank_application", "service",
                       "display_at", "column_navbar")
    autocomplete_fields = ['parent', "our_advantages"]

    # readonly_fields = ("bank_application","service")
    # def get_form(self, request, obj=None, **kwargs):
    #     # if obj.type == "1":

    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        try:
            queryset = queryset.exclude(is_deleted=True).filter(
                parent__isnull=True, bank_application__isnull=True, our_advantages__isnull=True,
                service__isnull=True,

            )
        except:
            pass
        results = super().get_search_results(request, queryset, search_term)
        return results
    #     form = super(SecondaryNavbarsStackAdmin, self).get_form(request, obj, **kwargs)
    #     return form
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(models.SecondaryNavbars, self).get_form(request, obj, **kwargs)

    #     if models.SecondaryNavbars.objects.filte(parent__isnull=True).count() > 1:

    #         # this will hide the null option for the parent field
    #         form.base_fields['parent'].empty_label = None

    #     return form
    model = models.Navbars
    # extra = 0
    extra = 1
    max_num = 1
    min_num = 1  # new in Django 1.7
# import SectionPage.models import SectionPage


class SecondaryNavbarserviceackAdmin(admin.StackedInline):
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        try:
            queryset = queryset.exclude(is_deleted=True).filter(
                parent__isnull=True, bank_application__isnull=True, our_advantages__isnull=True,
                service__isnull=True,

            )
        except:
            pass
        results = super().get_search_results(request, queryset, search_term)
        return results
    # ex = ("title","parent","our_advantages")
    readonly_fields = ("bank_application", "our_advantages",
                       "display_at", "column_navbar")
    autocomplete_fields = ['parent']

    # readonly_fields = ("bank_application","service")
    # def get_form(self, request, obj=None, **kwargs):
    #     # if obj.type == "1":

    #     form = super(SecondaryNavbarsStackAdmin, self).get_form(request, obj, **kwargs)
    #     return form
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(models.SecondaryNavbars, self).get_form(request, obj, **kwargs)

    #     if models.SecondaryNavbars.objects.filte(parent__isnull=True).count() > 1:

    #         # this will hide the null option for the parent field
    #         form.base_fields['parent'].empty_label = None

    #     return form
    model = models.Navbars
    # extra = 0
    extra = 1
    max_num = 1
    min_num = 1  # new in Django 1.7
# import SectionPage.models import SectionPage


class SecondaryNavbarsBankApplicationsStackAdmin(admin.StackedInline):
    # ex = ("title","parent","our_advantages")
    readonly_fields = ("service", "our_advantages",
                       "display_at", "column_navbar")
    autocomplete_fields = ['parent']

    # readonly_fields = ("bank_application","service")
    # def get_form(self, request, obj=None, **kwargs):
    #     # if obj.type == "1":
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        try:
            queryset = queryset.exclude(is_deleted=True).filter(
                parent__isnull=True, bank_application__isnull=True, our_advantages__isnull=True,
                service__isnull=True,

            )
        except:
            pass
        results = super().get_search_results(request, queryset, search_term)
        return results
    search_fields = ('titel',)

    #     form = super(SecondaryNavbarsStackAdmin, self).get_form(request, obj, **kwargs)
    #     return form
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(models.SecondaryNavbars, self).get_form(request, obj, **kwargs)

    #     if models.SecondaryNavbars.objects.filte(parent__isnull=True).count() > 1:

    #         # this will hide the null option for the parent field
    #         form.base_fields['parent'].empty_label = None

    #     return form
    model = models.Navbars
    # extra = 0
    extra = 1
    max_num = 1
    min_num = 1  # new in Django 1.7
# import SectionPage.models import SectionPage


class NavbarsAdmin(admin.ModelAdmin):
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(models.Navbars, self).get_form(request, obj, **kwargs)
    search_fields = ('titel',)

    #     if SectionPage.objects.count() > 1:

    #         # this will hide the null option for the parent field
    #         form.base_fields['parent'].empty_label = None

    #     return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj, form, change):
        obj.deleted_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    readonly_fields = ("display_at", "column_navbar")

    list_display = (
        'id',
        'titel',
        'dicript',
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'sort_no',
        'short_note',
    )
    list_filter = (
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'id',
        'titel',
        'dicript',
        'sort_no',
        'short_note',
    )
    date_hierarchy = 'created_at'


class SecondaryNavbarsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # if request.user.groups.filter(
    #     #         bank_application__isnull=True,our_advantages__isnull=True,
    #     #         service__isnull=True,

    #     #     ).exists():
    #     return qs.filter(is_deleted=False).filter(
    #         bank_application__isnull=True,our_advantages__isnull=True,
    #         service__isnull=True,

    #     )
        # return qs
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        try:
            queryset = queryset.exclude(is_deleted=True).filter(
                parent__isnull=True, bank_application__isnull=True, our_advantages__isnull=True,
                service__isnull=True,

            )
        except:
            pass
        results = super().get_search_results(request, queryset, search_term)
        return results
    #     form = super(SecondaryNavbarsStackAdmin, self).get_form(request, obj, **kwargs)
    #     return form
    # def get_form(self, request, obj=None, **kwargs):
    #

    def delete_model(self, request, obj, form, change):
        obj.deleted_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    search_fields = ('titel',)

    list_display = (
        'id',
        'titel',
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'sort_no',
        'short_note',
    )
    list_filter = (
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'id',
        'titel',
        'sort_no',
        'short_note',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


class ColumnNavbarsAdmin(admin.ModelAdmin):
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(models.Navbars, self).get_form(request, obj, **kwargs)

    #     if SectionPage.objects.count() > 1:

    #         # this will hide the null option for the parent field
    #         form.base_fields['parent'].empty_label = None

    #     return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj, form, change):
        obj.deleted_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    search_fields = ('titel',)

    list_display = (
        'id',
        'titel',
        # 'dicript',
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'sort_no',
        'short_note',
    )
    list_filter = (
        'is_hidden',
        'is_deleted',
        'created_by',
        'Date_Update',
        'Date_Added',
        'deleted_at',
        'deleted_by',
        'created_at',
        'edited_at',
        'edited_by',
        'id',
        'titel',
        # 'dicript',
        'sort_no',
        'short_note',
    )
    date_hierarchy = 'created_at'


# _register(models.Navbars, NavbarsAdmin)
# _register(models.SecondaryNavbars, SecondaryNavbarsAdmin)
# _register(models.ColumnNavbars, ColumnNavbarsAdmin)
