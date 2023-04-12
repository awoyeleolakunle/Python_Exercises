count = 1
factor = 0
user_input = int(input("enter a number "))

while (count <= user_input):
    if (user_input % count == 0):
        factor = factor + 1

    count += 1

if (factor > 2):
        print(user_input, " is not a prime number")
else:
        print(user_input, " is a prime number ")

