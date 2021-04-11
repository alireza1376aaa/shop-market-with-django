from django.shortcuts import redirect,render
import itertools
from Product_shop.models import product_shop
from account_shop.forms import login_form
from account_shop.views import Log_in
from django.contrib.auth.models import User

from collect_product.models import collect_product_main, collect_product, collect_product_type
from sitesetting.models import sitesetting
from slider.models import slider,collection
from shopping_cart.models import order
from AG_shop.form import khabarname_form
from django.conf import settings
from django.core.mail import send_mail



def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def Navigation(request, *args, **kwargs):


    sitesettings = sitesetting.objects.first()

    context = {'order': None,
               'orderDitails': None,
               'total': 0,
               'totalwithtravel': 0,
               'name':None,
               "site": sitesettings,

               }

    Order = order.objects.filter(owner_id=request.user.id, is_paid=False).first()


    if Order is not None:
        context['order'] = Order
        context['orderDitails'] = Order.order_ditails_set.all()
        context['total'] = Order.get_total_price()
        context['totalwithtravel'] = Order.get_total_price() + 30000


    if request.user.is_authenticated:
        name=request.user.first_name
        context['name']=name

        if Order is not None:
            lentotalwithtravel = len(Order.order_ditails_set.all())
            context['len']=lentotalwithtravel

    else:
        context={}

    return render(request, 'Main_template/Navigation.html',context)


def Footer(request, *args, **kwargs):
    forms_khabarname = khabarname_form(request.POST or None)

    if forms_khabarname.is_valid():
        Email = forms_khabarname.cleaned_data.get("email_khabar")
        subject = 'خوش آمدید به خبرنامه ما'
        if request.user.is_authenticated:
            name = request.user.first_name
            message = f'سلام {name}, جان مرسی که در خبرنامه ما سایت ما ثبت نام کردی.'
        else:
            message = f'سلام کاربر گرامی مرسی که در خبرنامه سایت ما ثبت نام کردی.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [Email, ]
        send_mail(subject, message, email_from, recipient_list)

    sitesettings = sitesetting.objects.first()
    result = kwargs['arg1'] + kwargs['arg2']
    kwargs['result'] = result
    kwargs['site']=sitesettings
    kwargs['register_form']=forms_khabarname
    return render(request, 'Main_template/Footer.html',kwargs)


def Search(request, *args, **kwargs):
    result = kwargs['arg1'] + kwargs['arg2']
    kwargs['result'] = result
    return render(request, 'Main_template/__search_templates.html', kwargs)



def Home_Page(request, *args, **kwargs):

    sliders = slider.objects.all()
    collections = collection.objects.first()

    Special_product=product_shop.objects.filter(product_type='discount').order_by('-price_discount').all()[:6]

    new_product = product_shop.objects.order_by('-product_date').all()

    views_product = product_shop.objects.order_by('-product_visit').all()

    contex={'sliders':sliders,
            'collection_slider':collections,
            'Special':Special_product,
            'new_product':new_product,
            'views':views_product
            }

    return render(request, 'Home_page.html', contex)


def khabarname(request):

    forms_khabarname =login_form(request.POST or None)
    context = {"register_form": forms_khabarname}


    if forms_khabarname.is_valid():
        Email=forms_khabarname.cleaned_data.get("email")
        subject = 'خوش آمدید به خبرنامه ما'
        message = f'سلام {request.user.first_name}, جان مرسی که در سایت ما ثبت نام کردی.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [Email, ]
        send_mail(subject, message, email_from, recipient_list)

    return render(request, 'Main_template/Footer.html',context)

def collect_men_nav(request,**kwargs):

    collect_main=collect_product_main.objects.filter(product_shop__product_Gender__iexact='men').distinct()
    collect=collect_product.objects.filter(product_shop__product_Gender__iexact='men').distinct()

    contex={"collect":collect,'collect_main':collect_main}

    return render(request,'navigation/nav_men.html' , contex)

def collect_women_nav(request,**kwargs):
    collect_type=collect_product_type.objects.filter(product_shop__product_Gender__iexact='women').distinct()
    collect_main = collect_product_main.objects.filter(product_shop__product_Gender__iexact='women').distinct()
    collect = collect_product.objects.filter(product_shop__product_Gender__iexact='women').distinct()

    contex = {"collect": collect, 'collect_main': collect_main}

    return render(request, 'navigation/nav_women.html', contex)

def product_collect_kids(request,**kwargs):
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='kids').distinct()
    collect_main = collect_product_main.objects.filter(product_shop__product_Gender__iexact='kids').distinct()
    collect = collect_product.objects.filter(product_shop__product_Gender__iexact='kids').distinct()

    contex = {"collect": collect, 'collect_type': collect_type, 'collect_main': collect_main}

    return render(request, 'products/collect/collect_partial_kids.html', contex)