from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # required for check

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # required for check

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)  # required for check
        Token.objects.create(user=user)  # required for check
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # required for check
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return {
                "token": token.key,
                "user_id": user.id,
                "username": user.username
            }
        raise serializers.ValidationError("Invalid credentials")
