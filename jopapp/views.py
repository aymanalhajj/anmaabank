from django.contrib import messages
from django.views.generic.base import View

from .models import *
from .form import *
from django.db.models import Q

from .viewsaccount import islogin
from SendEmile.views import *

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.base import View
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Jobs, Register
from .form import *
from django.http import HttpResponse
from .viewsaccount import contextDate
# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404



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

class index(View):

    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        try:
            user_id = request.session.get('userLoggedUserId')
            user = Register.objects.get(id=user_id) if user_id else None
        except Register.DoesNotExist:
            user = None
        count = countdata(request)
        if request.user.is_superuser:
            return render(request, "jop/home-admin.html", contextDate(url_name="home", request=request, count=count,
                                                                      title="التوظيف - الرئيسية",

                                                                      ))
        else:
            return render(request, "jop/home.html", contextDate(url_name="home", request=request, count=count,
                                                                title="التوظيف - الرئيسية"
                                                                ))


class Login(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'jop/login.html', contextDate(url_name="login", request=request,
                                                             title="تسجيل الدخول "

                                                             ))


class CreateAccoute(View):
    def get(self, request, *args, **kwargs):

        #

        #
        return render(request, 'jop/create_accounte.html', contextDate(request=request,
                                                                       title=" انشاء حساب "))
# .html


from django.utils import translation
from settingapp.views import static_content
from django.utils.translation import gettext_lazy as _
class vacancies(View):
    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)

        jobs = Jobs.objects.all()
        try:
            user_id = request.session.get('userLoggedUserId')
            user = Register.objects.get(id=user_id) if user_id else None
        except Register.DoesNotExist:
            user = None
        if request.user.is_superuser:
            return render(request, 'jop/vacancies.html', contextDate(lang = lang , url_name="vacancies", request=request, jobs=jobs,
                                                                     title="الوظائف الشاغرة"
                                                                     ))
        else:
            return render(request, 'jop/vacancies.html', contextDate(lang = lang , url_name="vacancies", request=request, jobs=jobs,
                                                                     title="الوظائف الشاغرة"
                                                                     ))
        # context["jobs"] = jobs


class customadmin(View, ):
    def get(self, request, *args, **kwargs):

        jobs = Jobs.objects.all()
        users_admin = Register.objects.all().filter(
            Q(oreder_Jobs_user__isnull=False)).distinct()
        user_data = self.request.GET.get("user")
        job_offred = None
        education_admin = None
        count = None
        experincedata = None
        coursesdata = None
        computerdata = None
        generaldata = None
        baseinfo = None
        form = SerchModelForm()
        Languageskill = None

        if user_data == None and self.kwargs and self.kwargs['id']:
            user_data = self.kwargs['id']

        # user = None
        if user_data:
            users_admin = Register.objects.all().filter(
                Q(oreder_Jobs_user__isnull=False)).filter(id=user_data).distinct()
            job_offred = oreder_Jobs.objects.filter(
                user=Register(id=user_data))
            education_admin = Education.objects.filter(
                user=Register(id=user_data))
            count = countdataForAdmin(request, user_data)
            baseinfo = Register.objects.get(
                id=user_data)
            Languageskill = LanguageSkill.objects.filter(
                user=Register(id=user_data))

            experincedata = Experience.objects.filter(
                user=Register(id=user_data))
            coursesdata = TrainingCourses.objects.filter(
                user=Register(id=user_data))
            computerdata = ComputerSkill.objects.filter(
                user=Register(id=user_data))
            generaldata = GeneralData.objects.filter(
                user=user_data).first()

        if request.user.is_superuser:
            return render(request, "jop/home-admin.html", contextDate(url_name="home-jop-manage-admin", request=request,
                                                                      jobs=jobs,
                                                                      users_admin=users_admin,
                                                                      #   job_offred=job_offred,
                                                                      count=count,
                                                                      form=form,
                                                                      education_admin=education_admin,
                                                                      title="التوظيف - الرئيسية",
                                                                      # jobs=None,djobs=None,
                                                                      #    job=None,formset=None,
                                                                      #    bankKonownData=None,
                                                                      #    bankKonown=None,
                                                                      #    disabled=None,
                                                                      #    employmentData=None,
                                                                      #    employment=None,
                                                                      experincedata=experincedata,
                                                                      #    experince=None,
                                                                      coursesdata=coursesdata,
                                                                      #    courses=None,
                                                                      #    comform=None,
                                                                      computerdata=computerdata,
                                                                      formdata=None,
                                                                      up=None,
                                                                      generaldata=generaldata,
                                                                      baseinfo=baseinfo,
                                                                      Languageskill=Languageskill,
                                                                      #   url_name="showCv",
                                                                      ))
        else:
            return render(request, 'jop/vacancies.html', contextDate(url_name="vacancies", request=request, jobs=jobs,
                                                                     title="الوظائف الشاغرة"
                                                                     ))
        # context["jobs"] = jobs

    def post(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        # form = SerchModelForm()

        form = SerchModelForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            # self.object.user = Register(id=request.session['userLoggedUserId'])
            # self.object.job = Jobs(id=1)
            self.object.save()
            # if request.method == 'POST':
        # form = SerchModelForm(request.POST, request.FILES)
        # formOurNewsletterForm = OurNewsletterForm(request.POST, request.FILES)

        # if form.is_valid():

        form.save()
        # messages.success(request, 'تم الإضافة بنجاح')
        # return redirect(revers_fun)
        # formOurNewsletterForm.save()
        job = request.POST["job"]
        specializ = request.POST["specialization"]
        search = request.POST["search"]
        # all_data = False
        # if request.POS
        all_data = request.POST.get('all_data', False)
        gender_input = request.POST["gender"]

        print(job)
        print(gender_input)
        print(specializ)
        display_name_ar = ""
        statictital = "الوظائف المقدمة"
        title = statictital

        # queryset = Branches.objects.all().order_by(
        # 'created_at').filter()
        queryset = Register.objects.all().filter(
            Q(oreder_Jobs_user__isnull=False)).distinct()

        if all_data is not None and all_data:
            queryset = queryset.filter(
                Q(EducationRegister__isnull=False) &
                Q(LanguageSkillRegister__isnull=False) &
                Q(ComputerSkillRegister__isnull=False) &
                Q(TrainingCoursesRegister__isnull=False) &
                Q(ExperienceRegister__isnull=False) &
                Q(EmploymentRegister__isnull=False) &
                Q(BankKonownRegister__isnull=False) &
                Q(GeneralDataRegister__isnull=False)
                #    Q(__isnull=False)&
                #    Q(__isnull=False)&
                #    Q(__isnull=False)&
                #    Q(__isnull=False)&
                #    Q(__isnull=False)&

            )
        if search is not None and search is not "":
            queryset = queryset.filter(

                Q(username__icontains=search) |
                Q(full_name__icontains=search) |
                Q(email__icontains=search) |
                Q(password__icontains=search) |
                Q(confirmpassword__icontains=search) |
                Q(gender__icontains=search) |
                Q(city__icontains=search) |
                Q(address__icontains=search) |

                Q(mobile_number__icontains=search) |
                Q(marital_status__icontains=search) |
                Q(number_whatsapp__icontains=search) |


                Q(governorate__name__icontains=search) |
                Q(governorate__name_ar__icontains=search) |
                # Q(governorate__display_name_ar__icontains=search) |
                # Q(governorate__display_name__icontains=search) |
                #    Q(governorate__name__icontains=search) |
                # Q(address1__long__icontains=search) |

                # Q(address1__address_line__icontains=search) |
                # Q(address1__street__icontains=search) |
                # Q(address1__lat__icontains=search) |
                # Q(address1__long__icontains=search) |
                # Q(address1__map_location__icontains=search) |

                # Q(address1__postcode__icontains=search) |


                Q(governorate__country__name__icontains=search) |
                Q(governorate__country__name_ar__icontains=search)
                # Q(governorate__country__display_name_ar__icontains=search) |
                # Q(governorate__country__display_name__icontains=search)

            )
        if gender_input is not None and gender_input is not "":
            queryset = queryset.filter(gender=gender_input)
        if job is not None and job is not "":
            # queryset = queryset.filter(category=category,)
            oreder_Job = oreder_Jobs.objects.filter(
                job=job).values("user")
            queryset = queryset.filter(id__in=oreder_Job)
        if specializ is not None and specializ is not "":
            education = Education.objects.filter(
                specialization=specializ).values("user")
            queryset = queryset.filter(id__in=education)

            # if Region.objects.filter(
            #     pk=region).exists():
            # display_name_ar = Region.objects.filter(
            #     pk=region).first().display_name_ar
            # context["region"] = display_name_ar
            # else:
            # title = statictital + display_name_ar,
            # title = statictital + display_name_ar,
        # context["branches"] = queryset
        # context["form"] = form
        # context["category"] = category
        if queryset.exists():
            print()
        else:
            messages.success(
                request, 'لايوجد مقدمين  يرجى اعادة صياغة جملة البحث او اعادة فلترة اخرى')
    # SaveContact(request, "index.html", context)
        if request.user.is_superuser:
            return render(request, "jop/home-admin.html", contextDate(request=request, form=form,
                                                                      users_admin=queryset,
                                                                      title=title))
        else:

            return render(request, 'jop/cv/oder_job.html', contextDate(request=request, form=form,
                                                                       users_admin=queryset,
                                                                       title=title))
    # else:

        # form = OrderJobForm

        #
        # context["form"] = form

        # context['active']= 'btn-primary'
        #


class OrderJobView(View):
    def get(self, request, *args, **kwargs):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:

            try:
                jop_data = None

                if jop_data == None and self.kwargs and self.kwargs['id']:
                    jop_data = self.kwargs['id']
                else:
                    return redirect('home-jop')
                user_id = request.session.get('userLoggedUserId')
                print(user_id)
                print(oreder_Jobs.objects.filter(
                    job=jop_data, user=user_id).count())

                # user_id = request.session.get('userLoggedUserId')
                # orederJob = oreder_Jobs.objects.filter(
                #     id=jop_data, user=Register.objects.get(id=user_id).id)
                # print(orederJob.exists())

                # if orederJob.exists():
                # form = OrderJobForm(initial=orederJob.first())
                # else:
                form = OrderJobForm(instance=oreder_Jobs.objects.filter(
                    job=jop_data, user=user_id).first())

                user = Register.objects.get(id=user_id) if user_id else None
            except Register.DoesNotExist:
                user = None

            # context["form"] = form
            # context['active']= 'btn-primary'

            return render(request, 'jop/cv/oder_job.html', contextDate(request=request, form=form,
                                                                       title="الوظائف المقدمة"))

    def post(self, request, *args, **kwargs):
        jop_data = None

        if jop_data == None and self.kwargs and self.kwargs['id']:
            jop_data = self.kwargs['id']
        else:
            return redirect('home-jop')
        user_id = request.session.get('userLoggedUserId')
        orederJob = oreder_Jobs.objects.filter(
            job=jop_data, user=user_id)
        if orederJob.exists:
            form = OrderJobForm(request.POST, request.FILES, instance=oreder_Jobs.objects.filter(
                job=jop_data, user=user_id).first())
        else:
            form = OrderJobForm(request.POST, request.FILES,)

        # form = OrderJobForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            jop_data = None

            if jop_data == None and self.kwargs and self.kwargs['id']:
                jop_data = self.kwargs['id']
            else:
                messages.error(
                    request, 'خطاء في بيانات الوظيفة')
                # form = OrderJobForm()
                return render(request, 'jop/cv/oder_job.html', contextDate(request=request, form=form,
                                                                           title="الوظائف المقدمة"))

            self.object.job = Jobs(id=jop_data)
            self.object.save()

            messages.success(
                request, 'تم حفظ الطلب يرجى اكمال ادخال بيانات cv ')
            # form = OrderJobForm

        #
        # context["form"] = form

        # context['active']= 'btn-primary'
            #
        return render(request, 'jop/cv/oder_job.html', contextDate(request=request, form=form,
                                                                   title="الوظائف المقدمة"))


def detail(request, id):
    djobs = Jobs.objects.get(id=id),
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
        djobs = Jobs.objects.get(id=id),
    #
    #
    #
    #
    #
    #
    # # context["form"] = form
    #
    # context["djobs"] = djobs

    # context['active']= 'btn-primary'
        #
    return render(request, 'jop/details_jobs.html', contextDate(request=request, djobs=djobs,
                                                                title="تفاصيل الوظيفة"))


def message_bank(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None

    # context["form"] = form

    # context["djobs"] = djobs

    # context['active']= 'btn-primary'
        #
    return render(request, 'jop/message_bank.html', contextDate(request=request,
                                                                title="رسالة البنك"))


def puocedures_job(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None

    # context["form"] = form

    # context["djobs"] = djobs

        #
    return render(request, 'jop/puocedures_job.html', contextDate(request=request,
                                                                  title="إجراءات التوظيف في بنك الانماء"))


def purpose_bank(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None

        #
    return render(request, 'jop/purpose_bank.html', contextDate(request=request,
                                                                title="مواصلة تبوء موقع ريادي في العمل البنكي يحقق عائد جيد للمساهمين والمودعين عن طريق"))


def strategy_bank(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None

    return render(request, 'jop/strategy_bank.html', contextDate(request=request,
                                                                 title="  بيان إستراتيجية بنك الانماء"))


def what_gion_bank(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
    return render(request, 'jop/what_gion_bank.html', contextDate(request=request,
                                                                  title="لماذا تنضم إلى فريق العمل في بنك الانماء للتمويل  الإسلامي"))


def valuesprinciples(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
    return render(request, 'jop/values_principles.html', contextDate(request=request,
                                                                     title="القيم والمبادئ"))


def ruicbank(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
    return render(request, 'jop/ruic_bank.html', contextDate(request=request))


def introcationjob(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    translation.activate(lang)
    try:
        user_id = request.session.get('userLoggedUserId')
        user = Register.objects.get(id=user_id) if user_id else None
    except Register.DoesNotExist:
        user = None
    return render(request, 'jop/introcation_job.html', contextDate(request=request))


def send_email_with_template(subject, recipient_list, template_name, context):
    html_message = render_to_string(template_name, context)

    plain_message = strip_tags(html_message)

    # Send the email
    send_mail(subject, plain_message, "anmaqbank@gmail.com",
              recipient_list, html_message=html_message)


class send_message_email(View):
    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        form = MyPasswordResetForm()
        return render(request, 'jop/forgetpassword.html', contextDate(request=request, form=form,))

    def post(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        form = MyPasswordResetForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST["email"]
            # email = request.POST.get("email")
            print(request.POST["email"])
            # print(form)
            # emile = request.POST["emile"]
            our_new = OurNewsletter.objects.create(emile=email)
            our_new.save()
            # request.session['emailrest'] = email

            user_email = Register.objects.filter(email=email)
            if user_email.exists():
                try:
                    subject = 'Your Subject'
                    template_name = 'jop/email_template.html'
                    context = {"switch_lang_url": getSwitchLangUrl(request),"login_out_toggle": login_out_toggle(request),
                        'username': 'John Doe', 'verification_link': 'http://127.0.0.1:8000/passswordrest/'}
                    html_message = render_to_string(
                        'jop/email_template.html', {'context': context})
                    recipient_list = [email]
                    # sendEmile()

                    send_email("This is an important message.",
                               "This is an important message.",
                               html_content=html_message,
                               is_html_content=True,
                               to=email,
                               # to_list=[recipient_list],
                               )
                    # send_email_with_template(subject, recipient_list, template_name, context)
                    request.session['emailrest'] = email
                    messages.success(
                        request, "Email with Template Sent Successfully!")

                    return render(request, 'jop/forgetpassword.html', contextDate(request=request, form=form,))

                    # return HttpResponse("Email with Template Sent Successfully!")
                except Exception as e:
                    print(e)
                    send_email_exeption_to_devloper(subject="Error sending the email."+str(e),
                                                    message="Error sending the email." +
                                                    str(e),
                                                    class_name="send_message_email",
                                                    function="post",
                                                    line="308"
                                                    )
                    messages.error(request, "Error sending the email."+str(e))
                    # Handle any exceptions that may occur during email sending
                    # return HttpResponse("Error sending the email.")
                    return render(request, 'jop/forgetpassword.html', contextDate(request=request, form=form,))

            else:
                messages.error(request, 'البريد غير متوفر من سابق')
                return render(request, 'jop/forgetpassword.html', contextDate(request=request, form=form,))

        else:
            # Handle the case when the form is not valid by re-rendering the form with errors
            return render(request, 'jop/forgetpassword.html', contextDate(request=request, form=form,))

#


class PasswordResetView(View):
    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)

        return render(request, 'jop/password-reset.html')

    def post(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        if 'btnresetpass' in request.POST:
            user_email = request.session.get('emailrest')
            if user_email:
                password1 = request.POST.get("password")
                confirmpassword = request.POST.get("confirmpassword")
                try:
                    Register.objects.get(email=user_email)
                except Register.DoesNotExist:
                    messages.error(request, 'User does not exist')
                    return redirect("passswordrest")
                if password1 == confirmpassword:

                    Register.objects.filter(
                        email=user_email).update(password=password1)
                    return redirect('/login/?urlredirect='+getUrl(request))
                else:
                    messages.error(request, 'Passwords do not match')
            else:
                messages.error(request, 'User email not found in session')
        else:
            return redirect("passswordrest")

        return render(request, 'jop/password-reset.html', contextDate(request=request,))


class Changepassword(View):
    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:

            return render(request, 'jop/passwordchange.html')

    def post(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        if 'changepassword' in request.POST:
            user_email = request.session.get('userLoggedEmailId')
            print(user_email)
            if user_email:
                passwordold = request.POST.get("passwordold")
                newpassword = request.POST.get("newpassword")
                newconfirmpassword = request.POST.get("confirmpassword")
                try:
                    Register.objects.get(
                        email=user_email, password=passwordold)
                except Register.DoesNotExist:
                    messages.error(request, 'User does not exist')
                    return redirect("passwordchange")
                if newpassword == newconfirmpassword:

                    Register.objects.filter(email=user_email, password=passwordold).update(
                        password=newpassword)
                    return redirect('/login/?urlredirect='+getUrl(request))
                else:
                    messages.error(request, 'Passwords do not match')
            else:
                messages.error(request, 'User email not found in session')
        else:
            return redirect("passwordchange")

        return render(request, 'jop/passwordchange.html', contextDate(request=request,))


class FileUploadView(View):

    def get(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)
        form = uploadCvForm()
        count = countdata(request)
        return render(request, 'jop/cv/uploadcv.html', contextDate(lang= lang, url_name="filedupload", request=request, form=form, count=count))

    def post(self, request, lang = "ar"):
        if lang is None or lang not in("ar","en"):
            lang = 'ar'
        translation.activate(lang)

        task = get_object_or_404(
            Register, id=request.session['userLoggedUserId'])
        form = uploadCvForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('baseinfo')  # Redirect to a success page
        return render(request, 'jop/cv/uploadcv.html', contextDate(lang= lang, url_name="filedupload", request=request, form=form,))


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


def countdataForAdmin(request, id):

    if id != None and Register.objects.filter(id=id).exists():
        count = 0
        user = Register.objects.get(id=id)

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
            # count += 20

        # Check for data in Employment model
        employmentData = Employment.objects.filter(user=user)
        if employmentData.exists():
            if count < 100:
                count += 20

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
            user=Register(id=request.session.get('userLoggedUserId')))
        if gdata.exists():
            if count < 100:
                count += 10
    else:
        count = None
    return count
