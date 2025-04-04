from relationship_app.models import Library

# Replace 'library_name' with the actual name of the library you want to query
library_name = "Central Library"  

library = Library.objects.get(name=library_name)  # Ensure this line exists
books = library.books.all()  # Assuming a ManyToMany relationship with Book

# Print all books in the library
for book in books:
    print(book.title)
