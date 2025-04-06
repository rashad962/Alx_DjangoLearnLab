from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_books, name='book_list'),
]
