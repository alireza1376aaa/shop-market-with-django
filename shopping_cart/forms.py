from django import forms
from shopping_cart.models import finally_order


class order_form(forms.Form):
    product_id=(forms.IntegerField(widget=forms.HiddenInput()))
    count=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input-text qty','id':'qty1'}),initial=1)


class finallyorder_form(forms.ModelForm):
   class Meta:
      model=finally_order
      fields=['fullname','email','phone','address','post_code','city']
      widgets={

         'fullname':forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}),
          'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
          'phone':forms.TextInput(attrs={'placeholder':'تلفن '}),
         'address': forms.TextInput(attrs={'placeholder': 'آدرس'}),
         'post_code': forms.TextInput(attrs={'placeholder': 'کد پستی'}),
         'city': forms.TextInput(attrs={'placeholder': 'شهر و استان'}),

      }