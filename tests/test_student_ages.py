from unittest import TestCase
from tasks.Student_Age import student_age


class Test(TestCase):
    def test_that_when_name_is_entered_age_is_shown(self):
        expected = {'dike': 33}
        self.assertEqual(expected, student_age())
