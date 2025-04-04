<<<<<<< HEAD
# Import necessary modules
=======
# relationship_app/views.py
>>>>>>> 7807924 (vuje)
from django.shortcuts import render
from django.views.generic import DetailView
<<<<<<< HEAD
from .models import Book, Library  # Ensure Library is imported here
=======
from .models import Book, Library  # Import Library model here
>>>>>>> 092f12d7c74663fce420e898c048019cd45c03eb

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View to Display Library Details
class LibraryDetailView(DetailView):
<<<<<<< HEAD
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
=======
    model = Library  # Set the model to Library to show details of a specific library
    template_name = "relationship_app/library_detail.html"  # Template for the class-based view
    context_object_name = "library"  # The context variable passed to the template
>>>>>>> 092f12d7c74663fce420e898c048019cd45c03eb
