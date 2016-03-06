from django.db import models

# Create your models here.


class Neighborhood(models.Model):
    neigh_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
