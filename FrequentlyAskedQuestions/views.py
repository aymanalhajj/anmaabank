from django.shortcuts import render
import smtplib
import smtplib
import ssl

# Create your views here.
# Create your views here.

from .models import *

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage

# https://myaccount.google.com/apppasswords
# anmaqbank@gmail.com


def FrequentlyAskedQuestionsQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = FrequentlyAskedQuestions.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('sort_no')
    print(len(queryset))
    return queryset
