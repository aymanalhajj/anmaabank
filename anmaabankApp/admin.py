from django.contrib import admin
from .models import *


# @admin.register(RequestMetaAndGet,)
class RequestMetaAndGetAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if SettingModel.objects.all().count() > 0 :
        return ("add" in request.path or "change" in request.path)
    # inlines = [ImagesPortfolioAdmin]
    exclude = ('Date_Added', 'Date_Update',
               #    'datajson', "cookie",
               #    "CONTENT_LENGTH", "CONTENT_TYPE",
               #    "HTTP_ACCEPT", "HTTP_ACCEPT_ENCODING",
               #    "HTTP_ACCEPT_LANGUAGE", "HTTP_REFERER",
               #    "HTTP_USER_AGENT", "HTTP_HOST",
               )
    readonly_fields = ('Date_Added', 'Date_Update',
                       'datajson', "cookie",
                       "CONTENT_LENGTH", "CONTENT_TYPE",
                       "HTTP_ACCEPT", "HTTP_ACCEPT_ENCODING",
                       "HTTP_ACCEPT_LANGUAGE", "HTTP_REFERER",
                       "HTTP_USER_AGENT", "HTTP_HOST",
                       "PATH", "QUERY_STRING",
                       "REMOTE_ADDR", "REMOTE_HOST",
                       "REMOTE_USER", "REQUEST_METHOD",
                       "SERVER_NAME", "SERVER_PORT",
                       "GET", "encoding",
                       "COOKIES", "ip_info",
                       "datajsonGet", "cookie"

                       )

    list_display = (
        "id",
        "datajson",
        'ip_info',
        # "latitude",
        # "longitude",

        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "datajson",
        'ip_info',
        # "latitude",
        # "longitude",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        # "id",
        "cookie",

        # "latitude",
        # "longitude",

        "Date_Update",
        "Date_Added",
    )

    search_fields = (
        # "id",
        "datajson",
        # "latitude",
        # "longitude",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = RequestMetaAndGet


# @admin.register(RequestHederInfo,)
class RequestHederInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if SettingModel.objects.all().count() > 0 :
        return ("add" in request.path or "change" in request.path)
    # inlines = [ImagesPortfolioAdmin]
    exclude = ('Date_Added', 'Date_Update', 'datajson',
               "cookie", "latitude", "longitude")
    readonly_fields = ('Date_Added', 'Date_Update',
                       'datajson', "cookie", "latitude", "longitude")
    list_display = (
        "id",
        "datajson",
        "ip_info",
        "latitude",
        "longitude",

        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "datajson",
        'ip_info',
        "latitude",
        "longitude",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        # "id",
        "cookie",
        # "latitude",
        # "longitude",

        # "Date_Update",
        "Date_Added",
    )

    search_fields = (
        "id",
        "datajson",
        "latitude",
        "longitude",

        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = RequestHederInfo

# Register your models here.


# @admin.register(IpInfo,)
class IpInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if SettingModel.objects.all().count() > 0 :
        return ("add" in request.path or "change" in request.path)
        # if SettingModel.objects.all().count() > 0 :
    exclude = ('id',

               "ip",
               "screen",
               "country",
               "countryCode",
               "timezone",
               "city",
               'regionCode',
               'regionName',
               "isp",
               "org",
               "asn",
               'zip',
               "latitude",
               "url_google_map_location",
               "longitude",


               "Date_Update",
               "Date_Added",

               )
    readonly_fields = ('id',

                       "ip",
                       "screen",
                       "country",
                       "countryCode",
                       "timezone",
                       "city",
                       "url_google_map_location",
                       'regionCode',
                       'regionName',
                       "isp",
                       "org",
                       "asn",
                       'zip',
                       "latitude",
                       "longitude",


                       "Date_Update",
                       "Date_Added",

                       )
    list_display = (
        "id",
        "ip",
        "screen",
        "url_google_map_location",

        "country",
        "countryCode",
        "timezone",
        "city",
        'regionCode',

        # "TypeComercialActiviesSecondary",
        'regionName',
        "isp",
        "org",
        "asn",


        'zip',
        "latitude",
        "longitude",


        "Date_Update",
        "Date_Added",

    )
    list_display_links = (
        "id",
        "ip",
        "screen",
        # "url_google_map_location",
        "country",
        "countryCode",
        "timezone",
        "city",
        'regionCode',

        # "TypeComercialActiviesSecondary",
        'regionName',
        "isp",
        "org",
        "asn",


        'zip',
        "latitude",
        "longitude",


        "Date_Update",
        "Date_Added",



    )
    list_editable = ()
    list_filter = (
        # "id",
        # "ip",

        "country",
        "countryCode",
        # "timezone",
        "city",
        'regionCode',
        # "screen",

        # "TypeComercialActiviesSecondary",
        'regionName',
        # "isp",
        # "org",
        # "asn",


        # 'zip',
        # "latitude",
        # "longitude",


        # "Date_Update",
        "Date_Added",
    )

    search_fields = (
        "id",
        "ip",
        "screen",

        "country",
        "countryCode",
        "timezone",
        "city",
        'regionCode',

        # "TypeComercialActiviesSecondary",
        'regionName',
        "isp",
        "org",
        "asn",


        'zip',
        "latitude",
        "longitude",


        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = IpInfo


# class ImagesPortfolioAdmin(admin.StackedInline):
#     model = ImagesPortfolio
#     extra = 1


# @admin.register(Portfolio,)
# class ComercialActiviesAdmin(admin.ModelAdmin):
#     inlines = [ImagesPortfolioAdmin]
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


# @admin.register(PortfolioNoDetils,)
# class PortfolioNoDetilsAdmin(admin.ModelAdmin):
#     inlines = [ImagesPortfolioNoDetilsAdmin]
#     list_display = (
#         "id",
#         "titel",

#         "category",
#         "created_by",

#         "Date_Update",
#         "Date_Added",

#     )
#     list_display_links = (
#         "id",
#         "created_by",
#         "titel",


#         "Date_Update",
#         "Date_Added",
#         "category",


#     )
#     list_editable = ()
#     list_filter = (
#         "id",
#         "titel",
#         "category__name",

#         "category",
#         "Date_Added", "Date_Update")

#     search_fields = (
#         "id",
#         "category__name",
#         "titel",
#         "category",
#         "created_by",

#         "Date_Update",
#         "Date_Added",
#     )

#     class Meta:
#         model = PortfolioNoDetils



# @admin.register(ServiceVIP,)
# class ServiceVIPAdmin(admin.ModelAdmin):
#     # inlines = [ImagesPortfolioAdmin]
#     list_display = (
#         "id",
#         "titel",
#         "image",
#         "created_by",

#         "Date_Update",
#         "Date_Added",


#     )
#     list_display_links = (
#         "id",
#         "titel",
#         "image",
#         "created_by",

#         "Date_Update",
#         "Date_Added",


#     )
#     list_editable = ()
#     list_filter = (
#         "id",
#         "titel",
#         "image",
#         "created_by",
#         "Date_Update",
#         "Date_Added"
#     )

#     search_fields = (
#         "id",
#         "titel",
#         "detial_ar",
#         "created_by",
#         "image",
#         "Date_Update",
#         "Date_Added",
#     )

#     class Meta:
#         model = ServiceVIP

@admin.register(Statistics,)
class StatisticsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    # inlines = [ImagesPortfolioAdmin]
    list_display = (
        "id",
        "titel",
        "number",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_display_links = (
        "id",
        "titel",
        "number",
        "created_by",

        "Date_Update",
        "Date_Added",


    )
    list_editable = ()
    list_filter = (
        # "id",
        # "titel",
        # "image",
        "created_by",
        "Date_Update",
        "Date_Added"
    )

    search_fields = (
        "id",
        "titel",
        "detial_ar",
        "created_by",
        "number",
        "Date_Update",
        "Date_Added",
    )

    class Meta:
        model = Statistics


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # inlines = [ImagesPortfolioAdmin]
#     list_display = (
#         "id",
#         "name",

#         "Date_Update",
#         "Date_Added",

#     )
#     list_display_links = (
#         "id",
#         "name",

#         "Date_Update",
#         "Date_Added",


#     )
#     list_editable = ()
#     list_filter = ("id", "name",
#                    "Date_Added", "Date_Update",)

#     search_fields = ("name",
#                      "Date_Added", "Date_Update",
#                      )

#     class Meta:
#         model = Category


# @admin.register(ImagesPortfolio)
# class ImagesPortfolioAdmins(admin.ModelAdmin):
#     pass
admin.site.headers = "بنك الإنماء"
admin.site.site_header = "بنك الإنماء"
admin.site.site_title = "بنك الإنماء"
admin.site.index_title = "بنك الإنماء"
admin.site.name = "بنك الإنماء"
admin.site.su = "بنك الإنماء"
