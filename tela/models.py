from django.db import models

class Center(models.Model):
    #venue = models.ForeignKey(Venue)
    title = models.CharField(max_length=50)
    group_size = models.IntegerField()

    def __str__(self):
        return self.title




