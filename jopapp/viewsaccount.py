
from .models import Register
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from settingapp.views import SettingModelQuerySet
from adsense.views import AdsenceHederQuerySet
from .form import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Jobs, Register
from .form import *
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib import messages
# from views import countdata
# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from settingapp.views import static_content

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

def contextDate(request, form=None, djobs=None, jobs=None, count=None,
                formset=None, job=None, bankKonownData=None, bankKonown=None,
                disabled=None,
                employmentData=None,
                employment=None,
                experincedata=None,
                experince=None,
                coursesdata=None,
                education_admin=None,
                courses=None,
                comform=None,
                job_offred=None,
                computerdata=None,
                formdata=None,
                users_admin=None,
                up=None,
                Languageskill=None,
                baseinfo=None,
                generaldata=None,
                orederJob=None,
                title="التوظيف",
                url_name="",
                lang ="ar"



                ):
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
    context = {"switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
        "url": getUrl(request),
        
        # "url": getUrl(request)
        "title": title,

    }
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    context['AdsenceHeder'] = AdsenceHederQuerySet()
    context["user_register"] = user
    context["form"] = form
    context["acitive"] = 'btn-primary'
    context["djobs"] = djobs
    context["jobs"] = jobs
    context["job"] = job

    context["acitive"] = 'btn-primary'
    # context["djobs"] = djobs

    # context['active']= 'btn-primary'
    context['active'] = 'btn-primary'
    context["count"] = count if count == None else countdata(request)
    context["formset"] = formset
    context['bankKonownData'] = bankKonownData
    context['bankKonown'] = bankKonown,
    context['bankKonownForm'] = bankKonown,
    
    context['disabled'] = disabled
    context['employmentData'] = employmentData
    context['employment'] = employment,
    context['experincedata'] = experincedata
    context['experince'] = experince
    context['coursesdata'] = coursesdata
    context['courses'] = courses
    context['comform'] = comform
    context['computerdata'] = computerdata
    context['formdata'] = formdata
    context['up'] = up
    context['generaldata'] = generaldata
    context['baseinfo'] = baseinfo
    context['Languageskill'] = Languageskill

    context['orederJob'] = orederJob
    context['orederJob'] = orederJob
    context['users_admin'] = users_admin
    context['job_offred'] = job_offred
    context['education_admin'] = education_admin

    context['url_name'] = url_name
    context["static_content"] = static_content[lang]
    # context['orederJob'] = orederJob

    # context['url'] = orederJob

    # context['experincedata']=experincedata
    # context['coursesdata']=coursesdata
    # context['computerdata']=computerdata
    # 'comform': comform,'computerdata':computerdata,
    # 'acitive': 'btn-primary'}
    return context


def countdata(request):
    if not islogin(request):
        return redirect('/login/?urlredirect='+getUrl(request))
    else:
        count = 0
        user = Register.objects.get(id=request.session.get('userLoggedUserId'))

        # Check if the user exists
        if user:
            if count < 100:
                count += 10

        # Check for data in Education model
        formdata = Education.objects.filter(
            user=request.session.get('userLoggedUserId'))
        if formdata.exists():
            if count < 100:
                count += 20

        # Check for data in LanguageSkill model
        languageskill = LanguageSkill.objects.filter(user=user)
        if languageskill.exists():
            if count < 100:
                count += 20

        # Check for data in Employment model
        employmentData = Employment.objects.filter(user=user)
        if employmentData.exists():
            if count < 100:
                count += 10

        # Check for data in BankKonown model
        bankKonownData = BankKonown.objects.filter(user=user)
        if bankKonownData.exists():
            if count < 100:
                count += 10

        # Check for data in Experience model
        experincedata = Experience.objects.filter(user=user)
        if experincedata.exists():
            if count < 100:
                count += 10

        # Check for data in TrainingCourses model
        coursesdata = TrainingCourses.objects.filter(user=user)
        if coursesdata.exists():
            if count < 100:
                count += 10

        # Check for data in ComputerSkill model
        computerdata = ComputerSkill.objects.filter(user=user)
        if computerdata.exists():
            if count < 100:
                count += 10

        # Check for data in oreder_Jobs model
        gdata = GeneralData.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))
        if gdata.exists():
            if count < 100:
                count += 10

        return count


class ProfileRegistration(View):
    def get(self, request, lang = "ar"):
        print(lang)
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        print("LANGUAGE_CODE")
        print(request.LANGUAGE_CODE)
        print(lang)
        form = RegisterForm()
        # Access the session variable
        user = request.session.get('userLoggedUserId')
        print(user)
        context =  contextDate(request=request, form=form,title=_("مستخدم جديد"))
        context["static_content"] = static_content[lang]
        return render(request, 'jop/create_accounte.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")
            if password == confirmpassword:
                form.save()
                messages.success(
                    request, 'Congratulations! Profile created successfully')
                return redirect('/login/?urlredirect='+getUrl(request))

            else:
                messages.error(request, ' كلمة المرور غير متطابقة  ')

        # If the form is not valid, create a new empty form

        return render(request, 'jop/create_accounte.html', contextDate(request=request, form=form,))


def islogin(request):
    if request.session.has_key('userLoggedName') and request.session.has_key('userLoggedEmailId'):
        return True
    else:
        return False


def register(request):
    formset = RegisterForm
    print(request.session.get('userLoggedUserId'))
    if request.method == "POST":
        formset = RegisterForm(request.POST)

        if formset.is_valid():
            formset.save()
            formset = RegisterForm

    return render(request, "jop/create_accounte.html", contextDate(request=request, formset=formset))


def login(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    
    urlredirect = request.GET.get("urlredirect")

    if islogin(request) == True:
        if urlredirect and str(urlredirect).endswith("userLogout/") == False:
            return redirect(urlredirect)
        return redirect("/"+lang)
    else:

        # Access the session variable
        user = request.session.get('userLoggedUserId')
        form = LoginModelForm()

        # if form.is_valid():
        if request.method == 'POST':
            form = LoginModelForm(request.POST)
            if form.is_valid():
                form.save()
                # if   request.POST:
                loginusername = request.POST.get("email")
                loginPassword = request.POST.get("password")
                emailExistQuery = Register.objects.filter(
                    email=loginusername, password=loginPassword)
                # emailExistQuery = Register.objects.filter(
                #     username=loginusername, password=loginPassword)
                if not emailExistQuery.exists():
                    emailExistQuery = Register.objects.filter(
                        email=loginusername, password=loginPassword)

                if emailExistQuery.exists():
                    # print(emailExistQuery)
                    # fetchedemailid = Register.objects.filter(
                    #     username=loginusername, password=loginPassword)[0].email
                    # fetchedid = Register.objects.filter(
                    #     email=loginusername, password=loginPassword)[0].id
                    # fetchedname = Register.objects.filter(
                    #     username=loginusername, password=loginPassword)[0].username
                    # request.session['username'] = Register.first().id
                    request.session['userLoggedIn'] = True
                    request.session['userLoggedEmailId'] = emailExistQuery[0].email
                    request.session['userLoggedName'] = emailExistQuery[0].username
                    request.session['userLoggedUserId'] = emailExistQuery[0].id
                    # sesion=request.session.has_key('username')
                    sesion = request.session.has_key('userLoggedIn')
                    userLoggedName = request.session['userLoggedName']
                    userLoggedUserId = request.session['userLoggedEmailId']

                    print(sesion)
                    print(userLoggedName)
                    print(userLoggedUserId)

                    send_email("حدثت عملية تسجيل دخول جديدة ",
                               "لقد رصدنا عملية تسجيل دخول جديدة إلى حسابك على موقع بنك الانماء https://alinmabank.com",
                               # html_content=html_message,
                               is_html_content=False,
                               to=loginusername
                               # to_list=recipient_list
                               )
                    print(urlredirect)
                    if urlredirect and str(urlredirect).endswith("userLogout/") == False:
                        return redirect(urlredirect)

                    return redirect("/"+lang)

                # messages.warning(request, 'Login Email Or Password')
                elif not emailExistQuery.exists():
                    print(" ")
                    messages.warning(request, 'ادخل ايميل او كلمة سر صحيحة')

        return render(request, "jop/login.html", contextDate(lang= lang ,request=request, form=form, title=_("تسجيل الدخول")))


def userLogout(request,lang="ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    if islogin(request) == False:
        return redirect('/')
    else:

        del request.session['userLoggedIn']
        del request.session['userLoggedEmailId']
        del request.session['userLoggedName']
        del request.session['userLoggedUserId']
        return redirect("/"+lang+'/login')

from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.utils import translation
def RequestToOpenAccountView(request, page=0, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    if islogin(request) == False:
        return redirect("/"+lang+'/login/?urlredirect='+getUrl(request))
    from anmaabankApp.views import get_cookie

    # if request.method == 'GET':
    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'service-single.html')
    user = Register.objects.filter(
        id=request.session['userLoggedUserId']).first()
    request_to_instance = RequestToOpenAccount.objects.filter(
        user=user).first()
    birth_data_instance = BirthData.objects.filter(user=user).first()
    Identification_Card_instance = IdentificationCard.objects.filter(
        user=user).first()
    AddressLocation_instance = AddressLocation.objects.filter(
        user=user).first()

    form = RequestToOpenAccountForm(instance=request_to_instance)
    birthdata = BirthDataForm(instance=birth_data_instance)
    addresslocation = AddressLocationForm(instance=AddressLocation_instance)
    id_card = IdentificationCardForm(instance=Identification_Card_instance)
    get_page = int(request.GET.get('page', 1))
    print(get_page)
    context = {"switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),

        # 'birth_data':birthdata,
        # "address_location":addresslocation,
        # "id_card":id_card,
        "titel": _("تقديم طلب فتح حساب - بيانات عامة") if get_page <= 1 else _("تقديم طلب فتح حساب - بيانات الميلاد") if get_page == 2 else _("تقديم طلب فتح حساب - عنوان السكن والاقامة ") if get_page == 3 else _("تقديم طلب فتح حساب - بيانات الهوية الشخصية "),
        "title": _("تقديم طلب فتح حساب - بيانات عامة") if get_page <= 1 else _("تقديم طلب فتح حساب - بيانات الميلاد") if get_page == 2 else _("تقديم طلب فتح حساب - عنوان السكن والاقامة ") if get_page == 3 else _("تقديم طلب فتح حساب - بيانات الهوية الشخصية "),
        "url": getUrl(request=request)


    }
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()

    if get_page <= 1:
        context["forms"] = form
    if get_page == 2:
        context["birth_data"] = birthdata
    if get_page == 3:
        context["address_location"] = addresslocation
    if get_page >= 4:
        context["id_card"] = id_card

        # 'forms': form,

    # context["applications"] = BankApplicationsQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    context["static_content"] = static_content[lang]
    print("lang")
    print(lang)
    # formOurNewsletterForm = OurNewsletterForm(request.POST, request.FILES)
    if request.method == 'POST':
        # revers_fun = '/service/'+str(id)+'#services-detail'
        revers_fun = "/open-account/"
        # 'اتصل بناء'
        form = RequestToOpenAccountForm(
            request.POST, request.FILES, instance=request_to_instance)
        birthdata = BirthDataForm(
            request.POST, request.FILES, instance=birth_data_instance)
        addresslocation = AddressLocationForm(
            request.POST, request.FILES, instance=AddressLocation_instance)
        id_card = IdentificationCardForm(
            request.POST, request.FILES, instance=Identification_Card_instance)
        if birthdata.is_valid():
            birthdatadata = birthdata.save(commit=False,)
            try:
                cookie = get_cookie(request)
                birthdatadata.cookie = cookie
                user_id = request.session.get('userLoggedUserId')
                user = Register.objects.get(id=user_id) if user_id else None
                birthdatadata.user = user
                birthdatadata.save()

            except Register.DoesNotExist:
                user = None
                birthdatadata.save()

        print(form.is_valid())
        print("form.is_valid()")
        if form.is_valid():
            form = form.save(commit=False)
            cookie = get_cookie(request)
            form.cookie = cookie
            # form.birth_data = birthdatadata
            # form.initial['cookie'] = cookie
            try:
                user_id = request.session.get('userLoggedUserId')
                user = Register.objects.get(id=user_id) if user_id else None
                form.user = user
                # form.save()

            except Register.DoesNotExist:
                user = None
                # form.save()
            form.save()
        if addresslocation.is_valid():
            addresslocation = addresslocation.save(commit=False)
            cookie = get_cookie(request)
            addresslocation.cookie = cookie
            # form.birth_data = birthdatadata
            # form.initial['cookie'] = cookie
            try:
                user_id = request.session.get('userLoggedUserId')
                user = Register.objects.get(id=user_id) if user_id else None
                addresslocation.user = user
                # form.save()

            except Register.DoesNotExist:
                user = None
                # form.save()
            addresslocation.save()
            # addresslocation.save()
        if id_card.is_valid():
            id_card = id_card.save(commit=True)
            cookie = get_cookie(request)
            id_card.cookie = cookie
            try:
                user_id = request.session.get('userLoggedUserId')
                user = Register.objects.get(id=user_id) if user_id else None
                id_card.user = user
                # form.save()
                id_card.save()

            except Register.DoesNotExist:
                user = None
                id_card.save()

            # form.birth_data = birthdatadata
            # form.initial['cookie'] = cookie

            # form.owner = request.user
            # print(form)
            # for forms in form:
            # print(forms)
        user = Register.objects.filter(
            id=request.session['userLoggedUserId']).first()
        request_to_instance = RequestToOpenAccount.objects.filter(
            user=user).first()
        birth_data_instance = BirthData.objects.filter(user=user).first()
        Identification_Card_instance = IdentificationCard.objects.filter(
            user=user).first()
        AddressLocation_instance = AddressLocation.objects.filter(
            user=user).first()

        form = RequestToOpenAccountForm(instance=request_to_instance)
        birthdata = BirthDataForm(instance=birth_data_instance)
        addresslocation = AddressLocationForm(
            instance=AddressLocation_instance)
        id_card = IdentificationCardForm(instance=Identification_Card_instance)
        get_page = int(request.GET.get('page', 1))
        print(get_page)
        context = {
            "static_content": static_content[lang],
            "switch_lang_url": getSwitchLangUrl(request),
            "login_out_toggle": login_out_toggle(request),

            # 'birth_data':birthdata,
            # "address_location":addresslocation,
            # "id_card":id_card,
            "titel": _("تقديم طلب فتح حساب - بيانات عامة") if get_page <= 1 else _("تقديم طلب فتح حساب - بيانات الميلاد") if get_page == 2 else _("تقديم طلب فتح حساب - عنوان السكن والاقامة ") if get_page == 3 else _("تقديم طلب فتح حساب - بيانات الهوية الشخصية "),
            "title": _("تقديم طلب فتح حساب - بيانات عامة") if get_page <= 1 else _("تقديم طلب فتح حساب - بيانات الميلاد") if get_page == 2 else _("تقديم طلب فتح حساب - عنوان السكن والاقامة ") if get_page == 3 else _("تقديم طلب فتح حساب - بيانات الهوية الشخصية "),
            "url": getUrl(request=request)


        }
        context['setting'] = SettingModelQuerySet()
        context["navbar"] = NavbarsQuerySet()
        context["ColumnNavbars"] = ColumnNavbarsQuerySet()
        if get_page <= 1:
            context["forms"] = form
        if get_page == 2:
            context["birth_data"] = birthdata
        if get_page == 3:
            context["address_location"] = addresslocation
        if get_page >= 4:
            context["id_card"] = id_card
            # messages.success(request, 'تم لإرسال الطلب بنجاح')
        return render(request, 'add-order.html', context)
        # else:
        #     messages.error(request, 'خطأ')

        # return render(request, 'add-order.html', context)
    # formOurNewsletter =

    return render(request, 'add-order.html', context)


def ajax_load_regions(request):
    country_id = request.GET.get('country')
    regions = Region.objects.filter(country = country_id).order_by('id')
    # regions = Region.objects.all()
    return render(request, 'region_dropdown_list.html', {'regions': regions})

