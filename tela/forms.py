from django.forms import ModelForm
from suit.widgets import HTML5Input, LinkedSelect


class BeneficiaryForm(ModelForm):
    class Meta:
        widgets = {
            # this defines the HTML5 input type for the beneficiary age attribute
            'age': HTML5Input(
                input_type='number',
                attrs={'min': '6', 'max': '17'}
            ),

        }
