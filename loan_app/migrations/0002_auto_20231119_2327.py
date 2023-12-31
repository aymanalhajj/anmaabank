# Generated by Django 3.2.22 on 2023-11-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuaranteeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='اسم نوع الضمانه')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='وصف مختصر لنوع الضمانة')),
            ],
            options={
                'verbose_name': 'نوع  الضمانه',
                'verbose_name_plural': 'نوع الضمانات',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'managed': True, 'verbose_name': 'نوع النشاط', 'verbose_name_plural': 'نوع النشاط'},
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='وصف مختصر لنوع النشاط'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='اسم نوع النشاط'),
        ),
    ]
