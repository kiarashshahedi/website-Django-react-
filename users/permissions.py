from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    """
    Allows access only to users with a seller role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'seller'
