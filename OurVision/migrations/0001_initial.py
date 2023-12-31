# Generated by Django 3.2.22 on 2023-11-09 11:00

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
            name='OurVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250, null=True, verbose_name='عنوان القسم')),
                ('detial_ar', tinymce.models.HTMLField(blank=True, default=' ', null=True, verbose_name='تفاصيل رؤية الشركة')),
                ('image', models.ImageField(null=True, upload_to='Image/OurVision/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='OurVision_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='OurVision_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='OurVision_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'رؤيتنــــا',
                'verbose_name_plural': 'رؤيتنــــا',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250, null=True, verbose_name='عنوان القسم')),
                ('detial_ar', tinymce.models.HTMLField(blank=True, default=' ', null=True, verbose_name='تفاصيل')),
                ('image', models.ImageField(null=True, upload_to='Image/OurVision/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Objectives_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Objectivesn_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Objectives_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'الـــغـــايــات',
                'verbose_name_plural': 'الـــغـــايــات',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MassegeAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250, verbose_name='العنوان')),
                ('detial_ar', tinymce.models.HTMLField(null=True, verbose_name='التفاصيل')),
                ('image', models.ImageField(null=True, upload_to='Image/About/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MassegeAbout_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MassegeAbout_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MassegeAbout_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'الرسالة',
                'verbose_name_plural': 'الرسالة',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250, verbose_name='العنوان')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('detial_ar', tinymce.models.HTMLField(default=' ', max_length=100000, null=True, verbose_name='التفاصيل')),
                ('image', models.ImageField(null=True, upload_to='Image/About/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Abouton_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='About_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='About_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'عنا',
                'verbose_name_plural': 'عنا',
                'managed': True,
            },
        ),
    ]
