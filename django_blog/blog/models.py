from django.db import models
from django.conf import settings
from .models import Post  # Assuming the Post model is in the same app

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to User model
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the comment was last updated

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'  # String representation of the comment

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})  # Redirect to the post's detail page
