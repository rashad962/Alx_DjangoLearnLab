from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn', 'available_copies']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 2100}),
            'isbn': forms.TextInput(attrs={'pattern': '[0-9]{13}'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
