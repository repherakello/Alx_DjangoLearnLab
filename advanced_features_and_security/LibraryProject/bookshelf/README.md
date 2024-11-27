# Permissions and Groups Setup

## Custom Permissions
The `Article` model includes the following custom permissions:
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating articles.
- `can_edit`: Allows editing articles.
- `can_delete`: Allows deleting articles.

## Groups
- **Viewers**: Can view articles (`can_view`).
- **Editors**: Can view, create, and edit articles (`can_view`, `can_create`, `can_edit`).
- **Admins**: Full access to all actions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Views
Permissions are enforced using Django’s `@permission_required` decorator:
- `article_list`: Requires `can_view`.
- `article_create`: Requires `can_create`.
- `article_edit`: Requires `can_edit`.
- `article_delete`: Requires `can_delete`.

## Testing
Assign users to groups and test access to each view to verify that permissions are enforced correctly.
