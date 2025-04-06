from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for liking a post
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    
    # URL pattern for unliking a post
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike_post'),
]
