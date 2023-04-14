


def rotateArrayInIndex(*numbers):

    list = []
    num = 0
    for i in range (len(numbers)):
        list.append(numbers[i])

    for i in range (len(numbers)):
            num =  list[0]
            list[0] = list[len(numbers)-1]
            list[len(numbers)-1] = num
    print(list)

rotateArrayInIndex(1,2,3,4,5)

