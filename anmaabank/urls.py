"""anmabank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render, redirect
from django.conf.urls import (handler400, handler403, handler404, handler500)
from anmaabankApp import viewaccount
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import
from django.conf.urls.static import static
from django.conf import settings
from jopapp.viewsaccount import register, ProfileRegistration, userSignin, userLogout
from django.views.generic.base import TemplateView  # import TemplateView
urlpatterns = []

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,

                      document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler400 = 'anmaabankApp.views.page_not_found'
handler403 = 'anmaabankApp.views.page_not_found'
handler404 = 'anmaabankApp.views.page_not_found'
handler500 = 'anmaabankApp.views.page_not_found'


urlpatterns += [
    # path('admin-web/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),  # Here's the typo
    # path(settings.STATIC_URL, include('jopapp.urls'), name="job-app"),
    path('', include('anmaabankApp.urls')),
    path("jobs/", include('jopapp.urls'), name="job-app"),
    path("select2/", include("django_select2.urls")),
    path(r'^media/(?P<path>.*)$', serve,
         {'document_root': settings.MEDIA_ROOT}),
    path(r'^static/(?P<path>.*)$', serve,
         {'document_root': settings.STATIC_ROOT}),
    path("login/", userSignin, name='login-user'),
    path("userLogout/login/", userSignin, name='userLogout-user'),
    path("userLogout/", userLogout, name='userLogout'),
    path("createaccoute/", ProfileRegistration.as_view(),
         name='createaccoute-user'),
    path("createaccoute/", ProfileRegistration.as_view(), name='createaccounte'),

    path("robots.txt", TemplateView.as_view(template_name="robots.txt",
                                            content_type="text/plain")),  # add the robots.txt file
    # path('account/', include('allauth.urls')),
    path('admin-web/', include('AdminApp.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # path('tinymce/', include('tinymce.urls')),
    path('tinymce/', include('tinymce.urls')),  # new
    path('selectable/', include('selectable.urls')),
    path("select2/", include("django_select2.urls")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt",
                                            content_type="text/plain")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt",
                                            content_type="text/plain"), name="robots.txt"),
    path("eth/login/", viewaccount.LoginView.as_view(), name="login-eth"),
    path("eth/logout/", viewaccount.LogoutView.as_view(), name="logout-eth"),
    path(
        "password_change/", viewaccount.PasswordChangeView.as_view(), name="password_change-eth"
    ),
    path(
        "eth/password_change/done/",
        viewaccount.PasswordChangeDoneView.as_view(),
        name="password_change_done-eth",
    ),
    path("eth/password_reset/", viewaccount.PasswordResetView.as_view(),
         name="password_reset-eth"),
    path(
        "eth/password_reset/done/",
        viewaccount.PasswordResetDoneView.as_view(),
        name="password_reset_done-eth",
    ),
    path(
        "eth/reset/<uidb64>/<token>/",
        viewaccount.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm-eth",
    ),
    path(
        "eth/reset/done/",
        viewaccount.PasswordResetCompleteView.as_view(),
        name="password_reset_complete-eth",
    ),
]


def handler404(request, *args, **argv):
    return redirect('home')
