# -*- coding: utf-8 -*-

from django.urls import re_path, include, path
from django.views.generic import TemplateView

urlpatterns = [
    path(r'^currencies/', include('currencies.urls')),
    path(r'^$', TemplateView.as_view(template_name='index.html')),
    path(r'^context_processor$', TemplateView.as_view(
        template_name='context_processor.html')),
    path(r'^context_tag$', TemplateView.as_view(
        template_name='context_tag.html')),
]
