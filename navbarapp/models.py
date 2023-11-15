from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
from sectionpage.models import SectionPage as ouradv
from django.core.exceptions import ValidationError
from servicesapp.models import BankApplications,Services
from portfolioapp.models import Portfolio
# Create your models here.
# class Navbars(models.Model):
#     titel= models.CharField(
#         max_length=50, verbose_name="اسم القسم  "
#     )
#     dicript= models.CharField(
#         max_length=100, blank=True,null=True, verbose_name="جملة مختصرة معبرة تكتب تحت العنوان  "
#     )
#     # Date_Update = models.DateTimeField(
#     #     auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
#     # Date_Added = models.DateTimeField(
#     #     auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
#     is_hidden = models.BooleanField(
#         default=False,
#         help_text=" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده",
#         verbose_name="مخفي"
#         )
#     is_deleted = models.BooleanField(
#         default=False,
#         help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ", 
#         verbose_name="محذوف "
#         )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     sort_no = models.IntegerField(
#         null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
#     )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, verbose_name="تاريخ الأضافة"
#     )
#     Date_Update = models.DateTimeField(
#         auto_now=True, verbose_name="تاريخ التعديل"
#     )

#     created_by = models.ForeignKey(User, blank=True, editable=False,
#                                    null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

#     Date_Update = models.DateTimeField(
#         auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
#     deleted_at = models.DateTimeField(  null=True, 
#                                         blank=True, 
#                                         editable=False,
#                                         verbose_name="تاريخ الحذف "
#     )
#     deleted_by = models.ForeignKey(User, related_name='Navbars_deleted_by',
    
#                                         verbose_name=" تم الحذف  بواسطة ", 
#                                         editable=False, 
                                        
#                                    null=True, on_delete=models.SET_NULL,)
#     created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")
#     edited_at = models.DateTimeField(   null=True,  
#                                         editable=False,
#                                         blank=True, 
#                                         auto_now=True, 
#                                         verbose_name="تاريخ اخر تعديل "
#     )
#     edited_by = models.ForeignKey(  User, 
#                                     blank=True,
#                                     editable=False,
#                                     verbose_name=" تم التعديل  بواسطة ", 
#                                     related_name='Navbars_edited_by',
#                                     null=True, 
#                                     on_delete=models.SET_NULL,
#     )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     sort_no = models.IntegerField(
#         null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
#     )
#     short_note = models.CharField(
#         max_length=200,
#         null=True,
#         default=" ",
#         blank=True,
#         help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

#         verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

#     class Meta:
#         db_table = ""
#         managed = True
#         verbose_name = " العنوان الرئيسي في رأس الصفحة"
#         verbose_name_plural =" العنوان الرئيسي في رأس الصفحة"

#     def save(self, *args, **kwargs):
#         if self.sort_no is None:
#             self.sort_no = self.id
#         else:
#             self.sort_no = self.sort_no
#         super().save(*args, **kwargs)

#     def restore(self):
#         self.is_deleted = False
#         self.save()

#     def delete(self):
#         self.is_deleted = True
#         self.save()

#     # def hard_delete(self):
#     #     super(SoftDeleteModel, self).delete()

#     def soft_delete(self, deleter):
#         self.deleted_by = deleter
#         self.deleted_at = timezone.now()
#         self.is_deleted = True
#         self.save()

#     def __str__(self):
#         return self.titel

#     # class Meta:
#     #     managed = True
#     #     verbose_name = "اقسام معرض الأعمال  "
#     #     verbose_name_plural = "قسم معرض الأعمال"

# Create your models here.
class Navbars(models.Model):
    url = models.CharField("URL", max_length=100, db_index=True)
    titel= models.CharField(
        max_length=50,null=True,unique=True, verbose_name="العنوان"
    )

    dicript= models.CharField(
        max_length=100, blank=True,null=True, verbose_name="جملة مختصرة معبرة تكتب تحت العنوان  "
    )
    # display_at = models.BooleanField(
    #     default=False,
    #     # help_text=" سيتم اخفاء هذا  من العرض بالموقع بحال تم تحديده",
    #     verbose_name="عرضه على الشريط في راس الصفحة"
    # )
    display_at = models.CharField(
        max_length=100,
        choices=(
                ("navbar" , ' في الشريط اعلى الصفحات'),
                ("footer", ' اسفل الصفخات'),
                ("none", 'عدم عرضه في اي شريط ( منفصل برابط مخصص له)'),
            ),
        # default="الرئيسية",
        null=True,
        verbose_name="مكان عرض القسم",
        # blank=True
    )
    
    parent_section = models.CharField(
        max_length=100,
        choices=(
                ("1" , 'خدمات الأفراد'),
                ("2", 'خدمات المنظمات'),
                ("3", 'خدمات الشركات'),
                ("4", 'تطبيقات البنك'),

                ("5", 'التمويل الأصغر '),
                ("6", 'الاقسام'),
                # ("none", ''),
                # ("none", ''),
                # ("none", ''),
                # ("none", ''),
                # ("none", ''),
                # ("none", ''),
                # ("none", ''),

            ),
        # default="الرئيسية",
        null=True,
        verbose_name="مكان عرض القسم",
        # blank=True
    )
    parent = models.ForeignKey('self',related_name="Navbars_parent",null=True,on_delete=models.SET_NULL,blank=True, verbose_name="القسم الاساسي")
    column_navbar = models.ForeignKey("ColumnNavbars",blank=True,related_name="column_navbar_chield",
                                   null=True, on_delete=models.SET_NULL, verbose_name="العمود")
    # Locations = models.ManyToManyField(
    # parent = models.ForeignKey(Navbars, related_name='parent_secondary_navbar',
    
    #                           null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")
    our_advantages = models.ForeignKey(ouradv, blank=True,unique=True,
                                   null=True, on_delete=models.SET_NULL, verbose_name="الاقسام والصفحات")
    bank_application = models.ForeignKey(BankApplications, blank=True,unique=True,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تطبيقات البنك")
    service = models.ForeignKey(Services, blank=True,unique=True,
                                   null=True, on_delete=models.SET_NULL, verbose_name="الخدمة")
    portfolio = models.ForeignKey(Portfolio, blank=True,unique=True,
                                   null=True, on_delete=models.SET_NULL, verbose_name="معرض اعمال")
    # Portfolio 
    # dicript= models.CharField(
    # dicript= models.CharField(

    #     max_length=100, blank=True,null=True, verbose_name="جملة مختصرة معبرة تكتب تحت العنوان  "
    # )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده",
        verbose_name="مخفي"
        )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ", 
        verbose_name="محذوف "
        )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name="تاريخ التعديل"
    )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    deleted_at = models.DateTimeField(  null=True, 
                                        blank=True, 
                                        editable=False,
                                        verbose_name="تاريخ الحذف "
    )
    deleted_by = models.ForeignKey(User, related_name='SecondaryNavbars_deleted_by',
    
                                        verbose_name=" تم الحذف  بواسطة ", 
                                        editable=False, 
                                        
                                   null=True, on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")
    edited_at = models.DateTimeField(   null=True,  
                                        editable=False,
                                        blank=True, 
                                        auto_now=True, 
                                        verbose_name="تاريخ اخر تعديل "
    )
    edited_by = models.ForeignKey(  User, 
                                    blank=True,
                                    editable=False,
                                    verbose_name=" تم التعديل  بواسطة ", 
                                    related_name='SecondaryNavbars_edited_by',
                                    null=True, 
                                    on_delete=models.SET_NULL,
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )
    short_note = models.CharField(
        max_length=200,
        null=True,
        default=" ",
        blank=True,
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

        verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

    class Meta:
        db_table = ""
        managed = True
        verbose_name = " العنوان في رأس الصفحة"
        verbose_name_plural = " العنوان في رأس الصفحة"
        ordering = ['sort_no']

    def clean(self):
        """
        In here you can validate the two fields
        raise ValidationError if you see anything goes wrong. 
        for example if you want to make sure that field1 != field2
        """
        parent = self.parent
        our_advantages = self.our_advantages
        bank_application = self.bank_application
        service = self.service
        portfolio = self.portfolio
        # app_store = self.app_store
        # website_url = self.website
        # desketop_url = self.desketop
        errors={}
        parentchild = None
        if  bank_application  is not None and portfolio is not None :
                errors["bank_application"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.bank_application.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"
        if  bank_application  is not None and our_advantages is not None :
                errors["bank_application"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.bank_application.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"
        if  bank_application  is not None and service is not None :
                errors["bank_application"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.bank_application.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"
        if  our_advantages  is not None and service is not None :
                errors["our_advantages"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.our_advantages.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"
        if  our_advantages  is not None and portfolio is not None :
                errors["our_advantages"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.our_advantages.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"
        if  portfolio  is not None and service is not None :
                errors["portfolio"]= "هذا العنصر مرتبط بآكثر من قسم"+". "+str(self.portfolio.titel)+" "+"الرجاء اختيار عنصر صحيح غير مرتبط باي قسم اخر"

        if  parent  is not None :
            parentchild = Navbars.objects.filter(id=parent.pk)
            
            # if parentchild.count() > 1:
                # errors["parent"]= "الرجاء اختيار عنصر اساسي  صحيح غير مرتبط بعنصر اساسي اخر"
            for dataa in parentchild:
                if dataa.parent  is not None :
                    errors["parent"]= "هذا العنصر مرتبط بعنصر اساسي"+". "+str(dataa.parent.titel)+" "+"الرجاء اختيار عنصر اساسي  صحيح غير مرتبط بعنصر اخر"

                if dataa.our_advantages  is not None :
                    errors["our_advantages"]= "هذا العنصر مرتبط بقسم"+". "+str(dataa.our_advantages.titel)+" "+"الرجاء اختيار عنصر اساسي  صحيح غير مرتبط باي قسم اخر"
                if dataa.bank_application  is not None :
                    errors["bank_application"]= "هذا العنصر مرتبط بتطبيق"+". "+str(dataa.bank_application.titel)+" "+"الرجاء اختيار تطبيق  صحيح غير مرتبط باي قسم اخر"
                if dataa.service  is not None :
                    errors["service"]= "هذا العنصر مرتبط بخدمة"+". "+str(dataa.service.titel)+" "+"الرجاء اختيار عنصر   صحيح غير مرتبط باي قسم اخر"



        # if our_advantages  is not None and parent  is not None :
            # errors["our_advantages"]= "الرجاء اختيار قسم رابط التطبيق على Google Play"
            # if google_play is None or google_play is '':  
                # errors["google_play"]= "الرجاء ادخال رابط التطبيق على Google Play"
            # if app_store is None or app_store is '':
                # errors["app_store"]= "الرجاء ادخال رابط التطبيق على app Store"
        # elif type_choice == website:
           
            # if app_store is None or app_store is '':
            #     errors["app_store"]= "الرجاء ادخال رابط التطبيق على app Store"
        # return self.cleaned_data
        if errors:
            raise ValidationError(errors)
    def save(self, *args, **kwargs):
        if self.sort_no is None:
            self.sort_no = self.id
        else:
            self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()

    # def hard_delete(self):
    #     super(SoftDeleteModel, self).delete()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.titel

    # class Meta:
    #     managed = True
    #     verbose_name = "اقسام معرض الأعمال  "
    #     verbose_name_plural = "قسم معرض الأعمال"

class ColumnNavbars(models.Model):
    
    titel= models.CharField(
        null=True,unique=True,
        max_length=50,  verbose_name=" اسم القسم  "
    )
    # parent = models.ForeignKey(SecondaryNavbars, related_name='Row_secondary_navbar',
    #                                null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")

    # dicript= models.CharField(
    #     max_length=100, blank=True,null=True, verbose_name="جملة مختصرة معبرة تكتب تحت العنوان  "
    # )
    # Date_Update = models.DateTimeField(
    #     auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    # Date_Added = models.DateTimeField(
    #     auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    is_hidden = models.BooleanField(
        default=False,
        help_text=" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده",
        verbose_name="مخفي"
        )
    is_deleted = models.BooleanField(
        default=False,
        help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ", 
        verbose_name="محذوف "
        )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    Date_Added = models.DateTimeField(
        auto_now_add=True, verbose_name="تاريخ الأضافة"
    )
    Date_Update = models.DateTimeField(
        auto_now=True, verbose_name="تاريخ التعديل"
    )

    created_by = models.ForeignKey(User, blank=True, editable=False,
                                   null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

    Date_Update = models.DateTimeField(
        auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
    Date_Added = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
    deleted_at = models.DateTimeField(  null=True, 
                                        blank=True, 
                                        editable=False,
                                        verbose_name="تاريخ الحذف "
    )
    deleted_by = models.ForeignKey(User, related_name='RowNavbars_deleted_by',
    
                                        verbose_name=" تم الحذف  بواسطة ", 
                                        editable=False, 
                                        
                                   null=True, on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")
    edited_at = models.DateTimeField(   null=True,  
                                        editable=False,
                                        blank=True, 
                                        auto_now=True, 
                                        verbose_name="تاريخ اخر تعديل "
    )
    edited_by = models.ForeignKey(  User, 
                                    blank=True,
                                    editable=False,
                                    verbose_name=" تم التعديل  بواسطة ", 
                                    related_name='RowNavbars_edited_by',
                                    null=True, 
                                    on_delete=models.SET_NULL,
    )
    # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
    # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
    sort_no = models.IntegerField(
        null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
    )
    short_note = models.CharField(
        max_length=200,
        null=True,
        default=" ",
        blank=True,
        help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

        verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

    class Meta:
        db_table = ""
        managed = True
        verbose_name = " العنوان الثنوي في رأس الصفحة"
        verbose_name_plural =" العنوان الثنوي في رأس الصفحة"
        ordering = ['sort_no']

    def save(self, *args, **kwargs):
        if self.sort_no is None:
            self.sort_no = self.id
        else:
            self.sort_no = self.sort_no
        super().save(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()

    # def hard_delete(self):
    #     super(SoftDeleteModel, self).delete()

    def soft_delete(self, deleter):
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.titel

    # class Meta:
    #     managed = True
    #     verbose_name = "اقسام معرض الأعمال  "
    #     verbose_name_plural = "قسم معرض الأعمال"

# class SyntexNavbars(models.Model):
    
#     titel= models.CharField(
#         max_length=50, verbose_name=" اسم القسم  "
#     )
#     parent = models.ForeignKey(Navbars, related_name='syntex_navbars',
#                                    null=True, on_delete=models.SET_NULL, verbose_name="القسم الاساسي")

#     # dicript= models.CharField(
#     #     max_length=100, blank=True,null=True, verbose_name="جملة مختصرة معبرة تكتب تحت العنوان  "
#     # )
#     # Date_Update = models.DateTimeField(
#     #     auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
#     # Date_Added = models.DateTimeField(
#     #     auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
#     is_hidden = models.BooleanField(
#         default=False,
#         help_text=" سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده",
#         verbose_name="مخفي"
#         )
#     is_deleted = models.BooleanField(
#         default=False,
#         help_text="سيتم اخفاء هذا من العرض بالموقع بحال تم تحديده وسيعتبر انه قد تم حذفه  ", 
#         verbose_name="محذوف "
#         )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     sort_no = models.IntegerField(
#         null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
#     )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, verbose_name="تاريخ الأضافة"
#     )
#     Date_Update = models.DateTimeField(
#         auto_now=True, verbose_name="تاريخ التعديل"
#     )

#     created_by = models.ForeignKey(User, blank=True, editable=False,
#                                    null=True, on_delete=models.SET_NULL, verbose_name="تم الأنشاء بواسطة ")

#     Date_Update = models.DateTimeField(
#         auto_now=True, blank=True, verbose_name="تاريخ التعديل ")
#     Date_Added = models.DateTimeField(
#         auto_now_add=True, blank=True, verbose_name="تاريخ الأضافة ")
#     deleted_at = models.DateTimeField(  null=True, 
#                                         blank=True, 
#                                         editable=False,
#                                         verbose_name="تاريخ الحذف "
#     )
#     deleted_by = models.ForeignKey(User, related_name='SyntexNavbars_deleted_by',
    
#                                         verbose_name=" تم الحذف  بواسطة ", 
#                                         editable=False, 
                                        
#                                    null=True, on_delete=models.SET_NULL,)
#     created_at = models.DateTimeField(null=True,    auto_now_add=True, editable=False,blank=True, verbose_name="تاريخ الأنشاء ")
#     edited_at = models.DateTimeField(   null=True,  
#                                         editable=False,
#                                         blank=True, 
#                                         auto_now=True, 
#                                         verbose_name="تاريخ اخر تعديل "
#     )
#     edited_by = models.ForeignKey(  User, 
#                                     blank=True,
#                                     editable=False,
#                                     verbose_name=" تم التعديل  بواسطة ", 
#                                     related_name='SyntexNavbars_edited_by',
#                                     null=True, 
#                                     on_delete=models.SET_NULL,
#     )
#     # is_hidden = models.BooleanField(default=False, verbose_name="مخفي")
#     # is_deleted = models.BooleanField(default=False, verbose_name="محذوف")
#     sort_no = models.IntegerField(
#         null=True, editable=True, blank=True, verbose_name="رقم الترتيب (يرتب بالموقع حسب الرقم)"
#     )
#     short_note = models.CharField(
#         max_length=200,
#         null=True,
#         default=" ",
#         blank=True,
#         help_text=" اختياري - فقط لأجل ان وجد لديكم اي ملاحظة للعمل عليها مستقبلاً",

#         verbose_name="ملاحظة قصيرة إن وجد (مخفي لاتعرض بالموقع)")

#     class Meta:
#         db_table = ""
#         managed = True
#         verbose_name = " العنوان الثنوي في رأس الصفحة"
#         verbose_name_plural =" العنوان الثنوي في رأس الصفحة"

#     def save(self, *args, **kwargs):
#         if self.sort_no is None:
#             self.sort_no = self.id
#         else:
#             self.sort_no = self.sort_no
#         super().save(*args, **kwargs)

#     def restore(self):
#         self.is_deleted = False
#         self.save()

#     def delete(self):
#         self.is_deleted = True
#         self.save()

#     # def hard_delete(self):
#     #     super(SoftDeleteModel, self).delete()

#     def soft_delete(self, deleter):
#         self.deleted_by = deleter
#         self.deleted_at = timezone.now()
#         self.is_deleted = True
#         self.save()

#     def __str__(self):
#         return self.titel

#     # class Meta:
#     #     managed = True
#     #     verbose_name = "اقسام معرض الأعمال  "
#     #     verbose_name_plural = "قسم معرض الأعمال"
