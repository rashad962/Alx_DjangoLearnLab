from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    Supports filtering, searching, and ordering.
    
    Filtering Examples:
    - /api/books/?title=The Great Gatsby
    - /api/books/?author__icontains=Tolkien
    - /api/books/?publication_year__gte=2020
    
    Searching Examples:
    - /api/books/?search=fantasy (searches title, author, description)
    
    Ordering Examples:
    - /api/books/?ordering=title (ascending)
    - /api/books/?ordering=-publication_year (descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Detailed filtering configuration
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'author': ['exact', 'icontains'],
        'publication_year': ['exact', 'gte', 'lte'],
        'price': ['exact', 'gte', 'lte'],
        'genre': ['exact'],
    }
    
    # Searchable fields
    search_fields = ['title', 'author', 'description']
    
    # Ordering options
    ordering_fields = ['title', 'author', 'publication_year', 'price', 'created_at']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book instance.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book instance.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book instance.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
