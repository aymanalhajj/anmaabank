from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from django.views import generic
from django.http import HttpResponse, request
from django.contrib import messages
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from settingapp.views import SettingModelQuerySet
# from blogapp.views import BlogsHomeListView
# from OurMarch.views import OurMarchQuerySet
# from anmaabankApp.forms import OurNewsletterForm
from OurNewsletter.forms import *
from OurNewsletter.views import *
from settingapp.views import static_content


def getUrl(request):
    if request is None:
        raise Exception("request is None")

    return request.build_absolute_uri()
# Create your views here.


def BlogsHomeListView():
    # model = Blogs
    return Blogs.objects.filter(
        # title__icontains='war'
    )[:10]  # Get 5 books containing the title war
    # def get_queryset(self):


def download_file(request, id):
    # Import mimetypes module

    import mimetypes
# import os module
    import os
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    # filename = '339623708_1166228024076966_4757709512309706332_n_1.jpg'
    # Define the full file path
    # filepath = BASE_DIR + '/' + filename
    # Open the file for reading content mediaimageBlogs 20230408339623708_1166228024076966_4757709512309706332_n_1jpg
    query = Blogs.objects.get(id=id)
    filepath = BASE_DIR + '/' + query.image.url
    filename = query.image.name

    # filename = os.path.splitext(query.image.url)
    # print(os.path.splitext(query.image.url))

    path = open(filepath, 'rb')
    # if request.method == 'GET':
    #     from anmaabankApp.views import saveInfoIp

    #     # saveInfoReqestHeder(request, filepath)
    #     saveInfoIp(request, filepath)
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


class BlogsListView(generic.ListView):
    # model = Blogs
    # your own name for the list as a template variable
    context_object_name = 'blogs'
    template_name = 'blog.html'
    allow_empty = True
    paginator = Paginator  # 6 employees per page
    paginate_by = 10
    ordering = ['-date_post']
    # queryset = Blogs.objects.all()
    # make_object_list = True
    # allow_future = True

    # queryset = None
    # model = ['prodactHome', 'category', 'citys', 'countrys', 'category']
    # paginate_by = 'page'
    # paginate_by = 1  # and that's it !!

    # paginate_orphans = 10
    # context_object_name = None

    # page_kwarg = 'page'
    # ordering = '-date_post'
    # context_object_name = 'index'
    # schema = None

    def get_context_data(self, **kwargs):
        from django.db.models import Count, Case, When

        # Call the base implementation first to get the context
        context = super(BlogsListView,
                        self).get_context_data(**kwargs)
        # if self.request.method == 'GET':
        #     from anmaabankApp.views import saveInfoIp

        #     # saveInfoReqestHeder(request, 'index.html')
        #     saveInfoIp(self.request, 'blog.html?page=' +
        #                str(self.request.GET.get('page', 1)))
        # Create any data and add it to the context
        # category_blog = int(self.request.GET.get('category_blog', 0))
        # print("category_blog")
        # print(category_blog)
        # if category_blog != 0:
        # context['daily_flight_list'] = Blogs.objects.filter(
        # category_blog=category_blog)
        # context['CategoryBlog'] =
        # context['CategoryBlog'] =
        context["titel"] = "المدونة"
        context["title"] = "المدونة"
        context["url"] = getUrl(request=self.request)

        context["navbar"] = NavbarsQuerySet()
        context["ColumnNavbars"] = ColumnNavbarsQuerySet()
        context['setting'] = SettingModelQuerySet()
        # context['FormOurNewsletter'] = OurNewsletterForm()

        context['CategoryBlog'] = CategoryBlog.objects.all(
            # title__icontains='war'
        ).annotate(Blogs_count=Count('category_blog'))
        context["titel"] = "المدونة"

        # .annotate(
    # total_completed=Count(
        # Case(
        # When(
        # status='completed', then=1), output_field=DecimalField()
        # )
    # ),
    # total_failed=Count(
        # Case(
        # When(status='failed', then=1), output_field=DecimalField()
        # )
    # )
# )
        # if self.request.method == 'POST':
        # return SaveContact(request,"blog.html",context)
        context['page'] = int(self.request.GET.get('page', 1))
        
        lang = self.kwargs['lang']
        context["static_content"] = static_content[lang]
        context['some_data'] = 'This is just some data'

        if self.request.method == 'POST':
            SaveContact(self.request, "blog.html", context)
            return render(self.request, 'blog.html', context)
        return context

    def get_queryset(self):
        qs = Blogs.objects.all().filter(category="المدونة")
        category_blog = int(self.request.GET.get('category_blog', 0))

        date_post__gte = self.request.GET.get(
            'date_post__gte', 0)
        date_post__lt = self.request.GET.get(
            'date_post__lt', 0)

        print("category_blog")
        print(category_blog)
        if category_blog != 0:
            print("category_blog 2")
            print(category_blog)
            if date_post__lt != 0:
                if date_post__gte != 0:
                    qs = qs.filter(
                        date_post__gte=date_post__gte,
                        date_post__lt=date_post__lt, category=category_blog
                    )
                    return qs
                qs = qs.filter(
                    date_post__lt=date_post__lt, category=category_blog)
                return qs
            # if self.request.GET.get("category_blog"):
            qs = qs.filter(category=category_blog)
            return qs
        elif date_post__lt != 0:
            if date_post__gte != 0:
                qs = qs.filter(
                    date_post__gte=date_post__gte,
                    date_post__lt=date_post__lt,
                )
                return qs
            qs = qs.filter(
                date_post__lt=date_post__lt)
            return qs
        return qs
    # Specify your own template name/location


class NewsListView(generic.ListView):
    # model = Blogs
    # your own name for the list as a template variable
    context_object_name = 'blogs'
    # queryset = Blogs.objects.all()
    template_name = 'blog.html'
    allow_empty = True
    # make_object_list = True
    # allow_future = True
    paginator = Paginator  # 6 employees per page

    # queryset = None
    # model = ['prodactHome', 'category', 'citys', 'countrys', 'category']
    # paginate_by = 'page'
    # paginate_by = 1  # and that's it !!
    paginate_by = 10

    # paginate_orphans = 10
    # context_object_name = None

    # page_kwarg = 'page'
    # ordering = '-date_post'
    # context_object_name = 'index'
    # schema = None
    ordering = ['-date_post']

    def get_context_data(self, **kwargs):
        from django.db.models import Count, Case, When

        # Call the base implementation first to get the context
        context = super(NewsListView,
                        self).get_context_data(**kwargs)
        # if self.request.method == 'GET':
        #     from anmaabankApp.views import saveInfoIp

        #     # saveInfoReqestHeder(request, 'index.html')
        #     saveInfoIp(self.request, 'blog.html?page=' +
        #                str(self.request.GET.get('page', 1)))
        # Create any data and add it to the context
        # category_blog = int(self.request.GET.get('category_blog', 0))
        # print("category_blog")
        # print(category_blog)
        # if category_blog != 0:
        # context['daily_flight_list'] = Blogs.objects.filter(
        # category_blog=category_blog)
        # context['CategoryBlog'] =
        # context['CategoryBlog'] =
        context["titel"] = "اخبار البنك"
        context["title"] = "اخبار البنك"
        context["url"] = getUrl(request=self.request)

        context["navbar"] = NavbarsQuerySet()
        context["ColumnNavbars"] = ColumnNavbarsQuerySet()
        context['setting'] = SettingModelQuerySet()
        # context['FormOurNewsletter'] = OurNewsletterForm()
        # if self.request.method == 'POST':
        # return SaveContact(self.request, "blog.html", context)
        context['CategoryBlog'] = CategoryBlog.objects.all(
            # title__icontains='war'
        ).annotate(Blogs_count=Count('category_blog'))
        # .annotate(
    # total_completed=Count(
        # Case(
        # When(
        # status='completed', then=1), output_field=DecimalField()
        # )
    # ),
    # total_failed=Count(
        # Case(
        # When(status='failed', then=1), output_field=DecimalField()
        # )
    # )
# )
        
        context['page'] = int(self.request.GET.get('page', 1))
        lang = self.kwargs['lang']
        context["static_content"] = static_content[lang]
        context['page'] = int(self.request.GET.get('page', 1))
        if self.request.method == 'POST':
            SaveContact(self.request, "blog.html", context)
            return render(self.request, 'blog.html', context)
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        qs = Blogs.objects.all().filter(category="اخبار البنك")
        category_blog = int(self.request.GET.get('category_blog', 0))

        date_post__gte = self.request.GET.get(
            'date_post__gte', 0)
        date_post__lt = self.request.GET.get(
            'date_post__lt', 0)

        print("category_blog")
        print(category_blog)
        if category_blog != 0:
            print("category_blog 2")
            print(category_blog)
            if date_post__lt != 0:
                if date_post__gte != 0:
                    qs = qs.filter(
                        date_post__gte=date_post__gte,
                        date_post__lt=date_post__lt, category=category_blog
                    )
                    return qs
                qs = qs.filter(
                    date_post__lt=date_post__lt, category=category_blog)
                return qs
            # if self.request.GET.get("category_blog"):
            qs = qs.filter(category=category_blog)
            return qs
        elif date_post__lt != 0:
            if date_post__gte != 0:
                qs = qs.filter(
                    date_post__gte=date_post__gte,
                    date_post__lt=date_post__lt,
                )
                return qs
            qs = qs.filter(
                date_post__lt=date_post__lt)
            return qs
        return qs
    # Specify your own template name/location


class EventListView(generic.ListView):
    # model = Blogs
    # your own name for the list as a template variable
    context_object_name = 'blogs'
    # queryset = Blogs.objects.all()
    template_name = 'blog.html'
    allow_empty = True
    # make_object_list = True
    # allow_future = True
    paginator = Paginator  # 6 employees per page

    # queryset = None
    # model = ['prodactHome', 'category', 'citys', 'countrys', 'category']
    # paginate_by = 'page'
    # paginate_by = 1  # and that's it !!
    paginate_by = 10

    # paginate_orphans = 10
    # context_object_name = None

    # page_kwarg = 'page'
    # ordering = '-date_post'
    # context_object_name = 'index'
    # schema = None
    ordering = ['-date_post']

    def get_context_data(self, **kwargs):
        from django.db.models import Count, Case, When

        # Call the base implementation first to get the context
        context = super(EventListView,
                        self).get_context_data(**kwargs)
        # if self.request.method == 'GET':
        #     from anmaabankApp.views import saveInfoIp

        #     # saveInfoReqestHeder(request, 'index.html')
        #     saveInfoIp(self.request, 'blog.html?page=' +
        #                str(self.request.GET.get('page', 1)))
        # Create any data and add it to the context
        # category_blog = int(self.request.GET.get('category_blog', 0))
        # print("category_blog")
        # print(category_blog)
        # if category_blog != 0:
        # context['daily_flight_list'] = Blogs.objects.filter(
        # category_blog=category_blog)
        # context['CategoryBlog'] =
        # context['CategoryBlog'] =
        context["navbar"] = NavbarsQuerySet()
        context["ColumnNavbars"] = ColumnNavbarsQuerySet()
        context['setting'] = SettingModelQuerySet()
        # context['FormOurNewsletter'] = OurNewsletterForm()
        # if self.request.method == 'POST':
        # return SaveContact(request,"blog.html",context)
        context['CategoryBlog'] = CategoryBlog.objects.all(
            # title__icontains='war'
        ).annotate(Blogs_count=Count('category_blog'))

        # .annotate(
    # total_completed=Count(
        # Case(
        # When(
        # status='completed', then=1), output_field=DecimalField()
        # )
    # ),
    # total_failed=Count(
        # Case(
        # When(status='failed', then=1), output_field=DecimalField()
        # )
    # )
# )
        context["titel"] = 'الفعاليات'
        context["title"] = 'الفعاليات'
        context["url"] = getUrl(request=self.request)
        context['page'] = int(self.request.GET.get('page', 1))
        # if self.request.method == 'POST':
        #     return SaveContact(request,"blog.html",context)
        lang = self.kwargs['lang']
        context["static_content"] = static_content[lang]
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        qs = Blogs.objects.all().filter(category="الفعاليات")
        category_blog = int(self.request.GET.get('category_blog', 0))

        date_post__gte = self.request.GET.get(
            'date_post__gte', 0)
        date_post__lt = self.request.GET.get(
            'date_post__lt', 0)

        print("category_blog")
        print(category_blog)
        if category_blog != 0:
            print("category_blog 2")
            print(category_blog)
            if date_post__lt != 0:
                if date_post__gte != 0:
                    qs = qs.filter(
                        date_post__gte=date_post__gte,
                        date_post__lt=date_post__lt, category=category_blog
                    )
                    return qs
                qs = qs.filter(
                    date_post__lt=date_post__lt, category=category_blog)
                return qs
            # if self.request.GET.get("category_blog"):
            qs = qs.filter(category=category_blog)
            return qs
        elif date_post__lt != 0:
            if date_post__gte != 0:
                qs = qs.filter(
                    date_post__gte=date_post__gte,
                    date_post__lt=date_post__lt,
                )
                return qs
            qs = qs.filter(
                date_post__lt=date_post__lt)
            return qs
        return qs
    # Specify your own template name/location


# class (generic.ListView):

def BlogSingleListView(request, id, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from django.db.models import Count, Case, When
    context = {

    }
    # if request.method == 'POST':
    #     return SaveContact(request,"blog.html",context)
    # Call the base implementation first to get the context
    # context = super(BlogsListView,
    # self).get_context_data(**kwargs)
    # if request.method == 'GET':
    #     from anmaabankApp.views import saveInfoIp

    #     # saveInfoReqestHeder(request, 'index.html')
    #     saveInfoIp(request, 'blog-single.html?page=' +
    #                str(request.GET.get('page', 1)))
    # Create any data and add it to the context
    # category_blog = int(self.request.GET.get('category_blog', 0))
    # print("category_blog")
    # print(category_blog)
    # if category_blog != 0:
    # context['daily_flight_list'] = Blogs.objects.filter(
    # category_blog=category_blog)
    # context['CategoryBlog'] =
    # context['CategoryBlog'] =
    images_blogs = ImagesBlogs.objects.filter(blog=id)
    qs = None
    if id != None:
        qs = Blogs.objects.filter(id=id)
        context['news'] = qs.first()

    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    # context['FormOurNewsletter'] = OurNewsletterForm()
    context['imagesblogs'] = images_blogs
    # "imagesservice": images_services,

    context['CategoryBlog'] = CategoryBlog.objects.all(
        # title__icontains='war'
    ).annotate(Blogs_count=Count('category_blog'))
    if qs != None:
        context["titel"] = "تفاصيل  المقال  Page not found(404) " if qs.first(
        ) == None else qs.first().titel
    if qs != None:
        context["title"] = "تفاصيل  المقال  Page not found(404) " if qs.first(
        ) == None else qs.first().titel,

    else:
        context["title"] = "تفاصيل المقال" + " Page not found(404) "
        context["titel"] = "تفاصيل المقال" + " Page not found(404) "

    context["url"] = getUrl(request=request)

    " "
    # context["title"] =
    # .annotate(
    # total_completed=Count(
    # Case(
    # When(
    # status='completed', then=1), output_field=DecimalField()
    # )
    # ),
    # total_failed=Count(
    # Case(
    # When(status='failed', then=1), output_field=DecimalField()
    # )
    # )
# )
    # context['page'] = intrequest.GET.get('page', 1))

    context["static_content"] = static_content[lang]
    context['some_data'] = 'This is just some data'
    # return context

    # def get_queryset(self):

    # category_blog = int(request.GET.get('category_blog', 0))

    # date_post__gte = self.request.GET.get(
    # 'date_post__gte', 0)
    # date_post__lt = self.request.GET.get(
    # 'date_post__lt', 0)

    # print("category_blog")
    if request.method == 'POST':
        SaveContact(request, "blog-single.html", context)
        return render(request, 'blog-single.html', context)
    # return context
    return render(request, 'blog-single.html', context)

    # Specify your own template name/location


def PrivacyPoliciesSingleListView(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from django.db.models import Count, Case, When
    context = {

    }
    # if request.method == 'POST':
    #     return SaveContact(request,"blog.html",context)
    # Call the base implementation first to get the context
    # context = super(BlogsListView,
    # self).get_context_data(**kwargs)
    # if request.method == 'GET':
    #     from anmaabankApp.views import saveInfoIp

    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'blog-single.html?page=' +
    #    str(request.GET.get('page', 1)))
    # Create any data and add it to the context
    # category_blog = int(self.request.GET.get('category_blog', 0))
    # print("category_blog")
    # print(category_blog)
    # if category_blog != 0:
    # context['daily_flight_list'] = Blogs.objects.filter(
    # category_blog=category_blog)
    # context['CategoryBlog'] =
    # context['CategoryBlog'] =
    # images_blogs = ImagesBlogs.objects.filter(blog=id)
    # qs = None
    # if id != None:
    qs = Policies.objects.filter(category="سياسة خصوصية")
    context['policie'] = qs.first()

    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    # context['FormOurNewsletter'] = OurNewsletterForm()
    # context['imagesblogs'] = images_blogs
    # "imagesservice": images_services,

    # context['CategoryBlog'] = CategoryBlog.objects.all(
    #     # title__icontains='war'
    # ).annotate(Blogs_count=Count('category_blog'))
    if qs.first() != None:
        context["titel"] = 'سياسة  الخصوصية  Page not found(404) ' if qs.first(
        ) == None else qs.first().titel
    # if qs.first() != None:
        context["title"] = 'سياسة  الخصوصية  Page not found(404) ' if qs.first(
        ) == None else qs.first().titel,

    else:
        context["title"] = 'سياسة  الخصوصية  Page not found(404) '
        context["titel"] = 'سياسة  الخصوصية  Page not found(404) '

    context["url"] = getUrl(request=request)

    " "
    # context["title"] =
    # .annotate(
    # total_completed=Count(
    # Case(
    # When(
    # status='completed', then=1), output_field=DecimalField()
    # )
    # ),
    # total_failed=Count(
    # Case(
    # When(status='failed', then=1), output_field=DecimalField()
    # )
    # )
# )
    # context['page'] = intrequest.GET.get('page', 1))

    context["static_content"] = static_content[lang]
    context['some_data'] = 'This is just some data'
    # return context

    # def get_queryset(self):

    # category_blog = int(request.GET.get('category_blog', 0))

    # date_post__gte = self.request.GET.get(
    # 'date_post__gte', 0)
    # date_post__lt = self.request.GET.get(
    # 'date_post__lt', 0)

    # print("category_blog")
    if request.method == 'POST':
        SaveContact(request, "blog-single.html", context)
        return render(request, 'blog-single.html', context)
    # return context
    return render(request, 'blog-single.html', context)

    # Specify your own template name/location


def AntiMoneyLaunderingSingleListView(request, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from django.db.models import Count, Case, When
    context = {

    }
    # if request.method == 'POST':
    #     return SaveContact(request,"blog.html",context)
    # Call the base implementation first to get the context
    # context = super(BlogsListView,
    # self).get_context_data(**kwargs)
    # if request.method == 'GET':
    #     from anmaabankApp.views import saveInfoIp

    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'blog-single.html?page=' +
    #    str(request.GET.get('page', 1)))
    # Create any data and add it to the context
    # category_blog = int(self.request.GET.get('category_blog', 0))
    # print("category_blog")
    # print(category_blog)
    # if category_blog != 0:
    # context['daily_flight_list'] = Blogs.objects.filter(
    # category_blog=category_blog)
    # context['CategoryBlog'] =
    # context['CategoryBlog'] =
    # images_blogs = ImagesBlogs.objects.filter(blog=id)
    # qs = None
    # if id != None:
    qs = Policies.objects.filter(category="مكافحة غسل الأموال",)
    context['policie'] = qs.first()

    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    # context['FormOurNewsletter'] = OurNewsletterForm()
    # context['imagesblogs'] = images_blogs
    # "imagesservice": images_services,

    # context['CategoryBlog'] = CategoryBlog.objects.all(
    #     # title__icontains='war'
    # ).annotate(Blogs_count=Count('category_blog'))
    if qs != None:
        context["titel"] = "  سياسة الخصوصية  Page not found(404) " if qs.first(
        ) == None else qs.first().titel
    if qs != None:
        context["title"] = "سياسة  الخصوصية  Page not found(404) " if qs.first(
        ) == None else qs.first().titel,

    else:
        context["title"] = "سياسة  الخصوصية " + " Page not found(404) "
        context["titel"] = "سياسة  الخصوصية " + " Page not found(404) "

    context["url"] = getUrl(request=request)

    " "
    # context["title"] =
    # .annotate(
    # total_completed=Count(
    # Case(
    # When(
    # status='completed', then=1), output_field=DecimalField()
    # )
    # ),
    # total_failed=Count(
    # Case(
    # When(status='failed', then=1), output_field=DecimalField()
    # )
    # )
# )
    # context['page'] = intrequest.GET.get('page', 1))

    context["static_content"] = static_content[lang]
    context['some_data'] = 'This is just some data'
   
    # return context

    # def get_queryset(self):

    # category_blog = int(request.GET.get('category_blog', 0))

    # date_post__gte = self.request.GET.get(
    # 'date_post__gte', 0)
    # date_post__lt = self.request.GET.get(
    # 'date_post__lt', 0)

    # print("category_blog")
    if request.method == 'POST':
        SaveContact(request, "blog-single.html", context)
        return render(request, 'blog-single.html', context)
    # return context
    return render(request, 'blog-single.html', context)

    # Specify your own template name/location


def PoliciesSingleListView(request, id, lang = "ar"):
    if lang is None or lang not in("ar","en"):
        lang = 'ar'

    from django.db.models import Count, Case, When
    context = {

    }
    # if request.method == 'POST':
    #     return SaveContact(request,"blog.html",context)
    # Call the base implementation first to get the context
    # context = super(BlogsListView,
    # self).get_context_data(**kwargs)
    # if request.method == 'GET':
    #     from anmaabankApp.views import saveInfoIp

    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'blog-single.html?page=' +
    #    str(request.GET.get('page', 1)))
    # Create any data and add it to the context
    # category_blog = int(self.request.GET.get('category_blog', 0))
    # print("category_blog")
    # print(category_blog)
    # if category_blog != 0:
    # context['daily_flight_list'] = Blogs.objects.filter(
    # category_blog=category_blog)
    # context['CategoryBlog'] =
    # context['CategoryBlog'] =
    # images_blogs = ImagesBlogs.objects.filter(blog=id)
    # qs = None
    # if id != None:
    qs = Policies.objects.filter(id=id,)
    context['policie'] = qs.first()

    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    # context['FormOurNewsletter'] = OurNewsletterForm()
    # context['imagesblogs'] = images_blogs
    # "imagesservice": images_services,

    # context['CategoryBlog'] = CategoryBlog.objects.all(
    #     # title__icontains='war'
    # ).annotate(Blogs_count=Count('category_blog'))
    if qs != None:
        context["titel"] = "  سياسة الخصوصية  Page not found(404) " if qs.first(
        ) == None else qs.first().titel
    if qs != None:
        context["title"] = "سياسة  الخصوصية  Page not found(404) " if qs.first(
        ) == None else qs.first().titel,

    else:
        context["title"] = "سياسة  الخصوصية " + " Page not found(404) "
        context["titel"] = "سياسة  الخصوصية " + " Page not found(404) "

    context["url"] = getUrl(request=request)

    " "
    # context["title"] =
    # .annotate(
    # total_completed=Count(
    # Case(
    # When(
    # status='completed', then=1), output_field=DecimalField()
    # )
    # ),
    # total_failed=Count(
    # Case(
    # When(status='failed', then=1), output_field=DecimalField()
    # )
    # )
# )
    # context['page'] = intrequest.GET.get('page', 1))

    # context['some_data'] = 'This is just some data'
    # return context

    # def get_queryset(self):

    # category_blog = int(request.GET.get('category_blog', 0))

    # date_post__gte = self.request.GET.get(
    # 'date_post__gte', 0)
    # date_post__lt = self.request.GET.get(
    # 'date_post__lt', 0)

    # print("category_blog")
    if request.method == 'POST':
        SaveContact(request, "blog-single.html", context)
        return render(request, 'blog-single.html', context)
    # return context
    return render(request, 'blog-single.html', context)

    # Specify your own template name/location
