count = 0
largest_so_far = float("-inf")
second_largest_so_far = float("-inf")
while count < 5:
    number = int(input("Enter a number: "))
    if number > largest_so_far:
       second_largest_so_far = largest_so_far
       largest_so_far = number
    if largest_so_far < second_largest_so_far:
       second_largest_so_far = number


    count = count + 1
print()
print("the largest number is ", largest_so_far)
print("the second largest number is ", second_largest_so_far)

