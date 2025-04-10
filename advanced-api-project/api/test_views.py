from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookApiTests(APITestCase):
    
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2023-01-01',
        }

    def test_create_book_authenticated(self):
        """Test creating a new book with authentication"""
        self.client.login(username='testuser', password='password')
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book"""
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_books(self):
        """Test retrieving a list of books"""
        Book.objects.create(**self.book_data)
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_update_book(self):
        """Test updating a book with authentication"""
        book = Book.objects.create(**self.book_data)
        update_data = {'title': 'Updated Book'}
        self.client.login(username='testuser', password='password')
        response = self.client.put(f'/api/books/{book.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], update_data['title'])
    
    def test_update_book_unauthenticated(self):
        """Test that unauthenticated users cannot update a book"""
        book = Book.objects.create(**self.book_data)
        update_data = {'title': 'Updated Book'}
        response = self.client.put(f'/api/books/{book.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete_book(self):
        """Test deleting a book with authentication"""
        book = Book.objects.create(**self.book_data)
        self.client.login(username='testuser', password='password')
        response = self.client.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())
    
    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete a book"""
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_books(self):
        """Test the filtering functionality of books"""
        book1 = Book.objects.create(title="Book One", author="Author A")
        book2 = Book.objects.create(title="Book Two", author="Author B")
        response = self.client.get('/api/books/?author=Author A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books(self):
        """Test the search functionality for books"""
        book1 = Book.objects.create(title="Django Basics", author="Author A")
        book2 = Book.objects.create(title="Advanced Django", author="Author B")
        response = self.client.get('/api/books/?search=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_order_books(self):
        """Test the ordering functionality for books"""
        book1 = Book.objects.create(title="Django Basics", author="Author A")
        book2 = Book.objects.create(title="Advanced Django", author="Author B")
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Advanced Django')
