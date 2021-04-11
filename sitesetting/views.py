from django.shortcuts import render, redirect
from sitesetting.models import sitesetting,contact_us,privacy,rules
from sitesetting.forms import creatform
# Create your views here.


def contact_us_page(request):

    forms = creatform(request.POST or None)
    sitesettings=sitesetting.objects.first()
    context = {"form": forms, "object": sitesettings,'massage':''}

    if forms.is_valid():
        Fullname=forms.cleaned_data.get('fullname')
        Subject = forms.cleaned_data.get('subject')
        Email = forms.cleaned_data.get('email')
        Massege = forms.cleaned_data.get('massege')

        contact_us.objects.create(fullname=Fullname,subject=Subject,email=Email,massege=Massege)
        context['massage']='پیام شما با موفقیت ارسال شد'
        forms=creatform()


    return render(request, "contact_us.html", context)

def privacy_page(request):
    privacy_mypage=privacy.objects.first()
    return render(request,'Privacy.html',{'privacy':privacy_mypage})


def rules_page(request):
    rules_mypage=rules.objects.first()
    return render(request,'rules.html',{'rules':rules_mypage})