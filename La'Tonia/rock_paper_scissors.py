'''
practice project courtesy favtutor:
https://favtutor.com/blog-details/7-Python-Projects-For-Beginners
'''
# GENERAL NOTES: Type in terminal/on command line control letter c to stop game 

# imports random integer from random library
from random import randint

# assign choice_options variable to list of options user can pick
choice_options = ["rock", "paper", "scissors"]

# assigns a random play to the opponent of the user/opponent is artificial_intelli_simul aka the computer
artificial_intelli_simul = choice_options[randint(0,2)]

# assign user to keyword boolean value False
user = False

# while loop that may or not continuously loop through various combinations for the game as outlined below ... change assignment of user to True prn
while user == False:
    user = input("Type rock, paper, or scissors? ")
    if user == artificial_intelli_simul:
        print("Tie")
    elif user == "rock":
        if artificial_intelli_simul == "paper":
            print("You lose", artificial_intelli_simul, "covers", user)
        else:
            print("You win", user, "smashes", artificial_intelli_simul)
    elif user == "paper":
        if artificial_intelli_simul == "scissors":
                print("You lose", artificial_intelli_simul, "cut", user)
        else:
                print("You win", user, "covers", artificial_intelli_simul)
    elif user == "scissors":
        if artificial_intelli_simul == "rock":
            print("You lose .. .", artificial_intelli_simul, "smashes", user)
        else:
            print("You win", user, "cut", artificial_intelli_simul)
    else:
        print("Invalid Play - Please Check Your Spelling")

# unsure reasons user must be set to True versus False when only False seems to work
    user = False
# opponent aka computer program user plays against is assigned value of options (represented here in a list) set to criteria of random integer with parameters of 0 and 2 ... this could be worded differently for better understanding of what is happening in the code
    artificial_intelli_simul = choice_options[randint(0,2)]
