from django.shortcuts import render


from .models import *


# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com
def ObjectivesQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Objectives.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except Objectives.DoesNotExist:
        print(" Objectives DoesNotExist ")
    return queryset

def OurVisionQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = OurVision.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except OurVision.DoesNotExist:
        print(" OurVision DoesNotExist ")
    return queryset
def AboutQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = About.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except About.DoesNotExist:
        print(" About DoesNotExist ")
    return queryset
def MassegeAboutQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = MassegeAbout.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')

    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except MassegeAbout.DoesNotExist:
        print(" MassegeAbout DoesNotExist ")
    return queryset