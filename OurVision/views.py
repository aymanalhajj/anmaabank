from django.shortcuts import render


from .models import *


# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com
def ObjectivesQuerySet():
    queryset = Objectives.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')
    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except Objectives.DoesNotExist:
        print(" Objectives DoesNotExist ")
    return queryset
def ValuesQuerySet():
    queryset = Values.objects.filter(is_deleted=False, is_hidden=False,).order_by('Date_Added')
    return queryset
def OurVisionQuerySet():
    queryset = OurVision.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added')
    try:
        if queryset != None:
            queryset = queryset.latest('Date_Added')
    except OurVision.DoesNotExist:
        print(" OurVision DoesNotExist ")
    return queryset

def OurStartupQuerySet():
    queryset = OurStartup.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('Date_Added').first()
    # try:
    #     if queryset != None:
    #         queryset = queryset.latest('Date_Added')
    # except OurVision.DoesNotExist:
    #     print(" OurVision DoesNotExist ")
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