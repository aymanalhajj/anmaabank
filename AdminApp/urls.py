from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView  # import TemplateView

urlpatterns = [
    path('', admin.site.urls),
    # path('admin/doc/', include('django.contrib.admindocs.urls'))
    # path('', include('SafarByCallMeApp.urls')),
    # path("robots.txt", TemplateView.as_view(template_name="robots.txt",
    # content_type="text/plain")),  # add the robots.txt file
    # path('account/', include('allauth.urls')),
    # path('tinymce/', include('tinymce.urls')),
    # path('tinymce/', include('tinymce.urls')),  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
