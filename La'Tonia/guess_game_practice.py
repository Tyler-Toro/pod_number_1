# practice project courtesy favtutor:
# https://favtutor.com/blog-details/7-Python-Projects-For-Beginners

# adds random package to the code to generate unknown numbers
import random
# creates variable named number assigned to random package with random integer method containing parameters for start and end numbers
number = random.randint(1, 10)

# variable player_name assigned to input function to get user input for personalized greeting later
player_name = input("Good Day, Please Enter Your Name. ")
# variable number_of_guesses assigned to zero as baseline from which the user can input guesses without throwing an error
number_of_guesses = 0
# outputs personalized greeting from previous input of name and concatenation to create a sentence stating I am guessing a number and to get the user to enter their guess
print('Fabulous! ' + player_name + ' - I\'m guessing a number between 1 and 10: ')

# while loop with if statements and else statement to track user input, compare against the randomly generate number, and output if guess is below, above, or same as randomly generated number
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your Guess is Too Low')
    if guess > number:
        print('Your Guess is Too High')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' attempts.')
# outputs update to user that they did not guess the number and tells the user what the number was    
else:
    print('You did not guess the number. The number was ' + str(number))