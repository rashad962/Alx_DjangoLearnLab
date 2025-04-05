from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, Permission
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title', 'author')

class CustomGroupAdmin(GroupAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['permissions'].queryset = Permission.objects.filter(
            content_type__app_label__in=['bookshelf', 'auth']
        )
        return form

# Unregister the default Group admin and register our custom one
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser)