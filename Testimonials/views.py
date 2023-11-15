from django.shortcuts import render
from .models import *

# Create your views here.
# FrequentlyAskedQuestionsQuerySet,TestimonialsQuerySet
def TestimonialsQuerySet():
    # sendEmile()
    # current_datetime = datetime.datetime.now().date()
    # print(current_datetime)
    queryset = Testimonials.objects.filter(
        is_deleted=False, is_hidden=False,).order_by('sort_no')
    return queryset
