count = 1
user_input = int(input("enter a number "))
negative_number = 0
positive_number = 0
sum_of_numbers = 0
sum_of_positive_numbers = 0
sum_of_negative_numbers = 0
while ((user_input < 0 or user_input > 0) and user_input!=0):
     if(user_input < 1):
        negative_number+=1
        sum_of_negative_numbers += user_input
     if(user_input>=0):
        positive_number+=1
        sum_of_positive_numbers+= user_input

     sum_of_numbers+=user_input
     average_of_numbers = sum_of_numbers / count


     user_input = int(input("enter a number"))
     count+=1

print("total negative numbers are :", negative_number)
print("total positive number are: ", positive_number)
print("sum of total numbers is: ",sum_of_numbers)
print("sum of total numbers of nagative numbers is: ", sum_of_negative_numbers)
print("sum of total numbers of positive number is: ", sum_of_positive_numbers)
print("the average of the total sum of numbers is :", average_of_numbers)



