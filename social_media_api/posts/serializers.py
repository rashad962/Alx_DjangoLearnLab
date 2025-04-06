from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Display username of the author

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Display username of the author
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Link to post

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
