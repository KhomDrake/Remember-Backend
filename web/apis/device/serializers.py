from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['id', 'device_id', 'firebase_token', 'name', 'os_version', 'owner', 'created_at', 'updated_at']