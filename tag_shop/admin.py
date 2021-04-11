from django.contrib import admin
from tag_shop.models import tag_product

# Register your models here.
class filterxx(admin.ModelAdmin):
    list_display = ['__str__','product_active','slug']
    list_filter = ['product_active']
    search_fields = ['product_title']
    class meta:
        model=tag_product

admin.site.register(tag_product,filterxx)