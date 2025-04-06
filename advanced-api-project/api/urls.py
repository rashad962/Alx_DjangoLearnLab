from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),  # List all books and create a book
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),  # Retrieve, update, or delete a book by ID
    path('books/create/', views.BookCreate.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),  # Update a book by ID
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),  # Delete a book by ID
]
