#celcius = float(input("enter your degree in celsius: "))
#celcius_fahr = celcius * 1.8+32.0
#print(celcius_fahr)



#def celcius_to_fahr(cel_val):
 #   """
    
  #  :param cel_val: float
   ##>>> celcius_to_fahr(16)
    #60.8
    #"""
    #return cel_val*1.8+32.0
    
#cel_val = 16
#print(celcius_to_fahr(cel_val))


#def my_name(name):
   
 #   """

  #  :param name: String
   # :return: String
   # >>> my_name("Prof")
    #'my name is Prof'
    #"""

    #return "my name is %s"%name

#my_name ("Prof")





#def get_digit(number, position):
 #   number = str(number)
  #  return number[position]

#print(get_digit(5276,2))


#def unique(numbers)

#x = (2, 3, 9, 12, 16, 4, 2, 3)
#y = (2,3,21,4,19,18,12)

#lenght = len(x)
#count = 0
#for i in range (1, lenght, 1 ):
    #if number in len(x) == number in len(x):
        #print("false")

def get_out_liar(list):
    for each in list:
        if each % 2 == 0:
            return each
        elif each % 2 != 0:
            return each

print(get_out_liar([1,2, 3, 5, 7, 9]))