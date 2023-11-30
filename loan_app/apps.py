from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class LoanAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loan_app'
    verbose_name = _("اعداد طلبات التمويل")
