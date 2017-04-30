import site

from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.db.models.fields.related import ManyToOneRel
from django.forms import ModelForm

from tela.models import Facilitator
from trash.widgets import ContentTypeSelect
from transactions.models import Checkout


class CheckoutForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        try:
            model = self.instance.content_type.model_class()
            model_key = model._meta.pk.name
        except:
            model = Facilitator
            model_key = 'id'
        self.fields['object_id'].widget = ForeignKeyRawIdWidget(rel=ManyToOneRel(model, model_key, field_name='id'), admin_site=site)
        self.fields['content_type'].widget.widget = ContentTypeSelect('lookup_id_object_id',
                                                                      self.fields['content_type'].widget.widget.attrs,
                                                                      self.fields['content_type'].widget.widget.choices)

    class Meta:
        model = Checkout
        fields = '__all__'
