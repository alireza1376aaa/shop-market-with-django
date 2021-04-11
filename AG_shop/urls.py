"""AG_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from Product_shop.views import product_collect_men,product_collect_women,product_collect_kids
from .views import Home_Page,Navigation,Footer,Search,collect_women_nav,collect_men_nav





urlpatterns = [

    path('', Home_Page),
    path('', include("account_shop.urls",namespace='account')),
    path('', include("Product_shop.urls", namespace='product_shop')),
    path('', include("shopping_cart.urls", namespace='shopping_cart')),
    path('', include("sitesetting.urls", namespace='sitesetting')),
    path('', include("comment_product.urls", namespace='comment_product')),
    path('', include("favorite_prducts.urls", namespace='favorite_product')),
    url('collect_women_nav', collect_women_nav, name='women_nav'),
    url('collect_men_nav', collect_men_nav, name='men_nav'),

    path('admin/', admin.site.urls),
    url('partial-view-nav/1hhd23',Navigation,name='Navigation'),
    url(r'^partial-view-fotter/(?P<arg1>\w+)/(?P<arg2>\w+)/$', Footer, name='Footer'),
    url(r'^partial-view-search/(?P<arg1>\w+)/(?P<arg2>\w+)/$', Search, name='Search'),
    url('collect_men',product_collect_men, name='product_collect_men'),
    url('collect_women', product_collect_women, name='product_collect_women'),
    url('collect_kids', product_collect_kids, name='product_collect_kids'),

    #


    # # url(r'^collect_kids_sas', product_collect_kids, name='collect_kids'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
