from django.urls import path
from . import views

urlpatterns = [
    # List all books and create a book (GET / POST)
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # Retrieve, update or delete a specific book (GET / PUT / DELETE)
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # Create a new book (POST /books/create/)
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # Update an existing book (PUT /books/<int:pk>/update/)
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    
    # Delete a book (DELETE /books/<int:pk>/delete/)
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
