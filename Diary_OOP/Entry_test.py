from unittest import TestCase

from Diary_OOP.Entry import Entry


class Entry_test(TestCase):

    def test_that_my_account_exists(self):
        entry: Entry = Entry('The Lord', "The Lord is my shepherd", 1)
        self.assertIsNotNone(entry)

    def test_that_my_entry_has_a_title(self):
        entry: Entry = Entry('The Lord', "The Lord is my shepherd", 1)
        entry.set_my_entry_title("The Lord")
        self.assertEquals("The Lord", entry.get_my_entry_title())

    def test_that_my_account_has_body(self):
        entry: Entry = Entry('The Lord', "The Lord is my shepherd", 1)
        entry.set_my_entry_body("The Lord is my shepherd")
        self.assertEqual("The Lord is my shepherd", entry.get_my_entry_body())
