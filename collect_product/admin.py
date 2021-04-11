from django.contrib import admin
from collect_product.models import collect_product,collect_product_type,collect_product_main

# Register your models here.
admin.site.register(collect_product)
admin.site.register(collect_product_type)
admin.site.register(collect_product_main)
