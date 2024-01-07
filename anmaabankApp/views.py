from django.shortcuts import render
from .models import *
from django.http import FileResponse
import os
from django.utils.timezone import localtime, now
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import messages
from django.core.paginator import Paginator
import requests
from . models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from portfolioapp.models import Category, Portfolio, ImagesPortfolio, ImagesPortfolioNoDetils
from django.db.models import Q  # new
from django.views.generic import TemplateView, ListView
from io import StringIO
from django.views import generic
from OurVision.models import About
from adsense.views import AdsenceHederQuerySet
# context[''] = ClientsQuerySet()
from clients.views import *
from servicesapp.views import BankApplicationsQuerySet
from teams.views import *
from OurNewsletter.models import *
from OurNewsletter.forms import *
from OurNewsletter.views import *
from SendEmile.views import *
# FrequentlyAskedQuestionsQuerySet
from FrequentlyAskedQuestions.views import *
from Testimonials.views import *
from OurVision.views import *
from OurMission.views import *
from Partners.views import *
from servicesapp.models import Services
from sectionpage.views import SectionPageHomeQuerySet, SectionPagePageQuerySet
from settingapp.views import SettingModelQuerySet
from branches.views import BranchesHederQuerySet
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from settingapp.views import SettingModelQuerySet
from blogapp.views import BlogsHomeListView
from OurMarch.views import OurMarchQuerySet
from django.shortcuts import render, get_object_or_404
# from django.core.u import resolve

from currencies.views import getCurancy

from settingapp.views import static_content


def getSwitchLangUrl(request):
    if request is None:
        raise Exception("request is None")
    url = request.build_absolute_uri()
    if '/ar' in url:
        url = url.replace('/ar','/en')
    elif '/en' in url:
        url = url.replace('/en','/ar')
    else:
        url = url+'ar'
    return url

def getUrl(request):
    if request is None:
        raise Exception("request is None")

    return request.build_absolute_uri()


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
    

def set_test_cookie(request, render, key_cookies):
    render.set_cookie("sessionid", key_cookies,
                      max_age=10000000, expires=10000000)
    request.session['session_cookies'] = key_cookies


def page_not_found(request, exception=None):
    return HttpResponseRedirect("/")
# def page_not_found(request, exception, template_name='404.html'):
    # return redirect('/')


def bad_request(request, exception=None, template_name='404.html'):
    return redirect('/')


def permission_denied(request, exception, template_name='404.html'):
    return redirect('/')


def server_error(request, exception, template_name='404.html'):
    return redirect('/')


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')  # or redirect('name-of-index-url')


def check_cookie(request, render, key_cookies):
    # print(request.COOKIES.get('csrftoken'))
    # # print(request.session['session_cookies'])
    cookis = request.COOKIES.get('sessionid')
    # print(request.COOKIES.get('cookies'))
    # print(cookis)
    # session = request.session()
    if cookis != None:
        # print(request.session.get('sessionid'))
        request.session.set_expiry(10000000)

        # render.cookies['cookies']['expires'] = datetime.today() + \
        #     timedelta(days=1000)
        # render.cookies['cookies']['expires'] = datetime.today() + \
        #     timedelta(days=1000)
        # request.session.delete_test_cookie()
        # print(request.session.get_session_cookie_age())

        cookis = request.COOKIES.get('sessionid')

    else:
        set_test_cookie(request, render, key_cookies)
        # render.updte.set_expiry(10000000)
        request.session.set_expiry(10000000)
    # print(request.COOKIES.get('cookies'))
    # print(request.COOKIES)
    # request.COOKIES['cookies']['expires'] = 10000000

    cookis = request.COOKIES.get('sessionid')

    # response = HttpResponse(
    #     "Dataflair <br> Your browser doesnot accept cookies")
    return cookis


def get_cookie(request):
    import random
    import string
    rend = HttpResponse(request, 'index.html')
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(100))
    req = request

    sessi = check_cookie(req, rend, result_str)
    if sessi == None:
        sessi = result_str
        set_test_cookie(req, rend, result_str)
        sessi = check_cookie(req, rend, result_str)
    return sessi


def get_clients_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_clients_ipss(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def saveInfoIp(request, screen):
    if request.method == 'GET':
        cookie = get_cookie(request)

        try:
            response = requests.get(
                'http://ip-api.com/json/{0}'.format(get_clients_ip(request))).json()

            result = {}
            result = response
            print(type(result))
            print(result)

            # print(result)
            if result['status'] != 'fail':
                ip_info = IpInfo.objects.create(
                    status=result['status'],
                    ip=result['query'],
                    latitude=result['lat'],
                    longitude=result['lon'],
                    isp=result['isp'],
                    screen=screen,
                    url_google_map_location="https://www.google.com/maps?q=" +
                    str(result['lat'])+","+str(result['lon']),
                    cookie=cookie,
                    COOKIES=cookie,
                    regionCode=result['region'],
                    countryCode=result['countryCode'],
                    country=result['country'],
                    regionName=result['regionName'],
                    city=result['city'],
                    zip=result['zip'],
                    timezone=result['timezone'],
                    asn=result['as'],
                    org=result['org'],
                )
                saveInfoReqestHeder(request, screen, cookie, ip_info)
            else:
                ip_info = IpInfo.objects.create(ip=result['query'],
                                                status=result['status'],

                                                #   latitude=result['lat'],
                                                #   longitude=result['lon'],
                                                #   isp=result['isp'],
                                                screen=screen,
                                                cookie=cookie,
                                                COOKIES=cookie,
                                                #   regionCode=result['region'],
                                                #   countryCode=result['countryCode'],
                                                #   country=result['country'],
                                                #   regionName=result['regionName'],
                                                #   city=result['city'],
                                                #   zip=result['zip'],
                                                #   timezone=result['timezone'],
                                                #   asn=result['as'],
                                                #   org=result['org'],
                                                )
                saveInfoReqestHeder(request, screen, cookie, ip_info)

        except ValueError as e:
            print("ValueError "+str(e))
        except requests.exceptions.ConnectionError as e:
            print("requests exceptions ConnectionError "+str(e))
        except Exception as e:
            print("requests exception  "+str(e))


def saveInfoReqestHeder(request, fromUrl, cookie, ip_info):
    print(request.META)
    # print(request.path)
    # print(request.META)
    # print(type(request.META))
    # print(type(request.headers))
    # print(request.method)
    # print("path")
    # print(request.headers)
    import json

    # for jjjj in request.META:
    # print(jjjj)

    # print(
    # json.dumps(request.GET)
    # )

    try:
        data_json = request.META
        my_dictss = {
            # 'body': request,
            'fromUrl': fromUrl,
            "Meta": str(request.META)
            # "META": request.META.items()
            # 'META': {k.lower(): v for (k, v) in request.META}
        }
        # my_dictsssss = {
        #     # 'body': request,
        #     'fromUrl': fromUrl,
        #     # "get": str(request.GET)
        #     'GET': json.dumps({k.lower(): v for (k, v) in request.GET})

        #     # "META": request.META.items()
        #     # 'META': {k.lower(): v for (k, v) in request.META}
        # }
        # .get("https://www.python.org/")
        RequestMetaAndGet.objects.create(
            datajson=my_dictss,
            datajsonGet=json.dumps(request.GET),
            PATH=request.path,
            cookie=cookie,
            # COOKIES=cookie,
            ip_info=ip_info,
            CONTENT_LENGTH=request.META.get("CONTENT_LENGTH", ''),
            CONTENT_TYPE=request.META.get("CONTENT_TYPE", ''),
            HTTP_ACCEPT=request.META.get("HTTP_ACCEPT", ''),
            HTTP_ACCEPT_ENCODING=request.META.get("HTTP_ACCEPT_ENCODING", ''),
            HTTP_ACCEPT_LANGUAGE=request.META.get("HTTP_ACCEPT_LANGUAGE", ''),
            HTTP_HOST=request.META.get("HTTP_HOST", ''),
            HTTP_REFERER=request.META.get("HTTP_DNT", ''),
            HTTP_USER_AGENT=request.META.get("HTTP_USER_AGENT", ''),
            # PATH=request.META.get("PATH", ''),
            QUERY_STRING=request.META.get("QUERY_STRING", ''),
            REMOTE_ADDR=request.META.get("REMOTE_ADDR", ''),
            REMOTE_HOST=request.META.get("REMOTE_HOST", ''),
            REMOTE_USER=request.META.get("SCRIPT_NAME", ''),
            REQUEST_METHOD=request.META.get("REQUEST_METHOD", ''),
            encoding=request.encoding,
            SERVER_PORT=request.META.get("SERVER_PORT", ''),
            GET=request.GET,
            COOKIES=request.META.get("CSRF_COOKIE", ''),

            # json.loads(request.GET.dict().keys()[0])
            # json.dumps({k: request.GET.getlist(k) for k in request.GET.keys()})
        )

        # sprint(data_json)
        # RequestHederInfo.objects.create(
        #     datajson=json.loads(request.META))
        # from django.core import serializers
        # import json
        # ip = request.META.get('REMOTE_ADDR')

        my_dict = {
            # 'body': request,
            'fromUrl': fromUrl,
            'headers': {k.lower(): v for (k, v) in request.headers.items()}
        }
        # tmpJson = serializers.serialize("json",request.headers)
        # tmpObj = json.loads(tmpJson)
        # print(request.headers)
        RequestHederInfo.objects.create(datajson=my_dict,
                                        cookie=cookie,
                                        ip_info=ip_info,

                                        )
    except ValueError as e:
        print("ValueError "+str(e))
    except requests.exceptions.ConnectionError as e:
        print("requests exceptions ConnectionError "+str(e))
    except Exception as e:
        print("requests exception  "+str(e))
    # except request.exceptions.ConnectionError:
        # pass


def indexed(request, tag='', lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    datCategory = Category.objects.all(

    )
    dataService = Services.objects.filter(

        is_deleted=False, is_hidden=False,
    )
    dataImagesPortfolioNoDetils = ImagesPortfolioNoDetils.objects.all().order_by('-Date_Added')

    formOurNewsletter = OurNewsletterForm()

    form = ContactForm()

    # send_email( "This is an important message.",
    #             "This is an important message.",
    #             html_content=html_designer(),
    #             is_html_content=True,
    #             to="ialzoriqi@gmail.com",
    #             to_list=["ialzoriqi@gmail.com", "ibrahim.alzoriqi@gmail.com"]
    #            )
    # data = Contact.objects.all()
    # form = ContactForm()

    # revers_fun = '/#contact'
    # 'اتصل بناء'
    # form = ContactForm(request.POST, request.FILES)
    # if form.is_valid():

    #     form.save()
    #     messages.success(request, 'تم الإضافة بنجاح')
    #     return redirect(revers_fun)
    # else:
    #     # if name_model == Task3:
    #     #     form.save(commit=False)
    #     messages.error(request, 'خطأ')
    #     return redirect(revers_fun)
    statistic = Statistics.objects.all()
    context = {
        "switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        'form': form,
        'FormOurNewsletter': formOurNewsletter,
        'SectionPageHome': SectionPageHomeQuerySet,
        'Category': datCategory,
        "statistics": statistic,
        'ImagesPortfolioNoDetils': dataImagesPortfolioNoDetils,
        "ServiceItem": dataService,

        "title": "الرئيسية",
        "titel": "الرئيسية",
        "section_title_services": "   خدماتنا دوماً معك ",
        "url": getUrl(request=request),

    }

    dataImagesPortfolio = ImagesPortfolio.objects.all()
    context['ImagesPortfolioss'] = dataImagesPortfolio
    context['AdsenceHeder'] = AdsenceHederQuerySet()
    context['Clients'] = ClientsQuerySet()
    context['teams'] = TeamsQuerySet()
# ,
    context['partners'] = PartnersQuerySet()

    context['frequentlys'] = FrequentlyAskedQuestionsQuerySet()
    context['testimonials'] = TestimonialsQuerySet()
    context["branches"] = BranchesHederQuerySet()
    context["applications"] = BankApplicationsQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    # context['ourmarch'] = OurMarchQuerySet()

    context['blogs'] = BlogsHomeListView()
    context["curancy"] = getCurancy()
    
    
    context["static_content"] = static_content[lang]
    if request.method == 'POST':
        SaveContact(request, "index.html", context)
        return render(request, 'index.html', context)

    return render(request, 'index.html', context)





def about(request,lang="ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    statistic = Statistics.objects.all()
    context = {
        "switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        "title": "عن بنك الانماء",
        "titel": "عن بنك الانماء",
        "url": getUrl(request=request)
    }
    
    context["static_content"] = static_content[lang]

    context['abouts'] = AboutQuerySet()
    context['Massegeabout'] = MassegeAboutQuerySet()
    context['objective'] = ObjectivesQuerySet()
    context['ourvision'] = OurVisionQuerySet()
    context['ourstartup'] = OurStartupQuerySet()
    context['aboutus'] = AboutUsQuerySet()
    context['values'] = ValuesQuerySet()
    print('values......................')


    context['ourmission'] = OurMissionQuerySet()
    context['ourmarch'] = OurMarchQuerySet()
    
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    context['FormOurNewsletter'] = OurNewsletterForm()
    if request.method == 'POST':
        SaveContact(request, "about.html", context)
        return render(request, 'about.html', context)
    return render(request, 'about.html', context)


def index(request,lang="ar"):
    return indexed(request = request,lang = lang)


def index_section(request, tag=""):
    return indexed(request)


def sitemap(request):
    import mimetypes
    # import os module
    import os
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR + '/' + 'templates', 'sitemap.xml')
    return FileResponse(open(filepath, 'rb'), content_type='application/xml')


def checkGoooglr(request):
    rends = render(request, 'google350bc5959c844c8d.html', {"data": "data",
                                                            "title": "google Seo",
                                                            "url": getUrl(request=request)
                                                            })
    return rends


def add_task_execution_officer(request):
    return add_data(request, Contact, ContactForm, 'index.html', 'add_Contact', 'اتصل بناء')


def add_data(request, name_model, name_form, name_template, revers_fun, titel):

    data = name_model.objects.all().order_by('-id')[: 10]
    form = name_form(request.POST or None)
    if request.method == 'POST':

        form = name_form(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request, 'تم الإضافة بنجاح')
           # return redirect(revers_fun)
            return redirect('index')
        else:
            # if name_model == Task3:
            #     form.save(commit=False)
            messages.error(request, 'خطأ')
            return redirect('index')
    context = {
        "switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        'data': data,
        'form': form,
        'title': titel,
        "url": getUrl(request=request)

    }
    return render(request, name_template, context)


def portfolio_details(request, id):

    dataImagesPortfolio = ImagesPortfolio.objects.filter(id=id)
    idpr = 0
    idImagepr = 0

    for obj in dataImagesPortfolio:
        idpr = obj.portfolio.id

    DataPortfolio = Portfolio.objects.filter(id=idpr)
    for obj in DataPortfolio:
        idImagepr = obj.id
    DataPortfolioImages = ImagesPortfolio.objects.filter(
        portfolio=idImagepr)

    context = {
        "switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        'dataImagesPortfolio': dataImagesPortfolio,
        'DataPortfolioImages': DataPortfolioImages,
        "title": "معرض اعمال البنك",
        "titel": "معرض اعمال البنك",

        "url": getUrl(request=request)


    }

    return render(request, 'portfolio-details.html', context)


def post(request):

    dataImagesPortfolio = ImagesPortfolio.objects.filter()
    idpr = 0
    idImagepr = 0

    for obj in dataImagesPortfolio:
        idpr = obj.portfolio.id

    DataPortfolio = Portfolio.objects.filter(id=idpr)
    for obj in DataPortfolio:
        idImagepr = obj.id
    DataPortfolioImages = ImagesPortfolio.objects.filter(
        portfolio=idImagepr)

    context = {
        "switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        'dataImagesPortfolio': dataImagesPortfolio,
        'DataPortfolioImages': DataPortfolioImages,
        "title": "معرض اعمال البنك",
        "titel": "معرض اعمال البنك",

        "url": getUrl(request=request)
    }

    return render(request, 'blog-single.html', context)


def manifest(request):
    import mimetypes
    # import os module
    import os
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR + '/' + 'static', 'manifest.json')
    return FileResponse(open(filepath, 'rb'), content_type='application/json')
