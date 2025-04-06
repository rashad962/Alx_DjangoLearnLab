from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class FollowUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"detail": "User followed successfully."}, status=status.HTTP_200_OK)

class UnfollowUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "User unfollowed successfully."}, status=status.HTTP_200_OK)
