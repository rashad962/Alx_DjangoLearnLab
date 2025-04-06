from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Prevent a user from following themselves
    if user_to_follow == request.user:
        return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Prevent a user from unfollowing themselves
    if user_to_unfollow == request.user:
        return Response({'detail': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
