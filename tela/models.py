from django.db import models


# Create your models here.

class LocalGovArea(models.Model):
    """
    This model defines the database table for storing information about the Local Government Areas from which
    participants come
    """

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
