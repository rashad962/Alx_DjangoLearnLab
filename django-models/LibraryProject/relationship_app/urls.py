from django.urls import path
<<<<<<< HEAD
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
=======
from .views import list_books, LibraryDetailView  # Import both views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for class-based view
>>>>>>> 092f12d7c74663fce420e898c048019cd45c03eb
]
