# Django Permissions and Groups System

This document explains how permissions and groups are configured in the application.

## Permission Structure

### Book Model Permissions
- `can_view_book` - Allows viewing book details
- `can_create_book` - Allows creating new books
- `can_edit_book` - Allows editing existing books
- `can_delete_book` - Allows deleting books

### User Model Permissions
- `can_view_dashboard` - Allows access to the admin dashboard

## Predefined Groups

1. **Viewers**
   - Permissions: `can_view_book`, `can_view_dashboard`

2. **Editors**
   - Permissions: `can_view_book`, `can_create_book`, `can_edit_book`, `can_view_dashboard`

3. **Admins**
   - All permissions including delete capabilities

## How to Set Up Groups

1. Go to the Django admin panel (/admin/)
2. Navigate to "Groups" under "Authentication and Authorization"
3. Create groups and assign appropriate permissions

## View Protection

All views are protected with either:
- `@permission_required` decorator (function-based views)
- `PermissionRequiredMixin` (class-based views)

## Testing Permissions

1. Create test users and assign them to different groups
2. Log in as each user and verify:
   - Viewers can only view books
   - Editors can view, create, and edit books
   - Admins can perform all actions including deletion