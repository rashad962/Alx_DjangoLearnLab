from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from notifications.models import Notification  # Adjust if it's in a different location
Notification.objects.create(
    recipient=post.author,
    actor=request.user,
    verb='liked',
    target=post
)

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.order_by('-timestamp')
