from django.test import TestCase
from .models import Fascilitator


class FascilitatorTest(TestCase):

    def create_fascilitator(self, first_name='Fatima', last_name='Hafsat', phone='0813456789', email='example@yahoo.com', age=21):
        return Fascilitator.objects.create(first_name=first_name, last_name=last_name, phone=phone, email=email, age=age)

    def test_fascilitator(self):
        f = self.create_fascilitator()
        self.assertTrue(isinstance(f, Fascilitator))

    def test_fascilitator_str_method(self):
        f = Fascilitator(first_name='Fatima', last_name='Umar')
        return self.assertEqual(f.__str__(), "Fatima Umar")


# Create your tests here.
