# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', views.BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router URLs for BookViewSet (CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
