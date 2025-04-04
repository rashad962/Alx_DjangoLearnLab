from relationship_app.models import Author, Book

# Replace 'author_name' with the actual name of the author you want to query
author_name = "George Orwell"  

# Get the author instance
author = Author.objects.get(name=author_name)  # Ensure this line exists

# Query all books by this author
books_by_author = Book.objects.filter(author=author)  # Ensure this line exists

# Print all books by the author
for book in books_by_author:
    print(book.title)
