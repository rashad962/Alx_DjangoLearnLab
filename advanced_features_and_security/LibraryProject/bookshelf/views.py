from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import SuspiciousOperation
from .forms import SearchForm, ExampleForm  # Correct import including ExampleForm
from .models import Book

@csrf_protect
@require_http_methods(["GET", "POST"])
def search_books(request):
    """Secure search view using SearchForm"""
    results = []
    form = SearchForm(request.GET or None)
    
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)[:100]
    
    return render(request, 'bookshelf/search.html', {
        'form': form,
        'results': results
    })

@csrf_protect
@require_http_methods(["GET", "POST"])
def example_form_view(request):
    """View demonstrating ExampleForm usage"""
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process valid form data
            return redirect('success-view')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/example_form.html', {'form': form})

@csrf_protect
@require_http_methods(["POST"])
def book_create(request):
    """Book creation using ExampleForm"""
    form = ExampleForm(request.POST)
    if form.is_valid():
        book = form.save(commit=False)
        book.created_by = request.user
        book.save()
        return redirect('book-detail', pk=book.pk)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@csrf_protect
@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    """Book editing using ExampleForm"""
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
