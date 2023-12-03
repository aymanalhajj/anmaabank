from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Awards'
    verbose_name = _("الجوائــــــز ")
