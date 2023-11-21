from django import forms
from django.forms import ModelForm
from .models import LoanApplication

from django_select2.forms import Select2Widget


class LoanApplicationForm(ModelForm):
    class Meta:
        model  = LoanApplication
        fields = "__all__"
        widgets = {
        'user'                  : forms.HiddenInput(),
        'client_name'           : forms.TextInput(attrs={'class':'form-control'}),
        # 'mobile_number'         : forms.TextInput(attrs={'class':'form-control'}),
        # 'city_name'             : forms.TextInput(attrs={'class':'form-control'}),
        # 'street_name'           : forms.TextInput(attrs={'class':'form-control'}),
        # 'nearest_known_place'   : forms.TextInput(attrs={'class':'form-control'}),
        # 'project_created_at'    : forms.TextInput(attrs={'class':'form-control'}),
        # 'current_capital'       : forms.TextInput(attrs={'class':'form-control'}),
        # 'loan_purpose'          : forms.TextInput(attrs={'class':'form-control'}),
        # 'required_amount'       : forms.TextInput(attrs={'class':'form-control'}),
        # 'loan_months'           : forms.TextInput(attrs={'class':'form-control'}),
        # 'monthly_installment'   : forms.TextInput(attrs={'class':'form-control'}),
        'activity_type'         : Select2Widget(attrs={'class':'form-control'}),
        'guarantee_type'        : Select2Widget(attrs={'class':'form-control'})
        }
        labels = {
        'client_name'           :'اسم العميل',
        'mobile_number'         :'رقم الجوال',
        'city_name'             :'المدينة',
        'street_name'           :'الحي/الشارع',
        'nearest_known_place'   :'أقرب معلم بارز',
        'project_created_at'    :'عمر المشروع(تاريخ التأسيس)',
        'current_capital'       :'رأس مال المشروع حالياً',
        'loan_purpose'          :'غرض التمويل',
        'required_amount'       :'مبلغ التمويل المطلوب',
        'loan_months'           :'مدة التمويل بالأشهر',
        'monthly_installment'   :'القسط الشهري',
        'activity_type'         :'نوع النشاط',
        'guarantee_type'        :'نوع الضمانة'
        }
        error_messages = {
        'client_name'           :{'required': 'يجب ادخال اسم العميل'},
        'mobile_number'         :{'required': 'يجب ادخال رقم الجوال'},
        'city_name'             :{'required': 'يجب ادخال المدينة'},
        'street_name'           :{'required': 'يجب ادخال الحي/الشارع'},
        'nearest_known_place'   :{'required': 'يجب ادخال أقرب معلم بارز'},
        'project_created_at'    :{'required': 'يجب ادخال عمر المشروع(تاريخ التأسيس)'},
        'current_capital'       :{'required': 'يجب ادخال رأس مال المشروع حالياً'},
        'loan_purpose'          :{'required': 'يجب ادخال غرض التمويل'},
        'required_amount'       :{'required': 'يجب ادخال مبلغ التمويل المطلوب'},
        'loan_months'           :{'required': 'يجب ادخال مدة التمويل بالأشهر'},
        'monthly_installment'   :{'required': 'يجب ادخال القسط الشهري'},
        'activity_type'         :{'required': 'يجب ادخال نوع النشاط'},
        'guarantee_type'        :{'required': 'يجب ادخال نوع الضمانة'}
        }
        help_texts = {
            
        # 'client_name'           :'اسم العميل',
        # 'mobile_number'         :'رقم الجوال',
        # 'city_name'             :'المدينة',
        # 'street_name'           :'الحي/الشارع',
        # 'nearest_known_place'   :'أقرب معلم بارز',
        # 'project_created_at'    :'عمر المشروع(تاريخ التأسيس)',
        # 'current_capital'       :'رأس مال المشروع حالياً',
        # 'loan_purpose'          :'غرض التمويل',
        # 'required_amount'       :'مبلغ التمويل المطلوب',
        # 'loan_months'           :'مدة التمويل بالأشهر',
        # 'monthly_installment'   :'القسط الشهري',
        # 'activity_type'         :'نوع النشاط',
        # 'guarantee_type'        :'نوع الضمانة'
        }
    def __init__(self, *args, **kwargs):
    #def __init__(self):
        super(LoanApplicationForm, self).__init__(*args, **kwargs)
        self.fields['project_created_at'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder':field.label})