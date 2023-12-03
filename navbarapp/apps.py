from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NavbarappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "navbarapp"
    verbose_name =  "شريط التنقل"
