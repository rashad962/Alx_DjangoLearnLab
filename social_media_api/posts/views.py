from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the users the current user is following
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
