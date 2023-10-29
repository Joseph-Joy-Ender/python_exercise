from unittest import TestCase
from functions_list.difference_between_smallest_and_larest import difference


class Test(TestCase):
    def test_difference(self):
        sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        smallest = 5
        largest = 75
        expected = largest - smallest
        self.assertEqual(expected, difference(sample_list))
