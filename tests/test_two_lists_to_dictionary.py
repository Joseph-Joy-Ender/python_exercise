from unittest import TestCase
from functions_list.two_lists_to_dictionary import two_list_to_dictionary


class Test(TestCase):
    def test_two_list_to_dictionary(self):
        input1 = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        sample_outputs = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sample_outputs, two_list_to_dictionary(input1, input2))
