from django.shortcuts import render

# Create your views here.
from portfolioapp.models import Category, Portfolio, ImagesPortfolio, ImagesPortfolioNoDetils
from .models import *
from .forms import *
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from settingapp.views import SettingModelQuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import messages
from OurNewsletter.forms import OurNewsletterForm
from django.db.models import Q
from settingapp.views import static_content

def getUrl(request):
    if request is None:
        raise Exception("request is None")

    return request.build_absolute_uri()


def CategoryServicesWithServicesNotNullQuerySet():
    queryset = CategoriesServices.objects.filter(
        is_deleted=False, is_hidden=False,
    ).filter(Q(category_services__isnull=False)).distinct().order_by('date_added')
    return queryset


def CategoryServicesQuerySet():
    queryset = CategoriesServices.objects.filter(
        is_deleted=False, is_hidden=False,
    ).order_by('date_added')
    return queryset


def ServicesQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Services.objects.filter(
        is_deleted=False, is_hidden=False,
    ).order_by('Date_Added')

    # try:
    #     if queryset != None:
    #         queryset = queryset.latest('Date_Added')
    # except Services.DoesNotExist:
    #     print(" OurVision DoesNotExist ")
    return queryset


def BankApplicationsQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = BankApplications.objects.filter(
        is_deleted=False,).order_by('Date_Added')

    # try:
    #     if queryset != None:
    #         queryset = queryset.latest('Date_Added')
    # except BankApplications.DoesNotExist:
    #     print(" OurVision DoesNotExist ")
    return queryset

# def BankApplicationsQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    # queryset = BankApplications.objects.filter(
    #     is_deleted=False, is_hidden=False,).order_by('Date_Added')
    # if queryset != None:
    #     queryset = queryset.latest('Date_Added')
    # return queryset


def service_single(request, id, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from anmaabankApp.views import get_cookie

    # if request.method == 'GET':
    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'service-single.html')

    images_services = ImagesServices.objects.filter(service=id)

    dataService = Services.objects.filter(
        is_deleted=False, is_hidden=False,
    )
    # form = ServiceRequestsForm()

    # data = ServiceRequests.objects.all()
    form = ServiceRequestsForm()
    # if request.method == 'POST':

    if request.method == 'POST':
        from OurNewsletter.views import SaveContact
        context = {

        }
        SaveContact(request, "blog.html", context)
        revers_fun = '/service/'+str(id)+'#services-detail'
        # 'اتصل بناء'
        form = ServiceRequestsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            # form.owner = request.user
            # print(form)
            # for forms in form:
            # print(forms)
            form.service = Services.objects.get(id=id)
            cookie = get_cookie(request)
            form.cookie = cookie
            # form.initial['cookie'] = cookie

            form.save()
            messages.success(request, 'تم لإرسال الطلب بنجاح')
            return redirect(revers_fun)
        else:
            messages.error(request, 'خطأ')
            return redirect(revers_fun)
    # formOurNewsletter =
    dataAbout = Services.objects.filter(id=id)

    context = {
        # 'data': data,
        'form': form,
        "section_title_services": "خدمات مشابهة",

        "imagesservice": images_services,
        "titel": "" if dataAbout.first() == None else " خدمة  " if dataAbout.first() == None else " خدمة  " + str(dataAbout.first().titel)
        if dataAbout.first() != None else " Page not found(404) ",
        "title": "" if dataAbout.first() == None else " خدمة  " if dataAbout.first() == None else " خدمة  " + str(dataAbout.first().titel)
        if dataAbout.first() != None else " Page not found(404) ",
        "url": getUrl(request=request),
        # 'ImagesPortfolioss': dataImagesPortfolio,
        # 'FormOurNewsletter': OurNewsletterForm(),
        "ServiceItem": dataService

    }

    # dataImagesPortfolio = ImagesPortfolio.objects.all()
    # context['ImagesPortfolioss'] = dataImagesPortfolio

    # if dataAbout is not None:
    # dataAbout = dataAbout.latest('Date_Added')

    context['services'] = dataAbout.first()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    context["static_content"] = static_content[lang]
    if dataAbout.first().category_services.id ==5:
        return render(request, 'finance-service.html', context)
    return render(request, 'service-single.html', context)


def application_single(request, lang , id):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from anmaabankApp.views import get_cookie
    from settingapp.views import SettingModelQuerySet

    # if request.method == 'GET':
    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'service-single.html')

    # dataImagesPortfolio = ImagesPortfolio.objects.all()

    # dataService = Services.objects.filter(
    #     is_deleted=False,
    # )
    application = BankApplications.objects.filter(
        id=id,  is_deleted=False, is_hidden=False,)

    # data = ServiceRequests.objects.all()
    # form = ServiceRequestsForm()
    if request.method == 'POST':
        revers_fun = '/service/'+str(id)+'#services-detail'
        # 'اتصل بناء'
        form = ServiceRequestsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            # form.owner = request.user
            # print(form)
            # for forms in form:
            # print(forms)
            # form.service = Services.objects.get(id=id)
            cookie = get_cookie(request)
            form.cookie = cookie
            # form.initial['cookie'] = cookie

            form.save()
            messages.success(request, 'تم لإرسال الطلب بنجاح')
            return redirect(revers_fun)
        else:
            messages.error(request, 'خطأ')
            return redirect(revers_fun)
    # formOurNewsletter =

    context = {
        'application': application.first(),
        'applications': BankApplications.objects.all(),

        # 'form': form,
        # 'ImagesPortfolioss': dataImagesPortfolio,
        # 'FormOurNewsletter': OurNewsletterForm(),
        # "ServiceItem": dataService,
        "titel": "" if application.first() == None else " تطبيق  " if application.first() == None else str(application.first().titel)
        if application.first() != None else " Page not found(404) ",
        "title": "" if application.first() == None else " تطبيق  " if application.first() == None else str(application.first().titel)
        if application.first() != None else " Page not found(404) ",
        "url": getUrl(request=request)

    }
    # context['setting'] = SettingModelQuerySet()
    context["applications"] = BankApplicationsQuerySet()

    # dataImagesPortfolio = ImagesPortfolio.objects.all()
    # context['ImagesPortfolioss'] = dataImagesPortfolio

    # dataAbout = Services.objects.get(id=id)
    # if dataAbout is not None:
    # dataAbout = dataAbout.latest('Date_Added')
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    # context['services'] = dataAbout
    context['setting'] = SettingModelQuerySet()

    
    context["static_content"] = static_content[lang]
    return render(request, 'blog-single.html', context)
