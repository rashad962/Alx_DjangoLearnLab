# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import the models

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View to Display Library Details
class LibraryDetailView(DetailView):
    model = Library  # Use Library model
    template_name = "relationship_app/library_detail.html"  # Template for displaying library details
    context_object_name = "library"  # This will pass the library object to the template as 'library'
