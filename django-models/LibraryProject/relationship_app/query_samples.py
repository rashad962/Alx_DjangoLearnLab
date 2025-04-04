from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    return author.books.all() if author else []

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.books.all() if library else []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.librarian if library else None

# Example Usage (for testing in Django shell)
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("City Library"))
    print(get_librarian_for_library("City Library"))
