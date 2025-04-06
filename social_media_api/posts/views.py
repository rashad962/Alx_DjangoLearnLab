from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from .serializers import PostSerializer

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        # Fetch the post object or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Optionally: Create a notification (if notifications are implemented)
        # Notification.objects.create(
        #     recipient=post.author,
        #     actor=request.user,
        #     verb='liked your post',
        #     target=post
        # )

        return Response({'detail': 'Post liked successfully!'}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        # Fetch the post object or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Delete the like
        like.delete()

        # Optionally: Create a notification for unliking (if notifications are implemented)
        # Notification.objects.create(
        #     recipient=post.author,
        #     actor=request.user,
        #     verb='unliked your post',
        #     target=post
        # )

        return Response({'detail': 'Post unliked successfully!'}, status=status.HTTP_200_OK)
