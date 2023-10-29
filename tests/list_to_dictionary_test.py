from unittest import TestCase
from functions_list.dictionary_functions import list_to_dictionary


class Test(TestCase):

    def test_list_to_diction(self):
        sample_input = ['apple', 'banana', 'coconut']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(expected, list_to_dictionary(sample_input))

    def test_if_key_is_present(self):
        sample_input = ['apple', 'banana', 'coconut', 'corn']
        output = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'}
        self.assertEqual(list_to_dictionary(sample_input), output)
