from colorfield.fields import ColorField
from django.db import models
from datetime  import datetime
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import Q
from tag_shop.models import tag_product
from ditails_product.models import size,color,brand
from collect_product.models import collect_product_type, collect_product_main,collect_product
from taggit.managers import TaggableManager

# Create your models here.


# class collect_product(models.Model):
#     title = models.CharField(max_length=80, verbose_name="عنوان دسته بندی")
#
#     name = models.CharField(max_length=80, verbose_name="نام دسته بندی در url")
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'دسته بندی محصول'
#         verbose_name_plural = 'دسته بندی محصولات'



class productManager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_product_active(self):
        return self.get_queryset().filter(product_active=True)



    def search(self,query):
        lookup=Q (product_name__icontains=query)| Q (tag_products__product_title__icontains=query)

        return self.get_queryset().filter(lookup,product_active=True).distinct()


    def get_product_category_type(self,category_name_type,gender):
        return self.get_queryset().filter(xxxxxxxxx__name_collect_product_type__iexact=category_name_type,product_Gender__iexact=gender)

    def get_product_category_main(self,category_name_main,gender):
        return self.get_queryset().filter(main_collect__name_collect_product_main__iexact=category_name_main,product_Gender__iexact=gender)

    def get_product_category(self,category_name,gender):
        return self.get_queryset().filter(collect__name_collect_product__iexact=category_name,product_Gender__iexact=gender)



class product_shop(models.Model):

    Gender_choices = (('women', 'زنانه'), ('men', 'مردانه'), ('kids', 'بجه گانه'))
    product_Gender = models.CharField(max_length=10, choices=Gender_choices, default="S", verbose_name="محصول مربوط با ")
    product_name = models.CharField(max_length=80,verbose_name="نام محصول")
    product_description = models.TextField(null=True,verbose_name="توضیحات محصول")
    product_price = models.DecimalField(max_digits=20,decimal_places=0,default=0.0,verbose_name="قیمت محصول")
    product_count = models.IntegerField(default=0,verbose_name="تعداد محصول")
    product_brand = models.ForeignKey(brand,verbose_name="برند محصول",on_delete=models.CASCADE)
    product_color = models.ManyToManyField(color, verbose_name="رنگ محصول")
    product_color1 = ColorField(verbose_name="رنگ خاص محصول",blank=True,null=True)
    product_size = models.ManyToManyField(size, verbose_name="سایز محصول")
    type_choices=(('simple','ساده'),('discount','تخفیف'),('new','جدبد'))
    product_type=models.CharField(max_length=10,choices=type_choices,default="S",verbose_name="مدل محصول")
    price_discount = models.IntegerField(default=0, verbose_name="درصد تخفیف محصول")
    product_image=models.ImageField(upload_to="product_shop",null=True,blank=True,default='defult.jpg',verbose_name="عکس محصول")
    product_date=models.DateTimeField(default=datetime.now(),verbose_name="تاریخ محصول")
    tag_products = models.ManyToManyField(tag_product,verbose_name="تگ ها")
    # collect_products = models.ManyToManyField(collect_product,verbose_name="دسته بندی",null=True,blank=True)
    product_visit = models.IntegerField(default=0,verbose_name="تعداد بازدید محصول",editable=False)
    product_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال بودن محصول")
    slug = models.SlugField(blank=True, unique=True, verbose_name="اسلاگ")
    main_collect = models.ForeignKey(collect_product_main, verbose_name="محصول",on_delete=models.CASCADE)
    collect = models.ForeignKey(collect_product, verbose_name="محصول",on_delete=models.CASCADE)
    xxxxxxxxx = models.ForeignKey(collect_product_type, verbose_name="گ محصول",on_delete=models.CASCADE)
    tags = TaggableManager()




    objects=productManager()

    def get_gender(self):
        return f"/list_view/{self.product_Gender}"

    def get_absolute_url(self):
        return f"/list_view/{self.product_Gender}/{self.slug}/{self.id}"


    def discount(self):
        if self.price_discount==0:
            return self.product_price
        percent=float( self.price_discount/100)*float(self.product_price)
        price=float(self.product_price)- percent
        return int(price)


    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name='فروشگاه محصول'
        verbose_name_plural='فروشگاه محصولات '



class product_gallery(models.Model):

    title = models.CharField(max_length=80, verbose_name="عنوان محصول")
    image = models.ImageField(upload_to="product_shop/product_gallery", null=True, blank=True, default='defult.jpg',
                                      verbose_name="عکس های محصول")
    product=models.ForeignKey(product_shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری عکس'
        verbose_name_plural = 'گالری عکس ها'







def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=product_shop)
