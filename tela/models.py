from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Person(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(__str__)


class LocalGovArea(models.Model):
    """
    This model defines the database table for storing information about the Local Government Areas from which
    participants come
    """
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(max_length=300)
    lga = models.ForeignKey(
        LocalGovArea,
        verbose_name="Local Government Area",
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Venue(models.Model):
    """
    This model defines the database table that will hold information about tutorial venues
    """
    address = models.CharField(max_length=300)
    location_latitude = models.FloatField('Latitude', max_length=20, null=True, blank=True)
    location_longitude = models.FloatField('Longitude', max_length=20, null=True, blank=True)

    def _get_coordinates(self):
        return "(%s,%s)" % (self.location_latitude, self.location_longitude)

    coordinate = property(_get_coordinates)

    def __str__(self):
        return "%s " % self.address


class TutorialType(models.Model):
    """
    this model defines the type of tutorials that can possibly be carried out at any given center
    this model has a many to many field in the center model
    """
    TUTORIAL_TYPES = (
        ('Feed and Read', 'Feed and Read'),
        ('After School Tutorial', 'After School Tutorial'),
        ('Face to Face', 'Tutorial'),
        ('Radio Tutorial', 'Radio Tutorial'),
    )
    tutorial_type = models.CharField(max_length=50, choices=TUTORIAL_TYPES)

    def __str__(self):
        return self.tutorial_type


class Facilitator(Person):
    neighborhood = models.ForeignKey(
        Neighborhood,
        null= True,
        blank=True,
        on_delete=models.SET_NULL
    )
    account_number = models.CharField(blank=True, null=True, max_length=12)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Center(models.Model):
    venue = models.ForeignKey(
        Venue,
        null=True,
        on_delete=models.SET_NULL,
    )

    tutorial_types = models.ManyToManyField(
        TutorialType
    )

    facilitator = models.ForeignKey(
        Facilitator,
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(max_length=50)
    group_size = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Beneficiary(Person):
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.SET_NULL,
        null=True
    )

    center = models.ForeignKey(
        Center,
        on_delete=models.SET_NULL,
        null=True,
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    beneficiary_id = models.CharField(max_length=20)
    is_in_school = models.BooleanField(default=True, verbose_name='is in School?')
    age = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'beneficiaries'


class Equipment(models.Model):
    TYPE_CHOICES = (
        ('Radio', 'Radio'),
        ('Tablet', 'Tablet'),
        ('Mat', 'Mat'),
        ('Workbook', 'Workbook'),
    )

    STATUS_CHOICES = (
        ('OK', 'OK'),
        ('Missing', 'Missing'),
        ('Damaged', 'Damaged'),
    )

    serial_num = models.CharField(max_length=20, unique=True, null=False)
    equipment_type = models.CharField(max_length=15, choices=TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    is_available = models.BooleanField(default=True, )

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name_plural = 'equipment'


class Tutor(Person):
    """
    this class stores the information of tutors, who are AUN students taking part in the tutoring
    """

    CLASSIFICATION_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )

    tutor_id = models.CharField(max_length=9)
    major = models.CharField(max_length=300)
    classification = models.CharField(max_length=2, choices=CLASSIFICATION_CHOICES)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Assessment(models.Model):
    # enter the attributes of assessment here

    class Meta:
        abstract = True


class Enumerator(Person):
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.SET_NULL,
        null=True
    )

    account_number = models.CharField(blank=True, null=True, max_length=12)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class PreAssessment(Assessment):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, null=True)
    enumerator = models.ForeignKey(Enumerator, on_delete=models.CASCADE)


class PostAssessment(Assessment):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, null=True)
    enumerator = models.ForeignKey(Enumerator, on_delete=models.CASCADE)
