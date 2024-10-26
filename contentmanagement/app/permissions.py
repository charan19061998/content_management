from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access to authors or admins for actions other than list and retrieve
        return request.user.role == 'admin' or request.user.role == 'author'
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.role == 'admin'
