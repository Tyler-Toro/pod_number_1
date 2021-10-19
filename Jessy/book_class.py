class Booklist():
	def __init__(self):
		# initialized the book attribute
		self.books=[]



	def add(self, title, author):
		# creating an empty dic. 
		book = {}
		# assigning key/value pairs inside the dictionaries.
		book['title'] = title
		book['author'] = author
		# appending the book dictionary to the books attribute in line 4
		self.books.append(book)



	def count_books(self):
		# have it count my list. Had to identify wheere my list is located.
		return len(self.books)
		

	def remove_title(self, title):
		for book in self.books:
			if (book['title'] == title):
				self.books.remove(book)


	def display_titles(self):
		alphabetized= []
		for book in self.books:
			alphabetized.append(book['title'])
		alphabetized.sort()
		print(alphabetized)

		pass 

