from django.contrib import admin
from django.contrib import admin
from .models import *
import datetime
# Register your models here.

from OurMarch.models import *
from OurMission.models import *

@admin.register(OurVision,)
class OurVisionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if OurVision.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
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
        "id",

        "detial_ar",
        "Date_Update",
        "Date_Added",
        'short_note',

        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )
    list_display_links = (
        "id",
        "detial_ar",
        "Date_Added",
        "Date_Update",
        'short_note',
        "is_hidden",
        "is_deleted",
        "created_by",
        'deleted_by',
        'deleted_at',

    )
    list_editable = ()
    list_filter = (

        "Date_Update",
        "Date_Added",
        'short_note',
        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )

    search_fields = (
        "id",

        "detial_ar",
        "created_by",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = OurVision


@admin.register(Values)
class ValuesAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Values.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
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
        "id",

        "detail_ar",
        "Date_Update",
        "Date_Added",
        'short_note',

        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )
    list_display_links = (
        "id",
        "detail_ar",
        "Date_Added",
        "Date_Update",
        'short_note',
        "is_hidden",
        "is_deleted",
        "created_by",
        'deleted_by',
        'deleted_at',

    )
    list_editable = ()
    list_filter = (

        "Date_Update",
        "Date_Added",
        'short_note',
        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )

    search_fields = (
        "id",

        "detail_ar",
        "created_by",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = Values



@admin.register(Objectives,)
class ObjectivesAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Objectives.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
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
        "id",

        "detial_ar",
        "Date_Update",
        "Date_Added",
        'short_note',

        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )
    list_display_links = (
        "id",
        "detial_ar",
        "Date_Added",
        "Date_Update",
        'short_note',
        "is_hidden",
        "is_deleted",
        "created_by",
        'deleted_by',
        'deleted_at',

    )
    list_editable = ()
    list_filter = (

        "Date_Update",
        "Date_Added",
        'short_note',
        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )

    search_fields = (
        "id",

        "detial_ar",
        "created_by",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = Objectives


# @admin.register(OurVision,)
# class OurVisionAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         obj.created_by = request.user
#         super().save_model(request, obj, form, change)
#     # inlines = [ImagesPortfolioAdmin]
#     list_display = (
#         "id",

#         "created_by",

#         "Date_Update",
#         "Date_Added",


#     )
#     list_display_links = (
#         "id",

#         "created_by",

#         "Date_Update",
#         "Date_Added",


#     )
#     list_editable = ()
#     list_filter = (
#         "id",

#         "created_by",
#         "Date_Update",
#         "Date_Added"
#     )

#     search_fields = (
#         "id",

#         "detial_ar",
#         "created_by",

#         "Date_Update",
#         "Date_Added",
#     )

#     class Meta:
#         model = OurVision


# @admin.register(About,)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     if not change:
    #         obj.created_by = request.user
    #     else:
    #         obj.deleted_by = request.user
            # obj.deleted_at = datetime.datetime.now()
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        "id",
        "titel",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "titel",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        "id",
        "titel",
        "image",
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "titel",
        "detial_ar"
        "image",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = About



@admin.register(MassegeAbout,)
class MassegeAboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MassegeAbout.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     if not change:
    #         obj.created_by = request.user
    #     else:
    #         obj.deleted_by = request.user
    #         obj.deleted_at = datetime.datetime.now()
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        "id",
        "title",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "title",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "title",
        "detail_ar"
        "image",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = MassegeAbout




@admin.register(OurStartup,)
class OurStartupAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if OurStartup.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     if not change:
    #         obj.created_by = request.user
    #     else:
    #         obj.deleted_by = request.user
    #         obj.deleted_at = datetime.datetime.now()
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        "id",
        "title",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "title",
        "image",
        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "title",
        "detail_ar"
        "image",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = OurStartup

# @admin.register(OurMarch,)
class OurMarchAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request):
        # return ("add" in request.path or "change" in request.path)
    def has_add_permission(self, request):
        if OurMarch.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return False
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
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
        "id",

        "detial_ar",
        "Date_Update",
        "Date_Added",
        'short_note',

        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )
    list_display_links = (
        "id",
        "detial_ar",
        "Date_Added",
        "Date_Update",
        'short_note',
        "is_hidden",
        "is_deleted",
        "created_by",
        'deleted_by',
        'deleted_at',

    )
    list_editable = ()
    list_filter = (

        "Date_Update",
        "Date_Added",
        'short_note',
        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )

    search_fields = (
        "id",

        "detial_ar",
        "created_by",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = OurMarch




# @admin.register(OurMission,)
class OurMissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MassegeAbout.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            #  return ("add" in request.path)
            return ("add")
           # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
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
        "id",

        "detial_ar",
        "Date_Update",
        "Date_Added",
        'short_note',

        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )
    list_display_links = (
        "id",
        "detial_ar",
        "Date_Added",
        "Date_Update",
        'short_note',
        "is_hidden",
        "is_deleted",
        "created_by",
        'deleted_by',
        'deleted_at',

    )
    list_editable = ()
    list_filter = (

        "Date_Update",
        "Date_Added",
        'short_note',
        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "created_by",

    )

    search_fields = (
        "id",

        "detial_ar",
        "created_by",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = OurMission
