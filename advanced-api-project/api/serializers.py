# api/serializers.py

from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']
    
    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
