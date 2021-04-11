from django.forms import ModelForm
from django import forms
from comment_product.models import comment


class commentform(ModelForm):


   class Meta:
      model=comment
      fields=['fullname','subject','email','massege','id_comment']
      widgets={

         'fullname':forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}),
         'subject':forms.TextInput(attrs={'placeholder':'موضوع'}),
         'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
         'massege': forms.Textarea(attrs={'placeholder': 'پیغام'}),
         'id_comment':forms.NumberInput(attrs={'type':'hidden'}),

      }