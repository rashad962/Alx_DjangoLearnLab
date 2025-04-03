```python
from bookshelf.models import Book

# Retrieve the book by its original title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
# Expected Output: Nineteen Eighty-Four
