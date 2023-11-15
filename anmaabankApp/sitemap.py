# from app.pages.sitemaps import PagesSitemap
from .models import *
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blogapp.models import *
from servicesapp.models import *
from sectionpage.views import SectionPageAllQuerySet
from jopapp.models import Jobs


class StaticPageViewSitemap(Sitemap):
    changefreq = "always"
    priority = 1

    def items(self):
        item = ['index',
                'contact',
                # '/#portfolio',
                "last-news-home",
                "testimonials",
                "currencies",
                "apps",
                "services-home",
                'about-page',
                "privacy-policy",
                "anti-money-laundering",
                "home-jop",
                "login-user",
                "createaccoute-user",
                "robots.txt"]
        return item

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["main", "about", "license"]

    def location(self, item):
        return reverse(item)


class PoliciesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.1
    # url = p.get_absolute_url()

    def items(self):
        return Policies.objects.filter()

    def lastmod(self, obj):
        return obj.Date_Update


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    # url = p.get_absolute_url()

    def items(self):
        return Services.objects.filter()

    def lastmod(self, obj):
        return obj.Date_Update
# def sitemap(request):

# class ServiceSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.5
#     # url = p.get_absolute_url()

#     def items(self):
#         return ImagesPortfolioNoDetils.objects.filter()

#     def lastmod(self, obj):
#         return obj.Date_Update


info_dict_blog_sitemap = {
    "queryset": Blogs.objects.filter(),
    "date_field": "Date_Update",
}


class JobsSitemap(Sitemap):
    # changefreq = "monthly"
    # priority = 0.5
    # url = p.get_absolute_url()
    changefreq = "always"
    priority = 1

    def items(self):
        return Jobs.objects.all()

    def lastmod(self, obj):
        return obj.edite_at


class SectionPageSitemap(Sitemap):
    # changefreq = "monthly"
    # priority = 0.5
    # url = p.get_absolute_url()
    changefreq = "always"
    priority = 1

    def items(self):
        return SectionPageAllQuerySet()

    def lastmod(self, obj):
        return obj.Date_Update


class BlogsSitemap(Sitemap):
    # changefreq = "monthly"
    # priority = 0.5
    # url = p.get_absolute_url()
    changefreq = "always"
    priority = 1

    def items(self):
        return Blogs.objects.filter()

    def lastmod(self, obj):
        return obj.Date_Update


class BankApplicationsSitemap(Sitemap):
    # changefreq = "monthly"
    # priority = 0.5
    # url = p.get_absolute_url()
    changefreq = "always"
    priority = 1
#  ).order_by('Date_Added')

    def items(self):
        return BankApplications.objects.filter(is_deleted=False,)

    def lastmod(self, obj):
        return obj.Date_Update
# def sitemap(request):
    # sitemap = Sitemap(

# def sitemap(request):
    # sitemap = Sitemap(
    #     # All URLs are passed through build_absolute_uri.
    #     build_absolute_uri=request.build_absolute_uri,
    # )

    # # URLs can be added one-by-one. The only required argument
    # # is the URL. All other arguments are keyword-only arguments.
    # for p in ImagesPortfolioNoDetils.objects.all():
    #     url = p.get_absolute_url()
    #     sitemap.add(
    #         url,
    #         changefreq='weekly',
    #         priority=0.5,
    #         lastmod=p.Date_Update,
    #         alternates={
    #             code: urljoin(domain, url)
    #             for code, domain in PAGE_DOMAINS[p.language].items()
    #         },
    #     )

    # # Adding conventional Django sitemaps is supported. The
    # # request argument is necessary because Django's sitemaps
    # # depend on django.contrib.sites, resp. RequestSite.
    # sitemap.add_django_sitemap(PagesSitemap, request=request)

    # # You can also specify the site and protocol manually should you wish
    # # to do so:
    # sitemap.add_django_sitemap(
    #     PagesSitemap, site=...site..., protocol=request.scheme
    # )
    # # Note! If you're omitting the request you *have* to specify site and
    # # protocol yourself.

    # # You could get the serialized XML...
    # # ... = sitemap.serialize([pretty_print=False])
    # # ... or use the ``response`` helper to return a
    # # ready-made ``HttpResponse``:
    # return sitemap.response(
    #     # pretty_print is False by default
    #     pretty_print=settings.DEBUG,
    # )
