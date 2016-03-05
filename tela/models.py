from django.db import models

class Venue(models.Model):
    address = models.CharField(max_length=300)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)

    def __str__(self):
        return self.address

    def coordinate(self):
        return "%s %s" %(self.longitude, self.latitude)
