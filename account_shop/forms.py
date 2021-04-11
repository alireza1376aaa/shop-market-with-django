from django import forms
from django.contrib.auth.models import User


class login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-1","placeholder":"نام کاربری"}),label="نام کاربری")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور"}),label="رمز عبور")


class register_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "نام کاربری خود را وارد کنید"}), label="نام کاربری")

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "نام  خود را وارد کنید"}), label="نام ")

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "نام خانوادگی خود را وارد کنید"}), label="نام خانوادگی")

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="ایمیل")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}), label="رمز عبور")

    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}), label="تکرار رمز عبور")


    def clean_username(self):

        UserNmae=self.cleaned_data.get('username')

        qu=User.objects.filter(username=UserNmae)

        if qu.exists():
            raise forms.ValidationError("کاربری با همچین مشخصه ای موجود است")
        return UserNmae

    def clean_password_again(self):
        pass1=self.cleaned_data.get('password')
        pass2=self.cleaned_data.get('password_again')

        if pass1 != pass2:
            raise forms.ValidationError("پسورد با هم تطابق ندارد")

    def clean_email(self):

        Email = self.cleaned_data.get('email')

        qu = User.objects.filter(email=Email)

        if qu.exists():
            raise forms.ValidationError("ایمیلی با همچین مشخصه ای موجود است")
        return Email

class forgetpass_form(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="ایمیل")
    def clean_email(self):

        Email = self.cleaned_data.get('email')

        qu = User.objects.filter(email=Email)

        if qu.exists()==False:
            raise forms.ValidationError("ایمیلی با همچین مشخصه ای ثبت نام نکرده است")
        return Email

class forgetpass_form_edit(forms.Form):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="رمز عبور")

    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="تکرار رمز عبور")

    def clean_password_again(self):
        pass1=self.cleaned_data.get('password')
        pass2=self.cleaned_data.get('password_again')

        if pass1 != pass2:
            raise forms.ValidationError("پسورد با هم تطابق ندارد")
