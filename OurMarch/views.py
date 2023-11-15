from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



from .models import *



# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com


def OurMarchQuerySet():

    queryset = OurMarch.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')
    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except OurMarch.DoesNotExist:
        print(" Objectives DoesNotExist ")
    return queryset
