from rest_framework import permissions

class BasePermission(object):
    """
    A base class from which all the classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return 'true' if permission is granted otherwise 'false'
        """
        return True
class IsStudentOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Readonly are allowed for any requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the student with the specific details
        return obj.regNo == request.user