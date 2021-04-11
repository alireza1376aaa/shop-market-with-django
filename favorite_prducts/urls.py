from django.conf.urls import url
from django.urls import path,include
from favorite_prducts.views import  make_favorite,favorite_page,remove_favorite

app_name='favorite_product'

urlpatterns = [

    path('makefavorite',make_favorite,name="favorite"),
    path('favorite',favorite_page,name="favorite_page"),
    path('remove_favorite/<favorite_id>',remove_favorite,name='remove'),

]
