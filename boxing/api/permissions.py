from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Authenticated users can make safe requests (GET, HEAD, OPTIONS)
    but unsafe requests (POST, DELETE, PUT, PATCH) are only for admin users
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated()
        else:
            return request.user and request.user.is_staff
