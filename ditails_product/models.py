from django.db import models

# Create your models here.


class size(models.Model):
    product_size=models.CharField(max_length=50,verbose_name="سایز محصول")
    product_unit=models.CharField(max_length=50,verbose_name="واحد سایز")

    def __str__(self):
        return self.product_size

    class Meta:
        verbose_name = 'سایز محصول'
        verbose_name_plural = 'سایز محصولات'

class color(models.Model):
    product_color=models.CharField(max_length=50,verbose_name="رنگ محصول")
    product_color_english=models.CharField(max_length=50,verbose_name="رنگ محصول به انگلیسی",null=True,blank=True)

    def __str__(self):
        return self.product_color

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ محصولات'

class brand(models.Model):
    product_brand=models.CharField(max_length=50,verbose_name="برند محصول")

    def __str__(self):
        return self.product_brand

    class Meta:
        verbose_name = 'برند محصول'
        verbose_name_plural = 'برند محصولات'

