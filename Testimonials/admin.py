from django.contrib import admin
from .models import *
# Register your models here.


# @admin.register(Testimonials)
class TestimonialsModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    readonly_fields = ('Date_Added', 'Date_Update', 'deleted_by',
                       'deleted_at',)

    list_display = ("id", "full_name", "detial_ar",
                    "sort_no",
                    "created_by",
                    'short_note',

                    "is_hidden",
                    "is_deleted",
                    'deleted_by',
                    'deleted_at',
                    "Date_Added",
                    "Date_Update",
                    )

    list_display_links = (
        "id", "full_name",  "detial_ar",
        "sort_no",
        'short_note',
        "created_by",


        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "Date_Added",
        "Date_Update",
    )
    list_editable = ()
    list_filter = ("Date_Added", "Date_Update", "created_by",


                   )
    search_fields = ("id", "full_name", "detial_ar",
                     "Date_Added",
                     "Date_Update",
                     #  "created_by",
                     #   "logo_image", "logo_svg",

                     )

    class Meta:
        model = Testimonials


#
