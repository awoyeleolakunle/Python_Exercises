i=0
user_input = int(input("enter a number "))
for i in range(1,user_input):
    if (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    elif (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
    else:
        print(i)
    #count = count + 1