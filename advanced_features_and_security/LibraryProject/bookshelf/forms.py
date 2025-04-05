from django import forms
from django.core.validators import validate_slug
from django.utils.html import escape
from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        validators=[validate_slug],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'xss_protected': True
        })
    )

    def clean_query(self):
        query = self.cleaned_data['query']
        return escape(query)

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'is_available']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'data-validation': 'required'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'data-validation': 'required'
            }),
            'published_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if '<script>' in title.lower():
            raise forms.ValidationError("Invalid characters in title")
        return escape(title)
