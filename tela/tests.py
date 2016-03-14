from django.test import TestCase
from .models import Neighborhood



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





from .models import Equipment
# from .models import Facilitator
from django.db import IntegrityError

from .models import Tutor



# Create your tests here.


class TestNeighborhood(TestCase):

    def setUp(self):
        Neighborhood.objects.create(name="The Neighborhood name")

    def test_neighborhood_creation(self):
        neigh = Neighborhood.objects.get(name="The Neighborhood name")
        self.assertTrue(isinstance(neigh, Neighborhood))
        self.assertEqual(neigh.__str__(), neigh.name)

class TestEquipmentModel(TestCase):

    def test_regular(self):
        """
        test that a single facilitator can collect multiple equipment but not vice versa
        """

        facilitator_1 = Facilitator.objects.create(first_name="f1")
        facilitator_2 = Facilitator.objects.create(first_name="f2")

        for serial_num in ['id1', 'id2', 'id3']:
            Equipment.objects.create(facilitator=facilitator_1, serial_num=serial_num)
            Equipment.objects.create(facilitator=facilitator_2, serial_num=serial_num)

        equipment_1 = [facilitator_1.first_name for facilitator in facilitator_1.equipment_set.all()]
        equipment_2 = [facilitator_1.first_name for facilitator in facilitator_2.equipment_set.all()]
        self.assertEqual(equipment_1, equipment_2, ['id1', 'id2', 'id3'])

    def test_uniqueness(self):
        """
        test that each equipment/facilitator record are unique
        """
        facilitator = Facilitator.objects.create(first_name = 'fn')
        Equipment.objects.create(facilitator=facilitator, serial_num='sn')

        with self.assertRaises(IntegrityError):
            Equipment.objects.create(facilitator=facilitator, serial_num='sn')


















        #
        # def setUp(self):
        #     self.equipment = Equipment.objects.create(serial_number="A12345", equipment_type="Radio",
        #                                               availability='available')
        #     self.equipment = Equipment.objects.create(serial_number="A12346", equipment_type="Radio",
        #                                               availability='available')
        #
        # def test_equipment_creation(self):
        #     """
        #     tests that an equipment record can be created
        #     :return:
        #     """
        #     equipment = Equipment.objects.create(serial_number="A12345", equipment_type="Radio",
        #                                          availability='available')
        #     self.assertTrue(isinstance(Equipment,  equipment))


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

















        #
        # def setUp(self):
        #     self.equipment = Equipment.objects.create(serial_number="A12345", equipment_type="Radio",
        #                                               availability='available')
        #     self.equipment = Equipment.objects.create(serial_number="A12346", equipment_type="Radio",
        #                                               availability='available')
        #
        # def test_equipment_creation(self):
        #     """
        #     tests that an equipment record can be created
        #     :return:
        #     """
        #     equipment = Equipment.objects.create(serial_number="A12345", equipment_type="Radio",
        #                                          availability='available')
        #     self.assertTrue(isinstance(Equipment,  equipment))

