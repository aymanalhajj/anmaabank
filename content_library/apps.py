from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content_library'
    verbose_name = 'التقارير والفيديوهات'