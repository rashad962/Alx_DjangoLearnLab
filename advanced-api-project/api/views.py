# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# List all books (GET /books/)
class BookList(generics.ListCreateAPIView):
    """
    List all books and allow authenticated users to create new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow read-only access for unauthenticated users, authenticated users can create

# Retrieve a single book by ID (GET /books/<int:pk>/)
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow read-only access for unauthenticated users, authenticated users can update/delete

# Create a new book (POST /books/)
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
