# Generated by Django 3.2.22 on 2023-12-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurNewsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='emile',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الألكتروني'),
        ),
    ]
