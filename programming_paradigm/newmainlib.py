# main.py

from library import Library
from book import Book

def main():
    # Create a library instance
    library = Library()

    # Add some books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List available books
    library.list_available_books()

    # Check out a book
    library.check_out_book("1984")

    # Try to check out the same book again
    library.check_out_book("1984")

    # Return the book
    library.return_book("1984")

    # List available books again
    library.list_available_books()

    # Return a book that is not checked out
    library.return_book("To Kill a Mockingbird")

if __name__ == "__main__":
    main()
