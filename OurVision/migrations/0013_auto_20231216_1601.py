# Generated by Django 3.2.22 on 2023-12-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurVision', '0012_auto_20231216_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourvision',
            name='detial_ar',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='تفاصيل رؤية الشركة'),
        ),
        migrations.AlterField(
            model_name='ourvision',
            name='detial_en',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='تفاصيل رؤية الشركة بالانجليزي'),
        ),
    ]