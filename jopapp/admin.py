from django.contrib import admin

from .models import *


class RegisterAdmin(admin.ModelAdmin):
    list_display = (

        'username', 'full_name', 'email', 'password', 'gender', 'governorate', 'city', 'address', 'village',
        'idnumber', 'Release_date', 'place_issue', 'date_birth', 'place_birth', 'marital_status', 'number_childer',
        'current_address', 'permanent_address', 'mobile_number', 'number_whatsapp', 'link_facebook', 'link_twiter', 'link_instigrem',

    )
    list_filter = (
        'username', 'full_name', 'email', 'password', 'gender', 'governorate', 'city', 'address', 'village',
        'idnumber', 'Release_date', 'place_issue', 'date_birth', 'place_birth', 'marital_status', 'number_childer',
        'current_address', 'permanent_address', 'mobile_number', 'number_whatsapp', 'link_facebook', 'link_twiter', 'link_instigrem',

    )
    date_hierarchy = 'created_at'


class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        # 'order_num',
        'description',
        'created_at',
        # 'image',
        'task',
        # 'task1',
        # 'task2',
        # 'task3',
        'conditions',
        # 'conditions1',
        # 'conditions2',
        # 'conditions3',
    )
    list_filter = (
        # 'id',
        # 'name',
        'type',
        # 'order_num',
        'description',
        'created_at',
        # 'image',
        'task',
        # 'task1',
        # 'task2',
        # 'task3',
        'conditions',
        # 'conditions1',
        # 'conditions2',
        # 'conditions3',
    )
    date_hierarchy = 'created_at'


class OrderJobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'oreder_message',
        'how_to_now_job',
        'user',
        'job',
        'created_at',
    )
    list_filter = (
        'id',
        # 'oreder_message',
        'how_to_now_job',
        'user',
        'job',
        'created_at',

    )
    search_fields = ('job',)


class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name_educational_institution',
        'country',
        'sducation_level',
        'specialization',
        'rate',
        'From_Date',
        'To_date',
        'create_at',
        'user'
    )
    list_filter = (
        'id',
        'name_educational_institution',
        'country',
        'sducation_level',
        'specialization',
        'rate', 'From_Date',
        'To_date',
        'create_at',
        'user'
    )

    search_fields = ('name_educational_institution',)


class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_language',
        'reading',
        'writing',
        'conversation',

        'user',

        'create_at',

    )

    list_filter = (
        'id',
        'name_language',
        'reading',
        'writing',
        'conversation',

        'user',
        'create_at',

    )

    search_fields = ('name_language',)


class ComputerSkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'level',

        'user',

        'create_at',

    )

    list_filter = (
        'id',
        'name',
        'level',

        'user',
        'create_at',

    )


class TrainingCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_institute',
        'name_courses',
        'country',
        'From_Date',
        'To_date',
        'create_at',
        'user',

    )

    list_filter = (
        'id',
        'name_institute',
        'name_courses',
        'From_Date',
        'country',
        'To_date',
        'create_at',
        'user'

    )

    search_fields = ('name_institute',)


class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name_word',
        'name_shop',
        'name_owner',
        'From_Date',
        'To_date',
        'address',
        'mobile',
        'task',
        'name_job_start',
        'name_job_end',
        'salary_start',
        'salary_end',
        'working_hours',
        'resson_leaving',
        'create_at',
        'user',
    )
    list_filter = (
        'id',
        'name_word',
        'name_shop',
        'name_owner',
        'From_Date',
        'To_date',
        'address',
        'mobile',
        'task',
        'name_job_start',
        'name_job_end',
        'salary_start',
        'salary_end',
        'working_hours',
        'resson_leaving',
        'create_at',
        'user'

    )

    search_fields = ('name_word',)


class EmploymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',

        'create_at',
        'user'
    )
    list_filter = (
        'id',
        'name',

        'create_at',
        'user'

    )

    search_fields = ('name',)


class BankKonownAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'relative',
        'address',
        'working',
        'mobile',
        'create_at',
        'user'

    )
    list_filter = (
        'name',
        'relative',
        'address',
        'working',
        'mobile',
        'create_at',
        'user'
    )


class GeneralDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'work_bank', 'receive_email',
        'file_civil_service',
        'spend_working',
        'purchasing_visa',
        'traveling', 'currently_working',
        'Current_working_phone',
        'Current_work_address',
        'currently_studying',
        'work_night',
        'start_working',
        'lowest_salary',
        'health_problems',
        'hobbies',
        'person_closest',
        'person_closest_Phone', 'relative_relation',
        'person_closest_address',
        'name_village_justice',
        'village_justice_Telephon',
        'village_justice_address',
        'manage_business', 'ready_work',
        'government_job',
        'source_financial_income', 'proficient_English',
        'have_illness',
        'graduation_certificate',
        'graduation_certificate_dispaly',
        'create_at',
        'user'
    )
    list_filter = (
        'id',
        'create_at',
        'user'
    )

# Register your models here.


# def _register(model, admin_class):
#     admin.site.register(model, admin_class)
# _register(Jobs, JobsAdmin)
admin.site.register(Jobs, JobsAdmin)

admin.site.register(Register, RegisterAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(LanguageSkill, LanguageSkillAdmin)
admin.site.register(ComputerSkill, ComputerSkillAdmin)
admin.site.register(TrainingCourses, TrainingCoursesAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(BankKonown, BankKonownAdmin)
admin.site.register(oreder_Jobs, OrderJobAdmin)
admin.site.register(GeneralData, GeneralDataAdmin)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


class BirthDataAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'country',
        'cookie',
        'region',
        'directorate',
        'isolation',
    )
    list_filter = (
        'country',
        'region',
        'directorate',
        'isolation',
        'id',
        'cookie',
    )


class AddressLocationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'country_address',
        'cookie',
        'region_address',
        'directorate_address',
        'isolation_address',
        'street',
        'nearest_branch',
        'nearest_outstanding_landmark',
        'accommodation_type',
    )
    list_filter = (
        'country_address',
        'region_address',
        'directorate_address',
        'isolation_address',
        'id',
        'cookie',
        'street',
        'nearest_branch',
        'nearest_outstanding_landmark',
        'accommodation_type',
    )


class IdentificationCardAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'cookie',
        'full_name',
        'id_number',
        'birth_date',
        'id_issuance_date',
        'id_expiry_date',
        'image_front',
        'image_back',
        'gender',
        'nationality_amrican',
        'have_nationality',
        'nationality',
        'nationality_othar',
        'maritalـstatus',
        'educational_level',
        'specialization',
    )
    list_filter = (
        'birth_date',
        'id_issuance_date',
        'id_expiry_date',
        'nationality_amrican',
        'have_nationality',
        'id',
        'cookie',
        'full_name',
        'id_number',
        'image_front',
        'image_back',
        'gender',
        'nationality',
        'nationality_othar',
        'maritalـstatus',
        'educational_level',
        'specialization',
    )


class SignUpValideteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quality_score',
        'email',
        'is_valid_format',
        'code',
        'user',
        # 'objects',
        # 'emile',
        'create_at',
        # 'note',
        # 'Date_Update',
        # 'Date_Added',
    )


class RequestToOpenAccountAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'cookie',
        # 'id_card',
        'country',
        'phone_whatsapp',
        'Phone_Number',
        'emile',
        'cookie',
        'note',
        'Date_Update',
        'Date_Added',
    )
    list_filter = (
        # 'birth_data',
        # 'address_location',
        # 'id_card',
        # 'country',
        'Date_Update',
        'Date_Added',
        'user',

        # 'id',
        # 'phone_whatsapp',
        # 'Phone_Number',
        # 'emile',
        # 'cookie',
        # 'note',
    )


_register(BirthData, BirthDataAdmin)
_register(AddressLocation, AddressLocationAdmin)
_register(IdentificationCard, IdentificationCardAdmin)
_register(RequestToOpenAccount, RequestToOpenAccountAdmin)

_register(SignUpValidete, SignUpValideteAdmin)
