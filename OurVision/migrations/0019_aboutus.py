# Generated by Django 4.2.7 on 2024-01-07 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OurVision', '0018_auto_20231216_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='العنوان')),
                ('detail_ar', models.TextField(blank=True, default=' ', null=True, verbose_name='التفاصيل بالعربي')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='العنوان انجليزي')),
                ('detail_en', models.TextField(blank=True, default=' ', null=True, verbose_name='التفاصيل بالانجليزي')),
                ('image', models.ImageField(null=True, upload_to='Image/About/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Aboutus_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Aboutus_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Aboutus_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'عنا',
                'verbose_name_plural': 'عنا',
                'managed': True,
            },
        ),
    ]
