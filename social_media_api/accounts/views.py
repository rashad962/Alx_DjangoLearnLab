from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound

User = get_user_model()  # Use your custom user model

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id, *args, **kwargs):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Prevent following oneself
        if user_to_follow == request.user:
            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Add user to the following list
        request.user.following.add(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id, *args, **kwargs):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Prevent unfollowing oneself
        if user_to_unfollow == request.user:
            return Response({'detail': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Remove user from the following list
        request.user.following.remove(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
