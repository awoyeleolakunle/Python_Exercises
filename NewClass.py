

class NewClass:
    def __init__ (self, first_name, age):
        self.first_name = first_name
        self.age = age

    def set_name(self,name):
            self.first_name = name

    def get_name(self):
             return self.first_name

    def set_age(self,age):
            self.age=age

    def get_age(self):
                return self.age



name = input("enter your name ")
age = int(input("enter your age"))
sola = NewClass(name, age)
print(sola.get_name() + " is my name and I am " , sola.get_age() , "years old")


