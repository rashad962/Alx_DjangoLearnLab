from django.urls import path
from . import views

urlpatterns = [
    # URL for viewing individual post details
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # URLs for CRUD operations on comments under a post
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Other URLs related to the blog (e.g., list of posts, etc.)
]
