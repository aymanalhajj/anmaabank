from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class AdsenseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adsense'
    verbose_name = _("الاعلانات المتحركة")
