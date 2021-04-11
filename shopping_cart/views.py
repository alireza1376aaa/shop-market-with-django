from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import order_form,finallyorder_form
from .models import order,order_ditails
from Product_shop.models import product_shop
from django.contrib.auth.models import User
from datetime import datetime
from .datetime import timedatePersian
# Create your views here.

@login_required(login_url='/Login')
def make_order(request):
    # card for details view
    order_forms=order_form(request.POST or None)
    if order_forms.is_valid():
        Order=order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if Order is None:
            Order=order.objects.create(owner_id=request.user.id,is_paid=False)
    Product_id=order_forms.cleaned_data.get("product_id")
    count=order_forms.cleaned_data.get("count")

    # card for small box
    product_cards_fild = request.POST.get('productid_small')
    product_cards_fild_count_main =request.POST.get('count_small')

    if product_cards_fild and product_cards_fild_count_main !=None:
        Order = order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if Order is None:
            Order = order.objects.create(owner_id=request.user.id, is_paid=False)
    if product_cards_fild_count_main!=None:
        product_cards_fild_count=int(product_cards_fild_count_main)

    if count!=None:
        if count<0:
            count=1



    product=product_shop.objects.get_by_id(product_id=Product_id or product_cards_fild)
    x=order_ditails.objects.filter(product_id=Product_id or product_cards_fild,order__owner_id=request.user.id)


    if x.exists():
        new_count=0
        count1=order_ditails.objects.filter(product_id=product.id,order__owner_id=request.user.id).first()
        xxc=count1.count
        new_count=xxc+(count or product_cards_fild_count)
        count1.count=new_count
        count1.save()

    else:
        if product.product_type == 'discount':

            Order.order_ditails_set.update_or_create(product_id=product.id, count=(count or product_cards_fild_count), price=product.discount())

        else:

            Order.order_ditails_set.create(product_id=product.id, count=(count or product_cards_fild_count), price=product.product_price)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='/Login')
def shopping_cart_page(request):


    contex={'order':None ,'orderDitails':None,'total':0,'totalwithtravel':0}
    Order=order.objects.filter(owner_id=request.user.id,is_paid=False).first()

    if Order is not None:
        contex['order']=Order
        contex['orderDitails']=Order.order_ditails_set.all()
        contex['total']=Order.get_total_price()
        contex['totalwithtravel'] = Order.get_total_price()+30000



    return render(request,'basket_page.html',contex)

@login_required(login_url='/Login')
def remove_order_detail(request,*args,**kwargs):
    detail_id=kwargs.get('detail_id')
    if detail_id is not None:
        Order_ditails=order_ditails.objects.get_queryset().get(id=detail_id,order__owner=request.user.id)
        if Order_ditails is not None:
            Order_ditails.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    raise Http404()

@login_required(login_url='/Login')
def shopping_cart_finally_page(request):

    user_id = request.user.id
    user = User.objects.get(id=user_id)
    form=finallyorder_form(request.POST or None,initial={'fullname':user.get_full_name(),'email':user.email})
    today=timedatePersian.today_date


    contex={'order':None ,'orderDitails':None,'total':0,'totalwithtravel':0,'form':form,'date':today}
    Order=order.objects.filter(owner_id=request.user.id,is_paid=False).first()

    if Order is not None:
        contex['order']=Order
        contex['orderDitails']=Order.order_ditails_set.all()
        contex['total']=Order.get_total_price()
        contex['totalwithtravel'] = Order.get_total_price()+30000

    if form.is_valid():
        form.save()

    return render(request,'finally_basket_page.html',contex)
