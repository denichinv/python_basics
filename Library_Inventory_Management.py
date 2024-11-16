class Books:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        search_title = lambda book: book.title.lower() == title.lower()  # Fixed comparison
        return list(filter(search_title, self.books))

    def search_by_author(self, author):
        search_author = lambda book: book.author.lower() == author.lower()  # Fixed comparison
        return list(filter(search_author, self.books))

    def update_availability(self, title, available):
        update_book = lambda book: setattr(book, 'available', available) if book.title.lower() == title.lower() else None
        list(map(update_book, self.books))


book1 = Books("Python Programming", "John Smith")
book2 = Books("Data Structures and Algorithms", "Jane Doe")
book3 = Books("Web Development with Python", "John Smith")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Books with title 'Python Programming':")
for book in library.search_by_title("Python Programming"):
    print(f"- {book.title} by {book.author}")

print("\nBooks by author 'John Smith':")
for book in library.search_by_author("John Smith"):
    print(f"- {book.title} by {book.author}")

library.update_availability("Data Structures and Algorithms", False)

print("\nAvailability of 'Data Structures and Algorithms':")
for book in library.search_by_title("Data Structures and Algorithms"):
    print(f"- {book.title} is {'available' if book.available else 'not available'}")