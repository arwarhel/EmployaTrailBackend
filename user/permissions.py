from rest_framework import permissions


class IsAuthenticatedOrUserCreatedBy(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            # Check if the user is the authenticated user or created_by employee
            return request.user == obj.user or request.user == obj.user.employee.created_by
        return False
