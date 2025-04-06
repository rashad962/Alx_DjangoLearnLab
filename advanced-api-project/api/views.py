# api/views.py

# List all books and allow creation (GET /books/)
class BookList(generics.ListCreateAPIView):
    """
    List all books and allow authenticated users to create new books.
    Permission: AllowAny (read access) or IsAuthenticated (create access).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Read-only access for all, create access for authenticated users

# Retrieve, update, and delete a book by ID (GET /books/<int:pk>/)
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific book by its ID.
    Permission: AllowAny (read access) or IsAuthenticated (update/delete access).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Read access for all, update/delete for authenticated users

# Create a new book (POST /books/create/)
class BookCreate(generics.CreateAPIView):
    """
    Create a new book. Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

# Update an existing book (PUT /books/<int:pk>/update/)
class BookUpdate(generics.UpdateAPIView):
    """
    Update an existing book. Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

# Delete a book (DELETE /books/<int:pk>/delete/)
class BookDelete(generics.DestroyAPIView):
    """
    Delete a book. Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book
