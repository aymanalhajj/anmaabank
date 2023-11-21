from django.shortcuts import render
from .models import *
# Create your views here.
from navbarapp.views import NavbarsQuerySet,ColumnNavbarsQuerySet

from settingapp.views import SettingModelQuerySet

def SectionPageHomeQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = SectionPage.objects.filter(
        is_deleted=False, is_hidden=False,view="الرئيسية"
        ).order_by('sort_no'
        )
    # .aggregate("our_dvantages_property")
    return queryset
def SectionPagePageQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = SectionPage.objects.filter(
        is_deleted=False, is_hidden=False,view="منفصل").order_by('-sort_no')
    return queryset
def SectionPageAllQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = SectionPage.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('-sort_no')
    return queryset
def section_single(request, id):

    from anmaabankApp.views import get_cookie
    # if request.method == 'GET':
    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'service-single.html')

    # dataImagesPortfolio = ImagesPortfolio.objects.all()

    dataService = SectionPage.objects.filter(

    )
    # form = ServiceRequestsForm()

    # data = SectionPage.objects.all()
    queryset = SectionPage.objects.filter(
        is_deleted=False, is_hidden=False)

    try:
        queryset = queryset.get(id=id)
    except SectionPage.DoesNotExist:
        print(" OurVision DoesNotExist ")
    # return queryset
    context = {
        'section_page': queryset,
        # 'form': form,
        # 'ImagesPortfolioss': dataImagesPortfolio,
        # 'FormOurNewsletter': OurNewsletterForm(),
        # "ServiceItem": dataService

    }

    # dataImagesPortfolio = ImagesPortfolio.objects.all()
    # context['ImagesPortfolioss'] = dataImagesPortfolio

    # dataAbout = Services.objects.get(id=id)
    # if dataAbout is not None:
    # dataAbout = dataAbout.latest('Date_Added')

    context["navbar"] = NavbarsQuerySet()
    # context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    # context['services'] = dataAbout
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    return render(request, 'blog-single.html', context)

