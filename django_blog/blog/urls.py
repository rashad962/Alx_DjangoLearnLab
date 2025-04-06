# urls.py

from django.urls import path
from .views import (
    PostListView, PostDetailView, CommentCreateView, 
    CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # Add the comment creation URL under a specific post
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    # Add the comment update URL using the comment pk
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    # Add the comment delete URL using the comment pk
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
