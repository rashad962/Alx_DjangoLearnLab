from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Book, Author, UserProfile

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'isbn')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name', 'isbn')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role')
    
    def get_role(self, obj):
        return obj.userprofile.get_role_display()
    get_role.short_description = 'Role'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
