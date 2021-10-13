from rest_framework import serializers
from .models import Invite
from apis.accounts.models import RememberAccount
from apis.accounts.serializers import RememberAccountSerializer
from .models import MemoryLine
from rest_framework.exceptions import ValidationError


class InviteOwnerSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = RememberAccount
        fields = ['id', 
                'photo',
                'nickname', 
                'name', 
                'username', 
                'email']


class InviteMemoryLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryLine
        fields = ['id', 'title', 'description']



class InviteSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField('get_owner')
    memory_line = InviteMemoryLineSerializer(read_only=True)

    class Meta:
        model = Invite
        read_only_fields = ['answered', 'accepted']
        fields = ['id', 'answered', 'accepted', 'memory_line', 'owner', 'guest']

    def get_owner(self, obj):
        queryset = RememberAccount.objects.get(email=obj.owner.email)
        return RememberAccountSerializer(queryset).data



class InviteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invite
        fields = ['id', 'memory_line', 'guest']

    def create(self, validated_data):
        invite = Invite.objects.filter(answered=False, guest=validated_data.get("guest"), memory_line=validated_data.get("memory_line"))
        inviteAnswered = Invite.objects.filter(answered=True, guest=validated_data.get("guest"), memory_line=validated_data.get("memory_line"))

        if inviteAnswered != None and inviteAnswered.count() > 0 and inviteAnswered[0].accepted == True:
            raise ValidationError("Failed To Create Invite")

        if invite != None and invite.count() > 0:
            raise ValidationError("Has Invite Pending")

        return Invite.objects.create(**validated_data)


class InviteAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['accepted']

    def update(self, invite, validated_data):
        invite.accepted = validated_data.get("accepted")
        invite.answered = True
        invite.save()
        return invite


