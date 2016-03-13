from django.test import TestCase


from .models import Venue

class VenueTest(TestCase):

    def create_venue(self, address='This is a test address', location_longitude='127.98374', location_latitude='124.7387484'):
        return Venue.objects.create(address=address, location_longitude=location_longitude, location_latitude=location_latitude)

    def test_venue_instance_creation(self):
        v = self.create_venue()
        self.assertTrue(isinstance(v, Venue))

    def test_venue_get_coordinate_method(self):
        v = Venue(location_latitude='123.98746', location_longitude='165.987636')
        self.assertEqual(v.get_coordinates(), "(123.98746,165.987636)")





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
