from django.conf.urls import url
from django.urls import path,include
from sitesetting.views import contact_us_page,privacy_page,rules_page

app_name='contact_us'

urlpatterns = [


    path('contact_us', contact_us_page, name="contact_us_form"),
    path('privacy_page', privacy_page, name="privacy_page"),
    path('rules_page', rules_page, name="rules_page"),


]
