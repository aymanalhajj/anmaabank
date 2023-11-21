# Generated by Django 3.2.22 on 2023-11-19 19:25

from django.db import migrations, models
import settingapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('settingapp', '0004_auto_20231119_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingmodel',
            name='facebook',
            field=models.URLField(blank=True, help_text='https://facebook.com', null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط حساب الفيسبوك إن وجد '),
        ),
        migrations.AlterField(
            model_name='settingmodel',
            name='instagram',
            field=models.URLField(blank=True, help_text='https://instagram.com', null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط حساب انستجرام إن وجد '),
        ),
        migrations.AlterField(
            model_name='settingmodel',
            name='linkedin',
            field=models.URLField(blank=True, null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط حساب لنكدإن  إن وجد '),
        ),
        migrations.AlterField(
            model_name='settingmodel',
            name='telegram',
            field=models.URLField(blank=True, help_text='https://t.me/', null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط تلجرام إن وجد '),
        ),
        migrations.AlterField(
            model_name='settingmodel',
            name='twitter',
            field=models.URLField(blank=True, help_text='https://twitter.com', null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط حساب تويتر او منصة اكس إن وجد '),
        ),
        migrations.AlterField(
            model_name='settingmodel',
            name='youtube',
            field=models.URLField(blank=True, help_text='https://youtube.com', null=True, validators=[settingapp.models.validate_hostname], verbose_name='رابط قناة اليوتيوب '),
        ),
    ]
