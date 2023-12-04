from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone
from tinymce.models import HTMLField

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    detial_ar = HTMLField(
        # blank=True,
        null=True,
        # max_length=1000000000,
        default="",
        verbose_name=_("تفاصيل")
    )
    # title_en = models.CharField(max_length=255)
    # detial_en = HTMLField(
    #     # blank=True,
    #     null=True,
    #     # max_length=1000000000,
    #     default="",
    #     verbose_name=_("تفاصيل")
    # )
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant

# class Skill(models.Model):
#     name = models.CharField(max_length = 64)

#     def __str__(self):
#         return f"{self.name}"
# class Candidate(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee")
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skill")

#     def __str__(self):
#         return f"{self.id}: {self.employee} knows - {self.skill}"
# class Experience(models.Model):
#     """Model representing a tutor's experience."""
#     # tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

#     name = models.CharField(max_length=100, null=True, blank=True)
#     # job_position_one = models.CharField(max_length=100, null=True, blank=True)

#     # organization_two = models.CharField(max_length=100, null=True, blank=True)
#     # job_position_two = models.CharField(max_length=100, null=True, blank=True)

#     # organization_three = models.CharField(max_length=100, null=True, blank=True)
#     # job_position_three = models.CharField(max_length=100, null=True, blank=True)
#     # ...
# # Create your models here.
# class Career(models.Model):
#     # """Model representing a Career."""
#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)
#    email_address = models.EmailField(max_length=100, primary_key=True)
#    phone_num = models.CharField(max_length=15)
#    years_of_experience = models.IntegerField(default=0)
#    username = models.CharField(max_length=50, unique=True)
#    cv = models.FileField(
#     storage=FileSystemStorage(location=settings.MEDIA_ROOT),
#     upload_to='cv',
#     )