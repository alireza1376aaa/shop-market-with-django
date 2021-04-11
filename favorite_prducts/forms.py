from django import forms
from shopping_cart.models import finally_order


class favorite_form(forms.Form):

    product_id=(forms.IntegerField(widget=forms.HiddenInput()))


