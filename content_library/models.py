from django.db import models
from urllib.parse import urlparse,parse_qs

# Create your models here.


VIDEO_SOURCES = (
    ('file','ملف'),
    ('url','رابط')
)

REPORT_TYPE = (
    ('yearly','تقرير سنوي'),
    ('finance','تقرير مالي')
)

def get_mime_type(file):
    """
    Get MIME by reading the header of the file
    """
    initial_pos = file.tell()
    file.seek(0)
    mime_type = magic.from_buffer(file.read(2048), mime=True)
    file.seek(initial_pos)
    return mime_type


def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

class Video(models.Model):
    title = models.CharField(max_length = 200,                                  verbose_name="عنوان الفيديو")
    source_type = models.CharField(max_length = 200,choices = VIDEO_SOURCES, verbose_name="مصدر الفيديو")
    url = models.URLField(max_length = 200,                                     verbose_name="رابط الفيديو")
    filename = models.FileField(max_length = 200,                                   verbose_name="ملف الفيديو")
    mime_type = models.CharField(max_length = 200,                                   verbose_name="نوع الفيديو")
    def save(self, *args, **kwargs):
        if self.filename and self.filename.file:
            try: 
                #Need to add a try catch such that in case a file is not being uploaded, then the mime_type is not assigned
                self.mime_type=self.filename.file.content_type
            except Exception as e:
                print(e)
                pass
            try: 
                youtube_video_id = video_id(self.url)
                if youtube_video_id != None:
                    self.url  = "https://www.youtube.com/embed/"+youtube_video_id
                #self.mime_type = get_mime_type(self.filename.file)
            except  Exception as e:
                print("youtube_video_id error")
                print(e)
                pass
        super().save(*args, **kwargs)
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