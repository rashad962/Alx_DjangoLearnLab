from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike_post'),
]
