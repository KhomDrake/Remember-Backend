from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .serializers import *
from .models import *
from apis.moments.models import Moment
from apis.moments.serializers import MomentsSerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from utils.permissions import IsRememberAccount
from .permissions import *
from apis.accounts.models import RememberAccount


class MemoryLineView(viewsets.ModelViewSet):

    queryset = MemoryLine.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_serializer_class(self):
        if self.action == 'invite':
            return MemoryLineInviteSerializer
        elif self.action == 'retrieve':
            return MemoryLineRetrieveSerializer
        elif self.action == 'participants':
            return MemoryLineParticipantsSerializer
        elif self.action == 'owner':
            return MemoryLineDetailSerializer
        elif self.action == 'moments':
            return MomentsSerializer
        return MemoryLineSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return MemoryLine.objects.none()
        if self.action == 'list':
            return MemoryLine.objects.filter(Q(owner=self.request.user) | Q(participants__in=[self.request.user])).order_by().order_by('-created_at')
        elif self.action == 'invite':
            return MemoryLine.objects.filter(owner=self.request.user).order_by('-created_at')
        return self.queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve' or self.action == 'participants' or self.action == 'moments':
            permission_classes = [IsAuthenticated & IsRememberAccount & RetrievePerm]
        elif self.action == 'destroy':
            permission_classes = (IsAuthenticated, IsRememberAccount, DestroyPerm)
        elif self.action == 'update':
            permission_classes = (IsAuthenticated, IsRememberAccount, UpdatePerm)
        elif self.action == 'invite':
            permission_classes = (IsAuthenticated, IsRememberAccount, InvitePerm)
        elif self.action == 'create_moments':
            permission_classes = (IsAuthenticated, IsRememberAccount, RetrievePerm)
        else:
            permission_classes = (IsAuthenticated, IsRememberAccount)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        owner = RememberAccount.objects.get(email=self.request.user.email)
        serializer.save(owner=owner)

    @action(detail=False, methods=['post'], url_path='(?P<pk>[0-9a-f-]+)/moments/create')
    def create_moments(self, request, pk=None):
        memory_line = self.get_object()
        serializer = MomentsSerializer(data={
            "memory_line": str(memory_line.id),
            "file": request.data["file"],
            "description": request.data["description"]
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=RememberAccount.objects.get(email=self.request.user.email))
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='(?P<pk>[0-9a-f-]+)/moments')
    def moments(self, request, pk=None):
        """
        List moments
        """
        memory_line = self.get_object()
        queryset = Moment.objects.filter(memory_line=memory_line).order_by('-pub_date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='types')
    def types(self, request, pk=None):
        """
        List types
        """
        queryset = MemoryLine.objects.filter(owner=request.user).values('type').distinct()
        return Response(queryset.values('type'), status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='(?P<pk>[0-9a-f-]+)/owner')
    def owner(self, request, pk=None):
        try:
            queryset = MemoryLine.objects.filter(id=pk).first()
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise ValidationError("Memory Line Invalid")

    @action(detail=False, methods=['get'], url_path='(?P<pk>[0-9a-f-]+)/participants')
    def participants(self, request, pk=None):
        """
        Get memory line participants
        """
        try:
            memory_line = self.get_object()
            queryset = MemoryLineParticipants.objects.filter(memory_line=memory_line)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise ValidationError("Memory Line Invalid")
        