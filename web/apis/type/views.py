from rest_framework.decorators import action
from rest_framework import status, viewsets
from utils.permissions import IsRememberAccount
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TypeOwner
from apis.accounts.models import RememberAccount
from .serializers import MemoryLineTypeOwnerSerializer, PrioritySerializer, MemoryLineCreateTypeSerializer, MemoryLineTypeChangePrioritySerializer

class TypeMemoryLineView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsRememberAccount)
    
    def get_queryset(self):
        return TypeOwner.objects.filter(owner=self.request.user).order_by('priority')
        
    def get_serializer_class(self):
        if(self.action == 'list'):
            return MemoryLineTypeOwnerSerializer
        elif(self.action == 'priority'):
            return PrioritySerializer
        return MemoryLineCreateTypeSerializer

    def perform_create(self, serializer):
        owner = RememberAccount.objects.get(email=self.request.user.email)
        serializer.save(owner=owner)

    @action(detail=False, methods=['put'], url_path='many')
    def change_priorities(self, request, pk=None):
        serializer = MemoryLineTypeChangePrioritySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        owner = RememberAccount.objects.get(email=self.request.user.email)
        for type in serializer._validated_data:
            instance = TypeOwner.objects.get(type=type.get("type"), owner=owner)
            instance.priority = type.get("priority")
            instance.save()
        return Response(None, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='(?P<pk>[0-9a-f-]+)/priority')
    def priority(self, request, pk=None):
        """
        Change Priority
        """
        type = self.get_object()
        serializer = self.get_serializer(type, request.data)
        serializer.is_valid(raise_exception=True)
        type = serializer.save()
        return Response(MemoryLineTypeOwnerSerializer(type).data, status=status.HTTP_200_OK)
