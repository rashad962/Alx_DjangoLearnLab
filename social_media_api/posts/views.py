from rest_framework.permissions import IsAuthenticated  # Import for authentication permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404  # Import for retrieving objects or returning 404
from .models import Post, Like  # Import your Post and Like models
from .serializers import PostSerializer  # If you have a serializer for the Post model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]


post = generics.get_object_or_404(Post, pk=pk)

# View to handle liking a post
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request, pk):
        # Retrieve the post or return a 404 if the post doesn't exist
        post = get_object_or_404(Post, pk=pk)

        # Create or get the Like instance (prevents multiple likes from the same user)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Post liked successfully!'}, status=status.HTTP_200_OK)

# View to handle unliking a post
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request, pk):
        # Retrieve the post or return a 404 if the post doesn't exist
        post = get_object_or_404(Post, pk=pk)

        # Find the like instance, if any, to remove
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        return Response({'detail': 'Post unliked successfully!'}, status=status.HTTP_200_OK)
