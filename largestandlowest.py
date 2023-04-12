count = 0
largest_number = float("-inf")
smallest_number= float("+inf")
user_input = int(input(" Enter a number "))

while (count > 0) :

    if user_input > largest_number:
        largest_number = user_input
    elif user_input < smallest_number:
        smallest_number = user_input


    count +=1
print ("the largest number is", largest_number)
print ("the smallest number is", smallest_number)