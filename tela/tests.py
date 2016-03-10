from django.test import TestCase
from .models import Center
class CenterTest(TestCase):
    def create_venue(self, title='Yola Center', group_size=23):
        return Center.objects.create(title=title, group_size=group_size)

    def test_venue(self):
        c = self.create_venue()
        return self.assertTrue(isinstance(c, Center))

    def test_center_str_method(self):
        c = Center(title='Yola Center')
        self.assertEqual(c.__str__(), "Yola Center")

# Create your tests here.
