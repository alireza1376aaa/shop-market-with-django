from datetime  import datetime
from django.db import models
# from Women_shop.models import woman_product
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class tag_productManager(models.Manager):

    def get_product_active(self):
        return self.get_queryset().filter(product_active=True)

class tag_product(models.Model):

    product_title=models.CharField(max_length=20,verbose_name="نام تگ")
    product_date=models.DateTimeField(default=datetime.now(),verbose_name="تاریخ تگ")
    product_active=models.BooleanField(default=False,verbose_name="فعال / غیر فعال بودن تگ")
    slug=models.SlugField(blank=True,unique=True,verbose_name="اسلاگ")
    # tag_product= models.ManyToManyField(woman_product, verbose_name="تگ ها",null=True)
    objects=tag_productManager()




    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name='مدل تگ'
        verbose_name_plural='مدل های تگ'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=tag_product)
