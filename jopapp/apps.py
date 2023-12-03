from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class JopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jopapp'
    verbose_name = _("الــوظــائف والــطــلــبــات")
