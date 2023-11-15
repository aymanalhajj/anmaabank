# Generated by Django 3.2.22 on 2023-11-09 10:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=70, verbose_name='عنوان الخبر او المقالة')),
                ('image', models.ImageField(null=True, upload_to='Image/Blog/%Y/%m/%d/', verbose_name=' إختيار صورة المدونة')),
                ('category', models.CharField(choices=[('اخبار البنك', 'اخبار البنك'), ('الفعاليات', 'الفعاليات'), ('المدونة', 'المدونة')], max_length=100, null=True, verbose_name='نوع المقال')),
                ('date_post', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='تاريخ النشر ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('detial_ar', tinymce.models.HTMLField(null=True, verbose_name='المقال او المحتوى')),
            ],
            options={
                'verbose_name': '  المقالات و آخر الأخبار  ',
                'verbose_name_plural': '  المقالات و آخر الأخبار  ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=70, verbose_name='عنوان السياسة ')),
                ('detial_ar', tinymce.models.HTMLField(default='', max_length=1000000000, null=True, verbose_name='تفاصيل')),
                ('image', models.ImageField(null=True, upload_to='Image/Blog/%Y/%m/%d/', verbose_name=' إختيار صورة السياسة')),
                ('category', models.CharField(choices=[('سياسة خصوصية', 'سياسة خصوصية'), ('مكافحة غسل الأموال', 'مكافحة غسل الأموال'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='نوع السياسة')),
                ('date_post', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='تاريخ النشر ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
            ],
            options={
                'verbose_name': ' السياسات ',
                'verbose_name_plural': '  السياسات ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagesBlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Image/ImagesBlogs/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.blogs', verbose_name=' المقال')),
            ],
            options={
                'verbose_name': 'صور المدونة البنك  ',
                'verbose_name_plural': 'صور المدونة البنك',
            },
        ),
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='عنوان القسم  ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
            ],
            options={
                'verbose_name': ' قسم المقالات و آخر الأخبار  ',
                'verbose_name_plural': ' قسم المقالات و آخر الأخبار  ',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='category_blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_blog', to='blogapp.categoryblog', verbose_name='الصنف'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة '),
        ),
    ]
