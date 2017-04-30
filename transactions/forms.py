from django import forms
from .models import Checkout


class CheckoutCreateForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['content_type', 'object_id']
