from rest_framework import serializers
from .models import Type, TypeOwner

class MemoryLineCreateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

    def create(self, validated_data):
        type = Type.create_type(**validated_data)
        return type

class MemoryLineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class MemoryLineTypeOwnerSerializer(serializers.ModelSerializer):
    type = MemoryLineTypeSerializer(read_only=True)

    class Meta:
        model = TypeOwner
        fields = ['id', 'type', 'priority']

class MemoryLineTypeChangePrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOwner
        fields = ['id', 'priority', 'type']

class PrioritySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeOwner
        fields = ['priority']
