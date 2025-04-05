from django import forms
from django.core.validators import validate_slug
from django.utils.html import escape

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        validators=[validate_slug],  # Restrict input to safe characters
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'xss_protected': True  # Custom attribute for documentation
        })
    )

    def clean_query(self):
        """Additional sanitization"""
        query = self.cleaned_data['query']
        return escape(query)  # HTML escape the input