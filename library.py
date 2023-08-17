class Book:
    def _init_(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")


# Example usage:
library = Library()

book1 = Book("Harry Potter", "J.K. Rowling", "Available")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Unavailable")

library.add_book(book1)
library.add_book(book2)

library.display_books()

found_book = library.search_book("Harry Potter")
if found_book:
 print(f"Book found: Title: {found_book.title}, Author: {found_book.author}")
else:
    print("Book not found.")