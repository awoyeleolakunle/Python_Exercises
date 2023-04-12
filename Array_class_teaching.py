from array import *

#x = array("i", [1,2,3,4,5])
#print(len(x))
x = array("i",[])
x = [1,2,3,4,5]
print(len(x))

sentence = ["obi is a boy", "ada is a girl", "Tommy is a dog"]
print(sentence[0])
print(sentence[0][:3])
print(sentence[0][9:12])
print(sentence[1][4::])
#sentence.append("Jonathan")
sentence.insert(0, 'Jonathan')
print(sentence)
