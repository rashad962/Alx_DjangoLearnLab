from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

# List view for comments (optional, usually displayed within a post's detail view)
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return Comment.objects.filter(post=post)

# Create view for comments
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})

# Update view for comments
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        # Ensure users can only update their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})

# Delete view for comments
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        # Ensure users can only delete their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})
