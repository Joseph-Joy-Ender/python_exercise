import unittest
from unittest import TestCase
from classWork import tripling_a_list
from classWork.tripling_a_list import triple_a_list


class Testcase(TestCase):

    def test_triple_number(self):
        numbers = triple_a_list([3, 7, 2, 6, 5])
        self.assertEqual(numbers, [27, 343, 8, 216, 125])
