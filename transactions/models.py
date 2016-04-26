from django.db import models
from inventory.models import Product
from tela.models import Facilitator

# Create your models here.

class Checkout(models.Model):
    facilitator = models.ForeignKey(Facilitator)
    checkout_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    check_in_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ('-checkout_date',)

    def __str__(self):
        return 'Checkout {}'.format(self.id)


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
