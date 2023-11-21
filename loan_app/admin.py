from django.contrib import admin

from .models import *
# Register your models here.

class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name','description')
    search_fields = ('name','description')


class GuaranteeTypeAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name','description')
    search_fields = ('name','description')

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = (
    'client_name', 'mobile_number' , 'city_name' ,
    'street_name','nearest_known_place' ,'project_created_at' ,
    'current_capital','loan_purpose' ,
    'required_amount',
    'loan_months',    'monthly_installment',    'activity_type' ,
    'guarantee_type')
    list_filter =  ('client_name', 'mobile_number' , 'city_name' ,
    'street_name','nearest_known_place' ,'project_created_at' ,
    'current_capital','loan_purpose' ,
    'required_amount',
    'loan_months',    'monthly_installment',    'activity_type' ,
    'guarantee_type')
    search_fields = ( 'client_name', 'mobile_number' , 'city_name' ,
    'street_name','nearest_known_place' ,'project_created_at' ,
    'current_capital','loan_purpose' ,
    'required_amount',
    'loan_months',    'monthly_installment',    'activity_type' ,
    'guarantee_type')

admin.site.register(ActivityType,ActivityTypeAdmin)
admin.site.register(GuaranteeType,GuaranteeTypeAdmin)
admin.site.register(LoanApplication,LoanApplicationAdmin)