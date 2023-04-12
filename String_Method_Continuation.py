hello = "Hello there!!!"

#print(hello.endswith("!"))
 #   hello.is
#rint(hello.replace("l","q"))
#print(hello.replace("l","q" ,2))

bin_ = "101100011001011110#78"
print(bin_.replace("1", "X").replace("0", "1").replace("X", "0"))
print(bin_.translate(str.maketrans("01","10")))
print(bin_.translate(str.maketrans("01", "10", "8#7")))