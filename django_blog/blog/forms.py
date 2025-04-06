from django import forms
from .models import Post
from taggit.forms import TagField, TagWidget  # Import TagWidget and TagField

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget())  # Apply the TagWidget to the tags field

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
