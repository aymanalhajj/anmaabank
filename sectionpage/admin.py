from django.contrib import admin
from .models import SectionPage,SectionPageProperty
from navbarapp.admin import SecondaryNavbarSSectionPageStackAdmin
# Register your models here.
from django.utils.safestring import mark_safe

class SectionPagePropertyAdmin(admin.StackedInline):
    model = SectionPageProperty
    extra = 0


@admin.register(SectionPage,)
class SectionPageAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     super().save_model(request, obj, form, change)
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj, form, change):
        obj.deleted_by = request.user
        super().save_model(request, obj, form, change)
    exclude = ('Date_Added', 'Date_Update',)
    readonly_fields = ('Date_Added', 'Date_Update',
                       'deleted_by',
                       'deleted_at',
                       'render_image',
                       )
    inlines = [SectionPagePropertyAdmin]
    list_display = (
        "id",
        "titel",
        "image",
        "created_by",

        "Date_Update",
        "Date_Added",

        'short_note',
        "created_by",
        'number_rows',
        'view',


        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "Date_Added",
        "Date_Update",

    )
    list_display_links = (
        "id",
        "titel",
        "image",
        "created_by",

       'short_note',
        "created_by",
        'number_rows',
        'view',


        "is_hidden",
        "is_deleted",
        'deleted_by',
        'deleted_at',
        "Date_Added",
        "Date_Update",


    )
    list_editable = ()
    list_filter = (
        # "id",
        # "titel",
        # "image",
        "created_by",
        'number_rows',
        'view',

        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "titel",
        "detial_ar",
        "created_by",
    'number_rows',
        'view',
        "image",
        "Date_Update",
        "Date_Added",
    )
    # readonly_fields = ()


    def render_image(self, obj):
        return mark_safe("""<img src="/images/%s.jpg" />""" % obj.image)
    # def get_exclude(self, request, obj=None):
    #     print(obj.view)

    #     if obj and obj.view == "عمودي":
    #         # When you create new data the obj is None
    #         return ("number_rows", )
    #     return super().get_exclude(request, obj)
    
    # def get_readonly_fields(self, request, obj=None):
    #     print(obj.view)
    #     if obj and obj.view == 'V':
    #         print(obj.view)
    #         # return [""]
    #         return ['number_rows']
    #     else:
    #         return []
    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     if db_field.name == 'V':
    #         kwargs['choices'] = (
    #             ('accepted', 'Accepted'),
    #             ('denied', 'Denied'),
    #         )
    #         if request.user.is_superuser:
    #             kwargs['choices'] += (('ready', 'Ready for deployment'),)
    #     return super().formfield_for_choice_field(db_field, request, **kwargs)

    class Meta:
        model = SectionPage

