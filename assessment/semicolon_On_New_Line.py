
def printWordOnNewLine( word):
    new_word  = str(word)
    list = []
    for i in range (len(new_word)):
        list.append(new_word[i])
        print(list[i])

printWordOnNewLine("semicolon")
