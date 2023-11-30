from django.shortcuts import render
from .models import Report,Video

from settingapp.views import SettingModelQuerySet
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from settingapp.views import static_content

def getUrl(request):
    if request is None:
        raise Exception("request is None")
    # print("url_name")
    # print(request.build_absolute_uri())
    return request.build_absolute_uri()

def VideoListView(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    videos = Video.objects.all
    context ={
        'videos' : videos,
        'title' : 'مكتبة الفيديوهات'
    }
    
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context["static_content"] = static_content[lang]
    return render(request, 'video-list.html',context)

def ReportListView(request, type, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'
    reports = Report.objects.filter(report_type = type)
    context ={
        'reports' : reports,
        'type' : type,
        'title' : 'التقارير'
    }
    
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context["static_content"] = static_content[lang]
    return render(request, 'report-list.html',context)