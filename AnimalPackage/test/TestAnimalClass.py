import unittest

from AnimalPackage.Animal import Animal


class TestAnimalClass(unittest.TestCase):
    animal = Animal("name", "Yoruba", "Shoki", "jgfvf",True,)
    #animal2 = Animal()

    def test_animal_name(self):
        #given
        self.animal.set_animal_name("Snoppy")
        #when
        result = self.animal.get_animal_name()
        #assert
        self.assertEqual("Snoppy", result)

    def test_animal_language(self):
        #given
        self.animal.set_animal_language("Swahili")
        #when
        animal_language = self.animal.get_animal_language()
        #assert
        self.assertEqual("Swahili", animal_language)

    def test_animal_can_run(self):
        #given
        self.animal.set_animal_can_run(True)
        animal_run = self.animal.animal_can()
        #assert
        self.assertTrue(animal_run)

    def test_lenght_of_legs(self):
        self.animal.size_of_legs(6,7,8,9)
        size = self.animal.get_size_of_leg_count()
        print(size)
        self.assertIsNotNone(size)
