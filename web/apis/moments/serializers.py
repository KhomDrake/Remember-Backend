from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from drf_extra_fields.fields import Base64ImageField
from apis.accounts.models import RememberAccount
from apis.comments.models import Comment

from .models import Moment


class MomentOwnerSerializer(serializers.ModelSerializer):
    """
    Serializer a Remember Account
    """
    class Meta:

        model = RememberAccount
        fields = ['id',
                  'photo',
                  ]


class MomentsSerializer(serializers.ModelSerializer):
    file = Base64ImageField(required=True)
    owner = MomentOwnerSerializer(read_only=True)
    comments_count = SerializerMethodField('get_comments_count')

    class Meta:
        model = Moment
        fields = ['id',
                  'file',
                  'description',
                  'owner',
                  'comments_count',
                  'memory_line',
                  'pub_date',
                  'updated_at']
        read_only_fields = ['id', 'owner', 'pub_date', 'updated_at']

    def create(self, validated_data):
        moment = Moment.create_moment(**validated_data)
        return moment
    
    def get_comments_count(self, obj):
        comments_count = Comment.objects.filter(moment=obj)\
                                         .count()
        return comments_count


class MomentsDetailSerializer(serializers.ModelSerializer):
    file = Base64ImageField(required=True)

    class Meta:
        model = Moment
        fields = [
                  'file',
                  'description'
                  ]

