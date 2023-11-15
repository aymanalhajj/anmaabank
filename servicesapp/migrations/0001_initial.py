# Generated by Django 3.2.22 on 2023-11-09 11:02

import branches.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('country_regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, verbose_name='اسم التطبيق')),
                ('detial_ar', models.CharField(blank=True, max_length=250, null=True, verbose_name='اسم التطبيق')),
                ('logo_image', models.ImageField(null=True, upload_to='Image/BankApplications/Logo/%Y/%m/%d/', verbose_name=' ايقون شعار التطبيق صورة مصغر ')),
                ('screen_image', models.ImageField(null=True, upload_to='Image/BankApplications/Screen/%Y/%m/%d/', verbose_name=' صورة شاشة التطبيق')),
                ('barcode_image', models.ImageField(null=True, upload_to='Image/BankApplications/Barcode/%Y/%m/%d/', verbose_name=' صورة باركود تحميل التطبيق')),
                ('type_choice', models.CharField(choices=[('desketop', 'تطبيق سطح المكتب'), ('mobile', 'تطبيق جوال'), ('website', 'موقع الكتروني ')], max_length=8, null=True, verbose_name='نوع التطبيق')),
                ('google_play', models.URLField(blank=True, help_text='https://play.google.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق على جوجل ابلاي ')),
                ('app_store', models.URLField(blank=True, help_text='https://apps.apple.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق على اب استور ')),
                ('desketop', models.URLField(blank=True, help_text='https://play.google.com', null=True, validators=[branches.models.validate_hostname], verbose_name='رابط تطبيق تحميل desketop')),
                ('website', models.URLField(blank=True, help_text='http://alinmabank.com', null=True, verbose_name='رابط website')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا التطبيق من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('is_hidden', models.BooleanField(default=False, help_text='سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  ', verbose_name='مخفي ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_applications_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_applications_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_applications_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'تطبيقات البنك',
                'verbose_name_plural': 'تطبيقات البنك',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CategoriesServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, unique=True, verbose_name='ا')),
                ('description', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='وصف مختصر جملة واحده فقط')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('is_hidden', models.BooleanField(default=False, help_text='سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  ', verbose_name='مخفي ')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل ')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_services_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_services_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_services_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'نوع الخدمة',
                'verbose_name_plural': 'نوع الخدمة',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100, verbose_name='العنوان')),
                ('short_detial', models.CharField(max_length=100, null=True, verbose_name='وصف مختصر جملة واحده فقط')),
                ('detial_ar', tinymce.models.HTMLField(default=' ', max_length=100000, null=True, verbose_name='التفاصيل')),
                ('name_action', models.CharField(blank=True, help_text='عنوان البوتون المراد النقر  فيها مثال : احجز الان او استفسر اكثر', max_length=250, null=True, verbose_name='اسم الحدث (النقرة)')),
                ('booking_link', models.URLField(blank=True, null=True, verbose_name='رابط الحجز او استفسار عن الخدمة (اختياري)')),
                ('phone_whatsapp', models.CharField(blank=True, help_text='https://api.whatsapp.com/send/?phone=phone_number_whatsapp  with out +', max_length=20, null=True, verbose_name='رقم تلفون الواتساب للحجز او استفسار عن الخدمة (اختياري)')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='رقم تلفون اتصال للحجز او استفسار عن الخدمة (اختياري)')),
                ('image', models.ImageField(null=True, upload_to='Image/Service/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا الرئي من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('is_hidden', models.BooleanField(default=False, help_text='سيتم اخفاء هذا التطبيق  من العرض بالموقع بحال تم تحديده وسيعتبر بانه مخفي مؤقتاً  ', verbose_name='مخفي ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=1000, null=True, verbose_name='ملاحظة قصيرة')),
                ('category_services', models.ForeignKey(help_text='مثال : خدمات الشركات او خدمات الأفراد او خدمات المنظمات', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_services', to='servicesapp.categoriesservices', verbose_name='نوع الخدمة')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_created_by', to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': 'الخدمة',
                'verbose_name_plural': 'الخدمات',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_whatsapp', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم تلفون الواتساب')),
                ('Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='رقم التلفون ')),
                ('emile', models.EmailField(blank=True, max_length=254, null=True, verbose_name='  البريد الألكتروني')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='إسمك')),
                ('cookie', tinymce.models.HTMLField(blank=True, default=' ', max_length=100000, null=True)),
                ('Message', tinymce.models.HTMLField(max_length=1000, null=True, verbose_name='الرساله')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countr_ServiceRequests', to='country_regions.country', verbose_name='الدولة')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_requests', to='servicesapp.services', verbose_name=' الخدمة')),
                ('service_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_application_requests', to='servicesapp.bankapplications', verbose_name='خدمات التطبيقات')),
            ],
            options={
                'verbose_name': ' حجوزات الخدمات ',
                'verbose_name_plural': 'حجوزات الخدمات  ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagesServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Image/ImagesServices/%Y/%m/%d/', verbose_name=' إختيار صورة')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicesapp.services', verbose_name=' الخدمة')),
            ],
            options={
                'verbose_name': 'صور خدمات البنك  ',
                'verbose_name_plural': 'صور خدمات البنك',
            },
        ),
        migrations.CreateModel(
            name='FutureApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='اسم الميزة')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأضافة')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('applications', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='future_applications', to='servicesapp.bankapplications', verbose_name='التطبيق')),
            ],
            options={
                'verbose_name': 'مميزات التطبيق',
                'verbose_name_plural': 'مميزات التطبيق',
            },
        ),
    ]
