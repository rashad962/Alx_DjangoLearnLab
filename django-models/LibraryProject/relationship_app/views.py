from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Explicitly importing Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library  # Now properly using the imported Library model
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
