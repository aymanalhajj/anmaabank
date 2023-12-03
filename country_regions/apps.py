from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

APP_NAME = 'country_regions'

class CountryRegionsConfig(AppConfig):
    name = APP_NAME
    verbose_name = _("الدول / المناطق")
