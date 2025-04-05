from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import UserProfile, Book

@receiver(post_save, sender=UserProfile)
def assign_permissions(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(Book)
    book_perms = Permission.objects.filter(content_type=content_type)
    
    if instance.role == 'ADMIN':
        # Admins get all permissions
        instance.user.user_permissions.set(book_perms)
    elif instance.role == 'LIBRARIAN':
        # Librarians can add and change books
        add_perm = book_perms.get(codename='can_add_book')
        change_perm = book_perms.get(codename='can_change_book')
        instance.user.user_permissions.add(add_perm, change_perm)
    elif instance.role == 'MEMBER':
        # Members can only view
        instance.user.user_permissions.clear()
