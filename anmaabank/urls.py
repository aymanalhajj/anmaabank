from django.shortcuts import render, redirect
from django.conf.urls import (handler400, handler403, handler404, handler500)
from anmaabankApp import viewaccount
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import
from django.conf.urls.static import static
from django.conf import settings
from jopapp.viewsaccount import register, ProfileRegistration, login, userLogout
from django.views.generic.base import TemplateView  # import TemplateView

from jopapp.viewcv import Baseinfo

from jopapp.viewcv import *
from jopapp.views import *

urlpatterns = []

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,

                      document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler400 = 'anmaabankApp.views.page_not_found'
handler403 = 'anmaabankApp.views.page_not_found'
handler404 = 'anmaabankApp.views.page_not_found'
handler500 = 'anmaabankApp.views.page_not_found'
urlpatterns += [
    # path('admin-web/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),  # Here's the typo
    # path(settings.STATIC_URL, include('jopapp.urls'), name="job-app"),
    # re_path(r'(?P<lang>\bar\b|\ben\b)', include('anmaabankApp.urls')),
    path('', include('anmaabankApp.urls')),
    path('admin', include('AdminApp.urls')),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/login/$", login, name='login-user'),
    path("login/", login, name='login-user'),
    path("userLogout/login/", login, name='userLogout-user'),
    path("userLogout/", userLogout, name='userLogout'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/userLogout$", userLogout, name='userLogout'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/createaccoute$", ProfileRegistration.as_view(), name='createaccoute-user'),
    # path("createaccoute/", ProfileRegistration.as_view(), name='createaccoute-user'),
    path("createaccoute/", ProfileRegistration.as_view(), name='createaccounte'),
    # re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/$", include('jopapp.urls'), name="job-app"),
     re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/admin/$", customadmin.as_view(), name='home-jop-manage-admin'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/$", vacancies.as_view(), name='home-jop'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/baseinfo/$", Baseinfo.as_view(), name="baseinfo"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/education/$", educationView.as_view(), name='education'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/education/deleteeducation/<int:id>$",         DeleteEducation, name='deleteeducation'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/languagskills/DeleteLangskils/<int:id>$",         DeleteLangskils, name='DeleteLangskils'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/computerskills/DeleteComSilks/<int:id>$",         DeleteComSilks, name='DeleteComSilks'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/triningcourses/DeleteTraincoiurses/<int:id>$",         DeleteTraincoiurses, name='DeleteTraincoiurses'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/experincev/DeleteExperiene/<int:id>$",         DeleteExperiene, name='DeleteExperiene'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/employment/DeleteEmployment/<int:id>$",         DeleteEmployment, name='DeleteEmployment'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/BankKonown/Deletebanknow/<int:id>$",         Deletebanknow, name='Deletebanknow'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/education/UpdateEducation/<int:id>$",         UpdateEducation, name='UpdateEducation'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/languagskills/UpdateLangskils/<int:id>$",         UpdateLangskils, name='UpdateLangskils'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/computerskills/UpdateComputerSkil/<int:id>$",         UpdateComputerSkil, name='UpdateComputerSkil'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/triningcourses/UpdateTrainingCourses/<int:id>$",         UpdateTrainingCourses, name='UpdateTrainingCourses'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/experince/UpdateExperience/<int:id>$",         UpdateExperience, name='UpdateExperience'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/employment/UpdateEmployment/<int:id>$",         UpdateEmployment, name='UpdateEmployment'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/BankKonown/UpdateBankKonown/<int:id>$",         UpdateBankKonown, name='UpdateBankKonown'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/OrderJob/<int:id>$$", OrderJobView.as_view(), name='OrderJob'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/ruic_bank/$", ruicbank, name='ruic_bank'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/introcation_job/$", introcationjob, name='introcation_job'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/detail/<int:id>$", detail, name='job-singles'),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/education/$", educationView.as_view(), name="education"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/languagskills/$", LanguageSkillView.as_view(), name="languagskills"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/computerskills/$", ComputerSkillView.as_view(), name="computerskills"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/triningcourses/$", TrainingCoursesview.as_view(), name="triningcourses"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/experince/$", ExperienceView.as_view(), name="experince"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/employment/$", EmploymentView.as_view(), name="employment"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/BankKonown/$", BankKonownView.as_view(), name="BankKonown"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/show_cv/$", show_cv.as_view(), name="show_cv"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/show_cv$", show_cv.as_view(), name="show_cv"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/cvedit/$", cv_edit, name="cvedit"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/generaldata/$", GeneralDataView.as_view(), name="generaldata"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/jobsoffered/$", JobsOfferedView.as_view(), name="jobsoffered"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/filedupload/$", FileUploadView.as_view(), name="filedupload"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/forgetpassword/$", send_message_email.as_view(), name="forgetpassword"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/passswordrest/$", PasswordResetView.as_view(), name="passswordrest"),
    re_path(r"^(?P<lang>\bar\b|\ben\b)/jobs/passwordchange/$", Changepassword.as_view(), name="passwordchange"),
    # re_path("jobs/", include('jopapp.urls'), name="job-app"),
    path("select2/", include("django_select2.urls")),
    path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path("robots.txt", TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),  
    # add the robots.txt file
    # path('account/', include('allauth.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # path('tinymce/', include('tinymce.urls')),
    path('tinymce/', include('tinymce.urls')),  # new
    path('selectable/', include('selectable.urls')),
    path("select2/", include("django_select2.urls")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt",content_type="text/plain"), name="robots.txt"),
    path("eth/login/", viewaccount.LoginView.as_view(), name="login-eth"),
    path("eth/logout/", viewaccount.LogoutView.as_view(), name="logout-eth"),
    path("password_change/", viewaccount.PasswordChangeView.as_view(), name="password_change-eth"),
    path("eth/password_change/done/",viewaccount.PasswordChangeDoneView.as_view(),name="password_change_done-eth",),
    path("eth/password_reset/", viewaccount.PasswordResetView.as_view(),name="password_reset-eth"),
    path("eth/password_reset/done/",viewaccount.PasswordResetDoneView.as_view(),name="password_reset_done-eth",),
    path("eth/reset/<uidb64>/<token>/",viewaccount.PasswordResetConfirmView.as_view(),name="password_reset_confirm-eth",),
    path("eth/reset/done/",viewaccount.PasswordResetCompleteView.as_view(),name="password_reset_complete-eth",),
]


def handler404(request, *args, **argv):
    return redirect('home')
