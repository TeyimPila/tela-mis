from django.db import models
from django.utils import timezone

# Create your models here.

class Equipment(models.Model):
    # venue = models.ForeignKey(Venue, on_delete=models.CASCADE(), null=True, Blank=True)

    TYPE_CHOICES=(
        ('R', 'Radio'),
        ('T', 'Tablet'),
        ('M', 'Mat'),
        ('W', 'Workbook'),
    )

    STATUS_CHOICES=(
        ('O', 'OK'),
        ('M', 'Missing'),
        ('D', 'Damaged'),
    )

    serial_number = models.CharField(max_length=20, unique=True, null=False)
    equipment_type = models.CharField(max_length=15, choices=TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    given_out = models.BooleanField(default=False)

    def check_out(self):
        if self.given_out==True:
            return "Tablet is already checked out"
        else:
            self.check_out_date = timezone.now()
            self.save()

    def check_in(self):
        self.date_returned = timezone.now()
        self.save()

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name_plural='equipment'