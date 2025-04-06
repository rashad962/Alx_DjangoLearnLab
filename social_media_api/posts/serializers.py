from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

# RegisterSerializer: Handles user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Create a new user with the provided data
        user = get_user_model().objects.create_user(**validated_data)
        # Optionally, create a Token for the newly created user
        Token.objects.create(user=user)
        return user

# LoginSerializer: Handles login and token creation
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Check if the user exists
        user = get_user_model().objects.get(username=data['username'])
        # Check if the password is correct
        if not user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data

# UserSerializer: Serializer for displaying user information (e.g., in the profile view)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

# TokenSerializer: Retrieves the refresh and access tokens
class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
