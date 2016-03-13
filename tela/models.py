from django.db import models

# Create your models here.


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
