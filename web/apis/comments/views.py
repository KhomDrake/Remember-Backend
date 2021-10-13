from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from apis.accounts.models import RememberAccount
from .serializers import CommentSerializer
from .models import *
from .permissions import DestroyCommentPerm, UpdateCommentPerm, CreateCommentPerm
from utils.pagination import StandardResultsSetPagination
from rest_framework.parsers import JSONParser
from utils.permissions import IsRememberAccount

# Create your views here.


class CommentView(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pagination_class = StandardResultsSetPagination
    parser_classes = (JSONParser,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsRememberAccount, CreateCommentPerm]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsRememberAccount, UpdateCommentPerm]
        else:
            permission_classes = [IsAuthenticated, IsRememberAccount, DestroyCommentPerm]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        owner = RememberAccount.objects.get(email=self.request.user.email)
        serializer.save(owner=owner)

