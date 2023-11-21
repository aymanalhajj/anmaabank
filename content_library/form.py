from django import forms
from django.forms import ModelForm


class VideoForm(ModelForm):
    class Meta:
        fields = [
            'title' 		,
            'source_type' 	,
            'url' 			,
            'filename' 
        ]
        labels = {
            'title' 		:'عنوان الفيديو',
            'source_type' 	:'مصدر الفيديو',
            'url' 			:'رابط الفيديو',
            'filename'      :'ملف الفيديو'
        }
        help_texts = {
            'title' 		:'عنوان الفيديو',
            'source_type' 	:'مصدر الفيديو',
            'url' 			:'رابط الفيديو',
            'filename'      :'ملف الفيديو'
        }
        widgets = {
            'title' 		:forms.TextInput(attrs={'class':'form-control'}),
            'source_type' 	:forms.TextInput(attrs={'class':'form-control'}),
            'url' 			:forms.TextInput(attrs={'class':'form-control'}),
            'filename'      :forms.TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'title' 		:{'required': 'يجب ادخال عنوان الفيديو'},
            'source_type' 	:{'required': 'يجب ادخال مصدر الفيديو'},
            'url' 			:{'required': 'يجب ادخال رابط الفيديو'},
            'filename'      :{'required': 'يجب ادخال ملف الفيديو'}

        }


class ReportForm(ModelForm):
    class Meta:
        fields = [
            'title' 		,
            'report_type' 	,
            'thumbnail_name',
            'filename' 
        ]
        labels = {
            'title' 		 :'اسم التقرير',
            'report_type' 	 :'نوع التقرير',
            'thumbnail_name' :'صورة التقرير',
            'filename'       :'ملف التقرير'
        }
        help_texts = {
            'title' 		 :'اسم التقرير',
            'report_type' 	 :'نوع التقرير',
            'thumbnail_name' :'صورة التقرير',
            'filename'       :'ملف التقرير'
        }
        widgets = {
            'title' 		    :forms.TextInput(attrs={'class':'form-control'}),
            'report_type' 	    :forms.TextInput(attrs={'class':'form-control'}),
            'thumbnail_name'	:forms.TextInput(attrs={'class':'form-control'}),
            'filename'          :forms.TextInput(attrs={'class':'form-control'})
        }
        error_messages = {
            'title' 		    :{'required': 'يجب ادخال اسم التقرير'},
            'report_type' 	    :{'required': 'يجب ادخال نوع التقرير'},
            'thumbnail_name'	:{'required': 'يجب ادخال صورة التقرير'},
            'filename'          :{'required': 'يجب ادخال ملف التقرير'}
        }
