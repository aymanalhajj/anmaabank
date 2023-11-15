# Generated by Django 3.2.22 on 2023-11-09 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='رقم التلفون ان وجد')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Image/Clients/%Y/%m/%d/', verbose_name='صورة الشعار ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='رقم الترتيب (يرتب بالموقع حسب الرقم)')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': ' العملاء ',
                'verbose_name_plural': 'العملاء',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
