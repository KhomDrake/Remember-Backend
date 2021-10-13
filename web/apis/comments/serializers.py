from rest_framework import serializers
from .models import Comment
from apis.accounts.models import RememberAccount


class CommentOwnerSerializer(serializers.ModelSerializer):
    """
    Serializer a Remember Account
    """

    class Meta:
        model = RememberAccount
        fields = ['id',
                  'photo',
                  'username',
                  'name',
                  'nickname'
                  ]


class CommentSerializer(serializers.ModelSerializer):
    owner = CommentOwnerSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'owner',
                  'moment',
                  'created_at',
                  'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Comment.create_moment(**validated_data)

    
