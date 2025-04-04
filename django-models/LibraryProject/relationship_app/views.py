# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import Library model here

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View to Display Library Details
class LibraryDetailView(DetailView):
    model = Library  # Set the model to Library to show details of a specific library
    template_name = "relationship_app/library_detail.html"  # Template for the class-based view
    context_object_name = "library"  # The context variable passed to the template
