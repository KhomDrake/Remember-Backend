from rest_framework.permissions import BasePermission


class CreateMomentPerm(BasePermission):
    """
    The moment create permissions;.
    """
    def has_object_permission(self, request, view, obj):
        print("teste")
        return request.user.has_perm('view_memoryline', obj)

class RetrieveMomentPerm(BasePermission):
    """
    The memory line is public or retrieve permission.
    """
    def has_object_permission(self, request, view, obj):

        return request.user.has_perm('view_memoryline', obj.memory_line)

class UpdateMomentPerm(BasePermission):
    """
    The moment update permissions;.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('view_memoryline', obj.memory_line):
            return False
        return request.user.has_perm('change_moment', obj)

class DestroyMomentPerm(BasePermission):
    """
    The memory line delete permissions;.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('view_memoryline', obj.memory_line):
            return False
        return request.user.has_perm('delete_moment', obj)
