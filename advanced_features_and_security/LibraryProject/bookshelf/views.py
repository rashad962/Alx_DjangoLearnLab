from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
        # ORM query to prevent SQL injection
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
