from django.shortcuts import render
from .forms import *
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from SendEmile.views import *
from servicesapp.models import Services
# from ouradvantages.views import SectionPageHomeQuerySet,OurAdvantagesPageQuerySet
from settingapp.views import SettingModelQuerySet
# from branches.views import BranchesHederQuerySet
from navbarapp.views import NavbarsQuerySet,ColumnNavbarsQuerySet
from settingapp.views import SettingModelQuerySet
# from blogapp.views import BlogsHomeListView
# from OurMarch.views import OurMarchQuerySet
from servicesapp.views import BankApplicationsQuerySet

def SaveContact(request,name_page,context):

    if request.method == 'POST':
        revers_fun = '/#contact'
        'اتصل بناء'

        form = ContactForm(request.POST, request.FILES)
        formOurNewsletterForm = OurNewsletterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            messages.success(request, 'تم الإضافة بنجاح')
            return redirect(revers_fun)

        elif formOurNewsletterForm.is_valid():
            revers_fun = '/#footer'
            # print(formOurNewsletterForm)
            # emile = formOurNewsletterForm["emile"].value
            # print(request.POST["emile"])
            # print(formOurNewsletterForm["emile"].value)

            formOurNewsletterForm.save()
            emile = request.POST["emile"]

            messages.success(request, 'تم الحفظ بنجاح')
            sendEmileForSubScripeNew(emile)
            # return render(request, name_page, context)

        else:
            # if name_model == Task3:
            #     form.save(commit=False)
            messages.error(request, 'البريد متوفر من سابق')
            # return redirect(name_page+revers_fun)
    # statistic = Statistics.objects.all()



