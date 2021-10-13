from rest_framework import serializers
from .models import RememberAccount
from drf_extra_fields.fields import Base64ImageField


class RememberAccountSerializer(serializers.ModelSerializer):
    """
    Serializer a Remember Account
    """
    photo = Base64ImageField(required=False)
    class Meta:

        model = RememberAccount
        fields = ['id',
                  'photo',
                  'username',
                  'password',
                  'name',
                  'nickname',
                  'email',
                  'phone_number',
                  'bio',
                  'gender', 
                  'birth_date',
                  'country',
                  'accept_terms'
                  ]

        extra_kwargs = {'id': {'read_only': True},
                        'password': {'write_only': True}}

    def create(self, validated_data):
        account = RememberAccount.create_account(**validated_data)
        return account


class RememberAccountDetailSerializer(serializers.ModelSerializer):
    """
    Serializer a Remember Account
    """
    class Meta:

        photo = Base64ImageField(required=False)

        model = RememberAccount
        fields = [
                  'photo',
                  'username',
                  'name',
                  'nickname',
                  'phone_number',
                  'bio',
                  'gender',
                  'birth_date',
                  'accept_terms']


class VerifyEmailSerializer(serializers.Serializer):

    email = serializers.EmailField()


class VerifyUsernameSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)


class PasswordRememberSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(max_length=128)

    class Meta:
        model = RememberAccount
        fields = ['old_password', 'password']


