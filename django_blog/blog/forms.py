from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the content field is needed for creating/updating comments

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally add custom validation or styling for the form here
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your comment here...', 'rows': 4, 'cols': 40})
        
    # Example of custom validation for content (optional)
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("Comment content must be at least 10 characters long.")
        return content
