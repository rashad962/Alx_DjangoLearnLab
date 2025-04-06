# api/urls.py

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', views.BookViewSet, basename='book_all')

urlpatterns = [
    # Token authentication endpoint
    path('auth-token/', obtain_auth_token, name='api-token-auth'),

    # Other routes
    path('', include(router.urls)),
]
