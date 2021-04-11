from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from favorite_prducts.forms import favorite_form
from .models import favorite
from Product_shop.models import product_shop
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/Login')
def make_favorite(request):

    favorite_forms=favorite_form(request.POST or None)

    product_favarit_fild = request.POST.get('salam')

    if favorite_forms.is_valid():

        Product_id=favorite_forms.cleaned_data.get("product_id")
        product=product_shop.objects.get_by_id(product_id=Product_id)


        x=favorite.objects.filter(product_id=Product_id,owner_id=request.user.id)

        if x.exists():
            pass
        else:

            favorite.objects.create(owner_id=request.user.id, product_id=product.id)
    else:
        product = product_shop.objects.get_by_id(product_id=product_favarit_fild)

        x = favorite.objects.filter(product_id=product_favarit_fild, owner_id=request.user.id)

        if x.exists():
            pass
        else:

            favorite.objects.create(owner_id=request.user.id, product_id=product.id)


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/Login')
def favorite_page(request):


    contex={'favoriteDitails':None}
    Favorite=favorite.objects.filter(owner_id=request.user.id)

    if Favorite is not None:
        contex['favoriteDitails']=Favorite

    return render(request,'favorite_page.html',contex)

@login_required(login_url='/Login')

def remove_favorite(request,*args,**kwargs):
    favorite_id=kwargs.get('favorite_id')
    if favorite_id is not None:
        favorite_ditails=favorite.objects.get_queryset().get(id=favorite_id,owner_id=request.user.id)
        if favorite_ditails is not None:
            favorite_ditails.delete()
            return redirect('/favorite')
    raise Http404()

