count = 1
while count <= 100:
    if(count % 3== 0):
        print ("fizz")
    elif (count%5 ==0):
        print("buzz")
    elif (count% 3==0 and count%5==0):
        print("fizz buzz")
    else:
     print(count, end="  ")
    count = count + 1
