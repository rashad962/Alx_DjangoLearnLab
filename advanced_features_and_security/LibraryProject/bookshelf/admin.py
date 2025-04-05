from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
