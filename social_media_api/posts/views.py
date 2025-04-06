from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the post using get_object_or_404
        post = get_object_or_404(Post, pk=pk)
        
        # Create a like or return a message if the user already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification when a post is liked
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'detail': 'Post liked'}, status=201)
        return Response({'detail': 'Already liked'}, status=400)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the like using get_object_or_404 to ensure the like exists
        like = get_object_or_404(Like, user=request.user, post_id=pk)
        like.delete()
        return Response({'detail': 'Post unliked'})
