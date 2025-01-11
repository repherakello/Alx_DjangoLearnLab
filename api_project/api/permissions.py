from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permission for safe methods
        if request.method in ('GET','HEAD', 'OPTIONS'):
            return True
        
        # Write permissions only for the owner
        return obj.owner == request.user