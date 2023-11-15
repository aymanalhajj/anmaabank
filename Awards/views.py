from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



from .models import *



# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com


def AwardsQuerySet():

    queryset = Awards.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')
    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except Awards.DoesNotExist:
        print(" Objectives DoesNotExist ")
    return queryset
    return queryset
