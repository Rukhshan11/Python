# Write a program with a loop that repeatedly asks the user to enter a word. The user should
# enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
# loop ends, the program should display the average length of the words entered, rounded to
# the nearest whole number.

totalWords = 0.0
avgWord = 0.0
wordCount = 0.0

userWord = input('Enter words/sentences or press Enter to quit: ')

while userWord != '':
    wordLength = len(userWord)
    userWord = input('Enter words/sentences or press Enter to quit: ')
    totalWords += wordLength
    wordCount += 1

avgWord = totalWords / wordCount
print('Average word is', avgWord)