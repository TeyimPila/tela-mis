from django.db import models

class Venue(models.Model):
    address = models.CharField(max_length=300)
    location_latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
    location_longitude = models.CharField('latitude', max_length=20, null=True, blank=True)

    def __str__(self):
        return "%s " % self.address

    def get_coordinates(self):
        return "(%s,%s)" % (self.location_latitude, self.location_longitude)



