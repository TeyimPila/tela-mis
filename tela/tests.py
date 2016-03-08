from django.test import TestCase
from .models import Neighborhood

# Create your tests here.


class TestNeighborhood(TestCase):

    def setUp(self):
        Neighborhood.objects.create(name="The Neighborhood name")

    def test_neighborhood_creation(self):
        neigh = Neighborhood.objects.get(name="The Neighborhood name")
        self.assertTrue(isinstance(neigh, Neighborhood))
        self.assertEqual(neigh.__str__(), neigh.name)
