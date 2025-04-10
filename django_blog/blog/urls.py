from django.urls import path
from .views import (
    post_detail,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
