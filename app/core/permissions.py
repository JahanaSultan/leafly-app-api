from rest_framework import permissions

class AdminOnlyPermission(permissions.BasePermission):
    """Allow access only to admin users"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
