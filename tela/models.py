from django.db import models
from django.utils import timezone

# Create your models here.


class Equipment(models.Model):

    # venue = models.ForeignKey(Venue, on_delete=models.CASCADE(), null=True, Blank=True)

    TYPE_CHOICES = (
        ('R', 'Radio'),
        ('T', 'Tablet'),
        ('M', 'Mat'),
        ('W', 'Workbook'),
    )

    STATUS_CHOICES = (
        ('O', 'OK'),
        ('M', 'Missing'),
        ('D', 'Damaged'),
    )

    AVAILABILITY_STATUS = (
        ('A', 'Available'),
        ('CO', 'Checked Out'),
    )

    serial_number = models.CharField(max_length=20, unique=True, null=False)
    equipment_type = models.CharField(max_length=15, choices=TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    checkin_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    availability = models.CharField(max_length=2, choices=AVAILABILITY_STATUS)

    def check_out(self, venue):
        if self.availability == self.AVAILABILITY_STATUS[1][0]:
            return "Equipment is already checked out"
        else:
            self.venue = venue
            self.availability = self.AVAILABILITY_STATUS[1][0]
            self.check_out_date = timezone.now()
            self.save()

    def check_in(self):
        """
        this method checks in an equipment when its being returned
        :return:
        """
        if self.availability == self.AVAILABILITY_STATUS[0][0]:
            return "This Equipment was not checked out"
        else:
            self.venue.venue_id = '0000'  # ie the equipment is in store
            self.availability = self.AVAILABILITY_STATUS[0][0]
            self.date_returned = timezone.now()
            self.save()

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name_plural = 'equipment'
