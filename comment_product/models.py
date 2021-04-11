from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from Product_shop.models import product_shop


class comment(models.Model):
    fullname = models.CharField(max_length=90, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل ")
    subject = models.CharField(max_length=90, verbose_name="موضوع")
    massege = models.TextField(verbose_name="پیغام")
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')
    product_id= models.ForeignKey(product_shop,on_delete=models.CASCADE)
    id_comment=models.IntegerField(blank=True,null=True)



    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = 'کامنت ها'