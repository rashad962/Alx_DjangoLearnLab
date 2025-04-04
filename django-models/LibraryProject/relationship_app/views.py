<<<<<<< HEAD
# Import necessary modules
=======
# relationship_app/views.py
>>>>>>> 7807924 (vuje)
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure Library is imported here

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View to Display Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
