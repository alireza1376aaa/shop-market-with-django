from django.conf.urls import url
from django.urls import path,include
from shopping_cart.views import  make_order,shopping_cart_page,remove_order_detail,shopping_cart_finally_page

app_name='shopping_cart'

urlpatterns = [

    path('makecarts',make_order,name="basket"),
    path('carts',shopping_cart_page,name="carts"),
    path('remove_order/<detail_id>',remove_order_detail,name='remove'),
    path('finallt_carts', shopping_cart_finally_page, name="finallt_carts"),

]
