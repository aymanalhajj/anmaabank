# vim: set fileencoding=utf-8 :
from django.contrib import admin

import OurNewsletter.models as models


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'country',
        'phone_whatsapp',
        'Phone_Number',
        'name',
        'emile',
        'Message',
        'Date_Update',
        'Date_Added',
    )
    list_filter = (
        'country',
        'Date_Update',
        'Date_Added',
        'id',
        'phone_whatsapp',
        'Phone_Number',
        'name',
        'emile',
        'Message',
    )
    search_fields = ('name',)


class OurNewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'emile', 'Date_Update', 'Date_Added')
    list_filter = ('Date_Update', 'Date_Added', 'id', 'emile')




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.OurNewsletter, OurNewsletterAdmin)

