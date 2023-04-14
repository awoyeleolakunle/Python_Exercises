
def divisible_by_three() -> int:
    number = 30
    sum = 0
    for i in range (1, number+1, 1):
        if i% 3 == 0:
            sum += i
    return sum

print(divisible_by_three())

