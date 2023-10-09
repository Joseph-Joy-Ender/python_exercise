import unittest
from unittest import TestCase
from functions_list import tuple_flakes
from functions_list.tuple_flakes import tuples1, more_than_one_tuple
from functions_list.tuple_flakes import swapped_tuple


class Testcase(TestCase):

    def test_that_tuple_is_reversed(self):
        tuple1 = (10, 20, 30, 40, 50)
        self.assertEqual((50, 40, 30, 20, 10), tuples1(tuple1))

    def test_that_tuple_position_is_swapped(self):
        numbers = (15, 25, 60, 50, 30, 40, 45, 55)
        self.assertEqual((55, 15), swapped_tuple(numbers))

    def test_that_tuple_that_appears_more_than_once(self):
        self.assertEqual((5, 10, 15), more_than_one_tuple())
