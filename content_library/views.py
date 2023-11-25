from django.shortcuts import render
from .models import Report,Video

from settingapp.views import SettingModelQuerySet
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
# Create your views here.

def getUrl(request):
    if request is None:
        raise Exception("request is None")
    # print("url_name")
    # print(request.build_absolute_uri())
    return request.build_absolute_uri()

def VideoListView(request):
    videos = Video.objects.all
    context ={
        'videos' : videos,
        'title' : 'مكتبة الفيديوهات'
    }
    
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    return render(request, 'video-list.html',context)

def ReportListView(request, type):
    reports = Report.objects.filter(report_type = type)
    context ={
        'reports' : reports,
        'type' : type,
        'title' : 'التقارير'
    }
    
    context['setting'] = SettingModelQuerySet()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    return render(request, 'report-list.html',context)