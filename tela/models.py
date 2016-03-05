from django.db import models

class Fascilitator(models.Model):
    #center = models.ForeignKey(Center)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)



