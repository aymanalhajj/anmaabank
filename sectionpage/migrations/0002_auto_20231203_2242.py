# Generated by Django 3.2.22 on 2023-12-03 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sectionpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='is_hidden',
            field=models.BooleanField(default=False, help_text='سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي'),
        ),
        migrations.AlterField(
            model_name='sectionpageproperty',
            name='is_hidden',
            field=models.BooleanField(default=False, help_text='سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده', verbose_name='مخفي'),
        ),
        migrations.AlterField(
            model_name='sectionpageproperty',
            name='our_advantage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='our_dvantages_property', to='sectionpage.sectionpage', verbose_name='القسم'),
        ),
        migrations.AlterField(
            model_name='sectionpageproperty',
            name='sort_no',
            field=models.IntegerField(blank=True, help_text='اختياري - يتم ترتيب ظهور الأراء على حسب الرقم هذا ان وجد', null=True, verbose_name='رقم الترتيب '),
        ),
        migrations.AlterField(
            model_name='sectionpageproperty',
            name='titel',
            field=models.CharField(max_length=250, null=True, verbose_name='عنوان الغاية'),
        ),
    ]
