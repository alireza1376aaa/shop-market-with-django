from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class collect_product_main(models.Model):
    title_collect_product_main = models.CharField(max_length=80, verbose_name="عنوان دسته بندی")
    name_collect_product_main = models.CharField(max_length=80, verbose_name="نام دسته بندی در url")

    def __str__(self):
        return self.title_collect_product_main

    class Meta:
        verbose_name = 'دسته بندی کلی  محصول'
        verbose_name_plural = 'دسته بندی کلی محصولات'







class collect_product(models.Model):
    title_collect_product = models.CharField(max_length=80, verbose_name="عنوان دسته بندی")

    name_collect_product = models.CharField(max_length=80, verbose_name="نام دسته بندی در url")

    details_collect=models.ForeignKey(collect_product_main,on_delete=models.CASCADE)


    def __str__(self):
        return self.title_collect_product

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'


class collect_product_type(models.Model):
    title_collect_product_type = models.CharField(max_length=80, verbose_name="عنوان ")
    name_collect_product_type = models.CharField(max_length=80, verbose_name="نام عنوان در url")

    details_collect_type = models.ForeignKey(collect_product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_collect_product_type

    class Meta:
        verbose_name = 'نوع محصول'
        verbose_name_plural = 'عنوان محصولات'



