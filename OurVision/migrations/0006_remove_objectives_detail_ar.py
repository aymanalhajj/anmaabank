# Generated by Django 3.2.22 on 2023-12-16 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OurVision', '0005_auto_20231216_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectives',
            name='detail_ar',
        ),
    ]
