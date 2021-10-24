# pretty print import for ease of reading output of big code blocks
from pprint import pprint

print('EXERCISE 1: ASSIGNMENT OF A LIST W/NESTED DICTIONARIES')
# You are working on a library management system, here is the list books at the library
books = ['MY OWN WORDS', 'WHITE FRAGILITY', 'THE BODY KEEPS THE SCORE', 'SO YOU WANT TO TALK ABOUT RACE', 'STAMPED FROM THE BEGINNING', 'JUST MERCY', 'BORN A CRIME',
         'THE WARMTH OF OTHER SUNS', 'THE COLOR OF LAW', 'THE NEW JIM CROW', 'THE TRUTHS WE HOLD', 'SAPIENS', 'BRAIDING SWEETGRASS', "MY GRANDMOTHER'S HANDS", 'ON TYRANNY']

# 1.0
print('EXERCISE 1.0: ARTICULATING ASSIGNMENT DATATYPES')
# What data type is the object 'books'? How do you know?
# Books is object type list. I know because I checked with type(). Also, it has hard brackets ([]) around the books content. In other words, the assignment of variable books is to an object of datatype list
print(type(books))
print()

# 1.1
print('EXERCISE 1.1: CREATING AVAILABLE BOOKS FN')
# Create a function 'available_books' to print the books list
# Parameters: Not needed for this function
# Return: Not needed for this function
# def defines variable available_books as a function ... lines 20 and 21 follow basic function syntax
def available_books():
    print(books) 

# 1.2
print('EXERCISE 1.2: INVOKING AVAILABLE BOOKS FN')
# Run the 'available_books' function
# line 26 invokes/calls/runs the defined function available_books ... and the following print() is to add an empty space between this print output and next printed content
available_books()
print()

# 1.3
print('EXERCISE 1.3: CREATING CHECK OUT FN')
# Create a function 'check_out' that removes a book from the books list
# Parameters: book (string)
# Return: Not needed for this function
# seemingly straight forward following basic syntax with exception of adding .remove method to books variable to allow a specified item to be taken out of the list books is assigned to
def check_out(lst):
    # print(available_books.remove(books[7]))
    books.remove(lst)

# 1.4
print('EXERCISE 1.4: IMPLEMENTING CHECK OUT FN')
# Check out 'SAPIENS' using the check_out function
check_out("SAPIENS")
check_out('THE WARMTH OF OTHER SUNS')
check_out('THE BODY KEEPS THE SCORE')

# Bonus: Run available_books function again to see if the book was checked out
print('BONUS: INVOKING AVAILABLE BOOKS FN PER CHECKED OUT BOOK(S)')
# pprint() - not print() - to format output for ease of reading 
# important to invoke correct function for proper results
pprint(books)
available_books()
print()

# 1.5
print('EXERCISE 1.5: CREATING CHECK IN FN')
# Create a function 'check_in' that adds a book to the books list
# Parameters: book (string)
# Return: Not needed for this function
# defined function check_in with a parameter allows for putting back into the list books previously removed - both times using the string representation of the books
def check_in(lst2):
    books.append(lst2)

# 1.6
print('EXERCISE 1.6: CHECKING IN BOOK(S)')
# Check in 'SAPIENS' using the check_in function
check_in("SAPIENS")
check_in('THE WARMTH OF OTHER SUNS')
check_in('THE BODY KEEPS THE SCORE') 

# Bonus: Run available_books function to see if the book was checked in
print('BONUS: INVOKING AVAILABLE BOOKS FN PER CHECKED IN BOOK(S)')
# again, pprint() for formatted output and remembering to reference the correct function (i.e. available_books) when invoking the call to get the correct output
pprint(books)
available_books()
print()

# 1.7
print('EXERCISE 1.7: CREATING SEARCH BY NAME FN')
# Create a function 'search_by_name' that prints 'Available' if exists in books list, 'Not Available' if it doesn't.
# Parameters: book (string)
# Return: Not needed for this function
# use of base defined function with if else 
def search_by_name(lst3):
    # if lst3 == available_books:
    if lst3 in books:
        print('Available')
    else:
        print('Not Available')

# 1.8
print('EXERCISE 1.8: SEARCHING SPECIFIC BOOK TITLE')
# Search for the book 'JUST MERCY'
# still using string parameter to call/pass through titles of books
search_by_name('JUST MERCY')
search_by_name('UNTO THESE SORDID TRUTHS')
print()

print('EXERCISE 2: BOOKS W/DETAILS LIST OF NESTED DICTIONARIES')
# Here's the same list of books, with additional details
# intimidating at first glance. still, variable books_with_details is assigned a list of several dictionaries one layer in with duplicate keys paired with unique values. error(s) not thrown because no duplicate keys in a single dictionary - separate dictionaries makes using the same key names error free 
books_with_details = [
    {
        'title': 'MY OWN WORDS',
        'author': 'Ruth Bader Ginsburg with Mary Hartnett and Wendy W Williams',
        'description': 'A collection of articles and speeches by the Supreme Court justice.'
    },
    {
        'title': 'WHITE FRAGILITY',
        'author': 'Robin DiAngelo',
        'description': 'Historical and cultural analyses on what causes defensive moves by white people and how this inhibits cross-racial dialogue.'
    },
    {
        'title': 'THE BODY KEEPS THE SCORE',
        'author': 'Bessel van der Kolk',
        'description': 'How trauma affects the body and mind, and innovative treatments for recovery.'
    },
    {
        'title': 'SO YOU WANT TO TALK ABOUT RACE',
        'author': 'Ijeoma Oluo',
        'description': 'A look at the contemporary racial landscape of the United States.'
    },
    {
        'title': 'STAMPED FROM THE BEGINNING',
        'author': 'Ibram X Kendi',
        'description': 'Winner of the 2016 National Book Award for nonfiction. A look at anti-Black racist ideas and their effect on the course of American history.'
    },
    {
        'title': 'JUST MERCY',
        'author': 'Bryan Stevenson',
        'description': 'A civil rights lawyer and MacArthur grant recipient’s memoir of his decades of work to free innocent people condemned to death.'
    },
    {
        'title': 'BORN A CRIME',
        'author': 'Trevor Noah',
        'description': 'A memoir about growing up biracial in apartheid South Africa by the host of “The Daily Show.”'
    },
    {
        'title': 'THE WARMTH OF OTHER SUNS',
        'author': 'Isabel Wilkerson',
        'description': 'An account of the Great Migration of 1915-70, in which six million African-Americans abandoned the South.'
    },
    {
        'title': 'THE COLOR OF LAW',
        'author': 'Richard Rothstein',
        'description': 'A case for how the American government abetted racial segregation in metropolitan areas across the country.'
    },
    {
        'title': 'THE NEW JIM CROW',
        'author': 'Michelle Alexander',
        'description': 'A law professor on the “war on drugs” and its role in the disproportionate incarceration of Black men.'
    },
    {
        'title': 'THE TRUTHS WE HOLD',
        'author': 'Kamala Harris',
        'description': 'A memoir by the daughter of immigrants who is now a California senator and the 2020 Democratic candidate for vice president.'
    },
    {
        'title': 'SAPIENS',
        'author': 'Yuval Noah Harari',
        'description': 'How Homo sapiens became Earth’s dominant species.'
    },
    {
        'title': 'BRAIDING SWEETGRASS',
        'author': 'Robin Wall Kimmerer',
        'description': 'A botanist and member of the Citizen Potawatomi Nation espouses having an understanding and appreciation of plants and animals.'
    },
    {
        'title': 'MY GRANDMOTHER\'S HANDS',
        'author': 'Resmaa Menakem',
        'description': 'A therapist who specializes in trauma, body-centered psychotherapy and violence prevention explains racism\'s effect on the body.'
    },
    {
        'title': 'ON TYRANNY',
        'author': 'Timothy Snyder',
        'description': 'Twenty lessons from the 20th century about the course of tyranny.'
    },
    {
        'title': 'THE ROAD TO UNFREEDOM',
        'author': 'Timothy Snyder',
        'description': 'Snyder explores Russian attempts to influence Western democracies and the influence of philosopher Ivan Ilyin on Russian President Vladimir Putin and the Russian Federation in general.'
    }
]
# 2.0
print('EXERCISE 2.0: DATA STRUCTURE OF BOOKS W/DETAILS')
# Describe the structure of the data in books_with_details. What types of data are nested within others? How do you know?
# books_with_details is a list with nested dictionaries
# ran type() to output datatype of assignment to books_with_details followed by type() to output the first object in the list to confirm datatype of dictionary, which is explicitly the same datatype of all the nested dictionaries in the list assigned to books_with_details
print(type(books_with_details))
print(type(books_with_details[0]))
print()

pprint(books_with_details)
print()


# 2.1
print('EXERCISE 2.1: CREATING COUNT BOOKS FN')
# Create a function 'count_books' that returns the number of books in the books_with_details list
# Parameters: Not needed for this function
# Return: number of books (integer)
# use of basic defined function syntax with return to store value to be outputted and len to output the number of items in the variable being passed as a second-level parameter
def count_books():
    return len(books_with_details)

# 2.2
print('EXERCISE 2.2: INVOKING COUNT BOOKS FN')
# Check the number of books available in the books list using the count_books function
# basic code structure to invoke the fn count_books
print(count_books())
print()

# 2.3
print('EXERCISE 2.3: CREATING SEARCH BY AUTHOR FN')
# Create a function 'search_by_author' that returns the titles of books by an author
# Parameters - author (string)
# Return - author's books (list of strings)
# # Hint - You will need a for loop, if statement, .append() for this solution!
def search_by_author(lst4):
    author_titles = []
    for author in books_with_details:
        if lst4 == author['author']:
            author_titles.append(author['title'])
        # if search_by_author != author:
        # if search_by_author != books_with_details[author]['author']:
            # search_by_author == 'Author Unknown'
            # print('Author Unknown')
        else:
            print('Author Unknown')
    return author_titles
   
print(search_by_author('Resmaa Menakem'))
print()


def search_by_author(str):
    author_titles = []
    for i in books_with_details:
        if str == i['author']:
            author_titles.append(i['title'])
            #print(title)
        else:
            print('No Such Author Here')
    return author_titles

print(search_by_author('Michelle Alexander'))
print()

# 2.4
print('EXERCISE 2.4: INVOKING SEARCH BY AUTHOR FN')
# Search for book titles by the author 'Timothy Snyder' using function search_by_author
print(search_by_author('Timothy Snyder'))