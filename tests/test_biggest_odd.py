from unittest import TestCase
from classWork import biggest_odd


class Test(TestCase):
    def test_biggest_odd_number(self):
        number = '12345'
        numbers = biggest_odd.biggest_odd(number)
        self.assertEqual(numbers, 5)

    def test_for_second_biggest_number(self):
        number = '23459'
        numbers = biggest_odd.biggest_odd2(number)
        self.assertEqual(numbers, 9)
