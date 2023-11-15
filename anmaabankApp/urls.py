"""MyGuideAtMyPhone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.urls import reverse, re_path
# from django.contrib import sitemaps
from . import models
# from django.contrib.sitemaps.views import sitemap
# from django_sitemaps import robots_txt
from .sitemap import *
# router.register('parents', ParentViewSet)
from django.contrib.sitemaps.views import sitemap
from jopapp.viewsaccount import RequestToOpenAccountView
from django.conf.urls.i18n import i18n_patterns
from servicesapp.views import service_single, application_single
from branches.views import service_points
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from blogapp.views import BlogsListView, download_file, BlogSingleListView, EventListView, NewsListView, PoliciesSingleListView, AntiMoneyLaunderingSingleListView, PrivacyPoliciesSingleListView
from django.views.generic.base import TemplateView

# class BlogSitemap(sitemaps.Sitemap):
#     changefreq = "never"
#     priority = 0.5

#     def items(self):
#         return ImagesPortfolioNoDetils.objects.all().order_by('-Date_Added')

#     def lastmod(self, obj):
#         return obj.pub_date
from django.utils.translation import gettext_lazy as _
from sectionpage.views import section_single
# class StaticViewSitemap(sitemaps.Sitemap):
#     priority = 0.5
#     changefreq = "daily"

#     def items(self):
#         return ["main", "about", "license"]

#     def location(self, item):
#         return reverse(item)

sitemaps = {
    #     'static': StaticViewSitemap,
    'service': ServiceSitemap,
    # 'last-news': ServiceSitemap
    'last-news-detiel': BlogsSitemap,
    "application-single": BankApplicationsSitemap,
    "section-singl": SectionPageSitemap,
    "job-singles": JobsSitemap,
    "static": StaticPageViewSitemap,
    "Policies": PoliciesSitemap,


}

urlpatterns = []
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# sitemap = {
#     "static": StaticViewSitemap,
# }
urlpatterns = [
    # path('', include(views.index)),
    path(r'', views.index, name='index'),
    #    path(r'^$', views.index,),
    #     17,19:                 '',
    path('#contact', views.index_section, name='contact'),
    path('#last-news-home', views.index_section, name='last-news-home'),

    path('manifest.json', views.manifest, name='manifest.json'),

    path('#testimonials', views.index_section, name='testimonials'),
    path('#currencies', views.index_section, name='currencies'),
    path('#apps', views.index_section, name='apps'),
    path('#services-home', views.index_section, name='services-home'),

    #  "",
    #  "",
    path('index/<str:tag>', views.index_section, name='index-section'),
    path('ar', views.index, name='index-ar'),
    path('ar/', views.index, name='index-ar-ar'),

    path('/about', views.about, name='about'),
    path('about', views.about, name='about-page'),

    path('index/', views.indexed, name='indexeds'),
    path(u"tag{0}".format(u"23"), views.indexed, name='portfolio'),
    path(u"{0}".format(u"about"), views.about, name='abouts'),
    path('hero/', views.indexed, name='hero'),
    path(u"?#{0}".format("license"), views.indexed, name='license'),
    path(u"?#:-<{0}>)?$".format("service"), views.indexed, name='service'),
    path('service/', service_single, name='service-single'),
    #     path('application/', application_single, name='application-single'),
    path('application/<int:id>', application_single, name='application-single'),
    path('application/<int:id>/', application_single, name='application-singles'),
    path('application/<int:id>/', application_single, name='application-singles'),
    path('section/<int:id>', section_single, name='section-singles'),
    path('section/<int:id>/', section_single, name='section-singl'),
    path('open-account(?:page=<int:page>[0-9])',
         RequestToOpenAccountView, name='open-account'),
    path('open-account/(?:page=<int:page>[0-9])/',
         RequestToOpenAccountView, name='open-account'),
    path('open-account(?:page=<int:page>[0-9])/',
         RequestToOpenAccountView, name='open-account'),

    path('open-account(?:page=<int:page>[0-9])',
         RequestToOpenAccountView, name='open-accountssssss'),
    path('open-account', RequestToOpenAccountView, name='open-account'),

    path('open-account/', RequestToOpenAccountView, name='open-accounts'),

    # {0}".format(hash_part)
    path('service/<int:id>', service_single, name='service-single'),

    path('service_points/', service_points, name='services-points'),
    path('service_points/<int:id>', service_points, name='services-point'),

    path('service/<int:id>/', service_single, name='service-singles'),
    #     path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}),

    path(
        "sitemap1.xml",
        sitemap,
        {"sitemaps": {"news": GenericSitemap(
            info_dict_blog_sitemap, priority=0.6)}},
        #    {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    path(
        "sitemap.xml",
        sitemap,
        #    {"sitemaps": {"news": GenericSitemap(
        #        info_dict_blog_sitemap, priority=0.6)}},
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('news/<int:id>/',
         BlogSingleListView, name='last-news-detiel'),

    path('privacy-policy/',
         PrivacyPoliciesSingleListView, name='privacy-policy'),
    path('anti-money-laundering/',
         AntiMoneyLaunderingSingleListView, name='anti-money-laundering'),
    path('Policies/<int:id>/',
         PoliciesSingleListView, name='Policies'),

    path(r"^news/(?:page<int:page>[0-9]+)/?$", NewsListView.as_view()),
    # path('post', views.post, name='post'),(?:page-(?P<
    path('news?page<int:page>?id<int:id>?$',
         BlogsListView.as_view(), name='last-newss'),
    #     path('news/<int:id>/',
    #     , name='last-news-detiel'),

    path('newss/',
         NewsListView.as_view(), name='last-news'),
    path('news/',
         NewsListView.as_view(), name='last-newsss'),
    path('events/',
         EventListView.as_view(), name='events'),
    path('blogs/',
         BlogsListView.as_view(), name='blogs'),
    path('news/(?:page-<int:page>)?$/',
         NewsListView.as_view()),
    path('news/(?:page-<int:page>)?$',
         NewsListView.as_view()),

    path('events?page<int:page>?id<int:id>?$',
         EventListView.as_view(), name='eventsss'),
    path('events/(?:page-<int:page>)?$/',
         EventListView.as_view()),
    path('events/(?:page-<int:page>)?$',
         EventListView.as_view()),

    path('blogs?page<int:page>?id<int:id>?$',
         BlogsListView.as_view(), name='blogsss'),
    path('blogs/(?:page-<int:page>)?$/',
         BlogsListView.as_view()),
    path('blogs/(?:page-<int:page>)?$',
         BlogsListView.as_view()),

    path('portfolio-details/<int:id>',
         views.portfolio_details, name='portfolio-details'),
    path('portfolio-details/<int:id>/',
         views.portfolio_details, name='portfolio-detail'),
    path('download_file/<int:id>/',
         # path('download_file//(?P<slug>[\w\-]+)/$',
         download_file, name='download-file'),
    path('download_file/<int:id>',
         # path('download_file//(?P<slug>[\w\-]+)/$',
         download_file, name='download-files'),
    path('sitemap', sitemap, {'sitemaps': sitemaps}),
    path('sitemap/', sitemap, {'sitemaps': sitemaps}),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
    #     path('sitemap/', views.sitemap, name='sitemap'),
    path('google350bc5959c844c8d.html', views.checkGoooglr, name='check-google'),
    # path(
    #     "sitemap.xml",
    #     BlogSitemap,
    #     {"sitemaps": sitemaps},
    #     name="django.contrib.sitemaps.views.sitemap",
    # ),

    # url(r'^sitemap\.xml$', sitemap),
    #     path(r'^robots\.txt$', robots_txt(timeout=86400)),
    # path('', include(router.urls)),
    # path('v1/cart-items/', views.ShoppingCart.as_view()),
    # path('update-item/<int:item_id>', views.ShoppingCartUpdate.as_view()),



    # path("v2/getListArea/<str:latitude>/<str:longitude>",
    #      views.area_list, name="Areas"),

    # path("v2/getListAreagetListArea/",
    #      views.area_list, name="apiArieas"),



]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += i18n_patterns(
#     path(_('about/'), views.indexed, name='about')
#     # path(_('news/'), include(news_patterns, namespace='news')),
# )
