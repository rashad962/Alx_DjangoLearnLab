from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class FeedPagination(PageNumberPagination):
    page_size = 10  # Adjust this to set how many posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostFeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        # Get posts from users the logged-in user is following
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
