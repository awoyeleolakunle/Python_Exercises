count = 1
user_input = int(input("Enter a number to display corresponding month of the year "))
while (user_input!=0 and user_input<=12) :

    if user_input ==1:
        print(user_input, "January")

    if (user_input==2):
        print(user_input, "February")

    if (user_input==3):
        print(user_input, "March")

    if(user_input==4):
        print(user_input, "April")

    if (user_input ==5):
        print (user_input, "May")

    if (user_input ==6):
        print(user_input, "June")

    if (user_input==7):
        print (user_input, "July")

    if (user_input==8):
        print(user_input, "August")

    if (user_input ==9):
        print(user_input, "September")

    if (user_input==10):
        print(user_input, "October")

    if (user_input ==11):
        print(user_input, "November")

    if (user_input==12):
        print(user_input, "December")

    user_input = int(input("Enter a number to display corresponding month of the year "))

    count+=1



