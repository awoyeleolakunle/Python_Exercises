import random
randomToBeGuess = random.randint(1,100)
count = 0
numberToBeGuessed = 50
numberOfGuesses = 0
guess = int(input("Enter a guess number between 1 and 100: "))
while count < 2:

    if guess > numberToBeGuessed:
        print("You are close but the number you entered is greater than the actual number")
    if guess == numberToBeGuessed:
        print("wow Omo Ope Ogbon Sodiki")

        break

    else:
        count = count + 1

        print("you are close but the number you entered is lesser than the actual number")
        guess = int(input("enter a guess number between 1 and 100: "))







