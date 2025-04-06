from django import forms
from .models import Post
from taggit.forms import TagField  # Import TagField for tags

class PostForm(forms.ModelForm):
    tags = TagField()  # Tag field for Post creation and updates

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
