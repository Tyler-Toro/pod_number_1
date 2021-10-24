'''
practice project courtesy favtutor:
https://favtutor.com/blog-details/7-Python-Projects-For-Beginners
'''

# GENERAL NOTES: This was solid practice for muscle memory, reiteration of loops, lists, functions, etc. and basic python design skills . .. However, overall design lacks essential functionality - such as clearly noting to user that the word is completely random ... I'm unsure reasons there is a list of character names ...  

# imports random library
import random
# defines hangman function
def hangman():

# assigns variable named word value of random with choice method passing list of strings
    word = random.choice(["ironman", "hulk", "thor", "captainamerica", "clint", "loki", "avengers", "nick", "phil", "maria"])
# assigns string of letters users can input
# sets 10 as number of tries
# initializes guesses made to start with empty string that'll store value in succession of guesses 
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

# while loop with length function greater than 0
# variable main assigned empty screen
# initializes variable missed at number 0
    while len(word) > 0:
        main = ""
        missed = 0

# for loop to check letters in a word
# if letter found add letter to variable main
# otherwise assign variable main with underscore symbol to create empty spaces where letters go plus empty space/string
# when variable main equals word guessed display win message
# then stop execution of the loop
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
            if main == word:
                print(main)
                print("You Win")
                break
# display message for user to guess word
# unsure what is happening here with variable main
# variable guess holds value of what user inputs
            print("Guess Word:", main)
            guess = input()
# when user guess is in letters considered value assign value of guess that was made to guess that was made plus the actual user guess
# otherwise display message for user to enter a valid character
# variable guess holds value of aka is assigned value of the user input
            if guess in validLetters:
                guessmade = guessmade + guess
            else:
                print("Enter Valid Character")
                guess = input()
# code to count down tries per user input and build the victim bit by bit until 10 tries done
            if guess not in word:
                turns = turns - 1
                if turns == 9:
                    print("9 turns left")
                    print(" ---------- ")
                if turns == 8:
                    print("8 turns left")
                    print(" ---------- ")
                    print("      0     ")
                if turns == 7:
                    print("7 turns left")
                    print(" ---------- ")
                    print("      0     ")
                    print("      |     ")
                if turns == 6:
                    print("6 turns left")
                    print(" ---------- ")
                    print("      0     ")
                    print("      |     ")
                    print("      /     ")
                if turns == 5:
                    print("5 turns left")
                    print(" ---------- ")
                    print("      0     ")
                    print("      |     ")
                    print("     / \    ")
                if turns == 4:
                    print("4 turns left")
                    print(" ---------- ")
                    print("    \ 0     ")
                    print("      |     ")
                    print("     / \    ")
                if turns == 3:
                    print("3 turns left")
                    print(" ---------- ")
                    print("    \ 0 /   ")
                    print("      |     ")
                    print("     / \    ")
                if turns == 2:
                    print("2 turns left")
                    print(" ---------- ")
                    print("    \ 0 /|  ")
                    print("      |     ")
                    print("     / \    ")
                if turns == 1:
                    print("1 turn left")
                    print("Last Breaths!")
                    print(" ---------- ")
                    print("    \ 0_|/  ")
                    print("      |     ")
                    print("     / \    ")
                if turns == 0:
                    print("You Lose")
                    print("A Kind Person Has Died - Try Harder Next Time")
                    print(" ---------- ")
                    print("      0_|   ")
                    print("     /|\    ")
                    print("     / \    ")
                    break

# variable name assigned value resulting from user input for their name
name = input("Enter Your Name: ")
# display personalized greeting per previous user name input
print("Good Day,", name )
# visual horizontal line break effect/basic design element
print("-------------------")
# show user they have 10 tries to guess the word
print("Guess the word in less than 10 tries.")
# invoke hangman function
hangman()
# print empty line
print()