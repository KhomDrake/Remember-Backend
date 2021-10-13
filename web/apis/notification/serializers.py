from rest_framework import serializers
from apis.accounts.models import RememberAccount
from .models import Notification

class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RememberAccount
        fiels = ['id']

class NotificationManySerializer(serializers.ModelSerializer):
    receivers = UserNotificationSerializer(many=True)

    class Meta:
        model = Notification
        fields = ['id', 'title', 'body', 'receivers', 'link', 'category']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'body', 'receiver', 'link', 'category']

class NotificationBodySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=200)
    link = serializers.CharField(max_length=300)
    category = serializers.CharField(max_length=50)

