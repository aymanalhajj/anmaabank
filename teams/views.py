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


def sendEmile():
    safarcallme = "anmaqbank@gmail.com"

    sender = 'anmaqbank@gmail.com'
    receivers = ['ibrahim.alzoriqi@gmail.com']
    title = "Here is the message."
    message = """From: From Person <anmaqbank@gmail.com>
    To: To Person <ibrahim.alzoriqi@gmail.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    msg = EmailMessage(
        title,
        message,
        # "Hello",
        # "Body goes here",
        sender,
        receivers,
        receivers,
        reply_to=receivers,
        headers={"Message-ID": "foo"},
    )
    msg.send()

    send_mail(
        title,
        message,
        sender,
        receivers,
        fail_silently=False,
    )
   # try:
   # smtpObj = smtplib.SMTP('localhost')
   # smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
    # except SMTPException:
    # print( "Error: unable to send email")


def TeamsQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Teams.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('sort_no')
    return queryset
