from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



from .models import *



# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com

def SettingModelQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = SettingModel.objects.filter(
        is_deleted=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except SettingModel.DoesNotExist:
        print(" OurVision DoesNotExist ")
    return queryset

# def SettingModelQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    # queryset = SettingModel.objects.filter(
    #     is_deleted=False, is_hidden=False,).order_by('Date_Added')
    # if queryset != None:
    #     queryset = queryset.latest('Date_Added')
    # return queryset
