from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', views.BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),
]
