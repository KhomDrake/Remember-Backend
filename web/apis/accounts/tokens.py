from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


class CustomJWTSerializer(TokenObtainPairSerializer):
    """
    Authentication for username or email
    """

    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        user_obj = User.objects.filter(
            email=attrs.get("username")).first() or User.objects.filter(
            username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)


account_activation_token = AccountActivationTokenGenerator()
