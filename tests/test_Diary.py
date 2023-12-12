from unittest import TestCase

from Banking.InvalidPinException import InvalidPinException
from diary.Diary import Diary


class TestDiary(TestCase):
    def testDiaryHasUsername(self):
        diary: Diary = Diary("JOY", "1234")
        self.assertTrue(diary.is_locked())
        diary.unlocked_diary("1234")
        self.assertFalse(diary.is_locked())

    def testThatDiaryCannotBeUnlockedWithWrongPassword(self):
        diary: Diary = Diary("JOY", "1234")
        with self.assertRaises(InvalidPinException):
            diary.unlocked_diary("1254")

    def testThatDiaryCanBeLockedAfterUnlocking(self):
        diary: Diary = Diary("JOY", "1234")
        self.assertTrue(diary.is_locked())
        diary.unlocked_diary("1234")
        diary.lock_diary()
        self.assertFalse(diary.is_locked())

    def testThatEntryCanBeCreated(self):
        diary: Diary = Diary("JOY", "1234")
        diary.unlocked_diary("1234")
        diary.create_entry("My diary app", "My love story just begun")
        self.assertEqual(1, diary.get_total_number_of_entry())

    def testThatEntryCanBeDeleted(self):
        diary: Diary = Diary("JOY", "1234")
        diary.unlocked_diary("1234")
        diary.create_entry("My diary app", "My love story just begun")
        diary.create_entry("My second diary", "story just begun")
        self.assertEqual(2, diary.get_total_number_of_entry())
        diary.delete_entry(1)
        self.assertEqual(1, diary.get_total_number_of_entry())
