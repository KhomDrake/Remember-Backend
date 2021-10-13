from apis.type.models import TypeOwner
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from apis.moments.models import Moment
from .models import MemoryLine, MemoryLineParticipants
from apis.accounts.models import RememberAccount
from apis.invite.models import Invite
from apis.moments.models import Moment
from rest_framework.exceptions import PermissionDenied


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RememberAccount
        fields = ['id', 'photo', 'nickname', 'name', 'username']


class MemoryLineMomentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moment
        fields = ['id', 'file']


class MemoryLineParticipantsSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(read_only=True)

    class Meta:
        model = MemoryLineParticipants
        fields = ['id', 'participant', 'created_at', 'updated_at']


class MemoryLineOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = RememberAccount
        fields = ['id', 'nickname', 'username', 'name', 'photo']


class MemoryLineRetrieveSerializer(serializers.ModelSerializer):
    some_participants = SerializerMethodField('get_some_participants')
    owner = MemoryLineOwnerSerializer(read_only=True)

    class Meta:
        model = MemoryLine
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'type', 'owner', 'some_participants']

    def get_some_participants(self, obj):
        queryset = MemoryLineParticipants.objects.filter(memory_line=obj)\
                                         .order_by('created_at')[:5]
        return MemoryLineParticipantsSerializer(queryset, many=True).data

class MemoryLineDetailSerializer(serializers.ModelSerializer):
    owner = MemoryLineOwnerSerializer(read_only=True)
    class Meta:
        model = MemoryLine
        extra_kwargs = {'id': {'read_only': True}}
        fields = ['id', 'owner']

class MemoryLineSerializer(serializers.ModelSerializer):
    some_participants = SerializerMethodField('get_some_participants')
    some_moments = SerializerMethodField('get_some_moments')
    owner = MemoryLineOwnerSerializer(read_only=True)

    class Meta:
        model = MemoryLine
        extra_kwargs = {'id': {'read_only': True}, 'updated_at': {'read_only': True}}
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'type', 'owner','some_moments', 'some_participants']

    def get_some_moments(self, obj):
        queryset = Moment.objects.filter(memory_line=obj)\
                                         .order_by('-pub_date')[:2]
        return MemoryLineMomentsSerializer(queryset, many=True).data

    def get_some_participants(self, obj):
        queryset = MemoryLineParticipants.objects.filter(memory_line=obj)\
                                         .order_by('created_at')[:2]
        return MemoryLineParticipantsSerializer(queryset, many=True).data

    def create(self, validated_data):
        owner = validated_data["owner"]
        query = TypeOwner.objects.filter(type=validated_data["type"], owner=owner).first()
        if query == None:
            raise PermissionDenied(detail="Don't have permission to see memory line type", code="Cannot create")
        memory_line = MemoryLine.create_memory_line(**validated_data)
        return memory_line


class MemoryLineInviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invite
        fields = ['guest']

    def create(self, validated_data):
        invite = Invite.create_invite(**validated_data)
        return invite




