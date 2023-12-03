from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TestimonialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Testimonials'
    verbose_name = _("آراء العملاء")
