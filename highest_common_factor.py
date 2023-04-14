def highest_common_factor(*numbers):
    list = []
    list2 = []
    list3 = []

    for index in range(len(numbers)):
        list2.append(numbers[index])


    for i in range(2, numbers[0], 1):

        for number in range(len(numbers)):
            if list2[number] % i == 0:
                list.append(i)
    #for k in range (len(list)):
    for y in range(len(list)):
        for k in range (len(numbers)):
            if(list2[k] % list[y]==0):
                list3.append(list[y])


    print(list)
    print(list2)
    print(list3)


highest_common_factor(10, 100)
