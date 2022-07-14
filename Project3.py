# File: WordleAssistant.py
# Student: Chukwuka Madueke
# UT EID: scm3449
# Course Name: CS303E
# 
# Date: 4/30/2022
# Description of Program: Program takes user input and run the popular WORDLE game

import os.path
import random

words = []
def createWordlist(filename):

    for word in filename:
        duplicate = 0
        placeWord = word.strip()
        if (len(placeWord) == 5):
            if(placeWord[-1] != "s"):
                for char in placeWord:
                    if (placeWord.count(char) != 1):
                        duplicate += 1
                if (duplicate == 0):
                    words.append(placeWord)
    return(words, len(words))

def BinarySearch ( words , key ):
    """ Search for key in sorted list lst . """
    low = 0
    high = len ( words ) - 1
    while ( high >= low ):
        mid = ( low + high ) // 2
        if key < words [ mid ]:
            high = mid - 1
        elif key == words [ mid ]:
            return True
        else :
            low = mid + 1
    # What ’s true here ? Why this value ?
    return (False)

def playWordle(manualAnswer = None):
    
    print("Welcome to WORDLE, the popular word game. The goal is to guess a \nfive letter \
    word chosen at random from our wordlist. None of the \nwords on the wordlist \
    have any duplicate letters. \n\nYou will be allowed 6 guesses. Guesses must be \
    from the allowed \nwordlist. We'll tell you if they're not. \n \nEach letter \
    in your guess will be marked as follows: \
            \n x means that the letter does not appear in the answer \
            \n ^ means that the letter is correct and in the correct location \n + means that the letter is correct, but in the wrong location \
            \nGood luck!")
    
    while(True):
        wordListName = input("Enter the name of the file from which to extract the wordlist: ")
        if((os.path.exists(wordListName+".txt")) == False):
            print("File does not exist. Try again!")
        else:
            break
    wordList = open(wordListName+".txt", "r")
    newList = createWordlist(wordList)
    if manualAnswer == None:
        answer = random.choice(newList[0])
    else:
        answer = manualAnswer 
        if ((answer in newList[0]) == False):
            return print("Answer supplied is not legal.")

    i = 0
    attempt = 0
    output = []
    while (attempt <= 6):
        guess = input("Enter your guess (" + str(attempt+1) + "): ")
        if ((guess in newList[0]) == False):
            print("Guess must be a 5-letter word in the wordlist. Try again!")
        else:
            while i < len(answer):
                if (answer[i] == guess[i]):
                    output.append("^")
                elif(BinarySearch(answer, guess[i])):
                    output.append("+")
                elif(guess[i] in answer): #Catches when the binary function fails
                    output.append("+")
                else:
                    output.append("x")
                i += 1
            guess = guess.upper()
            print(guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4])
            print(output[0] + " " + output[1] + " " + output[2] + " " + output[3] + " " + output[4])
            attempt += 1
            i = 0
            output = []
            if (guess == answer.upper()):
                print("CONGRATULATIONS! You win!")
                break
            elif (guess != answer and attempt == 6):
                print("Sorry! The word was "+ answer + ". Better luck next time!")
                break


playWordle("frank")

    








