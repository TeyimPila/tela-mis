from django.test import TestCase
from .models import Beneficiary, Assessment, Enumerator, Center, Neighborhood, Venue, TutorialType, Equipment, \
    Facilitator, Tutor, LocalGovArea
from django.db import IntegrityError


class FacilitatorTest(TestCase):
    def create_Facilitator(self, first_name='Fatima', last_name='Hafsat', phone='0813456789', email='example@yahoo.com',
                           age=21):
        return Facilitator.objects.create(first_name=first_name, last_name=last_name, phone=phone, email=email, age=age)

    def test_Facilitator(self):
        f = self.create_Facilitator()
        self.assertTrue(isinstance(f, Facilitator))

    def test_Facilitator_str_method(self):
        f = Facilitator(first_name='Fatima', last_name='Umar')
        return self.assertEqual(f.__str__(), "Fatima Umar")


class CenterTest(TestCase):
    def create_venue(self, title='Yola Center', group_size=23):
        return Center.objects.create(title=title, group_size=group_size)

    def test_venue(self):
        c = self.create_venue()
        return self.assertTrue(isinstance(c, Center))

    def test_center_str_method(self):
        c = Center(title='Yola Center')
        self.assertEqual(c.__str__(), "Yola Center")


class TestAssessment(TestCase):
    def setUp(self):
        self.beneficiary = Beneficiary.objects.create(first_name="first name", last_name="last name")
        self.enumerator = Enumerator.objects.create(first_name="first name", last_name="last name")
        self.assessment = Assessment.objects.create(beneficiary=self.beneficiary, enumerator=self.enumerator,
                                                    type="ass type")

    def test_assessment_creation(self):
        """
        test that an assessment can be created
        :return:
        """
        self.assertEqual(self.assessment.type, "ass type")
        self.assertEqual(self.assessment.beneficiary, self.beneficiary)
        self.assertEqual(self.assessment.enumerator, self.enumerator)

    def test_assessment_string_representation(self):
        """
        test that assessment object is represented as: first_name Last name's Pre assessment
        :return:
        """
        self.assertEqual(self.assessment.__str__(), '%s\'s %s' % (self.beneficiary, self.assessment.type))


class BeneficiaryModelTest(TestCase):
    """
    This class contains all the test cases for the Beneficiary Model
    """

    def test_verbose_name_plural(self):
        """
        The plural of beneficiary should be beneficiaries
        :return:
        """
        self.assertEqual(str(Beneficiary._meta.verbose_name_plural), "Beneficiaries")

    def test_string_representation(self):
        """
        A beneficiary class object name should return the name of the beneficiary, not 'object'
        :return:
        """
        beneficiary = Beneficiary(beneficiary_name="Name of Beneficiary")
        self.assertEqual(str(beneficiary), beneficiary.beneficiary_name)


class VenueTest(TestCase):
    def create_venue(self, address='This is a test address', location_longitude='127.98374',
                     location_latitude='124.7387484'):
        return Venue.objects.create(address=address, location_longitude=location_longitude,
                                    location_latitude=location_latitude)

    def test_venue_instance_creation(self):
        v = self.create_venue()
        self.assertTrue(isinstance(v, Venue))

    def test_venue_get_coordinate_method(self):
        v = Venue(location_latitude='123.98746', location_longitude='165.987636')
        self.assertEqual(v.get_coordinates(), "(123.98746,165.987636)")


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
        facilitator = Facilitator.objects.create(first_name='fn')
        Equipment.objects.create(facilitator=facilitator, serial_num='sn')

        with self.assertRaises(IntegrityError):
            Equipment.objects.create(facilitator=facilitator, serial_num='sn')


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


class TesTutorialType(TestCase):
    """
    this tests properties of the Tutor Model
    """

    def setUp(self):
        TutorialType.objects.create(tutorial_type="type of tutorial")

    def test_tutorial_type_creation(self):
        tutorial_type = TutorialType.objects.get(tutorial_type="type of tutorial")
        self.assertTrue(isinstance(tutorial_type, TutorialType))
        self.assertEqual(tutorial_type.__str__(), tutorial_type.tutorial_type)
