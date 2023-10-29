from unittest import TestCase
from tasks.Student_age_with_parameter import student_age


class Test(TestCase):
    def test_student_age(self):
        name = 'dike'
        expected = {'dike': 33}
        self.assertEqual(expected, name)
