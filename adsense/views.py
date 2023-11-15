from django.shortcuts import render
import datetime
from django.db.models import Q

from .models import *
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View
# Create your views here.


def AdsenceHederQuerySet():
    current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = AdsenceHeder.objects.all().order_by('Date_Update').filter(
        Q(Date_Finish_Posted__date__gt=current_datetime)
        |
        Q(Date_Finish_Posted__isnull=True))
    return queryset

    # serializer_class = AdsenceHederSerializer
