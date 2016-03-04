from django.db import models
from django.utils import timezone

import datetime

class Beneficiary(models.Model):
    # lga = models.ForeignKey(
    #     LGA,
    #     on_delete=models.CASCADE,
    #     verbose_name="Local Government Area",
    # )
    #
    # center = models.ForeignKey(
    #     Center,
    #     on_delete=models.CASCADE,
    #     verbose_name="related center",
    # )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    beneficiary_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    is_in_school = models.BooleanField(default=True, verbose_name='is in School?')
    gender = models.CharField(max_length=1, choices=GENDER)
    year_of_birth = models.IntegerField('year of birth', default=timezone.now().year)

    def _get_age(self):
        year = timezone.now().year
        return year - self.year_of_birth

    beneficiary_age = property(_get_age)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'beneficiaries'


class 