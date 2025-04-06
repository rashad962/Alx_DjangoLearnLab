from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # For the browsable API
    path('api-token-auth/', auth_views.obtain_auth_token),  # Token authentication
    path('api/', include('posts.urls')),  # Add 'api/' prefix for posts URLs
]
