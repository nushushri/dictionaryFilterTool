longList = open('words_alpha.txt', 'r')
shortList = open('fiveLetterOnly.txt', 'w')

for word in longList:
    if(len(word) == 6):
        shortList.write(word)

longList.close()
shortList.close()
