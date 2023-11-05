from unittest import TestCase
from chibuzo_assignment.Pizza_snacks import super_hungry, hungry_people


class Test(TestCase):

    def test_for_hungry_people(self):
        people = 5
        self.assertEqual(20, super_hungry(people))

    def test_for_hungry(self):
        people = 4
        self.assertEqual(8, hungry_people(people))
