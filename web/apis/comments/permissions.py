from rest_framework.permissions import BasePermission

class DestroyCommentPerm(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('view_memoryline', obj.moment.memory_line):
            return False
        return request.user.has_perm('delete_comment', obj)

class CreateCommentPerm(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('view_memoryline', obj.memory_line)

class UpdateCommentPerm(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('view_memoryline', obj.moment.memory_line):
            return False
        return request.user.has_perm('change_comment', obj)