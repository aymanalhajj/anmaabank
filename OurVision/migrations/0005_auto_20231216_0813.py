# Generated by Django 3.2.22 on 2023-12-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurVision', '0004_auto_20231216_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectives',
            name='detail_ar',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='تفاصيل بالعربي'),
        ),
        migrations.AlterField(
            model_name='objectives',
            name='detial_ar',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='تفاصيل بالعربي'),
        ),
    ]