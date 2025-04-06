from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Post

from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        users_list = [{"id": user.id, "username": user.username} for user in users]
        return Response({"users": users_list})

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
