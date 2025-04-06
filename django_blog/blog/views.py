from django.shortcuts import render
from django.db.models import Q  # For complex queries
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# Post views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Search view
def search(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |  # Search for title containing the query
            Q(content__icontains=query) |  # Search for content containing the query
            Q(tags__name__icontains=query)  # Search for tags containing the query
        ).distinct()  # Use distinct to avoid duplicate posts
    else:
        posts = Post.objects.all()  # If no search query, return all posts

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
