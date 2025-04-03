import django
import os

# Setup Django environment (if running outside Django shell)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return []

def list_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return []

def retrieve_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.librarian
    return None

# Sample function calls
if __name__ == "__main__":
    print("Books by author:", list(query_books_by_author("J.K. Rowling")))
    print("Books in library:", list(list_books_in_library("Central Library")))
    print("Librarian for library:", retrieve_librarian_for_library("Central Library"))
