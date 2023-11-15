from django.shortcuts import render
from .models import *

# Create your views here.


def ClientsQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Clients.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Update')
    return queryset
