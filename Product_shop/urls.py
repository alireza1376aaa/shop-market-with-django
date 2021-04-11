from django.conf.urls import url
from django.urls import path,include
from Product_shop.views import list_view_women, product_detail, search, \
    list_view_men,collect_product_types_men,collect_product_types_women,\
    collect_product_main_men,collect_product_main_women,collect_product_men,\
    collect_product_women,list_view_kids,collect_product_kids,collect_product_main_kids,collect_product_types_kids

app_name='product_shop'

urlpatterns = [

    #list view ------------------------------------------------------------
    path('list_view/women',list_view_women,name="list_view_women"),
    path('list_view/men', list_view_men, name="list_view_men"),
    path('list_view/kids', list_view_kids, name="list_view_kids"),

    # path('list_view-list-model',product_list_view_list_model.as_view(),name="list_view_list_model"),
    # path('list_view/collect/<category_name>',collect_product_page.as_view(),name="collect_product"),

    # details view ------------------------------------------------------------
    path('list_view/<product_Gender>/<slug>/<productId>', product_detail,name="details_view"),

    # search ------------------------------------------------------------
    path('list_view/search',search.as_view()),

    # collect ------------------------------------------------------------
    path('list_view/men_type/<category_name_type>', collect_product_types_men.as_view(), name="collect_men_type"),
    path('list_view/women_type/<category_name_type>', collect_product_types_women.as_view(), name="collect_women_type"),
    path('list_view/kids_type/<category_name_type>', collect_product_types_kids.as_view(), name="collect_kids_type"),

    path('list_view/men_main/<category_name_type>', collect_product_main_men.as_view(), name="collect_men_main"),
    path('list_view/women_main/<category_name_type>', collect_product_main_women.as_view(), name="collect_women_main"),
    path('list_view/kids_main/<category_name_type>', collect_product_main_kids.as_view(), name="collect_kids_main"),

    path('list_view/men/<category_name_type>', collect_product_men.as_view(), name="collect_men"),
    path('list_view/women/<category_name_type>', collect_product_women.as_view(), name="collect_women"),
    path('list_view/kids/<category_name_type>', collect_product_kids.as_view(), name="collect_kids"),

]
