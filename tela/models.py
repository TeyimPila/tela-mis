from django.db import models
from django.utils import timezone

import datetime

class Beneficiary(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    beneficiary_id = models.CharField(max_length=20)
    beneficiary_name = models.CharField(max_length=225)
    beneficiary_age = models.IntegerField
    is_in_school = models.BinaryField(default=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    year_of_birth = models.IntegerField
    age = models.IntegerField

    def set_age(self):
        year = timezone.now().year
        self.age=year-self.year_of_birth
        self.save()


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


    def __str__(self):
        return self.beneficiary_name

    class Meta:
        verbose_name_plural = 'Beneficiaries'