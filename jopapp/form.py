from cProfile import label
from django import forms
from django.forms import ModelForm
from .models import BankKonown, ComputerSkill, Education, Employment, Experience, GeneralData, Jobs, LanguageSkill, Register, TrainingCourses, oreder_Jobs
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation

# from datetime import datetime
from django import forms
from django.db.models.fields import IntegerField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, NumberInput
from country_regions.models import Country, Region, Directorate, Isolation
from dal import autocomplete  # don't forget to pip install django-querysetsequence
from django.forms import CharField, MultiValueField
from django.core.validators import RegexValidator
# from selectable.forms import AutoCompleteWidget,AutoCompleteSelectWidget
import selectable.forms as selectable
from .models import *
import datetime
from selectable.base import ModelLookup
from selectable.registry import registry
from OurNewsletter.models import *

from dal_queryset_sequence.fields import QuerySetSequenceModelField

from dal_select2_queryset_sequence.views import Select2QuerySetSequenceAutoView
from dal_select2_queryset_sequence.widgets import QuerySetSequenceSelect2

from django.urls import re_path as url
from django_select2 import forms as s2forms

from queryset_sequence import QuerySetSequence
from django_select2.forms import Select2Widget
# from django_select2.forms import Select2Widget
from .models import SerchJobsModel, loginModel


def iconsdata():
    return {
        'isolation_address': 'bi bi-flag-fill',
        'isolation': 'bi bi-flag-fill',
        'active': 'fas fa-lock',
        'deactivate': 'bi bi-phone ',
        'street': 'bi bi-geo',
        'accommodation_type': 'bi bi bi-building ',
        # 'nearest_branch': 'bi bi-bookmark-plus-fill ',
        'passowrd': 'bi bi-pass-fill ',
        #  'active': 'fas fa-lock',
        #  'deactivate': 'bi bi-phone ',
        'phone_whatsapp': 'bi bi-whatsapp ',
        'Phone_Number': 'bi bi-phone ',
        'name': 'bi bi-person-circle ',
        'country': 'bi bi-globe-asia-australia',
        'emile': 'bi bi-envelope ',
        'email': 'bi bi-envelope ',
        'gender': 'bi bi-gender-trans',

        'nearest_branch': 'bi bi-geo-fill ',
        'nearest_outstanding_landmark': 'bi bi-pin-map',
        'name': 'bi bi-person-circle ',
        'country_address': 'bi bi-globe-asia-australia',
        # 'country': 'bi bi-flag-fill',

        'directorate_address': 'bi bi-flag-fill',
        'directorate': 'bi bi-flag-fill',
        'region': 'bi bi-flag',
        'region_address': 'bi bi-flag',
        'brand_logo': 'bi bi-card-image ',
        'business': 'bi bi-building-fill ',
        'street': 'bi bi-geo',
        'full_name': 'bi bi-person-vcard-fill',
        'id_number': 'bi bi-credit-card-2-front-fill',
        'idnumber': 'bi bi-credit-card-2-front-fill',
        'birth_date': 'bi bi-calendar-date',
        'id_issuance_date': 'bi bi-calendar-date',
        'Release_date': 'bi bi-calendar-date',
        'place_issue': 'bi bi-calendar-date',
        'place_birth': 'bi bi-geo',
        'number_childer': 'bi bi-person-hearts',

        'date_birth': 'bi bi-calendar-date',

        'id_expiry_date': 'bi bi-calendar-date',
        'Message': 'bi bi-chat-left-fill',
        'note': 'bi bi-chat-left-fill',

        'postcode': 'bi bi-phone ',
        'website': 'bi bi-website ',
        'description': 'bi bi-chat-left-fill ',
        'account_name': 'bi bi-phone ',
        'opportunity_amount': 'bi bi-phone ',
        'is_active': 'bi bi-phone ',
        'enquiry_type': 'bi bi-phone ',
        'created_from_site': 'bi bi-phone ',
        'org': 'bi bi-phone ',
        'company': 'bi bi-phone ',
        'skype_ID': 'bi bi-phone ',
        'industry': 'bi bi-phone ',
        'organization': 'bi bi-phone ',
        'close_date': 'bi bi-phone ',
        'source': 'bi bi-phone ',
        'linkedin': 'bi bi-linkedin ',
        'twitter': 'bi bi-twitter ',
        'link_twiter': 'bi bi-twitter ',
        'link_facebook': 'bi bi-facebook',
        'current_address': 'bi bi-geo',
        'permanent_address': 'bi bi-geo',
        # 'number_whatsapp':'bi bi-geo',
        'number_whatsapp': 'bi bi-whatsapp ',
        'mobile_number': 'bi bi-phone ',
        'twitter': 'bi bi-twitter ',
        'link_instigrem': 'bi bi-instagram ',

        'instigrem': 'bi bi-instagram',
        'spend': 'bi bi-phone ',
        'state': 'bi bi-phone ',
        'value': 'bi bi-phone ',
        'uniqueid': 'bi bi-phone ',
        'budget': 'bi bi-phone ',
        'open_date': 'bi bi-phone ',
        'facebook': 'bi bi-phone ',
        'priority': 'bi bi-phone ',
        'companyemail': 'bi bi-phone ',
        'companyindustry': 'bi bi-phone ',
        'companyname': 'bi bi-phone ',
        'companyphone': 'bi bi-phone ',
        'addressline1': 'bi bi-phone ',
        'companysize': 'bi bi-phone ',
        'notes': 'bi bi-phone ',
        'educational_level': 'bi bi-journal-code',
        'nationality': 'bi bi-globe-asia-australia',
        'have_nationality': 'bi bi-globe-asia-australia',
        'nationality_othar': 'bi bi-globe-asia-australia',
        'nationality_amrican': 'bi bi-globe-americas',
        "language": "bi bi-translate",
        'name_language': "bi bi-translate",

        'otharـname_language': "bi bi-translate",
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
        #  'notes': 'bi bi-phone ',
    }
# super(AddressLocationForm, self).__init__(*args, **kwargs)


class LoginModelForm(forms.ModelForm):
    class Meta:

        model = loginModel
        fields = ["email", "password", 're_member_me', "right_privecy"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            're_member_me': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'right_privecy': forms.CheckboxInput(attrs={'class': 'form-control'}),

            # 'job':  Select2Widget(attrs={'class': 'form-control'}),
            # 'specialization': Select2Widget(attrs={'class': 'form-control'}),
        }

        # fields = [

        #     'id',
        #     'name',
        #     'type',
        #     'order_num',
        #     'description',
        #     # 'created_at',
        #     'image',
        #     'task',
        #     # 'task1',
        #     # 'task2',
        #     # 'task3',
        #     'conditions',
        #     # 'conditions1',
        #     # 'conditions2',
        #     # 'conditions3',
        # ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            # field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class SerchModelForm(forms.ModelForm):
    class Meta:

        model = SerchJobsModel
        fields = "__all__"
        widgets = {
            'job':  Select2Widget(attrs={'class': 'form-control'}),
            'specialization': Select2Widget(attrs={'class': 'form-control'}),
            'gender': Select2Widget(attrs={'class': 'form-control'}),
            'all_data': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }

        # fields = [

        #     'id',
        #     'name',
        #     'type',
        #     'order_num',
        #     'description',
        #     # 'created_at',
        #     'image',
        #     'task',
        #     # 'task1',
        #     # 'task2',
        #     # 'task3',
        #     'conditions',
        #     # 'conditions1',
        #     # 'conditions2',
        #     # 'conditions3',
        # ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'input-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class AuthorWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
        "namear__icontains",
    ]


class PhoneField(MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            "incomplete": "Enter a country calling code and a phone number.",
        }
        # Or define a different message for each field.
        fields = (
            CharField(
                error_messages={"incomplete": "Enter a country calling code."},
                validators=[
                    RegexValidator(
                        r"^[0-9]+$", "Enter a valid country calling code."),
                ],
            ),
            CharField(
                error_messages={"incomplete": "Enter a phone number."},
                validators=[RegexValidator(
                    r"^[0-9]+$", "Enter a valid phone number.")],
            ),
            CharField(
                validators=[RegexValidator(
                    r"^[0-9]+$", "Enter a valid extension.")],
                required=False,
            ),
        )
        super().__init__(
            error_messages=error_messages,
            fields=fields,
            require_all_fields=False,
            **kwargs
        )


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class ModelJobs(ModelForm):
    class Meta:

        model = Jobs
        # fields = "__all__"

        fields = [

            'id',
            'name',
            'type',
            # 'order_num',
            'description',
            # 'created_at',
            # 'image',
            'task',
            # 'task1',
            # 'task2',
            # 'task3',
            'conditions',
            # 'conditions1',
            # 'conditions2',
            # 'conditions3',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class OrderJobForm(ModelForm):
    class Meta:
        model = oreder_Jobs
        fields = [
            'oreder_message',
            'how_to_now_job',
        ]
        labels = {'how_to_now_job': 'كيف عرفت أن لدينا وظيفة شاغرة:',
                  'oreder_message': ''}
        help_texts = {'oreder_message': 'Some useful help text.',
                      'how_to_now_job': 'Some useful help text.', },
        error_messages = {
            'oreder_message': {'required': 'يجب إدخال الاسم كاملاً', },
            'how_to_now_job': {'required': 'يجب إدخال البريد الإلكتروني بشكل صحيح', },
        },
        widgets = {
            'oreder_message': forms.Textarea(attrs={'cols': 40, 'rows': 15, 'name': 'body', 'class': 'form-control'}),
            #    'how_to_now_job': forms.Select(attrs={'class': 'form-control'}),
            'how_to_now_job': Select2Widget(attrs={'class': 'form-control'}),


        }

        def clean_text_area(self):
            data = self.cleaned_data['oreder_message']
            letter_count = len([char for char in data if char.isalpha()])
            return letter_count


class RegisterForm(ModelForm):

    class Meta:
        model = Register
        # fields = "__all__"\

        fields = [

            'username', 'full_name', 'email', 'password', 'confirmpassword', 'gender', 'governorate', 'city', 'address', 'village',
            'idnumber', 'Release_date', 'place_issue', 'date_birth', 'place_birth', 'marital_status', 'number_childer',
            'current_address', 'permanent_address', 'mobile_number', 'number_whatsapp', 'link_facebook', 'link_twiter', 'link_instigrem',
        ]
        labels = {'username': _('اسم المستخدم'),
                 'full_name': 'الاسم الكامل :',
                  'email': 'البريد الإلكتروني:', 
                  'password': 'كلمة السر:',
                  'confirmpassword': 'تأكيد كلمة السر:', 
                  'gender': 'الجنس:', 
                  'governorate': 'المحافظة:',
                  'city': 'المدينة/المديرية:',  'address': 'العزلة/الشارع:', 'village': 'القرية/الحي:',
                  'idnumber': 'رقم البطاقة:', 'Release_date': 'تاريخ الإصدار:', 'place_issue': 'مكان الإصدار:',
                  'date_birth': 'تاريخ الميلاد:', 'place_birth': 'محل الميلاد:', 'marital_status': 'الحالة الاجتماعية:',
                  'number_childer': 'عدد من تعولهم:', 'current_address': 'العنوان الحالي:',
                  'permanent_address': 'عنوان السكن الدائم:', 'mobile_number': 'رقم الموبايل:',
                  'number_whatsapp': 'رقم الواتساب:', 'link_facebook': 'صفحتك على الفيسبوك:',
                  'link_twiter': 'صفحتك على التويتر:', 'link_instigrem': 'صفحتك على الإنستجرام:',

                  }
        help_texts = {'username': 'Some useful help text.', 'full_name': 'Some useful help text.',
                      'email': 'Some useful help text.', 'password': 'Some useful help text.',
                      'confirmpassword': 'Some useful help text.', 'gender': 'Some useful help text.',
                      'governorate': 'Some useful help text.', 'city': 'Some useful help text.',
                      'address': 'Some useful help text.', 'village': 'Some useful help text.',
                      'idnumber': 'Some useful help text.', 'Release_date': 'Some useful help text.',
                      'place_issue': 'Some useful help text.', 'place_birth': 'Some useful help text.',
                      'date_birth': 'Some useful help text.', 'number_childer': 'Some useful help text.',
                      'marital_status': 'Some useful help text.', 'current_address': 'Some useful help text.',
                      'permanent_address': 'Some useful help text.', 'mobile_number': 'Some useful help text.',
                      'number_whatsapp': 'Some useful help text.', 'link_facebook': 'Some useful help text.',
                      'link_twiter': 'Some useful help text.', 'link_instigrem': 'Some useful help text.', },
        error_messages = {'username': {'required': 'يجب ادخال اسم المستخدم', },
                          'full_name': {'required': 'يجب إدخال الاسم كاملاً', },
                          'email': {'required': 'يجب إدخال البريد الإلكتروني بشكل صحيح', },
                          'password': {'required': 'يجب إدخال كلمة السر', }, 'confirmpassword': {'required': 'يجب إعادة كتابة كلمة السر', },
                          'gender': {'required': 'sdfsdafdsfdssd', }, 'governorate': {'required': 'يجب اختيار المدينة', },
                          'city': {'required': 'يجب ادخال اسم المدينة/ المديرية', }, 'address': {'required': 'الرجاء ادخال اسم الشارع / العزلة', },
                          'village': {'required': 'الرجاء اسم الحي / القرية', }, 'idnumber': {'required': 'الرجاء رقم البطاقة', },
                          'Release_date': {'required': 'الرجاء ادخال تاريخ الإصدار', }, 'place_issue': {'required': 'الرجاء ادخال مكان الإصدار', },
                          'date_birth': {'required': 'الرجاء ادخال تاريخ الميلاد', }, 'place_birth': {'required': 'الرجاء ادخال مكان الميلاد', },
                          'marital_status': {'required': 'الرجاء تحديد الحالة الاجتماعية', }, 'number_childer': {'required': 'sdfsdafdsfdssd', },
                          'current_address': {'required': 'الرجاء تحديد العنوان الحالي', }, 'permanent_address': {'required': 'الرجاء تحديد عنوان السكن الدائم بالتفصيل', },
                          'mobile_number': {'required': 'الرجاء تحديد عنوان السكن الدائم بالتفصيل', }, 'number_whatsapp': {'required': 'الرجاء تحديد عنوان السكن الدائم بالتفصيل', },

                          }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmpassword': forms.PasswordInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control'}),
            # 'governorate': forms.Select(attrs={'class': 'form-control'}),
            'governorate': Select2Widget(attrs={'class': 'form-control'}),

            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'idnumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'Release_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'place_issue': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'place_birth': forms.TextInput(attrs={'class': 'form-control'}),
            # 'marital_status': forms.(attrs={'class': 'form-control'}),
            'number_childer': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_address': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_whatsapp': forms.NumberInput(attrs={'class': 'form-control'}),
            'link_facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'link_twiter': forms.TextInput(attrs={'class': 'form-control'}),

            'link_instigrem': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class uploadCvForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['cv_uploaded_file']
        labels = {'cv_uploaded_file': 'ملف السيرة الذاتية'}
        help_texts = {'cv_uploaded_file': 'file cv', },
        error_messages = {'cv_uploaded_file': {'required': '   ارفع ملف السيرة الذاتية', },
                          }
        widgets = {'cv_uploaded_file': forms.FileInput(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class PasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        # Add additional validation rules for password strength if needed


class EmploymentForm(forms.ModelForm):

    class Meta:
        model = Employment
        fields = ['name']
        labels = {'name': _('مجال العمل'), }
        help_texts = {'name': 'Some useful help text.', },
        error_messages = {'name': {'required': 'الرجاء كتابة مجال العمل', },
                          }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education

        fields = ['name_educational_institution', 'country', 'sducation_level', 'specialization',
                  "othar_specialization", 'rate', 'uploaded_image', 'From_Date', 'To_date']
        widgets = {
            # 'name_educational_institution':forms.TextInput(attrs={'class': 'form-control'}),
            # 'country': forms.Select(attrs={ 'class': 'form-control'}),
            #    'sducation_level': forms.TextInput(attrs={'class': 'form-control'}),
            #    'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            #    'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            #    'uploaded_image': forms.FileInput(attrs={'class': 'form-control'}),
            'country': Select2Widget(attrs={'class': 'form-control'}),
            'specialization': Select2Widget(attrs={'class': 'form-control'}),
            'sducation_level': Select2Widget(attrs={'class': 'form-control'}),
            'name_language': Select2Widget(attrs={'class': 'form-control'}),
            'From_Date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'To_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}), }
        labels = {'name_educational_institution': _(' اسم المؤسسة التعليمية:'),
                  'country': ' البلد:',
                  #   'sducation_level':'  المستوى التعليمي:',
                  'specialization': 'التخصص:',
                  'From_Date': 'من تاريخ :',
                  'rate': ' المعدل:',
                  'uploaded_image': 'شهادة التخرج',
                  'To_date': ' إلى تاريخ :',

                  }
        error_messages = {'name_educational_institution': {'required': 'الرجاء كتابة اسم المؤسسة التعليمية', },
                          'country': {'required': 'يرجى اختيار اسم البلد', },
                          'sducation_level': {'required': 'الرجاء كتابة المستوى التعليمي', },
                          'specialization': {'required': '   الرجاء كتابة التخصص', },
                          'From_Date': {'required': 'يجب تحديد تاريخ البداية', },
                          'rate': {'required': ' إدخال المعدل', },
                          # 'uploaded_image': {'required':' قم برفع شهادة التخرج ',  },
                          'To_date': {'required': '   يجب تحديد تاريخ النهاية', }

                          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class LanguageSkillFrom(forms.ModelForm):
    class Meta:
        model = LanguageSkill
        fields = ['name_language', "otharـname_language",
                  'reading', 'writing', 'conversation']
        widgets = {
            # 'name_language':forms.TextInput(attrs={'class': 'form-control'}),
            # 'reading': forms.Select(attrs={'class': 'form-control'}),
            # 'writing': forms.Select(attrs={'class': 'form-control'}),
            'reading': Select2Widget(attrs={'class': 'form-control'}),
            'writing': Select2Widget(attrs={'class': 'form-control'}),
            'conversation': Select2Widget(attrs={'class': 'form-control'}),
            'name_language': Select2Widget(attrs={'class': 'form-control'}),

            # 'conversation': forms.Select(attrs={'class': 'form-control'}),
        }

        error_messages = {'name_language': {'required': 'الرجاء كتابة اللغة', },
                          'reading': {'required': 'الرجاء كتابة مستوى القراءة', },
                          'writing': {'required': ' الرجاء كتابة مستوى الكتابة  ', },
                          'conversation': {'required': '   الرجاء كتابة مستوى المحادثة  ', },

                          }
        labels = {'name_language': _('   اللغة:'),
                  'reading': 'مستوى القراءة:',
                  'writing': '  مستوى الكتابة :',
                  'conversation': 'مستوى المحادثة:',


                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class ComputerSkillFrom(forms.ModelForm):
    class Meta:
        model = ComputerSkill
        fields = ['name', 'level']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   #    'level': forms.Select(attrs={'class': 'form-control'}),
                   'level': Select2Widget(attrs={'class': 'form-control'}),
                   #    'writing': Select2Widget(attrs={'class': 'form-control'}),
                   #    'conversation': Select2Widget(attrs={'class': 'form-control'}),
                   }
        error_messages = {'name': {'required': '  يجب إدخال اسم المهارة', },
                          'level': {'required': '   الرجاء كتابة مستوى الإجادة', },

                          }
        labels = {'name': _('   اسم المهارة:'),
                  'level': 'مستوى الإجادة :',



                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class TrainingCoursesForm(forms.ModelForm):
    class Meta:
        model = TrainingCourses
        fields = ['name_institute', 'name_courses',
                  'country', 'From_Date', 'To_date']
        widgets = {'name_institute': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_courses': forms.TextInput(attrs={'class': 'form-control'}),
                   #    'country': forms.Select(attrs={'class': 'form-control'}),
                   'country': Select2Widget(attrs={'class': 'form-control'}),

                   'From_Date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
                   'To_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),


                   }
        error_messages = {'name_institute': {'required': ' الرجاء كتابة اسم المعهد ', },
                          'name_courses': {'required': 'الرجاء كتابة اسم الدورة   ', },
                          'country': {'required': 'الرجاء اختيار اسم البلد ', },
                          'From_Date': {'required': '   يجب تحديد تاريخ البداية     ', },
                          'To_date': {'required': '     يجب تحديد تاريخ النهاية   ', },

                          }
        labels = {'name_institute': _('   اسم المعهد:'),
                  'name_courses': 'اسم الدورة :',
                  'country': '  البلد:',
                  'From_Date': 'من تاريخ:',
                  'To_date': 'إلى تاريخ:',


                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['name_word', 'name_shop', 'name_owner', 'From_Date', 'To_date', 'address',
                  'mobile', 'task', 'name_job_start', 'name_job_end', 'salary_start', 'salary_end',
                  'working_hours', 'resson_leaving']
        widgets = {'name_word': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_owner': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_shop': forms.TextInput(attrs={'class': 'form-control'}),
                   'From_Date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
                   'To_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'mobile': forms.TextInput(attrs={'class': 'form-control'}),
                   'task': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_job_start': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_job_end': forms.TextInput(attrs={'class': 'form-control'}),
                   'salary_start': forms.TextInput(attrs={'class': 'form-control'}),
                   'salary_end': forms.TextInput(attrs={'class': 'form-control'}),
                   'working_hours': forms.TextInput(attrs={'class': 'form-control'}),
                   'resson_leaving': forms.DateInput(attrs={'class': 'form-control'}),


                   }

        error_messages = {'name_word': {'required': 'الرجاء ادخال اسم العمل', },
                          'name_owner': {'required': 'يجب كتابة اسم صاحب العمل  ', },
                          'name_shop': {'required': 'يجب كتابة اسم الجهة أو اسم المحل', },
                          'From_Date': {'required': '  يجب تحديد بداية تاريخ العمل  ', },
                          'To_date': {'required': '    يجب تحديد تاريخ الانتهاء من العمل  ', },
                          'address': {'required': 'الرجاء ادخال عنوان العمل', },
                          'mobile': {'required': '    يجب ادخال تلفون العمل    ', },
                          'task': {'required': '     يجب تحدي المهام  ', },
                          'name_job_start': {'required': 'الرجاء كتابة المسمى الوظيفي في البداية', },
                          'name_job_end': {'required': '   الرجاء كتابة المسمى الوظيفي في النهاية   ', },
                          'salary_start': {'required': '     يجب تحديد تاريخ النهاية   ', },
                          'working_hours': {'required': '   الرجاء كتابة عدد ساعات العمل    ', },
                          'resson_leaving': {'required': '    يرجى كتابة سبب ترك العمل  ', },
                          'salary_end': {'required': '   يرجى ادخال الراتب في النهاية  ', },

                          }
        labels = {'name_word': _('  اسم العمل:'),
                  'name_owner': 'اسم صاحب العمل:',

                  'name_shop': 'اسم المحل/الجهة:',
                  'From_Date': 'من تاريخ:',
                  'To_date': 'إلى تاريخ:',
                  'address': '  عنوان العمل:',
                  'mobile': ' تلفون العمل:',
                  'task': 'المهام :',
                  'name_job_start': '  المسمى الوظيفي في البداية:',
                  'name_job_end': 'المسمى الوظيفي في النهاية: :',
                  'salary_start': ' الراتب في البداية:',
                  'salary_end': 'الراتب في النهاية:',
                  'working_hours': 'عدد ساعات العمل:',
                  'resson_leaving': '  سبب ترك العمل::',


                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class BankKonownForm(forms.ModelForm):
    class Meta:
        model = BankKonown
        fields = ['name', 'relative', 'working', 'mobile', 'address']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),

                   'relative': forms.TextInput(attrs={'class': 'form-control'}),
                   'working': forms.TextInput(attrs={'class': 'form-control'}),
                   'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
                   }
        error_messages = {'name': {'required': ' يجب إدخال الاسم', },
                          'relative': {'required': 'يجب كتابة صلة القرابة  ', },
                          'working': {'required': 'يجب ادخال العمل', },
                          'mobile': {'required': '  يجب ادخال التلفون    ', },
                          'address': {'required': '   الرجاء كتابة العنوان'},
                          }
        labels = {'name': _('   الاسم:'),
                  'relative': 'صلة القرابة:',
                  'working': '  العمل:',
                  'mobile': ' التلفون:',
                  'address': 'العنوان: :',



                  }

    def __init__(self, *args, **kwargs):
        super(BankKonownForm, self).__init__(*args, **kwargs)

        icons = getattr(self.Meta, 'icons', iconsdata())

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            if field_name in icons:
                field.icon = icons[field_name]
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs.update({'placeholder': field.label})

            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class GeneralDataForm(forms.ModelForm):
    class Meta:
        model = GeneralData
        fields = ['work_bank', 'receive_email', 'file_civil_service', 'spend_working', 'purchasing_visa', 'traveling', 'currently_working', 'Current_working_phone', 'Current_work_address', 'currently_studying', 'work_night', 'start_working', 'lowest_salary',
                  'health_problems', 'hobbies', 'person_closest', 'person_closest_Phone', 'relative_relation', 'person_closest_address', 'name_village_justice',
                  'village_justice_Telephon', 'village_justice_address', 'manage_business', 'ready_work',
                  'government_job', 'source_financial_income', 'proficient_English', 'have_illness', 'graduation_certificate', "graduation_certificate_file"]
        labels = {'work_bank': 'هل سبق لك العمل في الانماء:', 'receive_email': 'هل تريد استقبال بريد إلكتروني من البنك :', 'file_civil_service': 'هل قدمت ملفك للخدمة المدنية؟ ', 'spend_working': 'ما هي المدة التي تفكر في قضائها بالعمل لدينا؟ :',
                  'purchasing_visa': 'هل تفكر بشراء فيزا للعمل في الخارج؟ :', 'traveling': 'هل تمانع من السفر في إطار العمل إذا تطلب الأمر؟ :', 'currently_working': 'مالعمل الذي تقوم به حالياً:', 'Current_working_phone': 'تلفون العمل الحالي:',
                  'Current_work_address': 'عنوان العمل الحالي:', 'currently_studying': 'هل تدرس حاليا :', 'work_night': 'هل أنت مستعد للعمل ليلاً ؟:',
                  'start_working': 'متى تستطيع البدء بالعمل ؟:', 'lowest_salary': 'ما هو أقل راتب يمكنك أن تقبل به شاملاً جميع البدلات :',
                  'health_problems': 'هل لديك مشاكل صحية؟ :', 'hobbies': 'ماهي هواياتك ؟ :', 'person_closest': 'اسم أقرب شخص لك', 'person_closest_Phone': 'رقم تلفونه :', 'relative_relation': 'صلة القرابة :', 'person_closest_address': 'عنوانه:', 'name_village_justice': 'اسم عدل القرية',
                  'village_justice_Telephon': 'رقم تلفون :', 'village_justice_address': 'عنوانه :', 'manage_business': 'هل تمتلك او تدير اي مشروع تجاري خاص بك؟',
                  'ready_work': 'هل انت مستعد للعمل في اي محافظة وفي اي فرع من فروع المصرف في الجمهورية؟',
                  'government_job': 'هل لديك وظيفة حكومية؟', 'source_financial_income': 'هل لديك اي مصدر دخل مالي؟',
                  'proficient_English': 'هل تتقن اللغة الانجليزية (كتابة وقراءة ومحادثة)',
                  'have_illness': 'هل لديك اي مرض دائم أو إعاقة؟',
                  'graduation_certificate': 'هل حصلت على شهادة التخرج ؟',
                  'graduation_certificate_file': 'ارفع شهادة التخرج ان وجدت',
                  }
        widgets = {'work_bank': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'receive_email': forms.TextInput(attrs={'class': 'form-control'}),
                   'file_civil_service': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'spend_working': forms.TextInput(attrs={'class': 'form-control'}),
                   'purchasing_visa': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'traveling': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'currently_working': forms.TextInput(attrs={'class': 'form-control'}),
                   'Current_working_phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'Current_work_address': forms.TextInput(attrs={'class': 'form-control'}),
                   'currently_studying': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'work_night': forms.RadioSelect(attrs={'style': 'display: inline-block'}),
                   'start_working': forms.TextInput(attrs={'class': 'form-control'}),
                   'lowest_salary': forms.NumberInput(attrs={'class': 'form-control'}),
                   'health_problems': forms.TextInput(attrs={'class': 'form-control'}),
                   'hobbies': forms.TextInput(attrs={'class': 'form-control'}),
                   'person_closest': forms.TextInput(attrs={'class': 'form-control'}),
                   'person_closest_Phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'relative_relation': forms.TextInput(attrs={'class': 'form-control'}),
                   'person_closest_address': forms.TextInput(attrs={'class': 'form-control'}),
                   'name_village_justice': forms.TextInput(attrs={'class': 'form-control'}),
                   'village_justice_Telephon': forms.NumberInput(attrs={'class': 'form-control'}),
                   'village_justice_address': forms.TextInput(attrs={'class': 'form-control'}),
                   'manage_business': forms.TextInput(attrs={'class': 'form-control'}),
                   'ready_work': forms.TextInput(attrs={'class': 'form-control'}),
                   'government_job': forms.TextInput(attrs={'class': 'form-control'}),
                   'source_financial_income': forms.TextInput(attrs={'class': 'form-control'}),
                   'proficient_English': forms.TextInput(attrs={'class': 'form-control'}),
                   'have_illness': forms.TextInput(attrs={'class': 'form-control'}),
                   'graduation_certificate': forms.TextInput(attrs={'class': 'form-control'}),
                   #    'graduation_certificate_file': forms.FileField(attrs={'class': 'form-control'})




                   }
        error_messages = {

            'currently_working': {'required': 'الرجاء كتابة العمل الذي تقوم به الان ', },
            'Current_working_phone': {'required': ' الرجاء ادخال رقم تلفون العمل الحالي', },
            'Current_work_address': {'required': 'الرجاء كتابة عنوان العمل الحالي ', },
            'currently_studying': {'required': ' ', },
            'work_night': {'required': ' ', },
            'start_working': {'required': ' ', },
            'lowest_salary': {'required': ' يجب كتابة أقل راتب تتوقعه شاملاً جميع البدلات', },
            'health_problems': {'required': ' ', },
            'hobbies': {'required': 'الرجاء كتابة هواياتك ', },
            'person_closest': {'required': ' الرجاء كتابة أقرب شخص إليك', },
            'person_closest_Phone': {'required': ' الرجاء كتابة رقم تلفون قريبك', },
            'relative_relation': {'required': ' يرجى كتابة صلة القرابة', },
            'person_closest_address': {'required': 'الرجاء كتابة عنوان قريبك ', },
            'name_village_justice': {'required': 'الرجاء كتابة اسم عاقل الحارة أو عدل القرية ', },
            'village_justice_Telephon': {'required': 'الرجاء كتابة تلفون العاقل / العدل ', },
            'village_justice_address': {'required': 'الرجاء كتابة عنوان العاقل / العدل ', },
            'manage_business': {'required': 'هل تمتلك او تدير اي مشروع تجاري خاص بك؟الرجاء كتابة ', },
            'ready_work': {'required': 'هل انت مستعد للعمل في اي محافظة وفي اي فرع من فروع المصرف في الجمهورية؟الرجاء كتابة ', },
            'government_job': {'required': ' هل لديك وظيفة حكومية؟الرجاء كتابة', },
            'source_financial_income': {'required': ' هل لديك اي مصدر دخل مالي؟الرجاء كتابة', },
            'proficient_English': {'required': ' هل تتقن اللغة الانجليزية (كتابة وقراءة ومحادثة)الرجاء كتابة', },
            'have_illness': {'required': ' هل لديك اي مرض دائم أو إعاقة؟الرجاء كتابة', },
            'graduation_certificate': {'required': 'هل حصلت على شهادة التخرج ؟الرجاء كتابة ', },



        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]


class CountryLookup(ModelLookup):
    model = Country
    # search_fields = ('name_ar__icontains','name__icontains' ,)
    search_fields = ('name_ar__icontains', 'name__icontains',
                     'code3__icontains', 'phone')
# registry.register(CountryLookup)


class RegionLookup(ModelLookup):
    model = Region
    # search_fields = ('name_ar__icontains','name__icontains' ,)
    search_fields = ('name_ar__icontains', 'name__icontains',
                     'country__name_ar__icontains', 'country__name__icontains', 'country__code2__icontains', 'country__code3__icontains', 'country__phone__icontains',
                     )


class DirectorateLookup(ModelLookup):
    model = Directorate
    # search_fields = ('name_ar__icontains','name__icontains' ,)
    search_fields = ('name_ar__icontains', 'name__icontains',
                     'region__country__name_ar__icontains', 'region__country__name__icontains',
                     'region__name_ar__icontains', 'region__name__icontains',

                     )


class IsolationLookup(ModelLookup):
    model = Isolation
    # search_fields = ('name_ar__icontains','name__icontains' ,)
    search_fields = ('name_ar__icontains', 'name__icontains',
                     'directorate__region__country__name_ar__icontains', 'directorate__region__country__name__icontains', 'directorate__region__country__code2__icontains', 'directorate__region__country__code3__icontains', 'directorate__region__country__phone__icontains',
                     'directorate__region__name_ar__icontains', 'directorate__region__name__icontains', 'directorate__region__code2__icontains', 'directorate__region__code3__icontains', 'directorate__region__phone__icontains',
                     'directorate__name_ar__icontains', 'directorate__name__icontains', 'directorate__code2__icontains', 'directorate__code3__icontains', 'directorate__phone__icontains',

                     )


    # search_fields = ('name_ar__icontains','name__icontains' ,'display_name__icontains','display_name_ar__icontains',
    #                  'country__name_ar__icontains','country__name__icontains' ,'country__display_name__icontains','country__display_name_ar__icontains','country__code2__icontains','country__code3__icontains','country__phone__icontains',
    #                   )
# registry.register(CountryLookup)
registry.register(RegionLookup)
registry.register(CountryLookup)
registry.register(DirectorateLookup)
registry.register(IsolationLookup)


attrs = {"data-selectable-allow-new": True,
         # "aria-haspopup":True,
         # "role":"searchbox",
         "tabindex": 1,
         # "type":"text",
         "autocomplete": "off",
         "aria-autocomplete": "search",
         "data-selectable-type": "search",
         "data-ajax--cache": True,
         "data-allow-clear": True,
         "data-selectable-options": {'highlightMatch': False,

                                     'minLength': 0}}


class BirthDataForm(forms.ModelForm):
    # country = selectable.AutoCompleteSelectField(
    #     lookup_class=CountryLookup,
    #     label='الدولة',
    #     required=True,

    #     widget=selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs)
    # )

    # countrys = Country.objects.filter()
    # country = Select2GenericForeignKeyModelField(
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Country, 'name_ar', ),
    #                       (Region, 'name_ar', ),
    #                    ],
    #     )

    # country = forms.Select(
    #     # label='الدولة',
    #     # choices=  Country.objects.filter(),
    #     choices=
    #     # required=True,
    # )
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Region, 'name_ar', ),
    #                    ],
    #     )
    # Phone_Number = PhoneField()
    # country = forms.ComboField(
    #     label="الدولة",
    #     # max_length=254,
    #     fields=country,
    #     # widget=forms.CharField(attrs={"autocomplete": "email"}),
    # )
    class Meta:
        model = BirthData
        fields = "__all__"
        # autocomplete_fields = ['country',"region"]
        # raw_id_fields = ('country',

        #  )
        from django.contrib.admin.widgets import AutocompleteSelect

        widgets = {
            'cookie': forms.HiddenInput(),
            'user': forms.HiddenInput(
            ),
            'objects': forms.HiddenInput(
            ),
            # "country":AuthorWidget,
            # "region":AuthorWidget
            'country': Select2Widget(attrs={'class': 'form-control'}),
            'isolation': Select2Widget(attrs={'class': 'form-control'}),
            'directorate': Select2Widget(attrs={'class': 'form-control'}),

            # 'country_address': Select2Widget(attrs={'class': 'form-control'}),
            'region': Select2Widget(attrs={'class': 'form-control'}),

            # 'isolation_address': Select2Widget(attrs={'class': 'form-control'}),
            # "directorate_address": Select2Widget(attrs={'class': 'form-control'}),
            # "isolation_address": Select2Widget(attrs={'class': 'form-control'}),
            # "country":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup),
            #  "isolation":selectable.AutoComboboxSelectWidget(lookup_class=IsolationLookup,attrs=attrs),
            #  "directorate":selectable.AutoComboboxSelectWidget(lookup_class=DirectorateLookup,attrs=attrs),

            # "region":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup,attrs=attrs),
            # "region":AutocompleteSelect(
            #          BirthData._meta.get_field('region').remote_field,
            #             admin.site,
            #             choices=Region.objects.all(),
            #             attrs={'data-dropdown-auto-width': 'true', "class":"select2 select2-container select2-container--admin-autocomplete select2-container--below select2-container--open select2-container--focus"}
            # Region._meta.get_field('name_ar').remote_field,
            # admin.site,
            # attrs={'data-dropdown-auto-width': 'true', 'style': "width: 100%;"}
            # ),
        }

    def __init__(self, *args, **kwargs):

        super(BirthDataForm, self).__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            if field_name in icons:
                field.icon = icons[field_name]
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")
        # self.base_fields['cookie'].widget = forms.HiddenInput()
        # self.base_fields['service'].widget = forms.HiddenInput()
        # self.fields['country'].required = True
        # self.fields['directorate'].required = True
        # self.fields['region'].required = False
        # self.fields['isolation'].required = True
        # self.fields['service'].disabled = True
        # self.fields['cookie'].disabled = True

        # self.fields['Message'].required = True

        # fields  = ['description','unit_price','quantity']


class AddressLocationForm(forms.ModelForm):
    # country = selectable.AutoCompleteSelectField(
    #     lookup_class=CountryLookup,
    #     label='الدولة',
    #     required=True,

    #     widget=selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs)
    # )

    # countrys = Country.objects.filter()
    # country = Select2GenericForeignKeyModelField(
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Country, 'name_ar', ),
    #                       (Region, 'name_ar', ),
    #                    ],
    #     )

    # country = forms.Select(
    #     # label='الدولة',
    #     # choices=  Country.objects.filter(),
    #     choices=
    #     # required=True,
    # )
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Region, 'name_ar', ),
    #                    ],
    #     )
    # Phone_Number = PhoneField()
    # country = forms.ComboField(
    #     label="الدولة",
    #     # max_length=254,
    #     fields=country,
    #     # widget=forms.CharField(attrs={"autocomplete": "email"}),
    # )
    class Meta:
        model = AddressLocation
        fields = "__all__"
        # autocomplete_fields = ['country',"region"]

        # from django.contrib.admin.widgets import AutocompleteSelect

        widgets = {
            'cookie': forms.HiddenInput(),
            'user': forms.HiddenInput(
            ),
            'objects': forms.HiddenInput(
            ),

            'country_address': Select2Widget(attrs={'class': 'form-control'}),
            'region_address': Select2Widget(attrs={'class': 'form-control'}),

            'isolation_address': Select2Widget(attrs={'class': 'form-control'}),
            "directorate_address": Select2Widget(attrs={'class': 'form-control'}),
            "isolation_address": Select2Widget(attrs={'class': 'form-control'}),
            # "isolation_address":Select2Widget(attrs={'class': 'form-control'}),

            # "country":AuthorWidget,
            # "region":AuthorWidget
            # "country":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup),
            #  "isolation":selectable.AutoComboboxSelectWidget(lookup_class=IsolationLookup,attrs=attrs),
            #  "directorate":selectable.AutoComboboxSelectWidget(lookup_class=DirectorateLookup,attrs=attrs),

            # "region":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup,attrs=attrs),
            # "region":AutocompleteSelect(
            #          BirthData._meta.get_field('region').remote_field,
            #             admin.site,
            #             choices=Region.objects.all(),
            #             attrs={'data-dropdown-auto-width': 'true', "class":"select2 select2-container select2-container--admin-autocomplete select2-container--below select2-container--open select2-container--focus"}
            # Region._meta.get_field('name_ar').remote_field,
            # admin.site,
            # attrs={'data-dropdown-auto-width': 'true', 'style': "width: 100%;"}
            # ),
        }

    def __init__(self, *args, **kwargs):

        super(AddressLocationForm, self).__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())

        field_names = [field_name for field_name, _ in self.fields.items()]
        # for field_name, field in self.fields.items():
        #     field = self.fields.get(field_name)
        #     field.widget.attrs.update({'placeholder': field.label})
        #     field.widget.attrs.update({'placeholder': field.label})
        #     #  field.widget.attrs.update({'placeholder': field.label})
        #     field.label = ""

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            if field_name in icons:
                field.icon = icons[field_name]
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country_address'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")
        # self.base_fields['cookie'].widget = forms.HiddenInput()
        # self.base_fields['service'].widget = forms.HiddenInput()
        # self.fields['country'].required = True
        # self.fields['directorate'].required = True
        # self.fields['region'].required = False
        # self.fields['isolation'].required = True
        # self.fields['service'].disabled = True
        # self.fields['cookie'].disabled = True

        # self.fields['Message'].required = True

        # fields  = ['description','unit_price','quantity']


class IdentificationCardForm(forms.ModelForm):
    # country = selectable.AutoCompleteSelectField(
    #     lookup_class=CountryLookup,
    #     label='الدولة',
    #     required=True,

    #     widget=selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs)
    # )

    # birth_date = forms.DateField(
    #     label="تاريخ الميلاد",
    #     # max_length=254,
    #     # fields=C,
    #     # widget=forms.CharField(attrs={"autocomplete": "email"}),
    # )
    # countrys = Country.objects.filter()
    # country = Select2GenericForeignKeyModelField(
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Country, 'name_ar', ),
    #                       (Region, 'name_ar', ),
    #                    ],
    #     )

    # country = forms.Select(
    #     # label='الدولة',
    #     # choices=  Country.objects.filter(),
    #     choices=
    #     # required=True,
    # )
    #         # Model with values to filter, linked with the name field
    #         model_choice=[(Region, 'name_ar', ),
    #                    ],
    #     )
    # Phone_Number = PhoneField()
    # country = forms.ComboField(
    #     label="الدولة",
    #     # max_length=254,
    #     fields=country,
    #     # widget=forms.CharField(attrs={"autocomplete": "email"}),
    # )
    class Meta:
        model = IdentificationCard
        fields = "__all__"
        # autocomplete_fields = ['country',"region"]
        # raw_id_fields = ('country',

        #                  )
        # from django.contrib.admin.widgets import AutocompleteSelect

        widgets = {
            'cookie': forms.HiddenInput(),
            'user': forms.HiddenInput(
            ),
            'objects': forms.HiddenInput(
            ),
            # "birth_date": forms.DateInput(

            # ),
            'name_language': Select2Widget(attrs={'class': 'form-control'}),
            'educational_level': Select2Widget(attrs={'class': 'form-control'}),

            'specialization': Select2Widget(attrs={'class': 'form-control'}),
            "maritalـstatus": Select2Widget(attrs={'class': 'form-control'}),
            # "region":AuthorWidget
            # "country":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup),
            #  "isolation":selectable.AutoComboboxSelectWidget(lookup_class=IsolationLookup,attrs=attrs),
            #  "directorate":selectable.AutoComboboxSelectWidget(lookup_class=DirectorateLookup,attrs=attrs),

            # "region":selectable.AutoComboboxSelectWidget(lookup_class=RegionLookup,attrs=attrs),
            # "region":AutocompleteSelect(
            #          BirthData._meta.get_field('region').remote_field,
            #             admin.site,
            #             choices=Region.objects.all(),
            #             attrs={'data-dropdown-auto-width': 'true', "class":"select2 select2-container select2-container--admin-autocomplete select2-container--below select2-container--open select2-container--focus"}
            # Region._meta.get_field('name_ar').remote_field,
            # admin.site,
            # attrs={'data-dropdown-auto-width': 'true', 'style': "width: 100%;"}
            # ),
        }

    def __init__(self, *args, **kwargs):

        super(IdentificationCardForm, self).__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())

        self.fields['birth_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        self.fields['id_issuance_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        self.fields['id_expiry_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            if field_name in icons:
                field.icon = icons[field_name]

        # self.base_fields['cookie'].widget = forms.HiddenInput()
        # self.base_fields['service'].widget = forms.HiddenInput()
        # self.fields['country'].required = True
        # self.fields['directorate'].required = True
        # self.fields['region'].required = False
        # self.fields['isolation'].required = True
        # self.fields['service'].disabled = True
        # self.fields['cookie'].disabled = True

        # self.fields['Message'].required = True

        # fields  = ['description','unit_price','quantity']


class RequestToOpenAccountForm(forms.ModelForm):
    # nationality_amrican = forms.ComboField(
    #     # attrs=attrs,
    #     # choices=[(False, "لا"), (True, "نعم"),],
    # ),
    # country = forms.ModelChoiceField(queryset=Country.objects.all(),
    #                                  widget=selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs),
    #                                  label="الدولة",

    #                                  )

    # gender = forms.RadioSelect(choices=[('M', "ذكر"), ("F", "انثى")],initial="M",
    #  label="الجنس"
    #  )
    # nationality_amrican = forms.ChoiceField(choices=[(False, "لا"), (True, "نعم")],initial=False,
    #    label="الجنس"
    #    )
    class Meta:
        model = RequestToOpenAccount
        # fields = ["name",
        #           "Phone_Number",
        #           "emile",
        #           "Message",
        #         #   "service",
        #           "cookie",
        #           ]
        fields = "__all__"
        # raw_id_fields = ('birth_data',

        #              )
        widgets = {
            'cookie': forms.HiddenInput(),
            # 'birth_data': forms.HiddenInput(
            # ),
            # 'address_location': forms.HiddenInput(
            # ),
            'user': forms.HiddenInput(),
            'objects': forms.HiddenInput(),
            'gender': forms.RadioSelect(),
            # 'nationality'
            'nationality': Select2Widget(attrs={'class': 'form-control'}),
            'country': Select2Widget(attrs={'class': 'form-control'}),
            # 'nationality': Select2Widget(attrs={'class': 'form-control'}),


            # 'id_card': forms.HiddenInput(
            # ),
            # "nationality":selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs),
            # "country":selectable.AutoComboboxSelectWidget(lookup_class=CountryLookup,attrs=attrs),
            # 'nationality_amrican': forms.NullBooleanSelect(),

        }

    def __init__(self, *args, **kwargs):

        super(RequestToOpenAccountForm, self).__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', iconsdata())

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            if field_name in icons:
                field.icon = icons[field_name]
        self.fields['cookie'].widget = forms.HiddenInput()
        # self.fields['nationality_othar'].widget = forms.HiddenInput()
        # self.fields['specialization'].widget = forms.HiddenInput()

        # self.base_fields['service'].widget = forms.HiddenInput()
        # self.fields['id_card'].required = True
        # self.fields['Phone_Number'].required = True
        # self.fields['emile'].required = False
        # self.fields['note'].required = False
        # self.fields['service'].disabled = True
        self.fields['cookie'].disabled = True
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")
        # self.fields['nationality'].disabled = True

        # self.fields['Message'].required = True
