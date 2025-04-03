```python
from bookshelf.models import Book

# Retrieve the book by its updated title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Verify deletion by checking if any books exist
books = Book.objects.all()
print(list(books))
# Expected Output: []
