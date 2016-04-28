from django import forms
from inventory.models import Product

STATUS = (
    ('OK', 'OK'),
    ('Missing', 'Missing'),
    ('Damaged', 'Damaged'),
)


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=True, min_value=1, initial=1)
    status = forms.ChoiceField(choices=STATUS,)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
