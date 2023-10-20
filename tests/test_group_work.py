from unittest import TestCase

from tasks.group_work import list_of_given_number, odd_numbers_in_a_list, double_item_in_list, change_of_element, \
    empty_list, concatenate_list


class Test(TestCase):
    def test_list_of_numbers(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(expected, list_of_given_number(1, 21))

    def test_odd_numbers_in_a_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.assertEqual(expected, odd_numbers_in_a_list(numbers))

    def test_double_item_in_a_list(self):
        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
        self.assertEqual(expected, double_item_in_list(odd_numbers_in_a_list(inputs)))

    def test_change_of_element(self):
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 9, 25, 49, 0, 0, 0, 0, 289, 361]
        self.assertEqual(expected, change_of_element(double_item_in_list(odd_numbers_in_a_list(number))))

    def test_that_list_can_be_emptied(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        actual = []
        self.assertEqual(actual, empty_list(change_of_element(double_item_in_list(odd_numbers_in_a_list(expected)))))

    def test_that_list_can_be_concatenated(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        list3 = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(list3, concatenate_list(list1, list2))
