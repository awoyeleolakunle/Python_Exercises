def decimal_to_binary_conversion(number: int) -> None:
    list_of_numbers = []
    new_number: int

    while (number != 0):
        new_number = number % 2
        list_of_numbers.append(new_number)
        number = number // 2

    for i in range(len(list_of_numbers)-1 , -1, -1):
         print(list_of_numbers.__getitem__(i), end="")


decimal_to_binary_conversion(102)
