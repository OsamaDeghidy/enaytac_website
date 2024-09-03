from django.db import models

# Create your models here.

from django.db import models

from django.core.validators import RegexValidator




class Person(models.Model):
    SPECIALITY_CHOICES = (
        ('1', 'العيادات الطبية لدى الشركات'),
        ('2', 'مرافقة الأطفال وكبار السن'),
        ('3', 'الأشعة المنزلية'),
        ('4', 'العلاج الطبيعي المنزلي'),
        ('5', 'زيارة طبيب في المنزل'),
        ('6', 'خدمات التمريض المنزلية'),
        ('7', 'جلسة غسيل الكلى المنزلي'),
        ('8', 'التحاليل الطبية المنزلية'),
    )
    speciality = models.CharField(max_length=1, choices=SPECIALITY_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,) #validators=[RegexValidator(r'^\d{9,15}$')]
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)

    def __str__(self):  
        return self.name






