import random
count = 0
number_to_be_guessed = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))

number_to_be_guessed = 50
number_of_guesses = 0
while count < 2:
    if guess == number_to_be_guessed:
        print("you got it right")

        break
    else:

        count = count + 1
        print("try again later, Its unfortunate you could not guess", number_to_be_guessed)
        guess = int(input("Guess a number between 1 and 100: "))




