
def is_palindrom(number: int) -> bool:
    temp = str(number)
    list = []
    list2 =[]
    for i in range(len(temp)):
        list.append(temp[i])
    for i in range(len(temp) - 1, -1, -1):
        list2.append(temp[i])
    if list == list2:
        print("True")
    else:
        print("False")

is_palindrom(100000000000001)



def sum_of_digits(digits: int) -> int:
    sum_of_digits = 0
    while digits>0:
        sum_of_digits += digits%10
        digits = digits//10
    print("The sum of digits is ", sum_of_digits)

sum_of_digits(7512)

