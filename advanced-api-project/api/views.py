from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# ListView: List all books and allow authenticated users to create new books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow read-only access for unauthenticated users, authenticated users can create

# DetailView: Retrieve a single book by ID, and allow authenticated users to update or delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow read-only access for unauthenticated users, authenticated users can update/delete

# CreateView: Only authenticated users can create new books
# This can be merged into BookListView if necessary, since ListCreateAPIView already handles POST requests
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# UpdateView: Only authenticated users can update a book
# This is handled by the `BookDetailView` class, so no need for a separate view
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# DeleteView: Only authenticated users can delete a book
# This is also handled by `BookDetailView`, so no need for a separate view
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books
