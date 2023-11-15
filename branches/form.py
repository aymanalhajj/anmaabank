from cProfile import label
from django import forms
from django.forms import ModelForm

from .models import SerchModel

from django_select2.forms import Select2Widget


class SerchModelForm(forms.ModelForm):
    class Meta:

        model = SerchModel
        fields = "__all__"
        widgets = {
            'region': Select2Widget
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
        icons = {
            'passowrd': 'bi bi-pass-fill ',
            #  'active': 'fas fa-lock',
            #  'deactivate': 'bi bi-phone ',
            'phone_whatsapp': 'bi bi-whatsapp ',
            'Phone_Number': 'bi bi-phone ',
            'category': 'bi bi-person-circle ',
            'region': 'bi bi-flag-fill',
            'search': 'bi bi-search ',
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

        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', icons)
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
