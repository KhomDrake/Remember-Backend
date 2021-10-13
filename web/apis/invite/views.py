from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Invite

from utils.permissions import IsRememberAccount
from .permissions import *
from apis.accounts.models import RememberAccount
from utils.pagination import StandardResultsSetPagination


class InviteView(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'accept':
            return InviteAcceptSerializer
        if self.action == 'create':
            return InviteCreateSerializer
        return InviteSerializer

    def get_queryset(self):
        return Invite.objects.filter(guest=self.request.user,answered=False)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsRememberAccount, CreateInvitePerm]
        else:
            permission_classes = (IsAuthenticated, IsRememberAccount)
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['post'], url_path='many')
    def addManyInvites(self, request, pk=None):
        invites = InviteCreateSerializer(data=request.data, many=True)
        invites.is_valid(raise_exception=True)
        owner = RememberAccount.objects.get(email=self.request.user.email)
        invites.save(owner=owner)
        return Response(invites.data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        """
        Accept invite
        """
        invite = self.get_object()
        serializer = self.get_serializer(invite, request.data)
        serializer.is_valid(raise_exception=True)

        if(invite.answered):
            error = {
                "error_type": "INVALID_INVITE",
                "error_message": "Invite Already responded"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        invite = serializer.save()
        if(invite.accepted):
            remember_account = RememberAccount.objects.get(email=request.user.email)
            invite.memory_line.type.add_type_owner(remember_account)
            invite.memory_line.add_participant(participant=remember_account)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def perform_create(self, serializer):
        owner = RememberAccount.objects.get(email=self.request.user.email)
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=owner)


