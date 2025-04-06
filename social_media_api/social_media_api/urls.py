from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the posts URLs for the like and unlike functionality
    path('api/posts/', include('posts.urls')),  # This ensures that posts URLs are included
    
    # Include other app URLs
    path('api/accounts/', include('accounts.urls')),
    path('api/notifications/', include('notifications.urls')),
]
