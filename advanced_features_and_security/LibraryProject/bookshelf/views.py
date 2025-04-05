from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from .forms import SearchForm, ExampleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import SuspiciousOperation
from .forms import SearchForm, ExampleForm  # Added ExampleForm import
from .models import Book

@csrf_protect
@require_http_methods(["GET", "POST"])
def search_books(request):
    """Safe search implementation with parameterized queries"""
    results = []
    form = SearchForm(request.GET or None)
    
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)[:100]
    
    return render(request, 'bookshelf/search.html', {
        'form': form,
        'results': results
    })

@require_http_methods(["GET", "POST"])
@csrf_protect
def book_create(request):
    """Secure book creation view using ExampleForm"""
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/book_form.html', {'form': form})

@require_http_methods(["GET", "POST"])
@csrf_protect
def book_edit(request, pk):
    """Secure book editing view using ExampleForm"""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.last_modified_by = request.user
            book.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = ExampleForm(instance=book)
    
    return render(request, 'bookshelf/book_form.html', {'form': form})

def csrf_failure(request, reason=""):
    """Custom CSRF failure view"""
    return render(request, 'bookshelf/csrf_failure.html', status=403)