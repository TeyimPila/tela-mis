from django.db import models


# Create your models here.

class Inventory(models.Model):
    CATEGORIES = (
        ('A', 'Very Important'),
        ('B', 'Fairly Important'),
        ('C', 'Important')
    )
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
        verbose_name_plural = "inventory"

    def __str__(self):
        return self.item

    def save(self, *args, **kwargs):
        if not self.at_hand and not self.ok and not self.damaged and not self.out:
            self.at_hand = self.purchased
            self.ok = self.purchased
            self.damaged = 0
            self.out = 0
        super(Inventory, self).save(*args, **kwargs)
