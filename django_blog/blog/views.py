from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment, Post

# View for creating a comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Automatically link comment to post and current user
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail page after creating the comment
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})

# View for updating a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        # Redirect to the post detail page after editing the comment
        return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.id})

# View for deleting a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        # Redirect to the post detail page after deleting the comment
        return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.id})
