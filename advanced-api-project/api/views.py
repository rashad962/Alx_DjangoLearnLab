from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend  # Correct import for filtering
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Book
from .serializers import BookSerializer
import django_filters

# Create a filter class for the Book model
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search on title
    author = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search on author
    publication_year = django_filters.NumberFilter()  # Filter by publication year
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ListView: List all books with filtering, searching, and ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users, authenticated users can create
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Add filter backends
    filterset_class = BookFilter  # Use the custom BookFilter for filtering
    search_fields = ['title', 'author']  # Allow search on title and author fields
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication_year
    ordering = ['title']  # Default ordering (by title)

# DetailView: Retrieve a single book by ID, and allow authenticated users to update or delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users, authenticated users can update/delete

# CreateView: Only authenticated users can create new books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# UpdateView: Only authenticated users can update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# DeleteView: Only authenticated users can delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books
