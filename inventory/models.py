from django.core.urlresolvers import reverse
from django.db import models
# from django.utils import timezone
from django.utils.safestring import mark_safe

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

    # def thumb(self):
    #     if self.image:
    #         return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.image.url,))
    #     else:
    #         return mark_safe(u'<img src="%s" width=60 height=60 />' % ("static/no_image.png",))


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
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('inventory:product_detail',
                       args=[self.id, ])

# class Transaction(models.Model):
#     item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     description = models.TextField()
#     checkout_date = models.DateField(default=timezone.now)
#     to = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField
