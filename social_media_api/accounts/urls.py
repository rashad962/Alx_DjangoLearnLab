from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # "register/" ✅
    path('login/', LoginView.as_view(), name='login'),           # "login/" ✅
    path('profile/', ProfileView.as_view(), name='profile'),
]
