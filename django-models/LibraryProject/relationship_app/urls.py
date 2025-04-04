from django.urls import path
from .views import (
    admin_view,
    librarian_view,
    member_view,
    register,
    list_books,
    LibraryDetailView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Role-based URLs
    path('admin/dashboard/', admin_view, name='admin_view'),
    path('librarian/dashboard/', librarian_view, name='librarian_view'),
    path('member/dashboard/', member_view, name='member_view'),
    
    # Existing book URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
