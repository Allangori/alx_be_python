class Library:
    """A class representing a library which holds a collection of books."""
    
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f'You have checked out "{title}".')
                return True
        print(f'Sorry, "{title}" is not available for checkout.')
        return False

    def return_book(self, title):
        """Returns a book to the library, making it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f'You have returned "{title}".')
                return True
        print(f'Cannot return "{title}". It was not checked out.')
        return False

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f'- {book.title} by {book.author}')
        else:
            print("No books are currently available.")
