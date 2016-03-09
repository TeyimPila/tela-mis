from django.test import TestCase
from .models import LocalGovArea

# Create your tests here.


class TestLGA(TestCase):

    def setUp(self):
        LocalGovArea.objects.create(name="The local Government Area")

    def test_LGA_creation(self):
        """
        this tests that each object of the LocalGovArea model is created properly
        :return:
        """
        lga = LocalGovArea.objects.get(name="The local Government Area")
        self.assertTrue(isinstance(lga, LocalGovArea))

    def test_LGA_string_representation(self):
        """
        this tests that objects of the LocalGovArea have a name that is the same as the name attribute of the local
        government area
        :return:
        """
        lga = LocalGovArea.objects.get(name="The local Government Area")
        self.assertEqual(lga.__str__(), lga.name)
