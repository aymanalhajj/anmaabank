from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfolioappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolioapp"
    verbose_name = _(" معرض الصور  ")
