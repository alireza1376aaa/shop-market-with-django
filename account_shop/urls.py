
from django.urls import path,include
from account_shop.views import Log_in,Log_out,Register,Edit_user,forget_pass,forget_pass_reset
from django.contrib.auth import views as auth_views
app_name="account"



urlpatterns = [

    path('Login',Log_in ,name='login'),
    path('Logout',Log_out,name='loginout'),
    path('Register',Register,name='register'),
    path('Edit', Edit_user, name='Edit'),
    path('forget_pass',forget_pass,name='password_reset'),
    path('forget_pass/<uuidcode>',forget_pass_reset,name='forget_reet'),


]
