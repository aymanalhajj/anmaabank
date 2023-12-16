from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Category)

# admin.site.register(ImagesPortfolioNoDetils)
    # @admin.register(ImagesPortfolioNoDetils)
# class ImagesPortfolioNoDetilsAdmins(admin.ModelAdmin):
#     pass
# admin.register(ImagesPortfolioNoDetils,)
# class ImagesPortfolioNoDetilsAdmin(admin.StackedInline):
#     model = ImagesPortfolioNoDetils
#     extra = 1
# # @admin.register(ImagesPortfolio)
# class ImagesPortfolioAdmins(admin.StackedInline):
#     model = ImagesPortfolio
#     extra = 1
# @admin.register(Portfolio,)
# class ComercialActiviesAdmin(admin.ModelAdmin):
#     inlines = [ImagesPortfolioAdmins]
#     list_display = (
#         "id",
#         "titel",

#         "category",
#         "created_by",
#         "Client",
#         "PhoneNo_one",
#         'PhoneNo_two',

#         # "TypeComercialActiviesSecondary",
#         'PhoneNo_whatsapp',
#         "PhoneNo_landline",
#         "Url_ForProject",
#         "Date_Update",
#         "Date_Added",

#     )
#     list_display_links = (
#         "created_by",
#         "titel",
#         "Client",

#         "PhoneNo_one",
#         'PhoneNo_two',
#         # "TypeComercialActiviesSecondary",
#         'PhoneNo_whatsapp',
#         "PhoneNo_landline",
#         "Url_ForProject",
#         "Date_Update",
#         "Date_Added",
#         "category",


#     )
#     list_editable = ()
#     list_filter = (
#         "titel",
#         "category__name",

#         "category",
#         "Date_Added", "Date_Update", "Client")

#     search_fields = (
#         "category__name",
#         "titel",
#         "category",
#         "created_by",
#         "Client",
#         "PhoneNo_one",
#         'PhoneNo_two',
#         # "TypeComercialActiviesSecondary",
#         'PhoneNo_whatsapp',
#         "PhoneNo_landline",
#         "Url_ForProject",
#         "detial_ar",
#         "Date_Update",
#         "Date_Added",
#     )

#     class Meta:
#         model = Portfolio


admin.site.headers = "بنك الإنماء"
admin.site.site_header = "بنك الإنماء"
admin.site.site_title = "بنك الإنماء"
admin.site.index_title = "بنك الإنماء"
admin.site.name = "بنك الإنماء"
admin.site.su = "بنك الإنماء"
