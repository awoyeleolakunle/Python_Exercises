from NewClass import NewClass

if __name__== '__main__':

    name = input("enter your name ")
    age = int(input("enter your age"))
    sola = NewClass(name, age)
    print(sola.get_name() + " is my name and I am " , sola.get_age() , "years old")