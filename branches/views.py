from django.shortcuts import render
from .models import Branches
from navbarapp.views import NavbarsQuerySet, ColumnNavbarsQuerySet
from sectionpage.views import SectionPageHomeQuerySet, SectionPagePageQuerySet
from settingapp.views import SettingModelQuerySet
# Create your views here.
from .form import SerchModelForm
from django.db.models import Q

from country_regions.models import Region


def getUrl(request):
    if request is None:
        raise Exception("request is None")

    return request.build_absolute_uri()


def BranchesHederQuerySet():
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Branches.objects.all().order_by('created_at').filter()
    return queryset

    # serializer_class = BranchesHederSerializer


def service_points(request, id=None):

    from anmaabankApp.views import get_cookie

    # if request.method == 'GET':
    # saveInfoReqestHeder(request, 'index.html')
    # saveInfoIp(request, 'service-single.html')
    form = SerchModelForm()

    context = {
        # 'data': data,
        'form': form,
        # "imagesservice": images_services,
        "titel": " نقاط الخدمة  ",
        "title":  " نقاط الخدمة  ",
        "url": getUrl(request=request),
        # 'ImagesPortfolioss': dataImagesPortfolio,
        # 'FormOurNewsletter': OurNewsletterForm(),

    }

    # dataImagesPortfolio = ImagesPortfolio.objects.all()
    # context['ImagesPortfolioss'] = dataImagesPortfolio

    # if dataAbout is not None:
    # dataAbout = dataAbout.latest('Date_Added')

    # context['services'] = dataAbout.first()
    context["navbar"] = NavbarsQuerySet()
    context["ColumnNavbars"] = ColumnNavbarsQuerySet()
    context['setting'] = SettingModelQuerySet()
    context["branches"] = BranchesHederQuerySet()
    if id != None:
        qs = Branches.objects.all().order_by(
            'created_at').filter(id=id).first()
        context["branche"] = qs
        context["titel"] = " نقاط الخدمة  " + " - نقطة - "+str(qs.name)
        context["title"] = " نقاط الخدمة  " + " - نقطة - "+str(qs.name)
    if request.method == 'POST':
        form = SerchModelForm(request.POST, request.FILES)
        # formOurNewsletterForm = OurNewsletterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            # messages.success(request, 'تم الإضافة بنجاح')
            # return redirect(revers_fun)
            # formOurNewsletterForm.save()
            category = request.POST["category"]
            region = request.POST["region"]
            search = request.POST["search"]
            print(category)
            print(region)
            display_name_ar = ""

            queryset = Branches.objects.all().order_by(
                'created_at').filter()
            if search is not None and search is not "":
                queryset = queryset.filter(

                    Q(name__icontains=search) |
                    Q(phone__icontains=search) |
                    Q(HORSE__icontains=search) |
                    Q(from_hourse_firest__icontains=search) |
                    Q(to_hourse_firest__icontains=search) |
                    Q(from_hourse_scond__icontains=search) |
                    Q(to_hourse_scond__icontains=search) |
                    Q(category__icontains=search) |


                    Q(address1__region__name__icontains=search) |
                    Q(address1__region__name_ar__icontains=search) |
                    # Q(address1__region__display_name_ar__icontains=search) |
                    # Q(address1__region__display_name__icontains=search) |
                    #    Q(address1__region__name__icontains=search) |
                    Q(address1__long__icontains=search) |

                    Q(address1__address_line__icontains=search) |
                    Q(address1__street__icontains=search) |
                    Q(address1__lat__icontains=search) |
                    Q(address1__long__icontains=search) |
                    Q(address1__map_location__icontains=search) |

                    Q(address1__postcode__icontains=search) |


                    Q(address1__region__country__name__icontains=search) |
                    Q(address1__region__country__name_ar__icontains=search)
                    # Q(address1__region__country__display_name_ar__icontains=search) |
                    # Q(address1__region__country__display_name__icontains=search)

                )
            if category is not None and category is not "":
                queryset = queryset.filter(category=category,)
            if region is not None and region is not "":
                queryset = queryset.filter(address1__region=region)

                if Region.objects.filter(
                        pk=region).exists():
                    display_name_ar = Region.objects.filter(
                        pk=region).first().display_name_ar
                    context["region"] = display_name_ar
                # else:
                context["titel"] = " نقاط الخدمة  ",
                context["title"] = " نقاط الخدمة  ",
            context["branches"] = queryset
            context["form"] = form
            context["category"] = category

        # SaveContact(request, "index.html", context)
        return render(request, 'service-points.html', context)
    else:
        context["branches"] = BranchesHederQuerySet()

    return render(request, 'service-points.html', context)
