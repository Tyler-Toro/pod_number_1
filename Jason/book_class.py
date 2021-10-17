
# my_library
class Booklist():

# Set up the initialization function for class Booklist()
# The function should initialize just 1 attribute, called 'books', as an empty list
# No parameters needed, other than self     

	def __init__(self):
		self.books = []
		
# Define the add() method to add a book to an object of class Booklist
# -The method should take 2 parameters other than self, both strings -- 'title', and 'author'
# -The method should make a book variable as a dictionary with two key/value pairs for title/author
# -Then, the method should append this book to books attribute of the the Booklist object  - i.e. self.books.append(book)

	def add(self, title, author):
		book = {'title' : title , 'author' : author}
		self.books.append(book)
	
		
# Part #3: 
# Define the count_books() method to get the number of books in an object of class Booklist
# -the method only needs the self parameter
# -the method should return an integer that is the length of the list stored in the books attribute

	def count_books(self):
		return len(self.books)
		
# Part #4: 
# Define the remove_title() method which will remove a book by its title from an object of class Booklist
# -the method should take the self parameter, plus an additional paramter 'title' (a string for the title of the book to remove)
# -the method should remove any books matching the input title from the Booklist
# -it does not need to return anything
		
	def remove_title(self, title, author):
		book = {'title' : title , 'author' : author }
		self.books.remove(book)
		
		
# Instantiate another object of class Booklist called nyt_bestsellers
# Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
# You can find NYT books here: https://www.nytimes.com/books/best-sellers/
# Then, print out the books attribute of nyt_bestsellers




# Define a display_titles() method to display all the titles of the books in an object of class Booklist
# The titles should be displayed in alphabetical order!
# -The method requires no parameters other than self
# HINT: there's a quick way to sort a list in alphabetical order
# Once you have completed this method, test it out on both my_library and nyt_bestsellers


	def display_titles(self):
		empty_list = []
		for i in self.books:
			empty_list.append(i['title'])
		empty_list.sort()
		print(empty_list)
			
		
		

	


# Once you have finished the method, count the books in my_library and print out the result

# Part #5:
# Instantiate another object of class Booklist called nyt_bestsellers
# Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
# You can find NYT books here: https://www.nytimes.com/books/best-sellers/