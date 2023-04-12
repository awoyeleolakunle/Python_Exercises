class Animal:

    # def __init__(self): ...

    def __init__(self, name, speak, talk, dance, run: bool):

        self.animal_name = name
        self.speak = speak
        self.talk = talk
        self.animal_dance_skill = dance
        self.run: bool = run
        self.legs = []
        self.leg_count = 0

    def set_animal_name(self, name):
        self.animal_name = name

    def get_animal_name(self):
        return self.animal_name

    def set_animal_language(self, speak):
        self.speak = speak

    def get_animal_language(self):
        return self.speak

    def set_animal_can_run(self, run: bool):
        self.run = run

    def animal_can(self) -> bool:
        if self.run:
            return True
        return False

    def size_of_legs(self, *args):
        for i in range(len(args)):
            self.legs.append(i)
        #yself.animal.legs = [i for i in range]
            self.leg_count += 1

    def get_size_of_leg(self):
        return self.legs

    def get_size_of_leg_count(self):
        return self.leg_count

