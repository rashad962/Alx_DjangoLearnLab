from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from .serializers import PostSerializer

# View to handle liking a post
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, pk):
        # Retrieve the post or raise a 404 error if not found
        post = get_object_or_404(Post, pk=pk)

        # Create a Like instance if it doesn't exist
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Optionally create a notification here for the post author
        # Notification.objects.create(
        #     recipient=post.author,
        #     actor=request.user,
        #     verb='liked your post',
        #     target=post
        # )

        return Response({'detail': 'Post liked successfully!'}, status=status.HTTP_200_OK)

# View to handle unliking a post
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, pk):
        # Retrieve the post or raise a 404 error if not found
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        # Optionally create a notification for the post author that the post was unliked
        # Notification.objects.create(
        #     recipient=post.author,
        #     actor=request.user,
        #     verb='unliked your post',
        #     target=post
        # )

        return Response({'detail': 'Post unliked successfully!'}, status=status.HTTP_200_OK)
