# Generated by Django 3.2.22 on 2023-11-20 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jopapp', '0001_initial'),
        ('loan_app', '0004_auto_20231120_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jopapp.register', verbose_name='المستخدم'),
        ),
    ]
