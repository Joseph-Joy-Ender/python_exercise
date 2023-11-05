from unittest import TestCase
from tasks.Adding_a_string_to_another_string import add_to_string


class Test(TestCase):
    def test_add_to_string(self):
        inputs = 'abc'
        expected = 'abcing'
        self.assertEqual(expected, add_to_string(inputs))

    def test_that_another_string_can_be_added(self):
        inputs = 'sting'
        expected = 'stingly'
        self.assertEqual(expected, add_to_string(inputs))

    def test_that_string_is_left_unchanged(self):
        inputs = 'it'
        expected = 'it'
        self.assertEqual(expected, add_to_string(inputs))