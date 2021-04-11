from django.db import models
from django.contrib.auth.models import User
from Product_shop.models import product_shop
from datetime  import datetime

# Create your models here.

class manager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(product_id=product_id)

        return qs.first()



class favorite(models.Model):

    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id کاربر")
    product_date=models.DateTimeField(default=datetime.now(),verbose_name="تاریخ ")
    product = models.ForeignKey(product_shop, on_delete=models.CASCADE)
    objects = manager()

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'محصول مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'

