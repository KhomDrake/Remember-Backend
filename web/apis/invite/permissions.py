from rest_framework.permissions import BasePermission


class CreateInvitePerm(BasePermission):
    """
    The invite  create permissions;.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('view_memoryline', obj)


class RetrieveInvitePerm(BasePermission):
    """
    The invite update permissions;.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('view_invite', obj)
