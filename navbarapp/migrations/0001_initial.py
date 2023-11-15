# Generated by Django 3.2.22 on 2023-11-09 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sectionpage', '0001_initial'),
        ('portfolioapp', '__first__'),
        ('servicesapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnNavbars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, null=True, unique=True, verbose_name=' اسم القسم  ')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='رقم الترتيب (يرتب بالموقع حسب الرقم)')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=200, null=True, verbose_name='ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RowNavbars_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RowNavbars_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
            ],
            options={
                'verbose_name': ' العنوان الثنوي في رأس الصفحة',
                'verbose_name_plural': ' العنوان الثنوي في رأس الصفحة',
                'db_table': '',
                'ordering': ['sort_no'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Navbars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(db_index=True, max_length=100, verbose_name='URL')),
                ('titel', models.CharField(max_length=50, null=True, unique=True, verbose_name='العنوان')),
                ('dicript', models.CharField(blank=True, max_length=100, null=True, verbose_name='جملة مختصرة معبرة تكتب تحت العنوان  ')),
                ('display_at', models.CharField(choices=[('navbar', ' في الشريط اعلى الصفحات'), ('footer', ' اسفل الصفخات'), ('none', 'عدم عرضه في اي شريط ( منفصل برابط مخصص له)')], max_length=100, null=True, verbose_name='مكان عرض القسم')),
                ('parent_section', models.CharField(choices=[('1', 'خدمات الأفراد'), ('2', 'خدمات المنظمات'), ('3', 'خدمات الشركات'), ('4', 'تطبيقات البنك'), ('5', 'التمويل الأصغر '), ('6', 'الاقسام')], max_length=100, null=True, verbose_name='مكان عرض القسم')),
                ('is_hidden', models.BooleanField(default=False, help_text=' سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده', verbose_name='مخفي')),
                ('is_deleted', models.BooleanField(default=False, help_text='سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ', verbose_name='محذوف ')),
                ('Date_Update', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل ')),
                ('Date_Added', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافة ')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاريخ الحذف ')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الأنشاء ')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ اخر تعديل ')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='رقم الترتيب (يرتب بالموقع حسب الرقم)')),
                ('short_note', models.CharField(blank=True, default=' ', help_text=' اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً', max_length=200, null=True, verbose_name='ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)')),
                ('bank_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicesapp.bankapplications', unique=True, verbose_name='تطبيقات البنك')),
                ('column_navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='column_navbar_chield', to='navbarapp.columnnavbars', verbose_name='العمود')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم الأنشاء بواسطة ')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SecondaryNavbars_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم الحذف  بواسطة ')),
                ('edited_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SecondaryNavbars_edited_by', to=settings.AUTH_USER_MODEL, verbose_name=' تم التعديل  بواسطة ')),
                ('our_advantages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sectionpage.sectionpage', unique=True, verbose_name='الاقسام والصفحات')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Navbars_parent', to='navbarapp.navbars', verbose_name='القسم الاساسي')),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolioapp.portfolio', unique=True, verbose_name='معرض اعمال')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicesapp.services', unique=True, verbose_name='الخدمة')),
            ],
            options={
                'verbose_name': ' العنوان في رأس الصفحة',
                'verbose_name_plural': ' العنوان في رأس الصفحة',
                'db_table': '',
                'ordering': ['sort_no'],
                'managed': True,
            },
        ),
    ]
