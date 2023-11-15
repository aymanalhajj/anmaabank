# Generated by Django 3.2.22 on 2023-11-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anmaabankApp', '__first__'),
        ('servicesapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adsence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tital_AR', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالعربي')),
                ('Tital_EN', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالانجليزي')),
                ('Description_AR', models.CharField(max_length=1000, null=True, verbose_name='  الوصف عربي')),
                ('Description_EN', models.CharField(blank=True, max_length=1000, null=True, verbose_name='  الوصف انجليزي')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('image', models.ImageField(upload_to='Image/Adsence/%Y/%m/%d/%H/%M/%S')),
                ('Price', models.FloatField(default=0.0)),
                ('url_ads', models.URLField(blank=True, max_length=1000, null=True, verbose_name='الرابط')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serviceAdsence', to='servicesapp.services', verbose_name='المنتج')),
            ],
            options={
                'verbose_name': 'الأعلانات ',
                'verbose_name_plural': ' الأعلانات ',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AdsenceFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tital_AR', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالعربي')),
                ('Tital_EN', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالانجليزي')),
                ('Description_AR', models.CharField(max_length=1000, null=True, verbose_name='  الوصف عربي')),
                ('Description_EN', models.CharField(blank=True, max_length=1000, null=True, verbose_name='  الوصف انجليزي')),
                ('image', models.ImageField(null=True, upload_to='Image/Adsence/AdsenceHeder/%Y/%m/%d/%H/%M/%S', verbose_name='صورة الاعلان')),
                ('url_ads', models.URLField(blank=True, max_length=1000, null=True, verbose_name='الرابط')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('Date_Finish_Posted', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ أنتهاء النشر ')),
                ('Price', models.FloatField(default=0.0)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_footer', to='servicesapp.services', verbose_name='الخدمات')),
                ('service_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_application_ads_footer', to='servicesapp.bankapplications', verbose_name='خدمات التطبيقات')),
            ],
            options={
                'verbose_name': 'الأعلان في الاسف ',
                'verbose_name_plural': 'الأعلانات في الاسف ',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AdsenceHeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tital_AR', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالعربي')),
                ('Tital_EN', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان بالانجليزي')),
                ('Description_AR', models.CharField(blank=True, max_length=1000, null=True, verbose_name=' الوصف بالعربي ')),
                ('Description_EN', models.CharField(blank=True, max_length=1000, null=True, verbose_name=' الوصف بالانجليزي ')),
                ('image', models.ImageField(null=True, upload_to='Image/Adsence/AdsenceHeder/%Y/%m/%d/%H/%M/%S', verbose_name='صورة الاعلان')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('Date_Finish_Posted', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ أنتهاء النشر ')),
                ('Price', models.FloatField(default=0.0)),
                ('url_ads', models.URLField(blank=True, max_length=1000, null=True, verbose_name='الرابط')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_ads_header', to='servicesapp.services', verbose_name='الخدمات')),
                ('service_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_application_ads_header', to='servicesapp.bankapplications', verbose_name='خدمات التطبيقات')),
            ],
            options={
                'verbose_name': 'الأعلان في الصفحة الرئيسية ',
                'verbose_name_plural': 'صور إعلان متحرك في الصفحة الرئيسية ',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ViewAdsenceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('ipInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipInfoViewAdsenceHeader', to='anmaabankApp.ipinfo')),
                ('viewAdsenceHeader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsense.adsenceheder', verbose_name='الاعلانات في الاعلى')),
            ],
            options={
                'verbose_name': 'مشاهدات الاعلانات في الأعلى',
                'verbose_name_plural': 'مشاهدات الاعلانات في الاعلى',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ViewAdsenceFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('adsencefooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsense.adsencefooter', verbose_name='الاعلانات في الأسفل')),
                ('ipInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipInfoViewAdsenceFooter', to='anmaabankApp.ipinfo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userViewAdsenceFooter', to='anmaabankApp.requesthederinfo')),
            ],
            options={
                'verbose_name': 'مشاهدات الاعلانات في الاسفل',
                'verbose_name_plural': 'مشاهدات الاعلانات في الاسفل',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ViewAdcence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMEI_device', models.CharField(max_length=30, null=True, verbose_name='رقم معرف الجوال')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('adsence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsense.adsence', verbose_name='الاعلانات')),
                ('ipInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipInfoViewAdcence', to='anmaabankApp.ipinfo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userViewAdcence', to='anmaabankApp.requesthederinfo')),
            ],
            options={
                'verbose_name': 'مشاهدات الاعلانات',
                'verbose_name_plural': 'مشاهدات الاعلانات',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PressAdsenceHeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('url_ads', models.URLField(blank=True, max_length=1000, null=True, verbose_name='الرابط')),
                ('adsenceheder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsense.adsenceheder', verbose_name='الاعلانات في الاعلى')),
                ('ipInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipInfoPressAdsenceHeder', to='anmaabankApp.ipinfo')),
            ],
            options={
                'verbose_name': 'الضغط على الاعلانات في الاعلى',
                'verbose_name_plural': 'الضغط على الاعلانات في الاعلى',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PressAdsenceFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('Date_Update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('url_ads', models.URLField(blank=True, max_length=1000, null=True, verbose_name='الرابط')),
                ('adsencefooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsense.adsencefooter', verbose_name='الاعلانات في الأسفل')),
                ('ipInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipInfoPressAdsenceFooter', to='anmaabankApp.ipinfo')),
            ],
            options={
                'verbose_name': 'الضغط على الاعلانات في الاسفل',
                'verbose_name_plural': 'الضغط على الاعلانات في الاسفل',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
