from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.permissions import IsRememberAccount
from .permissions import *
from apis.accounts.models import RememberAccount
from apis.comments.models import Comment
from apis.comments.serializers import CommentSerializer
from rest_framework import status

class MomentsView(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    parser_classes = (JSONParser,)

    def get_serializer_class(self):
        if self.action == 'update':
            return MomentsDetailSerializer
        if self.action == 'comments':
            return CommentSerializer
        return MomentsSerializer

    def get_queryset(self):
        if self.action == "list":
            return Moment.objects.filter(owner=self.request.user)
        return Moment.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsRememberAccount, CreateMomentPerm]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsRememberAccount, UpdateMomentPerm]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsRememberAccount, DestroyMomentPerm]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsRememberAccount, RetrieveMomentPerm]
        elif self.action == 'comments' or self.action == 'create_comments':
            permission_classes = [IsAuthenticated, IsRememberAccount, RetrieveMomentPerm]
        else:
            permission_classes = [IsAuthenticated, IsRememberAccount]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        owner = RememberAccount.objects.get(email=self.request.user.email)
        serializer.save(owner=owner)

    @action(detail=False, methods=['post'], url_path='(?P<pk>[0-9a-f-]+)/comments/create')
    def create_comments(self, request, pk=None):
        moment = self.get_object()
        serializer = CommentSerializer(data={
            "moment": str(moment.id),
            "content": request.data["content"]
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=RememberAccount.objects.get(email=self.request.user.email))
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        """
        List moments
        """
        moment = self.get_object()
        queryset = Comment.objects.filter(moment=moment).order_by('-created_at')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
