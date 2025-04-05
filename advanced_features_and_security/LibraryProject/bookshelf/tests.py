from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from .models import Book

class PermissionTests(TestCase):
    def setUp(self):
        # Create groups
        self.viewer_group = Group.objects.create(name='Viewers')
        self.editor_group = Group.objects.create(name='Editors')
        self.admin_group = Group.objects.create(name='Admins')

        # Assign permissions to groups
        view_perm = Permission.objects.get(codename='can_view_book')
        create_perm = Permission.objects.get(codename='can_create_book')
        edit_perm = Permission.objects.get(codename='can_edit_book')
        delete_perm = Permission.objects.get(codename='can_delete_book')

        self.viewer_group.permissions.add(view_perm)
        self.editor_group.permissions.add(view_perm, create_perm, edit_perm)
        self.admin_group.permissions.add(view_perm, create_perm, edit_perm, delete_perm)

        # Create test users
        self.viewer = User.objects.create_user(username='viewer', password='testpass123')
        self.editor = User.objects.create_user(username='editor', password='testpass123')
        self.admin = User.objects.create_user(username='admin', password='testpass123')

        # Assign users to groups
        self.viewer.groups.add(self.viewer_group)
        self.editor.groups.add(self.editor_group)
        self.admin.groups.add(self.admin_group)

        # Create a test book
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-01-01',
            is_available=True
        )

    def test_viewer_permissions(self):
        client = Client()
        client.login(username='viewer', password='testpass123')
        
        # Viewer should be able to view
        response = client.get(reverse('book-detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)
        
        # Viewer should NOT be able to edit
        response = client.get(reverse('book-edit', args=[self.book.pk]))
        self.assertEqual(response.status_code, 403)

    def test_editor_permissions(self):
        client = Client()
        client.login(username='editor', password='testpass123')
        
        # Editor should be able to edit
        response = client.get(reverse('book-edit', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)
        
        # Editor should NOT be able to delete
        response = client.get(reverse('book-delete', args=[self.book.pk]))
        self.assertEqual(response.status_code, 403)

    def test_admin_permissions(self):
        client = Client()
        client.login(username='admin', password='testpass123')
        
        # Admin should be able to delete
        response = client.get(reverse('book-delete', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)