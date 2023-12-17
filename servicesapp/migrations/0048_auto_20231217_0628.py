# Generated by Django 3.2.22 on 2023-12-17 03:28

import branches.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0047_auto_20231216_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='services',
            name='cover_image_ar',
            field=models.ImageField(null=True, upload_to='Image/Service/%Y/%m/%d/', verbose_name='صورة الغلاف عربي'),
        ),
        migrations.AddField(
            model_name='services',
            name='cover_image_en',
            field=models.ImageField(null=True, upload_to='Image/Service/%Y/%m/%d/', verbose_name='صورة الغلاف انجليزي'),
        ),
        migrations.AddField(
            model_name='services',
            name='image_ar',
            field=models.ImageField(null=True, upload_to='Image/Service/%Y/%m/%d/', verbose_name='صورة الخدمة عربي'),
        ),
        migrations.AddField(
            model_name='services',
            name='image_en',
            field=models.ImageField(null=True, upload_to='Image/Service/%Y/%m/%d/', verbose_name='صورة الخدمة انجليزي'),
        ),
        migrations.AlterField(
            model_name='bankapplications',
            name='app_store',
            field=models.URLField(blank=True, help_text='https://apps.apple.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق على اب استور '),
        ),
        migrations.AlterField(
            model_name='bankapplications',
            name='desketop',
            field=models.URLField(blank=True, help_text='https://play.google.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق تحميل desketop'),
        ),
        migrations.AlterField(
            model_name='bankapplications',
            name='google_play',
            field=models.URLField(blank=True, help_text='https://play.google.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق على جوجل ابلاي '),
        ),
    ]