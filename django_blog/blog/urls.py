from django.urls import path
from .views import (
    post_detail,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # Post detail view
    path('post/<int:pk>/', post_detail, name='post_detail'),
    
    # Comment URLs with more intuitive structure
    path('post/<int:pk>/comments/new/', 
         CommentCreateView.as_view(), 
         name='comment_create'),
    
    path('comment/<int:pk>/update/', 
         CommentUpdateView.as_view(), 
         name='comment_update'),
    
    path('comment/<int:pk>/delete/', 
         CommentDeleteView.as_view(), 
         name='comment_delete'),
]
