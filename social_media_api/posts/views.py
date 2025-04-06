from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
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
        try:
            like = Like.objects.get(user=request.user, post_id=pk)
            like.delete()
            return Response({'detail': 'Post unliked'})
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post'}, status=400)
