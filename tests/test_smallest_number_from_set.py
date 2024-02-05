from unittest import TestCase
from tasks.smallest_number_from_set import smallest_from_set


class Test(TestCase):
    def test_smallest_from_set(self):
        first = {5, 4, 11, 13, 9}
        second = {9, 11, 15, 1, 14}
        ouputs = 9
        self.assertEqual(ouputs, smallest_from_set(first, second))

    def test_another_smallest_from_set(self):
        inputs1 = {2, -3, 5, 6, 7, 8}
        inputs2 = {1, -3, 7, 10, 11, 8}
        second_ouputs = -3
        self.assertEqual(second_ouputs, smallest_from_set(inputs1, inputs2))
