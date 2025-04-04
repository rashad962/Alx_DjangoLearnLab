from django.urls import path
from . import views

urlpatterns = [
    # Book URLs
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    
    # Author URLs
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.add_author, name='add_author'),
    
    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]
