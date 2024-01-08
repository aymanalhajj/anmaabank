
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


from .viewcv import *
from .views import *

urlpatterns = [
    path("", vacancies.as_view(), name='home-jop'),
    path("admin/", customadmin.as_view(), name='home-jop-manage-admin'),
    path("admin", customadmin.as_view(), name='home-jop-manage-admins'),
    path("admin/<int:id>", customadmin.as_view(),name='home-jop-manage-admin-detil'),
    path("message_bank/", message_bank, name='message_bank'),
    path("puocedures_job/", puocedures_job, name='puocedures_job'),
    path("vacancies/", vacancies.as_view(), name='vacancies'),
    path("what_gion_bank/", what_gion_bank, name='what_gion_bank'),
    path("strategy_bank/", strategy_bank, name='strategy_bank'),
    path("purpose_bank/", purpose_bank, name='purpose_bank'),
    path("values_principles/", valuesprinciples, name='values_principles'),
    path("education/", educationView.as_view(), name='education'),
    path("education/deleteeducation/<int:id>",         DeleteEducation, name='deleteeducation'),
    path("languagskills/DeleteLangskils/<int:id>",         DeleteLangskils, name='DeleteLangskils'),
    path("computerskills/DeleteComSilks/<int:id>",         DeleteComSilks, name='DeleteComSilks'),
    path("triningcourses/DeleteTraincoiurses/<int:id>",         DeleteTraincoiurses, name='DeleteTraincoiurses'),
    path("experincev/DeleteExperiene/<int:id>",         DeleteExperiene, name='DeleteExperiene'),
    path("employment/DeleteEmployment/<int:id>",         DeleteEmployment, name='DeleteEmployment'),
    path("BankKonown/Deletebanknow/<int:id>",         Deletebanknow, name='Deletebanknow'),
    path("education/UpdateEducation/<int:id>",         UpdateEducation, name='UpdateEducation'),
    path("languagskills/UpdateLangskils/<int:id>",         UpdateLangskils, name='UpdateLangskils'),
    path("computerskills/UpdateComputerSkil/<int:id>",         UpdateComputerSkil, name='UpdateComputerSkil'),
    path("triningcourses/UpdateTrainingCourses/<int:id>",         UpdateTrainingCourses, name='UpdateTrainingCourses'),
    path("experince/UpdateExperience/<int:id>",         UpdateExperience, name='UpdateExperience'),
    path("employment/UpdateEmployment/<int:id>",         UpdateEmployment, name='UpdateEmployment'),
    path("BankKonown/UpdateBankKonown/<int:id>",         UpdateBankKonown, name='UpdateBankKonown'),
    path("OrderJob/<int:id>", OrderJobView.as_view(), name='OrderJob'),
    path("ruic_bank/", ruicbank, name='ruic_bank'),
    path("introcation_job/", introcationjob, name='introcation_job'),
    # path('detail/<int:id>', detail, name='job-singles'),
    path('education/', educationView.as_view(), name="education"),
    path('languagskills/', LanguageSkillView.as_view(), name="languagskills"),
    path('computerskills/', ComputerSkillView.as_view(), name="computerskills"),
    path('triningcourses/', TrainingCoursesview.as_view(), name="triningcourses"),
    path('experince/', ExperienceView.as_view(), name="experince"),
    path('employment/', EmploymentView.as_view(), name="employment"),
    path('BankKonown/', BankKonownView.as_view(), name="BankKonown"),
    path('show_cv/', show_cv.as_view(), name="show_cv"),
    path('show_cv', show_cv.as_view(), name="show_cv"),
    path('cvedit/', cv_edit, name="cvedit"),
    path('generaldata/', GeneralDataView.as_view(), name="generaldata"),
    path('jobsoffered/', JobsOfferedView.as_view(), name="jobsoffered"),
    path('filedupload/', FileUploadView.as_view(), name="filedupload"),
    path('baseinfo/', Baseinfo.as_view(), name="baseinfo"),
    path('forgetpassword/', send_message_email.as_view(), name="forgetpassword"),
    path('passswordrest/', PasswordResetView.as_view(), name="passswordrest"),
    path('passwordchange/', Changepassword.as_view(), name="passwordchange"),
    # path("details_jobs/", detailsjobs.as_view(), name='details_jobs'),
#     path("/", vacancies.as_view(), name='home-jops'),
#     re_path(r"^(?P<lang>\bar\b|\ben\b)/baseinfo/$", Baseinfo.as_view(), name="baseinfo"),
#     path('<str:lang>/baseinfo/', Baseinfo.as_view(), name="baseinfo"),
    #  path('<int:id>',Baseinfo,name="editEduation"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
