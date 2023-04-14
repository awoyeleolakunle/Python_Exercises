

word = "Mississippi"

def numberOfCharactersInAWord(word:str):
        new_word = str(word)
        list = []
        s_count = 0
        i_count= 0

        for i in range(len(word)):
            list.append(word[i])

        for i in range (len(list)):
            if(list[i]=="s"):
                s_count+=1
            if (list[i]=="i"):
                i_count+=1
        print("s = ", s_count,  )
        print("i = ", i_count )

numberOfCharactersInAWord("Mississippi")
