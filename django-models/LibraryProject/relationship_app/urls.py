from django.urls import path
from django.contrib.auth import views as auth_views
from relationship_app.views import (
    list_books,
    add_book,
    edit_book,
    delete_book,
    author_list,
    add_author,
    register
)

urlpatterns = [
    # Book URLs
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
    
    # Author URLs
    path('authors/', author_list, name='author_list'),
    path('authors/add/', add_author, name='add_author'),
    
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
