from django.contrib import admin
from Product_shop.models import product_shop, product_gallery


# Register your models here.

class filterxx(admin.ModelAdmin):
    list_display = ['__str__','product_count','product_active','product_date']
    list_filter = ['product_active']
    search_fields = ['product_name']
    class meta:
        model=product_shop

admin.site.register(product_shop,filterxx)
admin.site.register(product_gallery)
