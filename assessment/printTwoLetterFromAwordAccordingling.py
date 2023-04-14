
def printTwoLettersAccordingly(word):
    new_word = str(word)
    list = []
    for i in range (len(new_word)):
        list.append(word[i])

    for i in range (len(list)):
        print(list[i], end="")
        if( i% 2 != 0):
            print()

printTwoLettersAccordingly("ventures")
