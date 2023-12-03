from django.shortcuts import render,redirect
from .form import LoanApplicationForm
from .models import LoanApplication
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from jopapp.models import  Register
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib import messages



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
from settingapp.views import SettingModelQuerySet
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
def getUrl(request):
    if request is None:
        raise Exception("request is None")
    # print("url_name")
    # print(request.build_absolute_uri())
    return request.build_absolute_uri()


def islogin(request):
    if request.session.has_key('userLoggedName') and request.session.has_key('userLoggedEmailId'):
        return True
    else:
        return False

from django.utils import translation
from settingapp.views import static_content
from django.utils.translation import gettext_lazy as _
# Create your views here.
def LoanApplicationView(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)

    print(lang)

    if islogin(request) == False:
        return redirect('/login/?urlredirect='+getUrl(request))
    from anmaabankApp.views import get_cookie

    user = Register.objects.filter(id=request.session['userLoggedUserId']).first()
    request_to_instance = LoanApplication.objects.filter(user=user).first()
    form = LoanApplicationForm(instance = request_to_instance)

    context = {"switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        'forms' : form,
        "title": _("تقديم طلب  تمويل"),
        "url": getUrl(request=request)
    }
    
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context["static_content"] = static_content[lang]
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST , instance = request_to_instance)
        if form.is_valid():
            form.save()
            messages.success(request,_('تم ارسال طلب التمويل بنجاح'))
            return render(request, 'load-app.html', context)
        else:
            messages.error(request,form.errors)
            messages.error(request,_('حدث خطأ، نرجو التأكد من البيانات واعادة المحاولة.'))
            return render(request, 'load-app.html', context)
    #form = LoanApplicationForm()

    #form = RequestToOpenAccountForm(instance=request_to_instance)

    # context['forms']=form
    return render(request, 'load-app.html', context)




