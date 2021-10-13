from rest_framework.permissions import BasePermission


class DestroyPerm(BasePermission):
    """
    The memory line delete permissions;.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('delete_memoryline', obj)

class UpdatePerm(BasePermission):
    """
    The memory line update permissions;.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('change_memoryline', obj)

class InvitePerm(BasePermission):
    """
    The memory line update permissions;.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('view_memoryline', obj)

class RetrievePerm(BasePermission):
    """
    The memory line is public or retrieve permission.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('view_memoryline', obj):
            return True
        return False
