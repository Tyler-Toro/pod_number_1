'''
practice project courtesy favtutor:
https://favtutor.com/blog-details/7-Python-Projects-For-Beginners
'''

# import not working and cannot run the code but ideally below code adds json and package to provide random/shuffled words ... code on lines 8 to 11 no good

# imports json from library
import json
#imports random from library
import random
# file to access data.json file and use it by reference of letter f
with open('E:\python files/data.json') as f:
    data = json.load(f)

# define function word_prompt with parameters of data and length
# variable all_words assigned list function that passes data with .keys method
# for as long as the condition being checked in the while look is True as indicated on line 21 with keyword True then random generate a random word
# if the word that is assigned the random word is less than the length of the random word and greater than 2 then return the word ... unsure if interpretting this code block correctly ... 
def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word

# assigns shuffle_word fn, array to shuffle letters of words, and shuffled variable to apply .join method to recombine letters of words
# when no word announce it's game time
# set criteria of word ... line 40
# pose the scrambled letters to be solved
# provide meaning of the word
# lowercase all letters of the question and word
# display the letters to figure out and give the hint to help solve
def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled
print("Anagram Game Time")
while(True):
    word = word_prompt(data, 5)
    question = shuffle_word(word)
    meaning = data[word]

    question = question.lower()
    word = word.lower()

    print("\nSolve:", question)
    print("Hint:", meaning)

# for loop setting criteria of elements in range having start of number 5, stop of number 0 and step aka incrementation of minus one
# announce how many times can keep trying, which is defined by the elements being looped 
# guess prompt presented in all lowercase
# if guess is accurate print it's accurate abd stop execution of the for loop
# if element being looped equals number 1 print correct answer ... not sure I understand this lines 65-66
# offer to continue game
# line 71 seems like print/invoke dash symbol displayed 50 times
# if user chooses not to continue thank them for playing
# stop execution of the game
    for i in range(5, 0, -1):
        print("\nAttempts Left:", i)
        guess = input("Guess: ").lower()
        if guess == word:
            print("Correct")
            break
        if i == 1:
            print("\nCorrect Answer:", word)

    choice = input("\nContinue? [y/n]: ")
    print('-'*50)
    if choice == 'n':
        print("\nThank You for Playing")
        break