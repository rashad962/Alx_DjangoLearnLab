from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import Post, Like
from accounts.models import CustomUser
from .serializers import PostSerializer
from notifications.models import Notification
from rest_framework import generics
post = generics.get_object_or_404(Post, pk=pk)
# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Get the post object
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"message": "You have already liked this post."}, status=400)

        # Create notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Post liked!"}, status=201)

# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Get the post object
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()  # Delete the like
            return Response({"message": "Post unliked!"}, status=200)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post yet."}, status=400)

# Feed view (posts from users the current user follows)
class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Users this user is following
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

