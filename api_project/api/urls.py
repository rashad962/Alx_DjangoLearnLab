# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
