from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from inventory.models import Product
from tela.models import Facilitator
from django import  forms


# Create your models here.

class Checkout(models.Model):
    checkout_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    check_in_complete = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ('-checkout_date',)

    def __str__(self):
        return 'Checkout {}'.format(self.id)

    # content_type = models.ForeignKey(ContentType)
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={"model__in": ('Facilitator', 'Enumerator', 'Tutor')},
                                     verbose_name="Collected by")
    object_id = models.PositiveIntegerField(verbose_name='Individual')
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=300, editable=False, null=True)

    def save(self, *args, **kwargs):
        self.name = self.content_object.full_name
        super(Checkout, self).save(*args, **kwargs)


class CheckoutItem(models.Model):
    STATUS = (
        ('OK', 'OK'),
        ('Missing', 'Missing'),
        ('Damaged', 'Damaged'),
    )

    checkout = models.ForeignKey(Checkout, related_name='items')
    product = models.ForeignKey(Product, related_name='checked_out_items')
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, default=STATUS[0][0], choices=STATUS)

    def __str__(self):
        return '{}'.format(self.id)
