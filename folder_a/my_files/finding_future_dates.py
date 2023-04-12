count = 0
day = ""
future_day = 0
current_day_of_the_week = int(input("enter a day of the week "))

while (current_day_of_the_week != -1):

    if (current_day_of_the_week == 0):
        day = "Sunday"

    if (current_day_of_the_week == 1):
        day = "Monday"

    if (current_day_of_the_week == 2):
        day = "Tuesday"

    if (current_day_of_the_week == 3):
        day = "Wednesday"

    if (current_day_of_the_week == 4):
        day = "Thursday"

    if (current_day_of_the_week == 5):
        day = "Friday"

    if (current_day_of_the_week == 6):
        day = "Saturday"

    print("today is ", day)

    a_new_day = int(input("enter a future day of week"))
    future_day = (current_day_of_the_week + a_new_day)%7
    #if ((a_new_day + current_day_of_the_week) > 6):
     #   future_day = a_new_day + current_day_of_the_week - 7
    #if ((a_new_day + current_day_of_the_week) > 13):
       # future_day = a_new_day + current_day_of_the_week - 14
    #if ((a_new_day + current_day_of_the_week) > 20):
        #future_day = a_new_day + current_day_of_the_week - 21
    #if ((a_new_day + current_day_of_the_week) > 27):
       # future_day = a_new_day + current_day_of_the_week - 28

    if (future_day == 0):
        day = "Sunday"
    elif (future_day == 1):
        day = "Monday"
    elif (future_day == 2):
        day = "Tuesday"
    elif (future_day == 3):
        day = "Wednesday"
    elif (future_day == 4):
        day = "Thursday"
    elif (future_day == 5):
        day = ("Friday")
    elif (future_day == 6):
        day = "Saturday"

    print("the future day is in the next", a_new_day,"days and the day is on ", day)

    current_day_of_the_week = int(input("enter a day of the week "))

count+=1
