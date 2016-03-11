from django.db import models

# Create your models here.
class Beneficiary(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


class Assessment (models.Model):

    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    # enumerator = models.ForeignKey(Enumerator, on_delete=models.CASCADE)

    ASSESSMENT_TYPES = (
        ('Pre-Assessment', 'Pre-assessment'),
        ('Post-Assessment', 'Post-Assessment'),
    )

    type = models.CharField(max_length=16, choices=ASSESSMENT_TYPES)

    def __str__(self):
        return '%s\'s %s' % (self.beneficiary, self.type)
