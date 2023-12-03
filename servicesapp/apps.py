from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServicesappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "servicesapp"
    verbose_name = _("الخدمات  وتطبيقات البنك")
