from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.


def islogin(request):
    if request.session.has_key('userLoggedName') and request.session.has_key('userLoggedEmailId'):
        return True
    else:
        return False

def login_out_toggle(request):
    if islogin(request):
        return "userLogout"
    else:
        return "login"
    

def getSwitchLangUrl(request):
    if request is None:
        raise Exception("request is None")
    url = request.build_absolute_uri()
    if '/ar' in url:
        url = url.replace('/ar','/en')
    elif 'en' in url:
        url = url.replace('/en','/ar')
    return url


def NavbarsQuerySetOld():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Navbars.objects.filter(

        is_deleted=False, is_hidden=False, parent__isnull=True,
    ).order_by('-sort_no').filter(Q(parent__bank_application__isnull=True) | Q(parent__service__isnull=True) | Q(parent__our_advantages__isnull=True),)
    # return queryset.filter(Q(Q(parent__bank_application__isnull=False ) | Q(parent__service__isnull=False))|
    #                           Q(parent__our_advantages__isnull=True)
    #                         &
    #                         Q(display_at="navbar")

    #                        )
    return queryset


def NavbarsQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    # queryset = Navbars.objects.filter(
    from servicesapp.views import ServicesQuerySet, BankApplicationsQuerySet, CategoryServicesWithServicesNotNullQuerySet
    from sectionpage.views import SectionPageAllQuerySet
    # is_deleted=False, is_hidden=False,parent__isnull=True,
    # ).order_by('-sort_no').filter(Q(parent__bank_application__isnull=True)|Q(parent__service__isnull=True)|Q(parent__our_advantages__isnull=True),)
    context = {
        'servicess': ServicesQuerySet(),
        'bank_applications': BankApplicationsQuerySet(),
        'section': SectionPageAllQuerySet(),
        'categories_services': CategoryServicesWithServicesNotNullQuerySet(),

    }
    # context['categories_services'] = CategoryServicesQuerySet()

    return context
# Create your views here.


def ColumnNavbarsQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = ColumnNavbars.objects.filter(
        is_deleted=False, is_hidden=False).order_by('-sort_no')
    return queryset

# def SecondaryNavbarsQuerySet():
#     # current_datetime = datetime.datetime.now().date()
#     # print(current_datetime)
#     queryset = SecondaryNavbars.objects.filter(
#         is_deleted=False, is_hidden=False,).order_by('-sort_no')
#     return queryset
