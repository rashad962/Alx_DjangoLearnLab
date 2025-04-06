from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('tags/<str:tag_name>/', views.tagged_posts, name='tag-detail'),
]
