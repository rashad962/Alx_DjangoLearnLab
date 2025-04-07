from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike_post'),
    path('feed/', views.FeedView.as_view(), name='feed'),
]
