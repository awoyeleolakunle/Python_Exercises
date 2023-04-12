user_input = int(input(" enter a number"))
count = 1
factor = 0
sum_factor= 0
while count < user_input:
    if user_input%count == 0:
      factor +=1
      sum_factor += count
    if sum_factor > user_input:
        print( user_input, "is abundant")
    elif sum_factor < user_input:
        print(user_input, "is deficient")
    else:
        print (user_input, "is a perfect number")

    count += 1
print (sum_factor, "is the sum of factor")
print ("total number of factors is ",factor )