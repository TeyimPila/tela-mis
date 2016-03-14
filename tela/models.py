from django.db import models
from django.utils import timezone


class Venue(models.Model):
    address = models.CharField(max_length=300)
    location_latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
    location_longitude = models.CharField('latitude', max_length=20, null=True, blank=True)

    def __str__(self):
        return "%s " % self.address

    def get_coordinates(self):
        return "(%s,%s)" % (self.location_latitude, self.location_longitude)



# Create your models here


class Neighborhood(models.Model):
    """
    This model holds information about the neighborhood from which
    participants of the TELA project come from
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    # facilitator = models.ForeignKey(Facilitator, on_delete=models.CASCADE, null=True, blank=True)

    TYPE_CHOICES = (
        ('Radio', 'Radio'),
        ('Tablet', 'Tablet'),
        ('Mat', 'Mat'),
        ('Workbook', 'Workbook'),
    )

    STATUS_CHOICES = (
        ('OK', 'OK'),
        ('Missing', 'Missing'),
        ('Damaged', 'Damaged'),
    )

    AVAILABILITY_STATUS = (
        ('Available', 'Available'),
        ('Checked out', 'Checked Out'),
    )

    serial_num = models.CharField(max_length=20, unique=True, null=False)
    equipment_type = models.CharField(max_length=15, choices=TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    # the condition in which an equipment is returned
    check_in_status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=True,
                                       blank=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    availability = models.CharField(max_length=12, choices=AVAILABILITY_STATUS)

    def check_out(self, facilitator):
        if self.availability == self.AVAILABILITY_STATUS[1][0]:
            return "Equipment is already checked out"
        else:
            self.facilitator = facilitator
            self.availability = self.AVAILABILITY_STATUS[1][0]
            self.check_out_date = timezone.now()
            self.save()

    def check_in(self, facilitator):
        """
        this method checks in an equipment when its being returned
        :param facilitator:
        :return:
        """
        if self.availability == self.AVAILABILITY_STATUS[0][0]:
            return "This Equipment was not checked out"
        else:
            self.entry_set.remove(facilitator)
            self.availability = self.AVAILABILITY_STATUS[0][0]
            self.date_returned = timezone.now()
            self.save()

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name_plural = 'equipment'
        unique_together = ('facilitator', 'serial_num')



class Tutor(models.Model):
    """this class stores the information of tutors,
    who are AUN students taking part in the tutoring"""

    # centers = models.ManyToManyField(Center)

    CLASSIFICATION_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )

    tutor_id = models.CharField(max_length=9)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    major = models.CharField(max_length=300)
    classification = models.CharField(max_length=2, choices=CLASSIFICATION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)



# Create your models here.

class LocalGovArea(models.Model):
    """
    This model defines the database table for storing information about the Local Government Areas from which
    participants come
    """

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
