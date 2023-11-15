from django.contrib import admin

# Register your models here.


# def sendEmile():
#     safarcallme = "anmaqbank@gmail.com"

#     sender = 'anmaqbank@gmail.com'
#     receivers = ['ialzoriqi@gmail.com']
#     title = "Here is the message."
#     message = """From: From Person <anmaqbank@gmail.com>
#     To: To Person <ialzoriqi@gmail.com>
#     Subject: SMTP e-mail test

#     This is a test e-mail message.
#     """

#     msg = EmailMessage(
#         title,
#         message,
#         # "Hello",
#         # "Body goes here",
#         sender,
#         receivers,
#         receivers,
#         reply_to=receivers,
#         headers={"Message-ID": "foo"},
#     )
#     msg.send()

#     send_mail(
#         title,
#         message,
#         sender,
#         receivers,
#         fail_silently=False,
#     )
#    # try:
#    # smtpObj = smtplib.SMTP('localhost')
#    # smtpObj.sendmail(sender, receivers, message)
#     print("Successfully sent email")
#     # except SMTPException:
#     # print( "Error: unable to send email")
