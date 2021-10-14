class Booklist():
	def __init__(self):
		self.books = []


	def add(self, title, author):
		self.books.append({'title': title, 'author' : author})

	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		for book in self.books:
			if (book['title'] == title):
				self.books.remove(book)

	def display_titles(self):
		alphabetically = sorted(self.books)

