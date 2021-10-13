from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreateOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method == 'POST'
        )


class IsRememberAccount(BasePermission):
    """
    The request is authenticated with a RememberAccount
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_remember_account)


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsRememberAccoutAowner(BasePermission):
    """
    The request is authenticated with a RememberAccount
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_remember_account)
