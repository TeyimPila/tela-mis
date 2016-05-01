from django.core.urlresolvers import reverse
from django.db import models
from tela.models import Facilitator


class Product(models.Model):
    CATEGORIES = (
        ('A', 'Very Important'),
        ('B', 'Fairly Important'),
        ('C', 'Important')
    )
    image = models.ImageField("Image", upload_to='products/%Y/%m/%d',
                              blank=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    purchased = models.PositiveIntegerField('Purchased')
    damaged = models.PositiveIntegerField(editable=False, null=True)
    ok = models.PositiveIntegerField('OK', editable=False, null=True)
    out = models.PositiveIntegerField(editable=False, null=True)
    at_hand = models.PositiveIntegerField(editable=False, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.at_hand and not self.ok and not self.damaged and not self.out:
            self.at_hand = self.purchased
            self.ok = self.purchased
            self.damaged = 0
            self.out = 0
        if self.purchased==0:
            self.available=False
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('inventory:product_detail',
                       args=[self.id, ])
