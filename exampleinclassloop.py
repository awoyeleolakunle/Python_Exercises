#hello = "hello world"
#for i, l in enumerate(hello):
 #   print(f"{l}--> {i}")

#for index in range(len(hello)):
 #   print (f"{hello[index]}-->{index}")


#s = "hello world"
#for i in range(len(s)):
    #print (s[i])
    #print(f"{s[i]} is at index {i}")

s= "hello world"
to_be_found = "l"
#for i in range(len(s)):

  #  if s[i] == to_be_found:
   #     print(f"{s[i]} was found at index{i}")
 #       break

#else:
 #   print(f"Sorry I could not find you{to_be_found}")


for index, char in enumerate(s):
     if char == to_be_found:
         print (f"{char} found at index{index}")
         break
else:
    print(-1)
