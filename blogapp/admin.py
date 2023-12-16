from django.contrib import admin
from .models import *
# Register your models here.


class ImagesBlogsAdminStackedInline(admin.StackedInline):
    model = ImagesBlogs
    extra = 1


# @admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        "id",
        "name",
        # "logo",
        "Date_Update",
        "Date_Added",

    )
    list_display_links = (
        "id",
        "name",
        # "logo",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = ("Date_Added", "Date_Update",)

    search_fields = ("name", "logo",
                     "Date_Added", "Date_Update",
                     )

    class Meta:
        model = CategoryBlog


class ImagesBlogsAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'date_added', 'date_update', 'blog')
    list_filter = ('date_added', 'date_update', 'blog', 'id', 'image')


@admin.register(Blogs,)
class BlogsAdmin(admin.ModelAdmin):
    inlines = [ImagesBlogsAdminStackedInline]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    autocomplete_fields = [
        # 'category_blog',

    ]
    exclude = ('Date_Added', 'Date_Update', 'created_by',)
    readonly_fields = ('Date_Added', 'Date_Update', "created_by",)

    list_display = (
        "id",
        "category",
        "date_post",
        "image",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "category",
        "date_post",
        "image",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        "id",
        "category",
        "date_post",
        # "image",
        "created_by",
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "category",
        "date_post",

        "detial_ar",
        "created_by",
        "image",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = Blogs


@admin.register(Policies,)
class PoliciesAdmin(admin.ModelAdmin):
    # inlines = [CategoryBlogAdmin]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    # autocomplete_fields = ['ComercialActivie']
    # raw_id_fields = ["category"]
    # list_per_page = sys.mai
    # filter_vertical = ['TypeProdact']
    # list_select_related = ['TypeProdact']
    exclude = ('Date_Added', 'Date_Update', 'created_by',)
    readonly_fields = ('Date_Added', 'Date_Update', "created_by",)

    list_display = (
        "id",
        "category",
        "date_post",
        "image",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "category",
        "date_post",
        "image",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        "id",
        "category",
        "date_post",
        # "image",
        "created_by",
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "category",
        "date_post",

        "detial_ar",
        "created_by",
        "image",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = Policies


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(ImagesBlogs, ImagesBlogsAdmin)
