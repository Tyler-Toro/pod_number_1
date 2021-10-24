class Booklist():
	def __init__(self):
		self.books = []
		
	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		# book = {'title': title, 'author', author}
		self.books.append(book)
		# [].append({})

	def count_books(self):
		book_num = int(len(self.books))
		return book_num
		# line 14 is my equivalent of the alternative on line 17
		# return len(self.books)

	def remove_title(self, title):
		for book in self.books:
			if (book['title'] == title):
				self.books.remove(book)
		# initial iterations below		
		# self.books[title] = title
		# self.title = 'title'
		# self.books.remove(title)
		# self.books.remove('title')
		# self.books.remove(title)

	def nyt_bestsellers(self, bs1, bs2):
		self.nyt_bestsellers = []
		self.bs1 = str(bs1)
		self.bs2 = str(bs2)
	
	# below code goes in challenge file
	# nyt_bestsellers = Booklist()

	def display_titles(self):
		titles_list = []
		for title in self.books:
			# titles_list.append(Booklist['titles'])
			titles_list.append(title['title'])
		titles_list.sort()
		print(titles_list)
