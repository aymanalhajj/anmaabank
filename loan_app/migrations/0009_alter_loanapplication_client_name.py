# Generated by Django 3.2.22 on 2023-11-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0008_alter_loanapplication_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='client_name',
            field=models.CharField(max_length=200, verbose_name='client name'),
        ),
    ]
