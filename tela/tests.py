from django.test import TestCase
from .models import Beneficiary




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

    



