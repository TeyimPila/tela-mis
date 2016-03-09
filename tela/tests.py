from django.test import TestCase
from .models import Tutor


# Create your tests here.


class TestTutor(TestCase):
    """
    this tests properties of the Tutor Model
    """

    def setUp(self):
        Tutor.objects.create(tutor_id="A00012345", first_name="Tutor Fname", last_name="Tutor last name",
                             email="tutor.email@example.com", major="Tutor's major", classification="FR")

    def test_tutor_creation(self):
        tutor = Tutor.objects.get(first_name="Tutor Fname", last_name="Tutor last name")
        self.assertTrue(isinstance(tutor, Tutor))
        self.assertEqual(tutor.__str__(), "%s %s" % (tutor.first_name, tutor.last_name))
