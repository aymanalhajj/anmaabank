# Generated by Django 3.2.22 on 2023-12-16 05:13

import branches.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0027_auto_20231216_0756'),
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
