# dictionaryFilterTool

This is a tool designed off of my love for Wordle (though I have no direct association with New York Times, the game Wordle, or anything of the like). Simply open up Wordle side-by-side, enter in each word, and report the outcomes (correct and incorrect letters and their positions) into the program as you go. The file "candidates.txt" will display the updated possible words as you go. The "updatedCandidates.txt" file can be ignored.

Enjoy!

Note: This program uses a dictionary obtained from https://github.com/dwyl/english-words . Specifically, I duplicated the "words_alpha.txt" file from that repo. I then extracted all of the 5-letter words into a text file called "fiveLetterOnly.txt", and further filtered this down in "candidates.txt" and "updatedCandidates.txt". 
