from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Book

@login_required
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    permission_required = 'bookshelf.can_view_book'
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'is_available']
    permission_required = 'bookshelf.can_create_book'
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'is_available']
    permission_required = 'bookshelf.can_edit_book'
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'bookshelf.can_delete_book'
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')