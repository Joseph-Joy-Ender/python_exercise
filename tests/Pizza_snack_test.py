from unittest import TestCase

from chibuzo_assignment import Pizza_snacks
from chibuzo_assignment.Pizza_snacks import super_hungry, hungry_people, classic_people, total_number_of_slices


class Test(TestCase):

    def test_for_hungry_people(self):
        people = 5
        self.assertEqual(20, super_hungry(people))

    def test_for_hungry(self):
        people = 4
        self.assertEqual(8, hungry_people(people))

    def test_for_classic(self):
        people = 5
        self.assertEqual(5, classic_people(people))

    def test_total_number_slices(self):
        superHungryPeople = 20
        hungryPeople = 10
        classicPeople = 10
        self.assertEqual(110, total_number_of_slices(superHungryPeople, hungryPeople, classicPeople))

    def test_for_number_of_big_box_of_pizza_needed(self):
        expected = Pizza_snacks.total_number_of_big_boxes(20, 15, 10)
        self.assertEqual(12, expected)

    def test_for_number_of_medium_box_of_pizza_needed(self):
        expected = Pizza_snacks.total_number_of_medium_boxes(10, 5, 10)
        self.assertEqual(10, expected)

    def test_for_number_of_small_box_of_pizza_needed(self):
        expected = Pizza_snacks.total_number_of_small_boxes(5, 5, 10)
        self.assertEqual(10, expected)

 