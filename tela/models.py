from django.db import models
from django.utils import timezone


class Beneficiary(models.Model):
    lga = models.ForeignKey(
        LocalGovArea,
        verbose_name="Local Government Area",
        on_delete=models.SET_NULL,
        null=True
    )

    center = models.ForeignKey(
        Center,
        on_delete=models.SET_NULL,
        null=True,
    )

    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.SET_NULL,
        null=True,
    )

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
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'beneficiaries'


class Venue(models.Model):
    """
    This model defines the database table that will hold information about tutorial venues
    """
    address = models.CharField(max_length=300)
    location_latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
    location_longitude = models.CharField('longitude', max_length=20, null=True, blank=True)

    def _get_coordinates(self):
        return "(%s,%s)" % (self.location_latitude, self.location_longitude)

    coordinate = property(_get_coordinates)

    def __str__(self):
        return "%s " % self.address


class Neighborhood(models.Model):
    """
    This model holds information about the neighborhood from which
    participants of the TELA project come from
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Equipment(models.Model):

    # equipment are handed over to facilitators, who then take the equipment to their various venues
    facilitator = models.ForeignKey(
        Facilitator,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

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

    AVAILABILITY_STATUS = (
        ('Available', 'Available'),
        ('Checked out', 'Checked Out'),
    )

    serial_num = models.CharField(max_length=20, unique=True, null=False)
    equipment_type = models.CharField(max_length=15, choices=TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    # the condition in which an equipment is returned from venues
    check_in_status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=True,
                                       blank=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    availability = models.CharField(max_length=12, choices=AVAILABILITY_STATUS)

    def check_out(self, facilitator):
        if self.availability == self.AVAILABILITY_STATUS[1][0]:
            return "Equipment is already checked out"
        else:
            self.facilitator = facilitator
            self.availability = self.AVAILABILITY_STATUS[1][0]
            self.check_out_date = timezone.now()
            self.save()

    def check_in(self):
        """
        this method checks in an equipment when its being returned
        :param facilitator:
        :return:
        """
        if self.availability == self.AVAILABILITY_STATUS[0][0]:
            return "This Equipment was not checked out"
        else:
            self.facilitator = None
            self.availability = self.AVAILABILITY_STATUS[0][0]
            self.date_returned = timezone.now()
            self.save()

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name_plural = 'equipment'
        unique_together = ('facilitator', 'serial_num')


class Tutor(models.Model):
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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=225)
    major = models.CharField(max_length=300)
    classification = models.CharField(max_length=2, choices=CLASSIFICATION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class LocalGovArea(models.Model):
    """
    This model defines the database table for storing information about the Local Government Areas from which
    participants come
    """
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


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
    group_size = models.IntegerField()

    def __str__(self):
        return self.title


class Facilitator(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Assessment(models.Model):
    beneficiary = models.ForeignKey(
        Beneficiary,
        on_delete=models.SET_NULL,
        null=True
    )
    # enumerator = models.ForeignKey(Enumerator, on_delete=models.CASCADE)

    ASSESSMENT_TYPES = (
        ('Pre-Assessment', 'Pre-assessment'),
        ('Post-Assessment', 'Post-Assessment'),
    )

    type = models.CharField(max_length=16, choices=ASSESSMENT_TYPES)

    def __str__(self):
        return '%s\'s %s' % (self.beneficiary, self.type)


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


class Enumerator(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
