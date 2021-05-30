from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from users.models import Patient

class IsOwner(permissions.BasePermission):
    """
    Check if user is owner or not.
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.owners
