from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Teams)
from django.contrib import admin
from .models import *

# Register your models here.


# @admin.register(Teams)
class TeamsModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    readonly_fields = ('Date_Added', 'Date_Update',)

    list_display = ("id", "full_name", "image",
                    "sort_no",
                    'short_note',

                    "is_hidden",
                    "is_deleted",
                    'deleted_by',
                    'deleted_at',
                    "Date_Added",
                    "Date_Update",
                    )

    list_display_links = (
        "id", "full_name", "image",
        "sort_no",
        'short_note',


        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "Date_Added",
        "Date_Update",
    )
    list_editable = ()
    list_filter = ("Date_Added", "Date_Update",

                   )
    search_fields = ("id", "full_name", "image",
                     "Date_Added",
                     "Date_Update",
                     #   "logo_image", "logo_svg",

                     )

    class Meta:
        model = Teams


#
