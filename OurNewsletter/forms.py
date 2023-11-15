from django import forms
from .models import *
from django_select2.forms import Select2Widget
# from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = [

            "name",
            "Phone_Number",
            #  "Phone_Number",
            "phone_whatsapp",
            "country",
            "emile",
            #   "subject",
            "Message",
            # "captcha",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-control'}),
            'Phone_Number': forms.NumberInput(attrs={'class': 'form-control input-control'}),
            'Message': forms.Textarea(attrs={'class': 'form-control input-control'}),
            'country': Select2Widget(attrs={'class': 'form-control input-control'}),
        }

    def __init__(self, *args, **kwargs):
        icons = {
            'passowrd': 'bi bi-pass-fill ',
            #  'active': 'fas fa-lock',
            #  'deactivate': 'bi bi-phone ',
            'phone_whatsapp': 'bi bi-whatsapp ',
            'Phone_Number': 'bi bi-phone ',
            'name': 'bi bi-person-circle ',
            'country': 'bi bi-flag-fill',
            'emile': 'bi bi-envelope ',
            #  'mobile_number': 'bi bi-phone ',
            #  'brand_logo': 'bi bi-card-image ',
            #  'business': 'bi bi-building-fill ',
            #  'street': 'bi bi-phone ',
            'Message': 'bi bi-chat-left-fill',
            #  'city': 'bi bi-phone ',
            #  'region': 'bi bi-phone ',
            #  'postcode': 'bi bi-phone ',
            #  'country': 'bi bi-phone ',
            #  'website': 'bi bi-phone ',
            #  'description': 'bi bi-phone ',
            #  'account_name': 'bi bi-phone ',
            #  'opportunity_amount': 'bi bi-phone ',
            #  'is_active': 'bi bi-phone ',
            #  'enquiry_type': 'bi bi-phone ',
            #  'created_from_site': 'bi bi-phone ',
            #  'org': 'bi bi-phone ',
            #  'company': 'bi bi-phone ',
            #  'skype_ID': 'bi bi-phone ',
            #  'industry': 'bi bi-phone ',
            #  'organization': 'bi bi-phone ',
            #  'close_date': 'bi bi-phone ',
            #  'source': 'bi bi-phone ',
            #  'linkedin': 'bi bi-phone ',
            #  'twitter': 'bi bi-phone ',
            #  'spend': 'bi bi-phone ',
            #  'state': 'bi bi-phone ',
            #  'value': 'bi bi-phone ',
            #  'uniqueid': 'bi bi-phone ',
            #  'budget': 'bi bi-phone ',
            #  'open_date':'bi bi-phone ',
            #  'facebook': 'bi bi-phone ',
            #  'priority': 'bi bi-phone ',
            #  'companyemail': 'bi bi-phone ',
            #  'companyindustry': 'bi bi-phone ',
            #  'companyname': 'bi bi-phone ',
            #  'companyphone': 'bi bi-phone ',
            #  'addressline1': 'bi bi-phone ',
            #  'companysize': 'bi bi-phone ',
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
            #  'notes': 'bi bi-phone ',
        }

        super(ContactForm, self).__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', icons)

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs.update({'placeholder': field.label})
            #  field.widget.attrs.update({'placeholder': field.label})
            # field.widget.attrs.update({'label': field.label})
            field.label = ""
            if field_name in icons:
                field.icon = icons[field_name]

        self.fields['name'].required = True
        self.fields['Phone_Number'].required = True
        # self.fields['subject'].required = True
        self.fields['Message'].required = True
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")


class OurNewsletterForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = OurNewsletter
        fields = [
            # "name",
            "emile",
            #   "subject",
            #   "Message",
            # "captcha"
        ]
        # error_messages = {'emile': {'required': 'الرجاء كتابة اللغة', 'unique': 'الايميل موجود من سابق ', },
        #                 #   'emile': { },

        #                   }
    def __init__(self, *args, **kwargs):

        super(OurNewsletterForm, self).__init__(*args, **kwargs)

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs.update({'label': field.label})
            field.label = ""

        # self.fields['name'].required = True
        self.fields['emile'].required = True
        self.fields['emile'].label = ""
        # self.fields['emile'].label = ""
        # self.fields['emile'].required = True

        # self.fields['subject'].required = True
        # self.fields['Message'].required = True
