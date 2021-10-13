from rest_framework.decorators import action
from rest_framework import viewsets, status
from utils.permissions import IsRememberAccount
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from apis.accounts.models import RememberAccount

class DeviceView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsRememberAccount)

    @action(detail=False, methods=['post'], url_path='add')
    def add_device(self, request, pk=None):
        serializer = DeviceSerializer(data=request.data)
        device = Device.objects.filter(device_id=request.data['device_id']).first()
        owner = RememberAccount.objects.get(email=self.request.user.email)

        if(device == None):        
            serializer.initial_data['owner'] = owner
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            device.owner = owner
            device.name = request.data["name"]
            device.firebase_token = request.data["firebase_token"]
            device.save()
        return Response(status=status.HTTP_200_OK)