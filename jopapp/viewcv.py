
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from .viewsaccount import islogin
from .views import countdata
from .models import BankKonown, ComputerSkill, Education, Employment, Experience, GeneralData, LanguageSkill, Register, TrainingCourses, oreder_Jobs
from .viewsaccount import contextDate
from .form import BankKonownForm, ComputerSkillFrom, EducationForm, EmploymentForm, ExperienceForm, GeneralDataForm, LanguageSkillFrom, OrderJobForm, RegisterForm, TrainingCoursesForm


def getUrl(request):
    if request is None:
        raise Exception("request is None")
    # print("url_name")
    # print(request.build_absolute_uri())
    return request.build_absolute_uri()


class Baseinfo(View):
    def get(self, request):
        if not islogin(request):
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            form = RegisterForm(instance=user)  # Correct indentation here
            print(request.session['userLoggedUserId'])
            return render(request, 'jop/cv/baseinfo.html',
                          contextDate(request=request, form=form, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=None,
                                      experince=None,
                                      coursesdata=None,
                                      courses=None,
                                      comform=None,
                                      computerdata=None,
                                      formdata=None,
                                      up=None,
                                      generaldata=None,
                                      baseinfo=None,
                                      Languageskill=None,
                                      orederJob=None,
                                      title="البيانات الاساسية",
                                      url_name="baseinfo",



                                      )
                          )

    def post(self, request):
        user = Register.objects.get(id=request.session['userLoggedUserId'])
        form = RegisterForm(request.POST, request.FILES, instance=user)
        # print(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully')
            return redirect("baseinfo")

        #

        if 'updateSectorNameBtn' in request.POST:
            user = request.session['userLoggedUserId']
            inputName = request.POST.get("full_name")
            inputemial = request.POST.get("email")
            inputgender = request.POST.get("gender")
            inputgovernorate = request.POST.get("governorate")
            inputcity = request.POST.get("city")
            inputaddress = request.POST.get("address")
            inputvillage = request.POST.get("village")
            inputidnumber = request.POST.get("idnumber")
            inputRelease_date = request.POST.get("Release_date")
            inputplace_issue = request.POST.get("place_issue")
            inputdate_birth = request.POST.get("date_birth")
            inputplace_birth = request.POST.get("place_birth")
            inputmarital_status = request.POST.get("marital_status")
            inputcurrent_address = request.POST.get("current_address")
            inputpermanent_address = request.POST.get("permanent_address")
            inputmobile_number = request.POST.get("mobile_number")
            inputnumber_whatsapp = request.POST.get("number_whatsapp")
            inputlink_facebook = request.POST.get("link_facebook")
            inputlink_twiter = request.POST.get("link_twiter")
            inputlink_instigrem = request.POST.get("link_instigrem")

            sectorDeleteQuery = Register.objects.filter(id=user).update(
                full_name=inputName, email=inputemial,
                gender=inputgender, address=inputaddress,
                city=inputcity, governorate=inputgovernorate,
                village=inputvillage, idnumber=inputidnumber,
                Release_date=inputRelease_date, place_issue=inputplace_issue,
                date_birth=inputdate_birth, place_birth=inputplace_birth,
                marital_status=inputmarital_status, current_address=inputcurrent_address,
                permanent_address=inputpermanent_address, mobile_number=inputmobile_number,
                number_whatsapp=inputnumber_whatsapp, link_facebook=inputlink_facebook,
                link_twiter=inputlink_twiter, link_instigrem=inputlink_instigrem,
            )

            # messages.success(request, 'Sector Name Updated  Successfully')
            return redirect("baseinfo")
        return render(request, 'jop/cv/baseinfo.html',  contextDate(request=request, form=form, count=None, jobs=None, djobs=None,
                                                                    job=None, formset=None,
                                                                    bankKonownData=None,
                                                                    bankKonown=None,
                                                                    disabled=None,
                                                                    employmentData=None,
                                                                    employment=None,
                                                                    experincedata=None,
                                                                    experince=None,
                                                                    coursesdata=None,
                                                                    courses=None,
                                                                    comform=None,
                                                                    computerdata=None,
                                                                    formdata=None,
                                                                    up=None,
                                                                    generaldata=None,
                                                                    baseinfo=None,
                                                                    Languageskill=None,
                                                                    orederJob=None,
                                                                    url_name="baseinfo",


                                                                    ))


def cv_edit(request):
    if islogin(request) == False:
        redirect('/login/?urlredirect='+getUrl(request))
    else:
        count = countdata(request)

        # user=Register.objects.get(id=request.session['userLoggedUserId'])
        formdata = Education.objects.filter(
            user=request.session['userLoggedUserId'])
        Languageskill = LanguageSkill.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))
        employmentData = Employment.objects.filter(
            user=request.session['userLoggedUserId'])
        bankKonownData = BankKonown.objects.filter(
            user=request.session['userLoggedUserId'])
        experincedata = Experience.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))
        coursesdata = TrainingCourses.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))
        computerdata = ComputerSkill.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))
        orederJob = oreder_Jobs.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))

        return render(request, 'jop/cv/cvedit.html',

                      contextDate(request=request, form=None, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=bankKonownData,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=employmentData,
                                  employment=None,
                                  experincedata=experincedata,
                                  experince=None,
                                  coursesdata=coursesdata,
                                  courses=None,
                                  comform=None,
                                  computerdata=computerdata,
                                  formdata=formdata,
                                  up=None,
                                  generaldata=None,
                                  baseinfo=None,
                                  Languageskill=Languageskill,
                                  orederJob=orederJob,
                                  url_name="cvedit",


                                  )
                      )


class show_cv(View):

    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)

            user = Register.objects.get(id=request.session['userLoggedUserId'])
            baseinfo = Register.objects.get(
                id=request.session['userLoggedUserId'])
            Languageskill = LanguageSkill.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))

            experincedata = Experience.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            coursesdata = TrainingCourses.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            computerdata = ComputerSkill.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            generaldata = GeneralData.objects.filter(
                user=request.session['userLoggedUserId']).first()
            print('gdata')
            return render(request, 'jop/cv/showCv.html',

                          contextDate(request=request, form=None, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=experincedata,
                                      experince=None,
                                      coursesdata=coursesdata,
                                      courses=None,
                                      comform=None,
                                      computerdata=computerdata,
                                      formdata=None,
                                      up=None,
                                      generaldata=generaldata,
                                      baseinfo=baseinfo,
                                      Languageskill=Languageskill,
                                      url_name="showCv",


                                      )
                          )

    def post(self, request):
        return get(self.request)


def baseinfoshow(request):
    if islogin(request) == False:
        return redirect('/login/?urlredirect='+getUrl(request))
    else:
        formdata = Register.objects.filter(
            id=request.session['userLoggedUserId'])
        count = countdata(request)
        # print(formdata.email)
        return render(request, 'jop/cv/baseinfo.html',
                      contextDate(url_name="baseinfo", request=request, form=None, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=None,
                                  courses=None,
                                  comform=None,
                                  computerdata=None,
                                  formdata=formdata,
                                  up=None


                                  )
                      )


def DeleteEducation(request, id):
    education = Education.objects.filter(id=id)
    education.delete()

    return redirect('education')


def UpdateEducation(request, id):
    disabled = "disabled"
    task = get_object_or_404(Education, pk=id)
    formdata = Education.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('education')
    else:
        form = EducationForm(instance=task)
    return render(request, 'jop/cv/education.html', {'disabled': disabled, 'formdata': formdata, 'form': form, 'active': 'btn-primary'})


class educationView(View):

    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            form = EducationForm()
            user = Register(id=request.session['userLoggedUserId'])
            formdata = Education.objects.filter(
                user=request.session['userLoggedUserId'])
            return render(request, 'jop/cv/education.html',
                          contextDate(url_name="education", request=request, form=form, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=None,
                                      experince=None,
                                      coursesdata=None,
                                      courses=None,
                                      comform=None,
                                      computerdata=None,
                                      formdata=formdata,
                                      up="up"


                                      )
                          )

    def post(self, request):

        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            form = EducationForm()

            return redirect('education')

        return render(request, 'jop/cv/education.html', contextDate(url_name="education", request=request, form=form, count=None, jobs=None, djobs=None,
                                                                    job=None, formset=None,
                                                                    bankKonownData=None,
                                                                    bankKonown=None,
                                                                    disabled=None,
                                                                    employmentData=None,
                                                                    employment=None,
                                                                    experincedata=None,
                                                                    experince=None,
                                                                    coursesdata=None,
                                                                    courses=None,
                                                                    comform=None,
                                                                    computerdata=None,
                                                                    formdata=None,


                                                                    ))


def DeleteLangskils(request, id):
    education = LanguageSkill.objects.filter(id=id)
    education.delete()

    return redirect('languagskills')


def UpdateLangskils(request, id):
    disabled = "disabled"
    task = get_object_or_404(LanguageSkill, pk=id)
    formdata = LanguageSkill.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = LanguageSkillFrom(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('languagskills')
    else:
        form = LanguageSkillFrom(instance=task)
        return render(request, 'jop/cv/languagskills.html',
                      contextDate(url_name="languagskills", request=request, form=form, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=disabled,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=None,
                                  courses=None,
                                  comform=None,
                                  computerdata=None,
                                  formdata=formdata,


                                  )

                      )


class LanguageSkillView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            form = LanguageSkillFrom()
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            formdata = LanguageSkill.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/languagskills.html',
                          contextDate(url_name="languagskills", request=request, form=form, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=None,
                                      experince=None,
                                      coursesdata=None,
                                      courses=None,
                                      comform=None,
                                      computerdata=None,
                                      formdata=formdata,


                                      )
                          )

    def post(self, request):
        form = LanguageSkillFrom(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            self.object.save()
            form = LanguageSkillFrom()
            formdata = LanguageSkill.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
        return render(request, 'jop/cv/languagskills.html',
                      contextDate(url_name="languagskills", request=request, form=form, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=None,
                                  courses=None,
                                  formdata=formdata,
                                  comform=None,
                                  computerdata=None,


                                  )
                      )


def DeleteComSilks(request, id):
    education = ComputerSkill.objects.filter(id=id)
    education.delete()

    return redirect('computerskills')


def UpdateComputerSkil(request, id):
    disabled = "disabled"
    task = get_object_or_404(ComputerSkill, pk=id)
    computerdata = LanguageSkill.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = ComputerSkillFrom(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('computerskills')
    else:
        comform = ComputerSkillFrom(instance=task)
        return render(request, 'jop/cv/computerkills.html',
                      contextDate(url_name="computerskills", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=disabled,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=None,
                                  courses=None,
                                  comform=comform,
                                  computerdata=computerdata,


                                  )
                      )


class ComputerSkillView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            comform = ComputerSkillFrom()
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            computerdata = ComputerSkill.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/computerkills.html',
                          contextDate(url_name="computerskills", request=request, form=None, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=None,
                                      experince=None,
                                      coursesdata=None,
                                      courses=None,
                                      comform=comform,
                                      computerdata=computerdata,


                                      )

                          )

    def post(self, request):
        computerdata = ComputerSkill.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))

        comform = ComputerSkillFrom(request.POST, request.FILES)
        if comform.is_valid():
            self.object = comform.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            comform = ComputerSkillFrom()

        return render(request, 'jop/cv/computerkills.html',
                      contextDate(url_name="computerkills", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=None,
                                  courses=None,
                                  comform=comform,
                                  computerdata=computerdata,


                                  )
                      )


def DeleteTraincoiurses(request, id):
    education = TrainingCourses.objects.filter(id=id)
    education.delete()

    return redirect('triningcourses')


def UpdateTrainingCourses(request, id):
    disabled = "disabled"
    task = get_object_or_404(TrainingCourses, pk=id)
    coursesdata = TrainingCourses.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = TrainingCoursesForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('triningcourses')
    else:
        courses = TrainingCoursesForm(instance=task)
        return render(request, 'jop/cv/triningcourses.html',
                      contextDate(url_name="triningcourses", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=disabled,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=coursesdata,
                                  courses=courses,

                                  )
                      )


class TrainingCoursesview(View):

    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            courses = TrainingCoursesForm()
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            coursesdata = TrainingCourses.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/triningcourses.html',
                          contextDate(url_name="triningcourses", request=request, form=None, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=None,
                                      experince=None,
                                      coursesdata=coursesdata,
                                      courses=courses,

                                      )
                          )

    def post(self, request):
        coursesdata = TrainingCourses.objects.filter(
            user=Register(id=request.session['userLoggedUserId']))

        courses = TrainingCoursesForm(request.POST, request.FILES)
        if courses.is_valid():
            self.object = courses.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            courses = TrainingCoursesForm()

        return render(request, 'jop/cv/triningcourses.html',
                      contextDate(url_name="triningcourses", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=None,
                                  experince=None,
                                  coursesdata=coursesdata,
                                  courses=courses,

                                  )
                      )


def DeleteExperiene(request, id):
    education = Experience.objects.filter(id=id)
    education.delete()

    return redirect('experincev')


def UpdateExperience(request, id):
    disabled = "disabled"
    task = get_object_or_404(Experience, pk=id)
    experincedata = Experience.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('experince')
    else:
        experince = ExperienceForm(instance=task)
        return render(request, 'jop/cv/experince.html',
                      contextDate(url_name="experince", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=disabled,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=experincedata,
                                  experince=experince

                                  )
                      )


class ExperienceView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            experince = ExperienceForm()
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            experincedata = Experience.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/experince.html',
                          contextDate(url_name="experince", request=request, form=None, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=None,
                                      employment=None,
                                      experincedata=experincedata,
                                      experince=experince

                                      )
                          )

    def post(self, request):
        experincedata = Experience.objects.filter(
            user=request.session['userLoggedUserId'])

        experince = ExperienceForm(request.POST, request.FILES)
        if experince.is_valid():
            self.object = experince.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            experince = ExperienceForm()

        return render(request, 'jop/cv/experince.html',
                      contextDate(url_name="experince", request=request, form=None, count=None, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=None,
                                  employment=None,
                                  experincedata=experincedata,
                                  experince=experince

                                  )
                      )


def DeleteEmployment(request, id):
    education = Employment.objects.filter(id=id)
    education.delete()

    return redirect('employment')


def UpdateEmployment(request, id):
    disabled = "disabled"
    task = get_object_or_404(Employment, pk=id)
    count = countdata(request)
    employmentData = Employment.objects.filter(
        user=request.session['userLoggedUserId'])

    if request.method == 'POST':
        form = EmploymentForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('employment')
    else:
        employment = EmploymentForm(instance=task)
        return render(request, 'jop/cv/employment.html',

                      contextDate(url_name="employment", request=request, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=employmentData,
                                  employment=employment,
                                  form=employment

                                  )
                      )


class EmploymentView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            employment = EmploymentForm()
            count = countdata(request)
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            employmentData = Employment.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/employment.html',
                          contextDate(url_name="employment", request=request, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=None,
                                      bankKonown=None,
                                      disabled=None,
                                      employmentData=employmentData,
                                      employment=employment,
                                      form=employment

                                      )
                          )

    def post(self, request):
        employmentData = Employment.objects.filter(
            user=request.session['userLoggedUserId'])

        employment = EmploymentForm(request.POST, request.FILES)
        if employment.is_valid():
            self.object = employment.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            employment = EmploymentForm()
            count = countdata(request)

        return render(request, 'jop/cv/employment.html',
                      contextDate(url_name="employment", request=request, form=employment, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=None,
                                  bankKonown=None,
                                  disabled=None,
                                  employmentData=employmentData,
                                  employment=employment,

                                  )
                      )


def Deletebanknow(request, id):
    education = BankKonown.objects.filter(id=id)
    education.delete()

    return redirect('BankKonown')


def UpdateBankKonown(request, id):
    disabled = "disabled"
    task = get_object_or_404(BankKonown, pk=id)
    bankKonownData = BankKonown.objects.filter(
        user=request.session['userLoggedUserId'])
    count = countdata(request)

    if request.method == 'POST':
        form = BankKonownForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('BankKonown')
    else:
        bankKonown = BankKonownForm(instance=task)
        return render(request, 'jop/cv/BankKonown.html',
                      contextDate(url_name="BankKonown", request=request, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=bankKonownData,
                                  bankKonown=bankKonown,
                                  disabled=disabled,
                                  form=bankKonown,
                                  )
                      )


class BankKonownView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            bankKonown = BankKonownForm()
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            bankKonownData = BankKonown.objects.filter(
                user=Register(id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/BankKonown.html',
                          contextDate(url_name="BankKonown", request=request, count=count, jobs=None, djobs=None,
                                      job=None, formset=None,
                                      bankKonownData=bankKonownData,
                                      bankKonown=bankKonown,
                                      form=bankKonown,
                                      )
                          )

    def post(self, request):
        bankKonownData = BankKonown.objects.filter(
            user=request.session['userLoggedUserId'])

        bankKonown = BankKonownForm(request.POST, request.FILES)
        if bankKonown.is_valid():
            self.object = bankKonown.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            messages.success(
                request, 'Congratualtions !! lauguage save Successfully')
            bankKonown = BankKonownForm()
            count = countdata(request)

        return render(request, 'jop/cv/BankKonown.html',
                      contextDate(url_name="BankKonown", request=request, form=bankKonown, count=count, jobs=None, djobs=None,
                                  job=None, formset=None,
                                  bankKonownData=bankKonownData,
                                  bankKonown=bankKonown
                                  )
                      )


class GeneralDataView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            try:
                count = countdata(request)
                g = GeneralData.objects.filter(
                    user=Register(id=request.session['userLoggedUserId'])).first()
                form = GeneralDataForm(instance=g)
            except GeneralData.DoesNotExist:
                form = GeneralDataForm()

            return render(request, 'jop/cv/general_data.html', contextDate(url_name="generaldata", request=request, form=form, count=count, jobs=None, djobs=None,
                                                                           job=None, formset=None,
                                                                           ))

    def post(self, request):
        try:
            g = GeneralData.objects.filter(
                user=Register(id=request.session['userLoggedUserId'])).first()
            form = GeneralDataForm(request.POST, request.FILES, instance=g)
        except GeneralData.DoesNotExist:
            g = None  # Set g to None if the object doesn't exist
        formsave = GeneralDataForm(
            request.POST, request.FILES, instance=g)
        if formsave.is_valid():
            self.object = formsave.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            self.object.save()
            messages.success(request, 'Data saved successfully!')
        g = GeneralData.objects.filter(
            user=Register(id=request.session['userLoggedUserId'])).first()

        form = GeneralDataForm(
            request.POST, request.FILES, instance=g)

        return render(request, 'jop/cv/general_data.html', contextDate(url_name="generaldata", request=request, form=form, count=None, jobs=None, djobs=None,
                                                                       job=None, formset=None,
                                                                       ))


class JobsOfferedView(View):
    def get(self, request):
        if islogin(request) == False:
            return redirect('/login/?urlredirect='+getUrl(request))
        else:
            count = countdata(request)
            user = Register.objects.get(id=request.session['userLoggedUserId'])
            job = oreder_Jobs.objects.filter(user=Register(
                id=request.session['userLoggedUserId']))
            return render(request, 'jop/cv/Jobs_offered.html', contextDate(url_name="Jobs_offered", request=request, job=job, count=count))

    def post(self, request):
        jobs = oreder_Jobs.objects.filter(
            user=request.session['userLoggedUserId'])

        job = OrderJobForm(request.POST, request.FILES)
        if job.is_valid():
            self.object = job.save(commit=False)
            self.object.user = Register(id=request.session['userLoggedUserId'])
            # usr = request.user
            self.object.save()
            # messages.success(
            #     request, 'Congratualtions !! lauguage save Successfully')
            job = OrderJobForm()

        return render(request, 'jop/cv/Jobs_offered.html', contextDate(url_name="Jobs_offered", request=request, job=job))
