from unittest import TestCase
from functions_list.removing_empty_strings import remove_multiple_empty_strings


class Test(TestCase):
    def test_remove_multiple_empty_strings(self):
        sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        sample_output = ['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(sample_output, remove_multiple_empty_strings(sample_input))
