from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"  

author = Author.objects.get(name=author_name)  # Required line
books_by_author = Book.objects.filter(author=author)  # Required line

# Print the results
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# Query all books in a specific library
library_name = "Central Library"  

library = Library.objects.get(name=library_name)  # Required line
books_in_library = library.books.all()  # Required line

# Print the results
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=library)  # Required line

# Print the librarian's name
print(f"\nLibrarian of {library_name}: {librarian.name}")
