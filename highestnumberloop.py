
count = 0
#largest_so_far = float("-inf")
#smallest_so_far = float("+inf")
largest_so_far = 0
smallest_so_far = 0
while count !=0 :

    number = int(input("Give me a number: "))
    if number > largest_so_far:
        largest_so_far = number
    else :
        smallest_so_far<= largest_so_far
        #number < smallest_so_far
        smallest_so_far = number

    count = count + 1

print("The largest number is", largest_so_far)
print("The smallest number is", smallest_so_far)

