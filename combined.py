import os
import tkinter as tk

# resetting the system at the beginning
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

# interface
window = tk.Tk()

titleFrame = tk.Frame()
titleText = tk.Label(master = titleFrame, text = "Dictionary Filter Tool", background = "#87CEFA", width=44)
titleText.pack(fill=tk.X)
titleFrame.pack(fill=tk.X)

promptOneFrame = tk.Frame()
promptOneText = tk.Label(master = promptOneFrame, text = "Letters that must be in the word: ", width=30)
inputOne = tk.Entry(master = promptOneFrame, background="#87CEFA", width=10)
promptOneText.pack(side=tk.LEFT)
inputOne.pack(side=tk.LEFT)
promptOneFrame.pack()

promptTwoFrame = tk.Frame()
promptTwoText = tk.Label(master = promptTwoFrame, text = "Letters that are not in the word: ", width=30)
inputTwo = tk.Entry(master = promptTwoFrame, background="#87CEFA", width=10)
promptTwoText.pack(side=tk.LEFT)
inputTwo.pack(side=tk.LEFT)
promptTwoFrame.pack()

promptThreeFrame = tk.Frame()
promptThreeText = tk.Label(master = promptThreeFrame, text = "Positions of Known Letters: ", width=30)
inputThree = tk.Entry(master = promptThreeFrame, background="#87CEFA", width=10)
promptThreeText.pack(side=tk.LEFT)
inputThree.pack(side=tk.LEFT)
promptThreeFrame.pack()

goFrame = tk.Frame()
goText = tk.Button(master=goFrame, text="Go", width=4)
goText.pack()
goFrame.pack()

    
fiveLetterFrame = tk.Frame()
firstLetterText = tk.Label(master=fiveLetterFrame, text="-", width=3, height=2, background="#98FB98")
secondLetterText = tk.Label(master=fiveLetterFrame, text="-", width=3, height=2, background="#98FB98")
thirdLetterText = tk.Label(master=fiveLetterFrame, text="-", width=3, height=2, background="#98FB98")
fourthLetterText = tk.Label(master=fiveLetterFrame, text="-", width=3, height=2, background="#98FB98")
fifthLetterText = tk.Label(master=fiveLetterFrame, text="-", width=3, height=2, background="#98FB98")
firstLetterText.grid(row=0, column=0, padx=2, pady=3)
secondLetterText.grid(row=0, column=1, padx=2, pady=3)
thirdLetterText.grid(row=0, column=2, padx=2, pady=3)
fourthLetterText.grid(row=0, column=3, padx=2, pady=3)
fifthLetterText.grid(row=0, column=4, padx=2, pady=3)
fiveLetterFrame.pack()

allLettersFrame = tk.Frame()
for i in range(2):
    for j in range(13):
        letterLabel = tk.Label(master=allLettersFrame, text=chr(65+13*i+j), width=3, height=2, background="gray")
        letterLabel.grid(row=i, column=j, padx=2, pady=3)
allLettersFrame.pack()

def updateLabel(letter, color):
    letter = letter.upper()
    gridRow = int(ord(letter)-65)//13
    gridCol = int(ord(letter)-65)%13
    # currentLabel = allLettersFrame.grid_slaves(gridRow, gridCol)[0]
    if(color == "yellow"):
        colorCode = "#FFE175"
    if(color == "red"):
        colorCode = "#FF9292"
    if(color == "green"):
        colorCode = "#98FB98"
    currentLabel = tk.Label(master=allLettersFrame, text=chr(65+13*gridRow+gridCol), width=3, height=2, background=colorCode)
    currentLabel.grid(row=gridRow, column=gridCol, padx=2, pady=3)

def updateFive(i, letter):
    letter = letter.upper()
    currentLabel = tk.Label(master = fiveLetterFrame, text = letter, width = 3, height = 2, background = "#98FB98")
    currentLabel.grid(row=0, column=i, padx=2, pady=3)

# clicking action
def go(self):
    candidates = open("candidates.txt", "r")
    updatedCandidates = open("updatedCandidates.txt", "w")

    guaranteed = inputOne.get()
    for letter in guaranteed:
        inWord.append(letter.lower())
        updateLabel(letter, "yellow")
    if(len(guaranteed) > 0): inputOne.delete(0, tk.END)

    ignore = inputTwo.get()
    for letter in ignore:
        notInWord.append(letter.lower())
        updateLabel(letter, "red")
    if(len(ignore) > 0): inputTwo.delete(0, tk.END)
    

    positions = inputThree.get()
    for i in range(0, min(len(positions),5)):
        if(positions[i] != "_"):
            wordPositions[i] = positions[i]
            updateLabel(wordPositions[i], "green")
            updateFive(i, wordPositions[i])
    if(len(positions) > 0): inputThree.delete(0, tk.END)

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
            print(word[0:5])
    
    updatedCandidates.close()
    candidates.close()
    os.remove("candidates.txt")
    os.rename("updatedCandidates.txt", "candidates.txt")
    print("---")

# loading the interface up
goText.bind("<ButtonRelease>", go)
window.mainloop()
