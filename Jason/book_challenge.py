# import the Booklist class and corresponding methods
from book_class import *


# Object-oriented book challenge! 

# Your challenge for today is to complete the fill out the missing parts of the Booklist class in book_class.py
# Then, test each method for the class Booklist!

# Hint: all methods for the Booklist class go in the book_class.py script
# This class and the methods are already imported in this script -- test them here for specific cases!


# PART #1. 
# Set up the initialization function for class Booklist()
# The function should initialize just 1 attribute, called 'books', as an empty list
# No parameters needed, other than self
# Then, create an object of class Booklist called 'my_library' in this script.
# Finally, print the books attribute of my_library -- it should be an empty list
# Also, print out the type of my_library to see what you get :) 

print('\nPart 1\n')
my_library = Booklist()
print(my_library.books)
print(type(my_library.books))
print()


# Once you have finished the method, add the following books to your booklist:
# Just Mercy - Bryan Stevenson
# The New Jim Crow - Michelle Alexander
# The Truths We Hold - Kamala Harris
# My Grandmother's Hands - Resmaa Menakem

print('\nPart 2\n')
my_library.add('Just Mercy' , 'Bryan Stevenson')
my_library.add('The New Jim Crow' , 'Michelle Alexander')
my_library.add('The Truths We Hold' , 'Kamala Harris')
my_library.add('My Grandmothers Hands' , 'Resmaa Menakem')
print(my_library.books)
print()


# Once you have finished the method, count the books in my_library and print out the result
# Finally, prinb the books attribute of my_library to make sure your books have been added!
print('\nPart 3\n')
print(my_library.count_books())
print()


# Once you have finished the method, remove 'Just Mercy' from my_library
# Then, print out the books attribute to make sure that book is gone
print('\nPart 4\n')
my_library.remove_title('Just Mercy', 'Bryan Stevenson')
print(my_library.books)
print()



# Instantiate another object of class Booklist called nyt_bestsellers
# Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
# You can find NYT books here: https://www.nytimes.com/books/best-sellers/
# Then, print out the books attribute of nyt_bestsellers


print('\nPart 5\n')
nyt_bestsellers =  Booklist()
nyt_bestsellers.add('Cloud Cukoo Land', 'Anthony Doerr')  
nyt_bestsellers.add('Apples Never Fall', 'Liane Moriarty')
nyt_bestsellers.add('1984', 'George Orwell')
print(nyt_bestsellers.books)
print()




# BONUS Part #6:
# Define a display_titles() method to display all the titles of the books in an object of class Booklist
# The titles should be displayed in alphabetical order!
# -The method requires no parameters other than self
# HINT: there's a quick way to sort a list in alphabetical order
# Once you have completed this method, test it out on both my_library and nyt_bestsellers


print('\nBONUS Part 6\n') 
# my_library = Booklist()
# print(sorted(my_library.books))
# print(sorted(display_titles.my_library))
# print(display_titles.books)

my_library.display_titles()
nyt_bestsellers.display_titles()




