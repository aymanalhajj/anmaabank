# Generated by Django 3.2.22 on 2023-11-21 00:46

import branches.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0016_auto_20231121_0340'),
    ]

    operations = [
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
