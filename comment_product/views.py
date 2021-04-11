from django.http import HttpResponseRedirect
from django.shortcuts import render

from Product_shop.models import product_shop
from comment_product.forms import commentform
from comment_product.models import comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/Login')
def comment_page(request):
    forms_comment = commentform(request.POST or None)




    if forms_comment.is_valid():
        Prouct = forms_comment.cleaned_data.get('id_comment')
        Fullname = forms_comment.cleaned_data.get('fullname')
        Subject = forms_comment.cleaned_data.get('subject')
        Email = forms_comment.cleaned_data.get('email')
        Massege = forms_comment.cleaned_data.get('massege')

        product = product_shop.objects.get_by_id(product_id=Prouct)

        comment.objects.create(fullname=Fullname, subject=Subject, email=Email, massege=Massege,product_id=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

