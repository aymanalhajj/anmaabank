
from .models import *
from django import forms
from django.db.models.fields import IntegerField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, NumberInput
from django_select2.forms import Select2Widget

# from servicesapp.models import *


class ServiceRequestsForm(forms.ModelForm):

    class Meta:
        model = ServiceRequests
        fields = ["name",
                  "Phone_Number",
                  "phone_whatsapp",
                  "country",
                  "emile",
                  "Message",
                  "service",
                  "cookie",
                  ]
        widgets = {'cookie': forms.HiddenInput(attrs={'class': 'form-control'}
                                               ), 'service': forms.HiddenInput(attrs={'class': 'form-control'}),

                   "Message": forms.Textarea(attrs={'class': 'form-control'}),
                   'country': Select2Widget(attrs={'class': 'form-control'}),

                   }

    def __init__(self, *args, **kwargs):

        super(ServiceRequestsForm, self).__init__(*args, **kwargs)

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
        self.base_fields['cookie'].widget = forms.HiddenInput()
        self.base_fields['service'].widget = forms.HiddenInput()
        self.fields['name'].required = True
        self.fields['Phone_Number'].required = True
        self.fields['emile'].required = False
        self.fields['Message'].required = True
        self.fields['service'].disabled = True
        self.fields['cookie'].disabled = True
        # if user.pk == 1:
        # self.fields['profile'] = forms.CharField(max_length=200)
        if Country.objects.filter(phone=967).exists():
            try:
                self.fields['country'].initial = Country.objects.filter(
                    phone=967).first().id
            except Country.DoesNotExist:
                print("Country NotExist")

        # self.fields['Message'].required = True
