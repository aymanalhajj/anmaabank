# Generated by Django 3.2.22 on 2023-12-15 15:47

from django.db import migrations, models
import teams.models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0025_auto_20231204_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='facebook',
            field=models.URLField(blank=True, help_text='https://facebook.com', null=True, validators=[teams.models.validate_hostname], verbose_name='رابط حساب الفيسبوك إن وجد '),
        ),
        migrations.AlterField(
            model_name='teams',
            name='instagram',
            field=models.URLField(blank=True, help_text='https://instagram.com', null=True, validators=[teams.models.validate_hostname], verbose_name='رابط حساب انستجرام إن وجد '),
        ),
        migrations.AlterField(
            model_name='teams',
            name='linkedin',
            field=models.URLField(blank=True, help_text='https://linkedin.com', null=True, validators=[teams.models.validate_hostname], verbose_name='رابط حساب لنكدإن  إن وجد '),
        ),
        migrations.AlterField(
            model_name='teams',
            name='twitter',
            field=models.URLField(blank=True, help_text='https://twitter.com', null=True, validators=[teams.models.validate_hostname], verbose_name='رابط حساب تويتر او منصة اكس إن وجد '),
        ),
        migrations.AlterField(
            model_name='teams',
            name='youtube',
            field=models.URLField(blank=True, help_text='https://youtube.com', null=True, validators=[teams.models.validate_hostname], verbose_name='رابط قناة اليوتيوب '),
        ),
    ]
