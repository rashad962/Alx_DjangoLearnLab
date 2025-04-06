# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View to list and create books
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
