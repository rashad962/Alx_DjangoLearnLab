from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostFeedViewSet

router = DefaultRouter()
router.register(r'feed', PostFeedViewSet, basename='post-feed')

urlpatterns = [
    path('', include(router.urls)),
]
