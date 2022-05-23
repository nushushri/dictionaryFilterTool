import os

try: os.remove("candidates.txt")
except FileNotFoundError: pass

try: os.remove("updatedCandidates.txt")
except FileNotFoundError: pass

fiveLetterOnly = open("fiveLetterOnly.txt", "r")
candidates = open("candidates.txt", "w")
for word in fiveLetterOnly:
    candidates.write(word)
fiveLetterOnly.close()
candidates.close()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

inWord = []
notInWord = []
wordPositions = {0:"_", 1: "_", 2: "_", 3: "_", 4: "_"}

while(True):
    candidates = open("candidates.txt", "r")
    updatedCandidates = open("updatedCandidates.txt", "w")

    guaranteed = input("letters that must be in the word, no separation: ")
    for letter in guaranteed:
        inWord.append(letter.lower)

    ignore = input("letters to ignore, no separation: ")
    for letter in ignore:
        notInWord.append(letter.lower)

    positions = input("letters you know the position of (put _ where you don't know a letter):")
    for i in range(0, 5):
        if(positions[i] != "_"):
            wordPositions[i] = positions[i]

    for word in candidates:
        considerFurther = True
        for letter in word:
            if letter in notInWord:
                considerFurther = False
        for letter in guaranteed:
            if letter not in word:
                considerFurther = False
        for i in range(0, 5):
            if(wordPositions[i] != "_"):
                if(word[i] != wordPositions[i]):
                    considerFurther = False
        if considerFurther:
            updatedCandidates.write(word)
    
    updatedCandidates.close()
    candidates.close()
    os.remove("candidates.txt")
    os.rename("updatedCandidates.txt", "candidates.txt")




