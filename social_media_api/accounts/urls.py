from django.urls import path
from .views import FollowUser, UnfollowUser

urlpatterns = [
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow_user'),
]
