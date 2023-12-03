from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnmaabankAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anmaabankApp'
    verbose_name =_( "الــــرئــيــســيــة ")
