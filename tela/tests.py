from django.test import TestCase
from .models import Beneficiary
from .models import Assessment
from .models import Enumerator

# Create your tests here.

class TestAssessment(TestCase):

    def setUp(self):
        self.beneficiary = Beneficiary.objects.create(first_name = "first name", last_name="last name")
        self.enumerator = Enumerator.objects.create(first_name = "first name", last_name="last name")
        self.assessment = Assessment.objects.create(beneficiary = self.beneficiary, enumerator = self.enumerator, type="ass type")

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
        self.assertEqual(self.assessment.__str__(), '%s\'s %s' %(self.beneficiary, self.assessment.type))

