from django.urls import path
from . import views

urlpatterns = [
    # List all books (GET) or create a new book (POST)
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # Retrieve, update or delete a specific book (GET / PUT / DELETE)
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]
