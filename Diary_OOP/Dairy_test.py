from unittest import TestCase

from Diary_OOP.Diary import Diary


class Diary_test(TestCase):

    def test_that_my_dairy_exists(self):
        dairy: Diary = Diary()
        self.assertIsNotNone(dairy)

    def test_how_that_my_entries_can_be_created(self):
        diary: Diary = Diary()
        diary.create_an_entry_for('The Lord', 'The Lord is my shepherd')
        self.assertEqual(1, diary.get_total_of_my_entries())

    def test_that_my_entry_can_be_found(self):
        diary: Diary = Diary()
        diary.create_an_entry_for("The Lord", "The Lord is my shepherd")
        diary.create_an_entry_for("My God", "The Lord is my shepherd")
        expected: str = """
                        Title: My God
                        Body: The Lord is my shepherd
                        Id: 2
                """
        self.assertEqual(expected, diary.view_my_entry(2).__str__())

    def test_that_an_entry_can_be_deleted(self):
        diary: Diary = Diary()
        diary.create_an_entry_for('The Lord', 'The Lord is my shepherd')
        diary.create_an_entry_for("God", "God is good")
        diary.delete_my_entry(1)
        diary.delete_my_entry(1)
        self.assertEqual(0, diary.get_total_of_my_entries())

    def test_that_my_entry_title_can_be_edited(self):
        diary: Diary = Diary()
        diary.create_an_entry_for("The Lord", " The Lord is good all the time")
        expected: str = """
                        Title: My God
                        Body:  The Lord is good all the time
                        Id: 1
                """
        diary.edit_my_entry_title(1, "My God")
        self.assertEqual(expected, diary.view_my_entry(1).__str__())

    def test_that_my_entry_body_can_be_edited(self):
        diary: Diary = Diary()
        diary.create_an_entry_for("The Lord", " The Lord is good all the time")
        expected: str = """
                        Title: The Lord
                        Body: My God is good now and forever
                        Id: 1
                """
        diary.edit_my_entry_body(1, "My God is good now and forever")
        self.assertEqual(expected, diary.view_my_entry(1).__str__())

    def test_for_invalid_id(self):
        diary: Diary = Diary()
        diary.create_an_entry_for("The Lord", " The Lord is good all the time")
        expected: str = """
                        Title: The Lord
                        Body: My God is good now and forever
                        Id: 1
                """
        with self.assertRaises(ValueError):
            diary.validate_id(2)
