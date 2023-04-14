
def guess_age():

    age = 20
    guess: int = int(input("guess my age"))
    while guess!=age:

        if guess > age:
            print("That is too high")
        if guess < age:
            print("that is too low")


        guess = int(input("guess my age"))

    print("Yes, you gueesed right")

guess_age()
