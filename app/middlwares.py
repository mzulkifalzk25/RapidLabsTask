from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.status == 'completed' and request.user.userprofile.role != 'Manager':
            raise PermissionDenied("Only Managers can mark tasks as completed.")
        
        return True
