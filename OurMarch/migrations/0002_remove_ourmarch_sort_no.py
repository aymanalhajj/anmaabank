# Generated by Django 4.0 on 2023-05-06 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OurMarch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourmarch',
            name='sort_no',
        ),
    ]
