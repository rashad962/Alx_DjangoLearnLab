from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission to ensure users can only edit their own posts/comments

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated users and owners can modify posts
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Allow searching by title and content

    def perform_create(self, serializer):
        # Ensure the post is created by the logged-in user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated users and owners can modify comments
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']  # Allow searching by comment content

    def perform_create(self, serializer):
        # Ensure the comment is created by the logged-in user
        serializer.save(author=self.request.user)
