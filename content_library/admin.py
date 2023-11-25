from django.contrib import admin
from .models import *
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request,obj,form,change)
    list_display = ('title','source_type','url','filename')
    list_filter =  ('title','source_type')
    search_fields =  ('title','source_type')

    
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title','report_type','thumbnail_name','filename')
    list_filter =  ('title','report_type')
    search_fields =  ('title','report_type')


admin.site.register(Video,VideoAdmin)
admin.site.register(Report,ReportAdmin)