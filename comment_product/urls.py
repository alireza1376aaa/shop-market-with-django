from django.conf.urls import url
from django.urls import path,include
from comment_product.views import comment_page

app_name='comment_product'

urlpatterns = [

    path('comment',comment_page,name="commentform"),

]
