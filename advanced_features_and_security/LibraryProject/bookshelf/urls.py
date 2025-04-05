from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/search/', views.search_books, name='book-search'),
    path('books/new/', views.book_create, name='book-create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book-edit'),
    path('example-form/', views.example_form_view, name='example-form'),
]
