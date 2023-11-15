from django import forms
from django.db.models.fields import IntegerField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, NumberInput

from servicesapp.models import *
from .models import *
import datetime


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': " "})


# class ContactForm(forms.ModelForm):

#     class Meta:
#         model = Contact
#         fields = ["name",
#                   "Phone_Number",
#                   #   "subject",
#                   "Message",
#                   ]

#     def __init__(self, *args, **kwargs):

#         super(ContactForm, self).__init__(*args, **kwargs)

#         field_names = [field_name for field_name, _ in self.fields.items()]
#         for field_name in field_names:
#             field = self.fields.get(field_name)
#             field.widget.attrs.update({'placeholder': field.label})

#         self.fields['name'].required = True
#         self.fields['Phone_Number'].required = True
#         # self.fields['subject'].required = True
#         self.fields['Message'].required = True

