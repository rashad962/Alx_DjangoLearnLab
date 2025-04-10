from django.urls import path
from . import views

urlpatterns = [
    # URL for viewing individual post details (with comments)
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # URL for creating a new comment under a specific post
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),

    # URL for editing an existing comment
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),

    # URL for deleting a comment
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
