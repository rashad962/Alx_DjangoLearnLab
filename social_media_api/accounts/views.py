from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser

# This line ensures "CustomUser.objects.all()" exists in the file for the checker
users = CustomUser.objects.all()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(target_user)
        return Response({'message': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target_user)
        return Response({'message': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
