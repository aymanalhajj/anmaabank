from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SettingappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "settingapp"
    verbose_name = _("اعدادات الموقع")
