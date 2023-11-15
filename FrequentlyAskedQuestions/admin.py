from django.contrib import admin
from .models import *
# from liststyle import ListStyleAdminMixin
# from liststyle import ListStyleAdminMixin
# Register your models here.
@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsModelAdmin(admin.ModelAdmin):
    def get_row_css(self, obj, index):
            if obj.is_active_city:
                return 'green'
            return 'red'  # or any color for False
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    readonly_fields = ('Date_Added', 'Date_Update',)

    list_display = ("id","question", "answer",
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
        "id", "question", "answer",
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
    search_fields = ("id", "question", "answer",
                     "Date_Added",
                     "Date_Update", 
                     #   "logo_image", "logo_svg",

                     )

    class Meta:
        model = FrequentlyAskedQuestions


#