from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_super_user
