from .models import *
# Register your models here.
from django.contrib import admin

from django.utils.translation import gettext_lazy as _

# _register(Branches)# vim: set fileencoding=utf-8 :
from django.contrib import admin


class BranchesAdmin(admin.ModelAdmin):

    list_display = (
        'id',

        'created_at',


        #








        'created_by',



        # 'website',
        # 'description',




        # 'phone1',








        # 'email',
        # 'number_employees',
        'name',




        # 'address2',
        'address1',



        'category',


        'name',
        'phone',


    )
    list_filter = (
        'created_at',







        # 'created_on',
        'created_by',
        #
        # '',
        #
        #
        #
        #
        'id',


        # 'website',
        # 'description',



        # 'phone1',
        'phone',





        # 'email',
        # 'number_employees',
        'name',




        # 'address2',
        'address1',



        'category',


        'name',
        'phone',


    )
    # raw_id_fields = ()
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class=None,):
    admin.site.register(model, admin_class)


_register(Branches, BranchesAdmin)
_register(Address)
