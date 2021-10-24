'''
practice project courtesy favtutor:
https://favtutor.com/blog-details/7-Python-Projects-For-Beginners
'''

# import not working and cannot run the code but ideally below code adds json and package to get similar matches from difflib ... filepath on line 9 is no good
import json
from difflib import get_close_matches
with open('E:\python files/data.json') as f:
# variable data assigned json file with load method and letter f as parameter
# not sure what this does
    data = json.load(f)
# seems to translate the word called as parameter in defined translate function
def translate(word):
# changes to lowercase letters
    word = word.lower()
# looks for word in data then from data variable stores value of word on line 19
    if word in data:
        return data[word]
# looks for word in data with word title method then returns word title on line 22
    elif word.title() in data:
        return data[word.title()]
# changes to uppercase letters
    elif word.upper() in data:
# looks for word in data targeting the word with upper method ?
        return data[word.upper()]
# unsuure what is happening here - see length function . ..
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Want to find %s" %get_close_matches(word, data.keys())[0])
# user input re: whether want to find word and if yes looks for similar matches but if no states search done wrong but then gives another chance to choose to seek word ... and once those conditions checked then defaults to statement that search done wrong ... lines 31 through 39 ... ending execution of the function
        decide = input("Press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Incorrect search. Please try again.")
        else:
            return("Incorrect input. Please enter y or n.")
    else:
        print("Incorrect search. Please try again.")

# word variable assigned to user input of the word to search 
# then output variable assigned to translate inputted word 
# and check if the output is equal to a list 
# printing an item from the output variable for an item in the output variable 
# otherwise printing the output, which has the value of a word translated
word = input("Enter word to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

    