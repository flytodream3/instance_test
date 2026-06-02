from django import forms
from django.forms import formset_factory

from .models import Product


class AssignShelfForm(forms.Form):
    product_name = forms.CharField(
        label='Product',
        widget=forms.TextInput(attrs={'list': 'product_list', 'autocomplete': 'off'}),
    )

    product_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)


AssignShelfFormSet = formset_factory(AssignShelfForm, extra=1, can_delete=True)
