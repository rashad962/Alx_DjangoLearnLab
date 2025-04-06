from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # List all books or create a new book (GET/POST)
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Retrieve, update, or delete a specific book (GET/PUT/DELETE)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Create a new book (POST)
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # Update a specific book (PUT)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    
    # Delete a specific book (DELETE)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
