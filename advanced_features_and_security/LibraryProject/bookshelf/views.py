from .forms import BookSearchForm, ExampleForm
from .forms import ExampleForm
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm, ExampleForm  # ✅ Import both forms

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(f"Received from form - Name: {name}, Email: {email}")
            return render(request, 'bookshelf/form_example.html', {
                'form': ExampleForm(), 'success': True
            })
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
