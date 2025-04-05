from django.urls import path
from .views import (
    BookListView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView,
    book_detail
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]