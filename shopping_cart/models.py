from django.db import models
from django.contrib.auth.models import User
from Product_shop.models import product_shop
from datetime  import datetime

# Create your models here.


class order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id کاربر")
    product_date=models.DateTimeField(default=datetime.now(),verbose_name="تاریخ سفارش")
    is_paid=models.BooleanField(default=False,verbose_name=" سفارش پرداخت شده / نشده")

    def __str__(self):
        return self.owner.get_full_name()

    class Meta:
        verbose_name = 'صبد خرید'
        verbose_name_plural = 'صبدهای خرید'

    def get_total_price(self):
        amount=0
        for detail in self.order_ditails_set.all():
            amount+=detail.price*detail.count
        return amount

class manager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(product_id=product_id)

        return qs.first()


class order_ditails(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    product=models.ForeignKey(product_shop,on_delete=models.CASCADE)
    count=models.IntegerField()
    price=models.IntegerField()
    objects= manager()



    def __str__(self):
        return self.product.product_name


    def get_detail_sum(self):
        return self.count*self.price



    class Meta:
        verbose_name = ' جزئیات صبد خرید'
        verbose_name_plural = 'جزئیات صبدهای خرید'

class finally_order(models.Model):

    fullname=models.CharField(max_length=90,verbose_name="نام نام خانوادگی")
    email=models.EmailField(verbose_name="ایمیل ",null=True,blank=True)
    phone=models.CharField(max_length=90,verbose_name="تلفن ")
    address=models.TextField(verbose_name="ادرس ")
    post_code=models.CharField(max_length=90,verbose_name="کد پستی")
    city=models.CharField(max_length=90,verbose_name="شهر و استان")


    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'
