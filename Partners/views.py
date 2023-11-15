from django.shortcuts import render
from .models import *

# Create your views here.


def PartnersQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Partners.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('-sort_no')
    return queryset
