from django.db import models

# Create your models here.


VIDEO_SOURCES = (
    ('file','ملف'),
    ('url','رابط')
)

REPORT_TYPE = (
    ('yearly','تقرير سنوي'),
    ('finance','تقرير مالي')
)


class Video(models.Model):
    title = models.CharField(max_length = 200,                                  verbose_name="عنوان الفيديو")
    source_type = models.CharField(max_length = 200,choices = VIDEO_SOURCES, verbose_name="مصدر الفيديو")
    url = models.URLField(max_length = 200,                                     verbose_name="رابط الفيديو")
    filename = models.FileField(max_length = 200,                                   verbose_name="ملف الفيديو")

    class Meta:
        managed = True
        verbose_name = "الفيديو"
        verbose_name_plural = "مكتبة الفيديوهات"

class Report(models.Model):
    title = models.CharField(max_length = 200,                                  verbose_name="اسم التقرير")
    report_type = models.CharField(max_length = 200,choices = REPORT_TYPE  ,    verbose_name="نوع التقرير")
    thumbnail_name = models.FileField(max_length = 200,                         verbose_name="صورة التقرير")
    filename = models.FileField(max_length = 200,                               verbose_name="ملف التقرير")

    class Meta:
        managed = True
        verbose_name = "التقرير"
        verbose_name_plural = "التقارير"