from django.http.request import validate_host
from django.utils.translation import deactivate_all
from rest_framework.response import Response
import requests
import os
from rest_framework import status
from apis.accounts.models import RememberAccount
from rest_framework.decorators import action
from rest_framework import viewsets
from apis.invite.models import Invite
from apis.invite.serializers import InviteSerializer
from .serializers import NotificationSerializer, NotificationBodySerializer
from apis.device.models import Device
from rest_framework.exceptions import PermissionDenied

authorization = os.getenv("NOTIFICATION_TOKEN")
key = os.getenv("FIREBASE_TOKEN")
key_complete = "key=" + key



class NotificationView(viewsets.ModelViewSet):

    def validateAuthorization(self, request):
        header = request.headers["Authorization"]
        print(header)
        print(authorization)
        if header != authorization: 
            raise PermissionDenied("Not authorized", "Permission Denied")

    def list(self, request, pk=None):
        invites = InviteSerializer(data=Invite.objects.filter(guest=self.request.user), many=True)
        invites.is_valid()
        body = {
            "memory_line_activities": [],
            "memories": [],
            "invites": invites.data
        }
        return Response(body, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='all')
    def notify_all_users(self, request, pk=None):
        self.validateAuthorization(request)

        serializer = NotificationBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        devices = Device.objects.all()
        devices_tokens = devices.values_list("firebase_token", flat=True)
        data = {
            "data": {
                "title": serializer._validated_data['title'],
                "body": serializer._validated_data['body'],
                "action_link": serializer._validated_data['link'],
                "category": serializer._validated_data['category'],
            },
            "registration_ids": list(devices_tokens)
        }

        notifications = []

        for device in devices:
            notificationData = {
                "title": serializer._validated_data['title'],
                "body": serializer._validated_data['body'],
                "receiver": device.owner,
                "link": serializer._validated_data['link'],
                "category": serializer._validated_data['category']
            }
            notifications.append(notificationData)
        
        notificationsSerializer = NotificationSerializer(data=notifications, many=True)
        notificationsSerializer.is_valid(raise_exception=True)
        notificationsSerializer.save()

        request = requests.post(
            'https://fcm.googleapis.com/fcm/send',
            headers={"Authorization": key_complete},
            json=data
        )

        return Response(request.json(), status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path='notify')
    def notify_users(self, request, pk=None):
        self.validateAuthorization(request)

        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        owner = RememberAccount.objects.get(email=self.request.user.email)

        devices = Device.objects.filter(owner=owner)        
        devices_tokens = devices.values_list("firebase_token", flat=True)

        data = {
            "data": {
                "title": serializer._validated_data['title'],
                "body": serializer._validated_data['body'],
                "action_link": serializer._validated_data['link'],
                "category": serializer._validated_data['category']
            },
            "registration_ids": list(devices_tokens)
        }
        serializer.save()
        request = requests.post(
            'https://fcm.googleapis.com/fcm/send',
            headers={"Authorization": key_complete},
            json=data
        )

        return Response(request.json(), status=status.HTTP_200_OK)