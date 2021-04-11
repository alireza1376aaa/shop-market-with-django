from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import login_form, register_form, forgetpass_form,forgetpass_form_edit
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
import uuid

def Log_in(request):

    if request.user.is_authenticated:
        return redirect('/')
    forms=login_form(request.POST or None)

    context = {"form": forms,'massage':None}

    pathurl=request.META.get('HTTP_REFERER')
    oldurl=pathurl.split('/')
    zz=len(oldurl)
    if oldurl[3]=='forget_pass':
        context['massage'] = 'ایمیل به شما با موفقیت ارسال شد'

    if len(oldurl)>4 :
        context['massage'] = 'کلمه عبور  شما با موفقیت تغیر پیدا کرد'

    if forms.is_valid():
        Username=forms.cleaned_data.get("username")
        Password=forms.cleaned_data.get("password")
        user=authenticate(request,username=Username,password=Password)


        if user is not None:
            login(request,user)

            context["form"]=forms

            if 'remember_me' in request.POST:
                x=request.session['username'] = Username
                y=request.session['password'] = Password
            else:
                return redirect('/')

            us = request.session.get('username')
            pas = request.session.get('password')
        else:
            forms.add_error("username","کاربری با این نام کاربری موجود نیست")



    return render(request, 'account/Log_in.html', context)

def Log_out(request):
    logout(request)

    return redirect("/Login")


def Register(request):

    forms_register = register_form(request.POST or None)
    context = {"register_form": forms_register}

    if forms_register.is_valid():
        UserName=forms_register.cleaned_data.get("username")
        First_name=forms_register.cleaned_data.get("first_name")
        Last_name=forms_register.cleaned_data.get("last_name")
        Email=forms_register.cleaned_data.get("email")
        Password=forms_register.cleaned_data.get("password")

        new_user=User.objects.create_user(username=UserName,email=Email,password=Password,first_name=First_name,last_name=Last_name)

        subject = 'خوش آمدید به فروشگاه لباس ما'
        message = f'سلام {new_user.first_name}, جان مرسی که در سایت ما ثبت نام کردی.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [new_user.email, ]
        send_mail(subject, message, email_from, recipient_list)


        return redirect("/Login")

    return render(request,"account/Register_page.html",context)

def Edit_user(request):
    user_id=request.user.id
    user=User.objects.get(id=user_id)

    if user is None:
        raise Http404("کاربری با این مشخصه یافت نشد")

    edit_user=register_form(request.POST or None ,initial={'username':user.username,'first_name':user.first_name,'last_name':user.first_name,'email':user.email})


    if edit_user.is_valid():
        username=edit_user.cleaned_data.get('username')
        first_name = edit_user.cleaned_data.get('first_name')
        last_name = edit_user.cleaned_data.get('last_name')
        email = edit_user.cleaned_data.get('email')


        user.username=username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

    contex={"edit_form":edit_user}

    return render(request,'account/edit_page.html',contex)

codepass = uuid.uuid1()

def forget_pass(request):

    my_form=forgetpass_form(request.POST or None)

    if my_form.is_valid():
        email_myform=my_form.cleaned_data.get('email')
        global emailaddres
        emailaddres = email_myform
        url_customer=f'http://127.0.0.1:8000{request.path_info}/{codepass}'
        subject = 'تغیر رمز عبور'

        message = url_customer

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_myform, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/Login')


    contex={'my_form':my_form}
    return render(request,'forgot_password/password_reset_email.html',contex)



def forget_pass_reset(request, *args, **kwargs):
    urlcode=kwargs['uuidcode']
    sourcecode = str(codepass)
    emails=emailaddres

    if urlcode != sourcecode:
        return Http404

    user = User.objects.get(email=emails)
    if user is None:
        raise Http404("کاربری با این مشخصه یافت نشد")

    passform=forgetpass_form_edit(request.POST or None)

    if passform.is_valid():
        password = passform.cleaned_data.get('password')
        newpass=make_password(password)
        user.password = newpass
        user.save()
        return redirect('/Login')

    contex = {"edit_form": passform}

    return render(request, 'forgot_password/reset_passs.html', contex)




