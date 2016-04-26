from django.db import models
from django.utils import timezone
from tela.models import Facilitator


class Product(models.Model):
    CATEGORIES = (
        ('A', 'Very Important'),
        ('B', 'Fairly Important'),
        ('C', 'Important')
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    item = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    purchased = models.PositiveIntegerField('Quantity Purchased')
    damaged = models.PositiveIntegerField(editable=False, null=True)
    ok = models.PositiveIntegerField('OK', editable=False, null=True)
    out = models.PositiveIntegerField(editable=False, null=True)
    at_hand = models.PositiveIntegerField(editable=False, null=True)
    still_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.item

    def save(self, *args, **kwargs):
        if not self.at_hand and not self.ok and not self.damaged and not self.out:
            self.at_hand = self.purchased
            self.ok = self.purchased
            self.damaged = 0
            self.out = 0
        super(Product, self).save(*args, **kwargs)

# class Transaction(models.Model):
#     item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     description = models.TextField()
#     checkout_date = models.DateField(default=timezone.now)
#     to = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField
